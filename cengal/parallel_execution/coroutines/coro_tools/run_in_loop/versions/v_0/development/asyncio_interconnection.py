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


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""


__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.1.12"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
from cengal.parallel_execution.coroutines.coro_scheduler import Interface, CoroWrapperBase, CoroID
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.cpu_tick_count_per_second import CpuTickCountPerSecond
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro
from cengal.parallel_execution.coroutines.coro_standard_services.kill_coro import KillCoro
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import AsyncioLoop, AsyncioLoopRequest
from time import perf_counter
from typing import Tuple
import asyncio


async def amy_coro(i: Interface) -> float:
    try:
        await i(AsyncioLoop, AsyncioLoopRequest().ensure_loop(interrupt_when_no_requests=True))
        await i(AsyncioLoop, AsyncioLoopRequest().turn_on_loops_intercommunication())
        print('Before AsyncIO...')
        start_time = perf_counter()
        
        await asyncio.sleep(0)
        await asyncio.sleep(1)
        async def ac(ti):
            await asyncio.sleep(ti)
        
        await ac(0)
        await ac(1)
        
        end_time = perf_counter()
        print(f'After AsyncIO. Delta time: {end_time - start_time}')
        return end_time
    finally:
        print('Ended')


print('AResult:', run_in_loop(amy_coro))
