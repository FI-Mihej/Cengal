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


__all__ = [
    'CoroPriority', 'ThisCoroWasRequestedToBeKilled', 'LoopYieldPrioritySchedulerRequest', 'LoopYieldManagedBase', 'LoopYieldManaged',
    'LoopYieldManagedAsync', 'FakeLoopYieldManaged', 'LoopYieldPriorityScheduler', 'get_loop_yield',
    'gly', 'aget_loop_yield', 'agly', 'LoopYieldManagedAsyncExternal', 'FakeLoopYieldManagedAsync', 'external_aget_loop_yield', 'eagly'
]

from asyncio.events import Handle
from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_tools.await_coro import *
from enum import Enum
from typing import Callable, Dict, Tuple, Union, Type, Optional, Any, Set, Hashable
from cengal.time_management.repeat_for_a_time import Tracer, TimeLimitIsTooSmall
from cengal.code_flow_control.smart_values.versions.v_1 import ValueExistence
from async_generator import asynccontextmanager, async_generator, yield_
import asyncio
import sys


MIN_TIME = 0.000001


class CoroPriority(Enum):
    high = 0
    normal = 1
    low = 2


class LoopYieldPrioritySchedulerRequest(ServiceRequest):
    def register(self, default_priority: CoroPriority) -> 'LoopYieldManagedBase':
        return self._save(0, default_priority)

    def setup(self, max_delay: float) -> None:
        return self._save(1, max_delay)

    def change_priority(self, new_priority: CoroPriority, old_priority: CoroPriority) -> None:
        return self._save(2, new_priority, old_priority)

    def get(self) -> 'LoopYieldManagedBase':
        return self._save(3)

    def register_external(self, asyncio_loop: asyncio.AbstractEventLoop, default_priority: CoroPriority) -> 'LoopYieldManagedAsyncExternal':
        return self._save(4, asyncio_loop, default_priority)

    def register_external_asyncio_task(self, asyncio_loop: asyncio.AbstractEventLoop, task: asyncio.Task, default_priority: CoroPriority) -> 'LoopYieldManagedAsyncExternal':
        return self._save(5, asyncio_loop, task, default_priority)

    def change_priority_external(self, loop_yield: 'LoopYieldManagedAsyncExternal', new_priority: CoroPriority, old_priority: CoroPriority) -> None:
        return self._save(6, loop_yield, new_priority, old_priority)

    def del_external(self, loop_yield: 'LoopYieldManagedAsyncExternal') -> None:
        return self._save(7, loop_yield)

    def request_coro_kill(self, coro_id: CoroID) -> None:
        """Make request for a coro kill asynchronously (immidiately returns). An exception ThisCoroWasRequestedToBeKilled will be emmited in coro with a requested coro_id during one of it's next requests to LoopYield service

        Args:
            coro_id (CoroID): _description_

        Returns:
            ServiceRequest: _description_
        """        
        return self._save(8, coro_id)
    
    def kill_coro(self, coro_id: CoroID) -> None:
        """Make request for a coro kill synchronously (waits for next steps). An exception ThisCoroWasRequestedToBeKilled will be emmited in coro with a requested coro_id during one of it's next requests to LoopYield service. After an exception was sent to the requested coro_id, current coro will receive an answer from the service (None).

        Args:
            coro_id (CoroID): _description_

        Returns:
            ServiceRequest: _description_
        """        
        return self._save(9, coro_id)


class LoopYieldManagedBase:
    def __init__(self, interface: Interface, time_atom: ValueExistence,
                 default_priority: CoroPriority, service: Type[Service]):
        self._interface = None
        self.interface = interface
        self.time_atom = time_atom
        self.default_priority = default_priority
        self.priority = self.default_priority
        self.service = service
        self.tracer = None

    @property
    def interface(self):
        if self._interface is None:
            self._interface = current_interface()
        
        return self._interface

    @interface.setter
    def interface(self, value):
        self._interface = value


