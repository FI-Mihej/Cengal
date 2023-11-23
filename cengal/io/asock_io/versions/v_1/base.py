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

import errno
import socket

from cengal.base.classes import BaseClassSettings
from cengal.code_flow_control.smart_values.versions.v_0 import ResultExistence
from cengal.data_containers.dynamic_list_of_pieces import \
    DynamicListOfPiecesDequeWithLengthControl
from cengal.data_containers.fast_fifo import FIFODequeWithLengthControl
from cengal.hardware.info.cpu.versions.v_0 import l2_cache_per_core

from .abstract import *
from .recv_buff_size_computer import RecvBuffSizeComputer

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


SET_OF_CONNECTION_ERRORS = {errno.ECONNRESET, errno.ECONNREFUSED, errno.ECONNABORTED, errno.EPIPE, errno.ESHUTDOWN}
INET_TYPE_CONNECTIONS = {socket.AF_INET, socket.AF_INET6}


try:
    BlockingIOError
except NameError:
    class BlockingIOError(OSError):
        pass

try:
    InterruptedError
except NameError:
    class InterruptedError(OSError):
        pass

try:
    ConnectionError
except NameError:
    class ConnectionError(OSError):
        pass

try:
    BrokenPipeError
except NameError:
    class BrokenPipeError(ConnectionError):
        pass

try:
    ConnectionAbortedError
except NameError:
    class ConnectionAbortedError(ConnectionError):
        pass

try:
    ConnectionRefusedError
except NameError:
    class ConnectionRefusedError(ConnectionError):
        pass

try:
    ConnectionResetError
except NameError:
    class ConnectionResetError(ConnectionError):
        pass


class InternalNotCriticalError(Exception):
    pass


MESSAGE_SIZE_LEN = 8
SERVER_ANSWER__KEYWORD_ACCEPTED = b'OK'


class SimpleNetworkError(Exception):
    pass


class ConnectionSettings(BaseClassSettings):
    def __init__(self,
                 connection_type: ConnectionType,
                 socket_address=None,
                 keyword: bytes = None,
                 socket_family=socket.AF_INET,
                 socket_type=socket.SOCK_STREAM,
                 socket_protocol=0,
                 socket_fileno=None,
                 backlog=0,
                 non_socket_connection_settings: NonSocketConnectionSettings = None):
        """
        :param connection_type: ConnectionType()
        :param socket_address: './main.server.AF_UNIX.socket', ('localhost', 8080), ('::', 50007, 0, 0), , ect.
        :param keyword: b'sdlkfj s894 saf 84ewksdhf sdf'. Can be None for a Super Server
        :param socket_family: AF_INET (the default), AF_INET6, AF_UNIX, AF_CAN or AF_RDS
        :param socket_type: SOCK_STREAM (the default), SOCK_DGRAM, SOCK_RAW or perhaps one of the other SOCK_ constants
        :param socket_protocol: in the case where the address family is AF_CAN the protocol should be one of CAN_RAW or
            CAN_BCM
        :param socket_fileno: If fileno is specified, the other arguments are ignored, causing the socket with the
            specified file descriptor to return
        """
        self.connection_type = connection_type
        self.keyword = keyword
        self.socket_address = socket_address
        self.socket_family = socket_family
        self.socket_type = socket_type
        self.socket_protocol = socket_protocol
        self.socket_fileno = socket_fileno
        self.backlog = backlog
        self.non_socket_connection_settings = non_socket_connection_settings
        self.expected_clients_with_empty_output_fifo = set()


class IOCoreMemoryManagement:
    def __init__(self):
        self.global__data_size_limit = ResultExistence(True, 2 * 1024**3)

        self.global_in__data_size_limit = ResultExistence(True, 512 * 1024**2)
        self.global_in__data_full_size = ResultExistence(True, 0)
        self.global_in__deletable_data_full_size = ResultExistence(True, 0)

        self.global_out__data_size_limit = ResultExistence(True, 512 * 1024**2)
        self.global_out__data_full_size = ResultExistence(True, 0)
        self.global_out__deletable_data_full_size = ResultExistence(True, 0)

    def link_to(self, parent):
        self.global__data_size_limit = parent.global__data_size_limit

        self.global_in__data_size_limit = parent.global_in__data_size_limit
        self.global_in__data_full_size = parent.global_in__data_full_size
        self.global_in__deletable_data_full_size = parent.global_in__deletable_data_full_size

        self.global_out__data_size_limit = parent.global_out__data_size_limit
        self.global_out__data_full_size = parent.global_out__data_full_size
        self.global_out__deletable_data_full_size = parent.global_out__deletable_data_full_size


class ASockIOCoreMemoryManagement(IOCoreMemoryManagement):
    def __init__(self):
        super(ASockIOCoreMemoryManagement, self).__init__()

        self.socket_read_fixed_buffer_size = ResultExistence(True,
                                                             int(l2_cache_per_core() / 2) or 1024 ** 2)
        # 1024**2 is the fastest fixed read buffer on my CPU.
        # Also ingeneral, it should be the half of the CPU cache per core (UPD: I don't remember why. Maybe to save other memory to instructions when we are dealing with big amount of connections).
        #
        # My CPU is Intel Core i5 3570:
        # Architecture	x86-64
        # Threads	4 threads
        # L2 cache	1 MB
        # L2 cache per core	0.25 MB/core
        # L3 cache	6 MB
        # L3 cache per core	1.5 MB/core

    def link_to(self, parent):
        super(ASockIOCoreMemoryManagement, self).link_to(parent)
        try:
            self.socket_read_fixed_buffer_size = parent.socket_read_fixed_buffer_size
        except AttributeError:
            pass


