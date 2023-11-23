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
# from efficient_streams import *
from cengal.parallel_execution.asyncio.efficient_streams import *
from time import perf_counter
from cengal.hardware.info.cpu.versions.v_1 import CpuInfo
from cengal.io.used_ports import *


# asyncio.selector_events._SelectorTransport.max_size = CpuInfo().l2_cache_size_per_virtual_core
# asyncio.selector_events._DEFAULT_LIMIT = CpuInfo().l2_cache_size_per_virtual_core


print('STARTED.')


async def read_with_counter(reader):
    if reader._exception is not None:
        raise reader._exception

    # This used to just loop creating a new waiter hoping to
    # collect everything in self._buffer, but that would
    # deadlock if the subprocess sends more than self.limit
    # bytes.  So just call self.read(self._limit) until EOF.
    blocks = []
    counter = 0
    while True:
        block = await reader.read(reader._limit)
        counter += 1
        if not block:
            break
        blocks.append(block)
    return b''.join(blocks), counter


async def tcp_echo_client(message):
    port = purify_ports(used_ports().port(Protocol.tcp, used_ports().tables[Table.user], {PortStatus.no})())
    # reader, writer = await asyncio.open_connection(
    #     '127.0.0.1', port)
    reader, writer = await StreamManager().open_connection(
        '127.0.0.1', port)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    # await asyncio.sleep(10)
    start_time = perf_counter()
    data_len_counter = 0
    io_counter = 0
    data = None
    while data is None or data:
        # data = await reader.read(100 * 1024**2)
        # data, counter = await reader.read()
        # data, counter = await read_with_counter(reader)

        # data, counter = await reader.read_with_counter()
        # io_counter += counter

        data = await reader.read_nearly_max()
        io_counter += 1
        data_len_counter += len(data)
        # print(f'Received: {data.decode()!r}')

    print(f'io_counter: {io_counter}')
    print(f'Bytes received: {data_len_counter}')
    end_time = perf_counter()
    diff_time = end_time - start_time
    if 0 != diff_time:
        speed = data_len_counter / diff_time
        print(f'Bytes per second: {speed}')

    print('Close the connection')
    writer.close()

asyncio.run(tcp_echo_client('Hello World!'))