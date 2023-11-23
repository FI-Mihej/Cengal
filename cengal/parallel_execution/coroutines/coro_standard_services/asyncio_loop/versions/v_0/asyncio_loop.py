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


__all__ = ['AsyncioLoop', 'AsyncioLoopRequest', 'AsyncioLoopWasNotSetError', 'run_in_thread_pool', 'run_in_thread_pool_fast']

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_tools.await_coro import create_task
from cengal.parallel_execution.coroutines.coro_tools.await_coro import task_in_thread_pool
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly, agly, CoroPriority, LoopYieldPriorityScheduler
from cengal.parallel_execution.coroutines.coro_standard_services.simple_yield import Yield
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro
from cengal.parallel_execution.coroutines.coro_standard_services.throw_coro import ThrowCoro
from cengal.parallel_execution.coroutines.coro_standard_services.kill_coro import KillCoro
from cengal.parallel_execution.coroutines.coro_standard_services.wait_coro import WaitCoro, WaitCoroRequest, CoroutineNotFoundError
from cengal.parallel_execution.asyncio.run_loop import run_forever, cancel_all_tasks
from cengal.parallel_execution.asyncio.atasks import create_task_awaitable
from cengal.file_system.file_manager import path_relative_to_current_dir
from cengal.time_management.load_best_timer import perf_counter
from cengal.time_management.sleep_tools import get_usable_min_sleep_interval, get_min_sleep_interval
from cengal.data_manipulation.serialization import *
from cengal.introspection.inspect import get_exception
from cengal.math.numbers import RationalNumber
from typing import Callable, Tuple, List, Any, Dict, Awaitable, Type
import sys
import os
from asyncio import AbstractEventLoop, get_event_loop, get_running_loop, Task as asyncio_Task, sleep as asyncio_sleep
from asyncio.coroutines import _is_coroutine
from cengal.code_flow_control.args_manager import args_kwargs
from types import coroutine as types_coroutine
from asyncio import coroutines
from asyncio import events
from asyncio import tasks
import threading


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


class AsyncioLoopWasNotSetError(Exception):
    pass


class ExternalAsyncioLoopAlreadyExistsError(Exception):
    pass


class WaitingCancelled(Exception):
    pass


WAITING_FOR_NEW_REQUESTS_EVENT = 'AsyncioLoopRequest - WaitingForNewRequestsEvent'


class AsyncioLoopRequest(ServiceRequest):
    def inherit_surrounding_loop(self) -> AbstractEventLoop:
        return self._save(0)

    def start_internal_loop(self, main_awaitable: Optional[Awaitable] = None, priority: Optional[CoroPriority] = None, interrupt_when_no_requests: Optional[bool] = None, debug: bool = False) -> AbstractEventLoop:
        return self._save(1, main_awaitable, priority, interrupt_when_no_requests, debug)

    def ensure_loop(self, main_awaitable: Optional[Awaitable] = None, priority: Optional[CoroPriority] = None, interrupt_when_no_requests: Optional[bool] = None) -> AbstractEventLoop:
        return self._save(2, main_awaitable, priority, interrupt_when_no_requests)

    def set(self, async_loop) -> None:
        return self._save(3, async_loop)

    def get(self) -> AbstractEventLoop:
        return self._save(4)

    def wait(self, awaitable: Awaitable) -> Any:
        return self._save(5, awaitable, False, True)

    def create_task(self, awaitable: Awaitable) -> asyncio_Task:
        return self._save(6, awaitable)

    def _internal_loop_yield(self) -> None:
        return self._save(7)

    def turn_on_loops_intercommunication(self, turn_on: bool = True) -> Optional[Callable]:
        return self._save(8, turn_on)

    def _wait_intercommunication(self, awaitable: Awaitable) -> Any:
        return self._save(9, awaitable, True, True)

    def wait_idle(self, awaitable: Awaitable) -> Any:
        return self._save(10, awaitable, False, False)

    def use_higher_level_sleep_manager(self, use_higher_level_sleep_manager: bool = True) -> Any:
        return self._save(12, use_higher_level_sleep_manager)

    def turn_on_low_latency_io_mode(self, low_latency_io_mode: bool = True) -> Any:
        return self._save(13, low_latency_io_mode)


async def asyncio_coro_sleep_0():
    return await asyncio_sleep(0)


