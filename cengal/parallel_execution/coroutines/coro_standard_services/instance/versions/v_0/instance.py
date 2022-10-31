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


__all__ = ['Instance', 'InstanceRequest', 'view_log', 'clear_log', 'log_fast', 'log', 'put_log_fast', 'plog_fast', 'put_log', 'plog', 'alog_fast', 'alog', 'aput_log_fast', 'aplog_fast', 'aput_log', 'aplog']

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
from cengal.parallel_execution.asyncio.efficient_streams import StreamManagerIOCoreMemoryManagement, TcpStreamManager, UdpStreamManager
from cengal.code_flow_control.smart_values import ValueExistence
from cengal.io.named_connections.named_connections_manager import NamedConnectionsManager
from cengal.code_flow_control.args_manager import number_of_provided_args
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


class InstanceRequest(ServiceRequest):
    def set(self, key: Union[Type, Hashable], instance: Any) -> ServiceRequest:
        return self._save(0, key, instance)
    def get(self, key: Union[Type, Hashable]) -> ServiceRequest:
        return self._save(1, key)
    def wait(self, key: Union[Type, Hashable]) -> ServiceRequest:
        return self._save(2, key)


class Instance(DualImmediateProcessingServiceMixin, Service, EntityStatsMixin):
    def __init__(self, loop: CoroScheduler):
        super(Instance, self).__init__(loop)
        self.instances: Dict = dict()
        self._default_init()
        self.waiters_per_key: Dict[Hashable, Set[CoroID]] = dict()
        self.results: Dict[CoroID, Hashable] = dict()
        self._request_workers = {
            0: self._on_set,
            1: self._on_get,
            2: self._on_wait,
        }

    def get_entity_stats(self, stats_level: 'EntityStatsMixin.StatsLevel' = EntityStatsMixin.StatsLevel.debug) -> Tuple[str, Dict[str, Any]]:
        return type(self).__name__, {
            'instances num': len(self.instances),
        }
    
    def _default_init(self):
        data_full_size = ValueExistence(True, 0)
        other_data_full_size = ValueExistence(True, 0)
        in_data_full_size = ValueExistence(True, 0)
        out_data_full_size = ValueExistence(True, 0)
        tcp_stream_manager: TcpStreamManager = TcpStreamManager()
        tcp_stream_manager.io_memory_management.global__data_full_size = data_full_size
        tcp_stream_manager.io_memory_management.global_other__data_full_size = other_data_full_size
        tcp_stream_manager.io_memory_management.global_in__data_full_size = in_data_full_size
        tcp_stream_manager.io_memory_management.global_out__data_full_size = out_data_full_size
        udp_stream_manager: UdpStreamManager = UdpStreamManager()
        udp_stream_manager.io_memory_management.global__data_full_size = data_full_size
        udp_stream_manager.io_memory_management.global_other__data_full_size = other_data_full_size
        udp_stream_manager.io_memory_management.global_in__data_full_size = in_data_full_size
        udp_stream_manager.io_memory_management.global_out__data_full_size = out_data_full_size
        named_connections_manager: NamedConnectionsManager = NamedConnectionsManager(data_full_size)
        self.instances.update({
            'data_full_size': ValueExistence(True, 0),
            'other_data_full_size': ValueExistence(True, 0),
            'in_data_full_size': ValueExistence(True, 0),
            'out_data_full_size': ValueExistence(True, 0),
            TcpStreamManager: tcp_stream_manager,
            UdpStreamManager: udp_stream_manager,
            NamedConnectionsManager: named_connections_manager,
        })

    def single_task_registration_or_immediate_processing_single(
            self, *args, **kwargs
    ) -> Tuple[bool, Union[Type, Hashable], Optional[BaseException]]:
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
    
    def _on_set(self, key: Union[Type, Hashable], instance: Any):
        self.instances[key] = instance
        if key in self.waiters_per_key:
            self.make_live()
            waiters = self.waiters_per_key[key]
            del self.waiters_per_key[key]
            for waiter_coro_id in waiters:
                self.results[waiter_coro_id] = instance
        
        return True, None, None
    
    def _on_get(self, key: Union[Type, Hashable]):
        instance = None
        exception = None
        try:
            instance = self.instances[key]
        except:
            exception = get_exception()
        
        return True, instance, exception
    
    def _on_wait(self, key: Union[Type, Hashable]):
        instance = None
        exception = None
        need_to_wait: bool = False
        try:
            instance = self.instances[key]
        except KeyError:
            need_to_wait = True
        except:
            exception = get_exception()
        
        if need_to_wait:
            current_coro_id = self.current_caller_coro_info.coro_id
            if key not in self.waiters_per_key:
                self.waiters_per_key = set()
            
            self.waiters_per_key[key].add(current_coro_id)
            return False, None, None
        else:
            return True, instance, exception
    
    def inline_set(self, key: Union[Type, Hashable], instance: Any):
        self.instances[key] = instance
    
    def inline_get(self, key: Union[Type, Hashable]) -> Any:
        return self.instances[key]
