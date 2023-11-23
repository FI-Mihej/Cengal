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
    'RWOperation', 'RWLockerRequest', 'RWLockerEntity', 'RWLockerContextManager', 'FakeRWLockerContextManager', 'UnknownLockerEntity', 'RWLocker', 'get_rw_lock', 'grwl', 'aget_rw_lock', 'agrwl'
]

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_tools.await_coro import *
from enum import Enum
from typing import Dict, Hashable, Tuple, Union, Type, Optional, Any, List, Set
from cengal.time_management.repeat_for_a_time import Tracer
from cengal.code_flow_control.smart_values.versions.v_1 import ValueExistence
from async_generator import asynccontextmanager, async_generator, yield_
import asyncio


class RWOperation(Enum):
    read = 0
    write = 1


class RWLockerRequest(ServiceRequest):
    def register(self, entity_id: Hashable, max_writers_in_progress: int, max_readers_in_progress: int, recursive: bool = True) -> 'RWLockerContextManager':
        return self._save(0, entity_id, max_writers_in_progress, max_readers_in_progress, recursive)

    def deregister(self, entity_id: Hashable, safe: bool = True) -> bool:
        return self._save(1, entity_id, safe)
    
    def wait_for_write(self, entity_id: Hashable) -> None:
        return self._save(2, entity_id)
    
    def wait_for_read(self, entity_id: Hashable) -> None:
        return self._save(3, entity_id)


class RWLockerEntity:
    def __init__(self, entity_id: Hashable, max_writers_in_progress: int, max_readers_in_progress: int, recursive: bool, service: Type[Service]):
        self.entity_id: Hashable = entity_id
        self.recursive: bool = recursive
        self.service = service
        self.writers_pending: int = 0
        self.writers_in_progress_dict: Dict[CoroID, int] = dict()
        self.writers_in_progress: int = 0
        self.max_writers_in_progress: int = max_writers_in_progress  # Must be edited directly from coroutine. In order to eliminate new writers arrived during the end of the current loop iteration
        self.readers_pending: int = 0
        self.readers_in_progress_dict: Dict[CoroID, int] = dict()
        self.readers_in_progress: int = 0
        self.max_readers_in_progress: int = max_readers_in_progress  # Must be edited directly from coroutine. In order to eliminate new readers arrived during the end of the current loop iteration
        self.last_operation: RWOperation = RWOperation.read  # Default is 'RWOperation.read' in order to force 'write' as a first operation among several first concurent operations
        self.waiting_coroutines: Set[CoroID] = set()
        self.related_coroutines: Set[CoroID] = set()

    def check_writers_in_progress_boundaries(self, coro_id: Optional[CoroID] = None) -> bool:
        if self.recursive:
            if 0 > self.max_writers_in_progress:
                return True
            else:
                if coro_id in self.writers_in_progress_dict:
                    return True
                else:
                    return self.writers_in_progress < self.max_writers_in_progress
        else:
            if 0 > self.max_writers_in_progress:
                return True
            else:
                return self.writers_in_progress < self.max_writers_in_progress
    
    def increase_writers_in_progress(self, coro_id: Optional[CoroID] = None):
        if self.recursive:
            if coro_id not in self.writers_in_progress_dict:
                self.writers_in_progress_dict[coro_id] = 0
                self.writers_in_progress += 1
            
            self.writers_in_progress_dict[coro_id] += 1
        else:
            self.writers_in_progress += 1
    
    def decrease_writers_in_progress(self, coro_id: Optional[CoroID] = None):
        if self.recursive:
            self.writers_in_progress_dict[coro_id] -= 1
            if 0 >= self.writers_in_progress_dict[coro_id]:
                del self.writers_in_progress_dict[coro_id]
                self.writers_in_progress -= 1
        else:
            self.writers_in_progress -= 1

    def check_readers_in_progress_boundaries(self, coro_id: Optional[CoroID] = None) -> bool:
        if self.recursive:
            if 0 > self.max_readers_in_progress:
                return True
            else:
                if coro_id in self.readers_in_progress_dict:
                    return True
                else:
                    return self.readers_in_progress < self.max_readers_in_progress
        else:
            if 0 > self.max_readers_in_progress:
                return True
            else:
                return self.readers_in_progress < self.max_readers_in_progress
    
    def increase_readers_in_progress(self, coro_id: Optional[CoroID] = None):
        if self.recursive:
            if coro_id not in self.readers_in_progress_dict:
                self.readers_in_progress_dict[coro_id] = 0
                self.readers_in_progress += 1
            
            self.readers_in_progress_dict[coro_id] += 1
        else:
            self.readers_in_progress += 1
    
    def decrease_readers_in_progress(self, coro_id: Optional[CoroID] = None):
        if self.recursive:
            self.readers_in_progress_dict[coro_id] -= 1
            if 0 >= self.readers_in_progress_dict[coro_id]:
                del self.readers_in_progress_dict[coro_id]
                self.readers_in_progress -= 1
        else:
            self.readers_in_progress -= 1

    def try_write_lock(self, coro_id: Optional[CoroID] = None, apply: bool = True) -> bool:
        need_to_try_later = False
        if self.readers_in_progress or self.readers_pending:
            if (not self.readers_in_progress) and self.readers_pending and (RWOperation.read == self.last_operation) and self.check_writers_in_progress_boundaries(coro_id):
                if apply:
                    self.increase_writers_in_progress(coro_id)
                    self.last_operation = RWOperation.write
            else:
                need_to_try_later = True
        else:
            if self.check_writers_in_progress_boundaries(coro_id):
                if apply:
                    self.increase_writers_in_progress(coro_id)
                    self.last_operation = RWOperation.write
            else:
                need_to_try_later = True
        
        return need_to_try_later

    def try_read_lock(self, coro_id: Optional[CoroID] = None, apply: bool = True) -> bool:
        need_to_try_later = False
        if self.writers_in_progress or self.writers_pending:
            if (not self.writers_in_progress) and self.writers_pending and (RWOperation.write == self.last_operation) and self.check_readers_in_progress_boundaries(coro_id):
                if apply:
                    self.increase_readers_in_progress(coro_id)
                    self.last_operation = RWOperation.read
            else:
                need_to_try_later = True
        else:
            if self.check_readers_in_progress_boundaries(coro_id):
                if apply:
                    self.increase_readers_in_progress(coro_id)
                    self.last_operation = RWOperation.read
            else:
                need_to_try_later = True
        
        return need_to_try_later
    
    def test_remove(self) -> bool:
        need_to_try_later = self.waiting_coroutines
        return need_to_try_later


