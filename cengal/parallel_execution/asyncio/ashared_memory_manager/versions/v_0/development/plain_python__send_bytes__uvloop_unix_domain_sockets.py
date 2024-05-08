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
__version__ = "4.4.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import asyncio
import os
import uvloop
from cengal.performance_test_lib import MeasureTimeTraceLine


socket_path = "/tmp/asyncio_domain_socket_uv"

async def unix_server():
    server = await asyncio.start_unix_server(handle_client, path=socket_path)
    print(f"Server listening on {socket_path}")
    async with server:
        await server.serve_forever()

async def handle_client(reader, writer):
    try:
        with MeasureTimeTraceLine('Reader', iterations=1000) as mt:
            while True:
                data = await reader.read(300000)
                if not data:
                    break
    finally:
        print(f'Reader Throughput: {(300000 * mt.iterations) / mt.time_spent:.2f} bytes per second')
        print()

        print("Closing client connection")
        writer.close()
        await writer.wait_closed()

async def unix_client():
    while not os.path.exists(socket_path):
        await asyncio.sleep(0.1)

    reader, writer = await asyncio.open_unix_connection(socket_path)
    try:
        data = bytes([255] * 300000)
        with MeasureTimeTraceLine('Writer', iterations=1000) as mt:
            for i in range(mt.iterations):
                writer.write(data)
                await writer.drain()
            
            writer.write_eof()
    finally:
        print(f'Writer Throughput: {(300000 * mt.iterations) / mt.time_spent:.2f} bytes per second')
        print()

        writer.close()
        await writer.wait_closed()
        print("Client has finished sending data")

async def main():
    # Ensure the socket file is cleaned up before starting
    try:
        os.unlink(socket_path)
    except FileNotFoundError:
        pass

    server_task = asyncio.create_task(unix_server())
    client_task = asyncio.create_task(unix_client())

    await client_task  # Wait for the client to finish
    server_task.cancel()  # Cancel the server

if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.run(main())
