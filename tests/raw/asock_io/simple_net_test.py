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
__version__ = "3.1.14"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import cProfile
import pstats
import os
from cengal.testing_lib.tests_list_runner import TestsRunner
from cengal.performance_test_lib.performance_test_lib import test_run_time
import marshal
from time import sleep
from cengal.help_tools import PLATFORM_NAME
from cengal.code_inspection import LineTracer, set_profiler, profiler_result
import httptools


# ALLOW_PROFILE = True
ALLOW_PROFILE = False

set_profiler(ALLOW_PROFILE)




__author__ = 'ButenkoMS <gtalk@butenkoms.space>'


CLIENT_KEYWORD = b'client'
MANAGER_CLIENT_KEYWORD = b'manager client'
BENCHMARK_SERVER_KEYWORD = b'benchmark server'
BENCHMARK_SERVER_ADDRESS = ('localhost', 19495)
BENCHMARK_SERVER_ADDRESS_AF_UNIX = 'benchmark_server.af_unix.socket'
SERVER_KEYWORD = b'server'
SERVER_ADDRESS = ('localhost', 18495)
# SERVER_ADDRESS = ('136.243.105.170', 18495)
SERVER_ADDRESS_AF_UNIX = 'server.af_unix.socket'

_SET_OF_CONNECTION_ERRORS = {errno.ECONNRESET, errno.ECONNREFUSED, errno.ECONNABORTED, errno.EPIPE, errno.ESHUTDOWN}
_INET_TYPE_CONNECTIONS = {socket.AF_INET, socket.AF_INET6}


# ======================================================================
# ===================BENCHMARK_SERVER_CLIENT SETTINGS===================
#
BSC__ITERATIONS_QNT = 100000
# BSC__DATA = '0'
# BSC__DATA = 'hello world'
BSC__DATA = ' ' + 'h' * (1024 - 1)
# BSC__DATA = 'h' * (1048280 - 1) + ' '
if len(BSC__DATA) > 512:
    BSC__DATA = BSC__DATA[:-19]
BSC__COMMAND = ('do', BSC__DATA)
BSC__COMPACT_COMMAND = marshal.dumps(BSC__COMMAND)
BSC__RESULT_COMPACT_COMMAND_RAW_SIZE = len(BSC__COMPACT_COMMAND)
BSC__RESULT_COMPACT_COMMAND_FULL_SIZE = BSC__RESULT_COMPACT_COMMAND_RAW_SIZE + 8
# BSC__COMPACT_COMMAND = b'h' * 1024
# BSC__RESULT_COMPACT_COMMAND_RAW_SIZE = len(BSC__COMPACT_COMMAND)
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

BSC__RAW_TRANSMITTING_IS_ALLOWED = True
# BSC__RAW_TRANSMITTING_IS_ALLOWED = False

# BSC__UNIVERSAL__USE_HANDSHAKE = True
BSC__UNIVERSAL__USE_HANDSHAKE = False

BSC__USE_READ_WITH_FIXED_BUFFER = True  # "Optimized for speed"
# BSC__USE_READ_WITH_FIXED_BUFFER = False  # "Optimized for memory"

BSC__SOCKET_READ_FIXED_BUFFER_SIZE = 1024**2
# BSC__SOCKET_READ_FIXED_BUFFER_SIZE = 1024 * 8
# BSC__SOCKET_READ_FIXED_BUFFER_SIZE = 1024 * 4
# BSC__SOCKET_READ_FIXED_BUFFER_SIZE = 1024

BSC__USE_NODELAY_INET = True
# BSC__USE_NODELAY_INET = False

BSC__REUSE_GATE_ADDR = True
# BSC__REUSE_GATE_ADDR = False

BSC__REUSE_GATE_PORT = True
# BSC__REUSE_GATE_PORT = False

LINE_TRACE_ALLOWED = True
# LINE_TRACE_ALLOWED = False

#
# ===================BENCHMARK_SERVER_CLIENT SETTINGS===================
# ======================================================================


def make_af_unix_names():
    if 'posix' == os.name:
        global SERVER_ADDRESS_AF_UNIX
        SERVER_ADDRESS_AF_UNIX = os.path.join(os.getcwd(), SERVER_ADDRESS_AF_UNIX)
        print(SERVER_ADDRESS_AF_UNIX)

        global BENCHMARK_SERVER_ADDRESS_AF_UNIX
        BENCHMARK_SERVER_ADDRESS_AF_UNIX = os.path.join(os.getcwd(), BENCHMARK_SERVER_ADDRESS_AF_UNIX)
        print(BENCHMARK_SERVER_ADDRESS_AF_UNIX)


# def working_function(data_string):
#     data_string = data_string.title()
#     return data_string


def working_function(data_string):
    return data_string


# def working_function(data_string):
#     data_string = data_string[:16]
#     return data_string


# @profile
def run_server():
    lt = LineTracer(trace_allowed=LINE_TRACE_ALLOWED)
    # lt()
    io_iteration_timeout = 0.5
    # io_iteration_timeout = 0

    set_of_tcp_settings = set()
    tcp_settings = ConnectionSettings(ConnectionType.passive, SERVER_ADDRESS, SERVER_KEYWORD)
    set_of_tcp_settings.add(tcp_settings)
    if 'posix' == os.name:
        # lt()
        tcp_settings = ConnectionSettings(ConnectionType.passive, SERVER_ADDRESS_AF_UNIX, SERVER_KEYWORD,
                                          socket.AF_UNIX, socket.SOCK_STREAM)
        set_of_tcp_settings.add(tcp_settings)
    tcp_app_server = ASockIOCore(set_of_tcp_settings)
    tcp_app_server.use_nodelay_inet = BSC__USE_NODELAY_INET
    tcp_app_server.use_speed_optimized_socket_read = BSC__USE_READ_WITH_FIXED_BUFFER
    tcp_app_server.reuse_gate_addr = BSC__REUSE_GATE_ADDR
    tcp_app_server.reuse_gate_port = BSC__REUSE_GATE_PORT
    tcp_app_server.socket_read_fixed_buffer_size.result = BSC__SOCKET_READ_FIXED_BUFFER_SIZE

    with asock_io_core_connect(tcp_app_server, True) as server:
        # lt()
        manager_client_tcp_settings = ConnectionSettings(ConnectionType.active_connected,
                                                         keyword=MANAGER_CLIENT_KEYWORD)
        manager_client_info = Client(manager_client_tcp_settings)
        manager_client_id = server.add_client(manager_client_info)

        another_client_tcp_settings = ConnectionSettings(ConnectionType.active_connected,
                                                         keyword=CLIENT_KEYWORD)
        another_client_info = Client(another_client_tcp_settings)
        server.add_client(another_client_info)

        index_in = 0
        index_out = 0
        in_amount = 0
        out_amount = 0

        in_data_size_max = 0
        in_data_size_on_hold_max = 0
        out_data_size_max = 0
        out_data_size_on_hold_max = 0

        shut_down = False
        while not shut_down:
            # lt()
            io_iteration_result = server.io_iteration(io_iteration_timeout)

            if server.global_in__data_full_size.result > in_data_size_max:
                in_data_size_max = server.global_in__data_full_size.result
            if server.global_in__deletable_data_full_size.result > in_data_size_on_hold_max:
                in_data_size_on_hold_max = server.global_in__deletable_data_full_size.result

            if server.global_out__data_full_size.result > out_data_size_max:
                out_data_size_max = server.global_out__data_full_size.result
            if server.global_out__deletable_data_full_size.result > out_data_size_on_hold_max:
                out_data_size_on_hold_max = server.global_out__deletable_data_full_size.result

            # data_stat_str = '\t\t\tIN DATA SIZE: {}; IN DATA SIZE ON HOLD: {};\tOUT DATA SIZE: {}; ' \
            #                 'OUT DATA SIZE ON HOLD: {};'
            # print(data_stat_str.format(server.global_in__data_full_size.result,
            #                            server.global_in__deletable_data_full_size.result,
            #                            server.global_out__data_full_size.result,
            #                            server.global_out__deletable_data_full_size.result))

            # CLOSED
            for another_client_id in io_iteration_result.clients_with_disconnected_connection:
                # lt()
                if another_client_id == manager_client_id:
                    # lt()
                    print('Manager client has been disconnected - Shut down server')
                    shut_down = True

                    data_stat_str = '\tMAX IN DATA SIZE: {}; MAX IN DATA SIZE ON HOLD: {};\tMAX OUT DATA SIZE: {}; ' \
                                    'MAX OUT DATA SIZE ON HOLD: {};'
                    print(data_stat_str.format(in_data_size_max, in_data_size_on_hold_max,
                                               out_data_size_max, out_data_size_on_hold_max))
                    in_data_size_max = in_data_size_on_hold_max = out_data_size_max = out_data_size_on_hold_max = 0
                else:
                    # lt()
                    print('Client "{}" has been disconnected'.format(
                        server.get_client_info(another_client_id).connection_settings.keyword))

            # CONNECTED
            for another_client_id in io_iteration_result.newly_connected_expected_clients:
                # lt()
                if another_client_id == manager_client_id:
                    # lt()
                    print('Manager client has been connected')
                    manager_client_connected = True
                else:
                    # lt()
                    print('Client "{}" has been connected'.format(
                        server.get_client_info(another_client_id).connection_settings.keyword))

            # HAVE DATA TO READ
            for another_client_id in io_iteration_result.clients_have_data_to_read:
                # lt()
                if another_client_id == manager_client_id:
                    # lt()
                    list_of_answers = list()
                    # while server.get_input_from_client_fifo_size_for_client(another_client_id):
                    #     compact_command = server.get_message_from_client(another_client_id)
                    for compact_command in server.get_messages_from_client(another_client_id):
                        # lt()
                        command = marshal.loads(compact_command)
                        if 'server command' == command[0]:
                            # lt()
                            if 'shut down' == command[1]:
                                # lt()
                                print('Client sent a Shut Down command!')
                                shut_down = True
                            elif 'switch client raw' == command[1]:
                                # lt()
                                raw_client_keyword = command[2]
                                is_raw_mode = command[3]
                                print('Making client "{}" raw == {}'.format(raw_client_keyword, is_raw_mode))

                                raw_client_id = None
                                original_is_raw_mode = None
                                try:
                                    # lt()
                                    raw_client_id = server.get_client_id_by_keyword(raw_client_keyword)
                                    original_is_raw_mode = server.get_client_raw_client_mode(raw_client_id)
                                    server.switch_client_raw_client_mode(raw_client_id, is_raw_mode)
                                    answer = ('server answer', 'switch client raw', raw_client_keyword, is_raw_mode)
                                except KeyError as err:
                                    # lt()
                                    print('Raw client with keyword "{}" was not found!'.format(raw_client_keyword))
                                    answer = ('server answer', 'switch client raw', raw_client_keyword,
                                              original_is_raw_mode)
                                compact_answer = marshal.dumps(answer)
                                list_of_answers.append(compact_answer)
                                # server.send_message_to_client(another_client_id, compact_answer)
                        elif 'do' == command[0]:
                            # lt()
                            data = command[1]
                            output_data = working_function(data)
                            output_data = marshal.dumps(output_data)
                            list_of_answers.append(output_data)
                            # server.send_message_to_client(another_client_id, output_data)
                    server.send_messages_to_client(another_client_id, list_of_answers)
                else:
                    # lt()
                    curr_in_amount = 0
                    curr_out_amount = 0

                    list_of_answers = list()
                    # while server.get_input_from_client_fifo_size_for_client(another_client_id):
                    #     message_data = server.get_message_from_client(another_client_id)
                    for message_data in server.get_messages_from_client(another_client_id):
                        # lt()
                        in_amount += len(message_data)
                        curr_in_amount += len(message_data)
                        index_in += 1
                        list_of_answers.append(message_data)
                        # server.send_message_to_client(another_client_id, message_data)
                        out_amount += len(message_data)
                        curr_out_amount += len(message_data)
                        index_out += 1
                    try:
                        # lt()
                        server.send_messages_to_client(another_client_id, list_of_answers)
                    except Exception as err:
                        # lt()
                        print(err)

                    # print('IN: ', curr_in_amount)
                    # print('OUT: ', curr_out_amount)
                    # print('index_in: {}, index_out: {}, in_amount: {}, out_amount: {}'.format(
                    #     index_in, index_out, in_amount, out_amount))

    print('Server has been Shut Down.')