class RWLockerContextManagerBase:
    def __init__(self, core: RWLockerEntity) -> None:
        self.core: RWLockerEntity = core
        self.current_context_operation: Optional[RWOperation] = None
    
    def lockable(self, operation: Optional[RWOperation] = None) -> bool:
        if operation is None:
            operation = RWOperation.read
        
        if RWOperation.write == operation:
            need_service_assistance = self.core.try_write_lock(self._interface.coro_id, False)
        else:
            need_service_assistance = self.core.try_read_lock(self._interface.coro_id, False)
        
        return not need_service_assistance
    
    def change_max_boundaries(self, max_writers_in_progress: int, max_readers_in_progress: int):
        self.core.max_writers_in_progress = max_writers_in_progress
        self.core.max_readers_in_progress = max_readers_in_progress
        
    def __call__(self, operation: Optional[RWOperation] = None):
        if operation is None:
            operation = RWOperation.read
        
        self.current_context_operation = operation
        return self
    

class RWLockerContextManager(RWLockerContextManagerBase):
    def __init__(self, core: RWLockerEntity, interface: Interface):
        super().__init__(core)
        self._interface = interface
    
    def __enter__(self):
        if self.current_context_operation is None:
            self.current_context_operation = RWOperation.read
        
        if RWOperation.write == self.current_context_operation:
            need_service_assistance = self.core.try_write_lock(self._interface.coro_id)
            if need_service_assistance:
                self.core.writers_pending += 1
                self._interface(self.core.service, RWLockerRequest().wait_for_write(self.core.entity_id))
        else:
            need_service_assistance = self.core.try_read_lock(self._interface.coro_id)
            if need_service_assistance:
                self.core.readers_pending += 1
                self._interface(self.core.service, RWLockerRequest().wait_for_read(self.core.entity_id))
        
        return self
    
    def __exit__(self, type, value: Exception, traceback):
        if RWOperation.write == self.current_context_operation:
            self.core.decrease_writers_in_progress(self._interface)
        else:
            self.core.decrease_readers_in_progress(self._interface)
        
        self.current_context_operation = None

    async def __aenter__(self):
        if self.current_context_operation is None:
            self.current_context_operation = RWOperation.read
        
        if RWOperation.write == self.current_context_operation:
            need_service_assistance = self.core.try_write_lock(self._interface.coro_id)
            if need_service_assistance:
                self.core.writers_pending += 1
                await self._interface(self.core.service, RWLockerRequest().wait_for_write(self.core.entity_id))
        else:
            need_service_assistance = self.core.try_read_lock(self._interface.coro_id)
            if need_service_assistance:
                self.core.readers_pending += 1
                await self._interface(self.core.service, RWLockerRequest().wait_for_read(self.core.entity_id))        
        
        return self

    async def __aexit__(self, type, value, traceback):
        if RWOperation.write == self.current_context_operation:
            self.core.decrease_writers_in_progress(self._interface)
        else:
            self.core.decrease_readers_in_progress(self._interface)
        
        self.current_context_operation = None