class LoopYieldManaged(LoopYieldManagedBase):
    def __init__(self, interface: Interface, time_atom: ValueExistence,
                 default_priority: CoroPriority, service: Type[Service]):
        super(LoopYieldManaged, self).__init__(interface, time_atom, default_priority, service)

    def __call__(self, priority: Optional[CoroPriority] = None):
        if priority is None:
            priority = self.default_priority
        
        if priority != self.priority:
            self.interface = None
            self.interface(self.service, LoopYieldPrioritySchedulerRequest().change_priority(priority,
                                                                                             self.priority))
            self.priority = priority
            try:
                self.tracer = Tracer(self.time_atom.result)
            except TimeLimitIsTooSmall as ex:
                self.tracer = Tracer(ex.min_time if ex.min_time is not None else MIN_TIME)
        
        if self.tracer is None:
            exception = None
            try:
                self.tracer = Tracer(self.time_atom.result)
            except TimeLimitIsTooSmall as ex:
                exception = ex

            if exception is not None:
                try:
                    self.tracer = Tracer(exception.min_time if exception.min_time is not None else MIN_TIME)
                except TimeLimitIsTooSmall as ex:
                    print(ex)
                
        if self.tracer is not None:
            if not self.tracer.iter():
                self.tracer = None
                self.interface = None
                self.interface(self.service)


class LoopYieldManagedAsync(LoopYieldManagedBase):
    def __init__(self, interface: Interface, time_atom: ValueExistence,
                 default_priority: CoroPriority, service: Type[Service]):
        super(LoopYieldManagedAsync, self).__init__(interface, time_atom, default_priority, service)

    async def __call__(self, priority: Optional[CoroPriority] = None):
        if priority is None:
            priority = self.default_priority
        if priority != self.priority:
            self.interface = None
            await self.interface(self.service, LoopYieldPrioritySchedulerRequest().change_priority(priority,
                                                                                                   self.priority))
            self.priority = priority
            try:
                self.tracer = Tracer(self.time_atom.result)
            except TimeLimitIsTooSmall as ex:
                self.tracer = Tracer(ex.min_time if ex.min_time is not None else MIN_TIME)
        if self.tracer is None:
            try:
                self.tracer = Tracer(self.time_atom.result)
            except TimeLimitIsTooSmall as ex:
                self.tracer = Tracer(ex.min_time if ex.min_time is not None else MIN_TIME)
        if not self.tracer.iter():
            self.tracer = None
            self.interface = None
            await self.interface(self.service)


class LoopYieldManagedAsyncExternal(LoopYieldManagedBase):
    def __init__(self, task_id: int, time_atom: ValueExistence,
                 default_priority: CoroPriority, service: Type[Service], coro_scheduler: CoroScheduler, asyncio_loop: asyncio.AbstractEventLoop):
        super(LoopYieldManagedAsyncExternal, self).__init__(None, time_atom, default_priority, service)
        self.task_id = task_id
        self.coro_scheduler = coro_scheduler
        self.asyncio_loop = asyncio_loop
        self.asyncio_task: asyncio.Task = None
        self.on_done_asyncio_coro: Callable = None

    async def __call__(self, priority: Optional[CoroPriority] = None):
        if priority is None:
            priority = self.default_priority
        if priority != self.priority:
            await await_task_fast(self.asyncio_loop, self.coro_scheduler, self.service,
                                  LoopYieldPrioritySchedulerRequest().change_priority_external(self, priority, self.priority))
            self.priority = priority
            try:
                self.tracer = Tracer(self.time_atom.result)
            except TimeLimitIsTooSmall as ex:
                self.tracer = Tracer(ex.min_time if ex.min_time is not None else MIN_TIME)
        if self.tracer is None:
            try:
                self.tracer = Tracer(self.time_atom.result)
            except TimeLimitIsTooSmall as ex:
                self.tracer = Tracer(ex.min_time if ex.min_time is not None else MIN_TIME)
        if not self.tracer.iter():
            self.tracer = None
            await await_task_fast(self.asyncio_loop, self.coro_scheduler, self.service)


class FakeLoopYieldManaged:
    def __call__(self, priority: Optional[CoroPriority] = None):
        pass

class FakeLoopYieldManagedAsync:
    async def __call__(self, priority: Optional[CoroPriority] = None):
        pass


