#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2022 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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


__all__ = ['RemoteNodes', 'RemoteNodesRequest', 'view_log', 'clear_log', 'log_fast', 'log', 'put_log_fast', 'plog_fast', 'put_log', 'plog', 'alog_fast', 'alog', 'aput_log_fast', 'aplog_fast', 'aput_log', 'aplog']

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
from cengal.introspection.inspect import get_exception
from cengal.io.core.memory_management import IOCoreMemoryManagement
from cengal.parallel_execution.asyncio.efficient_streams import StreamManagerIOCoreMemoryManagement, TcpStreamManager, UdpStreamManager, StreamManagerAbstract
from cengal.code_flow_control.smart_values import ValueExistence
from cengal.io.named_connections.named_connections_manager import NamedConnectionsManager
from cengal.code_flow_control.args_manager import number_of_provided_args
from cengal.data_manipulation.serialization import Serializer, Serializers, best_serializer
from cengal.system import PLATFORM_NAME
import sys
import os
import asyncio
import lmdb


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2022 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "0.0.8"
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


class Commands(Enum):
    suggest_best_serializers_list = 0  # client suggests list of it's best serializers (first is fastest)
    declare_best_serializers_list = 1  # server respondes with a sublist of apropriate sugested serializers (first is fastest)
    declare_service_class = 2  # client sends service class name, it's unique ID (int starting from 0, generated on the client side), it's module importable str (path) and it's module full file path
    declare_service_request_class = 3  # client sends service ID, service request class name and it's unique ID (int starting from 0, generated on the client side)
    send_request = 4
    send_service_request = 5
    send_service_request_with_request_class = 6
    send_response = 6


class Fields(Enum):
    command_name = 0  # See Commands class. Optional: if ommited then: 1) if `in_response_to` present then default is `send_response`; 2) if `in_response_to` is not present then default is `send_request`
    request_id = 1  # id of either request or response (requests and responses must have an independent counters)
    in_response_to = 2  # current response is a response to request with this ID. Optional: can be present only in `send_response`
    is_response_required = 3  # int. 1 = required; 0 = not required. Optional: if ommited then default is 0 (not required). This gives us ability to send smallest response-less request as possible. Even is not required, response still can be send. If required - response must be send.
    data = 4  # Data. Format depends on request type (command type). Optional: if ommited then default is None.
    data_serializer_id = 5  # If data was serialized explicitly with some serializer (Pickle for example). Optional.


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
        self.platform_name: str = PLATFORM_NAME
        self.state: State = State.stopped

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
    
    def serialize(self, foreign_platform_name, data) -> Tuple[Serializer, bytes]:
        current_platform = is_current_platform(self.platform_name, foreign_platform_name)
        if current_platform:
            serializer: Serializer = self.serializer__current_platform
        else:
            serializer = self.serializer__multi_platform
        
        try_with_custom_types = False
        try:
            return serializer, serializer.dumps(data)
        except:
            if not current_platform:
                raise
            else:
                try_with_custom_types = True
        
        if try_with_custom_types:
            serializer = self.serializer__current_platform__custom_types
            return serializer, serializer.dumps(data)
    
    def deserialize(self, serializer: Serializer, data: bytes) -> Any:
        return serializer.loads(data)
    
    def serialize_request(self, args, kwargs) -> bytes:
        ...

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