class FakeRWLockerContextManager(RWLockerContextManagerBase):
    def __init__(self, core: RWLockerEntity):
        super().__init__(core)
    
    def __enter__(self):
        if self.current_context_operation is None:
            self.current_context_operation = RWOperation.read
        
        if RWOperation.write == self.current_context_operation:
            self.core.increase_writers_in_progress()
            self.core.last_operation = RWOperation.write
        else:
            self.core.increase_readers_in_progress()
            self.core.last_operation = RWOperation.read
        
        return self
    
    def __exit__(self, type, value: Exception, traceback):
        if RWOperation.write == self.current_context_operation:
            self.core.decrease_writers_in_progress()
        else:
            self.core.decrease_readers_in_progress()
        
        self.current_context_operation = None

    async def __aenter__(self):
        if self.current_context_operation is None:
            self.current_context_operation = RWOperation.read
        
        if RWOperation.write == self.current_context_operation:
            self.core.increase_writers_in_progress()
            self.core.last_operation = RWOperation.write
        else:
            self.core.increase_readers_in_progress()
            self.core.last_operation = RWOperation.read
        
        return self

    async def __aexit__(self, type, value, traceback):
        if RWOperation.write == self.current_context_operation:
            self.core.decrease_writers_in_progress()
        else:
            self.core.decrease_readers_in_progress()
        
        self.current_context_operation = None


class UnknownLockerEntity(Exception):
    pass


