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


__all__ = ['run_in_loop', 'arun_in_loop', 'arun_in_fast_loop', 'run_in_fast_loop']


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


async def arun_in_loop(coro_worker: AnyWorker, *args, **kwargs):
    async_loop = get_running_loop()
    cs = CoroScheduler()
    set_primary_coro_scheduler(cs)
    cs.turn_on_embedded_mode(True)
    cs.set_coro_time_measurement(True)
    cs.set_coro_history_gathering(True)
    cs.set_loop_iteration_time_measurement(True)
    cs.set_global_on_start_handlers(True)
    cs.suppress_coro_exceptions = True
    cs.suppress_warnings_about_responses_to_not_existant_coroutines = True
    cs.use_internal_sleep = False

    async def initial_setup(i: Interface):
        await i(PutCoro, PutCoroRequest().turn_on_tree_monitoring(True))

    initial_setup_coro: CoroWrapperBase = cs.put_coro(initial_setup)

    async def main(i: Interface, rs: RunSchedulerInAsyncioLoop, initial_setup_coro: CoroWrapperBase, coro_worker: AnyWorker, *args, **kwargs):
        try:
            await i(WaitCoro, WaitCoroRequest().single(initial_setup_coro.coro_id))
        except CoroutineNotFoundError:
            pass

        await i(Instance, InstanceRequest().set(RunSchedulerInAsyncioLoop, rs))
        return await i(RunCoro, coro_worker, *args, **kwargs)

    rs = RunSchedulerInAsyncioLoop(cs, 0.020, async_loop, 6)
    rs.make_idle_when_possible = True
    rs.need_to_stop_when_possible = False
    rs.register()
    return await await_coro_fast(async_loop, cs, CoroType.auto, main, rs, initial_setup_coro, coro_worker, *args, **kwargs)


def run_in_loop(coro_worker: AnyWorker, *args, **kwargs):
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

    async def main(i: Interface, initial_setup_coro: CoroWrapperBase, coro_worker: AnyWorker, *args, **kwargs):
        try:
            await i(WaitCoro, WaitCoroRequest().single(initial_setup_coro.coro_id))
        except CoroutineNotFoundError:
            pass

        return await i(RunCoro, coro_worker, *args, **kwargs)

    coro: CoroWrapperBase = cs.put_coro(main, initial_setup_coro, coro_worker, *args, **kwargs)
    result: ValueExistence = ValueExistence()
    exception: ValueExistence = ValueExistence()

    def gather(coro: CoroWrapperBase) -> bool:
        result.value = coro.last_result
        exception.value = coro.exception
        return True

    coro.add_on_coro_del_handler(gather)
    cs.loop()
    if exception.value is not None:
        raise exception.value

    return result.value


async def arun_in_fast_loop(coro_worker: AnyWorker, *args, **kwargs):
    """30% faster than arun_in_loop()

    Args:
        coro_worker (AnyWorker): _description_

    Returns:
        _type_: _description_
    """
    async_loop = get_running_loop()
    cs = CoroScheduler()
    set_primary_coro_scheduler(cs)
    cs.turn_on_embedded_mode(False)
    cs.set_coro_time_measurement(False)
    cs.set_coro_history_gathering(False)
    cs.set_loop_iteration_time_measurement(False)
    cs.set_global_on_start_handlers(False)
    cs.suppress_coro_exceptions = True
    cs.suppress_warnings_about_responses_to_not_existant_coroutines = True
    cs.use_internal_sleep = False

    async def initial_setup(i: Interface):
        await i(PutCoro, PutCoroRequest().turn_on_tree_monitoring(False))

    initial_setup_coro: CoroWrapperBase = cs.put_coro(initial_setup)

    async def main(i: Interface, rs: RunSchedulerInAsyncioLoop, initial_setup_coro: CoroWrapperBase, coro_worker: AnyWorker, *args, **kwargs):
        try:
            await i(WaitCoro, WaitCoroRequest().single(initial_setup_coro.coro_id))
        except CoroutineNotFoundError:
            pass
        
        await i(Instance, InstanceRequest().set(RunSchedulerInAsyncioLoop, rs))
        return await i(RunCoro, coro_worker, *args, **kwargs)

    rs = RunSchedulerInAsyncioLoop(cs, 0.020, async_loop, 6)
    rs.make_idle_when_possible = True
    rs.need_to_stop_when_possible = False
    rs.register()
    return await await_coro_fast(async_loop, cs, CoroType.auto, main, rs, initial_setup_coro, coro_worker, *args, **kwargs)


def run_in_fast_loop(coro_worker: AnyWorker, *args, **kwargs):
    """30% faster than run_in_loop()

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

    async def main(i: Interface, initial_setup_coro: CoroWrapperBase, coro_worker: AnyWorker, *args, **kwargs):
        try:
            await i(WaitCoro, WaitCoroRequest().single(initial_setup_coro.coro_id))
        except CoroutineNotFoundError:
            pass

        return await i(RunCoro, coro_worker, *args, **kwargs)

    coro: CoroWrapperBase = cs.put_coro(main, initial_setup_coro, coro_worker, *args, **kwargs)
    result: ValueExistence = ValueExistence()
    exception: ValueExistence = ValueExistence()

    def gather(coro: CoroWrapperBase) -> bool:
        result.value = coro.last_result
        exception.value = coro.exception
        return True

    coro.add_on_coro_del_handler(gather)
    cs.loop()
    if exception.value is not None:
        raise exception.value

    return result.value
