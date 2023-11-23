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


import unittest
from cengal.unittest.behavior_stabilizer import UnittestTestCaseState, UnittestTestCaseWithState
from cengal.math.numbers import ae
from cengal.time_management.run_time import RT
from cengal.introspection.inspect import get_exception, pifrl

from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
from cengal.parallel_execution.coroutines.coro_scheduler import CoroScheduler, Interface, CoroWrapperBase, CoroID, GreenletExit, AnyWorker, current_interface
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
from cengal.time_management.load_best_timer import perf_counter
from contextlib import contextmanager, asynccontextmanager
from time import perf_counter
from typing import Tuple, Optional, OrderedDict as OrderedDictType
from shutil import rmtree


async def wait_for_db_env_unlocked(db_request: DbRequest):
    i: Interface = current_interface()
    loop: CoroScheduler = i._loop
    db_service: Db = loop.get_service_instance(Db)
    while db_request.env_id in db_service.write_locked:
        await i(Sleep, 0.01)


async def destroy_db_service(with_data: bool = False):
    i: Interface = current_interface()
    loop: CoroScheduler = i._loop
    db_service: Db = loop.get_service_instance(Db)
    dir_to_delete = db_service.root_path_to_db_environments_rel('')
    while db_service.write_locked:
        await i(Sleep, 0.01)
    
    loop.unregister_service(Db)
    if with_data:
        rmtree(dir_to_delete)


@asynccontextmanager
async def db(db_request: Optional[DbRequest] = None, destroy_with_data: bool = True):
    i: Interface = current_interface()
    db_service: Db = i._loop.get_service_instance(Db)
    await i(Db)
    while db_service.default_db_environment is None:
        await i(Sleep, 0.01)
    
    if db_request is not None:
        if db_request.env_id is not None:
            args, kwargs = default_env_path_and_params()
            await i(db_request.open_db_environment(db_request.env_id, *args, **kwargs))
        
        await i(db_request.open_databases({db_request.db_id}))

    try:
        yield db_service
    finally:
        db_service: Db = i._loop.get_service_instance(Db)
        while db_service.write_locked:
            await i(Sleep, 0.01)

        await i(db_request.sync())
        await destroy_db_service(destroy_with_data)


async def main(i: Interface, test: AnyWorker, *test_args, **test_kwargs) -> None:
    await i(AsyncioLoopRequest().ensure_loop(interrupt_when_no_requests=True))
    await i(AsyncioLoopRequest().turn_on_loops_intercommunication())
    await i(ShutdownOnKeyboardInterrupt)
    await i(InstanceRequest().set('app_name_for_fs', 'test__db'))
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


