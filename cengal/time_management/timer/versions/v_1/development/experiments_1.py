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
__version__ = "4.2.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.performance_test_lib import PrecisePerformanceTestTracer, MeasureTime
from cengal.time_management.timer.versions.v_0 import Timer, TimerRequest, TimerHandler
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
from cengal.time_management.load_best_timer import perf_counter
from cengal.code_flow_control.smart_values import ValueHolder
from copy import copy
from functools import partial
from typing import Dict, List


"""
<<< from cengal.time_management.timer.versions.v_1>>>:

>>> "Creation"
         It was used 2.9399991035461426e-05 seconds
         It is 34013.61581348201 iterations/seconds

>>> "Registration"
         It was used 3.017069897032343 seconds
         It is 0.33144740895251457 iterations/seconds

>>> "Execution - all tasks"
         It was used 3.0000364980078302 seconds
         It is 0.33332927804846657 iterations/seconds

Max call num: 1
========================================
>>> "Creation"
         It was used 0.0029741000034846365 seconds
         It is 336.2361718934599 iterations/seconds

>>> "Registration"
         It was used 2.4924262979766354 seconds
         It is 0.40121547458065465 iterations/seconds

>>> "Execution - wait for first"
         It was used 0.20197610004106537 seconds
         It is 4.951080844697378 iterations/seconds

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

<<< from cengal.time_management.timer.versions.v_0>>>:

>>> "Creation"
         It was used 8.500006515532732e-06 seconds
         It is 117646.9686432147 iterations/seconds

>>> "Registration"
         It was used 0.15310529700946063 seconds
         It is 6.531452663837022 iterations/seconds

>>> "Execution - all tasks"
         It was used 3.017543933005072 seconds
         It is 0.3313953407810481 iterations/seconds

Max call num: 1
========================================
>>> "Creation"
         It was used 0.0003347999881953001 seconds
         It is 2986.857930881008 iterations/seconds

>>> "Registration"
         It was used 0.1904736960423179 seconds
         It is 5.250068753733997 iterations/seconds

>>> "Execution - wait for first"
         It was used 0.09782769798766822 seconds
         It is 10.22205388218433 iterations/seconds
"""


class Handler:
    def __init__(self, desired_time: float):
        self.desired_time: float = desired_time
        self.creation_time: float = perf_counter()
        self.real_time: float = None
        self.call_num: int = 0
    
    def __call__(self):
        self.call_num += 1
        self.real_time = perf_counter() - self.creation_time

    def __bool__(self):
        return self.real_time is not None

    def __nonzero__(self):
        return self.__bool__()


tasks: List[Handler] = list()
for i in range(10000):
    tasks.append(Handler(2.0))
    tasks.append(Handler(0.5))
    tasks.append(Handler(0.01))
    tasks.append(Handler(0.1))
    tasks.append(Handler(3.0))


with MeasureTime('Creation'):
    timer = Timer()

with MeasureTime('Registration'):
    for task_handler in tasks:
        timer.register(task_handler, task_handler.desired_time)

with MeasureTime('Execution - all tasks'):
    while True:
        timer()
        if all(tasks):
            break


print('Max call num: {}'.format(max([task.call_num for task in tasks])))


print('========================================')


tasks = list()
for i in range(10000):
    tasks.append(Handler(2.0))
    tasks.append(Handler(0.5))
    tasks.append(Handler(0.01))
    tasks.append(Handler(0.1))
    tasks.append(Handler(3.0))


with MeasureTime('Creation'):
    timer = Timer()

with MeasureTime('Registration'):
    for task_handler in tasks:
        timer.register(task_handler, task_handler.desired_time)

with MeasureTime('Execution - wait for first'):
    while True:
        timer()
        if any(tasks):
            break