class ThisCoroWasRequestedToBeKilled(Exception):
    pass


class LoopYieldPriorityScheduler(TypedService[None], EntityStatsMixin):
    def __init__(self, loop: CoroScheduler):
        super(LoopYieldPriorityScheduler, self).__init__(loop)

        # loop.add_global_on_coro_del_handler(self._on_coro_del_handler_global)  # Todo: switch to local coro del handler

        self._request_workers = {
            0: self._on_register,
            1: self._on_setup,
            2: self._on_change_priority,
            3: self._on_get,
            4: self._on_register_external,
            5: self._on_register_external_asyncio_task,
            6: self._on_change_priority_external,
            7: self._on_del_external,
            8: self._request_coro_kill,
            9: self._kill_coro,
        }

        self.sigma = {
            0: 0.6827,
            1: 0.9545 - 0.6827,
            2: 1.0 - 0.9545,
        }

        self.max_delay = 0.01
        self.max_delays = {
            0: 0.0,
            1: 0.0,
            2: 0.0,
        }
        self.compute_delays()

        self.all_yield_objects = dict()  # type: Dict[CoroID, LoopYieldManagedBase]
        self.task_counter = Counter()
        while self.task_counter.get() <= 0:
            pass
        
        self.yields_num: int = 0
        self.coroutines_requested_to_be_deleted: Set[CoroID] = set()
        self.coroutines_requested_to_be_deleted_by_waiters: Dict[CoroID, Set[CoroID]] = dict()
        self.finished_waiters_for_coro_kill: Set[CoroID] = set()
        self.asyncio_task_ids: Dict[Hashable, int] = dict()

        self.yields_by_priority: Dict[CoroPriority, int] = {
            CoroPriority.high:   0,
            CoroPriority.normal: 0,
            CoroPriority.low:    0,
        }

        self.time_atom_by_priority = {
            CoroPriority.high:   ValueExistence(True, self.max_delays[0]),
            CoroPriority.normal: ValueExistence(True, self.max_delays[1]),
            CoroPriority.low:    ValueExistence(True, self.max_delays[2]),
        }

    def get_entity_stats(self, stats_level: 'EntityStatsMixin.StatsLevel' = EntityStatsMixin.StatsLevel.debug) -> Tuple[str, Dict[str, Any]]:
        coroutines_requested_to_be_killed = self.coroutines_requested_to_be_deleted | set(self.coroutines_requested_to_be_deleted_by_waiters.keys())
        return type(self).__name__, {
            'task counter': self.task_counter._index,
            'yields num': self.yields_num,
            'max_delay': self.max_delay,
            'max_delays': self.max_delays,
            'affected coroutines num': len(self.all_yield_objects),
            'coroutines num by priority': {
                'high': self.yields_by_priority[CoroPriority.high],
                'normal': self.yields_by_priority[CoroPriority.normal],
                'low': self.yields_by_priority[CoroPriority.low],
            },
            'time atoms by priority': {
                'high': self.time_atom_by_priority[CoroPriority.high].result,
                'normal': self.time_atom_by_priority[CoroPriority.normal].result,
                'low': self.time_atom_by_priority[CoroPriority.low].result,
            },
            'coroutines requested to be killed': {
                'num': len(coroutines_requested_to_be_killed),
                'list': coroutines_requested_to_be_killed,
            }
        }

    def single_task_registration_or_immediate_processing(self, request: Optional[LoopYieldPrioritySchedulerRequest]=None
                                                         ) -> Tuple[bool, Any, None]:
        self.yields_num += 1
        coro_should_be_killed = False
        coro_id = self.current_caller_coro_info.coro_id
        if coro_id in self.coroutines_requested_to_be_deleted:
            coro_should_be_killed = True
        
        if coro_id in self.coroutines_requested_to_be_deleted_by_waiters:
            self.finished_waiters_for_coro_kill |= self.coroutines_requested_to_be_deleted_by_waiters[coro_id]
            self.make_live()
            coro_should_be_killed = True
        
        if request is not None:
            if coro_should_be_killed and (self._on_del_external != self._request_workers[request.request_type]):
                return True, None, ThisCoroWasRequestedToBeKilled
                
            return self.resolve_request(request)

        if coro_should_be_killed:
            return True, None, ThisCoroWasRequestedToBeKilled
        
        return True, None, None

    def full_processing_iteration(self):
        for coro_id in self.finished_waiters_for_coro_kill:
            self.register_response(coro_id, None)
        
        self.compute_time_atoms()

    def compute_time_atoms(self):
        if self.all_yield_objects:
            top_sigma = 0

            if self.yields_by_priority[CoroPriority.high]:
                top_sigma += 1

            if self.yields_by_priority[CoroPriority.normal]:
                top_sigma += 1

            if self.yields_by_priority[CoroPriority.low]:
                top_sigma += 1

            median_time_atom = 1 / len(self.all_yield_objects)  # !!! Possible division by zero! Conditional must not be removed!
            if 1 == top_sigma:
                sigma_0_time_atom = min(median_time_atom, self.max_delays[0])
                self.time_atom_by_priority[CoroPriority.high].result = sigma_0_time_atom
                self.time_atom_by_priority[CoroPriority.normal].result = sigma_0_time_atom
                self.time_atom_by_priority[CoroPriority.low].result = sigma_0_time_atom
            elif 2 == top_sigma:
                sigma_0_time_atom = min(median_time_atom * self.sigma[0], self.max_delays[0])
                sigma_1_time_atom = min(median_time_atom * self.sigma[1], self.max_delays[1])
                if self.yields_by_priority[CoroPriority.high]:
                    self.time_atom_by_priority[CoroPriority.high].result = sigma_0_time_atom
                    self.time_atom_by_priority[CoroPriority.normal].result = sigma_1_time_atom
                    self.time_atom_by_priority[CoroPriority.low].result = sigma_1_time_atom
                else:
                    self.time_atom_by_priority[CoroPriority.high].result = sigma_0_time_atom
                    self.time_atom_by_priority[CoroPriority.normal].result = sigma_0_time_atom
                    self.time_atom_by_priority[CoroPriority.low].result = sigma_1_time_atom
            elif 3 == top_sigma:
                sigma_0_time_atom = min(median_time_atom * self.sigma[0], self.max_delays[0])
                sigma_1_time_atom = min(median_time_atom * self.sigma[1], self.max_delays[1])
                sigma_2_time_atom = min(median_time_atom * self.sigma[2], self.max_delays[2])
                self.time_atom_by_priority[CoroPriority.high].result = sigma_0_time_atom
                self.time_atom_by_priority[CoroPriority.normal].result = sigma_1_time_atom
                self.time_atom_by_priority[CoroPriority.low].result = sigma_2_time_atom
        
        self.make_dead()

    def in_work(self) -> bool:
        result: bool = bool(self.finished_waiters_for_coro_kill) or bool(self.all_yield_objects)
        return self.thrifty_in_work(result)

    def compute_delays(self):
        self.max_delays = {
            0: self.max_delay * self.sigma[0],
            1: self.max_delay * self.sigma[1],
            2: self.max_delay * self.sigma[2],
        }

    def _on_register(self, default_priority: CoroPriority):
        task_id = self.current_caller_coro_info.coro_id
        if task_id in self.all_yield_objects:
            loop_yield = self.all_yield_objects[task_id]
        else:
            interface: Interface = self.current_caller_coro_info.coro.interface
            if isinstance(interface, InterfaceGreenlet):
                loop_yield = LoopYieldManaged(interface,
                                            self.time_atom_by_priority[default_priority],
                                            default_priority,
                                            type(self))
            elif isinstance(interface, InterfaceAsyncAwait):
                loop_yield = LoopYieldManagedAsync(interface,
                                                self.time_atom_by_priority[default_priority],
                                                default_priority,
                                                type(self))
            else:
                raise NotImplementedError
            
            loop_yield.time_atom = self.time_atom_by_priority[loop_yield.priority]
            self.all_yield_objects[interface.coro_id] = loop_yield
            self.current_caller_coro_info.coro.add_on_coro_del_handler(self._on_coro_del_handler)
            self.yields_by_priority[loop_yield.priority] += 1
            self.make_live()
        
        return True, loop_yield, None

    def _on_setup(self, max_delay: float):
        self.max_delay = max_delay
        self.compute_delays()
        # self.compute_time_atoms()
        self.make_live()
        return True, None, None

    def _on_change_priority(self, new_priority: CoroPriority, old_priority: CoroPriority):
        self.yields_by_priority[old_priority] -= 1
        self.yields_by_priority[new_priority] += 1
        loop_yield = self.all_yield_objects[self.current_caller_coro_info.coro_id]
        loop_yield.time_atom = self.time_atom_by_priority[new_priority]
        self.make_live()
        return True, None, None

    def _on_get(self):
        return True, self.all_yield_objects.get(self.current_caller_coro_info.coro_id), None

    def get_yield_object(self, coro_id: CoroID) -> LoopYieldManagedBase:
        return self.all_yield_objects.get(coro_id)
    
    def _on_register_external(self, asyncio_loop: asyncio.AbstractEventLoop, default_priority: CoroPriority):
        task_id = -(self.task_counter.get())
        loop_yield = LoopYieldManagedAsyncExternal(task_id,
                                                   self.time_atom_by_priority[default_priority],
                                                   default_priority,
                                                   type(self),
                                                   self._loop,
                                                   asyncio_loop)
        loop_yield.time_atom = self.time_atom_by_priority[loop_yield.priority]
        self.all_yield_objects[task_id] = loop_yield
        self.yields_by_priority[loop_yield.priority] += 1
        self.make_live()
        return True, loop_yield, None
    
    def _on_register_external_asyncio_task(self, asyncio_loop: asyncio.AbstractEventLoop, task: asyncio.Task, default_priority: CoroPriority):
        asyncio_task_id = id(task)
        if asyncio_task_id not in self.asyncio_task_ids:
            self.asyncio_task_ids[asyncio_task_id] = -(self.task_counter.get())
            
        task_id = self.asyncio_task_ids[asyncio_task_id]
        if task_id in self.all_yield_objects:
            loop_yield = self.all_yield_objects[task_id]
        else:
            loop_yield = LoopYieldManagedAsyncExternal(task_id,
                                                    self.time_atom_by_priority[default_priority],
                                                    default_priority,
                                                    type(self),
                                                    self._loop,
                                                    asyncio_loop)
            def on_done_asyncio_coro(future):
                self._on_del_external(loop_yield)
                task.remove_done_callback(loop_yield.on_done_asyncio_coro)
            
            loop_yield.asyncio_task = task
            loop_yield.on_done_asyncio_coro = on_done_asyncio_coro
            task.add_done_callback(loop_yield.on_done_asyncio_coro)
            loop_yield.time_atom = self.time_atom_by_priority[loop_yield.priority]
            self.all_yield_objects[task_id] = loop_yield
            self.yields_by_priority[loop_yield.priority] += 1
            self.make_live()
        
        return True, loop_yield, None
    
    def _on_change_priority_external(self, loop_yield: LoopYieldManagedAsyncExternal, new_priority: CoroPriority, old_priority: CoroPriority):
        self.yields_by_priority[old_priority] -= 1
        self.yields_by_priority[new_priority] += 1
        loop_yield.time_atom = self.time_atom_by_priority[new_priority]
        self.make_live()
        return True, None, None
    
    def _on_del_external(self, loop_yield: LoopYieldManagedAsyncExternal):
        task_id = loop_yield.task_id
        if task_id in self.all_yield_objects:
            priority = self.all_yield_objects[task_id].priority
            del self.all_yield_objects[task_id]
            self.yields_by_priority[priority] -= 1
        self.make_live()
        return True, None, None
    
    def _request_coro_kill(self, coro_id: CoroID) -> ServiceProcessingResponse:
        self.coroutines_requested_to_be_deleted.add(coro_id)
        return True, None, None
    
    def _kill_coro(self, coro_id: CoroID) -> ServiceProcessingResponse:
        waiter_coro_id = self.current_caller_coro_info
        if coro_id not in self.coroutines_requested_to_be_deleted_by_waiters:
            self.coroutines_requested_to_be_deleted_by_waiters[coro_id] = set()
        
        self.coroutines_requested_to_be_deleted_by_waiters[coro_id].add(waiter_coro_id)
        return False, None, None

    def _on_coro_del_handler_global(self, coro: CoroWrapperBase) -> bool:
        coro_id = coro.coro_id
        if coro_id in self.all_yield_objects:
            priority = self.all_yield_objects[coro_id].priority
            del self.all_yield_objects[coro_id]
            self.yields_by_priority[priority] -= 1
            self.make_live()
        return False

    def _on_coro_del_handler(self, coro: CoroWrapperBase) -> bool:
        coro_id = coro.coro_id
        priority = self.all_yield_objects[coro_id].priority
        del self.all_yield_objects[coro_id]
        self.yields_by_priority[priority] -= 1
        self.make_live()
        return False