class RWLocker(Service, EntityStatsMixin):
    def __init__(self, loop: CoroScheduler):
        super(RWLocker, self).__init__(loop)

        # loop.add_global_on_coro_del_handler(self._on_coro_del_handler_global)  # Todo: switch to local coro del handler

        self._request_workers = {
            0: self._on_register,
            1: self._on_deregister,
            2: self._on_wait_for_write,
            3: self._on_wait_for_read,
        }
        
        self.locker_entities: Dict[Hashable, RWLockerEntity] = dict()
        self.entities_by_coroutine: Dict[CoroID, Set[Hashable]] = dict()
        
        self.remove_entity_requests: Dict[CoroID, Hashable] = dict()
        self.waiting_for_write_requests: Dict[CoroID, Hashable] = dict()
        self.waiting_for_read_requests: Dict[CoroID, Hashable] = dict()

    def get_entity_stats(self, stats_level: 'EntityStatsMixin.StatsLevel' = EntityStatsMixin.StatsLevel.debug) -> Tuple[str, Dict[str, Any]]:
        return type(self).__name__, {
            'locker entities num': len(self.locker_entities),
            'affected coroutines num': len(self.entities_by_coroutine),
            'waiting for write requests num': len(self.waiting_for_write_requests),
            'waiting_for_read_requests num': len(self.waiting_for_read_requests),
        }

    def single_task_registration_or_immediate_processing(self, request: Optional[RWLockerRequest]=None
                                                         ) -> ServiceProcessingResponse:
        if request is not None:
            return self.resolve_request(request)
        return True, None, None

    def full_processing_iteration(self):
        # entities_waiting_for_remove
        processed_coro_ids: Set[CoroID] = set()
        for coro_id, entity_id in self.remove_entity_requests.items():
            if entity_id not in self.locker_entities:
                self.register_response(coro_id, False, None)
                processed_coro_ids.add(coro_id)
                continue
            
            entity = self.locker_entities[entity_id]
            need_to_try_later = entity.test_remove()
            if need_to_try_later:
                continue
            else:
                del self.locker_entities[entity_id]
                processed_coro_ids.add(coro_id)
        
        for coro_id in processed_coro_ids:
            del self.remove_entity_requests[coro_id]
        
        # entities_waiting_for_write
        processed_coro_ids: Set[CoroID] = set()
        for coro_id, entity_id in self.waiting_for_write_requests.items():
            if entity_id not in self.locker_entities:
                self.register_response(coro_id, None, UnknownLockerEntity)
                processed_coro_ids.add(coro_id)
                continue
            
            entity = self.locker_entities[entity_id]
            need_to_try_later = entity.try_write_lock(coro_id)
            if need_to_try_later:
                continue
            else:
                entity.writers_pending -= 1
                if coro_id in entity.waiting_coroutines:
                    entity.waiting_coroutines.remove(coro_id)
                
                self.register_response(coro_id, None, None)
                processed_coro_ids.add(coro_id)
        
        for coro_id in processed_coro_ids:
            del self.waiting_for_write_requests[coro_id]
                    
        # entities_waiting_for_read
        processed_coro_ids: Set[CoroID] = set()
        for coro_id, entity_id in self.waiting_for_read_requests.items():
            if entity_id not in self.locker_entities:
                self.register_response(coro_id, None, UnknownLockerEntity)
                processed_coro_ids.add(coro_id)
                continue
            
            entity = self.locker_entities[entity_id]
            need_to_try_later = entity.try_read_lock(coro_id)
            if need_to_try_later:
                continue
            else:
                entity.readers_pending -= 1
                if coro_id in entity.waiting_coroutines:
                    entity.waiting_coroutines.remove(coro_id)
                
                self.register_response(coro_id, None, None)
                processed_coro_ids.add(coro_id)
        
        for coro_id in processed_coro_ids:
            del self.waiting_for_read_requests[coro_id]
        
        # general
        if not (self.remove_entity_requests or self.waiting_for_write_requests or self.waiting_for_read_requests):
            self.make_dead()

    def in_work(self) -> bool:
        result: bool = bool(self.remove_entity_requests) or bool(self.waiting_for_write_requests) or bool(self.waiting_for_read_requests)
        return self.thrifty_in_work(result)
    
    def get_locker_entity(self, entity_id: Hashable):
        return self.locker_entities.get(entity_id)

    def _on_register(self, entity_id: Hashable, max_writers_in_progress: int, max_readers_in_progress: int, recursive: bool = True) -> ServiceProcessingResponse:
        if entity_id not in self.locker_entities:
            self.locker_entities[entity_id] = RWLockerEntity(entity_id, max_writers_in_progress, max_readers_in_progress, recursive, type(self))
        entity: RWLockerEntity = self.locker_entities[entity_id]
        
        coro_id = self.current_caller_coro_info.coro.coro_id
        entity.related_coroutines.add(coro_id)
        if coro_id not in self.entities_by_coroutine:
            self.entities_by_coroutine[coro_id] = set()
        
        self.entities_by_coroutine[coro_id].add(entity_id)
        self.current_caller_coro_info.coro.add_on_coro_del_handler(self._on_coro_del_handler)
        context_manager: RWLockerContextManager = RWLockerContextManager(entity, self.current_caller_coro_info.coro.interface)
        return True, context_manager, None

    def _on_deregister(self, entity_id: Hashable, safe: bool = True) -> ServiceProcessingResponse:
        result = None
        if safe:
            self.remove_entity_requests[self.current_caller_coro_info.coro.coro_id] = entity_id
            self.current_caller_coro_info.coro.add_on_coro_del_handler(self._on_coro_del_handler)
            self.make_live()
            return False, None, None
        else:
            if entity_id in self.locker_entities:
                entity = self.locker_entities[entity_id]
                del self.locker_entities[entity_id]
                for related_coro_id in entity.related_coroutines:
                    coroutine_entities = self.entities_by_coroutine[related_coro_id]
                    if entity_id in coroutine_entities:
                        coroutine_entities.remove(entity_id)
                
                result = True
            else:
                result = False
            
            return True, result, None

    def _on_wait_for_write(self, entity_id: Hashable) -> ServiceProcessingResponse:
        if entity_id not in self.locker_entities:
            return True, None, UnknownLockerEntity()
        
        coro_id = self.current_caller_coro_info.coro.coro_id
        self.waiting_for_write_requests[coro_id] = entity_id
        self.current_caller_coro_info.coro.add_on_coro_del_handler(self._on_coro_del_handler)
        entity = self.locker_entities[entity_id]
        entity.waiting_coroutines.add(coro_id)
        self.make_live()
        return False, None, None

    def _on_wait_for_read(self, entity_id: Hashable) -> ServiceProcessingResponse:
        if entity_id not in self.locker_entities:
            return True, None, UnknownLockerEntity()
        
        coro_id = self.current_caller_coro_info.coro.coro_id
        self.waiting_for_read_requests[coro_id] = entity_id
        self.current_caller_coro_info.coro.add_on_coro_del_handler(self._on_coro_del_handler)
        entity = self.locker_entities[entity_id]
        entity.waiting_coroutines.add(coro_id)
        self.make_live()
        return False, None, None

    def _on_coro_del_handler_global(self, coro: CoroWrapperBase) -> bool:
        coro_id = coro.coro_id
        if coro_id in self.entities_by_coroutine:
            entities = self.entities_by_coroutine[coro_id]
            del self.entities_by_coroutine[coro_id]
            for entity_id in entities:
                if entity_id in self.locker_entities:
                    entity = self.locker_entities[entity_id]
                    if coro_id in entity.related_coroutines:
                        entity.related_coroutines.remove(coro_id)
                    
                    if coro_id in entity.waiting_coroutines:
                        entity.waiting_coroutines.remove(coro_id)
        
        if coro_id in self.remove_entity_requests:
            del self.remove_entity_requests[coro_id]
        
        if coro_id in self.waiting_for_write_requests:
            del self.waiting_for_write_requests[coro_id]
        
        if coro_id in self.waiting_for_read_requests:
            del self.waiting_for_read_requests[coro_id]

        return False

    def _on_coro_del_handler(self, coro: CoroWrapperBase) -> bool:
        return self._on_coro_del_handler_global(coro)


