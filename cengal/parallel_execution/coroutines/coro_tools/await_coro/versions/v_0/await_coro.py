#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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

__all__ = ['await_coro_fast', 'await_coro', 'await_coro_prim', 'asyncio_coro', 'await_task_fast', 'await_task', 'await_task_prim', 'RunSchedulerInAsyncioLoop',
           'coro_interfaces_arg_manager', 'create_task', 'create_task_in_thread_pool', 'task_in_thread_pool']

import sys
import asyncio
from inspect import signature, Signature, Parameter
from cengal.parallel_execution.coroutines.coro_scheduler import *
# from cengal.parallel_execution.coroutines.coro_standard_services import *
from cengal.time_management.load_best_timer import perf_counter
from cengal.time_management.timer import Timer
from cengal.code_flow_control.args_manager import ArgsManager, EArgs
from enum import Enum
from functools import partial
from typing import Union, Optional, Callable, Awaitable, Any, Coroutine
from cengal.time_management.sleep_tools import get_min_sleep_interval, try_sleep, get_usable_min_sleep_interval, get_countable_delta_time
from cengal.introspection.inspect import get_exception, get_exception_tripple
from cengal.parallel_execution.coroutines.coro_standard_services_internal_lib.service_with_a_direct_request import *
from cengal.code_flow_control.smart_values import ValueExistence
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.2.2"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


def _async_coro_wrapper(interface: Interface, future: asyncio.Future, coro_worker: Worker, *args, **kwargs):
    coro_worker_result = None
    try:
        if __debug__: dlog(f'λ wrapper => {func_info(coro_worker)}')
        coro_worker_result = coro_worker(interface, *args, **kwargs)
    except:
        if __debug__: dlog(f'λ wrapper (Exception) <= {repr(coro_worker)}')
        if not future.cancelled():
            ex_type, ex_value, ex_traceback = get_exception_tripple()
            if __debug__: dlog(ex_type, ex_value, ex_traceback)
            ex_value = ex_value.with_traceback(ex_traceback)
            future.set_exception(ex_value)
    else:
        if __debug__: dlog(f'λ wrapper <= {repr(coro_worker)}')
        if not future.cancelled():
            future.set_result(coro_worker_result)


async def _awaitable_async_coro_wrapper(interface: Interface, future: asyncio.Future, coro_worker: Worker, *args, **kwargs):
    coro_worker_result = None
    try:
        if __debug__: dlog(f'aλ wrapper => {func_info(coro_worker)}')
        
        # # TODO: fix required!
        # coro_worker_result = await interface(RunCoro, CoroType.awaitable, coro_worker, *args, **kwargs)
        # TODO: possible fix:
        coro_worker_result = await coro_worker(interface, *args, **kwargs)
    except:
        if __debug__: dlog(f'aλ wrapper (Exception) <= {repr(coro_worker)}')
        if not future.cancelled():
            ex_type, ex_value, ex_traceback = get_exception_tripple()
            if __debug__: dlog(ex_type, ex_value, ex_traceback)
            ex_value = ex_value.with_traceback(ex_traceback)
            future.set_exception(ex_value)
    else:
        if __debug__: dlog(f'aλ wrapper <= {repr(coro_worker)}')
        if not future.cancelled():
            future.set_result(coro_worker_result)


def await_coro_fast(loop: asyncio.AbstractEventLoop,
                    scheduler: CoroScheduler, coro_type: Optional[CoroType], coro_worker: Worker, *args, **kwargs
                    ) -> asyncio.Future:
    coro_type = coro_type or CoroType.auto
    if CoroType.auto == coro_type:
        coro_type = find_coro_type(coro_worker)
    
    future = loop.create_future()
    if CoroType.awaitable == coro_type:
        make_request_to_service_with_context(get_interface_and_loop_with_explicit_loop(scheduler), PutCoro, ExplicitWorker(coro_type, _awaitable_async_coro_wrapper), future, coro_worker, *args, **kwargs)
    elif CoroType.greenlet == coro_type:
        make_request_to_service_with_context(get_interface_and_loop_with_explicit_loop(scheduler), PutCoro, ExplicitWorker(coro_type, _async_coro_wrapper), future, coro_worker, *args, **kwargs)
    else:
        raise NotImplementedError
    
    return future


def await_coro(scheduler: CoroScheduler, coro_worker: Worker, *args, **kwargs) -> asyncio.Future:
    return await_coro_fast(asyncio.get_event_loop(), scheduler, None, coro_worker, *args, **kwargs)


