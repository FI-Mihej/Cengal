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


__all__ = ['TimerCoroRunner', 'add_timer_coro_run_from_other_service', 'discard_timer_coro_run_from_other_service', 'timer_coro_run_on', 'try_timer_coro_run_on', 'atimer_coro_run_on', 'atry_timer_coro_run_on', 'timer_coro_run', 'try_timer_coro_run', 'atimer_coro_run', 'atry_timer_coro_run']

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services_internal_lib.service_with_a_direct_request import *
from cengal.code_flow_control.smart_values import ValueExistence
from cengal.time_management.timer import Timer, TimerRequest
from functools import partial
from typing import Tuple, Optional, Union
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import put_current_from_other_service, put_root_from_other_service, put_from_other_service


class TimerCoroRunnerRequest(ServiceRequest):
    def add(self, delay: float, coro_worker: AnyWorker, *args, **kwargs) -> TimerRequest:
        return self._save(0, delay, coro_worker, args, kwargs)
    def discard(self, timer_request: TimerRequest) -> bool:
        return self._save(1, timer_request)


class TimerCoroRunner(DualImmediateProcessingServiceMixin, ServiceWithADirectRequestMixin, TypedService[TimerRequest]):
    def __init__(self, loop: CoroScheduler):
        super(TimerCoroRunner, self).__init__(loop)
        self.timer = Timer()
        self.pending_tasks_number = 0
        self.direct_requests = list()
        self._request_workers = {
            0: self._on_add,
            1: self._on_discard,
        }

    def single_task_registration_or_immediate_processing_single(
            self, delay: float, coro_worker: AnyWorker, *args, **kwargs) -> Tuple[bool, None]:
        timer_request: TimerRequest = self._add_request_impl(delay, coro_worker, *args, **kwargs)
        self.make_live()
        return True, timer_request, None
    
    def _add_request_impl(self, delay: float, coro_worker: AnyWorker, *args, **kwargs):
        def timer_handler_func(caller_coro_id, coro_worker_: AnyWorker, *args_, **kwargs_):
            put_from_other_service(self, caller_coro_id, coro_worker_, *args_, **kwargs_)
            self.task_triggered()

        timer_handler = partial(timer_handler_func, self.current_caller_coro_info.coro_id, coro_worker, *args, **kwargs)
        self.task_added()
        return self.timer.register(timer_handler, delay)
    
    def _add_request_external_impl(self, delay: float, coro_worker: AnyWorker, *args, **kwargs):
        def timer_handler_func(coro_worker_: AnyWorker, *args_, **kwargs_):
            try:
                put_root_from_other_service(self, coro_worker_, *args_, **kwargs_)
            finally:
                self.task_triggered()

        timer_handler = partial(timer_handler_func, coro_worker, *args, **kwargs)
        self.task_added()
        return self.timer.register(timer_handler, delay)
    
    def _on_add(self, delay: float, coro_worker: AnyWorker, *args, **kwargs) -> Tuple[bool, TimerRequest, None]:
        timer_request: TimerRequest = self._add_request_impl(delay, coro_worker, *args, **kwargs)
        self.make_live()
        return True, timer_request, None
    
    def _on_discard(self, timer_request: TimerRequest) -> Tuple[bool, TimerRequest, None]:
        result: bool = self.timer.discard(timer_request)
        if result:
            self.task_triggered()
        
        return True, result, None
    
    def add_timer_coro_run_from_other_service(self, delay: float, coro_worker: AnyWorker, *args, **kwargs) -> TimerRequest:
        timer_request: TimerRequest = self._add_request_external_impl(delay, coro_worker, *args, **kwargs)
        self.make_live()
        return timer_request
    
    def discard_timer_coro_run_from_other_service(self, timer_request: TimerRequest):
        result: bool = self.timer.discard(timer_request)
        if result:
            self.task_triggered()
        
        return result

    def full_processing_iteration(self):
        if self.direct_requests:
            direct_requests_buff = self.direct_requests
            self.direct_requests = type(direct_requests_buff)()
            for delay, coro_worker, args, kwargs in direct_requests_buff:
                self._add_request_external_impl(delay, coro_worker, *args, **kwargs)

        self.timer()
        if 0 == self.pending_tasks_number:
            self.make_dead()
    
    def _add_direct_request(self, delay: float, coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[None]:
        self.direct_requests.append((delay, coro_worker, args, kwargs))
        self.make_live()
        return ValueExistence()

    def task_added(self):
        self.pending_tasks_number += 1

    def task_triggered(self):
        self.pending_tasks_number -= 1

    def in_work(self) -> bool:
        result: bool = (self.pending_tasks_number != 0) or bool(self.direct_requests)
        return self.thrifty_in_work(result)
    
    def time_left_before_next_event(self) -> Tuple[bool, Optional[Union[int, float]]]:
        return True, self.timer.nearest_event()


TimerCoroRunnerRequest.default_service_type = TimerCoroRunner


def add_timer_coro_run_from_other_service(current_service: Service, delay: float, coro_worker: AnyWorker, *args, **kwargs) -> TimerRequest:
    timer_coro_runner: TimerCoroRunner = current_service._loop.get_service_instance(TimerCoroRunner)
    return timer_coro_runner.add_timer_coro_run_from_other_service(delay, coro_worker, *args, **kwargs)


def discard_timer_coro_run_from_other_service(current_service: Service, timer_request: TimerRequest) -> bool:
    timer_coro_runner: TimerCoroRunner = current_service._loop.get_service_instance(TimerCoroRunner)
    return timer_coro_runner.discard_timer_coro_run_from_other_service(timer_request)


def timer_coro_run_on(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], delay: float, coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[Optional[CoroID]]:
    """_summary_
        context can be generated by one of the [interface_and_loop_with_backup_loop, get_interface_and_loop_with_backup_loop, interface_and_loop_with_explicit_loop, get_interface_and_loop_with_explicit_loop, interface_for_an_explicit_loop, get_interface_for_an_explicit_loop] functions from the cengal/parallel_execution/coroutines/coro_scheduler module
        
        An example:

        from cengal.parallel_execution.coroutines.coro_scheduler import get_interface_and_loop_with_explicit_loop, CoroScheduler, ExplicitWorker, Worker, CoroID
        from cengal.parallel_execution.coroutines.coro_standard_services.timer_coro_runner import timer_coro_run_on
        from typing import Optional, Union

        def my_func(loop: CoroScheduler, coro_worker: AnyWorker, a, b) -> Optional[CoroID]:
            try:
                def print_hello_world(i: Interface, name: str):
                    print(f'Hello Wrold from {name}!)
                
                timer_coro_run_on(10, print_hello_world, 'John Doe')
            except CoroSchedulerContextIsNotAvailable:
                print('We are outside of the loop AND no loop was selected as a Primary AND our given `loop` var is None)
        
    Args:
        context (Tuple[Optional[CoroScheduler], Optional[Interface], bool]): _description_
        delay (float): delay in seconds
        coro_worker (AnyWorker): coro_worker

    Returns:
        ValueExistence[Optional[CoroID]]: _description_
    """
    return make_request_to_service_with_context(context, TimerCoroRunner, delay, coro_worker, *args, **kwargs)


def try_timer_coro_run_on(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], delay: float, coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[Optional[CoroID]]:
    """_summary_
        context can be generated by one of the [interface_and_loop_with_backup_loop, get_interface_and_loop_with_backup_loop, interface_and_loop_with_explicit_loop, get_interface_and_loop_with_explicit_loop, interface_for_an_explicit_loop, get_interface_for_an_explicit_loop] functions from the cengal/parallel_execution/coroutines/coro_scheduler module
        
        An example:

        from cengal.parallel_execution.coroutines.coro_scheduler import get_interface_and_loop_with_explicit_loop, CoroScheduler, ExplicitWorker, Worker, CoroID
        from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import try_put_coro_to
        from typing import Optional, Union

        def my_func(loop: CoroScheduler, coro_worker: AnyWorker, a, b) -> Optional[CoroID]:
            def print_hello_world(i: Interface, name: str):
                print(f'Hello Wrold from {name}!)
            
            try_timer_coro_run_on(10, print_hello_world, 'John Doe')
        
    Args:
        context (Tuple[Optional[CoroScheduler], Optional[Interface], bool]): _description_
        delay (float): delay in seconds
        coro_worker (AnyWorker): coro_worker

    Returns:
        ValueExistence[Optional[CoroID]]: _description_
    """
    return try_make_request_to_service_with_context(context, TimerCoroRunner, delay, coro_worker, *args, **kwargs)


async def atimer_coro_run_on(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], delay: float, coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[CoroID]:
    return await amake_request_to_service_with_context(context, TimerCoroRunner, delay, coro_worker, *args, **kwargs)


async def atry_timer_coro_run_on(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], delay: float, coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[Optional[CoroID]]:
    return await atry_make_request_to_service_with_context(context, TimerCoroRunner, delay, coro_worker, *args, **kwargs)


def timer_coro_run(delay: float, coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[CoroID]:
    return make_request_to_service(TimerCoroRunner, delay, coro_worker, *args, **kwargs)


def try_timer_coro_run(delay: float, coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[Optional[CoroID]]:
    return try_make_request_to_service(TimerCoroRunner, delay, coro_worker, *args, **kwargs)


async def atimer_coro_run(delay: float, coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[CoroID]:
    return await amake_request_to_service(TimerCoroRunner, delay, coro_worker, *args, **kwargs)


async def atry_timer_coro_run(delay: float, coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[Optional[CoroID]]:
    return await atry_make_request_to_service(TimerCoroRunner, delay, coro_worker, *args, **kwargs)
