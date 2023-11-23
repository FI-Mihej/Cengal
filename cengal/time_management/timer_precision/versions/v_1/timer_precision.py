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

from typing import Tuple, Sequence
from collections import deque
from math import sqrt
from cengal.time_management.repeat_for_a_time import Tracer
from cengal.time_management.load_best_timer import perf_counter

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


def timer_precision(timer_functor=perf_counter, testing_time: float=1.0)->float:
    time_sum = 0
    tr = Tracer(testing_time)
    while tr.iter():
        first_time = zero_time = timer_functor()
        while zero_time == first_time:
            first_time = timer_functor()
        second_time = first_time
        while first_time == second_time:
            second_time = timer_functor()
        time_diff = second_time - first_time
        time_sum += time_diff

    average_time_diff = time_sum / tr.iterations_made
    return average_time_diff


def timer_precision_statistics(timer_functor=perf_counter, testing_time: float=1.0) -> Tuple[float, Sequence[float]]:
    time_readings = deque()
    time_sum = 0
    tr = Tracer(testing_time)
    while tr.iter():
        first_time = zero_time = timer_functor()
        while zero_time == first_time:
            first_time = timer_functor()
        second_time = first_time
        while first_time == second_time:
            second_time = timer_functor()
        time_diff = second_time - first_time
        time_readings.append(time_diff)
        time_sum += time_diff

    time_diff_mean = time_sum / tr.iterations_made
    return time_diff_mean, time_readings


def timer_precision_variance(timer_functor=perf_counter, testing_time: float=1.0) -> Tuple[float, float, float, float]:
    max_deviation = None
    min_deviation = None
    time_diff_mean, time_readings = timer_precision_statistics(timer_functor, testing_time)
    deviation_square_sum = 0
    for time_reading in time_readings:
        time_deviation = time_reading - time_diff_mean
        deviation_square_sum += time_deviation ** 2
        if max_deviation is None:
            max_deviation = time_deviation
        max_deviation = max(max_deviation, time_deviation)
        if min_deviation is None:
            min_deviation = time_deviation
        min_deviation = min(min_deviation, time_deviation)

    variance = deviation_square_sum / len(time_readings)
    return time_diff_mean, variance, max_deviation, min_deviation


def timer_precision_standard_deviation(timer_functor=perf_counter, testing_time: float=1.0
                                       ) -> Tuple[float, float, float, float]:
    time_diff_mean, time_variance, max_deviation, min_deviation = timer_precision_variance(timer_functor, testing_time)
    return time_diff_mean, sqrt(time_variance), max_deviation, min_deviation


def timer_precision_99_95_68(timer_functor=perf_counter, testing_time: float=1.0
                             ) -> Tuple[float, float, float, float, float]:
    # See: https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule
    mean, sd, max_deviation, min_deviation = timer_precision_standard_deviation(timer_functor, testing_time)
    val_68 = mean + sd
    val_95 = mean + 2 * sd
    val_99 = mean + 3 * sd
    return val_99, val_95, val_68, max_deviation, min_deviation
