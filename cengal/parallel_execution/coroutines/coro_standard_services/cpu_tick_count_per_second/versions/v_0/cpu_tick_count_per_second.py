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


__all__ = ['CpuTickCountPerSecond', 'cpu_clock_cycles']

from collections import deque
from time import perf_counter
from typing import Tuple

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.timer_func_runner import (
    TimerFuncRunner, add_timer_func_run_from_other_service)
from cengal.statistics.normal_distribution import count_99_95_68
from cengal.math.numbers import RationalNumber
from cengal.time_management.cpu_clock_cycles import cpu_clock_cycles


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


class CpuTickCountPerSecond(TypedService[Tuple[int, float, RationalNumber, RationalNumber, RationalNumber, RationalNumber, RationalNumber]]):
    def __init__(self, loop: CoroScheduler):
        super().__init__(loop)
        self.sliding_window_size: int = 100
        self.measurement_period: float = 0.1
        self.sliding_window = deque(maxlen=self.sliding_window_size)
        self.val_99, self.val_95, self.val_68, self.max_deviation, self.min_deviation = 0, 0, 0, 0, 0
        self.last_cpu_clock_cycles: int = cpu_clock_cycles()
        self.last_time: float = perf_counter()
        self.last_ticks_per_second = None
        self.measurement_required: bool = True

    def single_task_registration_or_immediate_processing(self, with_fresh_cpu_clock_cycles: bool = True) -> Tuple[bool, None, None]:
        if with_fresh_cpu_clock_cycles:
            cpu_clock_cycles_val = cpu_clock_cycles()
        else:
            cpu_clock_cycles_val = self.last_cpu_clock_cycles

        result = (cpu_clock_cycles_val, self.last_ticks_per_second, self.val_99,
                  self.val_95, self.val_68, self.max_deviation, self.min_deviation)
        return True, result, None

    def full_processing_iteration(self):
        cpu_clock_cycles_delta = cpu_clock_cycles() - self.last_cpu_clock_cycles
        time_delta = perf_counter() - self.last_time
        if time_delta >= self.measurement_period:
            last_ticks_per_second = None
            try:
                last_ticks_per_second = cpu_clock_cycles_delta / time_delta
            except ZeroDivisionError:
                pass

            if last_ticks_per_second is not None:
                self.last_ticks_per_second = last_ticks_per_second
                self.sliding_window.append(last_ticks_per_second)
                self.val_99, self.val_95, self.val_68, self.max_deviation, self.min_deviation = count_99_95_68(
                    self.sliding_window)

        self.last_cpu_clock_cycles = cpu_clock_cycles()
        self.last_time = perf_counter()
        self.measurement_required = False

        def timer_handler():
            self.measurement_required = True
            self.make_live()

        add_timer_func_run_from_other_service(self, False, self.measurement_period, timer_handler)
        self.make_dead()

    def in_work(self) -> bool:
        result: bool = self.measurement_required
        return self.thrifty_in_work(result)
    
    def in_forground_work(self) -> bool:
        return False
