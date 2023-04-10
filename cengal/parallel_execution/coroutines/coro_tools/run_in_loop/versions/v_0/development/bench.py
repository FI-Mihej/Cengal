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
__version__ = "3.1.9"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.code_flow_control.smart_values import ValueExistence
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
from cengal.parallel_execution.coroutines.coro_scheduler import Interface, CoroWrapperBase, CoroID
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.cpu_tick_count_per_second import CpuTickCountPerSecond
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro
from cengal.parallel_execution.coroutines.coro_standard_services.kill_coro import KillCoro
from cengal.parallel_execution.coroutines.coro_standard_services.timer_func_runner import TimerFuncRunner
from cengal.parallel_execution.coroutines.coro_standard_services.simple_yield import Yield
from cengal.parallel_execution.coroutines.coro_standard_services.some_printer import SomePrinter
from time import perf_counter
from hwcounter import Timer, count, count_end
from typing import Tuple, Union


# async def await_for_cpu_tick_count(i: Interface) -> Tuple:
#     rdtsc, last_ticks_per_second, val_99, val_95, val_68, max_deviation, min_deviation = await i(CpuTickCountPerSecond)
#     while (last_ticks_per_second is None) or (val_99 < 1) or (val_95 < 1) or (val_68 < 1):
#         rdtsc, last_ticks_per_second, val_99, val_95, val_68, max_deviation, min_deviation = await i(CpuTickCountPerSecond)
    
#     return rdtsc, last_ticks_per_second, val_99, val_95, val_68, max_deviation, min_deviation


# def wait_for_cpu_tick_count(i: Interface) -> Tuple:
#     rdtsc, last_ticks_per_second, val_99, val_95, val_68, max_deviation, min_deviation = i(CpuTickCountPerSecond)
#     while (last_ticks_per_second is None) or (val_99 < 1) or (val_95 < 1) or (val_68 < 1):
#         rdtsc, last_ticks_per_second, val_99, val_95, val_68, max_deviation, min_deviation = i(CpuTickCountPerSecond)
    
#     return rdtsc, last_ticks_per_second, val_99, val_95, val_68, max_deviation, min_deviation


async def amain(i: Interface, bench_time: Union[float, int]) -> float:
    counter: int = 0

    # === With Sleep service active: ==========================================================
    need_to_stop: ValueExistence = ValueExistence(True, False)
    def counter_stopper(need_to_stop: ValueExistence):
        need_to_stop.value = True
    
    # print(await await_for_cpu_tick_count(i))
    await i(TimerFuncRunner, bench_time, counter_stopper, need_to_stop)
    start_time = perf_counter()
    with Timer() as t:
        while not need_to_stop.value:
            await i(Yield)
            counter += 1
    
    end_time = perf_counter()
    delta_time = end_time - start_time
    iterations_per_second = None
    if 0 != delta_time:
        iterations_per_second = counter / delta_time
    
    # print(await i(CpuTickCountPerSecond))
    print(f'Delta_time: {delta_time}; Iterations Per Second: {iterations_per_second}')
    print(f'CPU cycles per request to the service: {int(round(t.cycles / counter))}')

    # === Without Sleep service active (64% faster than with (see above): ==========================================================
    print('====')
    original_counter = counter
    start_time = perf_counter()
    with Timer() as t:
        while counter:
            await i(Yield)
            counter -= 1
    
    end_time = perf_counter()
    delta_time = end_time - start_time
    iterations_per_second = None
    if 0 != delta_time:
        iterations_per_second = original_counter / delta_time
    
    print(f'2) Delta_time: {delta_time}; Iterations Per Second: {iterations_per_second}')
    print(f'2) CPU cycles per request to the service: {int(round(t.cycles / original_counter))}')

    return iterations_per_second


def main(i: Interface, bench_time: Union[float, int]) -> float:
    counter: int = 0

    # === With Sleep service active: ==========================================================
    need_to_stop: ValueExistence = ValueExistence(True, False)
    def counter_stopper(need_to_stop: ValueExistence):
        need_to_stop.value = True
    
    # print(wait_for_cpu_tick_count(i))
    i(TimerFuncRunner, bench_time, counter_stopper, need_to_stop)
    start_time = perf_counter()
    with Timer() as t:
        while not need_to_stop.value:
            i(Yield)
            counter += 1
    
    end_time = perf_counter()
    delta_time = end_time - start_time
    iterations_per_second = None
    if 0 != delta_time:
        iterations_per_second = counter / delta_time
    
    # print(i(CpuTickCountPerSecond))
    print(f'1) Delta_time: {delta_time}; Iterations Per Second: {iterations_per_second}')
    print(f'1) CPU cycles per request to the service: {int(round(t.cycles / counter))}')

    # === Without Sleep service active (64% faster than with (see above): ==========================================================
    print('====')
    original_counter = counter
    start_time = perf_counter()
    with Timer() as t:
        while counter:
            i(Yield)
            counter -= 1
    
    end_time = perf_counter()
    delta_time = end_time - start_time
    iterations_per_second = None
    if 0 != delta_time:
        iterations_per_second = original_counter / delta_time
    
    print(f'2) Delta_time: {delta_time}; Iterations Per Second: {iterations_per_second}')
    print(f'2) CPU cycles per request to the service: {int(round(t.cycles / original_counter))}')

    return iterations_per_second


# TODO: make idle manager (single per thread) which creates an additional single thread which will sleep until closest shot time (using info about OS sleep granularity) and then assigns True to an appropriate flag (and removes this flag from the queue). CoroScheduler will take into account set of an idle services only when see that flag changed to True.


if '__main__' == __name__:
    print('AResult:', run_in_loop(main, 10), 'requests to service per second')
    print('\n=============================\n')
    print('Result:', run_in_loop(main, 10), 'requests to service per second')
