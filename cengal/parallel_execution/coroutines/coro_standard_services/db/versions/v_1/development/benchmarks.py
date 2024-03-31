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
__version__ = "4.3.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import unittest
from cengal.unittest.behavior_stabilizer import UnittestTestCaseState, UnittestTestCaseWithState
from cengal.math.numbers import ae
from cengal.time_management.run_time import RT
from cengal.introspection.inspect import get_exception, pifrl

from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
import cengal.parallel_execution.coroutines.coro_scheduler
# cengal.parallel_execution.coroutines.coro_scheduler.CoroScheduler = cengal.parallel_execution.coroutines.coro_scheduler.CoroSchedulerAwaitable
from cengal.parallel_execution.coroutines.coro_scheduler import CoroScheduler, CoroSchedulerType, Interface, CoroWrapperBase, CoroID, GreenletExit, AnyWorker, current_interface
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.cpu_tick_count_per_second import CpuTickCountPerSecond
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro, PutCoroRequest
from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
from cengal.parallel_execution.coroutines.coro_standard_services.kill_coro import KillCoro
from cengal.parallel_execution.coroutines.coro_standard_services.throw_coro import ThrowCoro
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_loop import ShutdownLoop
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import AsyncioLoopRequest
from cengal.parallel_execution.coroutines.coro_standard_services.instance import InstanceRequest
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_on_keyboard_interrupt import ShutdownOnKeyboardInterrupt
from cengal.parallel_execution.coroutines.coro_standard_services.db.versions.v_1 import *
from cengal.parallel_execution.coroutines.coro_standard_services.db.versions.v_1.tests.test__db import *
from cengal.time_management.load_best_timer import perf_counter
from cengal.performance_test_lib import PrecisePerformanceTestTracer
from contextlib import contextmanager, asynccontextmanager
from time import perf_counter
from typing import Tuple, Optional, OrderedDict as OrderedDictType
from shutil import rmtree


async def main(i: Interface, test: AnyWorker, *test_args, **test_kwargs) -> None:
    await i(AsyncioLoopRequest().ensure_loop(interrupt_when_no_requests=True))
    await i(AsyncioLoopRequest().turn_on_loops_intercommunication())
    await i(ShutdownOnKeyboardInterrupt)
    await i(InstanceRequest().set('app_name_for_fs', 'benchmark__db'))
    testing_envs_and_dbs = [
        (None, None),
        (None, 'db_1'),
        ('env_1', None),
        ('env_1', 'db_1'),
    ]
    for env_id, db_id in testing_envs_and_dbs:
        print()
        print(f'env_id: {env_id}, db_id: {db_id}')
        db_request: DbRequest = DbRequest(env_id, db_id)
        await i(RunCoro, test, db_request, *test_args, **test_kwargs)


items_to_be_put = dict()
keys_to_be_put = list()
for i in range(1000):
    items_to_be_put[f'key_{i}'] = f'value_{i}'
    keys_to_be_put.append(f'key_{i}')


def put_get_cached():
        pifrl()
        async def coro(i: Interface, db_request: DbRequest) -> None:
            async with db(db_request) as db_service:
                # await i(db_request.put('key_1', 'value_1'))
                await i(db_request.put_items(items_to_be_put))
                tr = PrecisePerformanceTestTracer(1.0)
                while tr.iter():
                    # await i(db_request.put('key_1', 'value_1'))
                    await i(db_request.put_items(items_to_be_put))
                    # result = await i(db_request.get('key_1'))
                    result = await i(db_request.get_items(keys_to_be_put))
                    # await i(db_request.delete('key_1'))
                    # if result != 'value_1':
                    #     raise Exception('Result is wrong')

                with tr as fast_iter:
                    for _ in fast_iter:
                        # await i(db_request.put('key_1', 'value_1'))
                        await i(db_request.put_items(items_to_be_put))
                        # result = await i(db_request.get('key_1'))
                        result = await i(db_request.get_items(keys_to_be_put))
                        # await i(db_request.delete('key_1'))
                        # if result != 'value_1':
                        #     raise Exception('Result is wrong')

                print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))

        with RT() as rt:
            run_in_loop(main, coro)
        
        print(f'Run time: {rt.rt}')


def put_get():
        pifrl()
        async def coro(i: Interface, db_request: DbRequest) -> None:
            async with db(db_request) as db_service:
                max_data_cache_size: int = db_service.max_data_cache_size
                db_service.max_data_cache_size = 0
                try:
                    # await i(db_request.put('key_1', 'value_1'))
                    await i(db_request.put_items(items_to_be_put))
                    tr = PrecisePerformanceTestTracer(1.0)
                    while tr.iter():
                        # await i(db_request.put('key_1', 'value_1'))
                        await i(db_request.put_items(items_to_be_put))
                        # result = await i(db_request.get('key_1'))
                        result = await i(db_request.get_items(keys_to_be_put))
                        # await i(db_request.delete('key_1'))
                        # if result != 'value_1':
                        #     raise Exception('Result is wrong')

                    with tr as fast_iter:
                        for _ in fast_iter:
                            # await i(db_request.put('key_1', 'value_1'))
                            await i(db_request.put_items(items_to_be_put))
                            # result = await i(db_request.get('key_1'))
                            result = await i(db_request.get_items(keys_to_be_put))
                            # await i(db_request.delete('key_1'))
                            # if result != 'value_1':
                            #     raise Exception('Result is wrong')

                    print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))
                finally:
                    db_service.max_data_cache_size = max_data_cache_size

        with RT() as rt:
            run_in_loop(main, coro)
        
        print(f'Run time: {rt.rt}')


def benchmarks():
    put_get_cached()
    put_get()


if '__main__' == __name__:
    benchmarks()
