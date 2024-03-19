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


# __all__ = []
__all__ = [
    'WaitType',
    'TasksListIsEmptyError',
    'IsNotDoneYetError',
    'NormalOnDoneHandler',
    'NormalInfo',
    'FastestOnDoneHandler',
    'FastestInfo',
    'FastestSuccessfulOnDoneHandler',
    'FastestSuccessfulInfo',
    'FastestExceptionOnDoneHandler',
    'FastestExceptionInfo',
    'FastestCustomOnDoneHandler',
    'FastestCustomInfo',
    'AtomicOnDoneHandler',
    'AtomicInfo',
    'AtomicCustomOnDoneHandler',
    'success_result_criteria_handler',
    'exception_result_criteria_handler',
    'same_first_failed_result_formatter',
    'none_first_failed_result_formatter',
    'AtomicCustomInfo',
    'GracefulTerminationSettings',
    'TerminationReason',
    'atask_graceful_destroyer',
    'aterminate_tasks_explicit',
    'aterminate_tasks_implicit',
    'aterminate_tasks',
    'aterminate_tasks_im',
    'terminate_tasks_explicit',
    'terminate_tasks_implicit',
    'terminate_tasks',
    'terminate_tasks_im',
    'await_tasks_explicit',
    'await_tasks_implicit',
    'await_tasks',
    'await_tasks_im',
    'wait_tasks_explicit',
    'wait_tasks_implicit',
    'wait_tasks',
    'wait_tasks_im',
    'await_tasks_fastest_explicit',
    'await_tasks_fastest_implicit',
    'await_tasks_fastest',
    'await_tasks_fastest_im',
    'wait_tasks_fastest_explicit',
    'wait_tasks_fastest_implicit',
    'wait_tasks_fastest',
    'wait_tasks_fastest_im',
    'await_tasks_fastest_successful_explicit',
    'await_tasks_fastest_successful_implicit',
    'await_tasks_fastest_successful',
    'await_tasks_fastest_successful_im',
    'wait_tasks_fastest_successful_explicit',
    'wait_tasks_fastest_successful_implicit',
    'wait_tasks_fastest_successful',
    'wait_tasks_fastest_successful_im',
    'await_tasks_fastest_exception_explicit',
    'await_tasks_fastest_exception_implicit',
    'await_tasks_fastest_exception',
    'await_tasks_fastest_exception_im',
    'wait_tasks_fastest_exception_explicit',
    'wait_tasks_fastest_exception_implicit',
    'wait_tasks_fastest_exception',
    'wait_tasks_fastest_exception_im',
    'await_tasks_fastest_custom_explicit',
    'await_tasks_fastest_custom_implicit',
    'await_tasks_fastest_custom',
    'await_tasks_fastest_custom_im',
    'wait_tasks_fastest_custom_explicit',
    'wait_tasks_fastest_custom_implicit',
    'wait_tasks_fastest_custom',
    'wait_tasks_fastest_custom_im',
    'await_tasks_atomic_explicit',
    'await_tasks_atomic_implicit',
    'await_tasks_atomic',
    'await_tasks_atomic_im',
    'wait_tasks_atomic_explicit',
    'wait_tasks_atomic_implicit',
    'wait_tasks_atomic',
    'wait_tasks_atomic_im',
    'await_tasks_atomic_custom_explicit',
    'await_tasks_atomic_custom_implicit',
    'await_tasks_atomic_custom',
    'await_tasks_atomic_custom_im',
    'wait_tasks_atomic_custom_explicit',
    'wait_tasks_atomic_custom_implicit',
    'wait_tasks_atomic_custom',
    'wait_tasks_atomic_custom_im',
    'wait_task_explicit',
    'wait_task_implicit',
    'wait_task',
    'wait_task_im',
    'await_task_explicit',
    'await_task_implicit',
    'await_task',
    'await_task_im',
]


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.2.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.parallel_execution.coroutines.coro_scheduler import Interface, current_interface, CoroID, get_interface_and_loop_with_explicit_loop
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import Task
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro_list import PutCoroList, PSCP
from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
from cengal.parallel_execution.coroutines.coro_standard_services.kill_coro_list import KillCoroList, KillSingleCoroParams
from cengal.parallel_execution.coroutines.coro_standard_services.wait_coro import TimeoutError, SubTimeoutError
from cengal.parallel_execution.coroutines.coro_standard_services.timer_func_runner import timer_func_run_on
from cengal.parallel_execution.coroutines.coro_tools.coro_flow_control import agraceful_coro_destroyer
from cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus import AsyncEventBusRequest, AsyncEventBus
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import CoroPriority
from cengal.parallel_execution.coroutines.coro_standard_services_internal_lib.service_with_a_direct_request import put_request_to_service

from uuid import uuid4
from enum import IntEnum
from typing import Optional, List, Union, Any, Type, Tuple, Dict, Callable


class WaitType(IntEnum):
    normal = 0
    fastest = 1
    fastest_successful = 2
    fastest_exception = 3
    fastest_custom = 4
    atomic = 5
    atomic_custom = 5


