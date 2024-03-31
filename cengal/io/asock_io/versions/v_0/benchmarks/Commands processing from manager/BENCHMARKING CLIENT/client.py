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
__version__ = "4.3.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import marshal
from cengal.help_tools import PLATFORM_NAME
from cengal.performance_test_lib.performance_test_lib import test_run_time



__author__ = 'ButenkoMS <gtalk@butenkoms.space>'

# ======================================================================
# ===================GLOBAL SETTINGS FOR ALL TESTS======================
#

CLIENT_KEYWORD = b'client'
MANAGER_CLIENT_KEYWORD = b'manager client'
CLIENT_GATE_KEYWORD = b'client gate'
CLIENT_GATE_ADDRESS = ('localhost', 23230)
CLIENT_GATE_ADDRESS_AF_UNIX = 'benchmark_server.af_unix.socket'

SERVER_KEYWORD = b'http server'
SERVER_ADDRESS = ('localhost', 25000)
SERVER_ADDRESS_AF_UNIX = 'server.af_unix.socket'

BSC__ITERATIONS_QNT = 100000
# BSC__DATA = '0'
BSC__DATA = 'hello world'
# BSC__DATA = ' ' + 'h' * (1024 - 1)
if len(BSC__DATA) > 512:
    BSC__DATA = BSC__DATA[:-19]
BSC__COMMAND = ('do', BSC__DATA)
BSC__COMPACT_COMMAND = marshal.dumps(BSC__COMMAND)
BSC__RESULT_COMPACT_COMMAND_RAW_SIZE = len(BSC__COMPACT_COMMAND)
BSC__RESULT_COMPACT_COMMAND_FULL_SIZE = BSC__RESULT_COMPACT_COMMAND_RAW_SIZE + 8
BSC__CLOSE_COMMAND = ('server command', 'shut down')
BSC__COMPACT_CLOSE_COMMAND = marshal.dumps(BSC__CLOSE_COMMAND)

print('MESSAGE RAW SIZE: {}'.format(BSC__RESULT_COMPACT_COMMAND_RAW_SIZE))
print('MESSAGE FULL SIZE: {}'.format(BSC__RESULT_COMPACT_COMMAND_FULL_SIZE))

BSC__IO_ITERATION_TIMEOUT = 0.5

BSC__SLEEP_TIME = 0.5

BSC__MPR = 1  # Количество одновременно отправляемых Тупым Клиентом сообщений (в других клиентах не используется)

BSC__USE_UNIX_SOCKET_ON_CLIENT = True
if 'PyPy' == PLATFORM_NAME:
    BSC__USE_UNIX_SOCKET_ON_CLIENT = False
BSC__USE_UNIX_SOCKET_ON_CLIENT = False

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


def run_non_blocking_server_benchmarking_client():
    # CREATE CLIENT
    tcp_app_server = ASockIOCore(set())

    # SET CLIENT SETTINGS
    tcp_app_server.use_nodelay_inet = BSC__USE_NODELAY_INET
    tcp_app_server.use_speed_optimized_socket_read = BSC__USE_READ_WITH_FIXED_BUFFER
    tcp_app_server.socket_read_fixed_buffer_size.result = BSC__SOCKET_READ_FIXED_BUFFER_SIZE

    # START CLIENT
    with asock_io_core_connect(tcp_app_server) as server:
        # REGISTER CONNECTION TO SUPER SERVER
        super_server_tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS,
                                                       MANAGER_CLIENT_KEYWORD)
        #   If AF_UNIX is allowed and this is Unix-like os
        if BSC__USE_UNIX_SOCKET_ON_CLIENT:
            if 'posix' == os.name:
                super_server_tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS_AF_UNIX,
                                                               MANAGER_CLIENT_KEYWORD, socket.AF_UNIX,
                                                               socket.SOCK_STREAM)
        super_server_info = Client(super_server_tcp_settings)
        super_server_id = server.add_client(super_server_info)
        super_server_connected = False
        shut_down = False

        # WAITING FOR CONNECTION TO SUPER SERVER
        while not super_server_connected:
            io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)

            if not super_server_connected:
                if super_server_id in io_iteration_result.newly_connected_expected_clients:
                    super_server_connected = True

        # THIS CLIENT HAS BEEN CONNECTED TO SUPER SERVER
        if super_server_connected:
            # BENCHMARKING FULL IO CYCLE
            with test_run_time('Full loop', BSC__ITERATIONS_QNT) as full_index:
                full_index.result = 0

                # BENCHMARKING CREATION OF OUTPUT MESSAGES LIST
                with test_run_time('Adding data to output FIFO', BSC__ITERATIONS_QNT) as index:
                    try:
                        server.send_messages_to_client(
                            super_server_id, [BSC__COMPACT_COMMAND for index in range(index.result)])
                    except Exception as err:
                        print(err, flush=True)
                    index.result = 0

                # BENCHMARKING IO ONLY
                with test_run_time('Data IO loop', BSC__ITERATIONS_QNT) as index:
                    while (not shut_down) and (index.result > 0):
                        io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)

                        if super_server_id in io_iteration_result.clients_with_disconnected_connection:
                            print('Super server has been disconnected - Shut down benchmark client', flush=True)
                            shut_down = True
                            break
                        if super_server_id in io_iteration_result.clients_have_data_to_read:
                            for compact_command in server.get_messages_from_client(super_server_id):
                                index.result -= 1

            # SENDING SHUT DOWN COMMAND TO SUPER SERVER
            if not shut_down:
                server.send_message_to_client(super_server_id, BSC__COMPACT_CLOSE_COMMAND)
                while not shut_down:
                    io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)

                    if super_server_id in io_iteration_result.clients_with_disconnected_connection:
                        print('Super server has been successfully disconnected - Shut down benchmark client',
                              flush=True)
                        shut_down = True
                        break
    print('Client has been Shut Down.')


def make_af_unix_names():
    if 'posix' == os.name:
        global CLIENT_GATE_ADDRESS_AF_UNIX
        CLIENT_GATE_ADDRESS_AF_UNIX = os.path.join(os.getcwd(), CLIENT_GATE_ADDRESS_AF_UNIX)
        print(CLIENT_GATE_ADDRESS_AF_UNIX)
        print()


def main():
    make_af_unix_names()
    run_non_blocking_server_benchmarking_client()


if __name__ == '__main__':
    main()
