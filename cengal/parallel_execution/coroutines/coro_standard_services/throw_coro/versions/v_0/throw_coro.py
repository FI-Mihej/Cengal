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


__all__ = ['ThrowCoro', 'throw_coro_on', 'try_throw_coro_on', 'athrow_coro_on', 'atry_throw_coro_on', 'throw_coro', 'try_throw_coro', 'athrow_coro', 'atry_throw_coro']


from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services_internal_lib.service_with_a_direct_request import *
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro
from cengal.code_flow_control.smart_values import ValueExistence
from cengal.introspection.inspect import get_exception, get_exception_tripple
from typing import Any, Optional, Tuple, Dict, Set, Union, Type, List


class ThrowCoro(TypedService[bool], ServiceWithADirectRequestMixin):
    def __init__(self, loop: CoroScheduler):
        super(ThrowCoro, self).__init__(loop)
        self.direct_requests: List[Tuple] = list()
    
    def single_task_registration_or_immediate_processing(
            self, coro_id: CoroID, ex_type: Type[Exception], ex_value: Exception = None, ex_traceback: Any = None, tree: bool = False) -> Tuple[bool, bool, Optional[BaseException]]:
        exception = None
        result = None
        try:
            if tree:
                put_coro: PutCoro = self._loop.get_service_instance(PutCoro)
                children: Set[CoroID] = put_coro.get_set_of_all_children(coro_id)
            
            result = self._loop.throw_coro_by_id(coro_id, ex_type, ex_value, ex_traceback)
            if tree:
                for child_coro_id in children:
                    self._loop.throw_coro_by_id(child_coro_id, ex_type, ex_value, ex_traceback)
        except:
            exception = get_exception()
        
        return True, result, exception

    def full_processing_iteration(self):
        direct_requests_buff = self.direct_requests
        self.direct_requests = type(direct_requests_buff)()
        put_coro: PutCoro = self._loop.get_service_instance(PutCoro)
        for coro_id, ex_type, ex_value, ex_traceback, tree in direct_requests_buff:
            try:
                if tree:
                    children: Set[CoroID] = put_coro.get_set_of_all_children(coro_id)
                
                self._loop.throw_coro_by_id(coro_id, ex_type, ex_value, ex_traceback)
                if tree:
                    for child_coro_id in children:
                        self._loop.throw_coro_by_id(child_coro_id, ex_type, ex_value, ex_traceback)
            except:
                ex_type, exception, tracback = get_exception_tripple()
                if __debug__: dlog(ex_type, exception, tracback)
                raise

        self.make_dead()
    
    def _add_direct_request(self, coro_id: CoroID, ex_type: Type[Exception], ex_value: Exception = None, ex_traceback: Any = None, tree: bool = False) -> ValueExistence[None]:
        self.direct_requests.append((coro_id, ex_type, ex_value, ex_traceback, tree))
        self.make_live()
        return ValueExistence()

    def in_work(self) -> bool:
        result: bool = bool(self.direct_requests)
        return self.thrifty_in_work(result)


def throw_coro_on(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], coro_id: CoroID, ex_type: Type[Exception], ex_value: Exception = None, ex_traceback: Any = None, tree: bool = False) -> ValueExistence[bool]:
    return make_request_to_service_with_context(context, ThrowCoro, coro_id, ex_type, ex_value, ex_traceback, tree)


def try_throw_coro_on(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], coro_id: CoroID, ex_type: Type[Exception], ex_value: Exception = None, ex_traceback: Any = None, tree: bool = False) -> ValueExistence[Optional[bool]]:
    return try_make_request_to_service_with_context(context, ThrowCoro, coro_id, ex_type, ex_value, ex_traceback, tree)


async def athrow_coro_on(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], coro_id: CoroID, ex_type: Type[Exception], ex_value: Exception = None, ex_traceback: Any = None, tree: bool = False) -> ValueExistence[bool]:
    return await amake_request_to_service_with_context(context, ThrowCoro, coro_id, ex_type, ex_value, ex_traceback, tree)


async def atry_throw_coro_on(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], coro_id: CoroID, ex_type: Type[Exception], ex_value: Exception = None, ex_traceback: Any = None, tree: bool = False) -> ValueExistence[Optional[bool]]:
    return await atry_make_request_to_service_with_context(context, ThrowCoro, coro_id, ex_type, ex_value, ex_traceback, tree)


def throw_coro(coro_id: CoroID, ex_type: Type[Exception], ex_value: Exception = None, ex_traceback: Any = None, tree: bool = False) -> ValueExistence[bool]:
    return make_request_to_service(ThrowCoro, coro_id, ex_type, ex_value, ex_traceback, tree)


def try_throw_coro(coro_id: CoroID, ex_type: Type[Exception], ex_value: Exception = None, ex_traceback: Any = None, tree: bool = False) -> ValueExistence[Optional[bool]]:
    return try_make_request_to_service(ThrowCoro, coro_id, ex_type, ex_value, ex_traceback, tree)


async def athrow_coro(coro_id: CoroID, ex_type: Type[Exception], ex_value: Exception = None, ex_traceback: Any = None, tree: bool = False) -> ValueExistence[bool]:
    return await amake_request_to_service(ThrowCoro, coro_id, ex_type, ex_value, ex_traceback, tree)


async def atry_throw_coro(coro_id: CoroID, ex_type: Type[Exception], ex_value: Exception = None, ex_traceback: Any = None, tree: bool = False) -> ValueExistence[Optional[bool]]:
    return await atry_make_request_to_service(ThrowCoro, coro_id, ex_type, ex_value, ex_traceback, tree)
