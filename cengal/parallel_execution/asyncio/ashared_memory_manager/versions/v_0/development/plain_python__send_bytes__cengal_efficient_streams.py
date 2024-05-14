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
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import asyncio
from cengal.parallel_execution.asyncio.efficient_streams import *
from cengal.performance_test_lib import MeasureTimeTraceLine


async def send_data(writer):
    data = bytes([255] * 300000)  # Generate a data block of 300000 bytes
    with MeasureTimeTraceLine('send_data', iterations=1000) as mt:
        for i in range(mt.iterations):
            writer.write(data)
            await writer.drain()
            
    print(f'Throughput: {(300000 * mt.iterations) / mt.time_spent:.2f} bytes per second')
    print()
    
    print("Finished sending data")
    writer.close()
    await writer.wait_closed()

async def receiver(reader, writer):
    try:
        with MeasureTimeTraceLine('receiver', iterations=1000) as mt:
            while True:
                data = await reader.read(300000)
                if not data:
                    break
    finally:
        print(f'Throughput: {(300000 * mt.iterations) / mt.time_spent:.2f} bytes per second')
        print()

        print("Closing connection")
        writer.close()
        await writer.wait_closed()

async def run_server():
    server = await TcpStreamManager().start_server(receiver, '127.0.0.1', 8888)
    async with server:
        addr = server.sockets[0].getsockname()
        print(f"Serving on {addr}")
        await server.serve_forever()

async def run_client():
    await asyncio.sleep(1)  # Delay to ensure server starts first
    reader, writer = await TcpStreamManager().open_connection('127.0.0.1', 8888)
    await send_data(writer)

async def main():
    server = asyncio.create_task(run_server())
    await asyncio.sleep(0.1)  # Ensure server starts before client attempts to connect
    client = asyncio.create_task(run_client())

    await client  # Wait for the client to finish
    server.cancel()  # Stop the server

if __name__ == "__main__":
    asyncio.run(main())