LoopYieldPrioritySchedulerRequest.default_service_type = LoopYieldPriorityScheduler


def get_loop_yield(default_priority: CoroPriority = CoroPriority.normal) -> Union[LoopYieldManaged, FakeLoopYieldManaged]:
    loop = CoroScheduler.current_loop()
    if loop is None:
        return FakeLoopYieldManaged()  # running not from inside the loop

    interface = loop.current_interface()
    if interface is None:
        return FakeLoopYieldManaged()  # running from Service

    # ly = interface(LoopYieldPriorityScheduler, LoopYieldPrioritySchedulerRequest().get())
    ly = interface._loop.get_service_instance(LoopYieldPriorityScheduler).get_yield_object(interface.coro_id)
    if ly is None:
        ly = interface(LoopYieldPriorityScheduler, LoopYieldPrioritySchedulerRequest().register(default_priority))
    
    return ly


gly = get_loop_yield


async def aget_loop_yield(default_priority: CoroPriority = CoroPriority.normal) -> Union[LoopYieldManagedAsync, FakeLoopYieldManagedAsync]:
    loop = CoroScheduler.current_loop()
    if loop is None:
        return FakeLoopYieldManagedAsync()  # running not from inside the loop

    interface = loop.current_interface()
    if interface is None:
        return FakeLoopYieldManagedAsync()  # running from Service

    # ly = await interface(LoopYieldPriorityScheduler, LoopYieldPrioritySchedulerRequest().get())
    ly = interface._loop.get_service_instance(LoopYieldPriorityScheduler).get_yield_object(interface.coro_id)
    if ly is None:
        ly = await interface(LoopYieldPriorityScheduler, LoopYieldPrioritySchedulerRequest().register(default_priority))
    
    return ly