RWLockerRequest.default_service_type = RWLocker


def get_rw_lock(entity_id: Hashable, max_writers_in_progress: int, max_readers_in_progress: int, recursive: bool = True) -> Union[RWLockerContextManager, FakeRWLockerContextManager]:
    loop = CoroScheduler.current_loop()
    if loop is None:
        return FakeRWLockerContextManager(RWLockerEntity(entity_id, max_writers_in_progress, max_readers_in_progress, recursive, RWLocker))  # running not from inside the loop

    interface = loop.current_interface()
    if interface is None:
        return FakeRWLockerContextManager(RWLockerEntity(entity_id, max_writers_in_progress, max_readers_in_progress, recursive, RWLocker))  # running from Service

    locker_entity = interface._loop.get_service_instance(RWLocker).get_locker_entity(entity_id)
    if locker_entity is None:
        lock = interface(RWLocker, RWLockerRequest().register(entity_id, max_writers_in_progress, max_readers_in_progress, recursive))
    else:
        lock = RWLockerContextManager(locker_entity, interface)
    
    return lock


grwl = get_rw_lock


async def aget_rw_lock(entity_id: Hashable, max_writers_in_progress: int, max_readers_in_progress: int, recursive: bool = True) -> Union[RWLockerContextManager, FakeRWLockerContextManager]:
    loop = CoroScheduler.current_loop()
    if loop is None:
        return FakeRWLockerContextManager(RWLockerEntity(entity_id, max_writers_in_progress, max_readers_in_progress, recursive, RWLocker))  # running not from inside the loop

    interface = loop.current_interface()
    if interface is None:
        return FakeRWLockerContextManager(RWLockerEntity(entity_id, max_writers_in_progress, max_readers_in_progress, recursive, RWLocker))  # running from Service

    locker_entity = interface._loop.get_service_instance(RWLocker).get_locker_entity(entity_id)
    if locker_entity is None:
        lock = await interface(RWLocker, RWLockerRequest().register(entity_id, max_writers_in_progress, max_readers_in_progress, recursive))
    else:
        lock = RWLockerContextManager(locker_entity, interface)
    
    return lock


agrwl = aget_rw_lock
