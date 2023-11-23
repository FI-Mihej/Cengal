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


__all__ = ['FastAggregatorRequest', 'FastAggregatorWaitFor', 'FastAggregatorPutSingle', 'FastAggregatorPutMultiple', 'FastAggregator', 'FastAggregatorWriter', 'FastAggregatorClient']


from collections import deque

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.introspection.inspect import get_exception
from typing import Hashable, Tuple, Dict, List, Any, Optional, Set, Deque


class FastAggregatorWaitFor(TypedServiceRequest[Any]):
    def __call__(self, key: Hashable, queued: bool = True) -> 'FastAggregatorWaitFor':
        """Will block coroutine untill result is ready

        Args:
            key (Hashable): _description_

        Returns:
            ServiceRequest: _description_
        """        
        return self._save(self.default__request__type__, key, queued)


class FastAggregatorPutSingle(TypedServiceRequest[None]):
    default__request__type__ = 1

    def __call__(self, key: Hashable, data: Any) -> 'FastAggregatorPutSingle':
        return self._save(self.default__request__type__, key, data)


class FastAggregatorPutMultiple(TypedServiceRequest[None]):
    default__request__type__ = 2
    
    def __call__(self, data: Dict[Hashable, List[Any]]) -> 'FastAggregatorPutMultiple':
        return self._save(self.default__request__type__, data)


class FastAggregatorRequest(ServiceRequest):
    def wait(self, key: Hashable, queued: bool = True) -> FastAggregatorWaitFor:
        """Will block coroutine untill result is ready

        Args:
            key (Hashable): _description_
            queued (bool, optional): When True - works like loadbalansers works. Otherwise gets same link to data as a first requester in a queue. Defaults to True.

        Returns:
            Any: _description_
        """        
        return FastAggregatorWaitFor[None]()(key, queued)

    def put_single(self, key: Hashable, data: Any) -> FastAggregatorPutSingle:
        return FastAggregatorPutSingle[None]()(key, data)

    def put_multiple(self, data: Dict[Hashable, List[Any]]) -> FastAggregatorPutMultiple:
        return FastAggregatorPutMultiple[None]()(data)


class FastAggregator(DualImmediateProcessingServiceMixin, TypedService[Any]):
    def __init__(self, loop: CoroScheduler):
        super().__init__(loop)
        self.data: Dict[Hashable, List[Any]] = dict()
        self.requester_by_key: Dict[Hashable, Deque[Set[CoroID]]] = dict()
        self._request_workers = {
            0: self._on_wait,
            1: self._on_put_single,
            2: self._on_put_multiple,
        }

    def single_task_registration_or_immediate_processing_single(
            self, key: Hashable) -> Tuple[bool, None, None]:
        exception = None
        result = None
        try:
            result = self.data[key]
            del self.data[key]
        except:
            exception = get_exception()
        
        return True, result, exception
    
    def _on_wait(self, key: Hashable, queued: bool = True) -> Tuple[bool, None, None]:
        if key not in self.requester_by_key:
            self.requester_by_key[key] = deque()
        
        if (not queued) and (self.requester_by_key[key]):
            self.requester_by_key[key][0].add(self.current_caller_coro_info.coro_id)
        else:
            self.requester_by_key[key].append({self.current_caller_coro_info.coro_id})

        self.make_live()
        return False, None, None
    
    def _on_put_single(self, key: Hashable, data: Any) -> Tuple[bool, None, None]:
        self.put_single(key, data)
        return True, None, None
    
    def _on_put_multiple(self, data: Dict[Hashable, List[Any]]) -> Tuple[bool, None, None]:
        self.put_multiple(data)
        return True, None, None
    
    def put_single(self, key: Hashable, data: Any):
        if key not in self.data:
            self.data[key] = list()

        if (key in self.requester_by_key) and self.requester_by_key[key]:
            self.make_live()

        self.data[key].append(data)
    
    def put_multiple(self, data: Dict[Hashable, List[Any]]):
        need_to_make_live = False
        
        for key in data.keys():
            if key not in self.data:
                self.data[key] = list()

            if (key in self.requester_by_key) and self.requester_by_key[key]:
                need_to_make_live = True
            
            self.data[key].extend(data[key])
        
        if need_to_make_live:
            self.make_live()

    def full_processing_iteration(self):
        requester_by_key_bak = self.requester_by_key
        possible_keys = set(requester_by_key_bak.keys()) & set(self.data.keys())
        for key in possible_keys:
            key_requesters_coro_ids_bak = requester_by_key_bak[key]
            if key_requesters_coro_ids_bak:
                first_requesters_coro_ids: Set[CoroID] = key_requesters_coro_ids_bak.popleft()
                data = self.data[key]
                for first_requester_coro_id in first_requesters_coro_ids:
                    self.register_response(first_requester_coro_id, data, None)
                
                del self.data[key]
            
            if not key_requesters_coro_ids_bak:
                del requester_by_key_bak[key]
        
        self.make_dead()

    def in_work(self) -> bool:
        return self.thrifty_in_work(bool(self.requester_by_key))


FastAggregatorWaitFor.default_service_type = FastAggregator
FastAggregatorPutSingle.default_service_type = FastAggregator
FastAggregatorPutMultiple.default_service_type = FastAggregator


class FastAggregatorWriter:
    def __init__(self) -> None:
        self.server:Optional[FastAggregator] = None
        self.data_buffer: Dict[Hashable, List[Any]] = dict()
    
    def try_find_server(self):
        loop = CoroScheduler.current_loop()
        if loop is not None:
            self.server = loop.get_service_instance(FastAggregator)
    
    def __call__(self, key: Hashable, data: Any) -> Any:
        if self.server is None:
            self.try_find_server()
        
        if self.server is None:
            if key not in self.data_buffer:
                self.data_buffer[key] = list()
            
            self.data_buffer[key].append(data)
        else:
            if self.data_buffer:
                self.server.put_multiple(self.data_buffer)
            
            self.server.put_single(key, data)


FastAggregatorClient = FastAggregatorWriter