def request_giver(request):
    yield request

@types_coroutine
def asyncio_coro_request(request):
    return (yield from request_giver(request))

asyncio_coro_request._is_coroutine = _is_coroutine


class AsyncioLoop(Service, EntityStatsMixin):
    def __init__(self, loop: CoroScheduler):
        super(AsyncioLoop, self).__init__(loop)
        self.async_loop: Optional[AbstractEventLoop] = None
        self.internal_async_loop: Optional[AbstractEventLoop] = None
        self._internal_loop_holding_coro: Optional[CoroWrapperBase] = None
        self.internal_loop_start_waiters: Set[CoroID] = set()
        self.need_to_stop_internal_loop: bool = False
        self.internal_loop_creation_error: Optional[Exception] = None
        self.internal_loop_in_yield: bool = False
        self.waiting_for_new_requests: bool = False
        self.loops_intercommunication: bool = False
        self._previous_on_wrong_request = None
        self.intercommunication_requests_coro_ids: Set[CoroID] = set()

        self._request_workers = {
            0: self._on_inherit_surrounding_loop,
            1: self._on_start_internal_loop,
            2: self._on_ensure_loop,
            3: self._on_set,
            4: self._on_get,
            5: self._on_await,
            6: self._on_create_task,
            7: self._on__internal_loop_yield,
            8: self._on_turn_on_loops_intercommunication,
            9: self._on_await,
            10: self._on_await,
            11: self._on__internal_wait_for_new_requests, 
            12: self._on__use_higher_level_sleep_manager, 
            13: self._on__low_latency_io_mode, 
        }
        
        self.pending_requests_num: int = 0
        self.new_requests_num: int = 0
        self.no_idle_calls: Set[CoroID] = set()
        self.results: Dict[CoroID, Tuple[Any, Exception]] = dict()
        self._waiting_coro_id: Optional[CoroID] = None
        self._original_loop_class: Type = None
        self._idle_for: Optional[RationalNumber] = None  # in seconds
        self.use_higher_level_sleep_manager: bool = False
        self.current_on_idle_handler: Optional[Callable] = None
        self.low_latency_io_mode: int = 0
    
    def destroy(self):
        if self.internal_async_loop is not None:
            events._set_running_loop(None)

    def _on_system_loop_idle(self, next_event_after: Optional[RationalNumber]):
        if next_event_after is None:
            self._idle_for = max(0.001, get_usable_min_sleep_interval())
        else:
            self._idle_for = max(0.001, next_event_after)

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
        from cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus import AsyncEventBusRequest, try_send_async_event
        if (self._waiting_coro_id is not None) and self.new_requests_num:
            # throw_coro_service: ThrowCoro = self._loop.get_service_instance(ThrowCoro)
            # throw_coro_service._add_direct_request(self._waiting_coro_id, WaitingCancelled)
            kill_coro_service: KillCoro = self._loop.get_service_instance(KillCoro)
            kill_coro_service._add_direct_request(self._waiting_coro_id)
            self._waiting_coro_id = None
            try_send_async_event(self._loop, WAITING_FOR_NEW_REQUESTS_EVENT, None)

        if self.internal_loop_in_yield:
            if self.pending_requests_num:
                self.register_response(self._internal_loop_holding_coro.coro_id, None, None)
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
            result, exception = response
            if coro_id in self.intercommunication_requests_coro_ids:
                self.intercommunication_requests_coro_ids.remove(coro_id)
                self._responses.append(DirectResponse(coro_id, type(self), result, exception))
            else:
                self.register_response(coro_id, result, exception)
        
        self.pending_requests_num -= len(self.results)
        self.results = type(self.results)()
        
        if not self.no_idle_calls:
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
    
    def _on_start_internal_loop(self, main_awaitable: Optional[Awaitable] = None, priority: Optional[CoroPriority] = None, interrupt_when_no_requests: Optional[bool] = None, debug: bool = False) -> Tuple[bool, Optional[AbstractEventLoop], Exception]:
        if self.internal_async_loop:
            self.async_loop = self.internal_async_loop
            return True, self.async_loop, None
        
        coro_id = self.current_caller_coro_info.coro_id
        self.internal_loop_start_waiters.add(coro_id)
        if self._internal_loop_holding_coro is None:
            self.internal_async_loop = None
            self.internal_loop_creation_error = None
            try:
                if self._is_asyncio_loop_has_run_once_method():
                    internal_loop_holding_coro_worker = ExplicitWorker(CoroType.awaitable, _internal_loop_holding_coro_run_once_based)
                else:
                    internal_loop_holding_coro_worker = ExplicitWorker(CoroType.greenlet, _internal_loop_holding_coro)
            except ExternalAsyncioLoopAlreadyExistsError as ex:
                return True, None, ex
            
            self._internal_loop_holding_coro = self._loop.put_coro(internal_loop_holding_coro_worker, self, main_awaitable, priority, interrupt_when_no_requests, debug)
            if interrupt_when_no_requests:
                self._internal_loop_holding_coro.is_background_coro = True

        return False, None, None
    
    def _is_asyncio_loop_has_run_once_method(self) -> bool:
        result = False
        if events._get_running_loop() is not None:
            raise ExternalAsyncioLoopAlreadyExistsError

        loop = None
        try:
            loop = events.new_event_loop()
            if hasattr(loop, '_run_once'):
                result = True
        finally:
            if loop is not None:
                loop.close()
        
        return result
    
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
            exception = AsyncioLoopWasNotSetError()
        else:
            exception = None
        
        return True, self.async_loop, exception
    
    def register_await_response(self, coro_id: CoroID, response: Any, exception: Optional[Exception]):
        self.results[coro_id] = (response, exception)
        self.no_idle_calls.discard(coro_id)
        self.make_live()

    def _on_await(self, awaitable: Awaitable, intercommunication_request: bool = False, prevent_idle: bool = True) -> Tuple[bool, Any, Optional[Exception]]:
        if self.async_loop is None:
            return True, None, AsyncioLoopWasNotSetError()
        
        coro_id = self.current_caller_coro_info.coro_id
        if intercommunication_request:
            self.intercommunication_requests_coro_ids.add(coro_id)
        
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
        if prevent_idle:
            self.no_idle_calls.add(coro_id)
        
        self.make_live()
        
        return False, None, None

    def _on_create_task(self, awaitable: Awaitable) -> Tuple[bool, Optional[asyncio_Task], Optional[Exception]]:
        if self.async_loop is None:
            return True, None, AsyncioLoopWasNotSetError()

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
    
    def _on__internal_wait_for_new_requests(self) -> Tuple[bool, None, None]:
        if self.new_requests_num:
            return True, None, None
        else:
            self.waiting_for_new_requests = True
            return False, None, None
    
    def register_new_asyncio_request(self) -> None:
        self.new_requests_num += 1
        self.make_live()
    
    def add_on_idle_handler(self) -> None:
        if not self.use_higher_level_sleep_manager:
            self.current_on_idle_handler = self._on_system_loop_idle
            self._loop.on_idle_handlers.add(self._on_system_loop_idle)
    
    def discard_on_idle_handler(self) -> None:
        self._loop.on_idle_handlers.discard(self._on_system_loop_idle)
        self.current_on_idle_handler = None
    
    def _on__use_higher_level_sleep_manager(self, use_higher_level_sleep_manager: bool) -> Tuple[bool, Optional[None], None]:
        self.use_higher_level_sleep_manager = use_higher_level_sleep_manager
        if use_higher_level_sleep_manager:
            if self.current_on_idle_handler is not None:
                self._loop.on_idle_handlers.add(self.current_on_idle_handler)
        else:
            self.discard_on_idle_handler()
        
        return True, None, None

    def _on__low_latency_io_mode(self, low_latency_io_mode: bool) -> Tuple[bool, Optional[bool], None]:
        buff_low_latency_io_mode = self.low_latency_io_mode > 0
        if low_latency_io_mode:
            self.low_latency_io_mode += 1
        else:
            self.low_latency_io_mode -= 1
        
        return True, buff_low_latency_io_mode, None
    
    def _on_turn_on_loops_intercommunication(self, turn_on: bool) -> Tuple[bool, Optional[Callable], None]:
        result = self._loop.on_wrong_request
        if turn_on:
            self._previous_on_wrong_request = self._loop.on_wrong_request
            self.loops_intercommunication = True
            self._loop.on_wrong_request = self._on_wrong_request
        else:
            if self.loops_intercommunication:
                self._loop.on_wrong_request = self._previous_on_wrong_request
                self.loops_intercommunication = False
            
            self._previous_on_wrong_request = None
        
        return True, result, None
    
    def _on_wrong_request(self, coro: CoroWrapperBase, request: Any) -> Request:
        if request is None:
            args, kwargs = args_kwargs(AsyncioLoopRequest()._wait_intercommunication(asyncio_coro_sleep_0()))
            result: Request = Request(coro, type(self), *args, **kwargs)
        else:
            args, kwargs = args_kwargs(AsyncioLoopRequest()._wait_intercommunication(asyncio_coro_request(request)))
            result = Request(coro, type(self), *args, **kwargs)

        return result
    
    def inline_get(self):
        if self.async_loop is None:
            raise AsyncioLoopWasNotSetError
        else:
            return self.async_loop
    
    def inline_set_internal_loop(self, loop, exception: Optional[Exception]):
        self.internal_async_loop = loop
        self.internal_loop_creation_error = exception
        self.make_live()
    
    def is_need_to_yield_internal_loop(self) -> bool:
        return not self.pending_requests_num


