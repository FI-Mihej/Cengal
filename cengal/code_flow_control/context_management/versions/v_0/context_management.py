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


__all__ = [
    'Combine', 
    'combine', 
    'Conditional', 
    'conditional', 
]


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.introspection.inspect import is_uni_context_manager, is_sync_context_manager, is_async_context_manager, is_context_manager

from typing import List, Any, Union, Callable


class Combine:
    __slots__ = ('sync_context_managers', 'async_context_managers')

    def __init__(self, *args):
        self.sync_context_managers: List[Any] = list()
        self.async_context_managers: List[Any] = list()
        for index, context_manager in enumerate(args):
            if is_uni_context_manager(context_manager):
                self.sync_context_managers.append(context_manager)
                self.async_context_managers.append(context_manager)
            elif is_sync_context_manager(context_manager):
                self.sync_context_managers.append(context_manager)
                self.async_context_managers.append(None)
            elif is_async_context_manager(context_manager):
                self.sync_context_managers.append(None)
                self.async_context_managers.append(context_manager)
            else:
                raise ValueError(f'Parameter #{index} is not a context manager. Its type: {type(context_manager)}')
    
    def __enter__(self):
        results: List[Any] = list()
        for sync_context_manager in self.sync_context_managers:
            if sync_context_manager is None:
                results.append(None)
            else:
                results.append(sync_context_manager.__enter__())
        
        return results
    
    def __exit__(self, exc_type, exc_value, traceback):
        suppress_exception: bool = False
        for sync_context_manager in self.sync_context_managers:
            if sync_context_manager is not None:
                if sync_context_manager.__exit__(exc_type, exc_value, traceback):
                    suppress_exception = True
        
        return suppress_exception
    
    async def __aenter__(self):
        results: List[Any] = list()
        for async_context_manager in self.async_context_managers:
            if async_context_manager is None:
                results.append(None)
            else:
                results.append(await async_context_manager.__aenter__())
        
        return results
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        suppress_exception: bool = False
        for async_context_manager in self.async_context_managers:
            if async_context_manager is not None:
                if await async_context_manager.__aexit__(exc_type, exc_value, traceback):
                    suppress_exception = True
        
        return suppress_exception


combine = Combine


class Conditional:
    __slots__ = ('context_manager', 'condition', 'condition_result', 'default', 'default_suppress_exception')

    def __init__(self, context_manager, condition: Union[bool, Callable] = True, default: Any = None, default_suppress_exception: bool = False):
        if not is_context_manager(context_manager):
            raise ValueError(f'Parameter is not a context manager. Its type: {type(context_manager)}')
        
        if not (isinstance(condition, bool) or callable(condition)):
            raise ValueError(f'Condition is neither bool nor callable. Its type: {type(condition)}')

        self.context_manager = context_manager
        self.condition: Union[bool, Callable] = condition
        self.condition_result: bool = None
        self.default: Any = default
        self.default_suppress_exception: bool = default_suppress_exception
    
    def __enter__(self):
        self.condition_result = condition = self.condition() if callable(self.condition) else self.condition
        if condition:
            return self.context_manager.__enter__()
        else:
            return self.default
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.condition_result:
            return self.context_manager.__exit__(exc_type, exc_value, traceback)
        else:
            return self.default_suppress_exception
    
    async def __aenter__(self):
        self.condition_result = condition = self.condition() if callable(self.condition) else self.condition
        if condition:
            return await self.context_manager.__aenter__()
        else:
            return self.default
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        if self.condition_result:
            return await self.context_manager.__aexit__(exc_type, exc_value, traceback)
        else:
            return self.default_suppress_exception


conditional = Conditional
