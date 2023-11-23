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

import select
from ..abstract import *

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


class IOLoopSelect(IOLoopBase):
    def __init__(self, interface: NetIOBase):
        super().__init__(interface)
        self._input_check_sockets = set()
        self._output_check_sockets = set()
        self._exception_check_sockets = set()
        self.select = select.select

    def loop_iteration(self, timeout=-1):
        if not self._input_check_sockets:
            return

        readable, writable, exceptional = select.select(self._input_check_sockets,
                                                        self._output_check_sockets,
                                                        self._exception_check_sockets,
                                                        timeout)

        # READ
        read_is_forbidden = True
        if (self.interface.global_in__data_full_size.result - self.interface.global_in__deletable_data_full_size.result) \
                <= self.interface.global_in__data_size_limit.result:
            read_is_forbidden = False

            # Handle inputs
            for fileno in readable:
                connection = self.interface.connection_by_fileno[fileno]
                # Read available. We can try to read event even if an error occurred
                if ConnectionType.passive == connection.connection_info.connection_type:
                    self.interface.on_accept_connection(connection)
                else:
                    self.interface.on_read(connection)
                # read_result = self._read_data_from_socket(s)
                # if read_result:
                #     # read_result = self._read_messages_from_raw_input_into_fifo(s)
                #     # if read_result:
                #     if s in self._unconfirmed_clients:
                #         self._process_client_keyword(s)
                #         self._check_is_client_have_data_to_read_in_fifo(s)
                #     else:
                #         self._client_have_data_to_read_in_fifo(s)

        if __debug__:
            read_is_forbidden_test = self.interface.show_inform_about_read_stop_because_of_in_buffer_size_limit.test_trigger(
                    read_is_forbidden)
            if read_is_forbidden_test is not None:
                if read_is_forbidden_test:
                    print('Read is suppressed until data will be processed.')
                else:
                    print('Read is allowed: data is processed.')
        # WRITE
        # Handle outputs
        for fileno in writable:
            curr_client_info = self._connections[self._connection_by_conn[s]]
            self._write_data_to_socket(curr_client_info)
            # self._write_data_to_socket(s)

        # =================

        events = self.epoll.poll(timeout)
        for fileno, event in events:
            connection = self.interface.connection_by_fileno[fileno]

            if event & select.EPOLLIN:
                # Read available. We can try to read event even if an error occurred
                if ConnectionType.passive == connection.connection_info.connection_type:
                    self.interface.on_accept_connection(connection)
                else:
                    self.interface.on_read(connection)

            if event & select.EPOLLHUP:
                # Some error. Connection should be closed
                self.should_be_closed.add(connection.conn)
            elif event & select.EPOLLOUT:
                # Write available. We will not write data if an error occurred
                if ConnectionState.waiting_for_connection == connection.connection_state:
                    if not connection.conn.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR):
                        # Connected successfully:
                        self.interface.on_connected(connection)
                    else:
                        # Some connection error - will be closed:
                        self.should_be_closed.add(connection.conn)
                else:
                    self.interface.on_write(connection)

            self._close_all()

    def _close_all(self):
        should_be_closed = self.should_be_closed
        self.should_be_closed = set()
        for conn in should_be_closed:
            if conn.fileno() in self.interface.connection_by_fileno:
                connection = self.interface.connection_by_fileno[conn.fileno()]
                self.interface.on_close(connection)  # self.remove_connection() should be run from inside of this
                #   callback
            else:
                self.remove_connection(conn)

    def destroy(self):
        self._close_all()
        self.epoll.close()

    def add_connection(self, conn: socket.socket):
        self.epoll.register(conn.fileno(), select.EPOLLIN)

    def remove_connection(self, conn: socket.socket):
        self.epoll.unregister(conn.fileno())

    def set__need_write(self, conn: socket.socket, state=True):
        if state:
            self.epoll.modify(conn.fileno(), select.EPOLLIN | select.EPOLLOUT)
        else:
            self.epoll.modify(conn.fileno(), select.EPOLLIN)

    def set__should_be_closed(self, conn: socket.socket):
        self.should_be_closed.add(conn)