def await_coro_prim(coro_worker: Worker, *args, **kwargs) -> asyncio.Future:
    """Tries to use primary coro scheduler (must be set before usage)

    Args:
        coro_worker (Worker): _description_

    Returns:
        asyncio.Future: _description_
    """
    return await_coro_fast(asyncio.get_event_loop(), available_coro_scheduler(), CoroType.auto, coro_worker, *args, **kwargs)


def asyncio_coro(coro_worker: Worker) -> Coroutine:
    """Decorator. Without arguments. Gives an ability to await any decorated Cengal coroutine from the async code

    Args:
        coro_worker (Worker): _description_

    Returns:
        Coroutine: _description_
    """    
    async def wrapper(*args, **kwargs):
        return await await_coro_prim(coro_worker, *args, **kwargs)
    
    coro_worker_sign: Signature = signature(coro_worker)
    wrapper.__signature__ = coro_worker_sign.replace(parameters=tuple(coro_worker_sign.parameters.values())[1:], return_annotation=coro_worker_sign.return_annotation)
    return wrapper


def _async_task_runner_coro_worker(interface: Interface, service_type: ServiceType, *args, **kwargs):
    if __debug__: dlog(f'λ wrapper <_async_task_runner_coro_worker> => interface({service_type}, {args}, {kwargs})')
    result = interface(service_type, *args, **kwargs)
    if __debug__: dlog(f'λ wrapper <_async_task_runner_coro_worker> <= interface({service_type}, {args}, {kwargs}): {result}')
    return result


def await_task_fast(loop: asyncio.AbstractEventLoop,
                    scheduler: CoroScheduler, service_type: ServiceType, *args, **kwargs
                    ) -> asyncio.Future:
    future = loop.create_future()
    make_request_to_service_with_context(get_interface_and_loop_with_explicit_loop(scheduler), PutCoro, ExplicitWorker(CoroType.greenlet, _async_coro_wrapper), future, _async_task_runner_coro_worker, service_type, *args, **kwargs)
    return future


def await_task(scheduler: CoroScheduler, service_type: ServiceType, *args, **kwargs) -> asyncio.Future:
    return await_task_fast(asyncio.get_event_loop(), scheduler, service_type, *args, **kwargs)


def await_task_prim(service_type: ServiceType, *args, **kwargs) -> asyncio.Future:
    """Tries to use primary coro scheduler (must be set before usage)

    Args:
        service_type (ServiceType): _description_

    Returns:
        asyncio.Future: _description_
    """
    return await_task_fast(asyncio.get_event_loop(), available_coro_scheduler(), service_type, *args, **kwargs)


def coro_interfaces_arg_manager(event_loop, coro_scheduler: CoroScheduler):
    acf = ArgsManager(
        EArgs(event_loop, coro_scheduler, CoroType.auto),
    ).callable(await_coro_fast)
    atf = ArgsManager(
        EArgs(event_loop, coro_scheduler),
    ).callable(await_task_fast)
    
    return EArgs(await_coro_fast=acf, await_task_fast=atf)