def run_input_echo_client():
    tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS, MANAGER_CLIENT_KEYWORD)
    if 'posix' == os.name:
        tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS_AF_UNIX,
                                          MANAGER_CLIENT_KEYWORD, socket.AF_UNIX,
                                          socket.SOCK_STREAM)
    simple_tcp_link = SimpleTcpLink(tcp_settings)
    with simple_tcp_link_connect(simple_tcp_link) as link:
        ok = True
        while ok:
            data = input('Enter string, or press Enter to shut down: ')
            command = None
            if data:
                command = ('do', data)
            else:
                command = ('server command', 'shut down')
                ok = False
            compact_command = marshal.dumps(command)
            link.send_message(compact_command)
            if ok:
                result = link.read_message()
                result = marshal.loads(result)
                print('RESULT: "{}"'.format(result))
    print('Server has been Shut Down.')


# def run_blocking_link_server_benchmarking_client():
#     iterations_qnt = 40000
#     tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS, MANAGER_CLIENT_KEYWORD)
#     if 'posix' == os.name:
#         tcp_settings = ConnectionSettings(ConnectionType.active_connected,
#                                           SERVER_ADDRESS_AF_UNIX, MANAGER_CLIENT_KEYWORD,
#                                           socket.AF_UNIX, socket.SOCK_STREAM)
#     simple_tcp_link = SimpleTcpLink(tcp_settings)
#     with simple_tcp_link_connect(simple_tcp_link) as link:
#         data = 'hello world'
#         command = ('do', data)
#         compact_command = marshal.dumps(command)
#         close_command = ('server command', 'shut down')
#         compact_close_command = marshal.dumps(close_command)
#         with test_run_time('Server access benchmark', iterations_qnt) as index:
#             while index.result > 0:
#                 link.send_message(compact_command)
#                 result = link.read_message()
#                 index.result -= 1
#             link.send_message(compact_close_command)
#             print('Client sent a Shut Down command to server!')
#     print('Client has been Shut Down.')


def run_blocking_link_server_benchmarking_client():
    tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS, MANAGER_CLIENT_KEYWORD)
    if BSC__USE_UNIX_SOCKET_ON_CLIENT:
        if 'posix' == os.name:
            tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS_AF_UNIX,
                                              MANAGER_CLIENT_KEYWORD, socket.AF_UNIX,
                                              socket.SOCK_STREAM)
    simple_tcp_link = SimpleTcpLink(tcp_settings)
    simple_tcp_link.use_nodelay_inet = BSC__USE_NODELAY_INET

    with simple_tcp_link_connect(simple_tcp_link) as link:
        with test_run_time('Server access benchmark', BSC__ITERATIONS_QNT) as index:
            while index.result > 0:
                link.send_message(BSC__COMPACT_COMMAND)
                result = link.read_message()
                index.result -= 1
            link.send_message(BSC__COMPACT_CLOSE_COMMAND)
            print('Client sent a Shut Down command to server!')
    print('Client has been Shut Down.')


# @profile
def run_non_blocking_server_benchmarking_client():
    lt = LineTracer(trace_allowed=LINE_TRACE_ALLOWED)
    set_of_tcp_settings = set()
    tcp_settings = ConnectionSettings(ConnectionType.passive, BENCHMARK_SERVER_ADDRESS, BENCHMARK_SERVER_KEYWORD)
    set_of_tcp_settings.add(tcp_settings)
    if 'posix' == os.name:
        # lt()
        tcp_settings = ConnectionSettings(ConnectionType.passive, BENCHMARK_SERVER_ADDRESS_AF_UNIX,
                                          BENCHMARK_SERVER_KEYWORD,
                                          socket.AF_UNIX, socket.SOCK_STREAM)
        set_of_tcp_settings.add(tcp_settings)

    tcp_app_server = ASockIOCore(set_of_tcp_settings)
    tcp_app_server.use_nodelay_inet = BSC__USE_NODELAY_INET
    tcp_app_server.use_speed_optimized_socket_read = BSC__USE_READ_WITH_FIXED_BUFFER
    tcp_app_server.socket_read_fixed_buffer_size.result = BSC__SOCKET_READ_FIXED_BUFFER_SIZE

    with asock_io_core_connect(tcp_app_server) as server:
        # lt()
        super_server_tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS,
                                                       MANAGER_CLIENT_KEYWORD)
        if BSC__USE_UNIX_SOCKET_ON_CLIENT:
            # lt()
            if 'posix' == os.name:
                # lt()
                super_server_tcp_settings = ConnectionSettings(ConnectionType.active_connected,
                                                               SERVER_ADDRESS_AF_UNIX, MANAGER_CLIENT_KEYWORD,
                                                               socket.AF_UNIX, socket.SOCK_STREAM)
        super_server_info = Client(super_server_tcp_settings)
        super_server_id = server.add_client(super_server_info)
        super_server_connected = False
        need_to_send_data = True
        shut_down = False

        while not super_server_connected:
            # lt()
            io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)

            if not super_server_connected:
                # lt()
                if super_server_id in io_iteration_result.newly_connected_expected_clients:
                    # lt()
                    super_server_connected = True

            if not BSC__IO_ITERATION_TIMEOUT:
                # lt()
                sleep(BSC__SLEEP_TIME)

        with test_run_time('Full loop', BSC__ITERATIONS_QNT) as full_index:
            # lt()
            full_index.result = 0

            if super_server_connected:
                # lt()
                if need_to_send_data:
                    # lt()
                    with test_run_time('Adding data to output FIFO', BSC__ITERATIONS_QNT) as index:
                        # lt()

                        # list_of_messages = list()
                        # while index.result > 0:
                        #     # lt()
                        #     # server.send_message_to_client(super_server_id, compact_command, add_size=False)
                        #     list_of_messages.append(BSC__COMPACT_COMMAND)
                        #     # server.send_message_to_client(super_server_id, BSC__COMPACT_COMMAND)
                        #     index.result -= 1
                        # server.send_messages_to_client(super_server_id, list_of_messages)

                        try:
                            server.send_messages_to_client(
                                super_server_id, [BSC__COMPACT_COMMAND for index in range(index.result)])
                        except Exception as err:
                            print(err)
                        index.result = 0
                    need_to_send_data = False

            # all_data_have_been_sent = False
            # with test_run_time('Sending data through socket', BSC__ITERATIONS_QNT) as index:
            #     # lt()
            #     index.result = 0
            #     while not all_data_have_been_sent:
            #         # lt()
            #         io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)
            #         if super_server_id in io_iteration_result.clients_with_empty_output_fifo:
            #             # lt()
            #             all_data_have_been_sent = True

            with test_run_time('Receiving data', BSC__ITERATIONS_QNT) as index:
                # lt()
                while (not shut_down) and (index.result > 0):
                    # lt()
                    io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)

                    if super_server_id in io_iteration_result.clients_with_disconnected_connection:
                        # lt()
                        print('Super server has been disconnected - Shut down benchmark client')
                        shut_down = True
                        break
                    if super_server_id in io_iteration_result.clients_have_data_to_read:
                        # lt()
                        # while server.get_input_from_client_fifo_size_for_client(super_server_id):
                        #     compact_command = server.get_message_from_client(super_server_id)
                        for compact_command in server.get_messages_from_client(super_server_id):
                            # lt()
                            index.result -= 1

        if not shut_down:
            # lt()
            server.send_message_to_client(super_server_id, BSC__COMPACT_CLOSE_COMMAND)
            while not shut_down:
                # lt()
                io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)

                if super_server_id in io_iteration_result.clients_with_disconnected_connection:
                    # lt()
                    print('Super server has been successfully disconnected - Shut down benchmark client')
                    shut_down = True
                    break
    print('Client has been Shut Down.')


