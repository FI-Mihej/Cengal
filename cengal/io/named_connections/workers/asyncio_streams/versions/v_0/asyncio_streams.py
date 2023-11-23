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


__all__ = ['ServerSideClient', 'create_server', 'start_server', 'ServerSideServer', 'CanNotEstablishNamedConnectionError', 'ClientSideClient', 'ClientSideServer']


from typing import Type
from cengal.parallel_execution.asyncio.efficient_streams import *
from cengal.io.named_connections.named_connections_manager import *
from cengal.parallel_execution.asyncio.atasks import create_task
from cengal.code_flow_control.smart_values import ValueCache, ValueExistence
from asyncio.tasks import sleep, Task
from asyncio.events import AbstractServer


class ServerSideClient(NamedConnectionsClient):
    def __init__(self, reader: StreamReaderAbstract, writer: StreamWriterAbstract, server_id: bytes, external_data_full_size: ValueExistence) -> None:
        super().__init__(server_id, external_data_full_size)
        self.reader: StreamReaderAbstract = reader
        self.writer: StreamWriterAbstract = writer
    
    async def serve(self):
        """client_connected_cb

        Returns:
            Any: _description_
        """        
        raise NotImplementedError
    
    # async def server(reader, writer):
    #     reader: StreamReaderAbstract = reader
    #     writer: StreamWriterAbstract = writer

    #     data = await reader.read(100)
    #     message = data.decode()
    #     addr = writer.get_extra_info('peername')

    #     print(f"Received {message!r} from {addr!r}")

    #     print(f"Send: {message!r}")
    #     # for i in range(100):
    #     #     writable_data = data * 1000000
    #     #     # print(f'writable_data len: {len(writable_data)}')
    #     #     writer.write(writable_data)

    #     data_chunk_len = int(CpuInfo().l2_cache_size_per_virtual_core / len(data))
    #     writer.start_aw()
    #     stime = perf_counter()
    #     dtime = 0
    #     return_time = 10
    #     index = 0
    #     while dtime < return_time:
    #         index += 1
    #         if 10 <= index:
    #             writer.owrite(pickle.dumps(PickleEncodableClass()))
    #             index = 0
    #         else:
    #             writer.owrite(marshal.dumps(data * randomized_data_size(data_chunk_len)))

    #         await writer.ar_drain_enough()
    #         dtime = perf_counter() - stime
        
    #     await writer.full_drain()

    #     print("Close the connection")
    #     writer.close()


async def create_server(server_side_client_type: Type[ServerSideClient], named_connections_manager: NamedConnectionsManager, stream_manager: StreamManagerAbstract, *args, **kwargs):
    async def client_connected_cb_wrapper(reader: StreamReaderAbstract, writer: StreamWriterAbstract):
        if not stream_manager.try_establish_message_protocol_server_side(reader, writer):
            raise CanNotEstablishNamedConnectionError
        
        server_id: bytes = await reader.read_message()
        named_connection_client: ServerSideClient = server_side_client_type(reader, writer, server_id, named_connections_manager.external_data_full_size)
        named_connections_manager.register_client(named_connection_client)
        await named_connection_client.serve()

    server: AbstractServer = stream_manager.start_server(client_connected_cb_wrapper, *args, **kwargs)
    return server


async def start_server(server: AbstractServer):
    async with server:
        await server.serve_forever()


ServerSideServer = NamedConnectionsServer


# ======================================================


class CanNotEstablishNamedConnectionError(Exception):
    pass


ClientSideClient = NamedConnectionsClient


class ClientSideServer(NamedConnectionsServer):
    def __init__(self, server_id: bytes, named_connections_manager: 'NamedConnectionsManager', stream_manager: StreamManagerAbstract, need_to_full_drain_on_connect: bool, *connection_args, **connection_kwargs) -> None:
        super().__init__(server_id, named_connections_manager)
        self._connected: bool = False
        self._stream_manager: StreamManagerAbstract = stream_manager
        self._need_to_full_drain_on_connect: bool = need_to_full_drain_on_connect
        self._connection_args = connection_args
        self._connection_kwargs = connection_kwargs
        self.autonomous_serving_future: Task = None
        self.reader: StreamReaderAbstract = None
        self.writer: StreamWriterAbstract = None
    
    async def serve(self):
        """Serve

        Returns:
            Any: _description_
        """        
        raise NotImplementedError
    
    async def connect(self):
        if self._connected:
            return
        
        reader, writer = self._stream_manager.open_connection(*self._connection_args, **self._connection_kwargs)
        self.reader = reader
        self.writer = writer
        if not self._stream_manager.try_establish_message_protocol_client_side(reader, writer):
            raise CanNotEstablishNamedConnectionError
        
        writer.optimized_write_message(self.id)
        if self._need_to_full_drain_on_connect:
            await writer.full_drain()
        
        self.autonomous_serving_future = create_task(self.serve)
        self._connected = True
    
    async def create_client(self, client_side_client_type: Type[ClientSideClient]):
        if not self._connected:
            await self.connect()
        
        return self.named_connections_manager().create_client(client_side_client_type, self.id)