class Connection:
    def __init__(self,
                 connection_id=None,
                 connection_settings: ConnectionSettings = None,
                 connection__conn_addr: tuple = None,
                 connection_state: ConnectionState = None,
                 global_memory_management: ASockIOCoreMemoryManagement = None
                 ):
        """

        :param connection_id: ID for this connection
        :param connection__conn_addr: tuple(conn, addr) where conn is a socket, addr is an address
        :param global_memory_management: global memory management obj
        """
        self.id = connection_id
        self.connection_settings = connection_settings
        if connection__conn_addr is None:
            self.conn = ResultExistence(False, None)
            self.addr = ResultExistence(False, None)
        else:
            self.conn = ResultExistence(True, connection__conn_addr[0])
            self.addr = ResultExistence(True, connection__conn_addr[1])
        self.connection_state = connection_state

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

        self.current_input_memoryview = None
        self.current_input_memoryview_offset = 0
        self.current_input_memoryview_nbytes = 0
        self.current_input_memoryview_diff = 0
        self.current_input_memoryview_message_nbytes = 0
        self.raw_input_from_client = DynamicListOfPiecesDequeWithLengthControl(
            external_data_length=global_memory_management.global_in__data_full_size)
        self.current_message_length = None  # length of current input message (or None, if size waw not read yet)
        self.input_from_client = FIFODequeWithLengthControl(
            external_data_full_size=global_memory_management.global_in__data_full_size)

        self.current_output_memoryview = None
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

    def add_data_to_output_buffer(self, data):
        pass

    def add_data_to_input_buffer(self, data):
        pass


class InlineProcessor(InlineWorkerBase):
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
        super(InlineProcessor, self).__init__(client_id, keyword, socket_family, socket_type, socket_proto,
                                              addr_info, host_names, external_parameters_set_trigger)

        self.__hold__client_id = client_id
        self.__set__is_in_raw_mode = False
        self.__set__mark_socket_as_should_be_closed_immediately = False
        self.__set__mark_socket_as_ready_to_be_closed = False
        self.__external_parameters_set_trigger = external_parameters_set_trigger

    def set__is_in_raw_mode(self, is_in_raw_mode: bool):
        self.__set__is_in_raw_mode = is_in_raw_mode
        self.__external_parameters_set_trigger.add(self.__hold__client_id)

    def mark__socket_as_should_be_closed_immediately(self, mark_socket_as: bool):
        self.__set__mark_socket_as_should_be_closed_immediately = mark_socket_as
        self.__external_parameters_set_trigger.add(self.__hold__client_id)

    def mark__socket_as_ready_to_be_closed(self, mark_socket_as: bool):
        self.__set__mark_socket_as_ready_to_be_closed = mark_socket_as
        self.__external_parameters_set_trigger.add(self.__hold__client_id)

    def __getstate__(self):
        return self.client_id, self.keyword, self.socket_family, self.socket_type, self.socket_proto, self.addr_info, \
            self.host_names, self.is_in_raw_mode, self.__hold__client_id, self.__set__is_in_raw_mode, \
            self.__set__mark_socket_as_should_be_closed_immediately, self.__set__mark_socket_as_ready_to_be_closed, \
            self.__external_parameters_set_trigger, self.output_messages

    def __setstate__(self, state):
        self.client_id, self.keyword, self.socket_family, self.socket_type, self.socket_proto, self.addr_info, \
            self.host_names, self.is_in_raw_mode, self.__hold__client_id, self.__set__is_in_raw_mode, \
            self.__set__mark_socket_as_should_be_closed_immediately, self.__set__mark_socket_as_ready_to_be_closed, \
            self.__external_parameters_set_trigger, self.output_messages = state


class Client:
    def __init__(self, connection_settings: ConnectionSettings, client_id=None, connection_id=None):
        """ Dasdfd safd

        :param client_id: ID of the expected client
        :param connection_id: ID of the connection
        :param connection_settings: useful ConnectionSettings parameters are {connection_type, keyword} - for a client,
            and all - for the super server.

        """

        self.id = client_id
        self.connection_id = connection_id
        # self.__connection = None  # Нельзя! Потому что в этом случае, объект клиента станет несериализуемым
        self.__connection = None  # Можно! Сделаем сериализуемым через переопределение магических методов
        self.connection_settings = connection_settings
        self.connection_settings.check()

        self.will_use_raw_client_connection = False
        self.will_use_raw_connection_without_handshake = False
        self.this_is_unknown_client = False

        self.obj_for_inline_processing = None

    def __getstate__(self):
        # data_for_pickling = (
        #     self.id,
        #     self.connection_id,
        #     self.connection_settings,
        #     self.will_use_raw_client_connection,
        #     self.will_use_raw_connection_without_handshake,
        #     self.this_is_unknown_client,
        #     self.obj_for_inline_processing
        # )
        # return data_for_pickling
        return self.id, \
            self.connection_id, \
            self.connection_settings, \
            self.will_use_raw_client_connection, \
            self.will_use_raw_connection_without_handshake, \
            self.this_is_unknown_client, \
            self.obj_for_inline_processing

    def __setstate__(self, data_after_unpickling):
        self.id, self.connection_id, self.connection_settings, self.will_use_raw_client_connection, \
            self.will_use_raw_connection_without_handshake, self.this_is_unknown_client, \
            self.obj_for_inline_processing = data_after_unpickling

        self.__connection = None


class CheckIsRawConnection:
    def __call__(self, asock_io_core: 'ASockIOCore', connection_info: Connection) -> bool:
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