class TasksListIsEmptyError(Exception):
    pass


class IsNotDoneYetError(Exception):
    pass


class NormalOnDoneHandler:
    def __init__(self, normal_info: 'NormalInfo') -> None:
        self.normal_info: 'NormalInfo' = normal_info
    
    def __call__(self, task: Task) -> Any:
        self.normal_info.add_result(task.coro_id, task._result, task._exception)


class NormalInfo:
    def __init__(self, wait_done_id: str, tasks: List[Task]) -> None:
        self.tasks: List[Task] = tasks
        self.coroutines_num: int = len(tasks)
        self.results: List[Tuple[CoroID, Any, Exception]] = list()
        self.wait_done_id: str = wait_done_id
        self.ignore: bool = False
        self._done: bool = False
        self._timeout: bool = False
        self._failure: bool = False
    
    def add_result(self, coro_id: CoroID, result: Any, exception: Exception) -> None:
        if self.ignore:
            return
        
        self.results.append((coro_id, result, exception))
        if len(self.results) >= self.coroutines_num:
            self.done = True
    
    @property
    def failure(self) -> bool:
        return self._failure
    
    @failure.setter
    def failure(self, value: bool) -> None:
        self._failure = value
    
    @property
    def done(self) -> bool:
        return self._done
    
    @done.setter
    def done(self, value: bool) -> None:
        if self._done:
            return
        
        self._done = value
        if value:
            self.ignore = True
            put_request_to_service(AsyncEventBus, self.wait_done_id, None, CoroPriority.high)
    
    @property
    def timeout(self) -> bool:
        return self._timeout
    
    def on_timeout(self) -> None:
        self._timeout = True
        self.done = True
    
    def gather(self) -> List[Tuple[CoroID, Any, Exception]]:
        if not self.done:
            raise IsNotDoneYetError
        
        return self.results


# =================================================================================


class FastestOnDoneHandler:
    def __init__(self, fastest_info: 'FastestInfo') -> None:
        self.fastest_info: 'FastestInfo' = fastest_info
    
    def __call__(self, task: Task) -> Any:
        self.fastest_info.add_result((task.coro_id, task._result, task._exception))


class FastestInfo(NormalInfo):
    def __init__(self, wait_done_id: str, tasks: List[Task]) -> None:
        super().__init__(wait_done_id, tasks)
        self.coroutines_num: int = 1


# =================================================================================


class FastestSuccessfulOnDoneHandler:
    def __init__(self, fastest_successful_info: 'FastestSuccessfulInfo') -> None:
        self.fastest_successful_info: 'FastestSuccessfulInfo' = fastest_successful_info
    
    def __call__(self, task: Task) -> Any:
        self.fastest_successful_info.add_result((task.coro_id, task._result, task._exception))


class FastestSuccessfulInfo(NormalInfo):
    def __init__(self, wait_done_id: str, tasks: List[Task]) -> None:
        super().__init__(wait_done_id, tasks)
        self.fastest_successful_result: Optional[Tuple[CoroID, Any, Exception]] = None
    
    def add_result(self, coro_id: CoroID, result: Any, exception: Exception) -> None:
        if self.ignore:
            return
        
        self.results.append((coro_id, result, exception))
        if exception is None:
            self.fastest_successful_result = (coro_id, result, exception)
            self.done = True
        elif (len(self.results) >= self.coroutines_num):
            self.done = True
    
    def gather(self) -> List[Tuple[CoroID, Any, Exception]]:
        if not self.done:
            raise IsNotDoneYetError
        
        if self.fastest_successful_result is None:
            self.failure = True
        
        return [self.fastest_successful_result]


# =================================================================================


class FastestExceptionOnDoneHandler:
    def __init__(self, fastest_exception_info: 'FastestExceptionInfo') -> None:
        self.fastest_exception_info: 'FastestExceptionInfo' = fastest_exception_info
    
    def __call__(self, task: Task) -> Any:
        self.fastest_exception_info.add_result((task.coro_id, task._result, task._exception))


class FastestExceptionInfo(NormalInfo):
    def __init__(self, wait_done_id: str, tasks: List[Task]) -> None:
        super().__init__(wait_done_id, tasks)
        self.fastest_exception_result: Optional[Tuple[CoroID, Any, Exception]] = None
    
    def add_result(self, coro_id: CoroID, result: Any, exception: Exception) -> None:
        if self.ignore:
            return
        
        self.results.append((coro_id, result, exception))
        if exception is not None:
            self.fastest_exception_result = (coro_id, result, exception)
            self.done = True
        elif (len(self.results) >= self.coroutines_num):
            self.done = True
    
    def gather(self) -> List[Tuple[CoroID, Any, Exception]]:
        if not self.done:
            raise IsNotDoneYetError
        
        if self.fastest_exception_result is None:
            self.failure = True
        
        return [self.fastest_exception_result]


# =================================================================================


class FastestCustomOnDoneHandler:
    def __init__(self, fastest_custom_info: 'FastestCustomInfo') -> None:
        self.fastest_custom_info: 'FastestCustomInfo' = fastest_custom_info
    
    def __call__(self, task: Task) -> Any:
        self.fastest_custom_info.add_result((task.coro_id, task._result, task._exception))