# @profile
def run_raw_non_blocking_server_benchmarking_client():
    set_of_tcp_settings = set()
    tcp_settings = ConnectionSettings(ConnectionType.passive, BENCHMARK_SERVER_ADDRESS, BENCHMARK_SERVER_KEYWORD)
    set_of_tcp_settings.add(tcp_settings)
    if 'posix' == os.name:
        tcp_settings = ConnectionSettings(ConnectionType.passive, BENCHMARK_SERVER_ADDRESS_AF_UNIX,
                                          BENCHMARK_SERVER_KEYWORD,
                                          socket.AF_UNIX, socket.SOCK_STREAM)
        set_of_tcp_settings.add(tcp_settings)

    # SERVER
    tcp_app_server = ASockIOCore(set_of_tcp_settings)
    tcp_app_server.use_nodelay_inet = BSC__USE_NODELAY_INET
    tcp_app_server.use_speed_optimized_socket_read = BSC__USE_READ_WITH_FIXED_BUFFER
    tcp_app_server.socket_read_fixed_buffer_size.result = BSC__SOCKET_READ_FIXED_BUFFER_SIZE

    with asock_io_core_connect(tcp_app_server) as server:
        # CONNECT AS MANAGER CLIENT
        super_server_tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS,
                                                       MANAGER_CLIENT_KEYWORD)
        if BSC__USE_UNIX_SOCKET_ON_CLIENT:
            if 'posix' == os.name:
                super_server_tcp_settings = ConnectionSettings(ConnectionType.active_connected,
                                                               SERVER_ADDRESS_AF_UNIX, MANAGER_CLIENT_KEYWORD,
                                                               socket.AF_UNIX, socket.SOCK_STREAM)
        super_server_info = Client(super_server_tcp_settings)
        super_server_id = server.add_client(super_server_info)

        # CONNECT AS RAW CLIENT
        raw_client_tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS, CLIENT_KEYWORD)
        if BSC__USE_UNIX_SOCKET_ON_CLIENT:
            if 'posix' == os.name:
                raw_client_tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS_AF_UNIX,
                                                             CLIENT_KEYWORD,
                                                             socket.AF_UNIX, socket.SOCK_STREAM)
        raw_client_info = Client(raw_client_tcp_settings)
        raw_client_id = server.add_client(raw_client_info)

        # SERVER RUN
        super_server_connected = False
        raw_client_connected = False
        shut_down = False

        # WAIT FOR CLIENTS TO BE CONNECTED
        while not (super_server_connected and raw_client_connected):
            io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)
            for another_client_id in io_iteration_result.newly_connected_expected_clients:
                if super_server_id == another_client_id:
                    super_server_connected = True
                elif raw_client_id == another_client_id:
                    raw_client_connected = True
            if io_iteration_result.newly_connected_expected_clients:
                if not BSC__IO_ITERATION_TIMEOUT:
                    sleep(BSC__SLEEP_TIME)

        # MAKE RAW_CLIENT RAW ON THE SERVER SIDE
        command = ('server command', 'switch client raw', CLIENT_KEYWORD, BSC__RAW_TRANSMITTING_IS_ALLOWED)
        compact_command = marshal.dumps(command)
        server.send_message_to_client(super_server_id, compact_command)
        # WAITING FOR AN ANSWER
        raw_client_command_answered = False
        while not raw_client_command_answered:
            io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)
            if super_server_id in io_iteration_result.clients_have_data_to_read:
                # while server.get_input_from_client_fifo_size_for_client(super_server_id):
                #     compact_command = server.get_message_from_client(super_server_id)
                for compact_command in server.get_messages_from_client(super_server_id):
                    command = marshal.loads(compact_command)
                    if 'server answer' == command[0]:
                        if 'switch client raw' == command[1]:
                            if CLIENT_KEYWORD == command[2]:
                                raw_client_command_answered = True
                                if command[3]:
                                    print('RAW TRANSMITTING through "{}"'.format(CLIENT_KEYWORD))
                                    print('Making client "{}" raw == {}'.format(CLIENT_KEYWORD, True))
                                    server.switch_client_raw_client_mode(raw_client_id, True)
                                else:
                                    print('STREAM TRANSMITTING through "{}"'.format(CLIENT_KEYWORD))
                                # if not command[3]:
                                #     raise Exception(
                                #         'Server has not switched raw mode for a client "{}". Shut down.'.format(
                                #             CLIENT_KEYWORD))
            else:
                if not BSC__IO_ITERATION_TIMEOUT:
                    sleep(BSC__SLEEP_TIME)

        with test_run_time('Full loop', BSC__ITERATIONS_QNT) as full_index:
            full_index.result = 0

            with test_run_time('Adding data to output FIFO', BSC__ITERATIONS_QNT) as index:
                # while index.result > 0:
                #     server.send_message_to_client(raw_client_id, BSC__COMPACT_COMMAND)
                #     index.result -= 1
                try:
                    # server.send_messages_to_client(raw_client_id, [BSC__COMPACT_COMMAND] * index.result)
                    server.send_messages_to_client(
                        raw_client_id, [BSC__COMPACT_COMMAND for index in range(index.result)])
                except Exception as err:
                    print(err)
                index.result = 0

            # all_data_have_been_sent = False
            # with test_run_time('Sending raw data through socket', BSC__ITERATIONS_QNT) as index:
            #     index.result = 0
            #     while not all_data_have_been_sent:
            #         io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)
            #         if raw_client_id in io_iteration_result.clients_with_empty_output_fifo:
            #             all_data_have_been_sent = True

            with test_run_time('Receiving raw data', BSC__ITERATIONS_QNT) as index:
                index.result = 0
                result_data_amount = 0
                all_data_amount = BSC__RESULT_COMPACT_COMMAND_RAW_SIZE * BSC__ITERATIONS_QNT
                while (not shut_down) and (result_data_amount < all_data_amount):
                    io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)

                    if io_iteration_result.clients_with_disconnected_connection:
                        print('Super server has been disconnected - Shut down benchmark client')
                        shut_down = True
                        break
                    if raw_client_id in io_iteration_result.clients_have_data_to_read:
                        # while server.get_input_from_client_fifo_size_for_client(raw_client_id):
                        #     compact_command = server.get_message_from_client(raw_client_id)
                        for compact_command in server.get_messages_from_client(raw_client_id):
                            result_data_amount += len(compact_command)

        if not shut_down:
            server.send_message_to_client(super_server_id, BSC__COMPACT_CLOSE_COMMAND)
            while not shut_down:
                io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)

                if super_server_id in io_iteration_result.clients_with_disconnected_connection:
                    print('Super server has been successfully disconnected - Shut down benchmark client')
                    shut_down = True
                    break
    print('Client has been Shut Down.')


# @profile
def run_raw_non_blocking_server_benchmarking_stupid_client():
    set_of_tcp_settings = set()
    tcp_settings = ConnectionSettings(ConnectionType.passive, BENCHMARK_SERVER_ADDRESS, BENCHMARK_SERVER_KEYWORD)
    set_of_tcp_settings.add(tcp_settings)
    if 'posix' == os.name:
        tcp_settings = ConnectionSettings(ConnectionType.passive, BENCHMARK_SERVER_ADDRESS_AF_UNIX,
                                          BENCHMARK_SERVER_KEYWORD,
                                          socket.AF_UNIX, socket.SOCK_STREAM)
        set_of_tcp_settings.add(tcp_settings)

    # SERVER
    tcp_app_server = ASockIOCore(set_of_tcp_settings)
    tcp_app_server.use_nodelay_inet = BSC__USE_NODELAY_INET
    tcp_app_server.use_speed_optimized_socket_read = BSC__USE_READ_WITH_FIXED_BUFFER
    tcp_app_server.socket_read_fixed_buffer_size.result = BSC__SOCKET_READ_FIXED_BUFFER_SIZE

    with asock_io_core_connect(tcp_app_server) as server:
        # CONNECT AS MANAGER CLIENT
        super_server_tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS,
                                                       MANAGER_CLIENT_KEYWORD)
        if BSC__USE_UNIX_SOCKET_ON_CLIENT:
            if 'posix' == os.name:
                super_server_tcp_settings = ConnectionSettings(ConnectionType.active_connected,
                                                               SERVER_ADDRESS_AF_UNIX, MANAGER_CLIENT_KEYWORD,
                                                               socket.AF_UNIX, socket.SOCK_STREAM)
        super_server_info = Client(super_server_tcp_settings)
        super_server_id = server.add_client(super_server_info)

        # CONNECT AS RAW CLIENT
        raw_client_tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS, CLIENT_KEYWORD)
        if BSC__USE_UNIX_SOCKET_ON_CLIENT:
            if 'posix' == os.name:
                raw_client_tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS_AF_UNIX,
                                                             CLIENT_KEYWORD,
                                                             socket.AF_UNIX, socket.SOCK_STREAM)
        raw_client_info = Client(raw_client_tcp_settings)
        raw_client_id = server.add_client(raw_client_info)

        # SERVER RUN
        super_server_connected = False
        raw_client_connected = False
        shut_down = False

        # WAIT FOR CLIENTS TO BE CONNECTED
        while not (super_server_connected and raw_client_connected):
            io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)
            for another_client_id in io_iteration_result.newly_connected_expected_clients:
                if super_server_id == another_client_id:
                    super_server_connected = True
                elif raw_client_id == another_client_id:
                    raw_client_connected = True
            if io_iteration_result.newly_connected_expected_clients:
                if not BSC__IO_ITERATION_TIMEOUT:
                    sleep(BSC__SLEEP_TIME)

        # MAKE RAW_CLIENT RAW ON THE SERVER SIDE
        command = ('server command', 'switch client raw', CLIENT_KEYWORD, BSC__RAW_TRANSMITTING_IS_ALLOWED)
        compact_command = marshal.dumps(command)
        server.send_message_to_client(super_server_id, compact_command)
        # WAITING FOR AN ANSWER
        raw_client_command_answered = False
        while not raw_client_command_answered:
            io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)
            if super_server_id in io_iteration_result.clients_have_data_to_read:
                # while server.get_input_from_client_fifo_size_for_client(super_server_id):
                #     compact_command = server.get_message_from_client(super_server_id)
                for compact_command in server.get_messages_from_client(super_server_id):
                    command = marshal.loads(compact_command)
                    if 'server answer' == command[0]:
                        if 'switch client raw' == command[1]:
                            if CLIENT_KEYWORD == command[2]:
                                raw_client_command_answered = True
                                if command[3]:
                                    print('RAW TRANSMITTING through "{}"'.format(CLIENT_KEYWORD))
                                    print('Making client "{}" raw == {}'.format(CLIENT_KEYWORD, True))
                                    server.switch_client_raw_client_mode(raw_client_id, True)
                                else:
                                    print('STREAM TRANSMITTING through "{}"'.format(CLIENT_KEYWORD))
            else:
                if not BSC__IO_ITERATION_TIMEOUT:
                    sleep(BSC__SLEEP_TIME)

        with test_run_time('Full loop', BSC__ITERATIONS_QNT) as full_index:
            full_index.result = 0

            try:
                for i in range(BSC__MPR):
                    server.send_message_to_client(raw_client_id, BSC__COMPACT_COMMAND)
            except Exception as err:
                print(err)

            with test_run_time('Receiving raw data', BSC__ITERATIONS_QNT) as index:
                index.result = 0
                result_data_amount = 0
                current_bunch_data_amount = 0
                all_data_amount = BSC__RESULT_COMPACT_COMMAND_RAW_SIZE * BSC__ITERATIONS_QNT
                while (not shut_down) and (result_data_amount < all_data_amount):
                    io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)

                    if io_iteration_result.clients_with_disconnected_connection:
                        print('Super server has been disconnected - Shut down benchmark client')
                        shut_down = True
                        break
                    if raw_client_id in io_iteration_result.clients_have_data_to_read:
                        # while server.get_input_from_client_fifo_size_for_client(raw_client_id):
                        #     compact_command = server.get_message_from_client(raw_client_id)
                        for compact_command in server.get_messages_from_client(raw_client_id):
                            command_len = len(compact_command)
                            result_data_amount += command_len
                            current_bunch_data_amount += command_len
                        if current_bunch_data_amount >= BSC__RESULT_COMPACT_COMMAND_RAW_SIZE * BSC__MPR:
                            try:
                                for i in range(BSC__MPR):
                                    server.send_message_to_client(raw_client_id, BSC__COMPACT_COMMAND)
                            except Exception as err:
                                print(err)

        if not shut_down:
            server.send_message_to_client(super_server_id, BSC__COMPACT_CLOSE_COMMAND)
            while not shut_down:
                io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)

                if super_server_id in io_iteration_result.clients_with_disconnected_connection:
                    print('Super server has been successfully disconnected - Shut down benchmark client')
                    shut_down = True
                    break
    print('Client has been Shut Down.')


class RawClientCheckerAllNormal(CheckIsRawConnection):
    def __call__(self, app_server: ASockIOCore, client_info: Connection):
        return False


