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

from .net_io_abstract import *
import sys
import traceback

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


class NetIO(NetIOBase):
    def __init__(self, transport):
        super().__init__(transport)

        self._need_to_stop = False
        self._already_begun = False

        self._new_connection_id = 0

        self.need_to_print_exceptions_info = False

    def destroy(self):
        self.method.destroy()

    def start(self, destroy_on_finish=True):
        if self._already_begun:
            raise LoopIsAlreadyBegun()

        self._already_begun = True
        try:
            while not self._need_to_stop:
                self.method.loop_iteration()
        finally:
            self._already_begun = False
            if destroy_on_finish:
                self.destroy()

    def stop(self):
        self._need_to_stop = True

    def make_connection(self, connection_info: ConnectionInfo=None, name=None)->Connection:
        new_connection = None
        if ConnectionType.passive == connection_info.connection_type:
            new_connection = self._make_passive_connection(connection_info, name)
        elif ConnectionType.active_connected == connection_info.connection_type:
            new_connection = self._make_active_connected_connection(connection_info, name)
        else:
            raise WrongConnectionType()
        return new_connection

    def add_connection(self, connection: Connection):
        self.all_connections.add(connection)
        if ConnectionType.passive == connection.connection_info.connection_type:
            self.passive_connections.add(connection)
        self.connection_by_id[connection.connection_id] = connection
        if connection.connection_name is not None:
            self.connection_by_name[connection.connection_name] = connection
        self.connection_by_fileno[connection.conn.fileno()] = connection

        if connection.worker_obj.api is None:
            connection.worker_obj.api = self
        if connection.worker_obj.connection is None:
            connection.worker_obj.connection = connection

        self.method.add_connection(connection.conn)
        self.check_is_connection_need_to_sent_data(connection)

    def remove_connection(self, connection: Connection):
        connection.connection_state = ConnectionState.waiting_for_disconnection
        self.method.set__should_be_closed(connection.conn)

    def on_accept_connection(self, connection):
        new_conn = None
        try:
            conn_and_address_pair = connection.conn.accept()
            new_conn, new_address = conn_and_address_pair
            new_connection = self._construct_active_accepted_connection(connection, conn_and_address_pair)
            self.add_connection(new_connection)
            try:
                new_connection.worker_obj.on_connect()
                self.check_is_connection_need_to_sent_data(new_connection)
            except:
                if __debug__: self.log_exception()
                self._set_connection_to_be_closed(new_connection, ConnectionState.worker_fault)
        except BlockingIOError:
            pass
        except:
            if __debug__: self.log_exception()
            if new_conn is not None:
                self.method.should_be_closed.add(new_conn)

    def on_connected(self, connection: Connection):
        connection.connection_state = ConnectionState.connected
        try:
            connection.worker_obj.on_connect()
            self.check_is_connection_need_to_sent_data(connection)
        except:
            if __debug__: self.log_exception()
            self._set_connection_to_be_closed(connection, ConnectionState.worker_fault)

    def on_read(self, connection: Connection):
        try:
            another_read_data_part = connection.conn.recv(1024)
            if another_read_data_part:
                connection.read_data += another_read_data_part
                try:
                    connection.worker_obj.on_read()
                    self.check_is_connection_need_to_sent_data(connection)
                except:
                    if __debug__: self.log_exception()
                    self._set_connection_to_be_closed(connection, ConnectionState.worker_fault)
            else:
                self._set_connection_to_be_closed(connection, ConnectionState.io_fault)
        except BlockingIOError:
            pass
        except:
            if __debug__: self.log_exception()
            self._set_connection_to_be_closed(connection, ConnectionState.io_fault)

    def on_write(self, connection: Connection):
        try:
            if connection.must_be_written_data:
                nsent = connection.conn.send(connection.must_be_written_data)
                connection.must_be_written_data = connection.must_be_written_data[nsent:]
            if not connection.must_be_written_data:
                try:
                    connection.worker_obj.on_no_more_data_to_write()
                    self.check_is_connection_need_to_sent_data(connection)
                except:
                    if __debug__: self.log_exception()
                    self._set_connection_to_be_closed(connection, ConnectionState.worker_fault)
        except BlockingIOError:
            pass
        except:
            if __debug__: self.log_exception()
            self._set_connection_to_be_closed(connection, ConnectionState.io_fault)

    def on_close(self, connection: Connection):
        self._remove_connection_from_internal_structures(connection)
        connection.conn.close()
        connection.connection_state = ConnectionState.disconnected
        try:
            connection.worker_obj.on_connection_lost()
        except:
            if __debug__: self.log_exception()
            pass

    def _get_new_connection_id(self):
        result = self._new_connection_id
        self._new_connection_id += 1
        return result

    def _construct_active_accepted_connection(self, base_passive_connection: Connection,
                                              conn_and_address_pair: tuple):
        conn, address = conn_and_address_pair
        new_worker_obj = copy.copy(base_passive_connection.worker_obj)
        new_worker_obj.api = None
        new_worker_obj.connection = None
        new_connection_info = ConnectionInfo(new_worker_obj,
                                             ConnectionType.active_accepted,
                                             address, conn.family, conn.type, conn.proto)
        new_connection = Connection(self._get_new_connection_id(), new_connection_info, conn_and_address_pair,
                                    ConnectionState.connected)
        return new_connection

    def _make_active_connected_connection(self, connection_info: ConnectionInfo=None, name=None)->Connection:
        conn = None
        try:
            conn = socket.socket(connection_info.socket_family, connection_info.socket_type,
                                 connection_info.socket_protocol, connection_info.socket_fileno)
            conn.setblocking(0)
            conn.connect(connection_info.socket_address)
        except (socket.error, OSError) as err:
            if err.errno not in {errno.EINPROGRESS, errno.EAGAIN}:
                conn.close()
                raise err
        conn_and_address_pair = (conn, connection_info.socket_address)
        new_connection = Connection(self._get_new_connection_id(), connection_info, conn_and_address_pair,
                                    ConnectionState.waiting_for_connection, name)
        self.add_connection(new_connection)
        self.method.set__need_write(new_connection.conn, True)
        return new_connection

    def _make_passive_connection(self, connection_info: ConnectionInfo=None, name=None)->Connection:
        conn = None
        try:
            conn = socket.socket(connection_info.socket_family, connection_info.socket_type,
                                 connection_info.socket_protocol, connection_info.socket_fileno)
            conn.setblocking(0)
            conn.bind(connection_info.socket_address)
            conn.listen(connection_info.backlog)
        except:
            conn.close()
            raise
        conn_and_address_pair = (conn, connection_info.socket_address)
        new_connection = Connection(self._get_new_connection_id(), connection_info, conn_and_address_pair,
                                    ConnectionState.connected, name)
        self.add_connection(new_connection)

        try:
            new_connection.worker_obj.on_connect()
            self.check_is_connection_need_to_sent_data(new_connection)
        except:
            if __debug__: self.log_exception()
            self._set_connection_to_be_closed(new_connection, ConnectionState.worker_fault)

        return new_connection

    def _remove_connection_from_internal_structures(self, connection: Connection):
        if connection in self.all_connections:
            self.all_connections.remove(connection)
        if connection in self.passive_connections:
            self.passive_connections.remove(connection)
        if connection.connection_id in self.connection_by_id:
            del self.connection_by_id[connection.connection_id]
        if connection.connection_name is not None:
            if connection.connection_name in self.connection_by_name:
                del self.connection_by_name[connection.connection_name]
        if connection.conn.fileno() in self.connection_by_fileno:
            del self.connection_by_fileno[connection.conn.fileno()]
        self.method.remove_connection(connection.conn)

    def _set_connection_to_be_closed(self, connection: Connection, state: ConnectionState):
        connection.connection_state = state
        self.method.set__should_be_closed(connection.conn)

    def check_is_connection_need_to_sent_data(self, connection: Connection):
        if connection.must_be_written_data or connection.force_write_call:
            if not isinstance(connection.must_be_written_data, memoryview):
                connection.must_be_written_data = memoryview(connection.must_be_written_data)
            self.method.set__need_write(connection.conn, True)
        else:
            self.method.set__need_write(connection.conn, False)

    def log_exception(self):
        if not self.need_to_print_exceptions_info:
            return
        exc = sys.exc_info()
        exception = exc
        error_str = '{} {}'.format(str(exception[0]), str(exception[1].args[0]))
        formatted_traceback = traceback.format_exception(exception[0], exception[1], exception[2])
        exception = exception[:2] + (formatted_traceback,)
        trace_str = ''.join(exception[2])
        result_string = '\n\tEXCEPTION:{}\n\tTRACE:{}'.format(error_str, trace_str)
        print(result_string)