class FastestCustomInfo(NormalInfo):
    def __init__(self, wait_done_id: str, tasks: List[Task], result_criteria_handler: Callable[[CoroID, Any, Exception], bool]) -> None:
        super().__init__(wait_done_id, tasks)
        self.result_criteria_handler: Callable[[CoroID, Any, Exception], bool] = result_criteria_handler
        self.fastest_custom_result: Optional[Tuple[CoroID, Any, Exception]] = None
    
    def add_result(self, coro_id: CoroID, result: Any, exception: Exception) -> None:
        if self.ignore:
            return
        
        self.results.append((coro_id, result, exception))
        if self.result_criteria_handler(coro_id, result, exception):
            self.fastest_custom_result = (coro_id, result, exception)
            self.done = True
        elif (len(self.results) >= self.coroutines_num):
            self.done = True
    
    def gather(self) -> List[Tuple[CoroID, Any, Exception]]:
        if not self.done:
            raise IsNotDoneYetError
        
        if self.fastest_custom_result is None:
            self.failure = True
        
        return [self.fastest_custom_result]


# =================================================================================


class AtomicOnDoneHandler:
    def __init__(self, atomic_info: 'AtomicInfo') -> None:
        self.atomic_info: 'AtomicInfo' = atomic_info
    
    def __call__(self, task: Task) -> Any:
        self.atomic_info.add_result(task.coro_id, task._result, task._exception)


class AtomicInfo(NormalInfo):
    def __init__(self, wait_done_id: str, tasks: List[Task], include_first_failure: bool = True) -> None:
        super().__init__(wait_done_id, tasks)
        self.include_first_failure: bool = include_first_failure
    
    def add_result(self, coro_id: CoroID, result: Any, exception: Exception) -> None:
        if self.ignore:
            return
        
        if exception is not None:
            if self.include_first_failure:
                self.results.append((coro_id, result, exception))
            
            self.failure = True
            self.done = True
        else:
            self.results.append((coro_id, result, exception))
        
        if len(self.results) >= self.coroutines_num:
            self.done = True
    
    def gather(self) -> List[Tuple[CoroID, Any, Exception]]:
        if not self.done:
            raise IsNotDoneYetError
        
        normalized_results: List[Tuple[CoroID, Any, Exception]] = list()
        provided_results: Dict[CoroID, Tuple[Any, Exception]] = dict()
        for result_info in self.results:
            if result_info is None:
                continue

            coro_id, result, exception = result_info
            provided_results[coro_id] = (result, exception)
        
        for task in self.tasks:
            coro_id = task.coro_id
            if coro_id in provided_results:
                result, exception = provided_results[coro_id]
                normalized_results.append((coro_id, result, exception))
            else:
                normalized_results.append(None)
        
        return normalized_results


# =================================================================================


class AtomicCustomOnDoneHandler:
    def __init__(self, atomic_custom_info: 'AtomicCustomInfo') -> None:
        self.atomic_custom_info: 'AtomicCustomInfo' = atomic_custom_info
    
    def __call__(self, task: Task) -> Any:
        self.atomic_custom_info.add_result(task.coro_id, task._result, task._exception)


def success_result_criteria_handler(coro_id: CoroID, result: Any, exception: Exception) -> bool:
    return exception is None


def exception_result_criteria_handler(coro_id: CoroID, result: Any, exception: Exception) -> bool:
    return exception is not None


def same_first_failed_result_formatter(coro_id: CoroID, result: Any, exception: Exception) -> Any:
    return (coro_id, result, exception)


def none_first_failed_result_formatter(coro_id: CoroID, result: Any, exception: Exception) -> Any:
    return None


class AtomicCustomInfo(NormalInfo):
    def __init__(
            self, 
            wait_done_id: str, 
            tasks: List[Task], 
            result_criteria_handler: Callable[[CoroID, Any, Exception], bool], 
            first_failed_result_formatter: Optional[Callable[[CoroID, Any, Exception], Any]] = None,
            ) -> None:
        super().__init__(wait_done_id, tasks)
        self.result_criteria_handler: Callable[[CoroID, Any, Exception], bool] = result_criteria_handler
        self.first_failed_result_formatter: Callable[[CoroID, Any, Exception], Any] = \
            none_first_failed_result_formatter if first_failed_result_formatter is None else first_failed_result_formatter
    
    def add_result(self, coro_id: CoroID, result: Any, exception: Exception) -> None:
        if self.ignore:
            return
        
        self.results.append((coro_id, result, exception))
        if (len(self.results) >= self.coroutines_num) or (exception is not None):
            self.done = True
        
        if not self.result_criteria_handler(coro_id, result, exception):
            result = self.first_failed_result_formatter(coro_id, result, exception)
            self.failure = True
            self.done = True
        else:
            result = (coro_id, result, exception)
        
        self.results.append(result)
        if len(self.results) >= self.coroutines_num:
            self.done = True
    
    def gather(self) -> List[Tuple[CoroID, Any, Exception]]:
        if not self.done:
            raise IsNotDoneYetError
        
        normalized_results: List[Tuple[CoroID, Any, Exception]] = list()
        provided_results: Dict[CoroID, Tuple[Any, Exception]] = dict()
        for result_info in self.results:
            if result_info is None:
                continue

            coro_id, result, exception = result_info
            provided_results[coro_id] = (result, exception)
        
        for task in self.tasks:
            coro_id = task.coro_id
            if coro_id in provided_results:
                result, exception = provided_results[coro_id]
                normalized_results.append((coro_id, result, exception))
            else:
                normalized_results.append(None)
        
        return normalized_results


