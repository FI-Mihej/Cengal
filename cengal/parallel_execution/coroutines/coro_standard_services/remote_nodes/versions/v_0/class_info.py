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


class LocalClassInfo:
    def __init__(self, local_id: Hashable, class_type: Type) -> None:
        self.class_type: Type = class_type
        self._class_name: str = self.class_type.__name__
        self._module_importable_str: str = entity_owning_module_importable_str(self.class_type)
        self._local_id: Hashable = local_id
    
    def __call__(self) -> Type:
        return {
            CommandDataFieldsDeclareServiceClass.local_id.value: self._local_id,
            CommandDataFieldsDeclareServiceClass.class_name.value: self._class_name,
            CommandDataFieldsDeclareServiceClass.module_importable_str.value: self._module_importable_str,
        }
    
    @property
    def class_name(self):
        return self._class_name
    
    @property
    def module_importable_str(self):
        return self._module_importable_str
    
    @property
    def local_id(self):
        return self._local_id


class RemoteClassInfo:
    def __init__(self, local_id: Hashable, class_name: str, module_importable_str: str) -> None:
        self.local_id: Hashable = local_id
        self.class_name: str = class_name
        self.module_importable_str: str = module_importable_str
        self.module = import_module(self.module_importable_str)
        self._class_type: Type = getattr(self.module, self.class_name)
    
    @classmethod
    def from_data(cls, data: Dict[Hashable, Any]) -> 'RemoteClassInfo':
        local_id: Hashable = data[CommandDataFieldsDeclareServiceClass.local_id.value]
        class_name: str = data[CommandDataFieldsDeclareServiceClass.class_name.value]
        module_importable_str: str = data[CommandDataFieldsDeclareServiceClass.module_importable_str.value]
        return cls(local_id, class_name, module_importable_str)
    
    def __call__(self) -> Type:
        return self._class_type
    
    @property
    def class_type(self):
        return self()
