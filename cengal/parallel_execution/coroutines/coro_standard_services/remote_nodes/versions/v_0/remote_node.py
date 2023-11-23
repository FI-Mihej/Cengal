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

from .exceptions import *
from .commands import *
from .class_info import *
from .request_class_info import *
from .serializers import *


class RemoteNode:
    def __init__(self) -> None:
        self.foreign_platform_name: str = None
        self.serializers: Dict[SerializerID, Serializer] = dict()
        self.request_id_gen: IDGenerator = IDGenerator(GeneratorType.integer)
    
    def register_node(self, data: Dict):
        raise NotImplementedError
    
    def gen_request_id(self) -> int:
        return self.request_id_gen()

    def register_service_class(self, *args, **kwargs):
        raise NotImplementedError

    def register_request_class(self, *args, **kwargs):
        raise NotImplementedError


class RemoteServer(RemoteNode):
    def __init__(self) -> None:
        super().__init__()
        self.service_class_id_gen: IDGenerator = IDGenerator(GeneratorType.integer)
        self.remotely_registered_service_classes: Dict[Type, LocalClassInfo] = dict()
        
        self.request_class_id_gen: IDGenerator = IDGenerator(GeneratorType.integer)
        self.remotely_registered_request_classes: Dict[Type, LocalRequestClassInfo] = dict()
    
    def register_service_class(self, class_type: Type[Service]):
        self.remotely_registered_service_classes[class_type] = LocalClassInfo(self.service_class_id_gen(), class_type)
    
    def register_request_class(self, request: Request):
        self.remotely_registered_request_classes[type(request)] = LocalRequestClassInfo(self.request_class_id_gen(), request)


class RemoteClient(RemoteNode):
    def __init__(self) -> None:
        super().__init__()
        self.locally_registered_service_classes: Dict[Hashable, RemoteClassInfo] = dict()
        self.locally_registered_request_classes: Dict[Hashable, RemoteClassInfo] = dict()
    
    def register_service_class(self, data: Dict):
        remote_class_info: RemoteClassInfo = RemoteClassInfo.from_data(data)
        self.locally_registered_service_classes[remote_class_info.local_id] = remote_class_info
    
    def register_request_class(self, data: Dict):
        remote_request_class_info: RemoteRequestClassInfo = RemoteRequestClassInfo.from_data(data)
        self.locally_registered_request_classes[remote_request_class_info.local_id] = remote_request_class_info