# =================================================================================


class GracefulTerminationSettings:
    def __init__(self, 
                 phase_time_limit: Optional[float], 
                 ex_type: Type[Exception] = None, ex_value: Exception = None, ex_traceback: Any = None, 
                 first_phase_is_wait: bool = True,
                 last_phase_is_kill: bool = True, 
                 ) -> None:
        self.phase_time_limit: Optional[float] = phase_time_limit
        self.ex_type: Type[Exception] = ex_type
        self.ex_value: Exception = ex_value
        self.ex_traceback: Any = ex_traceback
        self.first_phase_is_wait: bool = first_phase_is_wait
        self.last_phase_is_kill: bool = last_phase_is_kill


class TerminationReason(IntEnum):
    success = 0
    failure = 1
    timeout = 2

                
async def atask_graceful_destroyer(
        i: Interface, 
        task: Task, 
        tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        ) -> None:
    await agraceful_coro_destroyer(
        i, 
        graceful_termination_settings.phase_time_limit, 
        task.coro_id, 
        graceful_termination_settings.ex_type, 
        graceful_termination_settings.ex_value, 
        graceful_termination_settings.ex_traceback, 
        tree, 
        graceful_termination_settings.first_phase_is_wait, 
        graceful_termination_settings.last_phase_is_kill, 
        )