# @profile
def run_raw_server_with_handshake(shut_down_on_client_close=False):
    io_iteration_timeout = 0.5

    set_of_tcp_settings = set()
    tcp_settings = ConnectionSettings(ConnectionType.passive, SERVER_ADDRESS, SERVER_KEYWORD)
    set_of_tcp_settings.add(tcp_settings)
    if 'posix' == os.name:
        tcp_settings = ConnectionSettings(ConnectionType.passive, SERVER_ADDRESS_AF_UNIX, SERVER_KEYWORD,
                                          socket.AF_UNIX, socket.SOCK_STREAM)
        set_of_tcp_settings.add(tcp_settings)
    tcp_app_server = ASockIOCore(set_of_tcp_settings)
    # tcp_app_server.raw_checker_for_new_incoming_connections = RawClientCheckerAllNormal()
    tcp_app_server.unknown_clients_are_allowed = True
    tcp_app_server.should_get_client_addr_info_on_connection = False
    tcp_app_server.use_nodelay_inet = BSC__USE_NODELAY_INET
    tcp_app_server.use_speed_optimized_socket_read = BSC__USE_READ_WITH_FIXED_BUFFER
    tcp_app_server.reuse_gate_addr = BSC__REUSE_GATE_ADDR
    tcp_app_server.reuse_gate_port = BSC__REUSE_GATE_PORT
    tcp_app_server.socket_read_fixed_buffer_size.result = BSC__SOCKET_READ_FIXED_BUFFER_SIZE

    with asock_io_core_connect(tcp_app_server, True) as server:
        tcp_app_server.need_to_auto_check_incoming_raw_connection = True

        another_client_tcp_settings = ConnectionSettings(ConnectionType.active_connected, keyword=CLIENT_KEYWORD)
        another_client_info = Client(another_client_tcp_settings)
        another_client_info.will_use_raw_client_connection = True
        server.add_client(another_client_info)

        shut_down = False
        while not shut_down:
            io_iteration_result = server.io_iteration(io_iteration_timeout)

            # CLOSED
            for another_client_id in io_iteration_result.clients_with_disconnected_connection:
                print('Client "{}" has been disconnected'.format(
                    server.get_client_info(another_client_id).connection_settings.keyword))
                server.remove_client(another_client_id)
                if shut_down_on_client_close:
                    shut_down = True

            # CONNECTED
            for another_client_id in io_iteration_result.newly_connected_expected_clients:
                print('Client "{}" has been connected'.format(
                    server.get_client_info(another_client_id).connection_settings.keyword))

            # HAVE DATA TO READ
            for another_client_id in io_iteration_result.clients_have_data_to_read:
                list_of_answers = list()
                # while server.get_input_from_client_fifo_size_for_client(another_client_id):
                #     message_data = server.get_message_from_client(another_client_id)
                for message_data in server.get_messages_from_client(another_client_id):
                    list_of_answers.append(message_data)
                    # try:
                    #     server.send_message_to_client(another_client_id, message_data)
                    # except Exception as err:
                    #     print(err)
                try:
                    server.send_messages_to_client(another_client_id, list_of_answers)
                except Exception as err:
                    print(err)
    print('Server has been Shut Down.')


class RawClientCheckerAllRaw(CheckIsRawConnection):
    def __call__(self, app_server: ASockIOCore, client_info: Connection):
        return True


# @profile
def run_raw_server_without_handshake(shut_down_on_client_close=False):
    io_iteration_timeout = 0.5

    set_of_tcp_settings = set()
    tcp_settings = ConnectionSettings(ConnectionType.passive, SERVER_ADDRESS, SERVER_KEYWORD)
    set_of_tcp_settings.add(tcp_settings)
    if 'posix' == os.name:
        tcp_settings = ConnectionSettings(ConnectionType.passive, SERVER_ADDRESS_AF_UNIX, SERVER_KEYWORD,
                                          socket.AF_UNIX, socket.SOCK_STREAM)
        set_of_tcp_settings.add(tcp_settings)
    tcp_app_server = ASockIOCore(set_of_tcp_settings)
    tcp_app_server.raw_checker_for_new_incoming_connections = RawClientCheckerAllRaw()
    tcp_app_server.unknown_clients_are_allowed = True
    tcp_app_server.should_get_client_addr_info_on_connection = False
    tcp_app_server.use_nodelay_inet = BSC__USE_NODELAY_INET
    tcp_app_server.use_speed_optimized_socket_read = BSC__USE_READ_WITH_FIXED_BUFFER
    tcp_app_server.reuse_gate_addr = BSC__REUSE_GATE_ADDR
    tcp_app_server.reuse_gate_port = BSC__REUSE_GATE_PORT
    tcp_app_server.socket_read_fixed_buffer_size.result = BSC__SOCKET_READ_FIXED_BUFFER_SIZE

    with asock_io_core_connect(tcp_app_server, True) as server:
        tcp_app_server.need_to_auto_check_incoming_raw_connection = True

        index_in = 0
        index_out = 0
        in_amount = 0
        out_amount = 0

        shut_down = False
        while not shut_down:
            io_iteration_result = server.io_iteration(io_iteration_timeout)

            # CLOSED
            for another_client_id in io_iteration_result.clients_with_disconnected_connection:
                print('Client "{}" has been disconnected'.format(
                    server.get_client_info(another_client_id).connection_settings.keyword))
                server.remove_client(another_client_id)
                if shut_down_on_client_close:
                    shut_down = True

            # CONNECTED
            for another_client_id in io_iteration_result.newly_connected_unknown_clients:
                print('Unknown client "{}" has been connected'.format(
                    server.get_client_info(another_client_id).connection_settings.keyword))

            # HAVE DATA TO READ
            for another_client_id in io_iteration_result.clients_have_data_to_read:
                # print('CLIENT {} HAVE {} DATA TO READ - start')
                curr_in_amount = 0
                curr_out_amount = 0
                list_of_answers = list()

                # sleep(0.01)
                for message_data in server.get_messages_from_client(another_client_id):
                    in_amount += len(message_data)
                    curr_in_amount += len(message_data)
                    index_in += 1

                    # out_data = bytes(message_data).decode()
                    # out_data = out_data.upper()
                    # out_data = out_data.encode()

                    list_of_answers.append(message_data)

                    out_amount += len(message_data)
                    curr_out_amount += len(message_data)
                    index_out += 1

                    # try:
                    #     server.send_message_to_client(another_client_id, message_data)
                    #     out_amount += len(message_data)
                    #     curr_out_amount += len(message_data)
                    #     index_out += 1
                    # except Exception as err:
                    #     print(err)
                try:
                    # print('CLIENT {}: SENDING {} DATA - start')
                    server.send_messages_to_client(another_client_id, list_of_answers)
                    # print('CLIENT {}: SENDING DATA - end')
                except Exception as err:
                    print(err)
                # print('CLIENT {} HAVE DATA TO READ - end')
                # print()

                # for message_data in server.get_messages_from_expected_client(another_client_id):
                # # while server.get_input_from_client_fifo_size_for_client(another_client_id):
                # #     message_data = server.get_message_from_client(another_client_id)
                #     in_amount += len(message_data)
                #     curr_in_amount += len(message_data)
                #     index_in += 1
                #     try:
                #         server.send_message_to_client(another_client_id, message_data)
                #         out_amount += len(message_data)
                #         curr_out_amount += len(message_data)
                #         index_out += 1
                #     except Exception as err:
                #         print(err)

                # print('IN: ', curr_in_amount)
                # print('OUT: ', curr_out_amount)
                # print('index_in: {}, index_out: {}, in_amount: {}, out_amount: {}'.format(
                #     index_in, index_out, in_amount, out_amount))
    print('Server has been Shut Down.')


def run_raw_server(shut_down_on_client_close=ALLOW_PROFILE):
    if BSC__UNIVERSAL__USE_HANDSHAKE:
        run_raw_server_with_handshake(shut_down_on_client_close)
    else:
        run_raw_server_without_handshake(shut_down_on_client_close)


# @profile
def run_universal_raw_non_blocking_benchmarking_client():
    set_of_tcp_settings = set()

    # SERVER
    tcp_app_server = ASockIOCore(set_of_tcp_settings)
    tcp_app_server.use_nodelay_inet = BSC__USE_NODELAY_INET
    tcp_app_server.use_speed_optimized_socket_read = BSC__USE_READ_WITH_FIXED_BUFFER
    tcp_app_server.socket_read_fixed_buffer_size.result = BSC__SOCKET_READ_FIXED_BUFFER_SIZE

    with asock_io_core_connect(tcp_app_server) as server:
        # CONNECT AS RAW CLIENT
        raw_client_tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS, CLIENT_KEYWORD)
        if BSC__USE_UNIX_SOCKET_ON_CLIENT:
            if 'posix' == os.name:
                raw_client_tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS_AF_UNIX,
                                                             CLIENT_KEYWORD,
                                                             socket.AF_UNIX, socket.SOCK_STREAM)
        raw_client_info = Client(raw_client_tcp_settings)
        raw_client_info.will_use_raw_client_connection = True
        if not BSC__UNIVERSAL__USE_HANDSHAKE:
            raw_client_info.will_use_raw_connection_without_handshake = True
        raw_client_id = server.add_client(raw_client_info)

        # SERVER RUN
        shut_down = False

        with test_run_time('Full loop', BSC__ITERATIONS_QNT) as full_index:
            full_index.result = 0

            with test_run_time('Adding data to output FIFO', BSC__ITERATIONS_QNT) as index:
                # while index.result > 0:
                #     server.send_message_to_client(raw_client_id, BSC__COMPACT_COMMAND)
                #     index.result -= 1
                try:
                    # server.send_messages_to_client(raw_client_id, [BSC__COMPACT_COMMAND] * index.result)
                    # out_command = ' ' + 'x' * (len(BSC__COMPACT_COMMAND) - 1)
                    # out_command = out_command.encode()
                    server.send_messages_to_client(
                        raw_client_id, [BSC__COMPACT_COMMAND for index in range(index.result)])
                except Exception as err:
                    print(err)
                index.result = 0

            # all_data_have_been_sent = False
            # with test_run_time('Sending raw data through socket', BSC__ITERATIONS_QNT) as index:
            #     index.result = 0
            #     while not all_data_have_been_sent:
            #         io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)
            #         if raw_client_id in io_iteration_result.clients_with_empty_output_fifo:
            #             all_data_have_been_sent = True

            with test_run_time('Receiving raw data', BSC__ITERATIONS_QNT) as index:
                index.result = 0
                result_data_amount = 0
                all_data_amount = BSC__RESULT_COMPACT_COMMAND_RAW_SIZE * BSC__ITERATIONS_QNT
                while (not shut_down) and (result_data_amount < all_data_amount):
                    io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)

                    if io_iteration_result.clients_with_disconnected_connection:
                        print('Super server has been disconnected - Shut down benchmark client')
                        shut_down = True
                        break
                    if raw_client_id in io_iteration_result.clients_have_data_to_read:
                        # while server.get_input_from_client_fifo_size_for_client(raw_client_id):
                        #     compact_command = server.get_message_from_client(raw_client_id)
                        #     print(len(bytes(compact_command)))
                        for compact_command in server.get_messages_from_client(raw_client_id):
                            result_data_amount += len(compact_command)

                print('result_data_amount: {}; all_data_amount: {}'.format(result_data_amount, all_data_amount))

    print('Client has been Shut Down.')


