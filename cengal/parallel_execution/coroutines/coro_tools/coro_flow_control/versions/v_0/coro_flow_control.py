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


__all__ = ['execution_time_limiter', 'aexecution_time_limiter', 'GracefulCoroDestroy', 'simple_graceful_coro_destroyer', 'asimple_graceful_coro_destroyer']


from typing import Optional, Type, Any, Hashable
from cengal.parallel_execution.coroutines.coro_scheduler import CoroScheduler, Interface, CoroID, ExplicitWorker, Worker, CoroWrapperBase, get_interface_for_an_explicit_loop
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro, put_coro_to, put_coro
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.simple_yield import Yield
from cengal.parallel_execution.coroutines.coro_standard_services.kill_coro import KillCoro
from cengal.parallel_execution.coroutines.coro_standard_services.throw_coro import ThrowCoro
from cengal.parallel_execution.coroutines.coro_standard_services.wait_coro import WaitCoro, WaitCoroRequest, CoroutineNotFoundError
from cengal.code_flow_control.smart_values import ValueExistence


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


def execution_time_limiter(i: Interface, coro_id: CoroID, time_limit: Optional[float] = None):
    def wait_for(i: Interface, coro_id: CoroID):
        try:
            i(WaitCoro, WaitCoroRequest().single(coro_id))
        except CoroutineNotFoundError:
            pass
    
    def time_limiter(i: Interface, coro_id: CoroID, time_limit: Optional[float] = None):
        if time_limit:
            i(Sleep, time_limit)
            i(KillCoro, coro_id)
    
    waiter_coro_id = i(PutCoro, wait_for, coro_id)
    time_limiter_coro_id = i(PutCoro, time_limiter, waiter_coro_id, time_limit)
    
    def wait_for_on_coro_del_handler(coro: CoroWrapperBase) -> bool:
        def killer(i: Interface, time_limiter_coro_id):
            i(KillCoro, time_limiter_coro_id)
        
        put_coro(killer, time_limiter_coro_id)
        return True
    
    cs: CoroScheduler = i._loop
    coro_wrapper_base, _, _ = cs.find_coro_by_id(waiter_coro_id)
    if coro_wrapper_base is not None:
        coro_wrapper_base: CoroWrapperBase = coro_wrapper_base
        coro_wrapper_base.add_on_coro_del_handler(wait_for_on_coro_del_handler)

    try:
        i(WaitCoro, WaitCoroRequest().single(waiter_coro_id))
    except CoroutineNotFoundError:
        pass


async def aexecution_time_limiter(i: Interface, coro_id: CoroID, time_limit: Optional[float] = None):
    async def wait_for(i: Interface, coro_id: CoroID):
        try:
            await i(WaitCoro, WaitCoroRequest().single(coro_id))
        except CoroutineNotFoundError:
            pass
    
    async def time_limiter(i: Interface, coro_id: CoroID, time_limit: Optional[float] = None):
        if time_limit:
            await i(Sleep, time_limit)
            await i(KillCoro, coro_id)
    
    waiter_coro_id = await i(PutCoro, wait_for, coro_id)
    time_limiter_coro_id = await i(PutCoro, time_limiter, waiter_coro_id, time_limit)
    
    def wait_for_on_coro_del_handler(coro: CoroWrapperBase) -> bool:
        async def killer(i: Interface, time_limiter_coro_id):
            await i(KillCoro, time_limiter_coro_id)
        
        put_coro(killer, time_limiter_coro_id)
        return True
    
    cs: CoroScheduler = i._loop
    coro_wrapper_base, _, _ = cs.find_coro_by_id(waiter_coro_id)
    if coro_wrapper_base is not None:
        coro_wrapper_base: CoroWrapperBase = coro_wrapper_base
        coro_wrapper_base.add_on_coro_del_handler(wait_for_on_coro_del_handler)

    try:
        await i(WaitCoro, WaitCoroRequest().single(waiter_coro_id))
    except CoroutineNotFoundError:
        pass


class GracefulCoroDestroy(Exception):
    pass


def simple_graceful_coro_destroyer(i: Interface, phase_time_limit: Optional[float], coro_id: CoroID, ex_type: Type[Exception] = None, ex_value: Exception = None, ex_traceback: Any = None, tree: bool = False):
    phase_time_limit = phase_time_limit or 0
    if (ex_type is not None) or (ex_value is not None):
        i(ThrowCoro, coro_id, ex_type, ex_value, ex_traceback, tree)
        i(Sleep, phase_time_limit)

    i(ThrowCoro, coro_id, GracefulCoroDestroy, tree=tree)
    i(Sleep, phase_time_limit)
    i(KillCoro, coro_id, tree)
    i(Yield)


async def asimple_graceful_coro_destroyer(i: Interface, phase_time_limit: Optional[float], coro_id: CoroID, ex_type: Type[Exception] = None, ex_value: Exception = None, ex_traceback: Any = None, tree: bool = False):
    phase_time_limit = phase_time_limit or 0
    if (ex_type is not None) or (ex_value is not None):
        await i(ThrowCoro, coro_id, ex_type, ex_value, ex_traceback, tree)
        await i(Sleep, phase_time_limit)

    await i(ThrowCoro, coro_id, GracefulCoroDestroy, tree=tree)
    await i(Sleep, phase_time_limit)
    await i(KillCoro, coro_id, tree)
    await i(Yield)


def graceful_coro_destroyer(i: Interface, phase_time_limit: Optional[float], coro_id: CoroID, ex_type: Type[Exception] = None, ex_value: Exception = None, ex_traceback: Any = None, tree: bool = False):
    raise NotImplementedError


async def agraceful_coro_destroyer(i: Interface, phase_time_limit: Optional[float], coro_id: CoroID, ex_type: Type[Exception] = None, ex_value: Exception = None, ex_traceback: Any = None, tree: bool = False):
    raise NotImplementedError