AsyncioLoopRequest.default_service_type = AsyncioLoop


def _internal_loop_holding_coro(i: Interface, service: AsyncioLoop, main_awaitable: Optional[Awaitable] = None, priority: Optional[CoroPriority] = None, interrupt_when_no_requests: Optional[bool] = None, debug: bool = False):
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
                if service._idle_for is None:
                    loop.call_soon(on_loop_simple_yield)
                else:
                    idle_for = service._idle_for
                    service._idle_for = None
                    loop.call_later(idle_for, on_loop_simple_yield)
        
        def on_loop_loop_yield():
            if interrupt_when_no_requests and service.is_need_to_yield_internal_loop():
                i(AsyncioLoop, AsyncioLoopRequest()._internal_loop_yield())
            else:
                ly()
            
            if not service.need_to_stop_internal_loop:
                if service._idle_for is None:
                    loop.call_soon(on_loop_loop_yield)
                else:
                    idle_for = service._idle_for
                    service._idle_for = None
                    loop.call_later(idle_for, on_loop_loop_yield)
        
        if ly is None:
            loop.call_soon(on_loop_simple_yield)
        else:
            loop.call_soon(on_loop_loop_yield)

        if main_awaitable is not None:
            create_task_awaitable(main_awaitable)
    
    exception = None
    try:
        service.add_on_idle_handler()
        run_forever(main_wrapper(service, main_awaitable, priority, interrupt_when_no_requests), debug=debug)
    except:
        exception = get_exception()
        # TODO: do something with exception
    finally:
        try:
            service._loop.on_idle_handlers.discard(service._on_system_loop_idle)
            service.current_on_idle_handler = None
        except ValueError:
            pass

        service.inline_set_internal_loop(None, exception)


