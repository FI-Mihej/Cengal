#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.1.12"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import marshal
from asock_io.asock_io_core import *



__author__ = 'ButenkoMS <gtalk@butenkoms.space>'


# ======================================================================
# ===================GLOBAL SETTINGS FOR ALL TESTS======================
#

CLIENT_KEYWORD = b'client'
MANAGER_CLIENT_KEYWORD = b'manager client'

SERVER_KEYWORD = b'http server'
SERVER_ADDRESS = ('localhost', 25000)
SERVER_ADDRESS_AF_UNIX = 'server.af_unix.socket'

BSC__USE_READ_WITH_FIXED_BUFFER = True  # "Optimized for speed". Good for Named Clients.
# BSC__USE_READ_WITH_FIXED_BUFFER = False  # "Optimized for memory". Good for big amount of Unknown Clients (raw,
# http, etc.) if you have small server.

BSC__SOCKET_READ_FIXED_BUFFER_SIZE = 1024 ** 2

BSC__USE_NODELAY_INET = True

BSC__REUSE_GATE_ADDR = True

BSC__REUSE_GATE_PORT = False  # Do not use 'True' with this server: there is two different connections per single client
# and they both should be connected to the same server process - not to different server processes!

LINE_TRACE_ALLOWED = True

#
# ===================GLOBAL SETTINGS FOR ALL TESTS======================
# ======================================================================


class RawClientCheckerAllRaw(CheckIsRawConnection):
    def __call__(self, app_server: ASockIOCore, client_info: Connection):
        return True


def run_server():
    io_iteration_timeout = 0.5

    # ADD SERVER GATE CONNECTIONS
    set_of_tcp_settings = set()
    #   Add gate connection for AF_INET:
    tcp_settings = ConnectionSettings(ConnectionType.passive, SERVER_ADDRESS, SERVER_KEYWORD)
    set_of_tcp_settings.add(tcp_settings)
    #   Add gate connection for AF_UNIX:
    if 'posix' == os.name:
        tcp_settings = ConnectionSettings(ConnectionType.passive, SERVER_ADDRESS_AF_UNIX, SERVER_KEYWORD,
                                          socket.AF_UNIX, socket.SOCK_STREAM)
        set_of_tcp_settings.add(tcp_settings)

    # CREATE SERVER
    tcp_app_server = ASockIOCore(set_of_tcp_settings)

    # SET SERVER SETTINGS
    tcp_app_server.use_nodelay_inet = BSC__USE_NODELAY_INET
    tcp_app_server.use_speed_optimized_socket_read = BSC__USE_READ_WITH_FIXED_BUFFER
    tcp_app_server.reuse_gate_addr = BSC__REUSE_GATE_ADDR
    tcp_app_server.reuse_gate_port = BSC__REUSE_GATE_PORT
    tcp_app_server.socket_read_fixed_buffer_size.result = BSC__SOCKET_READ_FIXED_BUFFER_SIZE

    # START SERVER
    with asock_io_core_connect(tcp_app_server, True) as server:
        # REGISTER INCOMING MANAGER
        manager_client_tcp_settings = ConnectionSettings(ConnectionType.active_connected, keyword=MANAGER_CLIENT_KEYWORD)
        manager_client_info = Client(manager_client_tcp_settings)
        manager_client_id = server.add_client(manager_client_info)

        # REGISTER INCOMING ORDINARY CLIENT
        another_client_tcp_settings = ConnectionSettings(ConnectionType.active_connected, keyword=CLIENT_KEYWORD)
        another_client_info = Client(another_client_tcp_settings)
        server.add_client(another_client_info)

        # RUN SERVER LOOP
        shut_down = False
        while not shut_down:
            io_iteration_result = server.io_iteration(io_iteration_timeout)

            # CLIENT CLOSED
            for another_client_id in io_iteration_result.clients_with_disconnected_connection:
                if another_client_id == manager_client_id:
                    print('Manager client had been disconnected - Shut down server')
                    shut_down = True
                else:
                    print('Client "{}" has been disconnected'.format(
                        server.get_client_info(another_client_id).connection_settings.keyword))

            # CLIENT CONNECTED
            for another_client_id in io_iteration_result.newly_connected_expected_clients:
                if another_client_id == manager_client_id:
                    print('Manager client has been connected')
                else:
                    print('Client "{}" has been connected'.format(
                        server.get_client_info(another_client_id).connection_settings.keyword))

            # CLIENT HAVE DATA TO READ
            for another_client_id in io_iteration_result.clients_have_data_to_read:
                if another_client_id == manager_client_id:
                    shut_down = on__manager_data_in(another_client_id, server, shut_down)
                else:
                    shut_down = on__ordinary_client_data_in(another_client_id, server, shut_down)

    print('Server has been Shut Down.')


def working_function(data_string: str)->str:
    return data_string.upper()


def on__manager_data_in(client_id, server, shut_down):
    list_of_answers = list()
    for compact_command in server.get_messages_from_client(client_id):
        command = marshal.loads(compact_command)
        if 'server command' == command[0]:
            if 'shut down' == command[1]:
                print('Shut Down command from manager!')
                shut_down = True
        elif 'do' == command[0]:
            data = command[1]
            output_data = working_function(data)
            output_data = marshal.dumps(output_data)
            list_of_answers.append(output_data)
    try:
        server.send_messages_to_client(client_id, list_of_answers)
    except Exception as err:
        print(err)

    return shut_down


def on__ordinary_client_data_in(client_id, server, shut_down):
    list_of_answers = list()
    for message_data in server.get_messages_from_client(client_id):
        list_of_answers.append(message_data)
    try:
        server.send_messages_to_client(client_id, list_of_answers)
    except Exception as err:
        print(err)

    return shut_down


def make_af_unix_names():
    if 'posix' == os.name:
        global SERVER_ADDRESS_AF_UNIX
        SERVER_ADDRESS_AF_UNIX = os.path.join(os.getcwd(), SERVER_ADDRESS_AF_UNIX)
        print(SERVER_ADDRESS_AF_UNIX)
        print()


def main():
    make_af_unix_names()
    run_server()


if __name__ == '__main__':
    main()