class RunSchedulerInAsyncioLoop:
    def __init__(self, scheduler: CoroScheduler, idle_time: Optional[Union[int, float]]=None, loop: Optional[asyncio.AbstractEventLoop]=None, execute_every_X_iterations: int = 1):
        self.scheduler = scheduler
        self.scheduler.on_woke_up_callback = self.on_woke_up_callback
        if idle_time is None:
            idle_time = get_usable_min_sleep_interval()
        
        self.idle_time = get_min_sleep_interval() * (idle_time // get_min_sleep_interval())
        self.min_sleep_interval = max(get_min_sleep_interval(), self.idle_time or 0)
        self.usable_idle_time = (get_min_sleep_interval() * (idle_time // get_min_sleep_interval())) + get_countable_delta_time()
        self.loop = loop or asyncio.get_event_loop()
        self.handle = None  # type: Optional[asyncio.Handle]
        self.make_idle_when_possible = False
        self.need_to_stop_when_possible = False
        self.need_to_stop_now = False
        self.in_idle_state = False
        if execute_every_X_iterations < 1:
            execute_every_X_iterations = 1
        
        self.execute_every_X_iterations = execute_every_X_iterations
        self.current_iteration = execute_every_X_iterations
    
    def on_woke_up_callback(self):
        if self.in_idle_state:
            self.cancel_handle()
            self.in_idle_state = False
            self.register()

    def __call__(self, *args, **kwargs):
        self.current_iteration -= 1
        if self.current_iteration:
            self.register()
            return
        else:
            self.current_iteration = self.execute_every_X_iterations
        
        self.handle = None
        self.in_idle_state = False
        if self.need_to_stop_now:
            self.need_to_stop_now = False
            self.need_to_stop_when_possible = False
            return

        in_work = self.scheduler.iteration()
        
        if (not in_work) and self.need_to_stop_when_possible:
            self.need_to_stop_now = False
            self.need_to_stop_when_possible = False
            return

        idle_time = self.scheduler.next_event_after()
        # is_awake = self.scheduler.is_awake()
        is_idle = self.scheduler.is_idle()
        need_to_register = False
        if self.make_idle_when_possible:
            if not is_idle:
                need_to_register = True
        else:
            need_to_register = True

        if need_to_register:
            self.register()
        else:
            self.register_idle(idle_time)

    def ready_to_stop(self) -> bool:
        return not self.scheduler.in_work()

    def register(self):
        # self.register_idle()
        self.handle = self.loop.call_soon(self)

    def register_idle(self, idle_time: Optional[float] = None):
        if idle_time is None:
            idle_time = self.usable_idle_time
        
        # self.handle = self.loop.call_later(self.idle_time, self)
        if idle_time < self.min_sleep_interval:
            self.register()
        else:
            # self.handle = try_sleep(self.idle_time * (idle_time // self.idle_time), self.loop.call_later, self)
            # # self.handle = try_sleep(0.001, self.loop.call_later, self)
            self.in_idle_state = True
            idle_time = (self.idle_time * (idle_time // self.idle_time)) + get_countable_delta_time()
            self.handle = self.loop.call_later(idle_time, self)

    def cancel_handle(self):
        if self.handle and (not self.handle.cancelled()):
            self.handle.cancel()
            self.handle = None

    def stop(self):
        if self.handle and (not self.handle.cancelled()):
            self.need_to_stop_now = True
            self.handle.cancel()
            self.handle = None

    def stop_when_possible(self):
        self.need_to_stop_when_possible = True


# def call_soon_future(loop: Optional[asyncio.AbstractEventLoop], awaitable_coro_obj: Awaitable):
#     if __debug__: dlog('call_soon_future - start')
#     loop = loop or asyncio.get_event_loop()
#
#     def handler():
#         if __debug__: dlog('call_soon_future.handler - start')
#         loop.create_task(awaitable_coro_obj)
#         if __debug__: dlog('call_soon_future.handler - end')
#
#     loop.get_event_loop().call_soon(handler)
#     if __debug__: dlog('call_soon_future - end')


def call_soon_future(loop: Optional[asyncio.AbstractEventLoop], awaitable_coro_obj: Awaitable):
    if __debug__: dlog('call_soon_future - start')
    loop = loop or asyncio.get_event_loop()

    def handler():
        if __debug__: dlog('call_soon_future.handler - start')
        loop.create_task(awaitable_coro_obj)
        if __debug__: dlog('call_soon_future.handler - end')

    loop.get_event_loop().call_soon(handler)
    if __debug__: dlog('call_soon_future - end')


def create_task(loop: Optional[asyncio.AbstractEventLoop], acoro: Callable, *args, **kwargs) -> asyncio.Task:
    if __debug__: dlog('call_soon_future - start')
    loop = loop or asyncio.get_event_loop()
    awaitable_coro_obj = acoro(*args, **kwargs)
    return loop.create_task(awaitable_coro_obj)


def create_task_in_thread_pool(loop: Optional[asyncio.AbstractEventLoop], joiner: Optional[Awaitable[Any]], worker: Callable, *args, **kwargs):
    async def sync_handler(loop, joiner, worker, args, kwargs):
        worker_with_args = partial(worker, *args, **kwargs)
        result = await loop.run_in_executor(None, worker_with_args)
        if joiner is not None:
            await joiner(result)
                        
    create_task(loop, sync_handler, loop, joiner, worker, args, kwargs)


async def task_in_thread_pool(loop: Optional[asyncio.AbstractEventLoop], worker: Callable, *args, **kwargs):
    worker_with_args = partial(worker, *args, **kwargs)
    return await loop.run_in_executor(None, worker_with_args)
