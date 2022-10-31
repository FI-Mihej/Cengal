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


__all__ = ['FastAggregator', 'FastAggregatorClient']

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.introspection.inspect import get_exception
from typing import Hashable, Tuple, Dict, List, Any, Optional


class FastAggregator(Service):
    def __init__(self, loop: CoroScheduler):
        super().__init__(loop)
        self.data: Dict[Hashable, List[Any]] = dict()
    
    def single_task_registration_or_immediate_processing(
            self, key: Hashable) -> Tuple[bool, None, None]:
        exception = None
        result = None
        try:
            result = self.data[key]
            del self.data[key]
        except:
            exception = get_exception()
        
        return True, result, exception
    
    def put_single(self, key: Hashable, data: Any):
        if key not in self.data:
            self.data[key] = list()
        
        self.data[key].append(data)
    
    def put_multiple(self, data: Dict[Hashable, List[Any]]):
        for key in data.keys():
            if key not in self.data:
                self.data[key] = list()
            
            self.data[key].extend(data[key])

    def full_processing_iteration(self):
        self.make_dead()

    def in_work(self) -> bool:
        return self.thrifty_in_work(False)


class FastAggregatorClient:
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