class TestCaseForDb(unittest.TestCase):
    # @unittest.skip('Skip')
    def test_00_register_service(self):
        pifrl()
        async def coro(i: Interface, db_request: DbRequest) -> None:
            loop: CoroScheduler = i._loop
            loop.register_service(Db)
            await i(Sleep, 0.01)
            db_service = loop.get_service_instance(Db)
            print(repr(db_service))

        with RT() as rt:
            run_in_loop(main, coro)
        
        print(f'Run time: {rt.rt}')

    # @unittest.skip('Skip')
    def test_01_init(self):
        pifrl()
        async def coro(i: Interface, db_request: DbRequest) -> None:
            await i(Db)
            await i(Sleep, 0.1)
            loop: CoroScheduler = i._loop
            db_service: Db = loop.get_service_instance(Db)
            await i(Db)
            while db_service.default_db_environment is None:
                await i(Sleep, 0.01)
            
            await destroy_db_service(True)

        with RT() as rt:
            run_in_loop(main, coro)
        
        print(f'Run time: {rt.rt}')

    # @unittest.skip('Skip')
    def test_02_put(self):
        pifrl()
        async def coro(i: Interface, db_request: DbRequest) -> None:
            async with db(db_request, False) as db_service:
                await i(db_request.put('key_1', 'value_1'))
                result = await i(db_request.get('key_1'))
                self.assertEqual(result, 'value_1', 'Result is wrong')
                await i(db_request.sync())
                await wait_for_db_env_unlocked(db_request)
                result = await i(db_request.get('key_1'))
                self.assertEqual(result, 'value_1', 'Result is wrong')

        with RT() as rt:
            run_in_loop(main, coro)
        
        print(f'Run time: {rt.rt}')

    # @unittest.skip('Skip')
    def test_03_get(self):
        pifrl()
        async def coro(i: Interface, db_request: DbRequest) -> None:
            result = None
            async with db(db_request, False) as db_service:
                result = await i(db_request.get('key_1'))
            
            print(f'Result: {result}')
            self.assertEqual(result, 'value_1', 'Result is wrong')
            return result

        with RT() as rt:
            run_in_loop(main, coro)
        
        print(f'Run time: {rt.rt}')

    # @unittest.skip('Skip')
    def test_04_cleanup(self):
        pifrl()
        async def coro(i: Interface, db_request: DbRequest) -> None:
            result = None
            async with db(db_request) as db_service:
                pass
            
            return result

        with RT() as rt:
            run_in_loop(main, coro)
        
        print(f'Run time: {rt.rt}')

    # @unittest.skip('Skip')
    def test_05_put_items(self):
        pifrl()
        async def coro(i: Interface, db_request: DbRequest) -> None:
            async with db(db_request, False) as db_service:
                await i(db_request.put_items({'key_1': 'value_1', 'key_2': 'value_2', 'key_3': 'value_3'}))
                result: OrderedDictType = await i(db_request.get_items(['key_1', 'key_2', 'key_3']))
                self.assertEqual([item[0] for item in result.values()], ['value_1', 'value_2', 'value_3'], 'Result is wrong')
                await i(db_request.sync())
                await wait_for_db_env_unlocked(db_request)
                result = await i(db_request.get_items(['key_1', 'key_2', 'key_3']))
                self.assertEqual([item[0] for item in result.values()], ['value_1', 'value_2', 'value_3'], 'Result is wrong')

        with RT() as rt:
            run_in_loop(main, coro)
        
        print(f'Run time: {rt.rt}')

    # @unittest.skip('Skip')
    def test_06_get_items(self):
        pifrl()
        async def coro(i: Interface, db_request: DbRequest) -> None:
            result__get_first = None
            result__get_last = None
            result__get_items = None
            result__get_n_items = None
            result__get_reverse_n_items = None
            result__get_items_range = None
            result__get_reverse_items_range = None
            result__get_all_items = None
            async with db(db_request, False) as db_service:
                result__get_first = await i(db_request.get_first())
                result__get_last = await i(db_request.get_last())
                result__get_items = await i(db_request.get_items(['key_1', 'key_2', 'key_3']))
                result__get_n_items = await i(db_request.get_n_items('key_1', 2))
                result__get_reverse_n_items = await i(db_request.get_reverse_n_items('key_3', 2))
                result__get_items_range = await i(db_request.get_items_range('key_1', 'key_3'))
                result__get_reverse_items_range = await i(db_request.get_reverse_items_range('key_3', 'key_1'))
                result__get_all_items = await i(db_request.get_all_items())
            
            self.assertEqual(result__get_first[1], 'value_1')
            self.assertEqual(result__get_last[1], 'value_3')
            self.assertEqual([item[0] for item in result__get_items.values()], ['value_1', 'value_2', 'value_3'], 'Result is wrong')
            self.assertEqual(result__get_n_items, [('key_1', 'value_1'), ('key_2', 'value_2')], 'Result is wrong')
            self.assertEqual(result__get_reverse_n_items, [('key_3', 'value_3'), ('key_2', 'value_2')], 'Result is wrong')
            self.assertEqual(result__get_items_range, [('key_1', 'value_1'), ('key_2', 'value_2'), ('key_3', 'value_3')], 'Result is wrong')
            self.assertEqual(result__get_reverse_items_range, [('key_3', 'value_3'), ('key_2', 'value_2'), ('key_1', 'value_1')], 'Result is wrong')
            self.assertEqual(result__get_all_items, [('key_1', 'value_1'), ('key_2', 'value_2'), ('key_3', 'value_3')], 'Result is wrong')

        with RT() as rt:
            run_in_loop(main, coro)
        
        print(f'Run time: {rt.rt}')

    # @unittest.skip('Skip')
    def test_07_delete_items(self):
        pifrl()
        async def coro(i: Interface, db_request: DbRequest) -> None:
            result__delete = None
            result__delete_kv = None
            result__delete_items = None
            result__delete_kv_items = None
            async with db(db_request, False) as db_service:
                await i(db_request.delete('key_1'))
                result__delete = await i(db_request.get_all_items())
                await i(db_request.delete_kv('key_2', 'value_2'))
                result__delete_kv = await i(db_request.get_all_items())
                await i(db_request.put_items({'key_4': 'value_4', 'key_5': 'value_5', 'key_6': 'value_6'}))
                result__put_items = await i(db_request.get_all_items())
                await i(db_request.delete_items({'key_3', 'key_4'}))
                result__delete_items = await i(db_request.get_all_items())
                await i(db_request.delete_kv_items({'key_5': 'value_5', 'key_6': 'value_6'}))
                result__delete_kv_items = await i(db_request.get_all_items())
            
            self.assertEqual(result__delete, [('key_2', 'value_2'), ('key_3', 'value_3')], 'Result is wrong')
            self.assertEqual(result__delete_kv, [('key_3', 'value_3')], 'Result is wrong')
            self.assertEqual(result__put_items, [('key_3', 'value_3'), ('key_4', 'value_4'), ('key_5', 'value_5'), ('key_6', 'value_6')], 'Result is wrong')
            self.assertEqual(result__delete_items, [('key_5', 'value_5'), ('key_6', 'value_6')], 'Result is wrong')
            self.assertEqual(result__delete_kv_items, list(), 'Result is wrong')

        with RT() as rt:
            run_in_loop(main, coro)
        
        print(f'Run time: {rt.rt}')

    # @unittest.skip('Skip')
    def test_08_cleanup(self):
        pifrl()
        async def coro(i: Interface, db_request: DbRequest) -> None:
            result = None
            async with db(db_request) as db_service:
                pass
            
            return result

        with RT() as rt:
            run_in_loop(main, coro)
        
        print(f'Run time: {rt.rt}')


if __name__ == '__main__':
    unittest.main()
