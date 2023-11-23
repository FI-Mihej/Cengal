#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""


__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import os
import sys
import traceback
import select
import time
# from fileinput import input
from typing import Set, Iterable, Optional, Tuple, Dict
import copy
from collections import deque

from cengal.data_generation.id_generator import IDGenerator, GeneratorType
from .base import *

from cengal.data_containers.dynamic_list_of_pieces import DynamicListOfPiecesDequeWithLengthControl
from cengal.data_containers.fast_fifo import FIFODequeWithLengthControl, FIFOIsEmpty
from cengal.data_manipulation.front_triggerable_variable import FrontTriggerableVariable, FrontTriggerableVariableType
from cengal.code_flow_control.smart_values.versions.v_0 import ResultExistence
from contextlib import contextmanager
from cengal.code_inspection.line_profiling import set_profiler
from .recv_buff_size_computer import RecvBuffSizeComputer
from math import ceil

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/

CAUTION: some code here is optimized for speed - not for readability or beauty.
"""

__author__ = 'ButenkoMS <gtalk@butenkoms.space>'

# set_profiler(True)
set_profiler(False)


class IoIterationResult:
    """
    ([1] подключившиеся ожидаемые клиенты (ОКл); [2] ОКл сокет которых был отключен по причине ошибки
    (сами ОКл еще небыли удалены - удаление нужно инициировать явно); [3] ОКл имеет очередь непрочитанных принятых
    сообщений; [4] размер очереди неотправленных сообщений ОКл меньше порогового, а значит в нее можно записывать
    новые запросы (не уверен пока в надобности этого параметра. Скорее всего он не нужен: актор в большинстве
    случаев блокируется при вызове IO-операции; кроме случаев когда был задействован ассинхронный интерфейс,
    при котором актор отправляет запрос не требуя ответа об успешном окончании операции (без какого-либо контроля
    успешности, или же с ручным контролем путем вызова спец-метода, который-бы и проводил проверку, или же
    считывание имеющихся результатов операций)))
    """

    def __init__(self):
        self.newly_connected_expected_clients = set()
        self.newly_connected_unknown_clients = set()
        self.clients_with_disconnected_connection = set()
        self.clients_have_data_to_read = set()
        self.clients_with_empty_output_fifo = set()

    def update(self, other):
        self.newly_connected_expected_clients.update(other.newly_connected_expected_clients)
        self.newly_connected_unknown_clients.update(other.newly_connected_unknown_clients)
        self.clients_with_disconnected_connection.update(
            other.clients_with_disconnected_connection)
        self.clients_have_data_to_read.update(other.clients_have_data_to_read)
        self.clients_with_empty_output_fifo.update(other.clients_with_empty_output_fifo)

    def remove(self, item):
        if item in self.newly_connected_expected_clients:
            self.newly_connected_expected_clients.remove(item)
        if item in self.newly_connected_unknown_clients:
            self.newly_connected_unknown_clients.remove(item)
        if item in self.clients_with_disconnected_connection:
            self.clients_with_disconnected_connection.remove(item)
        if item in self.clients_have_data_to_read:
            self.clients_have_data_to_read.remove(item)
        if item in self.clients_with_empty_output_fifo:
            self.clients_with_empty_output_fifo.remove(item)

    def clear(self):
        self.newly_connected_expected_clients.clear()
        self.newly_connected_unknown_clients.clear()
        self.clients_with_disconnected_connection.clear()
        self.clients_have_data_to_read.clear()
        self.clients_with_empty_output_fifo.clear()


class ASockIOCoreMemoryManagement(IOCoreMemoryManagement):
    def __init__(self):
        super(ASockIOCoreMemoryManagement, self).__init__()

        self.socket_read_fixed_buffer_size = ResultExistence(True,
                                                             1024 ** 2)  # 1024**2 is the fastest fixed read buffer.

    def link_to(self, parent):
        super(ASockIOCoreMemoryManagement, self).link_to(parent)
        try:
            self.socket_read_fixed_buffer_size = parent.socket_read_fixed_buffer_size
        except AttributeError:
            pass


class Connection:
    def __init__(self,
                 connection_id=None,
                 connection__conn_addr: tuple = None,
                 global_memory_management: ASockIOCoreMemoryManagement = None
                 ):
        """
        
        :param connection_id: ID for this connection
        :param connection__conn_addr: tuple(conn, addr) where conn is a socket, addr is an address
        :param global_memory_management: global memory management obj
        """
        self.id = connection_id
        if connection__conn_addr is None:
            self.conn = ResultExistence(False, None)
            self.addr = ResultExistence(False, None)
        else:
            self.conn = ResultExistence(True, connection__conn_addr[0])
            self.addr = ResultExistence(True, connection__conn_addr[1])

        self.addr_info = None
        self.host_names = None

        self.recv_buff_size_computer = RecvBuffSizeComputer()
        self.recv_buff_size = 0
        self.calc_new_recv_buff_size(0)

        self.should_be_closed = False  # socket should be closed immediately. For example because of IO error.
        self.ready_to_be_closed = False  # socket should be closed, after all messages had been sent to client.
        self.ready_for_deletion = False  # connection should be deleted immediately. For example because of unexpected
        #   keyword.

        self.keyword = None

        self.raw_input_from_client = DynamicListOfPiecesDequeWithLengthControl(
            external_data_length=global_memory_management.global_in__data_full_size)
        self.current_message_length = None  # length of current input message (or None, if size waw not read yet)
        self.input_from_client = FIFODequeWithLengthControl(
            external_data_full_size=global_memory_management.global_in__data_full_size)
        self.current_memoryview_output = None
        self.current_memoryview_input = None
        self.output_to_client = FIFODequeWithLengthControl(
            external_data_full_size=global_memory_management.global_out__data_full_size)

        self.this_is_raw_connection = False

        self.connected_expected_client_id = None
        self.connected_expected_client = None
        self.has_inline_processor = False

    def calc_new_recv_buff_size(self, last_recv_amount):
        self.recv_buff_size = self.recv_buff_size_computer.calc_new_recv_buff_size(last_recv_amount)

    def remove(self):
        self.raw_input_from_client.remove()
        self.input_from_client.remove()
        self.output_to_client.remove()


class InlineProcessor:
    __slots__ = ('client_id', 'keyword', 'socket_family', 'socket_type', 'socket_proto', 'addr_info', 'host_names',
                 'is_in_raw_mode', '__set__is_in_raw_mode', '__set__mark_socket_as_should_be_closed_immediately',
                 '__set__mark_socket_as_ready_to_be_closed', '__external_parameters_set_trigger', 'output_messages',
                 '__hold__client_id')

    def __init__(self, client_id=None, keyword: bytes = None, socket_family=None, socket_type=None, socket_proto=None,
                 addr_info=None, host_names=None, external_parameters_set_trigger: Set = None):
        """

        :param keyword: client keyword. You may check for a known keywords to act appropriately
        :param socket_family:
        :param socket_type:
        :param socket_proto:
        :param addr_info: result of socket.getaddrinfo() call
        :param host_names: result of socket.gethostbyaddr() call
        """
        self.client_id = client_id
        self.keyword = keyword
        self.socket_family = socket_family
        self.socket_type = socket_type
        self.socket_proto = socket_proto
        self.addr_info = addr_info
        self.host_names = host_names
        self.is_in_raw_mode = None
        self.__hold__client_id = client_id
        self.__set__is_in_raw_mode = False
        self.__set__mark_socket_as_should_be_closed_immediately = False
        self.__set__mark_socket_as_ready_to_be_closed = False
        self.__external_parameters_set_trigger = external_parameters_set_trigger

        # self.output_messages = FIFODequeWithLengthControl()
        self.output_messages = deque()
        # self.output_messages = list()

    def on__data_received(self, data: bytes):
        """
        Use self.output_messages (self.output_messages.append(out_message)) to store output messages or raw output data
        Any unhandled exception will lead to force destroying of current Inline Processor object. Also situation will 
        be logged
        :param data: piece of input data if connection is in RAW-mode and full message otherwise.
        """
        pass

    def on__output_buffers_are_empty(self):
        """
        Will be called immediately when all output data was send.
        Use self.output_messages (self.output_messages.append(out_message)) to store output messages or raw output data
        Any unhandled exception will lead to force destroying of current Inline Processor object. Also situation will 
        be logged
        """
        pass

    def on__connection_lost(self):
        """
        Will be called after connection was closed. Current Inline Processor object will be destroyed after this call.
        Situation with unhandled exception will be logged.
        """
        pass

    def set__is_in_raw_mode(self, is_in_raw_mode: bool):
        self.__set__is_in_raw_mode = is_in_raw_mode
        self.__external_parameters_set_trigger.add(self.__hold__client_id)

    def mark__socket_as_should_be_closed_immediately(self, mark_socket_as: bool):
        self.__set__mark_socket_as_should_be_closed_immediately = mark_socket_as
        self.__external_parameters_set_trigger.add(self.__hold__client_id)

    def mark__socket_as_ready_to_be_closed(self, mark_socket_as: bool):
        self.__set__mark_socket_as_ready_to_be_closed = mark_socket_as
        self.__external_parameters_set_trigger.add(self.__hold__client_id)


class Client:
    def __init__(self, connection_settings: ConnectionSettings, client_id=None, client_tcp_id=None):
        """

        :param client_id: ID of the expected client
        :param client_tcp_id: ID of the connection
        :param connection_settings: useful ConnectionSettings parameters are {direction_role, keyword} - for a client,
            and all - for the super server.
        """
        self.id = client_id
        self.connection_id = client_tcp_id
        self.__connection = None  # type: Optional[Connection]
        self.connection_settings = connection_settings
        self.connection_settings.check()

        self.will_use_raw_client_connection = False
        self.will_use_raw_connection_without_handshake = False
        self.this_is_unknown_client = False

        self.obj_for_inline_processing = None

    def get_connection(self)->Connection:
        return self.__connection


class ASockIOCore(ASockIOCoreMemoryManagement):
    def __init__(self, gates_connections_settings: Set[ConnectionSettings]):
        """
        Port should not be open to a external world!
        :param gates_connections_settings: set() of ConnectionSettings()
        :return:
        """
        super(ASockIOCore, self).__init__()

        if os.name != 'nt':
            self.po = select.poll()
        self.last_all_sockets = set()  # type: Set[int]
        self.socket_by_fd = dict()  # type: Dict[int, socket.socket]

        self.check_sockets_sum_time = 0.0
        self.check_sockets_qnt = 0
        self.check_sockets_max_time = 0.0

        self.gates_connections_settings = gates_connections_settings
        if not self.gates_connections_settings:
            self.gates_connections_settings = set()
            # raise Exception('gates_connections_settings should be provided!')
        for gates_connections_settings in self.gates_connections_settings:
            gates_connections_settings.check()
        self.faulty_connection_settings = set()
        self._connection_settings_by_gate_conn = dict()

        self.set_of_gate_addresses = set()
        self._gate = set()
        self.reuse_gate_addr = False
        self.reuse_gate_port = False

        self.message_size_len = MESSAGE_SIZE_LEN
        self.server_answer__keyword_accepted = SERVER_ANSWER__KEYWORD_ACCEPTED

        self._connections = dict()  # key: ID; data: Connection()
        self._connection_by_conn = dict()  # key: conn; data: ID
        self._connections_id_gen = IDGenerator()

        self._connections_marked_as_ready_to_be_closed = set()
        self._connections_marked_to_be_closed_immediately = set()
        self._connections_marked_as_ready_to_be_deleted = set()

        self._unconfirmed_clients = set()

        self._we_have_connections_for_select = False
        self._input_check_sockets = set()
        self._output_check_sockets = set()
        self._exception_check_sockets = set()

        # ID (GUID) и другая информация клиентов, подключение которых явно ожидается
        self._expected_clients = dict()  # key: ID; data: Client()
        self._expected_clients_id_gen = IDGenerator()
        self._keywords_for_expected_clients = dict()  # key: keyword; data: info
        self._conns_of_expected_clients = dict()  # key: conn; data expected_client_ID

        self.unexpected_clients_are_allowed = True

        # Список неопознанных и неожидаемых клиентов. Если клиент выдал свой GUID и позже кто-то добавил этот GUID в
        # список ожидаемых клиентов - данный клиент будет автоматически подхвачен.
        self._unexpected_clients = dict()  # key: ID; data: Client()
        self._unexpected_clients_id_gen = IDGenerator()
        self._keywords_of_unexpected_clients = dict()
        self._conns_of_unexpected_clients = dict()

        self._io_iteration_result = IoIterationResult()

        self.raw_checker_for_new_incoming_connections = CheckIsRawConnection()
        self.need_to_auto_check_incoming_raw_connection = False
        self.unknown_clients_are_allowed = False
        self._unknown_clients_keyword_gen = IDGenerator(GeneratorType.guid_string)
        self.prefix_for_unknown_client_keywords = b'UNKNOWN CLIENT: '

        self.echo_log = False
        self._internal_log = deque()

        self.recv_sizes = deque()
        self.recv_buff_sizes = deque()

        self.should_get_client_addr_info_on_connection = True

        self.use_nodelay_inet = False
        self.use_speed_optimized_socket_read = False

        self.show_inform_about_accept_stop_because_of_all_buffers_size_limit = \
            FrontTriggerableVariable(FrontTriggerableVariableType.equal, True)
        self.show_inform_about_read_stop_because_of_in_buffer_size_limit = \
            FrontTriggerableVariable(FrontTriggerableVariableType.equal, True)
        self.show_inform_about_work_stop_because_of_out_buffer_size_limit = \
            FrontTriggerableVariable(FrontTriggerableVariableType.equal, True)

        self.class_for_unknown_clients_inline_processing = None

        self._clients_with_inline_processors_that_need_to_apply_parameters = set()

    @staticmethod
    def check_sockets_select(read: Set[int], write: Set[int], error: Set[int],
                             timeout: float)->Tuple[Set[int], Set[int], Set[int]]:
        all_sockets = read | write | error
        if all_sockets:
            return select.select(read,
                                 write,
                                 error,
                                 timeout)
        else:
            return set(), set(), set()

    def check_sockets_poll(self, read: Set[int], write: Set[int], error: Set[int],
                           timeout: float)->Tuple[Set[int], Set[int], Set[int]]:
        read_events = select.POLLIN | select.POLLPRI
        write_events = select.POLLOUT
        except_events = select.POLLERR | select.POLLHUP | select.POLLNVAL
        if hasattr(select, 'POLLRDHUP'):
            except_events |= select.POLLRDHUP
        readable_events = {select.POLLIN, select.POLLPRI}
        writable_events = {select.POLLOUT}
        exceptional_events = {select.POLLERR, select.POLLHUP, select.POLLNVAL}
        if hasattr(select, 'POLLRDHUP'):
            exceptional_events.add(select.POLLRDHUP)
        all_events_set = readable_events | writable_events | exceptional_events

        timeout = int(timeout * 1000)

        # print('>>> POLL {}: last_all_sockets: {}'.format(time.perf_counter(), self.last_all_sockets))
        all_sockets = read | write | error
        # print('>>> POLL {}: all_sockets: {}'.format(time.perf_counter(), all_sockets))
        new_sockets = all_sockets - self.last_all_sockets
        # print('>>> POLL {}: new_sockets: {}'.format(time.perf_counter(), new_sockets))
        still_sockets = all_sockets & self.last_all_sockets
        # print('>>> POLL {}: still_sockets: {}'.format(time.perf_counter(), still_sockets))
        deleted_sockets = self.last_all_sockets - all_sockets
        # print('>>> POLL {}: deleted_sockets: {}'.format(time.perf_counter(), deleted_sockets))
        self.last_all_sockets = all_sockets

        for socket_fd in new_sockets:
            event_mask = 0
            if socket_fd in read:
                event_mask |= read_events
            if socket_fd in write:
                event_mask |= write_events
            if socket_fd in error:
                event_mask |= except_events
            # print('>>> POLL {}: new_socket: {}; event_mask: {}'.format(time.perf_counter(), socket_fd, event_mask))
            self.po.register(socket_fd, event_mask)

        for socket_fd in still_sockets:
            event_mask = 0
            if socket_fd in read:
                event_mask |= read_events
            if socket_fd in write:
                event_mask |= write_events
            if socket_fd in error:
                event_mask |= except_events
            # print('>>> POLL {}: still_socket: {}; event_mask: {}'.format(time.perf_counter(), socket_fd, event_mask))
            self.po.modify(socket_fd, event_mask)

        for socket_fd in deleted_sockets:
            # print('>>> POLL {}: deleted_socket: {}'.format(time.perf_counter(), socket_fd))
            self.po.unregister(socket_fd)

        poll_result = self.po.poll(timeout)
        # print('>>> POLL {}: result: {}'.format(time.perf_counter(), poll_result))
        # sys.stdout.flush()

        readable = set()
        writable = set()
        exceptional = set()
        for socket_fd, event_mask in poll_result:
            socket_events_set = set()
            for another_event in all_events_set:
                if event_mask & another_event:
                    socket_events_set.add(another_event)

            if socket_events_set & readable_events:
                readable.add(socket_fd)
            if socket_events_set & writable_events:
                writable.add(socket_fd)
            if socket_events_set & exceptional_events:
                exceptional.add(socket_fd)

        return readable, writable, exceptional

    def check_sockets(self, read: Set[socket.socket], write: Set[socket.socket], error: Set[socket.socket],
                      timeout: float)->Tuple[Set[socket.socket], Set[socket.socket], Set[socket.socket]]:
        all_sockets = read | write | error
        if all_sockets:
            read_fd = set()
            write_fd = set()
            error_fd = set()
            for conn in read:
                read_fd.add(conn.fileno())
            for conn in write:
                write_fd.add(conn.fileno())
            for conn in error:
                error_fd.add(conn.fileno())

            check_sockets = self.check_sockets_select
            if os.name != 'nt':
                check_sockets = self.check_sockets_poll

            readable_fd, writable_fd, exceptional_fd = check_sockets(read_fd,
                                                                     write_fd,
                                                                     error_fd,
                                                                     timeout)
            readable = set()
            writable = set()
            exceptional = set()
            for fd in readable_fd:
                readable.add(self.socket_by_fd[fd])
            for fd in writable_fd:
                writable.add(self.socket_by_fd[fd])
            for fd in exceptional_fd:
                exceptional.add(self.socket_by_fd[fd])
            return readable, writable, exceptional
        else:
            return set(), set(), set()

    def gate_io_iteration(self, timeout=0.0):
        result = self._io_iteration_result
        if self._gate:
            readable, writable, exceptional = self.check_sockets_select(self._gate,
                                                                        set(),
                                                                        set(),
                                                                        timeout)

            # Handle inputs
            for s in readable:
                self._read_data_from_socket(s)

        self._io_iteration_result = IoIterationResult()
        return result

    # @profile
    def io_iteration(self, timeout=0.0):
        """

        :param timeout: timeout in seconds
        :return:
        """
        result = self._io_iteration_result

        if self._we_have_connections_for_select:
            # need_to_process = False
            # all_sockets = self._input_check_sockets | self._output_check_sockets | self._exception_check_sockets
            # if not (all_sockets - self._gate):
            #     timeout = 0.01

            need_to_repeat = True

            while need_to_repeat:
                output_check_sockets = set()

                # Is need to check writable sockets
                need_to_check_writable_sockets = False
                for s in self._output_check_sockets:
                    curr_client_info = self._connections[self._connection_by_conn[s]]
                    if curr_client_info.output_to_client.size():
                        need_to_check_writable_sockets = True
                        break

                if need_to_check_writable_sockets:
                    output_check_sockets = self._output_check_sockets

                # print('>>> POLL {}: ri: {}, wi: {}, ei: {}'.format(time.perf_counter(),
                #                                                    len(self._input_check_sockets),
                #                                                    len(self._output_check_sockets),
                #                                                    len(self._exception_check_sockets)))
                # sys.stdout.flush()
                check_sockets_start_time = time.perf_counter()
                readable, writable, exceptional = self.check_sockets(self._input_check_sockets,
                                                                     output_check_sockets,
                                                                     self._exception_check_sockets,
                                                                     timeout)
                check_sockets_finish_time = time.perf_counter()
                check_sockets_delta_time = check_sockets_finish_time - check_sockets_start_time
                self.check_sockets_sum_time += check_sockets_delta_time
                self.check_sockets_qnt += 1
                if self.check_sockets_max_time < check_sockets_delta_time:
                    self.check_sockets_max_time = check_sockets_delta_time
                check_socket_average_time = self.check_sockets_sum_time / self.check_sockets_qnt
                # print('>>> CHECK SOCKET: DELTA {}: AVG: {}; SUM: {}; MAX: {}'.format(
                #     check_sockets_delta_time,
                #     check_socket_average_time,
                #     self.check_sockets_sum_time,
                #     self.check_sockets_max_time
                # ))
                # print('>>> POLL {}: ro: {}, wo: {}, eo: {}'.format(time.perf_counter(),
                #                                                    len(readable),
                #                                                    len(writable),
                #                                                    len(exceptional)))
                # sys.stdout.flush()

                read_is_forbidden = True
                if (self.global_in__data_full_size.result - self.global_in__deletable_data_full_size.result) \
                        <= self.global_in__data_size_limit.result:
                    read_is_forbidden = False

                    # Handle inputs
                    for s in readable:
                        read_result = self._read_data_from_socket(s)
                        if read_result:
                            if s in self._unconfirmed_clients:
                                self._process_client_keyword(s)
                                self._check_is_client_have_data_to_read_in_fifo(s)
                            else:
                                self._client_have_data_to_read_in_fifo(s)

                if __debug__:
                    read_is_forbidden_test = self.show_inform_about_read_stop_because_of_in_buffer_size_limit.test_trigger(
                        read_is_forbidden)
                    if read_is_forbidden_test is not None:
                        if read_is_forbidden_test:
                            print('Read is suppressed until data will be processed.')
                        else:
                            print('Read is allowed: data is processed.')

                # Handle outputs
                for s in writable:
                    curr_client_info = self._connections[self._connection_by_conn[s]]
                    self._write_data_to_socket(curr_client_info)
                    # self._write_data_to_socket(s)

                # Handle "exceptional conditions"
                for s in exceptional:
                    self._handle_connection_error(s)

                # Set parameters for inline processors
                if self._clients_with_inline_processors_that_need_to_apply_parameters:
                    for ec_id in self._clients_with_inline_processors_that_need_to_apply_parameters:
                        expected_client_info = self._expected_clients[ec_id]
                        connection_info = expected_client_info._Client__connection
                        self._inline_processor__apply_parameters(connection_info, expected_client_info)
                    self._clients_with_inline_processors_that_need_to_apply_parameters.clear()

                # Close sockets
                if self._connections_marked_to_be_closed_immediately:
                    sockets_should_be_closed_immediately = self._connections_marked_to_be_closed_immediately
                    self._connections_marked_to_be_closed_immediately = set()
                    for closeable_socket in sockets_should_be_closed_immediately:
                        connection_id = self._connection_by_conn[closeable_socket]
                        # self.close_connection_by_conn(closeable_socket)
                        self.close_connection(connection_id)
                        self._inline_processor__on__connection_lost_by_connection_id(connection_id)

                # Removing clients
                if self._connections_marked_as_ready_to_be_deleted:
                    clients_ready_to_be_deleted = self._connections_marked_as_ready_to_be_deleted
                    self._connections_marked_as_ready_to_be_deleted = set()
                    for faulty_socket in clients_ready_to_be_deleted:
                        self.remove_connection_by_conn(faulty_socket)

                if (self.global_out__data_full_size.result - self.global_out__deletable_data_full_size.result) \
                        <= self.global_out__data_size_limit.result:
                    need_to_repeat = False
                else:
                    need_to_repeat = True

                need_to_repeat = False

                if __debug__:
                    need_to_repeat_show = self.show_inform_about_work_stop_because_of_out_buffer_size_limit.test_trigger(
                        need_to_repeat)
                    if need_to_repeat_show is not None:
                        if need_to_repeat_show:
                            print('Work is suppressed until data will be out.')
                        else:
                            print('Work is allowed: data is out.')

        self._io_iteration_result = IoIterationResult()
        return result

    def listen(self, backlog=1):
        # backlog = backlog or 1

        new_connection_settings = set()
        for gate_connection_settings in self.gates_connections_settings:
            gate = None
            try:
                gate = socket.socket(gate_connection_settings.socket_family, gate_connection_settings.socket_type,
                                     gate_connection_settings.socket_protocol, gate_connection_settings.socket_fileno)
                self.socket_by_fd[gate.fileno()] = gate
                gate.setblocking(0)
                # gate.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            except (socket.error, OSError) as err:
                gate = None
                if __debug__: self._log('EXCEPTION: GATE: LISTEN: CREATE SOCKET: {}, {}'.format(
                    err.errno, err.strerror))
                continue

            if self.reuse_gate_port:
                gate.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

            try:
                self._check_for_initial_af_unix_socket_unlink(gate_connection_settings)
                gate.bind(gate_connection_settings.socket_address)
            except (socket.error, OSError) as err:
                del self.socket_by_fd[gate.fileno()]
                gate.close()
                gate = None
                if __debug__: self._log('EXCEPTION: GATE: BIND:"{}", {}, {}'.format(
                    gate_connection_settings.socket_address, err.errno, err.strerror))
                continue
            try:
                gate.listen(backlog)
            except (socket.error, OSError) as err:
                del self.socket_by_fd[gate.fileno()]
                gate.close()
                gate = None
                if __debug__: self._log('EXCEPTION: GATE: LISTEN:"{}", {}, {}'.format(
                    gate_connection_settings.socket_address, err.errno, err.strerror))
                continue

            if self.reuse_gate_addr:
                gate.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            self._input_check_sockets.add(gate)
            self._exception_check_sockets.add(gate)

            if gate:
                self._gate.add(gate)
                if gate_connection_settings.socket_family in INET_TYPE_CONNECTIONS:
                    self.set_of_gate_addresses.add(gate_connection_settings.socket_address[0])
                elif socket.AF_UNIX == gate_connection_settings.socket_family:
                    self.set_of_gate_addresses.add(gate_connection_settings.socket_address)
                else:
                    self.set_of_gate_addresses.add(gate_connection_settings.socket_address)
                    self._log('WARNING: GATE: SAVE CONNECTION ADDRESS: UNKNOWN SOCKET FAMILY')
                self._connection_settings_by_gate_conn[gate] = gate_connection_settings
                self._we_have_connections_for_select = True
                new_connection_settings.add(gate_connection_settings)
            else:
                self.faulty_connection_settings.add(gate_connection_settings)
        self.gates_connections_settings = new_connection_settings

        return len(self.gates_connections_settings)

    def close_all_connections(self):
        if __debug__: self._log('CLOSE ALL CONNECTIONS:')
        clients_list = dict(self._connections)
        for connection_id, client_info in clients_list.items():
            self.close_connection(connection_id)

    def remove_all_connections(self):
        clients_list = dict(self._connections)
        for connection_id, client_info in clients_list.items():
            self.remove_connection(connection_id)

    def close(self):
        for gate in self._gate:
            del self.socket_by_fd[gate.fileno()]
            gate.close()

            if gate in self._input_check_sockets:
                self._input_check_sockets.remove(gate)
            if gate in self._exception_check_sockets:
                self._exception_check_sockets.remove(gate)

            if not self._input_check_sockets:
                self._we_have_connections_for_select = False
        self._unlink_good_af_unix_sockets()

    def destroy(self):
        self.close()
        self.close_all_connections()
        self.remove_all_connections()

    def add_client(self, expected_client_info: Client):
        """
        Добавляет новый expected client в список. Это может быть как клиент (который сам подключился или подключится в
        будущем), так и супер-сервер, попытка подключения к которому будет осуществлена тут же - на месте.
        При этом если произойдет какая-либо ошибка при подключении к супер-серверу - expected client не будет
        зарегистрирован. Однако client может быть создан. В случае ошибки он будет помечен для закрытия и удаления.
        Поэтому исключения нужно перехватывать, и после этого проводить как минимум один (как минимум завершающий -
        перед закрытием и уничтожением сервера) цикл обработки io_iteration().
        :param expected_client_info: link to Client()
        :return: expected_client_id
        """
        if (expected_client_info.connection_settings.keyword is None) \
                and (ConnectionDirectionRole.client == expected_client_info.connection_settings.direction_role):
            raise Exception('Keyword in Client.connection_settings should not be None for a Client connection!')

        if expected_client_info.connection_settings.keyword in self._keywords_for_expected_clients:
            raise Exception('Expected Client with keyword "{}" is already registered!'.format(
                expected_client_info.connection_settings.keyword))

        expected_client_info.id = self._expected_clients_id_gen.get_new_ID()

        if self.unexpected_clients_are_allowed:
            if expected_client_info.connection_settings.keyword in self._keywords_of_unexpected_clients:
                # клиент уже подключен
                unexpected_client_id = self._keywords_of_unexpected_clients[
                    expected_client_info.connection_settings.keyword]
                unexpected_client_info = self._unexpected_clients[unexpected_client_id]
                connection_info = expected_client_info._Client__connection
                if (
                    unexpected_client_info.connection_settings.direction_role == expected_client_info.connection_settings.direction_role) and \
                        (ConnectionDirectionRole.client == unexpected_client_info.connection_settings.direction_role):
                    # Произошел запрос на подключение к клиенту, и клиент с таким же ключевым словом уже
                    # подключен (с сервером этого быть не должно, и может произойти только при неверном ручном изменении
                    # внутренних данных объекта класса ASockIOCore). Необходимо переиспользовать уже имеющееся
                    # подключение.
                    # В случае если все же тут оказался соккет подключенный к супер-серверу - он будет автоматически
                    # отключен и соединение будет установлено в новом сокете.
                    expected_client_info.connection_id = unexpected_client_info.connection_id
                    expected_client_info._Client__connection = \
                        unexpected_client_info._Client__connection
                    self._conns_of_expected_clients[connection_info.conn.result] = expected_client_info.id
                    connection_info.connected_expected_client_id = expected_client_info.id
                    connection_info.connected_expected_client = expected_client_info
                    self._io_iteration_result.newly_connected_expected_clients.add(expected_client_info.id)
                else:
                    # Произошел запрос на подключение к супер-серверу, но клиент с таким же ключевым словом уже
                    # подключен (или наоборот). Или же просто имеется установленное соединение с супер-сервером.
                    # Необходимо его отключить.
                    self._mark_connection_to_be_closed_immediately(connection_info)
                    self._mark_connection_as_ready_for_deletion(connection_info)
                self._remove_unexpected_client(unexpected_client_id)
            else:
                # клиент еще не подключен
                expected_client_info.connection_id = None
                expected_client_info._Client__connection = None

        if ConnectionDirectionRole.server == expected_client_info.connection_settings.direction_role:
            self._connect_to_super_server(expected_client_info)

        self._keywords_for_expected_clients[expected_client_info.connection_settings.keyword] = expected_client_info.id
        self._expected_clients[expected_client_info.id] = expected_client_info

        return expected_client_info.id

    def get_client_id_by_keyword(self, expected_client_keyword):
        """
        :param expected_client_keyword: expected_client_keyword
        :return: link to Client()
        """
        return self._keywords_for_expected_clients[expected_client_keyword]

    def get_client_info(self, expected_client_id):
        """
        :param expected_client_id: expected_client_id
        :return: link to Client()
        """
        return self._expected_clients[expected_client_id]

    def get_connection_input_fifo_size_for_client(self, expected_client_id):
        expected_client_info = self._expected_clients[expected_client_id]
        connection_info = expected_client_info._Client__connection
        if connection_info is None:
            raise Exception('Expected client was not connected yet!')
        # if client_info.this_is_raw_connection:
        #     if client_info.input_from_client.size():
        #         return 1
        #     else:
        #         return 0
        # else:
        #     return client_info.input_from_client.size()
        return connection_info.input_from_client.size()

    def get_message_from_client(self, expected_client_id):
        expected_client_info = self._expected_clients[expected_client_id]
        connection_info = expected_client_info._Client__connection
        if connection_info is None:
            raise Exception('Expected client was not connected yet!')
        if not connection_info.input_from_client.size():
            raise Exception('There is no readable data in expected client\'s FIFO!')
        # if client_info.this_is_raw_connection:
        #     self._consolidate_raw_messages_in_input_from_client_fifo(client_info)
        return connection_info.input_from_client.get()

    # @profile
    def get_messages_from_client(self, expected_client_id):
        expected_client_info = self._expected_clients[expected_client_id]
        connection_info = expected_client_info._Client__connection
        if connection_info is None:
            raise Exception('Expected client was not connected yet!')
        try:
            while True:
                yield connection_info.input_from_client.get()
        except FIFOIsEmpty:
            pass
            # while client_info.input_from_client.size():
            #     yield client_info.input_from_client.get()

    def get_connection_output_fifo_size_for_client(self, expected_client_id):
        expected_client_info = self._expected_clients[expected_client_id]
        connection_info = expected_client_info._Client__connection
        if connection_info is None:
            raise Exception('Expected client was not connected yet!')
        return connection_info.output_to_client.size()

    def send_message_to_client(self, expected_client_id, data):
        # data = bytes(data)
        expected_client_info = self._expected_clients[expected_client_id]
        connection_info = expected_client_info._Client__connection
        if connection_info is None:
            raise Exception('Expected client was not connected yet!')
        if connection_info.this_is_raw_connection:
            self._send_message_through_connection_raw(connection_info, data)
        else:
            self._send_message_through_connection(connection_info, data)

    def send_messages_to_client(self, expected_client_id, messages_list):
        # data = bytes(data)
        expected_client_info = self._expected_clients[expected_client_id]
        connection_info = expected_client_info._Client__connection
        if connection_info is None:
            raise Exception('Expected client was not connected yet!')
        if connection_info.this_is_raw_connection:
            self._send_messages_through_connection_raw(connection_info, messages_list)
        else:
            self._send_messages_through_connection(connection_info, messages_list)

    def check_is_client_is_in_raw_connection_mode(self, expected_client_id):
        expected_client_info = self._expected_clients[expected_client_id]
        connection_info = expected_client_info._Client__connection
        if connection_info is None:
            raise Exception('Expected client was not connected yet!')
        return connection_info.this_is_raw_connection

    def switch_client_raw_connection_mode(self, expected_client_id, is_raw: bool):
        expected_client_info = self._expected_clients[expected_client_id]
        connection_info = expected_client_info._Client__connection
        if connection_info is None:
            raise Exception('Expected client was not connected yet!')
        connection_info.this_is_raw_connection = is_raw

    def set_inline_processor_for_client(self, expected_client_id,
                                        class_for_unknown_clients_inline_processing: type):
        expected_client_info = self._expected_clients[expected_client_id]
        connection_info = expected_client_info._Client__connection
        if connection_info is None:
            raise Exception('Expected client was not connected yet!')
        self._set_inline_processor_for_client(connection_info, expected_client_info,
                                              class_for_unknown_clients_inline_processing)

    def close_client_connection(self, expected_client_id, raise_if_already_closed=True):
        """
        Connection will be closed immediately (inside this method)
        :param expected_client_id:
        :param raise_if_already_closed:
        :return:
        """
        if __debug__: self._log('CLOSE EXPECTED CLIENT SOCKET:')
        expected_client_info = self._expected_clients[expected_client_id]
        connection_info = expected_client_info._Client__connection
        if raise_if_already_closed and (connection_info is None):
            raise Exception('Expected client was not connected yet!')
        self.close_connection(connection_info.id)

    def mark_client_connection_as_should_be_closed_immediately(self, expected_client_id,
                                                               raise_if_already_closed=True):
        """
        Connection will be closed immediately (inside main IO loop)
        :param expected_client_id:
        :param raise_if_already_closed:
        :return:
        """
        if __debug__: self._log('MARK EXPECTED CLIENT SOCKET AS SHOULD BE CLOSED IMMEDIATELY:')
        expected_client_info = self._expected_clients[expected_client_id]
        connection_info = expected_client_info._Client__connection
        if raise_if_already_closed and (connection_info is None):
            raise Exception('Expected client was not connected yet!')
        self._mark_connection_to_be_closed_immediately(connection_info)

    def mark_client_connection_as_ready_to_be_closed(self, expected_client_id, raise_if_already_closed=True):
        """
        Connection will be closed when all output will be sent (inside main IO loop).
        :param expected_client_id:
        :param raise_if_already_closed:
        :return:
        """
        if __debug__: self._log('MARK EXPECTED CLIENT SOCKET AS READY TO BE CLOSED:')
        expected_client_info = self._expected_clients[expected_client_id]
        connection_info = expected_client_info._Client__connection
        if raise_if_already_closed and (connection_info is None):
            raise Exception('Expected client was not connected yet!')
        self._mark_connection_as_ready_to_be_closed(connection_info)

    def remove_client(self, expected_client_id):
        if __debug__: self._log('REMOVE EXPECTED CLIENT: {}'.format(expected_client_id))
        expected_client_info = self._expected_clients[expected_client_id]
        if __debug__: self._log('\tWITH KEYWORD: {}'.format(expected_client_info.connection_settings.keyword))
        connection_id = expected_client_info.connection_id
        if connection_id is None:
            self._remove_client(expected_client_id)
        self.remove_connection(connection_id)

    def add_connection(self, conn, address):
        """
        :param conn: socket
        :param address: address
        :return: client ID
        """
        if conn is None:
            raise TypeError('conn should not be None!')

        self.socket_by_fd[conn.fileno()] = conn
        conn.setblocking(0)
        if self.use_nodelay_inet and (conn.family in INET_TYPE_CONNECTIONS):
            conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        new_client_id = self._connections_id_gen.get_new_ID()

        client_info = Connection(new_client_id, (conn, address), self)
        self._connections[new_client_id] = client_info
        self._connection_by_conn[conn] = new_client_id
        self._input_check_sockets.add(conn)
        self._exception_check_sockets.add(conn)
        self._we_have_connections_for_select = True

        self._unconfirmed_clients.add(conn)

        return new_client_id

    def check_connection_existance(self, connection_id):
        if connection_id not in self._expected_clients:
            return False
        if connection_id not in self._connections:
            return False
        client_info = self._connections[connection_id]
        if not client_info.conn.existence:
            return False
        conn = client_info.conn.result
        if conn is None:
            return False
        return True

    def close_connection(self, connection_id):
        if __debug__: self._log('CLOSE CLIENT {}:'.format(connection_id))
        client_info = self._connections[connection_id]
        if not client_info.conn.existence:
            if __debug__: self._log('CLIENT {} CONN IS NOT SET.'.format(connection_id))
            return
        conn = client_info.conn.result
        if conn is None:
            if __debug__: self._log('CLIENT {} CONN IS NONE.'.format(connection_id))
            return

        del self.socket_by_fd[conn.fileno()]
        conn.close()
        client_info.conn.existence = False
        client_info.output_to_client = copy.copy(client_info.output_to_client)  # clear all output data to free some
        #   memory even before destroying

        if connection_id in self._connections_marked_as_ready_to_be_closed:
            self._connections_marked_as_ready_to_be_closed.remove(connection_id)
        if conn in self._connections_marked_to_be_closed_immediately:
            self._connections_marked_to_be_closed_immediately.remove(conn)
        if conn in self._connection_by_conn:
            del self._connection_by_conn[conn]
        if conn in self._input_check_sockets:
            self._input_check_sockets.remove(conn)
        if conn in self._output_check_sockets:
            self._output_check_sockets.remove(conn)
        if conn in self._exception_check_sockets:
            self._exception_check_sockets.remove(conn)

        if not self._input_check_sockets:
            self._we_have_connections_for_select = False

        if __debug__: self._log('CLIENT {} NORMALLY CLOSED.'.format(connection_id))

    def close_connection_by_conn(self, conn):
        # Если conn не в списке - вылетет ошибка. Это предотвратит ошибочное закрытие незарегистрированного сокета.
        # И мы сможем обнаружить наличие соответствующей ошибки в коде.
        if __debug__: self._log('CLOSE CLIENT BY CONN: {}'.format(repr(conn)))
        connection_id = self._connection_by_conn[conn]
        if __debug__: self._log('\t WITH CLIENT ID: {}'.format(connection_id))
        self.close_connection(connection_id)

    def remove_connection(self, connection_id):
        # client should NOT be removed immediately after connection close (close_connection):
        # code should do it by itself after reading all available input data
        if __debug__: self._log('REMOVE CLIENT: {}'.format(connection_id))
        client_info = self._connections[connection_id]
        if __debug__: self._log('\tWITH KEYWORD: {}'.format(client_info.keyword))
        if client_info.conn.existence:
            self.close_connection(connection_id)
        conn = client_info.conn.result
        if conn is None:
            return

        if conn in self._conns_of_unexpected_clients:
            self._remove_unexpected_client(self._conns_of_unexpected_clients[conn])

        # if conn in self._conns_of_expected_clients:
        #     self._remove_client(self._conns_of_expected_clients[conn])
        if client_info.connected_expected_client_id is not None:
            self._remove_client(client_info.connected_expected_client_id)

        client_info.connected_expected_client_id = None
        client_info.connected_expected_client = None

        if connection_id in self._connections_marked_as_ready_to_be_deleted:
            self._connections_marked_as_ready_to_be_deleted.remove(connection_id)

        client_info.conn.existence = False
        client_info.conn.result = None

        del self._connections[connection_id]
        if conn in self._connection_by_conn:
            del self._connection_by_conn[conn]
        if conn in self._input_check_sockets:
            self._input_check_sockets.remove(conn)
        if conn in self._output_check_sockets:
            self._output_check_sockets.remove(conn)
        if conn in self._exception_check_sockets:
            self._exception_check_sockets.remove(conn)

            # client_info.remove()

    def remove_connection_by_conn(self, conn):
        connection_id = self._connection_by_conn[conn]
        self.remove_connection(connection_id)

    def _log(self, log_string):
        self._internal_log.append(log_string)
        if self.echo_log:
            print(log_string)
            sys.stdout.flush()

    def _create_unknown_client_from_connection(self, client_info: Connection):
        keyword = None
        keyword_is_ok = False
        while not keyword_is_ok:
            keyword = self.prefix_for_unknown_client_keywords + self._unknown_clients_keyword_gen.get_new_ID().encode()
            if keyword not in self._keywords_for_expected_clients:
                keyword_is_ok = True
        connection_settings = ConnectionSettings(direction_role=ConnectionDirectionRole.client,
                                                 socket_address=client_info.addr.result, keyword=keyword)
        expected_client_info = Client(connection_settings)
        expected_client_info.id = self._expected_clients_id_gen.get_new_ID()

        expected_client_info.connection_id = client_info.id
        expected_client_info._Client__connection = client_info
        expected_client_info.will_use_raw_client_connection = True
        expected_client_info.will_use_raw_connection_without_handshake = True
        expected_client_info.this_is_unknown_client = True
        if self.class_for_unknown_clients_inline_processing is not None:
            self._set_inline_processor_for_client(client_info, expected_client_info,
                                                  self.class_for_unknown_clients_inline_processing)

        self._conns_of_expected_clients[client_info.conn.result] = expected_client_info.id
        client_info.connected_expected_client_id = expected_client_info.id
        client_info.connected_expected_client = expected_client_info
        self._keywords_for_expected_clients[expected_client_info.connection_settings.keyword] = expected_client_info.id
        self._expected_clients[expected_client_info.id] = expected_client_info

        self._io_iteration_result.newly_connected_unknown_clients.add(expected_client_info.id)

        return expected_client_info.id

    def _set_inline_processor_for_client(self, connection_info: Connection,
                                         expected_client_info: Client,
                                         class_for_unknown_clients_inline_processing: type):
        assert type(class_for_unknown_clients_inline_processing) == type, \
            '.class_for_unknown_clients_inline_processing must be a class or None'
        keyword = expected_client_info.connection_settings.keyword
        expected_client_info.obj_for_inline_processing = class_for_unknown_clients_inline_processing(
            expected_client_info.id, keyword, connection_info.conn.result.family, connection_info.conn.result.type,
            connection_info.conn.result.proto, copy.copy(connection_info.addr_info),
            copy.copy(connection_info.host_names), self._clients_with_inline_processors_that_need_to_apply_parameters
        )
        connection_info.has_inline_processor = True
        self._inline_processor__init_parameters(connection_info, expected_client_info)

    def _connect_to_super_server(self, expected_client_info: Client):
        """
        Подключение происходит в блокируещем режиме (неблокирующий режим включается позже - в методе add_connection()).
        Для реализации неблокирующего режима надо оттестировать текущий код и ввести дополнительную неблокирующую
        логику через select/poll/epoll:
        http://man7.org/linux/man-pages/man2/connect.2.html
        :param expected_client_info:
        :return:
        """
        connection_settings = expected_client_info.connection_settings
        conn = None
        try:
            conn = socket.socket(connection_settings.socket_family, connection_settings.socket_type,
                                 connection_settings.socket_protocol, connection_settings.socket_fileno)
            self.socket_by_fd[conn.fileno()] = conn
            # conn.setblocking(0)
        except (socket.error, OSError) as err:
            if __debug__: self._log('EXCEPTION: SUPER SERVER: CONNECT TO: CREATE SOCKET: {}, {}'.format(
                err.errno, err.strerror))
            raise

        try:
            conn.connect(connection_settings.socket_address)
        except (TimeoutError, socket.error, OSError) as err:
            # https://stackoverflow.com/questions/16772519/socket-recv-on-selected-socket-failing-with-etimedout
            del self.socket_by_fd[conn.fileno()]
            conn.close()
            if __debug__: self._log('EXCEPTION: SUPER SERVER: CONNECT TO: CONNECT:"{}", {}, {}'.format(
                connection_settings.socket_address, err.errno, err.strerror))
            raise

        super_server_client_id = self.add_connection(conn, connection_settings.socket_address)

        addr_info = host_names = None
        try:
            if self.should_get_client_addr_info_on_connection and (conn.family in INET_TYPE_CONNECTIONS):
                addr_info = socket.getaddrinfo(connection_settings.socket_address[0],
                                               connection_settings.socket_address[1])
                host_names = socket.gethostbyaddr(connection_settings.socket_address[0])
        except ConnectionError as err:
            # An established connection was aborted by the software in your host machine
            if __debug__: self._log('CLOSING {}: Connection reset by peer'.format(connection_settings.socket_address))
            if __debug__: self._log('EXCEPTION: CONNECT TO SUPER SERVER: GETTING CONNECTION INFO:"{}", {}, {}'.format(
                connection_settings.socket_address, err.errno, err.strerror))
            self._mark_connection_to_be_closed_immediately(super_server_client_id)
            ok = False
        except (socket.error, OSError) as err:
            if __debug__: self._log('EXCEPTION: CONNECT TO SUPER SERVER: GETTING CONNECTION INFO:"{}", {}, {}'.format(
                connection_settings.socket_address, err.errno, err.strerror))
            if err.errno in SET_OF_CONNECTION_ERRORS:
                # An established connection was aborted by the software in your host machine
                if __debug__: self._log(
                    'CLOSING {}: Connection reset by peer'.format(connection_settings.socket_address))
                if __debug__: self._log(
                    'EXCEPTION: CONNECT TO SUPER SERVER: GETTING CONNECTION INFO:"{}", {}, {}'.format(
                        connection_settings.socket_address, err.errno, err.strerror))
                self._mark_connection_to_be_closed_immediately(super_server_client_id)
                ok = False
            else:
                if 'nt' == os.name:
                    if errno.WSAECONNRESET == err.errno:
                        # An existing connection was forcibly closed by the remote host
                        if __debug__: self._log(
                            'CLOSING {}: Connection reset by peer'.format(connection_settings.socket_address))
                        if __debug__: self._log(
                            'EXCEPTION: CONNECT TO SUPER SERVER: GETTING CONNECTION INFO:"{}", {}, {}'.format(
                                connection_settings.socket_address, err.errno, err.strerror))
                        self._mark_connection_to_be_closed_immediately(super_server_client_id)
                        ok = False
                    else:
                        raise err
                else:
                    raise err

        super_server_client_info = self._connections[super_server_client_id]
        super_server_client_info.addr_info = addr_info
        super_server_client_info.host_names = host_names
        self._log_new_connection(super_server_client_info, False)

        if expected_client_info.will_use_raw_connection_without_handshake:
            # Connection is made without handshake
            super_server_client_info.this_is_raw_connection = True
            self._unconfirmed_clients.remove(super_server_client_info.conn.result)
            self._io_iteration_result.newly_connected_expected_clients.add(expected_client_info.id)
        else:
            keyword = expected_client_info.connection_settings.keyword
            if keyword is None:
                keyword = self._get_own_keyword_appropriate_for_connection(conn)
            if keyword is None:
                # Если ключевое слово не предоставлено - клиент будет помечен для закрытия и удаления
                self._mark_connection_to_be_closed_immediately(super_server_client_info)
                self._mark_connection_as_ready_for_deletion(super_server_client_info)
                raise Exception('Own keyword should be provided in connection_settings!')
            if keyword:
                # Если ключевое слово предоставлено (даже если оно путое типа b'' - оно будет отправлено супер-серверу).
                self._send_message_through_connection(super_server_client_info, keyword)

        expected_client_info.connection_id = super_server_client_id
        expected_client_info._Client__connection = super_server_client_info
        self._conns_of_expected_clients[conn] = expected_client_info.id
        super_server_client_info.connected_expected_client_id = expected_client_info.id
        super_server_client_info.connected_expected_client = expected_client_info

    def _get_own_keyword_appropriate_for_connection(self, conn):
        keyword = None
        random_keyword = None
        for gate_connection_settings in self.gates_connections_settings:
            random_keyword = gate_connection_settings.keyword
            if (conn.family == gate_connection_settings.socket_family) and (
                conn.type == gate_connection_settings.socket_type) and \
                    (conn.proto == gate_connection_settings.socket_protocol):
                keyword = gate_connection_settings.keyword
        if keyword is None:
            keyword = random_keyword
        return keyword

    def _pack_message(self, data):
        return len(data).to_bytes(self.message_size_len, 'little') + data

    def _remove_client(self, expected_client_id):
        expected_client_info = self._expected_clients[expected_client_id]
        del self._keywords_for_expected_clients[expected_client_info.connection_settings.keyword]
        del self._expected_clients[expected_client_id]
        connection_info = expected_client_info._Client__connection
        if connection_info is not None:
            # you can remove expected client before it will be connected to the server
            del self._conns_of_expected_clients[connection_info.conn.result]
        expected_client_info.connection_id = None
        expected_client_info._Client__connection = None

    def _add_unexpected_client(self, connection_id, keyword):
        connection_settings = ConnectionSettings(direction_role=ConnectionDirectionRole.client, keyword=keyword)
        unexpected_client_info = Client(connection_settings, self._unexpected_clients_id_gen.get_new_ID(),
                                        connection_id)

        self._unexpected_clients[unexpected_client_info.id] = unexpected_client_info
        self._keywords_of_unexpected_clients[keyword] = unexpected_client_info.id
        connection_info = unexpected_client_info._Client__connection
        self._conns_of_unexpected_clients[connection_info.conn.result] = unexpected_client_info.id

        return unexpected_client_info.id

    def _remove_unexpected_client(self, unexpected_client_id):
        unexpected_client_info = self._unexpected_clients[unexpected_client_id]
        connection_info = unexpected_client_info._Client__connection  # unexpected client appears only after
        #   connection
        del self._keywords_of_unexpected_clients[unexpected_client_info.connection_settings.keyword]
        del self._unexpected_clients[unexpected_client_id]
        del self._conns_of_unexpected_clients[connection_info.conn.result]
        unexpected_client_info.connection_id = None
        unexpected_client_info._Client__connection = None

    # @profile
    def _accept_new_connection(self, readable_socket: socket.socket):
        # One of a "readable" self._gate sockets is ready to accept a connection
        ok = True
        while ok:
            connection_id = None
            client_info = None

            connection = None
            client_address = None
            try:
                connection, client_address = readable_socket.accept()
                self.socket_by_fd[connection.fileno()] = connection
                connection_id = self.add_connection(connection, client_address)
                client_info = self._connections[connection_id]
            except BlockingIOError as err:
                ok = False
            except InterruptedError as err:
                pass
            except (socket.error, OSError) as err:
                if (errno.EAGAIN == err.errno) or (errno.EWOULDBLOCK == err.errno):
                    ok = False
                elif errno.EINTR == err.errno:
                    pass
                elif errno.ECONNABORTED == err.errno:
                    ok = False
                elif errno.EMFILE == err.errno:
                    if __debug__: self._log(
                        'The per-process limit on the number of open file descriptors had been reached.')
                    ok = False
                elif errno.ENFILE == err.errno:
                    if __debug__: self._log(
                        'The system-wide limit on the total number of open files had been reached.')
                    ok = False
                elif (errno.ENOBUFS == err.errno) or (errno.ENOMEM == err.errno):
                    if __debug__: self._log(
                        'Not enough free memory. Allocation is limited by the socket buffer limits.')
                    ok = False
                elif errno.EPROTO == err.errno:
                    if __debug__: self._log('Protocol error.')
                    ok = False
                elif errno.EPERM == err.errno:
                    if __debug__: self._log('Firewall rules forbid connection.')
                    ok = False
                else:
                    raise err

            if (connection is not None) and (client_info is not None):
                addr_info = host_names = None
                try:
                    if self.should_get_client_addr_info_on_connection and \
                            (connection.family in INET_TYPE_CONNECTIONS):
                        addr_info = socket.getaddrinfo(client_address[0], client_address[1])
                        host_names = socket.gethostbyaddr(client_address[0])
                except ConnectionError as err:
                    # An established connection was aborted by the software in your host machine
                    if __debug__: self._log('CLOSING {}: Connection reset by peer'.format(client_address))
                    if __debug__: self._log('EXCEPTION: ACCEPT CLIENT: GETTING CONNECTION INFO:"{}", {}, {}'.format(
                        client_address, err.errno, err.strerror))
                    self._mark_connection_to_be_closed_immediately(client_info)
                    ok = False
                except (socket.error, OSError) as err:
                    if __debug__: self._log('EXCEPTION: ACCEPT CLIENT: GETTING CONNECTION INFO:"{}", {}, {}'.format(
                        client_address, err.errno, err.strerror))
                    if err.errno in SET_OF_CONNECTION_ERRORS:
                        # An established connection was aborted by the software in your host machine
                        if __debug__: self._log('CLOSING {}: Connection reset by peer'.format(client_address))
                        if __debug__: self._log('EXCEPTION: ACCEPT CLIENT: GETTING CONNECTION INFO:"{}", {}, {}'.format(
                            client_address, err.errno, err.strerror))
                        self._mark_connection_to_be_closed_immediately(client_info)
                        ok = False
                    else:
                        if 'nt' == os.name:
                            if errno.WSAECONNRESET == err.errno:
                                # An existing connection was forcibly closed by the remote host
                                if __debug__: self._log(
                                    'CLOSING {}: Connection reset by peer'.format(client_address))
                                if __debug__: self._log(
                                    'EXCEPTION: ACCEPT CLIENT: GETTING CONNECTION INFO:"{}", {}, {}'.format(
                                        client_address, err.errno, err.strerror))
                                self._mark_connection_to_be_closed_immediately(client_info)
                                ok = False
                            else:
                                raise err
                        else:
                            raise err

                client_info.addr_info = addr_info
                client_info.host_names = host_names
                self._log_new_connection(client_info, True)

                if self.need_to_auto_check_incoming_raw_connection \
                        and self.raw_checker_for_new_incoming_connections(self, client_info):
                    # Is should be RAW:
                    if self.unknown_clients_are_allowed:
                        # Unknown clients are allowed - create Unknown Expected Client for this connection
                        client_info.this_is_raw_connection = True
                        self._unconfirmed_clients.remove(client_info.conn.result)
                        self._create_unknown_client_from_connection(client_info)
                    else:
                        # Unknown clients are Non allowed - close connection.
                        if __debug__: self._log(
                            'UNKNOWN CLIENT {} WILL BE CLOSED: UNKNOWN CLIENTS ARE NOT ALLOWED'.format(
                                client_info.addr.result
                            ))
                        self._mark_connection_to_be_closed_immediately(client_info)

    # @profile
    def _read_data_from_already_connected_socket__inner__memory_optimized(self, curr_client_info: Connection,
                                                                          possible_messages_in_client_input_fifo=False):
        ok = True

        data = curr_client_info.conn.result.recv(curr_client_info.recv_buff_size)
        data_len = len(data)
        curr_client_info.calc_new_recv_buff_size(data_len)
        if data:
            data = memoryview(data)
            if curr_client_info.this_is_raw_connection:
                curr_client_info.input_from_client.put(data)
                possible_messages_in_client_input_fifo = True
            else:
                curr_client_info.raw_input_from_client.add_piece_of_data(data)
                possible_messages_in_client_input_fifo = self._read_messages_from_raw_input_into_fifo(
                    curr_client_info)
        else:
            # Interpret empty result as closed connection
            if __debug__: self._log(
                'CLOSING {} after reading no data:'.format(curr_client_info.addr.result))
            self._mark_connection_to_be_closed_immediately(curr_client_info)
            ok = False

        result = (ok, possible_messages_in_client_input_fifo)
        return result

    # @profile
    def _read_data_from_already_connected_socket__inner__speed_optimized(self, curr_client_info: Connection,
                                                                         possible_messages_in_client_input_fifo=False):
        ok = True

        if curr_client_info.current_memoryview_input:
            nbytes = 0
            try:
                nbytes = curr_client_info.conn.result.recv_into(curr_client_info.current_memoryview_input)
            except TimeoutError:
                # https://stackoverflow.com/questions/16772519/socket-recv-on-selected-socket-failing-with-etimedout
                pass

            if nbytes > 0:
                data = curr_client_info.current_memoryview_input[:nbytes]
                curr_client_info.current_memoryview_input = curr_client_info.current_memoryview_input[nbytes:]

                if curr_client_info.this_is_raw_connection:
                    curr_client_info.input_from_client.put(data)
                    possible_messages_in_client_input_fifo = True
                else:
                    curr_client_info.raw_input_from_client.add_piece_of_data(data)
                    possible_messages_in_client_input_fifo = self._read_messages_from_raw_input_into_fifo(
                        curr_client_info)
            else:
                # Interpret empty result as closed connection
                if __debug__: self._log(
                    'CLOSING {} after reading no data:'.format(curr_client_info.addr.result))
                self._mark_connection_to_be_closed_immediately(curr_client_info)
                ok = False
        else:
            input_buffer = bytearray(self.socket_read_fixed_buffer_size.result)
            curr_client_info.current_memoryview_input = memoryview(input_buffer)

        result = (ok, possible_messages_in_client_input_fifo)
        return result

    # @profile
    def _read_data_from_already_connected_socket__shell(self, readable_socket: socket.socket):
        possible_messages_in_client_input_fifo = False

        curr_client_id = self._connection_by_conn[readable_socket]
        curr_client_info = self._connections[curr_client_id]

        ok = True
        while ok:
            try:
                if self.use_speed_optimized_socket_read:
                    ok, possible_messages_in_client_input_fifo = \
                        self._read_data_from_already_connected_socket__inner__speed_optimized(
                            curr_client_info, possible_messages_in_client_input_fifo)
                else:
                    ok, possible_messages_in_client_input_fifo = \
                        self._read_data_from_already_connected_socket__inner__memory_optimized(
                            curr_client_info, possible_messages_in_client_input_fifo)
                break  # makes IO faster on 10-30% on all modes (message/raw, data/http,
                #   static_read_buffer/non_static_read_buffer).
                # Ускорение происходит за счет того, что: 1) данных оказывается не настолько много чтобы кеш процессора
                # переполнялся и требовалась бы работа с оперативной памятью; 2) при таком разбиении ввод и вывод
                # начинают происходить (на уровне ОС) одновременно. Т.е. мы взяли из входного буфера порцию данных и
                # пустили в обработку. В это время ввод на уровне ОС продолжается: ОС заполняет опустевшие буферы.
                # После обработки мы пускаем данные на отправку и забираем очередную порцию данных из входного буфера.
                # В это время происходит отправка данных из буферов на уровне ОС. И т.д.
            except BlockingIOError as err:
                ok = False
            except InterruptedError as err:
                pass
            except ConnectionError as err:
                # An established connection was aborted by the software in your host machine
                if __debug__: self._log('CLOSING {}: Connection reset by peer'.format(curr_client_info.addr.result))
                if __debug__: self._log('EXCEPTION: READ DATA FROM SOCKET: "{}", {}, {}'.format(
                    curr_client_info.addr.result, err.errno, err.strerror))
                self._mark_connection_to_be_closed_immediately(curr_client_info)
                ok = False
            except (socket.error, OSError) as err:
                if (errno.EAGAIN == err.errno) or (errno.EWOULDBLOCK == err.errno):
                    ok = False
                elif errno.EINTR == err.errno:
                    pass
                elif err.errno in SET_OF_CONNECTION_ERRORS:
                    # An established connection was aborted by the software in your host machine
                    if __debug__: self._log('CLOSING {}: Connection reset by peer'.format(curr_client_info.addr.result))
                    if __debug__: self._log('EXCEPTION: READ DATA FROM SOCKET: "{}", {}, {}'.format(
                        curr_client_info.addr.result, err.errno, err.strerror))
                    self._mark_connection_to_be_closed_immediately(curr_client_info)
                    ok = False
                else:
                    if 'nt' == os.name:
                        if errno.WSAECONNRESET == err.errno:
                            # An existing connection was forcibly closed by the remote host
                            if __debug__: self._log(
                                'CLOSING {}: Connection reset by peer'.format(curr_client_info.addr.result))
                            if __debug__: self._log('EXCEPTION: READ DATA FROM SOCKET: "{}", {}, {}'.format(
                                curr_client_info.addr.result, err.errno, err.strerror))
                            self._mark_connection_to_be_closed_immediately(curr_client_info)
                            ok = False
                        elif errno.EHOSTUNREACH == err.errno:
                            # OSError: [Errno 113] No route to host
                            if __debug__: self._log(
                                'CLOSING {}: No route to host'.format(curr_client_info.addr.result))
                            if __debug__: self._log('EXCEPTION: READ DATA FROM SOCKET: "{}", {}, {}'.format(
                                curr_client_info.addr.result, err.errno, err.strerror))
                            self._mark_connection_to_be_closed_immediately(curr_client_info)
                            ok = False
                        else:
                            if __debug__: self._log(
                                'CLOSING {}: Unknown reason'.format(curr_client_info.addr.result))
                            if __debug__: self._log('EXCEPTION: READ DATA FROM SOCKET: "{}", {}, {}'.format(
                                curr_client_info.addr.result, err.errno, err.strerror))
                            raise err
                    else:
                        if errno.WSAEHOSTUNREACH == err.errno:
                            # OSError: [Errno 113] No route to host
                            if __debug__: self._log(
                                'CLOSING {}: No route to host'.format(curr_client_info.addr.result))
                            if __debug__: self._log('EXCEPTION: READ DATA FROM SOCKET: "{}", {}, {}'.format(
                                curr_client_info.addr.result, err.errno, err.strerror))
                            self._mark_connection_to_be_closed_immediately(curr_client_info)
                            ok = False
                        else:
                            if __debug__: self._log(
                                'CLOSING {}: Unknown reason'.format(curr_client_info.addr.result))
                            if __debug__: self._log('EXCEPTION: READ DATA FROM SOCKET: "{}", {}, {}'.format(
                                curr_client_info.addr.result, err.errno, err.strerror))
                            self._mark_connection_to_be_closed_immediately(curr_client_info)
                            ok = False
                            # raise err

            read_is_forbidden = False
            if (self.global_in__data_full_size.result - self.global_in__deletable_data_full_size.result) \
                    > self.global_in__data_size_limit.result:
                read_is_forbidden = True
                ok = False

            read_is_forbidden_test = self.show_inform_about_read_stop_because_of_in_buffer_size_limit.test_trigger(
                read_is_forbidden)
            if read_is_forbidden_test is not None:
                if read_is_forbidden_test:
                    print('Read is suppressed until data will be processed.')
                else:
                    print('Read is allowed: data is processed.')

        return possible_messages_in_client_input_fifo

    # @profile
    def _read_data_from_socket(self, readable_socket: socket.socket):
        possible_messages_in_client_input_fifo = False
        if readable_socket in self._gate:
            accept_is_forbidden = True
            if (self.global_in__data_full_size.result + self.global_out__data_full_size.result) \
                    <= self.global__data_size_limit.result:
                accept_is_forbidden = False
                self._accept_new_connection(readable_socket)

            if __debug__:
                accept_is_forbidden_test = \
                    self.show_inform_about_accept_stop_because_of_all_buffers_size_limit.test_trigger(
                        accept_is_forbidden)
                if accept_is_forbidden_test is not None:
                    if accept_is_forbidden_test:
                        print('Accept is suppressed until data will be processed and/or out.')
                    else:
                        print('Accept is allowed: data is processed and/or out.')
        else:
            possible_messages_in_client_input_fifo = self._read_data_from_already_connected_socket__shell(
                readable_socket)

        return possible_messages_in_client_input_fifo

    def _log_new_connection(self, client_info: Connection, is_incoming_connection):
        connection = client_info.conn.result
        client_address = client_info.addr.result
        addr_info = client_info.addr_info
        host_names = client_info.host_names

        connection_type_string = 'OUTGOING'
        from_to = 'to'
        if is_incoming_connection:
            connection_type_string = 'INCOMING'
            from_to = 'from'

        if __debug__: self._log('New {} connection {} {}'.format(connection_type_string, from_to, client_address))
        if connection.family in {socket.AF_INET, socket.AF_INET6}:
            if __debug__: self._log('\taddr_info: {}'.format(addr_info))
            if __debug__: self._log('\thost_names: {}'.format(host_names))

    # @profile
    def _write_data_to_socket(self, curr_client_info: Connection):
        # CAUTION: code here is optimized for speed - not for readability or beauty.

        expected_client_info = curr_client_info.connected_expected_client
        writable_socket = curr_client_info.conn.result
        if curr_client_info.should_be_closed:
            curr_client_info.current_memoryview_output = None
            curr_client_info.output_to_client = copy.copy(curr_client_info.output_to_client)
            return

        ok = True
        first_pass = True
        can_call__inline_processor__on__output_buffers_are_empty = True
        while ok:
            try:
                if curr_client_info.current_memoryview_output:
                    nsent = writable_socket.send(curr_client_info.current_memoryview_output)
                    curr_client_info.current_memoryview_output = curr_client_info.current_memoryview_output[nsent:]
                else:
                    curr_client_info.current_memoryview_output = None
                    output_fifo_size = curr_client_info.output_to_client.size()
                    if output_fifo_size > 1:
                        result_data, result_size, result_qnt = \
                            curr_client_info.output_to_client.get_at_least_size(524288)
                        if result_qnt > 1:
                            curr_client_info.current_memoryview_output = memoryview(b''.join(result_data))
                        else:
                            curr_client_info.current_memoryview_output = memoryview(result_data.popleft())
                    elif output_fifo_size == 1:
                        curr_client_info.current_memoryview_output = memoryview(curr_client_info.output_to_client.get())

                    if curr_client_info.current_memoryview_output is None:
                        # if curr_client_info.ready_to_be_closed:
                        #     if first_pass:
                        #         # Т.е. если данных на отправку небыло даже при первом проходе цикла - т.е. изначально.
                        #         # Это значит что все данные были отправлены, и можно закрывать соединение.
                        #         self._output_check_sockets.remove(writable_socket)
                        #         self._mark_connection_to_be_closed_immediately(curr_client_info)
                        #     # Если соединение помечено как "Готово к закрытию" - то нам надо дождаться момента когда
                        #     # данные будут отправлены, и только в этот момент закрывать соединение. Поэтому надо
                        #     # сохранить сокет в списке проверяемых для отправки.
                        # else:
                        #     self._output_check_sockets.remove(writable_socket)
                        if not curr_client_info.ready_to_be_closed:
                            # Если соединение помечено как "Готово к закрытию" - то нам надо дождаться момента когда
                            # данные будут отправлены, и только в этот момент закрывать соединение. Поэтому надо
                            # сохранить сокет в списке проверяемых для отправки.
                            self._output_check_sockets.remove(writable_socket)
                        if first_pass and curr_client_info.ready_to_be_closed:
                            # Т.е. если данных на отправку небыло даже при первом проходе цикла - т.е. изначально.
                            # Это значит что все данные были отправлены, и можно закрывать соединение.
                            self._output_check_sockets.remove(writable_socket)
                            self._mark_connection_to_be_closed_immediately(curr_client_info)
                        ok = False
                        if expected_client_info:
                            self._io_iteration_result.clients_with_empty_output_fifo.add(
                                curr_client_info.connected_expected_client_id)
                            if curr_client_info.has_inline_processor:
                                if can_call__inline_processor__on__output_buffers_are_empty:
                                    if self._inline_processor__on__output_buffers_are_empty(curr_client_info,
                                                                                            expected_client_info):
                                        ok = True
                                    can_call__inline_processor__on__output_buffers_are_empty = False
            except BlockingIOError as err:
                ok = False
            except InterruptedError as err:
                pass
            except ConnectionError as err:
                # An established connection was aborted by the software in your host machine
                if __debug__: self._log('CLOSING {}: Connection reset by peer'.format(curr_client_info.addr.result))
                if __debug__: self._log('EXCEPTION: WRITE DATA TO SOCKET: "{}", {}, {}'.format(
                    curr_client_info.addr.result, err.errno, err.strerror))
                self._mark_connection_to_be_closed_immediately(curr_client_info)
                ok = False
            except (socket.error, OSError) as err:
                if (errno.EAGAIN == err.errno) or (errno.EWOULDBLOCK == err.errno):
                    ok = False
                elif errno.EINTR == err.errno:
                    pass
                elif err.errno in SET_OF_CONNECTION_ERRORS:
                    # Connection reset by peer
                    if __debug__: self._log(
                        'CLOSING {}: Connection reset by peer ({})'.format(curr_client_info.addr.result,
                                                                           err.strerror))
                    if __debug__: self._log('EXCEPTION: WRITE DATA TO SOCKET: "{}", {}, {}'.format(
                        curr_client_info.addr.result, err.errno, err.strerror))
                    self._mark_connection_to_be_closed_immediately(curr_client_info)
                    ok = False
                else:
                    if 'nt' == os.name:
                        if errno.WSAECONNRESET == err.errno:
                            # An existing connection was forcibly closed by the remote host
                            if __debug__: self._log(
                                'CLOSING {}: Connection reset by peer'.format(curr_client_info.addr.result))
                            if __debug__: self._log('EXCEPTION: WRITE DATA TO SOCKET: "{}", {}, {}'.format(
                                curr_client_info.addr.result, err.errno, err.strerror))
                            self._mark_connection_to_be_closed_immediately(curr_client_info)
                            ok = False
                        else:
                            raise err
                    else:
                        raise err
            first_pass = False

    def _mark_connection_to_be_closed_immediately(self, client_info: Connection):
        client_info.should_be_closed = True
        client_info.current_memoryview_input = None
        self._connections_marked_to_be_closed_immediately.add(client_info.conn.result)
        if client_info.connected_expected_client_id is not None:
            self._io_iteration_result.clients_with_disconnected_connection.add(
                client_info.connected_expected_client_id)

    def _mark_connection_as_ready_to_be_closed(self, client_info: Connection):
        client_info.ready_to_be_closed = True

    def _mark_connection_as_ready_for_deletion(self, client_info: Connection):
        client_info.ready_for_deletion = True
        self._connections_marked_as_ready_to_be_deleted.add(client_info.conn.result)

    def _handle_connection_error(self, writable_socket: socket.socket):
        # Data read from already connected client
        curr_client_id = self._connection_by_conn[writable_socket]
        curr_client_info = self._connections[curr_client_id]
        if curr_client_info.should_be_closed:
            return
        if __debug__: self._log('handling exceptional condition for {}'.format(curr_client_info.addr.result))
        self._mark_connection_to_be_closed_immediately(curr_client_info)

    # @profile
    def _read_messages_from_raw_input_into_fifo(self, curr_client_info: Connection):
        result = False

        try:
            while True:
                if curr_client_info.current_message_length is None:
                    current_message_length = curr_client_info.raw_input_from_client.get_data(self.message_size_len)
                    if current_message_length is None:
                        break

                    curr_client_info.current_message_length = int.from_bytes(current_message_length, 'little')

                current_message = curr_client_info.raw_input_from_client.get_data(
                    curr_client_info.current_message_length)
                if current_message is None:
                    break
                else:
                    curr_client_info.input_from_client.put(current_message)
                    curr_client_info.current_message_length = None
                    result = True
        except TypeError:
            pass

        return result

    def _send_message_through_connection(self, client_info: Connection, data):
        if client_info.conn.existence:
            client_info.output_to_client.put(len(data).to_bytes(self.message_size_len, 'little'))
            client_info.output_to_client.put(data)

            self._output_check_sockets.add(client_info.conn.result)
        else:
            if __debug__: self._log('ERROR: SEND MESSAGE TO CLIENT {}: "{}"'.format(client_info.addr.result, data))
            raise Exception('EXCEPTION: SEND MESSAGE TO CLIENT: Client is disconnected! You can not send data to him!')

    def _generate_list_of_messages_with_their_length(self, messages_list):
        for message in messages_list:
            yield len(message).to_bytes(self.message_size_len, 'little')
            yield message

    def _send_messages_through_connection(self, client_info: Connection, messages_list):
        if client_info.conn.existence:
            client_info.output_to_client.extend(self._generate_list_of_messages_with_their_length(messages_list))

            self._output_check_sockets.add(client_info.conn.result)
        else:
            if __debug__: self._log(
                'ERROR: SEND MESSAGES TO CLIENT {}: "{}"'.format(client_info.addr.result, messages_list))
            raise Exception('EXCEPTION: SEND MESSAGES TO CLIENT: Client is disconnected! You can not send data to him!')

    def _send_message_through_connection_raw(self, client_info: Connection, data):
        if client_info.conn.existence:
            client_info.output_to_client.put(data)
            self._output_check_sockets.add(client_info.conn.result)
        else:
            if __debug__: self._log('ERROR: SEND MESSAGE TO CLIENT {}: "{}"'.format(client_info.addr.result, data))
            raise Exception(
                'EXCEPTION: SEND MESSAGE TO CLIENT RAW: Client is disconnected! You can not send data to him!')

    def _send_messages_through_connection_raw(self, client_info: Connection, messages_list):
        if client_info.conn.existence:
            client_info.output_to_client.extend(messages_list)
            self._output_check_sockets.add(client_info.conn.result)
        else:
            if __debug__: self._log(
                'ERROR: SEND MESSAGES TO CLIENT {}: "{}"'.format(client_info.addr.result, messages_list))
            raise Exception(
                'EXCEPTION: SEND MESSAGES TO CLIENT RAW: Client is disconnected! You can not send data to him!')

    def _move_message_from_fifo_to_memoryview(self, client_info: Connection):
        if client_info.current_memoryview_output is None:
            if client_info.output_to_client.size():
                client_info.current_memoryview_output = memoryview(client_info.output_to_client.get())

    # @profile
    def _consolidate_and_move_messages_from_fifo_to_memoryview(self, client_info: Connection):
        output_fifo_size = client_info.output_to_client.size()
        if output_fifo_size > 1:
            result_data, result_size, result_qnt = \
                client_info.output_to_client.get_at_least_size(524288)
            if result_qnt > 1:
                client_info.current_memoryview_output = memoryview(b''.join(result_data))
            else:
                client_info.current_memoryview_output = memoryview(result_data.popleft())
        elif output_fifo_size == 1:
            client_info.current_memoryview_output = memoryview(client_info.output_to_client.get())

    def _process_client_keyword(self, client_socket: socket.socket):
        curr_client_id = self._connection_by_conn[client_socket]
        curr_client_info = self._connections[curr_client_id]

        if curr_client_info.input_from_client.size() >= 0:
            expected_client_id = None
            expected_client_info = None

            this_is_super_server_client = False
            if curr_client_info.connected_expected_client is not None:
                expected_client_info = curr_client_info.connected_expected_client
                expected_client_id = expected_client_info.id
                if ConnectionDirectionRole.server == expected_client_info.connection_settings.direction_role:
                    this_is_super_server_client = True

            if this_is_super_server_client:
                # This is connection to Super-Server. So we expect an answer like b'OK'
                super_server_answer__keyword_accepted = curr_client_info.input_from_client.get()
                super_server_answer__keyword_accepted = bytes(super_server_answer__keyword_accepted)
                if super_server_answer__keyword_accepted == self.server_answer__keyword_accepted:
                    # Answer was acceptable
                    self._unconfirmed_clients.remove(client_socket)
                    self._io_iteration_result.newly_connected_expected_clients.add(expected_client_id)
                    if expected_client_info.will_use_raw_client_connection:
                        curr_client_info.this_is_raw_connection = True
                else:
                    # Answer was NOT acceptable
                    self._mark_connection_to_be_closed_immediately(curr_client_info)
                    self._mark_connection_as_ready_for_deletion(curr_client_info)
                    if __debug__: self._log('ERROR: SUPER SERVER ANSWER - KEYWORD WAS NOT ACCEPTED: {}'.format(
                        super_server_answer__keyword_accepted))
            else:
                # This is connection to client. So we expect a keyword
                keyword = curr_client_info.input_from_client.get()
                keyword = bytes(keyword)
                curr_client_info.keyword = keyword
                self._unconfirmed_clients.remove(client_socket)
                self._send_message_through_connection(curr_client_info, self.server_answer__keyword_accepted)

                if keyword in self._keywords_for_expected_clients:
                    # empty expected client was already registered
                    expected_client_id = self._keywords_for_expected_clients[keyword]
                    expected_client_info = self._expected_clients[expected_client_id]
                    expected_client_info.connection_id = curr_client_id
                    expected_client_info._Client__connection = curr_client_info
                    self._conns_of_expected_clients[client_socket] = expected_client_id
                    curr_client_info.connected_expected_client_id = expected_client_id
                    curr_client_info.connected_expected_client = expected_client_info
                    self._io_iteration_result.newly_connected_expected_clients.add(expected_client_id)
                    if expected_client_info.will_use_raw_client_connection:
                        curr_client_info.this_is_raw_connection = True
                else:
                    # it is unknown expected client
                    if self.unexpected_clients_are_allowed:
                        self._add_unexpected_client(curr_client_id, keyword)
                    else:
                        self._mark_connection_to_be_closed_immediately(curr_client_info)
                        self._mark_connection_as_ready_for_deletion(curr_client_info)

    def _check_is_client_have_data_to_read_in_fifo(self, readable_socket: socket.socket):
        client_info = self._connections[self._connection_by_conn[readable_socket]]
        if client_info.connected_expected_client_id is not None:
            if client_info.input_from_client.size():
                self._io_iteration_result.clients_have_data_to_read.add(
                    client_info.connected_expected_client_id)
                if client_info.has_inline_processor:
                    self._inline_processor__on__data_received(client_info)

    def _client_have_data_to_read_in_fifo(self, readable_socket: socket.socket):
        if readable_socket in self._conns_of_expected_clients:
            expected_client_id = self._conns_of_expected_clients[readable_socket]
            expected_client = self._expected_clients[expected_client_id]
            self._io_iteration_result.clients_have_data_to_read.add(expected_client_id)
            client_info = expected_client._Client__connection
            if client_info.has_inline_processor:
                self._inline_processor__on__data_received(client_info)

    def _inline_processor__apply_parameters(self, connection_info: Connection,
                                            expected_client: Client):
        inline_processor = expected_client.obj_for_inline_processing

        inline_processor.is_in_raw_mode = inline_processor._InlineProcessor__set__is_in_raw_mode
        connection_info.this_is_raw_connection = inline_processor._InlineProcessor__set__is_in_raw_mode

        if inline_processor._InlineProcessor__set__mark_socket_as_should_be_closed_immediately:
            inline_processor._InlineProcessor__set__mark_socket_as_should_be_closed_immediately = False
            self._mark_connection_to_be_closed_immediately(connection_info)

        if inline_processor._InlineProcessor__set__mark_socket_as_ready_to_be_closed:
            inline_processor._InlineProcessor__set__mark_socket_as_ready_to_be_closed = False
            self._mark_connection_as_ready_to_be_closed(connection_info)

    def _inline_processor__init_parameters(self, connection_info: Connection,
                                           expected_client: Client):
        inline_processor = expected_client.obj_for_inline_processing

        inline_processor.is_in_raw_mode = connection_info.this_is_raw_connection
        inline_processor._InlineProcessor__set__is_in_raw_mode = connection_info.this_is_raw_connection

    def _inline_processor__on__data_received(self, connection_info: Connection):
        expected_client = connection_info.connected_expected_client
        inline_processor = expected_client.obj_for_inline_processing

        try:
            while connection_info.input_from_client.size():
                inline_processor.on__data_received(connection_info.input_from_client.get())

            if inline_processor.output_messages:
                while inline_processor.output_messages:
                    another_message = inline_processor.output_messages.popleft()
                    if not connection_info.this_is_raw_connection:
                        connection_info.output_to_client.put(
                            len(another_message).to_bytes(self.message_size_len, 'little'))
                    connection_info.output_to_client.put(another_message)
                self._output_check_sockets.add(connection_info.conn.result)
                if connection_info.output_to_client.get_data_full_size() >= 65536:
                    self._write_data_to_socket(connection_info)
                return True
        except:
            self.remove_client(expected_client.id)
            exc = sys.exc_info()
            exception = exc
            error_str = '{} {}'.format(str(exception[0]), str(exception[1].args[0]))
            formatted_traceback = traceback.format_exception(exception[0], exception[1], exception[2])
            exception = exception[:2] + (formatted_traceback,)
            trace_str = ''.join(exception[2])
            result_string = '\n\tEXCEPTION:{}\n\tTRACE:{}'.format(error_str, trace_str)
            if __debug__: self._log('EXCEPTION: INLINE PROCESSOR: ON DATA RECEIVED: {}'.format(result_string))

        return False

    def _inline_processor__on__output_buffers_are_empty(self, connection_info: Connection,
                                                        expected_client: Client):
        inline_processor = expected_client.obj_for_inline_processing

        if not connection_info.has_inline_processor:
            return False

        try:
            inline_processor.on__output_buffers_are_empty()

            if inline_processor.output_messages:
                while inline_processor.output_messages:
                    another_message = inline_processor.output_messages.popleft()
                    if not connection_info.this_is_raw_connection:
                        connection_info.output_to_client.put(
                            len(another_message).to_bytes(self.message_size_len, 'little'))
                    connection_info.output_to_client.put(another_message)
                self._output_check_sockets.add(connection_info.conn.result)
                if connection_info.output_to_client.get_data_full_size() >= 65536:
                    # self._write_data_to_socket(connection_info.conn.result)
                    self._write_data_to_socket(connection_info)
                return True
        except:
            self.remove_client(expected_client.id)
            exc = sys.exc_info()
            exception = exc
            error_str = '{} {}'.format(str(exception[0]), str(exception[1].args[0]))
            formatted_traceback = traceback.format_exception(exception[0], exception[1], exception[2])
            exception = exception[:2] + (formatted_traceback,)
            trace_str = ''.join(exception[2])
            result_string = '\n\tEXCEPTION:{}\n\tTRACE:{}'.format(error_str, trace_str)
            if __debug__: self._log(
                'EXCEPTION: INLINE PROCESSOR: ON OUTPUT BUFFERS ARE EMPTY: {}'.format(result_string))

        return False

    def _inline_processor__on__connection_lost(self, connection_info: Connection,
                                               expected_client: Client):
        inline_processor = expected_client.obj_for_inline_processing

        if not connection_info.has_inline_processor:
            return False

        try:
            inline_processor.on__connection_lost()
        except:
            exc = sys.exc_info()
            exception = exc
            error_str = '{} {}'.format(str(exception[0]), str(exception[1].args[0]))
            formatted_traceback = traceback.format_exception(exception[0], exception[1], exception[2])
            exception = exception[:2] + (formatted_traceback,)
            trace_str = ''.join(exception[2])
            result_string = '\n\tEXCEPTION:{}\n\tTRACE:{}'.format(error_str, trace_str)
            if __debug__: self._log('EXCEPTION: INLINE PROCESSOR: ON CONNECTION LOST: {}'.format(result_string))
        self.remove_client(expected_client.id)

    def _inline_processor__on__connection_lost_by_connection_id(self, connection_id):
        connection_info = self._connections[connection_id]
        expected_client_info = connection_info.connected_expected_client
        if (expected_client_info is not None) and connection_info.has_inline_processor:
            self._inline_processor__on__connection_lost(connection_info, expected_client_info)
            self._io_iteration_result.clients_with_disconnected_connection.remove(
                expected_client_info.id)

    def _unlink_good_af_unix_sockets(self):
        if 'posix' == os.name:
            for gate_connection_settings in self.gates_connections_settings:
                if gate_connection_settings.socket_family == socket.AF_UNIX:
                    try:
                        os.unlink(gate_connection_settings.socket_address)
                    except:
                        if __debug__: self._log('EXCEPTION: SERVER END: TRYING TO UNLINK GOOD AF_UNIX GATE: {}'.format(
                            gate_connection_settings.socket_address))
                        raise

    def _check_for_initial_af_unix_socket_unlink(self, connection_settings: ConnectionSettings):
        if 'posix' == os.name:
            if connection_settings.socket_family == socket.AF_UNIX:
                if os.path.exists(connection_settings.socket_address):
                    if __debug__: self._log('EXCEPTION: INITIATION: GATE: AF_UNIX SOCKET IS ALREADY EXIST: {}'.format(
                        connection_settings.socket_address))

class ThereAreNoGateConections(Exception):
    pass

class NotEnoughGateConnections(Exception):
    pass

@contextmanager
def asock_io_core_connect(asock_io_core_obj: ASockIOCore, should_have_gate_connections: bool=False, backlog: int=1,
                          should_have_all_desired_gate_connections: bool=False):
    try:
        desired_amount_of_gate_connections = len(asock_io_core_obj.gates_connections_settings)
        gate_connections_num = asock_io_core_obj.listen(backlog)
        if should_have_gate_connections and (not gate_connections_num):
            error_text = 'ERROR: CONTEXTMANAGER: BASIC INITIATION: THERE IS NO GOOD GATE CONNECTIONS!'
            asock_io_core_obj._log(error_text)
            raise ThereAreNoGateConections(error_text)
        else:
            if should_have_all_desired_gate_connections:
                if desired_amount_of_gate_connections != gate_connections_num:
                    error_text = 'ERROR: CONTEXTMANAGER: BASIC INITIATION: NOT ENOUGH GOOD GATE CONNECTIONS!'
                    asock_io_core_obj._log(error_text)
                    raise NotEnoughGateConnections(error_text)
            print('THERE ARE CREATED {} GOOD GATE CONNECTIONS'.format(gate_connections_num))
        yield asock_io_core_obj
    except:
        raise
    finally:
        asock_io_core_obj.io_iteration()
        asock_io_core_obj.destroy()
        asock_io_core_obj.io_iteration()
        if __debug__: print('RECV BUFF SIZES: {}'.format(str(asock_io_core_obj.recv_buff_sizes)[:150]))
        if __debug__: print('RECV SIZES: {}'.format(str(asock_io_core_obj.recv_sizes)[:150]))


class CheckIsRawConnection:
    def __call__(self, asock_io_core: ASockIOCore, connection_info: Connection)->bool:
        """
        :param asock_io_core:
        :param connection_info:
        :return: "True" if it is RAW connection for Unknow Client. "False" otherwise.
        """
        result = False
        try:
            if connection_info.conn.result.family in {socket.AF_INET, socket.AF_INET6}:
                if connection_info.addr.result[0] not in asock_io_core.set_of_gate_addresses:
                    # If connected not from local IP address
                    result = True
        except:
            pass
        return result
