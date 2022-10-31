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


__all__ = ['AsyncioLoop', 'AsyncioLoopRequest', 'AsyncioLoopWasNotSet', 'run_in_thread_pool']

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_tools import create_task
from cengal.parallel_execution.coroutines.coro_tools import task_in_thread_pool
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly, CoroPriority
from cengal.parallel_execution.coroutines.coro_standard_services.simple_yield import Yield
from cengal.parallel_execution.asyncio.run_loop import run_forever
from cengal.parallel_execution.asyncio.atasks import create_task_awaitable
from cengal.file_system.file_manager import path_relative_to_current_dir
from cengal.time_management.load_best_timer import perf_counter
from cengal.data_manipulation.serialization import *
from cengal.introspection.inspect import get_exception
from typing import Callable, Tuple, List, Any, Dict, Awaitable
import sys
import os
from asyncio import AbstractEventLoop, get_event_loop, get_running_loop, Task as asyncio_Task


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


class AsyncioLoopWasNotSet(Exception):
    pass


class AsyncioLoopRequest(ServiceRequest):
    def inherit_surrounding_loop(self) -> ServiceRequest:
        return self._save(0)

    def start_internal_loop(self, main_awaitable: Optional[Awaitable] = None, priority: Optional[CoroPriority] = None, interrupt_when_no_requests: Optional[bool] = None) -> ServiceRequest:
        return self._save(1, main_awaitable, priority, interrupt_when_no_requests)

    def ensure_loop(self, main_awaitable: Optional[Awaitable] = None, priority: Optional[CoroPriority] = None, interrupt_when_no_requests: Optional[bool] = None) -> ServiceRequest:
        return self._save(2, main_awaitable, priority, interrupt_when_no_requests)

    def set(self, async_loop) -> ServiceRequest:
        return self._save(3, async_loop)

    def get(self) -> ServiceRequest:
        return self._save(4)

    def wait(self, awaitable: Awaitable) -> ServiceRequest:
        return self._save(5, awaitable)

    def create_task(self, awaitable: Awaitable) -> ServiceRequest:
        return self._save(6, awaitable)

    def _internal_loop_yield(self) -> ServiceRequest:
        return self._save(7)


class AsyncioLoop(Service, EntityStatsMixin):
    def __init__(self, loop: CoroScheduler):
        super(AsyncioLoop, self).__init__(loop)
        self.async_loop: Optional[AbstractEventLoop] = None
        self.internal_async_loop: Optional[AbstractEventLoop] = None
        self._internal_loop_holding_coro: Optional[GreenetCoro] = None
        self.internal_loop_start_waiters: Set[CoroID] = set()
        self.need_to_stop_internal_loop: bool = False
        self.internal_loop_creation_error: Optional[Exception] = None
        self.internal_loop_in_yield: bool = False

        self._request_workers = {
            0: self._on_inherit_surrounding_loop,
            1: self._on_start_internal_loop,
            2: self._on_ensure_loop,
            3: self._on_set,
            4: self._on_get,
            5: self._on_await,
            6: self._on_create_task,
            7: self._on__internal_loop_yield,
        }
        
        self.pending_requests_num: int = 0
        self.results: Dict[CoroID, Tuple[Any, Exception]] = dict()

    def get_entity_stats(self, stats_level: 'EntityStatsMixin.StatsLevel' = EntityStatsMixin.StatsLevel.debug) -> Tuple[str, Dict[str, Any]]:
        return type(self).__name__, {
            'pending requests num': self.pending_requests_num
        }

    def single_task_registration_or_immediate_processing(
            self, request: Optional[AsyncioLoopRequest]=None) -> Tuple[bool, None, None]:
        if request is not None:
            return self.resolve_request(request)
        return True, None, None

    def full_processing_iteration(self):
        if self.internal_loop_in_yield:
            if self.pending_requests_num:
                self.register_response(self._internal_loop_holding_coro, None, None)
                self.internal_loop_in_yield = False

        if self.internal_loop_start_waiters:
            loop_response = None
            exception_response = None
            if self.internal_async_loop is not None:
                loop_response = self.async_loop = self.internal_async_loop
            elif self.internal_loop_creation_error is not None:
                exception_response = self.internal_loop_creation_error
            
            if loop_response or exception_response:
                for coro_id in self.internal_loop_start_waiters:
                    self.register_response(coro_id, loop_response, exception_response)

                self.internal_loop_start_waiters = type(self.internal_loop_start_waiters)()

        for coro_id, response in self.results.items():
            result, exeption = response
            self.register_response(coro_id, result, exeption)
        
        self.pending_requests_num -= len(self.results)
        self.results = type(self.results)()
        
        self.make_dead()
    
    def is_low_latency(self) -> bool:
        return True

    def in_work(self) -> bool:
        result: bool = bool(self.internal_loop_start_waiters) | bool(self.pending_requests_num) | bool(self.results)
        return self.thrifty_in_work(result)
    
    def _on_inherit_surrounding_loop(self) -> Tuple[bool, Optional[AbstractEventLoop], Exception]:
        exception = None
        try:
            self.async_loop = get_running_loop()
        except:
            exception = get_exception()

        return True, self.async_loop, exception
    
    def _on_start_internal_loop(self, main_awaitable: Optional[Awaitable] = None, priority: Optional[CoroPriority] = None, interrupt_when_no_requests: Optional[bool] = None) -> Tuple[bool, Optional[AbstractEventLoop], Exception]:
        if self.internal_async_loop:
            self.async_loop = self.internal_async_loop
            return True, self.async_loop, None
        
        coro_id = self.current_caller_coro_info.coro_id
        self.internal_loop_start_waiters.add(coro_id)
        if self._internal_loop_holding_coro is None:
            self.internal_async_loop = None
            self.internal_loop_creation_error = None
            self._internal_loop_holding_coro = self._loop.put_coro(ExplicitWorker(CoroType.greenlet, _internal_loop_holding_coro), self, main_awaitable, priority, interrupt_when_no_requests)

        return False, None, None
    
    def _on_ensure_loop(self, main_awaitable: Optional[Awaitable] = None, priority: Optional[CoroPriority] = None, interrupt_when_no_requests: Optional[bool] = None) -> Tuple[bool, Optional[AbstractEventLoop], Exception]:
        result_exists, result, exception = self._on_get()
        if result and (exception is None):
            return result_exists, result, exception

        result_exists, result, exception = self._on_inherit_surrounding_loop()
        if result and (exception is None):
            return result_exists, result, exception
        
        return self._on_start_internal_loop(main_awaitable, priority, interrupt_when_no_requests)

    def _on_set(self, async_loop):
        self.async_loop = async_loop
        return True, None, None

    def _on_get(self):
        if self.async_loop is None:
            exception = AsyncioLoopWasNotSet()
        else:
            exception = None
        
        return True, self.async_loop, exception
    
    def register_await_response(self, coro_id: CoroID, response: Any, exception: Optional[Exception]):
        self.results[coro_id] = (response, exception)
        self.make_live()

    def _on_await(self, awaitable: Awaitable):
        if self.async_loop is None:
            return True, None, AsyncioLoopWasNotSet()
        
        coro_id = self.current_caller_coro_info.coro_id
        
        async def awaiting_worker(asyncio_loop_instance: AsyncioLoop, coro_id: CoroID, awaitable: Awaitable):
            exception = None
            result = None
            try:
                result = await awaitable
            except:
                exception = get_exception()
            
            asyncio_loop_instance.register_await_response(coro_id, result, exception)
        
        create_task(self.async_loop, awaiting_worker, self, coro_id, awaitable)
        
        self.pending_requests_num += 1
        self.make_live()
        
        return False, None, None

    def _on_create_task(self, awaitable: Awaitable) -> Tuple[bool, Optional[asyncio_Task], Optional[Exception]]:
        if self.async_loop is None:
            return True, None, AsyncioLoopWasNotSet()

        async def awaiting_wrapper(awaitable: Awaitable):
            return await awaitable

        task: asyncio_Task = create_task(self.async_loop, awaiting_wrapper, awaitable)
        return True, task, None
    
    def _on__internal_loop_yield(self) -> Tuple[bool, None, None]:
        if self.pending_requests_num:
            return True, None, None
        else:
            self.internal_loop_in_yield = True
            return False, None, None
    
    def inline_get(self):
        if self.async_loop is None:
            raise AsyncioLoopWasNotSet
        else:
            return self.async_loop
    
    def inline_set_internal_loop(self, loop, exception: Optional[Exception]):
        self.internal_async_loop = loop
        self.internal_loop_creation_error = exception
        self.make_live()
    
    def is_need_to_yield_internal_loop(self) -> bool:
        return not self.pending_requests_num


