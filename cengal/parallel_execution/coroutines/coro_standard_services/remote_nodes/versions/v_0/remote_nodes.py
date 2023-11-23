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


__all__ = ['RemoteNodes', 'RemoteNodesRequest']

from enum import Enum
from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_tools.await_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import *
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import CoroPriority
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.timer_func_runner import *
from cengal.file_system.file_manager import path_relative_to_current_dir
from cengal.time_management.load_best_timer import perf_counter
from cengal.data_manipulation.serialization import *
from typing import Hashable, Tuple, List, Any, Dict, Callable, Type
from cengal.introspection.inspect import get_exception, entity_owning_module_importable_str, entity_owning_module_info_and_owning_path, entity_properties
from cengal.io.core.memory_management import IOCoreMemoryManagement
from cengal.parallel_execution.asyncio.efficient_streams import StreamManagerIOCoreMemoryManagement, TcpStreamManager, UdpStreamManager, StreamManagerAbstract
from cengal.code_flow_control.smart_values import ValueExistence
from cengal.io.named_connections.named_connections_manager import NamedConnectionsManager
from cengal.code_flow_control.args_manager import number_of_provided_args
from cengal.data_manipulation.serialization import Serializer, Serializers, best_serializer
from cengal.code_flow_control.args_manager import find_arg_position_and_value, UnknownArgumentError
from cengal.data_generation.id_generator import IDGenerator, GeneratorType
from cengal.system import PLATFORM_NAME, PYTHON_VERSION
from importlib import import_module
import sys
import os
import asyncio
import lmdb

from .exceptions import *
from .commands import *
from .class_info import *
from .request_class_info import *
from .remote_node import *
from .serializers import *


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


class RemoteNodesRequest(ServiceRequest):
    def start(self, host=None, port=None, tls: bool = True, stream_manager: Optional[StreamManagerAbstract] = None) -> ServiceRequest:
        return self._save(0, host, port)
    def stop(self) -> ServiceRequest:
        return self._save(1)
    def connect(self, host=None, port=None, connection_id_alias=None, tls: bool = True, stream_manager: Optional[StreamManagerAbstract] = None) -> ServiceRequest:
        return self._save(2, host, port, connection_id_alias)
    def disconnect(self, connection_id) -> ServiceRequest:
        return self._save(3, connection_id)


class State(Enum):
    start_initiated = 0
    started = 1
    stop_initiated = 2
    stopped = 3


def is_current_platform(current_platform_name, foreign_platform_name):
    return current_platform_name == foreign_platform_name