# @profile
def run_universal_raw_non_blocking_benchmarking_stupid_client():
    set_of_tcp_settings = set()

    # SERVER
    tcp_app_server = ASockIOCore(set_of_tcp_settings)
    tcp_app_server.use_nodelay_inet = BSC__USE_NODELAY_INET
    tcp_app_server.use_speed_optimized_socket_read = BSC__USE_READ_WITH_FIXED_BUFFER
    tcp_app_server.socket_read_fixed_buffer_size.result = BSC__SOCKET_READ_FIXED_BUFFER_SIZE

    with asock_io_core_connect(tcp_app_server) as server:
        # CONNECT AS RAW CLIENT
        raw_client_tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS, CLIENT_KEYWORD)
        if BSC__USE_UNIX_SOCKET_ON_CLIENT:
            if 'posix' == os.name:
                raw_client_tcp_settings = ConnectionSettings(ConnectionType.active_connected, SERVER_ADDRESS_AF_UNIX,
                                                             CLIENT_KEYWORD,
                                                             socket.AF_UNIX, socket.SOCK_STREAM)
        raw_client_info = Client(raw_client_tcp_settings)
        raw_client_info.will_use_raw_client_connection = True
        if not BSC__UNIVERSAL__USE_HANDSHAKE:
            raw_client_info.will_use_raw_connection_without_handshake = True
        raw_client_id = server.add_client(raw_client_info)

        # SERVER RUN
        shut_down = False

        with test_run_time('Full loop', BSC__ITERATIONS_QNT) as full_index:
            full_index.result = 0

            index_in = 0
            index_out = 0
            in_amount = 0
            out_amount = 0

            curr_out_amount = 0
            try:
                for i in range(BSC__MPR):
                    server.send_message_to_client(raw_client_id, BSC__COMPACT_COMMAND)
                    index_out += 1
                    out_amount += len(BSC__COMPACT_COMMAND)
                    curr_out_amount += len(BSC__COMPACT_COMMAND)
            except Exception as err:
                print(err)

            # print('OUT: ', curr_out_amount)
            # print('index_in: {}, index_out: {}, in_amount: {}, out_amount: {}'.format(
            #     index_in, index_out, in_amount, out_amount))

            with test_run_time('Receiving raw data', BSC__ITERATIONS_QNT) as index:
                index.result = 0
                result_data_amount = 0
                current_bunch_data_amount = 0
                all_data_amount = BSC__RESULT_COMPACT_COMMAND_RAW_SIZE * BSC__ITERATIONS_QNT
                while (not shut_down) and (result_data_amount < all_data_amount):
                    # print(0)
                    io_iteration_result = server.io_iteration(BSC__IO_ITERATION_TIMEOUT)

                    if io_iteration_result.clients_with_disconnected_connection:
                        # print(1)
                        print('Super server has been disconnected - Shut down benchmark client')
                        shut_down = True
                        break
                    if raw_client_id in io_iteration_result.clients_have_data_to_read:
                        # print(2)
                        curr_in_amount = 0
                        # while server.get_input_from_client_fifo_size_for_client(raw_client_id):
                        #     compact_command = server.get_message_from_client(raw_client_id)
                        for compact_command in server.get_messages_from_client(raw_client_id):
                            command_len = len(compact_command)
                            result_data_amount += command_len
                            current_bunch_data_amount += command_len
                            index_in += 1
                            in_amount += len(compact_command)
                            curr_in_amount += len(compact_command)
                        # print('IN: ', curr_in_amount)
                        curr_out_amount = 0
                        if (result_data_amount < all_data_amount) and \
                                (current_bunch_data_amount >= BSC__RESULT_COMPACT_COMMAND_RAW_SIZE * BSC__MPR):
                            current_bunch_data_amount = 0
                            try:
                                for i in range(BSC__MPR):
                                    server.send_message_to_client(raw_client_id, BSC__COMPACT_COMMAND)
                                    index_out += 1
                                    out_amount += len(BSC__COMPACT_COMMAND)
                                    curr_out_amount += len(BSC__COMPACT_COMMAND)
                            except Exception as err:
                                print(err)
                            # print('OUT: ', curr_out_amount)
                        # else:
                        #     pr_str = 'result_data_amount: {}, all_data_amount: {}, current_bunch_data_amount: {}, ' \
                        #              'BSC__RESULT_COMPACT_COMMAND_RAW_SIZE * BSC__MPR: {}'
                        #     print(pr_str.format(
                        #         result_data_amount, all_data_amount, current_bunch_data_amount,
                        #         BSC__RESULT_COMPACT_COMMAND_RAW_SIZE * BSC__MPR
                        #     ))
                        # print('index_in: {}, index_out: {}, in_amount: {}, out_amount: {}'.format(
                        #     index_in, index_out, in_amount, out_amount))
                print('result_data_amount: {}'.format(result_data_amount))

    print('Client has been Shut Down.')


def run_naive_universal_blocking_server(shut_down_on_client_close=False):
    # print(current_line())
    print('Server started.')
    gate = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    gate.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    gate.bind(SERVER_ADDRESS)
    gate.listen(1)
    conn, addr = gate.accept()
    print('Connected by', addr)

    gate.setblocking(0)
    conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    input_buffer = None
    current_memoryview_input = None
    received_all = 0
    sent_all = 0
    server_ok = True
    while server_ok:
        # print(current_line())
        data = None
        
        read_ok = True
        while read_ok:
            # print(current_line())
            try:
                # print(current_line())
                if current_memoryview_input:
                    # print(current_line())
                    nbytes = conn.recv_into(current_memoryview_input)
                    if nbytes > 0:
                        # print(current_line())
                        data = current_memoryview_input[:nbytes]
                        # recv_data_len = len(data)
                        # received_all += recv_data_len
                        # print('Received:', recv_data_len)
                        # print('received_all =', received_all)
                        current_memoryview_input = current_memoryview_input[nbytes:]
                        read_ok = False
                    else:
                        # print(current_line())
                        print(nbytes)
                        print('Client disconnected - shut down server.')
                        server_ok = False
                        break
                else:
                    # print(current_line())
                    input_buffer = bytearray(1048576)
                    current_memoryview_input = memoryview(input_buffer)
            except BlockingIOError as err:
                # print(current_line())
                read_ok = False
            except InterruptedError as err:
                # print(current_line())
                pass
            except ConnectionError as err:
                # print(current_line())
                print('Client disconnected - shut down server.')
                server_ok = False
                read_ok = False
            except (socket.error, OSError) as err:
                # print(current_line())
                if (errno.EAGAIN == err.errno) or (errno.EWOULDBLOCK == err.errno):
                    # print(current_line())
                    read_ok = False
                elif errno.EINTR == err.errno:
                    # print(current_line())
                    pass
                elif err.errno in _SET_OF_CONNECTION_ERRORS:
                    # print(current_line())
                    print('Client disconnected - shut down server.')
                    server_ok = False
                    read_ok = False
                else:
                    # print(current_line())
                    if 'nt' == os.name:
                        # print(current_line())
                        if errno.WSAECONNRESET == err.errno:
                            # print(current_line())
                            print('Client disconnected - shut down server.')
                            server_ok = False
                            read_ok = False
                        else:
                            # print(current_line())
                            raise err
                    else:
                        # print(current_line())
                        raise err

        if data:
            # print(current_line())
            data = memoryview(data)

            write_ok = True
            while write_ok:
                # print(current_line())
                try:
                    # print(current_line())
                    if data:
                        # print(current_line())
                        nbytes = conn.send(data)
                        if nbytes >= 0:
                            # print(current_line())
                            # print('Sent:', nbytes)
                            # sent_all += nbytes
                            # print('sent_all =', sent_all)
                            data = data[nbytes:]
                        else:
                            # print(current_line())
                            print('Client disconnected - shut down server.')
                            server_ok = False
                            break
                    else:
                        # print(current_line())
                        # data = None
                        write_ok = False
                except BlockingIOError as err:
                    # print(current_line())
                    pass
                except InterruptedError as err:
                    # print(current_line())
                    pass
                except ConnectionError as err:
                    # print(current_line())
                    print('Client disconnected - shut down server.')
                    server_ok = False
                    write_ok = False
                except (socket.error, OSError) as err:
                    # print(current_line())
                    if (errno.EAGAIN == err.errno) or (errno.EWOULDBLOCK == err.errno):
                        # print(current_line())
                        pass
                    elif errno.EINTR == err.errno:
                        # print(current_line())
                        pass
                    elif err.errno in _SET_OF_CONNECTION_ERRORS:
                        # print(current_line())
                        print('Client disconnected - shut down server.')
                        server_ok = False
                        write_ok = False
                    else:
                        # print(current_line())
                        if 'nt' == os.name:
                            # print(current_line())
                            if errno.WSAECONNRESET == err.errno:
                                # print(current_line())
                                print('Client disconnected - shut down server.')
                                server_ok = False
                                write_ok = False
                            else:
                                # print(current_line())
                                raise err
                        else:
                            # print(current_line())
                            raise err

    print('Server shut down.')


