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


from cengal.data_generation.id_generator import IDGenerator
from cengal.data_containers.fast_fifo import FIFODequeWithLengthControl
from cengal.code_flow_control.smart_values import ValueCache, ValueExistence
from weakref import ref, ReferenceType
from typing import Optional, Set, Dict, List, Tuple, Callable, Awaitable, Sequence, Type


# class NamedConnectionsTransport:
#     def disconnect(self):
#         raise NotImplementedError
    
#     def disconnected(self):
#         ...
    
#     def eof(self) -> bool:
#         ...


class NamedConnectionsClient:
    def __init__(self, server_id: bytes, external_data_full_size: ValueExistence) -> None:
        self.id = None
        self.server_id: bytes = server_id
        self.server_ref: Optional[ReferenceType['NamedConnectionsServer']] = None
        self.input_from_client: FIFODequeWithLengthControl = FIFODequeWithLengthControl(external_data_full_size)
        self.output_to_client: FIFODequeWithLengthControl = FIFODequeWithLengthControl(external_data_full_size)
    
    def callback__bind(self, server: 'NamedConnectionsServer'):
        """Server can emit this callback

        Args:
            server (NamedConnectionsServer): _description_
        """
        self.server_ref = ref(server)
    
    def callback__unbind(self):
        """Server can emit this callback
        """
        self.server_ref = None

    def callback__data_to_client_added(self):
        """Server can emit this callback

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError
    
    def callback__server_ready_for_data(self):
        """Server can emit this callback

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError

    def callback__is_client_ready_for_data(self) -> bool:
        """Server can emit this callback

        Raises:
            NotImplementedError: _description_

        Returns:
            bool: _description_
        """
        raise NotImplementedError
    
    def callback__stop(self):
        """Server can emit this callback. No additional data from the server will be provided. No read from the server side will be made.

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError
    
    def data_to_server_added(self):
        """Client can call this method
        """
        server = self.server_ref()
        if server:
            server.callback__data_to_server_added(self)
    
    def is_server_ready_for_data(self) -> bool:
        """Client can call this method

        Returns:
            bool: _description_
        """
        server = self.server_ref()
        if server:
            return server.callback__is_server_ready_for_data(self)
        else:
            return False

    def client_ready_for_data(self):
        """Client can call this method
        """
        server = self.server_ref()
        if server:
            server.callback__client_ready_for_data(self)
    
    def stop(self):
        """Client can call this method. Server should not call it. Server should call NamedConnectionsClient.callback__stop() when wants to close connection
        """
        server = self.server_ref()
        if server:
            server.callback__client_stopped(self)



class NamedConnectionsServer:
    # def __init__(self, server_id: bytes, named_connections_manager: Optional['NamedConnectionsManager'] = None) -> None:
    #     self.id: bytes = server_id
    #     if named_connections_manager:
    #         self.named_connections_manager: ReferenceType['NamedConnectionsManager'] = ref(named_connections_manager)
    #     else:
    #         self.named_connections_manager = None
        
    #     self.bind_clients: Dict[int, NamedConnectionsClient] = dict()

    def __init__(self, server_id: bytes, named_connections_manager: 'NamedConnectionsManager') -> None:
        self.id: bytes = server_id
        self.named_connections_manager: ReferenceType['NamedConnectionsManager'] = ref(named_connections_manager)
        self.bind_clients: Dict[int, NamedConnectionsClient] = dict()

    def bind(self, client: NamedConnectionsClient):
        self.bind_clients[client.id] = client
        client.callback__bind(self)

    def unbind(self, client: NamedConnectionsClient):
        try:
            del self.bind_clients[client.id]
        except KeyError:
            pass
        finally:
            client.callback__unbind()
    
    def callback__data_to_server_added(self, client: NamedConnectionsClient):
        raise NotImplementedError
    
    def callback__is_server_ready_for_data(self, client: NamedConnectionsClient) -> bool:
        raise NotImplementedError

    def callback__client_ready_for_data(self, client: NamedConnectionsClient):
        raise NotImplementedError
    
    def callback__client_stopped(self, client: NamedConnectionsClient):
        """Client can emit this callback. No additional data from the client will be provided. No read from the client side will be made.

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError


