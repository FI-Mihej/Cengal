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


class LocalRequestClassInfo(LocalClassInfo):
    def __init__(self, local_id: Hashable, request: Request) -> None:
        super().__init__(local_id, type(request))
        self._properties: Dict[str, Hashable] = {property_name: index for index, property_name in enumerate(entity_properties(request))}  # key: property name; value: property id
        self._properties_tuple: Tuple[Tuple[str, Hashable]] = tuple(self._properties.items())
    
    def __call__(self) -> Type:
        return {
            CommandDataFieldsDeclareServiceRequestClass.local_id.value: self._local_id,
            CommandDataFieldsDeclareServiceRequestClass.class_name.value: self._class_name,
            CommandDataFieldsDeclareServiceRequestClass.module_importable_str.value: self._module_importable_str,
            CommandDataFieldsDeclareServiceRequestClass.properties_tuple.value: self._properties_tuple,
        }
    
    @property
    def properties(self):
        return self._properties
    
    @property
    def properties_tuple(self):
        return self._properties_tuple
    
    def request_to_data(self, request: Request) -> Dict:
        return {
            CommandDataFieldsServiceRequestWithRequestClass.request_class_id.value: self._local_id,
            CommandDataFieldsServiceRequestWithRequestClass.properties_tuple.value: tuple(((property_id, getattr(request, property_name)) for property_name, property_id in self._properties_tuple)),
        }


class RemoteRequestClassInfo(RemoteClassInfo):
    def __init__(self, local_id: Hashable, class_name: str, module_importable_str: str, properties_tuple: Tuple[Tuple[str, Hashable]]) -> None:
        super().__init__(local_id, class_name, module_importable_str)
        self._properties_tuple: Tuple[Tuple[str, Hashable]] = properties_tuple
        self._properties: Dict[Hashable, str] = {index: property_name for property_name, index in properties_tuple}  # key: property id; value: property name
    
    @classmethod
    def from_data(cls, data: Dict[Hashable, Any]) -> 'RemoteRequestClassInfo':
        local_id: Hashable = data[CommandDataFieldsDeclareServiceRequestClass.local_id.value]
        class_name: str = data[CommandDataFieldsDeclareServiceRequestClass.class_name.value]
        module_importable_str: str = data[CommandDataFieldsDeclareServiceRequestClass.module_importable_str.value]
        properties_tuple: Tuple[Tuple[str, Hashable]] = data[CommandDataFieldsDeclareServiceRequestClass.properties_tuple.value]
        return cls(local_id, class_name, module_importable_str, properties_tuple)
    
    def __call__(self, data: Dict) -> Request:
        request: Request = self.class_type()
        properties_tuple: Tuple[Tuple[Hashable, Any]] = data[CommandDataFieldsDeclareServiceRequestClass.properties_tuple.value]
        for index, value in properties_tuple:
            name: str = self._properties[index]
            setattr(request, name, value)
        
        return request