def _internal_loop_holding_coro(i: Interface, service: AsyncioLoop, main_awaitable: Optional[Awaitable] = None, priority: Optional[CoroPriority] = None, interrupt_when_no_requests: Optional[bool] = None):
    ly = None
    if priority is not None:
        ly = gly(priority)

    async def main_wrapper(service: AsyncioLoop, main_awaitable: Optional[Awaitable] = None, priority: Optional[CoroPriority] = None, interrupt_when_no_requests: Optional[bool] = None):
        loop: AbstractEventLoop = get_event_loop()
        service.inline_set_internal_loop(loop, None)
        if interrupt_when_no_requests is None:
            interrupt_when_no_requests = main_awaitable is None
        
        def on_loop_simple_yield():
            if interrupt_when_no_requests and service.is_need_to_yield_internal_loop():
                i(AsyncioLoop, AsyncioLoopRequest()._internal_loop_yield())
            else:
                i(Yield)
            
            if not service.need_to_stop_internal_loop:
                loop.call_soon(on_loop_simple_yield)
        
        def on_loop_loop_yield():
            if interrupt_when_no_requests and service.is_need_to_yield_internal_loop():
                i(AsyncioLoop, AsyncioLoopRequest()._internal_loop_yield())
            else:
                ly()
            
            if not service.need_to_stop_internal_loop:
                loop.call_soon(on_loop_loop_yield)
        
        if ly is None:
            loop.call_soon(on_loop_simple_yield)
        else:
            loop.call_soon(on_loop_loop_yield)

        if main_awaitable is not None:
            create_task_awaitable(main_awaitable)
    
    exception = None
    try:
        run_forever(main_wrapper(service, main_awaitable, priority, interrupt_when_no_requests))
    except:
        exception = get_exception()
    finally:
        service.inline_set_internal_loop(None, exception)


def run_in_thread_pool_fast(interface: Interface, function: Callable, *args, **kwargs) -> Any:
    async def task_wrapper(loop, *args, **kwargs):
        return await task_in_thread_pool(loop, function, *args, **kwargs)

    return interface(AsyncioLoop, AsyncioLoopRequest().wait(task_wrapper(
        interface._loop.get_service_instance(AsyncioLoop).inline_get(), 
        *args, **kwargs)))


def run_in_thread_pool(function: Callable, *args, **kwargs) -> Any:
    return run_in_thread_pool_fast(current_interface(), function, *args, **kwargs)