class NamedConnectionsManager:
    def __init__(self, external_data_full_size: ValueExistence) -> None:
        self.external_data_full_size: ValueExistence = external_data_full_size
        self.gen_client_id: IDGenerator = IDGenerator()
        self.unbind_clients: Dict[int, NamedConnectionsClient] = dict()
        self.unbind_clients_per_server: Dict[str, Set[NamedConnectionsClient]] = dict()
        self.bind_clients: Dict[int, NamedConnectionsClient] = dict()
        self.servers: Dict[bytes, NamedConnectionsServer] = dict()
    
    def create_client(self, client_type: Type[NamedConnectionsClient], server_id: bytes) -> NamedConnectionsClient:
        client: NamedConnectionsClient = client_type(server_id, self.external_data_full_size)
        client_id = self.gen_client_id()
        client.id = client_id
        if server_id in self.servers:
            self.bind_clients[client_id] = client
            self.servers[server_id].bind(client)
        else:
            self._unbind_client_impl(client)
        
        return client_id
    
    def register_client(self, client: NamedConnectionsClient) -> int:
        server_id: bytes = client.server_id
        client_id = self.gen_client_id()
        client.id = client_id
        if server_id in self.servers:
            self.bind_clients[client_id] = client
            self.servers[server_id].bind(client)
        else:
            self.unbind_clients[client_id] = client
            if server_id not in self.unbind_clients_per_server:
                self.unbind_clients_per_server[server_id] = set()
            
            self.unbind_clients_per_server[server_id].add(client)
        
        return client_id

    def register_server(self, server: NamedConnectionsServer):
        server_id: bytes = server.id
        if server_id in self.servers:
            raise RuntimeError('NamedConnectionsServer already registered')
        
        self.servers[server_id] = server
        if server_id in self.unbind_clients_per_server:
            unbind_clients = self.unbind_clients_per_server[server_id]
            del self.unbind_clients_per_server[server_id]
            for client in unbind_clients:
                del self.unbind_clients[client.id]
                self.bind_clients[client.id] = client
                server.bind(client)

    def unregister_server(self, server: NamedConnectionsServer):
        server_clients = server.bind_clients.items()
        for client_id, client in server_clients:
            self.unbind_client(client)
        
        try:
            del self.servers[server.id]
        except KeyError:
            pass

    def unregister_client(self, client: NamedConnectionsClient):
        server = client.server_ref()
        if server:
            server.unbind(client)
        
        client_id = client.id
        self.bind_clients.pop(client_id, None)
        self.unbind_clients.pop(client_id, None)
        try:
            self.unbind_clients_per_server[client.server_id].discard(client)
        except KeyError:
            pass

    def unbind_client(self, client: NamedConnectionsClient):
        server = client.server_ref()
        if server:
            server.unbind(client)

        self._unbind_client_impl(client)

    def _unbind_client_impl(self, client: NamedConnectionsClient):
        client_id = client.id
        server_id = client.server_id
        self.bind_clients.pop(client_id, None)
        self.unbind_clients[client_id] = client
        if server_id not in self.unbind_clients_per_server:
            self.unbind_clients_per_server[server_id] = set()
        
        self.unbind_clients_per_server[server_id].add(client)

    def rebind_client(self, client: NamedConnectionsClient, server_id: bytes):
        """Force rebind client to another server
        """
        self.servers[client.server_id].unbind(client)
        client.server_id = server_id
        self.servers[server_id].bind(client)
    
    # def put_client_message_to_server_queue(self, message):
    #     ...
    
    # def put_server_message_to_client_queue(self, message):
    #     ...
    
    # def client_to_server_queue_len(self):
    #     ...
    
    # def server_to_client_queue_len(self):
    #     ...