async def _internal_loop_holding_coro_run_once_based(i: Interface, service: AsyncioLoop, main_awaitable: Optional[Awaitable] = None, priority: Optional[CoroPriority] = None, interrupt_when_no_requests: Optional[bool] = None, debug: bool = False):
    from cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus import AsyncEventBusRequest, try_send_async_event
    from .known_asyncio_compatible_loops import prepare_loop, restore_loop

    cs: CoroScheduler = current_coro_scheduler()
    lyps: LoopYieldPriorityScheduler = cs.get_service_instance(LoopYieldPriorityScheduler)
    umsi: RationalNumber = get_usable_min_sleep_interval()

    ly = None
    if priority is not None:
        ly = await agly(priority)

    async def main_wrapper_for_run_once(service: AsyncioLoop, main_awaitable: Optional[Awaitable] = None):
        loop: AbstractEventLoop = get_event_loop()
        service.inline_set_internal_loop(loop, None)
        if main_awaitable is not None:
            create_task_awaitable(main_awaitable)
    
    if interrupt_when_no_requests is None:
        interrupt_when_no_requests = main_awaitable is None
    
    main_wrapper_for_run_once_coro = main_wrapper_for_run_once(service, main_awaitable)
    
    exception = None
    try:
        if events._get_running_loop() is not None:
            raise RuntimeError(
                'run_forever() cannot be called from a running event loop')

        if not coroutines.iscoroutine(main_wrapper_for_run_once_coro):
            raise ValueError('a coroutine was expected, got {!r}'.format(main_wrapper_for_run_once))

        loop = events.new_event_loop()
        service._original_loop_class = prepare_loop(loop)
        try:
            events.set_event_loop(loop)
            loop.set_debug(debug)
            loop.create_task(main_wrapper_for_run_once_coro)
            loop._check_closed()
            loop._check_running()
            loop._set_coroutine_origin_tracking(loop._debug)
            loop._thread_id = threading.get_ident()

            old_agen_hooks = sys.get_asyncgen_hooks()
            sys.set_asyncgen_hooks(firstiter=loop._asyncgen_firstiter_hook,
                                finalizer=loop._asyncgen_finalizer_hook)
            try:
                events._set_running_loop(loop)
                while True:
                    if ly is None:
                        await i(Yield)
                    else:
                        await ly()

                    loop.call_soon(lambda: None)
                    # if (not loop._ready) and (not loop._stopping) and (not loop._scheduled):
                    #     loop.call_soon(lambda: None)
                    
                    loop._run_once()
                    if loop._stopping:
                        break

                    if (not loop._ready) and (not loop._stopping):
                        if not loop._scheduled:
                            await i(AsyncioLoop, AsyncioLoopRequest()._internal_loop_yield())
                            continue
                        else:
                            when = loop._scheduled[0]._when
                            from asyncio.base_events import MAXIMUM_SELECT_TIMEOUT
                            timeout = min(max(0, when - loop.time()), MAXIMUM_SELECT_TIMEOUT)
                            # if get_min_sleep_interval() <= timeout:
                            #     usable_min_sleep_interval = get_usable_min_sleep_interval()
                            #     if usable_min_sleep_interval > timeout:
                            #         timeout = usable_min_sleep_interval

                            if (not service.low_latency_io_mode) and (0.001 <= timeout) and (not service.results):
                                service.new_requests_num = 0
                                service.make_dead()
                                async def waiting_coro(i: Interface, timeout: float):
                                    from cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus import AsyncEventBusRequest, try_send_async_event
                                    try:
                                        await i(Sleep, timeout)
                                        await i(AsyncEventBusRequest().send_event(WAITING_FOR_NEW_REQUESTS_EVENT, None))
                                    except WaitingCancelled:
                                        print(f'AsyncIoLoop {datetime.now().strftime("%H:%M:%S.%f")} >> WaitingCancelled')
                                
                                from datetime import datetime
                                try:
                                    # TODO: reimplement it in more efficient and elegant way. Btw: Sleep currently will not cancel an event upon coro destroyed
                                    lyps_max_delay = lyps.max_delay
                                    new_max_timeout = umsi if lyps_max_delay < umsi else lyps_max_delay
                                    new_timeout = timeout if new_max_timeout > timeout else new_max_timeout
                                    waiting_coro_id = await i(PutCoro, waiting_coro, new_timeout)
                                    service._waiting_coro_id = waiting_coro_id
                                    # await i(WaitCoro, WaitCoroRequest().single(waiting_coro_id))
                                    await i(AsyncEventBusRequest().wait(WAITING_FOR_NEW_REQUESTS_EVENT))
                                    # print(f'AsyncIoLoop {datetime.now().strftime("%H:%M:%S.%f")} >> WAITING_FOR_NEW_REQUESTS_EVENT')
                                except (WaitingCancelled, CoroutineNotFoundError):
                                    print(f'AsyncIoLoop {datetime.now().strftime("%H:%M:%S.%f")} >> WaitingCancelled or CoroutineNotFoundError')
                                    pass
                                except:
                                    print(f'AsyncIoLoop {datetime.now().strftime("%H:%M:%S.%f")} >> {get_exception()}')
                                    raise

                    if interrupt_when_no_requests and service.is_need_to_yield_internal_loop():
                        await i(AsyncioLoop, AsyncioLoopRequest()._internal_loop_yield())
                        continue
            finally:
                loop._stopping = False
                loop._thread_id = None
                events._set_running_loop(None)
                loop._set_coroutine_origin_tracking(False)
                sys.set_asyncgen_hooks(*old_agen_hooks)
        finally:
            restore_loop(loop, service._original_loop_class)
            try:
                cancel_all_tasks(loop)
                loop.run_until_complete(loop.shutdown_asyncgens())
            finally:
                events.set_event_loop(None)
                loop.close()
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