# @profile
def run_http_server(shut_down_on_client_close=ALLOW_PROFILE):
    io_iteration_timeout = 0.5

    set_of_tcp_settings = set()
    tcp_settings = ConnectionSettings(ConnectionType.passive, SERVER_ADDRESS, SERVER_KEYWORD)
    set_of_tcp_settings.add(tcp_settings)
    if 'posix' == os.name:
        tcp_settings = ConnectionSettings(ConnectionType.passive, SERVER_ADDRESS_AF_UNIX, SERVER_KEYWORD,
                                          socket.AF_UNIX, socket.SOCK_STREAM)
        set_of_tcp_settings.add(tcp_settings)
    tcp_app_server = ASockIOCore(set_of_tcp_settings)
    tcp_app_server.raw_checker_for_new_incoming_connections = RawClientCheckerAllRaw()
    tcp_app_server.unknown_clients_are_allowed = True
    tcp_app_server.should_get_client_addr_info_on_connection = False
    tcp_app_server.use_nodelay_inet = BSC__USE_NODELAY_INET
    tcp_app_server.use_speed_optimized_socket_read = BSC__USE_READ_WITH_FIXED_BUFFER
    tcp_app_server.reuse_gate_addr = BSC__REUSE_GATE_ADDR
    tcp_app_server.reuse_gate_port = BSC__REUSE_GATE_PORT
    tcp_app_server.socket_read_fixed_buffer_size.result = BSC__SOCKET_READ_FIXED_BUFFER_SIZE

    with asock_io_core_connect(tcp_app_server, True, listen_num=1000) as server:
        tcp_app_server.need_to_auto_check_incoming_raw_connection = True

        clients_per_transport_id = dict()

        connections_counter = 0
        simultaneous_connections_counter = 0
        simultaneous_connections_counter_max = simultaneous_connections_counter

        in_data_size_max = 0
        in_data_size_on_hold_max = 0
        out_data_size_max = 0
        out_data_size_on_hold_max = 0

        shut_down = False
        while not shut_down:
            io_iteration_result = server.io_iteration(io_iteration_timeout)

            if __debug__:
                if server.global_in__data_full_size.result > in_data_size_max:
                    in_data_size_max = server.global_in__data_full_size.result
                if server.global_in__deletable_data_full_size.result > in_data_size_on_hold_max:
                    in_data_size_on_hold_max = server.global_in__deletable_data_full_size.result

                if server.global_out__data_full_size.result > out_data_size_max:
                    out_data_size_max = server.global_out__data_full_size.result
                if server.global_out__deletable_data_full_size.result > out_data_size_on_hold_max:
                    out_data_size_on_hold_max = server.global_out__deletable_data_full_size.result

            # print('\t\tSIMULTANEOUS CONNECTIONS QNT: {}; ALL CONNECTIONS QNT: {}'.format(
            #     simultaneous_connections_counter, connections_counter))
            #
            # data_stat_str = '\t\t\tIN DATA SIZE: {}; IN DATA SIZE ON HOLD: {};\tOUT DATA SIZE: {}; ' \
            #                 'OUT DATA SIZE ON HOLD: {};'
            # print(data_stat_str.format(server.global_in__data_full_size.result,
            #                            server.global_in__deletable_data_full_size.result,
            #                            server.global_out__data_full_size.result,
            #                            server.global_out__deletable_data_full_size.result))

            # CONNECTED
            for another_client_id in io_iteration_result.newly_connected_unknown_clients:
                if __debug__:
                    connections_counter += 1
                    simultaneous_connections_counter += 1
                    if simultaneous_connections_counter > simultaneous_connections_counter_max:
                        simultaneous_connections_counter_max = simultaneous_connections_counter
                # print('{}; {}'.format(connections_counter, connections_counter_max))
                # print('Unknown client "{}" has been connected'.format(
                #     server.get_client_info(another_client_id).connection_settings.keyword))
                clients_per_transport_id[another_client_id] = HttpClientData(another_client_id, server)

            # HAVE DATA TO READ
            for another_client_id in io_iteration_result.clients_have_data_to_read:
                clients_per_transport_id[another_client_id].data_received()

            # CLOSED
            for another_client_id in io_iteration_result.clients_with_disconnected_connection:
                if __debug__:
                    simultaneous_connections_counter -= 1
                    if simultaneous_connections_counter > simultaneous_connections_counter_max:
                        simultaneous_connections_counter_max = simultaneous_connections_counter
                    # print('{}; {}'.format(connections_counter, connections_counter_max))
                    if not simultaneous_connections_counter:
                        print('MAX SIMULTANEOUS CONNECTIONS QNT: {}; ALL CONNECTIONS QNT: {}'.format(
                            simultaneous_connections_counter_max, connections_counter))
                        connections_counter = 0
                        simultaneous_connections_counter_max = 0

                        data_stat_str = '\tMAX IN DATA SIZE: {}; MAX IN DATA SIZE ON HOLD: {};' \
                                        '\tMAX OUT DATA SIZE: {}; ' \
                                        'MAX OUT DATA SIZE ON HOLD: {};'
                        print(data_stat_str.format(in_data_size_max, in_data_size_on_hold_max,
                                                   out_data_size_max, out_data_size_on_hold_max))
                        in_data_size_max = in_data_size_on_hold_max = out_data_size_max = out_data_size_on_hold_max = 0

                # print('Client "{}" has been disconnected'.format(
                #     server.get_client_info(another_client_id).connection_settings.keyword))
                # server.remove_client(another_client_id)
                if clients_per_transport_id[another_client_id].socket_error():
                    del clients_per_transport_id[another_client_id]

                # if shut_down_on_client_close:
                #     shut_down = True
    print('Server has been Shut Down.')


_RESP_CACHE = {}


class HttpRequest:
    __slots__ = ('_protocol', '_url', '_headers', '_version')

    def __init__(self, protocol, url, headers, version):
        self._protocol = protocol
        self._url = url
        self._headers = headers
        self._version = version


class HttpResponse:
    __slots__ = ('_protocol', '_request', '_headers_sent')

    def __init__(self, protocol, request: HttpRequest):
        self._protocol = protocol
        self._request = request
        self._headers_sent = False

    def write(self, data):
        # print('OUT {}:'.format(self._protocol._transport_id), data[:50])
        self._protocol.output_list.append(b''.join([
            'HTTP/{} 200 OK\r\n'.format(
                self._request._version).encode('latin-1'),
            b'Content-Type: text/plain\r\n',
            'Content-Length: {}\r\n'.format(len(data)).encode('latin-1'),
            b'\r\n',
            data
        ]))


class HttpClientData:
    __slots__ = ('server', 'output_list', 'transport_id',
                 '_current_request', '_current_parser',
                 '_current_url', '_current_headers', '_last_piece_of_data',
                 '_previous_piece_of_data')

    def __init__(self, transport_id, server: ASockIOCore):
        # print('INIT: {}'.format(transport_id))
        self.server = server
        self.transport_id = transport_id
        # self.output_list = deque()
        self.output_list = list()
        self._current_parser = httptools.HttpRequestParser(self)
        self._current_headers = list()
        self._current_request = None
        self._current_url = None

        self._last_piece_of_data = None
        self._previous_piece_of_data = None

    def data_received(self):
        try:
            for message in self.server.get_messages_from_client(self.transport_id):
                # print('IN {}: {}'.format(self.transport_id, bytes(message)))
                self._current_parser.feed_data(message)
            self.server.send_messages_to_client(self.transport_id, self.output_list)
        except Exception as err:
            print('EXCEPTION:', err)
            self.server.mark_client_connection_as_should_be_closed_immediately(self.transport_id, False)
            # raise err
        del self.output_list[:]
        # self.output_list.clear()

    def socket_error(self):
        self._current_request = self._current_parser = None
        self.server.remove_client(self.transport_id)
        return True

    # ==== HttpRequestParser methods: ====

    # def on_message_begin(self):
    #     self._current_request = None
    #     self._current_url = None
    #     self._current_headers = list()

    def on_url(self, url):
        if self._current_url:
            self._current_url += url
        else:
            self._current_url = url

    # def on_status(self, data):
    #     # print('on_status: {}'.format(data))
    #     pass

    def on_header(self, name, value):
        self._current_headers.append((name, value))

    def on_headers_complete(self):
        try:
            # self._current_url = b''.join(self._current_url_parts)
            # self._current_url_parts = list()
            self._current_request = HttpRequest(
                self, self._current_url, self._current_headers,
                self._current_parser.get_http_version())

            self.handle(self._current_request, HttpResponse(self, self._current_request))
        except:
            print('ON HEADERS COMPLETE. ID: {}. Last: {}. Previous : {}.'.format(
                self.transport_id, self._last_piece_of_data, self._previous_piece_of_data))
            raise

    # def on_body(self, data):
    #     # print('on_body: {}'.format(data))
    #     pass

    # def on_message_complete(self):
    #     self._current_request = None
    #     self._current_url = None
    #     self._current_headers = list()
    #     # print('KEEP ALIVE:', self._current_parser.should_keep_alive())
    #     if not self._current_parser.should_keep_alive():
    #         self._server.mark_client_connection_as_ready_to_be_closed(self._transport_id, False)
    #         # self._current_parser = None
    #     # self._current_request = None

    # def on_chunk_header(self):
    #     pass
    #
    # def on_chunk_complete(self):
    #     pass

    ####

    # ==== END ====

    def handle(self, request, response: HttpResponse):
        parsed_url = httptools.parse_url(self._current_url)
        payload_size = parsed_url.path.decode('ascii')[1:]
        if not payload_size:
            payload_size = 1024
        else:
            payload_size = int(payload_size)
        resp = _RESP_CACHE.get(payload_size)
        if resp is None:
            resp = b'X' * payload_size
            _RESP_CACHE[payload_size] = resp
        response.write(resp)

        self._current_request = None
        self._current_url = None
        self._current_headers = list()
        # print('KEEP ALIVE:', self._current_parser.should_keep_alive())
        if not self._current_parser.should_keep_alive():
            self.server.mark_client_connection_as_ready_to_be_closed(self.transport_id, False)


class FakeHttpClientData(HttpClientData):
    def data_piece_received(self, data):
        try:
            self.data_received_(data)
        except Exception as err:
            print('EXCEPTION:', err)
            raise err
            # self.server.mark_client_connection_as_should_be_closed_immediately(self.transport_id, False)
        del self.output_list[:]

    def data_received_(self, data):
            self._current_parser.feed_data(data)


# class HttpProtocol:
#
#     __slots__ = ('_server',
#                  '_transport_id', '_current_request', '_current_parser',
#                  '_current_url', '_current_headers', '_output_list', '_last_piece_of_data',
#                  '_previous_piece_of_data')
#
#     # def __init__(self, server: ASockIOCore, output_list: deque):
#     def __init__(self, server: ASockIOCore, output_list: list):
#         self._server = server
#         self._transport_id = None
#         self._output_list = output_list
#         self._current_request = None
#         self._current_parser = None
#         self._current_url = None
#         self._current_headers = list()
#         self._last_piece_of_data = None
#         self._previous_piece_of_data = None
#         # self._lt = LineTracer(trace_allowed=False)
#
#     # def on_message_begin(self):
#     #     # self._lt()
#     #     self._current_request = None
#     #     self._current_url = None
#     #     self._current_headers = list()
#
#     def on_url(self, url):
#         # self._lt()
#         # self._current_url_parts.append(url)
#         if self._current_url:
#             self._current_url += url
#         else:
#             self._current_url = url
#
#     # def on_status(self, data):
#     #     # self._lt()
#     #     # print('on_status: {}'.format(data))
#     #     pass
#
#     def on_header(self, name, value):
#         # self._lt()
#         self._current_headers.append((name, value))
#
#     def on_headers_complete(self):
#         # self._lt()
#         try:
#             # self._current_url = b''.join(self._current_url_parts)
#             # self._current_url_parts = list()
#             self._current_request = HttpRequest(
#                 self, self._current_url, self._current_headers,
#                 self._current_parser.get_http_version())
#
#             self.handle(self._current_request, HttpResponse(self, self._current_request))
#         except:
#             print('ON HEADERS COMPLETE. ID: {}. Last: {}. Previous : {}.'.format(
#                 self._transport_id, self._last_piece_of_data, self._previous_piece_of_data))
#             raise
#
#     # def on_body(self, data):
#     #     # self._lt()
#     #     # print('on_body: {}'.format(data))
#     #     pass
#
#     # def on_message_complete(self):
#     #     self._current_request = None
#     #     self._current_url = None
#     #     self._current_headers = list()
#     #     # self._lt()
#     #     # print('KEEP ALIVE:', self._current_parser.should_keep_alive())
#     #     if not self._current_parser.should_keep_alive():
#     #         self._server.mark_client_connection_as_ready_to_be_closed(self._transport_id, False)
#     #         # self._current_parser = None
#     #     # self._current_request = None
#
#     # def on_chunk_header(self):
#     #     # self._lt()
#     #     pass
#     #
#     # def on_chunk_complete(self):
#     #     # self._lt()
#     #     pass
#
#     ####
#
#     def connection_made(self, transport_id):
#         # self._lt()
#         self._transport_id = transport_id
#         self._current_parser = httptools.HttpRequestParser(self)
#         self._current_headers = list()
#         self._current_request = None
#         self._current_url = None
#         # self._last_piece_of_data = None
#         # self._previous_piece_of_data = None
#
#     def connection_lost(self):
#         # self._lt()
#         self._current_request = self._current_parser = None
#         self._server.remove_client(self._transport_id)
#         # print('HTTP client {} removed.'.format(self._transport_id))
#         return True
#
#     def data_received(self, data):
#         # self._lt()
#         # self._previous_piece_of_data = self._last_piece_of_data
#         # self._last_piece_of_data = bytes(data)
#
#         self._current_parser.feed_data(data)
#
#     def handle(self, request, response: HttpResponse):
#         # self._lt()
#         parsed_url = httptools.parse_url(self._current_url)
#         payload_size = parsed_url.path.decode('ascii')[1:]
#         if not payload_size:
#             payload_size = 1024
#         else:
#             payload_size = int(payload_size)
#         resp = _RESP_CACHE.get(payload_size)
#         if resp is None:
#             resp = b'X' * payload_size
#             _RESP_CACHE[payload_size] = resp
#         response.write(resp)
#
#         self._current_request = None
#         self._current_url = None
#         self._current_headers = list()
#         # self._lt()
#         # print('KEEP ALIVE:', self._current_parser.should_keep_alive())
#         if not self._current_parser.should_keep_alive():
#             self._server.mark_client_connection_as_ready_to_be_closed(self._transport_id, False)


