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
__version__ = "4.2.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.parallel_execution.asyncio.init_loop import init_loop, restore_default_loop
from cengal.parallel_execution.coroutines.integrations.uvloop import uvloop_install
from cengal.parallel_execution.asyncio.efficient_streams import *
from cengal.io.used_ports import *
from cengal.system import OS_TYPE

from typing import Dict
import asyncio
import json
from unittest import TestCase, main, skip, skipIf


# Raw protocol:

async def server_worker(server, reader, writer):
    reader: TcpStreamReader = reader
    writer: TcpStreamWriter = writer

    message_size_len_encoded = await reader.readexactly(8)
    message_size_len = int.from_bytes(message_size_len_encoded, 'little')
    data = await reader.readexactly(message_size_len)
    message_raw = bytes(data).decode()
    message_info: Dict = json.loads(message_raw)
    message: str = message_info['message']
    messages_num: int = message_info['messages_num']
    message_data: bytes = message.encode()

    writer.start_aw()
    try:
        while messages_num:
            messages_num -= 1
            writer.owrite(message_data)
            await writer.aw_drain_enough()
        
        await writer.full_drain()
    finally:
        writer.close()
        await writer.stop_aw()
        server.close()


async def server(port: int, server_ready: asyncio.Future):
    server = await TcpStreamManager().start_server(
        lambda reader, writer: server_worker(server, reader, writer), '127.0.0.1', port)

    async with server:
        server_ready.set_result(True)
        try:
            await server.serve_forever()
        except asyncio.exceptions.CancelledError:
            pass


async def client(port: int) -> bool:
    message: str = 'Hello World!'
    message_encoded: bytes = message.encode()
    messages_num: int = 1000
    message_info: Dict = {
        'message': message,
        'messages_num': messages_num
    }
    message_raw: str = json.dumps(message_info)
    data: bytes = message_raw.encode()
    message_size_len: int = len(data)
    message_size_len_encoded: bytes = message_size_len.to_bytes(8, 'little')

    reader, writer = await TcpStreamManager().open_connection(
        '127.0.0.1', port)

    writer.write(message_size_len_encoded)
    writer.write(data)
    await writer.drain()

    data_len_counter = 0
    data = None
    while data is None or data:
        data = await reader.read_nearly_max()
        data_len_counter += len(data)

    writer.close()
    return data_len_counter == (messages_num * len(message_encoded))


async def transmit(port: int) -> bool:
    server_ready: asyncio.Future = asyncio.Future()
    server_task = asyncio.create_task(server(port, server_ready))
    await server_ready
    client_task = asyncio.create_task(client(port))
    await asyncio.gather(server_task, client_task)
    result = client_task.result()
    return result


# Message protocol:

async def msg_server_worker(stream_manager: TcpStreamManager, server, reader, writer):
    if not await stream_manager.try_establish_message_protocol_server_side(reader, writer):
        raise RuntimeError('Failed to establish message protocol')

    reader: TcpStreamReader = reader
    writer: TcpStreamWriter = writer
    
    data: bytes = await reader.read_message()
    message_raw = bytes(data).decode()
    message_info: Dict = json.loads(message_raw)
    message: str = message_info['message']
    messages_num: int = message_info['messages_num']
    message_data: bytes = message.encode()

    with writer:
        async with writer.aw():
            while messages_num:
                messages_num -= 1
                writer.owrite_message(message_data)
                await writer.aw_drain_enough()
            
            await writer.full_drain()

    server.close()


async def msg_server(port: int, server_ready: asyncio.Future):
    stream_manager: TcpStreamManager = TcpStreamManager()
    server = await stream_manager.start_server(
        lambda reader, writer: msg_server_worker(stream_manager, server, reader, writer), '127.0.0.1', port)

    async with server:
        server_ready.set_result(True)
        try:
            await server.serve_forever()
        except asyncio.exceptions.CancelledError:
            pass


async def msg_client(port: int) -> bool:
    message: str = 'Hello World!'
    message_encoded: bytes = message.encode()
    messages_num: int = 1000
    message_info: Dict = {
        'message': message,
        'messages_num': messages_num
    }
    message_raw: str = json.dumps(message_info)
    data: bytes = message_raw.encode()

    stream_manager: TcpStreamManager = TcpStreamManager()
    reader, writer = await stream_manager.open_connection(
        '127.0.0.1', port)

    if not await stream_manager.try_establish_message_protocol_client_side(reader, writer):
        raise RuntimeError('Failed to establish message protocol')

    with writer:
        async with writer.aw():
            await writer.send_message(data)

            data_len_counter = 0
            data = None
            while data is None or data:
                try:
                    data = await reader.read_message()
                except asyncio.exceptions.IncompleteReadError:
                    data = bytes()
                
                data_len_counter += len(data)

    return data_len_counter == (messages_num * len(message_encoded))


async def msg_transmit(port: int) -> bool:
    server_ready: asyncio.Future = asyncio.Future()
    server_task = asyncio.create_task(msg_server(port, server_ready))
    await server_ready
    client_task = asyncio.create_task(msg_client(port))
    await asyncio.gather(server_task, client_task)
    result = client_task.result()
    return result


class TestTcpEfficientStream(TestCase):
    def setUp(self):
        restore_default_loop()
        init_loop()

    def test_transmit(self):
        port = purify_ports(used_ports().port(Protocol.tcp, used_ports().tables[Table.user], {PortStatus.no})())
        result = asyncio.run(transmit(port))
        self.assertTrue(result)

    def test_msg_transmit(self):
        port = purify_ports(used_ports().port(Protocol.tcp, used_ports().tables[Table.user], {PortStatus.no})())
        result = asyncio.run(msg_transmit(port))
        self.assertTrue(result)


if __name__ == '__main__':
    main()