async def aterminate_tasks_explicit(
        i: Interface, 
        tasks: List[Task], 
        termination_reason: TerminationReason,
        tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> bool:
    if not tasks:
        return False
    
    if terminate_other_tasks is not None:
        terminate_other_tasks_on_success = terminate_other_tasks
        terminate_other_tasks_on_failure = terminate_other_tasks
        terminate_other_tasks_on_timeout = terminate_other_tasks

    if ((TerminationReason.success == termination_reason) and terminate_other_tasks_on_success) or \
        ((TerminationReason.failure == termination_reason) and terminate_other_tasks_on_failure) or \
            ((TerminationReason.timeout == termination_reason) and terminate_other_tasks_on_timeout):
        if graceful_termination_settings is None:
            termination_tasks_params: List[KillSingleCoroParams] = list([KillSingleCoroParams(task.coro_id, tree) for task in tasks if not task.done])
            if not termination_tasks_params:
                return False
            
            i(KillCoroList, termination_tasks)
        else:
            termination_tasks_params: List[PSCP] = [PSCP(atask_graceful_destroyer, task, tree, graceful_termination_settings) for task in tasks if not task.done]
            if not termination_tasks_params:
                return False
            
            termination_tasks: List[Task] = await i(PutCoroList, termination_tasks_params, True)
            if wait_for_termination:
                await await_tasks_explicit(i, termination_tasks, False, None, None, False, False, False, False)
    
    return True


async def aterminate_tasks_implicit(
        tasks: List[Task], 
        termination_reason: TerminationReason,
        tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> bool:
    i: Interface = current_interface()
    return await aterminate_tasks_explicit(
        i, 
        tasks, 
        termination_reason, 
        tree, 
        graceful_termination_settings, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


aterminate_tasks: Callable = aterminate_tasks_explicit
aterminate_tasks_im: Callable = aterminate_tasks_implicit


def terminate_tasks_explicit(
        i: Interface, 
        tasks: List[Task], 
        termination_reason: TerminationReason,
        tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> bool:
    i(RunCoro, aterminate_tasks_explicit,
        tasks, 
        termination_reason, 
        tree, 
        graceful_termination_settings, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


def terminate_tasks_implicit(
        tasks: List[Task], 
        termination_reason: TerminationReason,
        tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> bool:
    i: Interface = current_interface()
    return terminate_tasks_explicit(
        i, 
        tasks, 
        termination_reason, 
        tree, 
        graceful_termination_settings, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


terminate_tasks: Callable = terminate_tasks_explicit
terminate_tasks_im: Callable = terminate_tasks_implicit


# =================================================================================


async def await_tasks_explicit(
        i: Interface, 
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    if isinstance(tasks, Task):
        tasks = [tasks]
    
    if not tasks:
        raise TasksListIsEmptyError

    normal_wait_id: str = str(f'wait_task__normal__{uuid4()}')
    normal_info: NormalInfo = NormalInfo(normal_wait_id, tasks)

    if timeout is not None:
        # TODO: implement discard timer request when needed in order to improve performance
        timer_func_run_on(get_interface_and_loop_with_explicit_loop(i._loop), timeout, normal_info.on_timeout)

    for another_task in tasks:
        another_task.add_on_done_handler(NormalOnDoneHandler(normal_info))
    
    await i(AsyncEventBus, AsyncEventBusRequest().wait(normal_wait_id))
    results: List[Tuple[CoroID, Any, Exception]] = normal_info.gather()
    if normal_info.timeout:
        termination_reason: TerminationReason = TerminationReason.timeout
    elif normal_info.failure:
        termination_reason = TerminationReason.failure
    else:
        termination_reason = TerminationReason.success

    await terminate_tasks_explicit(
        i, 
        tasks, 
        termination_reason, 
        terminate_tree, 
        graceful_termination_settings, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )
    return results


async def await_tasks_implicit(
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i: Interface = current_interface()
    return await await_tasks_explicit(
        i, 
        tasks, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


await_tasks: Callable = await_tasks_explicit
await_tasks_im: Callable = await_tasks_implicit


def wait_tasks_explicit(
        i: Interface, 
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i(RunCoro, await_tasks_explicit,
        tasks, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


def wait_tasks_implicit(
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i: Interface = current_interface()
    return wait_tasks_explicit(
        i, 
        tasks, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


wait_tasks: Callable = wait_tasks_explicit
wait_tasks_im: Callable = wait_tasks_implicit


# =================================================================================


async def await_tasks_fastest_explicit(
        i: Interface, 
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> Tuple[CoroID, Any]:
    if isinstance(tasks, Task):
        tasks = [tasks]
    
    if not tasks:
        raise TasksListIsEmptyError

    fastest_wait_id: str = str(f'wait_task__fastest__{uuid4()}')
    fastest_info: FastestInfo = FastestInfo(fastest_wait_id, tasks)

    if timeout is not None:
        # TODO: implement discard timer request when needed in order to improve performance
        timer_func_run_on(get_interface_and_loop_with_explicit_loop(i._loop), timeout, fastest_info.on_timeout)

    for another_task in tasks:
        another_task.add_on_done_handler(FastestOnDoneHandler(fastest_info))
    
    await i(AsyncEventBus, AsyncEventBusRequest().wait(fastest_wait_id))
    results: List[Tuple[CoroID, Any, Exception]] = fastest_info.gather()
    if fastest_info.timeout:
        termination_reason: TerminationReason = TerminationReason.timeout
    elif fastest_info.failure:
        termination_reason = TerminationReason.failure
    else:
        termination_reason = TerminationReason.success

    await aterminate_tasks_explicit(
        i, 
        tasks, 
        termination_reason, 
        terminate_tree, 
        graceful_termination_settings, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )
    if not results:
        return None, None
    
    coro_id, result, exception = results[0]
    if exception is not None:
        if isinstance(exception, TimeoutError) and (coro_id is not None):
            exception = SubTimeoutError()
        
        raise exception
    
    return coro_id, result


async def await_tasks_fastest_implicit(
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i: Interface = current_interface()
    return await await_tasks_fastest_explicit(
        i, 
        tasks, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


await_tasks_fastest: Callable = await_tasks_fastest_explicit
await_tasks_fastest_im: Callable = await_tasks_fastest_implicit


def wait_tasks_fastest_explicit(
        i: Interface, 
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i(RunCoro, await_tasks_fastest_explicit,
        tasks, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


def wait_tasks_fastest_implicit(
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i: Interface = current_interface()
    return wait_tasks_fastest_explicit(
        i, 
        tasks, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


wait_tasks_fastest: Callable = wait_tasks_fastest_explicit
wait_tasks_fastest_im: Callable = wait_tasks_fastest_implicit


# =================================================================================


async def await_tasks_fastest_successful_explicit(
        i: Interface, 
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> Tuple[CoroID, Any]:
    if isinstance(tasks, Task):
        tasks = [tasks]
    
    if not tasks:
        raise TasksListIsEmptyError

    fastest_successful_wait_id: str = str(f'wait_task__fastest_successful__{uuid4()}')
    fastest_successful_info: FastestSuccessfulInfo = FastestSuccessfulInfo(fastest_successful_wait_id, tasks)

    if timeout is not None:
        # TODO: implement discard timer request when needed in order to improve performance
        timer_func_run_on(get_interface_and_loop_with_explicit_loop(i._loop), timeout, fastest_successful_info.on_timeout)

    for another_task in tasks:
        another_task.add_on_done_handler(FastestSuccessfulOnDoneHandler(fastest_successful_info))
    
    await i(AsyncEventBus, AsyncEventBusRequest().wait(fastest_successful_wait_id))
    results: List[Tuple[CoroID, Any, Exception]] = fastest_successful_info.gather()
    if fastest_successful_info.timeout:
        termination_reason: TerminationReason = TerminationReason.timeout
    elif fastest_successful_info.failure:
        termination_reason = TerminationReason.failure
    else:
        termination_reason = TerminationReason.success

    await aterminate_tasks_explicit(
        i, 
        tasks, 
        termination_reason, 
        terminate_tree, 
        graceful_termination_settings, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )
    if not results:
        return None, None
    
    coro_id, result, exception = results[0]
    if exception is not None:
        if isinstance(exception, TimeoutError) and (coro_id is not None):
            exception = SubTimeoutError()
        
        raise exception
    
    return coro_id, result


async def await_tasks_fastest_successful_implicit(
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i: Interface = current_interface()
    return await await_tasks_fastest_successful_explicit(
        i, 
        tasks, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


await_tasks_fastest_successful: Callable = await_tasks_fastest_successful_explicit
await_tasks_fastest_successful_im: Callable = await_tasks_fastest_successful_implicit


def wait_tasks_fastest_successful_explicit(
        i: Interface, 
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i(RunCoro, await_tasks_explicit,
        tasks, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


def wait_tasks_fastest_successful_implicit(
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i: Interface = current_interface()
    return wait_tasks_fastest_successful_explicit(
        i, 
        tasks, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


wait_tasks_fastest_successful: Callable = wait_tasks_fastest_successful_explicit
wait_tasks_fastest_successful_im: Callable = wait_tasks_fastest_successful_implicit


# =================================================================================


async def await_tasks_fastest_exception_explicit(
        i: Interface, 
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> Tuple[CoroID, Exception]:
    if isinstance(tasks, Task):
        tasks = [tasks]
    
    if not tasks:
        raise TasksListIsEmptyError

    fastest_exception_wait_id: str = str(f'wait_task__fastest_exception__{uuid4()}')
    fastest_exception_info: FastestExceptionInfo = FastestExceptionInfo(fastest_exception_wait_id, tasks)

    if timeout is not None:
        # TODO: implement discard timer request when needed in order to improve performance
        timer_func_run_on(get_interface_and_loop_with_explicit_loop(i._loop), timeout, fastest_exception_info.on_timeout)

    for another_task in tasks:
        another_task.add_on_done_handler(FastestExceptionOnDoneHandler(fastest_exception_info))
    
    await i(AsyncEventBus, AsyncEventBusRequest().wait(fastest_exception_wait_id))
    results: List[Tuple[CoroID, Any, Exception]] = fastest_exception_info.gather()
    if fastest_exception_info.timeout:
        termination_reason: TerminationReason = TerminationReason.timeout
    elif fastest_exception_info.failure:
        termination_reason = TerminationReason.failure
    else:
        termination_reason = TerminationReason.success

    await aterminate_tasks_explicit(
        i, 
        tasks, 
        termination_reason, 
        terminate_tree, 
        graceful_termination_settings, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )
    if not results:
        return None, None
    
    coro_id, result, exception = results[0]
    if exception is not None:
        if isinstance(exception, TimeoutError) and (coro_id is not None):
            exception = SubTimeoutError()
    
    return coro_id, exception


async def await_tasks_fastest_exception_implicit(
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i: Interface = current_interface()
    return await await_tasks_explicit(
        i, 
        tasks, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


await_tasks_fastest_exception: Callable = await_tasks_fastest_exception_explicit
await_tasks_fastest_exception_im: Callable = await_tasks_fastest_exception_implicit


def wait_tasks_fastest_exception_explicit(
        i: Interface, 
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i(RunCoro, await_tasks_fastest_exception_explicit,
        tasks, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


def wait_tasks_fastest_exception_implicit(
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i: Interface = current_interface()
    return wait_tasks_fastest_exception_explicit(
        i, 
        tasks, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


wait_tasks_fastest_exception: Callable = wait_tasks_fastest_exception_explicit
wait_tasks_fastest_exception_im: Callable = wait_tasks_fastest_exception_implicit


# =================================================================================


async def await_tasks_fastest_custom_explicit(
        i: Interface, 
        tasks: Union[Task, List[Task]], 
        result_criteria_handler: Callable[[CoroID, Any, Exception], bool], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> Tuple[CoroID, Any]:
    if isinstance(tasks, Task):
        tasks = [tasks]
    
    if not tasks:
        raise TasksListIsEmptyError

    fastest_custom_wait_id: str = str(f'wait_task__fastest_custom__{uuid4()}')
    fastest_custom_info: FastestCustomInfo = FastestCustomInfo(fastest_custom_wait_id, tasks, result_criteria_handler)

    if timeout is not None:
        # TODO: implement discard timer request when needed in order to improve performance
        timer_func_run_on(get_interface_and_loop_with_explicit_loop(i._loop), timeout, fastest_custom_info.on_timeout)

    for another_task in tasks:
        another_task.add_on_done_handler(FastestCustomOnDoneHandler(fastest_custom_info))
    
    await i(AsyncEventBus, AsyncEventBusRequest().wait(fastest_custom_wait_id))
    results: List[Tuple[CoroID, Any, Exception]] = fastest_custom_info.gather()
    if fastest_custom_info.timeout:
        termination_reason: TerminationReason = TerminationReason.timeout
    elif fastest_custom_info.failure:
        termination_reason = TerminationReason.failure
    else:
        termination_reason = TerminationReason.success

    await aterminate_tasks_explicit(
        i, 
        tasks, 
        termination_reason, 
        terminate_tree, 
        graceful_termination_settings, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )
    if not results:
        return None, None
    
    coro_id, result, exception = results[0]
    if exception is not None:
        if isinstance(exception, TimeoutError) and (coro_id is not None):
            exception = SubTimeoutError()
        
        raise exception
    
    return coro_id, result


async def await_tasks_fastest_custom_implicit(
        tasks: Union[Task, List[Task]], 
        result_criteria_handler: Callable[[CoroID, Any, Exception], bool], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i: Interface = current_interface()
    return await await_tasks_fastest_custom_explicit(
        i, 
        tasks, 
        result_criteria_handler, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


await_tasks_fastest_custom: Callable = await_tasks_fastest_custom_explicit
await_tasks_fastest_custom_im: Callable = await_tasks_fastest_custom_implicit


def wait_tasks_fastest_custom_explicit(
        i: Interface, 
        tasks: Union[Task, List[Task]], 
        result_criteria_handler: Callable[[CoroID, Any, Exception], bool], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i(RunCoro, await_tasks_fastest_custom_explicit,
        tasks, 
        result_criteria_handler, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


def wait_tasks_fastest_custom_implicit(
        tasks: Union[Task, List[Task]], 
        result_criteria_handler: Callable[[CoroID, Any, Exception], bool], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i: Interface = current_interface()
    return wait_tasks_fastest_custom_explicit(
        i, 
        tasks, 
        result_criteria_handler, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


wait_tasks_fastest_custom: Callable = wait_tasks_fastest_custom_explicit
wait_tasks_fastest_custom_im: Callable = wait_tasks_fastest_custom_implicit


# =================================================================================


async def await_tasks_atomic_explicit(
        i: Interface, 
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ):
    if terminate_other_tasks is not None:
        terminate_other_tasks_on_success = terminate_other_tasks
        terminate_other_tasks_on_failure = terminate_other_tasks
        terminate_other_tasks_on_timeout = terminate_other_tasks

    if isinstance(tasks, Task):
        tasks = [tasks]
    
    if not tasks:
        raise TasksListIsEmptyError

    atomic_wait_id: str = str(f'wait_task__atomic__{uuid4()}')
    atomic_info: AtomicInfo = AtomicInfo(atomic_wait_id, tasks)

    if timeout is not None:
        # TODO: implement discard timer request when needed in order to improve performance
        timer_func_run_on(get_interface_and_loop_with_explicit_loop(i._loop), timeout, atomic_info.on_timeout)

    for another_task in tasks:
        another_task.add_on_done_handler(AtomicOnDoneHandler(atomic_info))
    
    await i(AsyncEventBus, AsyncEventBusRequest().wait(atomic_wait_id))
    results: List[Tuple[CoroID, Any, Exception]] = atomic_info.gather()
    if atomic_info.timeout:
        termination_reason: TerminationReason = TerminationReason.timeout
    elif atomic_info.failure:
        termination_reason = TerminationReason.failure
    else:
        termination_reason = TerminationReason.success

    await aterminate_tasks_explicit(
        i, 
        tasks, 
        termination_reason, 
        terminate_tree, 
        graceful_termination_settings, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )
    return results


async def await_tasks_atomic_implicit(
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i: Interface = current_interface()
    return await await_tasks_atomic_explicit(
        i, 
        tasks, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


await_tasks_atomic: Callable = await_tasks_atomic_explicit
await_tasks_atomic_im: Callable = await_tasks_atomic_implicit


def wait_tasks_atomic_explicit(
        i: Interface, 
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i(RunCoro, await_tasks_atomic_explicit,
        tasks, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


def wait_tasks_atomic_implicit(
        tasks: Union[Task, List[Task]], 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i: Interface = current_interface()
    return wait_tasks_atomic_explicit(
        i, 
        tasks, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


wait_tasks_atomic: Callable = wait_tasks_atomic_explicit
wait_tasks_atomic_im: Callable = wait_tasks_atomic_implicit


# =================================================================================


async def await_tasks_atomic_custom_explicit(
        i: Interface, 
        tasks: Union[Task, List[Task]], 
        result_criteria_handler: Callable[[CoroID, Any, Exception], bool], 
        first_failed_result_formatter: Optional[Callable[[CoroID, Any, Exception], Any]] = None, 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ):
    if terminate_other_tasks is not None:
        terminate_other_tasks_on_success = terminate_other_tasks
        terminate_other_tasks_on_failure = terminate_other_tasks
        terminate_other_tasks_on_timeout = terminate_other_tasks

    if isinstance(tasks, Task):
        tasks = [tasks]
    
    if not tasks:
        raise TasksListIsEmptyError

    atomic_custom_wait_id: str = str(f'wait_task__atomic_custom__{uuid4()}')
    atomic_custom_info: AtomicCustomInfo = AtomicCustomInfo(
        atomic_custom_wait_id, 
        tasks, 
        result_criteria_handler, 
        first_failed_result_formatter, 
        )

    if timeout is not None:
        # TODO: implement discard timer request when needed in order to improve performance
        timer_func_run_on(get_interface_and_loop_with_explicit_loop(i._loop), timeout, atomic_custom_info.on_timeout)

    for another_task in tasks:
        another_task.add_on_done_handler(AtomicCustomOnDoneHandler(atomic_custom_info))
    
    await i(AsyncEventBus, AsyncEventBusRequest().wait(atomic_custom_wait_id))
    results: List[Tuple[CoroID, Any, Exception]] = atomic_custom_info.gather()
    if atomic_custom_info.timeout:
        termination_reason: TerminationReason = TerminationReason.timeout
    elif atomic_custom_info.failure:
        termination_reason = TerminationReason.failure
    else:
        termination_reason = TerminationReason.success

    await aterminate_tasks_explicit(
        i, 
        tasks, 
        termination_reason, 
        terminate_tree, 
        graceful_termination_settings, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )
    return results


async def await_tasks_atomic_custom_implicit(
        tasks: Union[Task, List[Task]], 
        result_criteria_handler: Callable[[CoroID, Any, Exception], bool], 
        first_failed_result_formatter: Optional[Callable[[CoroID, Any, Exception], Any]] = None, 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i: Interface = current_interface()
    return await await_tasks_atomic_custom_explicit(
        i, 
        tasks, 
        result_criteria_handler, 
        first_failed_result_formatter, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


await_tasks_atomic_custom: Callable = await_tasks_atomic_custom_explicit
await_tasks_atomic_custom_im: Callable = await_tasks_atomic_custom_implicit


def wait_tasks_atomic_custom_explicit(
        i: Interface, 
        tasks: Union[Task, List[Task]], 
        result_criteria_handler: Callable[[CoroID, Any, Exception], bool], 
        first_failed_result_formatter: Optional[Callable[[CoroID, Any, Exception], Any]] = None, 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i(RunCoro, await_tasks_atomic_custom_explicit,
        tasks, 
        result_criteria_handler, 
        first_failed_result_formatter, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


def wait_tasks_atomic_custom_implicit(
        tasks: Union[Task, List[Task]], 
        result_criteria_handler: Callable[[CoroID, Any, Exception], bool], 
        first_failed_result_formatter: Optional[Callable[[CoroID, Any, Exception], Any]] = None, 
        terminate_tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        timeout: Optional[float] = None, 
        terminate_other_tasks: Optional[bool] = None, 
        terminate_other_tasks_on_success: bool = False, 
        terminate_other_tasks_on_failure: bool = False, 
        terminate_other_tasks_on_timeout: bool = False, 
        wait_for_termination: bool = False, 
        ) -> List[Tuple[CoroID, Any, Exception]]:
    i: Interface = current_interface()
    return wait_tasks_atomic_custom_explicit(
        i, 
        tasks, 
        result_criteria_handler, 
        first_failed_result_formatter, 
        terminate_tree, 
        graceful_termination_settings, 
        timeout, 
        terminate_other_tasks, 
        terminate_other_tasks_on_success, 
        terminate_other_tasks_on_failure, 
        terminate_other_tasks_on_timeout, 
        wait_for_termination, 
        )


wait_tasks_atomic_custom: Callable = wait_tasks_atomic_custom_explicit
wait_tasks_atomic_custom_im: Callable = wait_tasks_atomic_custom_implicit


# =================================================================================


def wait_task_explicit(i: Interface, task: Union[Task, List[Task]]):
    wait_id: str = str(f'wait_task__{uuid4()}')
    def on_done_handler():
        put_request_to_service(AsyncEventBus, wait_id, None, CoroPriority.high)

    task.add_on_done_handler(on_done_handler)
    i(AsyncEventBus, AsyncEventBusRequest().wait(wait_id))
    return task.result


def wait_task_implicit(task: Union[Task, List[Task]]):
    i: Interface = current_interface()
    wait_id: str = str(f'wait_task__{uuid4()}')
    def on_done_handler():
        put_request_to_service(AsyncEventBus, wait_id, None, CoroPriority.high)

    task.add_on_done_handler(on_done_handler)
    i(AsyncEventBus, AsyncEventBusRequest().wait(wait_id))
    return task.result


wait_task = wait_task_explicit
wait_task_im = wait_task_implicit


async def await_task_explicit(i: Interface, task: Union[Task, List[Task]]):
    wait_id: str = str(f'wait_task__{uuid4()}')
    def on_done_handler():
        put_request_to_service(AsyncEventBus, wait_id, None, CoroPriority.high)

    task.add_on_done_handler(on_done_handler)
    await i(AsyncEventBus, AsyncEventBusRequest().wait(wait_id))
    return task.result


async def await_task_implicit(task: Union[Task, List[Task]]):
    i: Interface = current_interface()
    wait_id: str = str(f'wait_task__{uuid4()}')
    def on_done_handler():
        put_request_to_service(AsyncEventBus, wait_id, None, CoroPriority.high)

    task.add_on_done_handler(on_done_handler)
    await i(AsyncEventBus, AsyncEventBusRequest().wait(wait_id))
    return task.result


await_task = await_task_explicit
await_task_im = await_task_implicit
