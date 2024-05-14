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


__all__ = []


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"

# test.py
from cengal.time_management.cpu_clock_cycles import perf_counter
from cengal.io.serve_free_ports import simple_port_search
from cengal.io.used_ports import PortsIterator, used_ports, Protocol, PortStatus, unify_ports, purify_ports
from cengal.time_management.run_time import RT
from cengal.performance_test_lib import test_run_time, measure_time
from cengal.introspection.inspect import pdi, gmsodi
from cengal.code_inspection.line_tracer import nln
from cengal.code_inspection.auto_line_tracer import AutoLineTracer, CodeStartReplType, ts, alt
# from cengal.code_inspection.auto_line_tracer import fts as ts
from cengal.parallel_execution.coroutines.integrations.nim__netty.core.versions.v_0.compilable import serve, client, connect, tick
# import cengal.parallel_execution.coroutines.integrations.nim__netty.core.versions.v_0.compilable as netty_core
# import cengal.parall .netty_core as mymodule
from warnings import warn
from time import sleep
from typing import Dict, List, Any


NimObj = Dict[str, Any]


def main():
    alt.print_start()
    host = '0.0.0.0'
    ports_range = slice(18000, 18100)
    port: int = simple_port_search('0.0.0.0', ports_range, Protocol.tcp, {PortStatus.na, PortStatus.no}, 5.0)
    if port is None:
        warn(f'Can\'t find free port for the server in ther [{ports_range.start}, ..., {ports_range.stop}] range. Exiting...')
        return
    
    server_reactors: List[NimObj] = ts(serve([{'host': host, 'port': port}]))
    
    client_connections: List[NimObj] = ts(connect([{'host': host, 'port': port}]))
    
    our_connection = ts(client_connections[0])
    with measure_time(f'line: {nln()}'):
        tick_result = ts(tick(dict(), {our_connection['id']: ['Hello, Nim!']}))
    
    for connection_id, messages in tick_result['server_received'].items():
        for message in messages:
            print(len(message))
            ts(message)
    
    sleep(0.1)
    with measure_time(f'line: {nln()}'):
        tick_result = ts(tick(dict(), dict()))
    
    for connection_id, messages in tick_result['server_received'].items():
        for message in messages:
            print(len(message))
            ts(message)
    
    sleep(0.1)
    with measure_time(f'line: {nln()}'):
        tick_result = ts(tick(dict(), dict()))
    
    for connection_id, messages in tick_result['server_received'].items():
        for message in messages:
            print(len(message))
            ts(message)

    with RT() as rt:
        client_obj = client()
    
    print(rt.rt, 1 / rt.rt)
    ts(client_obj)
    
    print(len(client_obj))

    messages_num = 500
    with test_run_time(f'Transmitting {messages_num} messages. line: {nln()}', messages_num + 1, ignore_index=True):
        received_messages = []
        index = messages_num
        messages = [f'{index} Hello, Nim!' for index in range(messages_num)]
        client_connection_id = our_connection['id']
        tick(dict(), {client_connection_id: messages})
        while index:
            tick_result = tick(dict(), dict())
            for connection_id, messages in tick_result['server_received'].items():
                for message in messages:
                    received_messages.append(message)
                    index -= 1

    messages_num = 20
    start_time = perf_counter()
    received_messages = []
    messages = [f'{index} Hello, Nim!' for index in range(messages_num)]
    client_connection_id = our_connection['id']
    tick(dict(), {client_connection_id: messages})
    index = 0
    while 5.0 > perf_counter() - start_time:
        index += 1
        tick_result = tick(dict(), {client_connection_id: messages})
        for connection_id, messages in tick_result['server_received'].items():
            for message in messages:
                received_messages.append(message)
    
    stop_time = perf_counter()
    dtime = stop_time - start_time
    print(f'{index} * {messages_num} = {index * messages_num} messages sent')
    print(f'{len(received_messages)} messages received')
    print(f'transmission speed: {len(received_messages) / dtime} messages per second')
    
    # for message in received_messages:
    #     print(len(message))
    #     ts(message)

    alt.print_end()


if '__main__' == __name__:
    main()