agly = aget_loop_yield


@asynccontextmanager
@async_generator
async def external_aget_loop_yield(default_priority: CoroPriority = CoroPriority.normal, coro_scheduler: Optional[CoroScheduler]=None, asyncio_loop: Optional[asyncio.AbstractEventLoop]=None):
    if coro_scheduler is None:
        coro_scheduler = CoroScheduler.current_loop()
    
    if coro_scheduler is None:
        await yield_(FakeLoopYieldManagedAsync())  # can not determine coro scheduler loop
    else:
        if asyncio_loop is None:
            asyncio_loop = asyncio.get_event_loop()
        
        if (3, 7) <= sys.version_info:
            ly: LoopYieldManagedAsyncExternal = await await_task_fast(
                asyncio_loop, coro_scheduler, LoopYieldPriorityScheduler,
                LoopYieldPrioritySchedulerRequest().register_external_asyncio_task(asyncio_loop, asyncio.current_task(loop=asyncio_loop), default_priority))
        else:
            ly: LoopYieldManagedAsyncExternal = await await_task_fast(
                asyncio_loop, coro_scheduler, LoopYieldPriorityScheduler,
                LoopYieldPrioritySchedulerRequest().register_external(asyncio_loop, default_priority))

        try:
            await yield_(ly)
        finally:
            if (3, 7) > sys.version_info:
                await await_task_fast(asyncio_loop, coro_scheduler, LoopYieldPriorityScheduler,
                                    LoopYieldPrioritySchedulerRequest().del_external(ly))

eagly = external_aget_loop_yield