class RemoteNodes(DualImmediateProcessingServiceMixin, Service, EntityStatsMixin):
    def __init__(self, loop: CoroScheduler):
        super(RemoteNodes, self).__init__(loop)
        self._request_workers = {
            0: self._on_start,
            1: self._on_stop,
            2: self._on_connect,
            2: self._on_disconnect,
        }
        self.platform_name: str = f'{PLATFORM_NAME}-{".".join(PYTHON_VERSION)}'
        self.state: State = State.stopped
        self.servers: Dict[Hashable, RemoteServer] = dict()
        self.clients: Dict[Hashable, RemoteClient] = dict()

        self.serializer__current_platform__custom_types: Serializer = best_serializer({
            DataFormats.any,
            Tags.current_platform,
            Tags.deep,
            Tags.can_use_custom_types,
            Tags.can_use_bytes,
            Tags.can_use_set,
            Tags.decode_str_as_str,
            Tags.decode_bytes_as_bytes,
            Tags.decode_tuple_as_tuple,
            Tags.decode_list_as_list,
        }, test_data_factory(TestDataType.deep_large), 0.1)
        print(self.serializer__current_platform__custom_types.serializer)

        self.serializer__current_platform: Serializer = best_serializer({
            DataFormats.any,
            Tags.deep,
            Tags.can_use_set,
            Tags.can_use_bytes,
            Tags.decode_str_as_str,
            Tags.decode_bytes_as_bytes,
            Tags.decode_tuple_as_tuple,
            Tags.decode_list_as_list,
        }, test_data_factory(TestDataType.deep_large), 0.1)
        print(self.serializer__current_platform.serializer)

        self.serializer__multi_platform: Serializer = best_serializer({
            DataFormats.any,
            Tags.deep,
            Tags.multi_platform,
            Tags.can_use_bytes,
            Tags.decode_str_as_str,
            Tags.decode_list_as_list,
        }, test_data_factory(TestDataType.deep_large), 0.1)
        print(self.serializer__multi_platform.serializer)

        self.serializer__multi_platform_fast: Serializer = best_serializer({
            DataFormats.any,
            Tags.deep,
            Tags.multi_platform,
            Tags.can_use_bytes,
        }, test_data_factory(TestDataType.small), 0.1)
        print(self.serializer__multi_platform_fast.serializer)

        self.serializer__multi_platform__initial_communication: Serializer = best_serializer({
            DataFormats.json,
            Tags.deep,
            Tags.multi_platform,
        }, test_data_factory(TestDataType.small), 0.1)
        print(self.serializer__multi_platform_fast.serializer)
    
    def serialize(self, foreign_platform_name, data) -> Tuple[Serializer, SerializerID, bytes]:
        """_summary_

        Args:
            foreign_platform_name (_type_): _description_
            data (_type_): _description_

        Raises:
            MessageDataCanNotBeSerializedForRequestedNodeError: _description_

        Returns:
            Tuple[Serializer, SerializerID, bytes]: _description_
        """        
        current_platform = is_current_platform(self.platform_name, foreign_platform_name)
        if current_platform:
            serializer_id: SerializerID = SerializerID.current_platform
            serializer: Serializer = self.serializer__current_platform
        else:
            serializer_id = SerializerID.multi_platform
            serializer = self.serializer__multi_platform
        
        try:
            return serializer, serializer_id, serializer.dumps(data)
        except:
            if not current_platform:
                raise MessageDataCanNotBeSerializedForRequestedNodeError
        
        serializer_id = SerializerID.current_platform__custom_types
        serializer = self.serializer__current_platform__custom_types
        return serializer, serializer_id, serializer.dumps(data)
    
    def deserialize(self, serializer_id: int, data: bytes) -> Any:
        """_summary_

        Args:
            serializer_id (int): _description_
            data (bytes): _description_

        Raises:
            UnknownSerializerIDError: _description_

        Returns:
            Any: _description_
        """        
        if SerializerID.multi_platform_fast.value == serializer_id:
            serializer: Serializer = self.serializer__multi_platform_fast
        elif SerializerID.multi_platform.value == serializer_id:
            serializer = self.serializer__multi_platform
        elif SerializerID.current_platform.value == serializer_id:
            serializer = self.serializer__current_platform
        elif SerializerID.current_platform__custom_types.value == serializer_id:
            serializer = self.serializer__current_platform__custom_types
        else:
            raise UnknownSerializerIDError(serializer_id)

        return serializer.loads(data)
    
    def serialize_request(self, server_id: Hashable, args, kwargs) -> bytes:
        """_summary_

        Args:
            server_id (Hashable): _description_
            args (_type_): _description_
            kwargs (_type_): _description_

        Raises:
            MessageCanNotBeEmptyError: _description_
            RuntimeError: _description_
            RuntimeError: _description_

        Returns:
            bytes: _description_
        """        
        result: bytes = None
        remote_server: RemoteServer = self.servers[server_id]
        remotely_registered_service_classes: Dict[Type, LocalClassInfo] = remote_server.remotely_registered_service_classes
        remotely_registered_request_classes: Dict[Type, LocalRequestClassInfo] = remote_server.remotely_registered_request_classes
        try:
            is_raw_request: bool = False
            service_type_param_name: str = 'service_type'
            request_param_name: str  = 'request'
            if 0 == number_of_provided_args(args, kwargs):
                # an error
                raise MessageCanNotBeEmptyError
            elif 2 == number_of_provided_args(args, kwargs):
                service_type: Type[Service] = None
                request_obj: Request = None
                params = {service_type_param_name: 0, request_param_name: 1}
                service_type_param_found, service_type_param_pos, service_type_param_value = find_arg_position_and_value(service_type_param_name, params, args, kwargs)
                if service_type_param_found:
                    if isinstance(service_type_param_value, type) and issubclass(service_type_param_value, Service):
                        service_type = service_type_param_value
                    else:
                        is_raw_request = True
                else:
                    is_raw_request = True
                
                if not is_raw_request:
                    request_param_found, request_param_pos, request_param_value = find_arg_position_and_value(request_param_name, params, args, kwargs)
                    if request_param_found:
                        if isinstance(request_param_value, Request):
                            request_obj = request_param_value
                        else:
                            is_raw_request = True
                    else:
                        is_raw_request = True
                
                if not is_raw_request:
                    if (service_type is None) or (request_obj is None):
                        raise RuntimeError  # executed only if there is some bug in code
                    
                    # check service existance
                    new_service: bool = False
                    if service_type not in remotely_registered_service_classes:
                        new_service = True
                        remote_server.register_service_class(service_type)

                    local_service_class_info: LocalClassInfo = remotely_registered_service_classes[service_type]
                    messages: List[bytes] = list()
                    
                    # register new service
                    if new_service:
                        sys_data: Dict = local_service_class_info()
                        request: Dict = {
                            Fields.command_name.value: Commands.declare_service_class.value,
                            Fields.request_id.value: remote_server.gen_request_id(),
                            Fields.data.value: sys_data,
                        }
                        serialized_request: bytes = self.serializer__multi_platform_fast.dumps(request)
                        messages.append(serialized_request)
                    
                    request_obj_type: Type[Request] = type(request_obj)

                    # check request type existance
                    new_request_type: bool = False
                    if request_obj_type not in remotely_registered_request_classes:
                        new_request_type = True
                        remote_server.register_request_class(request_obj)

                    local_request_class_info: LocalRequestClassInfo = remotely_registered_request_classes[request_obj_type]
                    
                    # register new request type
                    if new_request_type:
                        sys_data: Dict = local_request_class_info()
                        request: Dict = {
                            Fields.command_name.value: Commands.declare_service_request_class.value,
                            Fields.request_id.value: remote_server.gen_request_id(),
                            Fields.data.value: sys_data,
                        }
                        serialized_request: bytes = self.serializer__multi_platform_fast.dumps(request)
                        messages.append(serialized_request)

                    # - actual request to service
                    request_data: Dict = local_request_class_info.request_to_data(request_obj)
                    request_data[CommandDataFieldsServiceRequestWithRequestClass.service_class_id.value] = local_service_class_info.local_id
                    _, serializer_id, request_data = self.serialize(remote_server.foreign_platform_name, request_data)
                    request: Dict = {
                        Fields.command_name.value: Commands.send_service_request_with_request_class.value,
                        Fields.request_id.value: remote_server.gen_request_id(),
                        Fields.is_response_required.value: 1,
                        Fields.data_serializer_id.value: serializer_id.value,
                        Fields.data.value: request_data,
                    }
                    
                    serialized_request: bytes = self.serializer__multi_platform_fast.dumps(request)
                    messages.append(serialized_request)
                    result = b''.join(messages)
            else:
                params = {service_type_param_name: 0}
                found, pos, value = find_arg_position_and_value(service_type_param_name, params, args, kwargs)
                if found:
                    if pos is None:
                        del kwargs[service_type_param_name]
                    else:
                        args = args[1:]
                    
                    if isinstance(value, type) and issubclass(value, Service):
                        service_type: Type[Service] = value

                        # check service existance
                        new_service: bool = False
                        if service_type not in remotely_registered_service_classes:
                            new_service = True
                            remote_server.register_service_class(service_type)

                        local_service_class_info: LocalClassInfo = remotely_registered_service_classes[service_type]
                        
                        messages: List[bytes] = list()
                        
                        # register new service
                        if new_service:
                            sys_data: Dict = local_service_class_info()
                            request: Dict = {
                                Fields.command_name.value: Commands.declare_service_class.value,
                                Fields.request_id.value: remote_server.gen_request_id(),
                                Fields.data.value: sys_data,
                            }
                            serialized_request: bytes = self.serializer__multi_platform_fast.dumps(request)
                            messages.append(serialized_request)

                        # actual request to service
                        request_data: Dict = {
                            CommandDataFieldsServiceRequest.service_class_id.value: local_service_class_info.local_id,
                        }
                        explicit_serializer_required: bool = False
                        if args:
                            explicit_serializer_required = True
                            request_data[CommandDataFieldsServiceRequest.args.value] = args
                        
                        if kwargs:
                            explicit_serializer_required = True
                            request_data[CommandDataFieldsServiceRequest.kwargs.value] = kwargs
                        
                        if explicit_serializer_required:
                            _, serializer_id, request_data = self.serialize(remote_server.foreign_platform_name, request_data)
                        
                        request: Dict = {
                            Fields.command_name.value: Commands.send_service_request.value,
                            Fields.request_id.value: remote_server.gen_request_id(),
                            Fields.is_response_required.value: 1,
                            Fields.data.value: request_data,
                        }
                        if explicit_serializer_required:
                            request[Fields.data_serializer_id.value] = serializer_id.value
                        
                        serialized_request: bytes = self.serializer__multi_platform_fast.dumps(request)
                        messages.append(serialized_request)
                        result = b''.join(messages)
                    else:
                        is_raw_request = True
                else:
                    is_raw_request = True
            
            if is_raw_request:
                # raw request
                request_data: Dict = {
                    CommandDataFieldsRequest.args.value: args,
                    CommandDataFieldsRequest.kwargs.value: kwargs,
                }
                _, serializer_id, request_data = self.serialize(remote_server.foreign_platform_name, request_data)
                
                request: Dict = {
                    Fields.command_name.value: Commands.send_request.value,
                    Fields.request_id.value: remote_server.gen_request_id(),
                    Fields.is_response_required.value: 1,
                    Fields.data_serializer_id.value: serializer_id.value,
                    Fields.data.value: request_data,
                }
                
                result = self.serializer__multi_platform_fast.dumps(request)
        except UnknownArgumentError:
            raise RuntimeError  # executed only if there is some bug in code
        
        return result

    def get_entity_stats(self, stats_level: 'EntityStatsMixin.StatsLevel' = EntityStatsMixin.StatsLevel.debug) -> Tuple[str, Dict[str, Any]]:
        return type(self).__name__, {
            'instances num': len(self.instances),
        }

    def single_task_registration_or_immediate_processing_single(
            self, *args, **kwargs
    ) -> Tuple[bool, Optional[CoroID], Any]:
        number_of_args: int = number_of_provided_args(args, kwargs)
        if 1 == number_of_args:
            return self._on_get(*args, **kwargs)
        elif 2 == number_of_args:
            return self._on_set(*args, **kwargs)
        else:
            return True, None, RuntimeError(f'Wrong number of parameters: {number_of_args}')

    def full_processing_iteration(self):
        results_bak = self.results
        self.results = type(results_bak)()
        for waiter_coro_id, instance in results_bak.items():
            self.register_response(waiter_coro_id, instance)

        self.make_dead()

    def in_work(self) -> bool:
        return self.thrifty_in_work(bool(self.results))
    
    def _on_start(self, host=None, port=None):
        if State.stopped != self.state:
            return True, None, RuntimeError('Already started or not yet stopped.')
        else:
            ...
        
        return True, None, None


RemoteNodesRequest.default_service_type = RemoteNodes
