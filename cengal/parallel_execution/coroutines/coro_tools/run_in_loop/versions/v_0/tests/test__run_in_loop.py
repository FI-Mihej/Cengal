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

from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
from cengal.parallel_execution.coroutines.coro_scheduler import Interface, CoroWrapperBase, CoroID
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.cpu_tick_count_per_second import CpuTickCountPerSecond
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro
from cengal.parallel_execution.coroutines.coro_standard_services.kill_coro import KillCoro
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_loop import ShutdownLoop
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_on_keyboard_interrupt import ShutdownOnKeyboardInterrupt
from cengal.time_management.load_best_timer import perf_counter
from time import perf_counter
from typing import Tuple


async def sub_background_coro(i: Interface, period: float):
    while True:
        await i(Sleep, period)
        print(f'{perf_counter()}')


def background_coro(i: Interface, period: float):
    i(PutCoro, sub_background_coro, period / 2)
    while True:
        i(Sleep, period)
        print(f'{perf_counter()} || {i(CpuTickCountPerSecond)}')


async def await_for_cpu_tick_count(i: Interface) -> Tuple:
    cpu_clock_cycles, last_ticks_per_second, val_99, val_95, val_68, max_deviation, min_deviation = await i(CpuTickCountPerSecond)
    while (last_ticks_per_second is None) or (val_99 < 1) or (val_95 < 1) or (val_68 < 1):
        cpu_clock_cycles, last_ticks_per_second, val_99, val_95, val_68, max_deviation, min_deviation = await i(CpuTickCountPerSecond)
    
    return cpu_clock_cycles, last_ticks_per_second, val_99, val_95, val_68, max_deviation, min_deviation


async def amy_coro(i: Interface, a, b) -> int:
    try:
        await i(ShutdownOnKeyboardInterrupt)
        print('Started', perf_counter())
        print(await await_for_cpu_tick_count(i))
        coro_id: CoroID = await i(PutCoro, background_coro, 0.1)
        await i(Sleep, 0.5)
        await i(KillCoro, coro_id, tree=True)
        print(await i(CpuTickCountPerSecond))
        return a + b
    finally:
        print('Ended', perf_counter())


class TestCaseForRunInLoop(UnittestTestCaseWithState):
    @classmethod
    def setUpClass(cls):
        cls.state = UnittestTestCaseState()

    @classmethod
    def tearDownClass(cls):
        cls.state.unregister()
    
    def test_amain(self):
        with RT() as rt:
            result = self.state.register_outro(run_in_loop)(amy_coro, 2, 5)
        
        self.assertEqual(result, 7, 'Result is wrong')
        self.assertTrue(ae(rt.rt, 0.5, 0.5), f'Run time is wrong: {rt.rt}')


if __name__ == '__main__':
    unittest.main()