def httptools_test():
    tcp_app_server = ASockIOCore(set())
    with asock_io_core_connect(tcp_app_server) as server:
        full_request = b'GET /1000 HTTP/1.1\r\nHost: 127.0.0.1:18495\r\n\r\n'
        fake_client = FakeHttpClientData(0, server)
        print('FULL REQUEST TEST:')
        fake_client.data_piece_received(full_request)
        print('PARTLY REQUEST TEST 1:')
        fake_client.data_piece_received(full_request[:6])
        print('PARTLY REQUEST TEST 2:')
        fake_client.data_piece_received(full_request[6:11])
        print('PARTLY REQUEST TEST 2:')
        fake_client.data_piece_received(full_request[11:])


# class HttpInlineProcessor(InlineProcessor):
#     __slots__ = ('protocol', 'server', 'output_list', 'transport_id')
#
#     def __init__(self, *args, **kwargs):
#         super(HttpInlineProcessor, self).__init__(*args, **kwargs)
#         self.protocol = HttpProtocolForInlineProcessor(self, self.output_messages)
#         self.protocol.connection_made(self.keyword)
#
#     def on__data_received(self, data: bytes):
#         try:
#             self.protocol.data_received(data)
#         except Exception as err:
#             print('EXCEPTION:', err)
#             self.mark__socket_as_should_be_closed_immediately(True)
#             # raise err
#
#     def on__connection_lost(self):
#         self.protocol.connection_lost()


class HttpRequestForInlineProcessor:
    __slots__ = ('_protocol', '_url', '_headers', '_version')

    def __init__(self, protocol, url, headers, version):
        self._protocol = protocol
        self._url = url
        self._headers = headers
        self._version = version


class HttpResponseForInlineProcessor:
    __slots__ = ('_protocol', '_request', '_headers_sent')

    def __init__(self, protocol, request: HttpRequestForInlineProcessor):
        self._protocol = protocol
        self._request = request
        self._headers_sent = False

    def write(self, data):
        # print('OUT {}:'.format(self._protocol._transport_id), data[:50])
        self._protocol.output_messages.append(b''.join([
            'HTTP/{} 200 OK\r\n'.format(self._request._version).encode('latin-1'),
            b'Content-Type: text/plain\r\n',
            'Content-Length: {}\r\n'.format(len(data)).encode('latin-1'),
            b'\r\n',
            data
        ]))


class HttpInlineProcessor(InlineProcessor):
    __slots__ = ('_current_request', '_current_parser',
                 '_current_url', '_current_headers', '_last_piece_of_data',
                 '_previous_piece_of_data')

    def __init__(self, *args, **kwargs):
        super(HttpInlineProcessor, self).__init__(*args, **kwargs)
        self._current_parser = httptools.HttpRequestParser(self)
        self._current_headers = list()
        self._current_request = None
        self._current_url = None
        self._last_piece_of_data = None
        self._previous_piece_of_data = None

    def on__data_received(self, data: bytes):
        try:
            self._current_parser.feed_data(data)
        except Exception as err:
            print('EXCEPTION:', err)
            self.mark__socket_as_should_be_closed_immediately(True)
            # raise err

    def on__connection_lost(self):
        self._current_request = self._current_parser = None

    # ==== HttpRequestParser methods: ====

    # def on_message_begin(self):
    #     self._current_request = None
    #     self._current_url = None
    #     self._current_headers = list()

    def on_url(self, url):
        if self._current_url:
            self._current_url += url
        else:
            self._current_url = url

    # def on_status(self, data):
    #     # print('on_status: {}'.format(data))
    #     pass

    def on_header(self, name, value):
        self._current_headers.append((name, value))

    def on_headers_complete(self):
        try:
            self._current_request = HttpRequestForInlineProcessor(
                self, self._current_url, self._current_headers,
                self._current_parser.get_http_version())

            self.handle(self._current_request, HttpResponseForInlineProcessor(self, self._current_request))
        except:
            print('ON HEADERS COMPLETE. ID: {}. Last: {}. Previous : {}.'.format(
                self.client_id, self._last_piece_of_data, self._previous_piece_of_data))
            raise

    # def on_body(self, data):
    #     # print('on_body: {}'.format(data))
    #     pass

    # def on_message_complete(self):
    #     self._current_request = None
    #     self._current_url = None
    #     self._current_headers = list()
    #     # print('KEEP ALIVE:', self._current_parser.should_keep_alive())
    #     if not self._current_parser.should_keep_alive():
    #         self._server.mark_client_connection_as_ready_to_be_closed(self._transport_id, False)
    #         # self._current_parser = None
    #     # self._current_request = None

    # def on_chunk_header(self):
    #     pass
    #
    # def on_chunk_complete(self):
    #     pass

    # ==== END ====

    def handle(self, request, response: HttpResponseForInlineProcessor):
        parsed_url = httptools.parse_url(self._current_url)
        payload_size = parsed_url.path.decode('ascii')[1:]
        if not payload_size:
            payload_size = 1024
        else:
            payload_size = int(payload_size)
        # resp = get_message_by_payload_size(payload_size)
        resp = _RESP_CACHE.get(payload_size)
        if resp is None:
            resp = b'X' * payload_size
            _RESP_CACHE[payload_size] = resp
        response.write(resp)

        self._current_request = None
        self._current_url = None
        self._current_headers = list()
        # print('KEEP ALIVE:', self._current_parser.should_keep_alive())
        if not self._current_parser.should_keep_alive():
            self.mark__socket_as_ready_to_be_closed(True)


# @lru_cache(maxsize=128)
# def get_message_by_payload_size(payload_size: int)->bytes:
#     return b'X' * payload_size


# class HttpProtocolForInlineProcessor:
#
#     __slots__ = ('_current_request', '_current_parser',
#                  '_current_url', '_current_headers', '_last_piece_of_data',
#                  '_previous_piece_of_data', '_output_list', '_transport_id', '_server')
#
#     def __init__(self, server: HttpInlineProcessor, output_list):
#         self._server = server
#         self._transport_id = None
#         self._output_list = output_list
#         self._current_request = None
#         self._current_parser = None
#         self._current_url = None
#         self._current_headers = list()
#         self._last_piece_of_data = None
#         self._previous_piece_of_data = None
#         # self._lt = LineTracer(trace_allowed=False)
#
#     # def on_message_begin(self):
#     #     # self._lt()
#     #     self._current_request = None
#     #     self._current_url = None
#     #     self._current_headers = list()
#
#     def on_url(self, url):
#         # self._lt()
#         # self._current_url_parts.append(url)
#         if self._current_url:
#             self._current_url += url
#         else:
#             self._current_url = url
#
#     # def on_status(self, data):
#     #     # self._lt()
#     #     # print('on_status: {}'.format(data))
#     #     pass
#
#     def on_header(self, name, value):
#         # self._lt()
#         self._current_headers.append((name, value))
#
#     def on_headers_complete(self):
#         # self._lt()
#         try:
#             # self._current_url = b''.join(self._current_url_parts)
#             # self._current_url_parts = list()
#             self._current_request = HttpRequestForInlineProcessor(
#                 self, self._current_url, self._current_headers,
#                 self._current_parser.get_http_version())
#
#             self.handle(self._current_request, HttpResponseForInlineProcessor(self, self._current_request))
#         except:
#             print('ON HEADERS COMPLETE. ID: {}. Last: {}. Previous : {}.'.format(
#                 self._transport_id, self._last_piece_of_data, self._previous_piece_of_data))
#             raise
#
#     # def on_body(self, data):
#     #     # self._lt()
#     #     # print('on_body: {}'.format(data))
#     #     pass
#
#     # def on_message_complete(self):
#     #     self._current_request = None
#     #     self._current_url = None
#     #     self._current_headers = list()
#     #     # self._lt()
#     #     # print('KEEP ALIVE:', self._current_parser.should_keep_alive())
#     #     if not self._current_parser.should_keep_alive():
#     #         self._server.mark_client_connection_as_ready_to_be_closed(self._transport_id, False)
#     #         # self._current_parser = None
#     #     # self._current_request = None
#
#     # def on_chunk_header(self):
#     #     # self._lt()
#     #     pass
#     #
#     # def on_chunk_complete(self):
#     #     # self._lt()
#     #     pass
#
#     ####
#
#     def connection_made(self, transport_id):
#         # self._lt()
#         self._current_parser = httptools.HttpRequestParser(self)
#         self._current_headers = list()
#         self._current_request = None
#         self._current_url = None
#         self._transport_id = transport_id
#         # self._last_piece_of_data = None
#         # self._previous_piece_of_data = None
#
#     def connection_lost(self):
#         # self._lt()
#         self._current_request = self._current_parser = None
#         return True
#
#     def data_received(self, data):
#         # self._lt()
#         # self._previous_piece_of_data = self._last_piece_of_data
#         # self._last_piece_of_data = bytes(data)
#
#         self._current_parser.feed_data(data)
#
#     def handle(self, request, response: HttpResponseForInlineProcessor):
#         # self._lt()
#         parsed_url = httptools.parse_url(self._current_url)
#         payload_size = parsed_url.path.decode('ascii')[1:]
#         if not payload_size:
#             payload_size = 1024
#         else:
#             payload_size = int(payload_size)
#         # resp = get_message_by_payload_size(payload_size)
#         resp = _RESP_CACHE.get(payload_size)
#         if resp is None:
#             resp = b'X' * payload_size
#             _RESP_CACHE[payload_size] = resp
#         response.write(resp)
#
#         self._current_request = None
#         self._current_url = None
#         self._current_headers = list()
#         # self._lt()
#         # print('KEEP ALIVE:', self._current_parser.should_keep_alive())
#         if not self._current_parser.should_keep_alive():
#             self._server.mark__socket_as_ready_to_be_closed(True)


