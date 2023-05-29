#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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


__all__ = ['prepare_loop', 'prepare_fast_loop']


from asyncio import AbstractEventLoop
from asyncio import Task as asyncio_Task
from asyncio import get_event_loop, get_running_loop

from cengal.code_flow_control.smart_values import ValueExistence
from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import (
    PutCoro, PutCoroRequest)
from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import \
    RunCoro
from cengal.parallel_execution.coroutines.coro_standard_services.wait_coro import (
    CoroutineNotFoundError, WaitCoro, WaitCoroRequest)
from cengal.parallel_execution.coroutines.coro_standard_services.instance import Instance, InstanceRequest
from cengal.parallel_execution.coroutines.coro_tools.await_coro import (
    RunSchedulerInAsyncioLoop, await_coro_fast)
from cengal.time_management.sleep_tools import get_usable_min_sleep_interval
from typing import Tuple, Any, Union, Optional

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.2.5"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


class LoopWasEndedBeforeSetupWasPrepared(Exception):
    pass


def prepare_loop(setup_coro_worker: Optional[AnyWorker], *args, **kwargs) -> Tuple[CoroScheduler, ValueExistence[Any]]:
    cs = CoroScheduler()
    set_primary_coro_scheduler(cs)
    cs.turn_on_embedded_mode(True)
    cs.set_coro_time_measurement(True)
    cs.set_coro_history_gathering(True)
    cs.set_loop_iteration_time_measurement(True)
    cs.set_global_on_start_handlers(True)
    cs.suppress_coro_exceptions = True
    cs.suppress_warnings_about_responses_to_not_existant_coroutines = True
    cs.use_internal_sleep = True

    async def initial_setup(i: Interface):
        await i(PutCoro, PutCoroRequest().turn_on_tree_monitoring(True))

    initial_setup_coro: CoroWrapperBase = cs.put_coro(initial_setup)

    async def main(i: Interface, initial_setup_coro: CoroWrapperBase, setup_coro_worker: Optional[AnyWorker], *args, **kwargs):
        try:
            await i(WaitCoro, WaitCoroRequest().single(initial_setup_coro.coro_id))
        except CoroutineNotFoundError:
            pass

        if setup_coro_worker is None:
            return None
        
        return await i(RunCoro, setup_coro_worker, *args, **kwargs)

    coro: CoroWrapperBase = cs.put_coro(main, initial_setup_coro, setup_coro_worker, *args, **kwargs)
    result: ValueExistence = ValueExistence()

    def gather(coro: CoroWrapperBase) -> bool:
        result.value = (coro.last_result, coro.exception)
        return True

    coro.add_on_coro_del_handler(gather)
    in_work: bool = True
    while in_work and (not result):
        in_work = cs.iteration()
    
    if not result:
        raise LoopWasEndedBeforeSetupWasPrepared
    
    result, exception = result.value
    if exception is not None:
        raise exception

    return cs, result


def prepare_fast_loop(setup_coro_worker: Optional[AnyWorker], *args, **kwargs) -> Tuple[CoroScheduler, ValueExistence[Any]]:
    """30% faster than prepare_loop()

    Args:
        coro_worker (AnyWorker): _description_

    Raises:
        exception.value: _description_

    Returns:
        _type_: _description_
    """
    cs = CoroScheduler()
    set_primary_coro_scheduler(cs)
    cs.turn_on_embedded_mode(False)
    cs.set_coro_time_measurement(False)
    cs.set_coro_history_gathering(False)
    cs.set_loop_iteration_time_measurement(False)
    cs.set_global_on_start_handlers(False)
    cs.suppress_coro_exceptions = True
    cs.suppress_warnings_about_responses_to_not_existant_coroutines = True
    cs.use_internal_sleep = True

    async def initial_setup(i: Interface):
        await i(PutCoro, PutCoroRequest().turn_on_tree_monitoring(False))

    initial_setup_coro: CoroWrapperBase = cs.put_coro(initial_setup)

    async def main(i: Interface, initial_setup_coro: CoroWrapperBase, setup_coro_worker: Optional[AnyWorker], *args, **kwargs):
        try:
            await i(WaitCoro, WaitCoroRequest().single(initial_setup_coro.coro_id))
        except CoroutineNotFoundError:
            pass

        if setup_coro_worker is None:
            return None

        return await i(RunCoro, setup_coro_worker, *args, **kwargs)

    coro: CoroWrapperBase = cs.put_coro(main, initial_setup_coro, setup_coro_worker, *args, **kwargs)
    result: ValueExistence = ValueExistence()

    def gather(coro: CoroWrapperBase) -> bool:
        result.value = (coro.last_result, coro.exception)
        return True

    coro.add_on_coro_del_handler(gather)
    in_work: bool = True
    while in_work and (not result):
        in_work = cs.iteration()
    
    if not result:
        raise LoopWasEndedBeforeSetupWasPrepared
    
    result, exception = result.value
    if exception is not None:
        raise exception

    return cs, result
