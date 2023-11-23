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


#!/usr/bin/env python
# coding=utf-8




"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""





import asyncio
from time import perf_counter
# from efficient_streams import *
from cengal.parallel_execution.asyncio.efficient_streams import *
from cengal.hardware.info.cpu.versions.v_1 import CpuInfo
from cengal.io.used_ports import *
from random import random
import marshal
import pickle


asyncio.selector_events._SelectorTransport.max_size = CpuInfo().l2_cache_size_per_virtual_core
asyncio.selector_events._DEFAULT_LIMIT = CpuInfo().l2_cache_size_per_virtual_core


class PickleEncodableClass:
    def __init__(self) -> None:
        self.name = 'ad;slfakldjgldskfj'
        self.d = [{
            'asdf': 243.0,
            2: [0] * 3000,
            ('asdf', 345): [('erihtserkdhtg', (3, 4, 5))] * 100000,
            ('hjg', 55): [('erihtserkdhtg', (3, 4, 5))] * 100000,
        }] * 100000

st = perf_counter()
dumped_data = pickle.dumps(PickleEncodableClass())
dt = perf_counter() - st
print(f'PickleEncodableClass size: {len(dumped_data)}; time: {dt}')


def randomized_data_size(data_size: int) -> int:
    offset = 0.1
    range = 10.0
    ran = random()
    result = offset + range * ran
    return round(data_size * result)


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    # for i in range(100):
    #     writable_data = data * 1000000
    #     # print(f'writable_data len: {len(writable_data)}')
    #     writer.write(writable_data)

    data_chunk_len = int(CpuInfo().l2_cache_size_per_virtual_core / len(data))
    stime = perf_counter()
    dtime = 0
    return_time = 10
    index = 0
    while dtime < return_time:
        writable_data = data * randomized_data_size(data_chunk_len)
        # print(f'writable_data len: {len(writable_data)}')
        index += 1
        if 10 <= index:
            writer.write(pickle.dumps(PickleEncodableClass()))
            index = 0
        else:
            writer.write(marshal.dumps(writable_data))

        await writer.drain()
        dtime = perf_counter() - stime

    print("Close the connection")
    writer.close()

async def handle_echo_1(reader, writer):
    reader: StreamReader = reader
    writer: StreamWriter = writer

    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    # for i in range(100):
    #     writable_data = data * 1000000
    #     # print(f'writable_data len: {len(writable_data)}')
    #     writer.write(writable_data)

    data_chunk_len = int(CpuInfo().l2_cache_size_per_virtual_core / len(data))
    stime = perf_counter()
    dtime = 0
    return_time = 10
    index = 0
    while dtime < return_time:
        index += 1
        if 10 <= index:
            writer.owrite(pickle.dumps(PickleEncodableClass()))
            index = 0
        else:
            writer.owrite(marshal.dumps(data * randomized_data_size(data_chunk_len)))

        await writer.partial_drain()
        dtime = perf_counter() - stime
    
    await writer.full_drain()

    print("Close the connection")
    writer.close()

async def handle_echo_2(reader, writer):
    reader: StreamReader = reader
    writer: StreamWriter = writer

    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    # for i in range(100):
    #     writable_data = data * 1000000
    #     # print(f'writable_data len: {len(writable_data)}')
    #     writer.write(writable_data)

    data_chunk_len = int(CpuInfo().l2_cache_size_per_virtual_core / len(data))
    writer.start_aw()
    stime = perf_counter()
    dtime = 0
    return_time = 10
    index = 0
    while dtime < return_time:
        index += 1
        if 10 <= index:
            writer.owrite(pickle.dumps(PickleEncodableClass()))
            index = 0
        else:
            writer.owrite(marshal.dumps(data * randomized_data_size(data_chunk_len)))

        await writer.ar_drain_enough()
        dtime = perf_counter() - stime
    
    await writer.full_drain()

    print("Close the connection")
    writer.close()

async def main():
    port = purify_ports(used_ports().port(Protocol.tcp, used_ports().tables[Table.user], {PortStatus.no})())
    # server = await asyncio.start_server(
    #     handle_echo, '127.0.0.1', port)
    # server = await StreamManager().start_server(
    #     handle_echo, '127.0.0.1', port)
    # server = await StreamManager().start_server(
    #     handle_echo_1, '127.0.0.1', port)
    server = await StreamManager().start_server(
        handle_echo_2, '127.0.0.1', port)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())