# @profile
def run_http_server_with_inline_processor(shut_down_on_client_close=ALLOW_PROFILE):
    io_iteration_timeout = 0.5

    set_of_tcp_settings = set()
    tcp_settings = ConnectionSettings(ConnectionType.passive, SERVER_ADDRESS, SERVER_KEYWORD)
    set_of_tcp_settings.add(tcp_settings)
    if 'posix' == os.name:
        tcp_settings = ConnectionSettings(ConnectionType.passive, SERVER_ADDRESS_AF_UNIX, SERVER_KEYWORD,
                                          socket.AF_UNIX, socket.SOCK_STREAM)
        set_of_tcp_settings.add(tcp_settings)
    tcp_app_server = ASockIOCore(set_of_tcp_settings)
    tcp_app_server.raw_checker_for_new_incoming_connections = RawClientCheckerAllRaw()
    tcp_app_server.unknown_clients_are_allowed = True
    tcp_app_server.should_get_client_addr_info_on_connection = False
    tcp_app_server.use_nodelay_inet = BSC__USE_NODELAY_INET
    tcp_app_server.use_speed_optimized_socket_read = BSC__USE_READ_WITH_FIXED_BUFFER
    tcp_app_server.reuse_gate_addr = BSC__REUSE_GATE_ADDR
    tcp_app_server.reuse_gate_port = BSC__REUSE_GATE_PORT
    tcp_app_server.socket_read_fixed_buffer_size.result = BSC__SOCKET_READ_FIXED_BUFFER_SIZE
    tcp_app_server.class_for_unknown_clients_inline_processing = HttpInlineProcessor

    with asock_io_core_connect(tcp_app_server, True, listen_num=1000) as server:
        tcp_app_server.need_to_auto_check_incoming_raw_connection = True

        connections_counter = 0
        simultaneous_connections_counter = 0
        simultaneous_connections_counter_max = simultaneous_connections_counter

        in_data_size_max = 0
        in_data_size_on_hold_max = 0
        out_data_size_max = 0
        out_data_size_on_hold_max = 0

        shut_down = False
        while not shut_down:
            io_iteration_result = server.io_iteration(io_iteration_timeout)

            if server.global_in__data_full_size.result > in_data_size_max:
                in_data_size_max = server.global_in__data_full_size.result
            if server.global_in__deletable_data_full_size.result > in_data_size_on_hold_max:
                in_data_size_on_hold_max = server.global_in__deletable_data_full_size.result

            if server.global_out__data_full_size.result > out_data_size_max:
                out_data_size_max = server.global_out__data_full_size.result
            if server.global_out__deletable_data_full_size.result > out_data_size_on_hold_max:
                out_data_size_on_hold_max = server.global_out__deletable_data_full_size.result

            # CONNECTED
            for another_client_id in io_iteration_result.newly_connected_unknown_clients:
                connections_counter += 1
                simultaneous_connections_counter += 1
                if simultaneous_connections_counter > simultaneous_connections_counter_max:
                    simultaneous_connections_counter_max = simultaneous_connections_counter
                # print('{}; {}'.format(connections_counter, connections_counter_max))
                # print('Unknown client "{}" has been connected'.format(
                #     server.get_client_info(another_client_id).connection_settings.keyword))

            # CLOSED
            for another_client_id in io_iteration_result.clients_with_disconnected_connection:
                simultaneous_connections_counter -= 1
                if simultaneous_connections_counter > simultaneous_connections_counter_max:
                    simultaneous_connections_counter_max = simultaneous_connections_counter
                # print('{}; {}'.format(connections_counter, connections_counter_max))
                if not simultaneous_connections_counter:
                    print('MAX SIMULTANEOUS CONNECTIONS QNT: {}; ALL CONNECTIONS QNT: {}'.format(
                        simultaneous_connections_counter_max, connections_counter))
                    connections_counter = 0
                    simultaneous_connections_counter_max = 0

                    data_stat_str = '\tMAX IN DATA SIZE: {}; MAX IN DATA SIZE ON HOLD: {};\tMAX OUT DATA SIZE: {}; ' \
                                    'MAX OUT DATA SIZE ON HOLD: {};'
                    print(data_stat_str.format(in_data_size_max, in_data_size_on_hold_max,
                                               out_data_size_max, out_data_size_on_hold_max))
                    in_data_size_max = in_data_size_on_hold_max = out_data_size_max = out_data_size_on_hold_max = 0

                # print('Client "{}" has been disconnected'.format(
                #     server.get_client_info(another_client_id).connection_settings.keyword))
                # server.remove_client(another_client_id)

                # if shut_down_on_client_close:
                #     shut_down = True
    print('Server has been Shut Down.')


def profiled__run_server():
    cProfile.run('run_server()', 'profiled__run_server.prof')


def profiled__run_input_echo_client():
    cProfile.run('run_input_echo_client()', 'profiled__run_input_echo_client.prof')


def profiled__run_blocking_link_server_benchmarking_client():
    cProfile.run('run_blocking_link_server_benchmarking_client()',
                 'profiled__run_blocking_link_server_benchmarking_client.prof')


def profiled__run_non_blocking_server_benchmarking_client():
    cProfile.run('run_non_blocking_server_benchmarking_client()',
                 'profiled__run_non_blocking_server_benchmarking_client.prof')


def profiled__run_raw_non_blocking_server_benchmarking_client():
    cProfile.run('run_raw_non_blocking_server_benchmarking_client()',
                 'profiled__run_raw_non_blocking_server_benchmarking_client.prof')


def profiled__run_raw_non_blocking_server_benchmarking_stupid_client():
    cProfile.run('run_raw_non_blocking_server_benchmarking_stupid_client()',
                 'profiled__run_raw_non_blocking_server_benchmarking_stupid_client.prof')


def profiled__run_raw_server():
    cProfile.run('run_raw_server(shut_down_on_client_close=True)',
                 'profiled__run_raw_server.prof')


def profiled__run_universal_raw_non_blocking_benchmarking_client():
    cProfile.run('run_universal_raw_non_blocking_benchmarking_client()',
                 'profiled__run_universal_raw_non_blocking_benchmarking_client.prof')


def profiled__run_universal_raw_non_blocking_benchmarking_stupid_client():
    cProfile.run('run_universal_raw_non_blocking_benchmarking_stupid_client()',
                 'profiled__run_universal_raw_non_blocking_benchmarking_stupid_client.prof')


def profiled__run_naive_universal_blocking_server():
    cProfile.run('run_naive_universal_blocking_server()',
                 'profiled__run_naive_universal_blocking_server.prof')


def profiled__run_http_server():
    cProfile.run('run_http_server(shut_down_on_client_close=False)',
                 'profiled__run_http_server.prof')


def profiled__httptools_test():
    cProfile.run('httptools_test()',
                 'profiled__httptools_test.prof')


def profiled__run_http_server_with_inline_processor():
    cProfile.run('run_http_server_with_inline_processor(shut_down_on_client_close=False)',
                 'profiled__run_http_server_with_inline_processor.prof')


ALL_VARIANTS = [
    run_server,
    profiled__run_server,

    run_input_echo_client,
    profiled__run_input_echo_client,

    run_blocking_link_server_benchmarking_client,
    profiled__run_blocking_link_server_benchmarking_client,

    run_non_blocking_server_benchmarking_client,
    profiled__run_non_blocking_server_benchmarking_client,

    run_raw_non_blocking_server_benchmarking_client,
    profiled__run_raw_non_blocking_server_benchmarking_client,

    run_raw_non_blocking_server_benchmarking_stupid_client,
    profiled__run_raw_non_blocking_server_benchmarking_stupid_client,

    run_raw_server,
    profiled__run_raw_server,

    run_universal_raw_non_blocking_benchmarking_client,
    profiled__run_universal_raw_non_blocking_benchmarking_client,

    run_universal_raw_non_blocking_benchmarking_stupid_client,
    profiled__run_universal_raw_non_blocking_benchmarking_stupid_client,

    run_naive_universal_blocking_server,
    profiled__run_naive_universal_blocking_server,

    run_http_server,
    profiled__run_http_server,

    httptools_test,
    profiled__httptools_test,

    run_http_server_with_inline_processor,
    profiled__run_http_server_with_inline_processor,

]


def print_profiler_result(function_name):
    if function_name.startswith('profiled__'):
        prof_name = function_name + '.prof'
        prof_full_file_name = os.path.join(os.getcwd(), prof_name)
        s = pstats.Stats(prof_full_file_name)
        s = s.strip_dirs()
        s = s.sort_stats('cumtime', 'tottime', 'ncalls')
        # s.print_stats(.4)
        s.print_stats()
        # s.print_callees(['get_set_of_assumed_triangles'])


def main():
    # setup_console()
    # print('Проверка')

    make_af_unix_names()

    runner = TestsRunner(ALL_VARIANTS)
    tool_is_chosen, tool_number, input_raw_last_tool_id = runner.choose_and_run()

    # print(tool_is_chosen, tool_number, input_raw_last_tool_id)
    chosen_variant = ALL_VARIANTS[tool_number]
    print_profiler_result(chosen_variant.__name__)


def main_hardcoded():
    make_af_unix_names()

    profiled__run_non_blocking_server_benchmarking_client()
    print_profiler_result(profiled__run_non_blocking_server_benchmarking_client.__name__)

    # profiled__run_raw_non_blocking_server_benchmarking_client()
    # print_profiler_result(profiled__run_raw_non_blocking_server_benchmarking_client.__name__)


# def setup_console(sys_enc="utf-8"):
#     reload_module(sys)
#     try:
#         # для win32 вызываем системную библиотечную функцию
#         if sys.platform.startswith("win"):
#             import ctypes
#             enc = "cp%d" % ctypes.windll.kernel32.GetOEMCP() #TODO: проверить на win64/python64
#         else:
#             # для Linux всё, кажется, есть и так
#             enc = (sys.stdout.encoding if sys.stdout.isatty() else
#                         sys.stderr.encoding if sys.stderr.isatty() else
#                             sys.getfilesystemencoding() or sys_enc)
#
#         # кодировка для sys
#         sys.setdefaultencoding(sys_enc)
#
#         # переопределяем стандартные потоки вывода, если они не перенаправлены
#         if sys.stdout.isatty() and sys.stdout.encoding != enc:
#             sys.stdout = codecs.getwriter(enc)(sys.stdout, 'replace')
#
#         if sys.stderr.isatty() and sys.stderr.encoding != enc:
#             sys.stderr = codecs.getwriter(enc)(sys.stderr, 'replace')
#
#     except:
#         pass # Ошибка? Всё равно какая - работаем по-старому...

if __name__ == "__main__":
    with profiler_result(profile, print_result=True):
        main()
        # main_hardcoded()
