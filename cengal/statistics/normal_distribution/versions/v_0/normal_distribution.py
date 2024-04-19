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


__all__ = ['count_99_95_68', 'guess_99_95_68', 'standard_deviation', 'variance', 'statistics', 'average', 'Number']


from typing import Tuple, Sequence, Iterable, Union, Callable
from collections import deque
from math import sqrt
from cengal.math.numbers import *


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.3.4"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


def statistics(iterable_readings: Iterable[Number]) -> Tuple[float, Sequence[Number]]:
    """Example
    
        ```
        diff_mean, readings = statistics(iterable_readings)
        ```

    Args:
        iterable_readings (Iterable[Number]): _description_

    Returns:
        Tuple[float, Sequence[Number]]: _description_
    """    
    readings = deque()
    data_sum = 0
    for reading in iterable_readings:
        readings.append(reading)
        data_sum += reading

    try:
        diff_mean = data_sum / len(readings)
    except ZeroDivisionError:
        diff_mean = 0
    
    return diff_mean, readings


def variance(diff_mean: float, readings: Sequence[Number]) -> Tuple[float, float, float, float]:
    """Example:

        ```
        diff_mean, readings = statistics(iterable_readings)
        diff_mean, variance, max_deviation, min_deviation = variance(diff_mean, readings)
        ```

    Alternative example:

        ```
        diff_mean, variance, max_deviation, min_deviation = variance(*statistics(iterable_readings))
        ```

    Args:
        diff_mean (float): _description_
        readings (Sequence[Number]): _description_

    Returns:
        Tuple[float, float, float, float]: _description_
    """    
    max_deviation = None
    min_deviation = None
    deviation_square_sum = 0
    for reading in readings:
        deviation = reading - diff_mean
        deviation_square_sum += deviation ** 2
        if max_deviation is None:
            max_deviation = deviation
        max_deviation = max(max_deviation, deviation)
        if min_deviation is None:
            min_deviation = deviation
        min_deviation = min(min_deviation, deviation)

    try:
        variance = deviation_square_sum / len(readings)
    except ZeroDivisionError:
        variance = 0

    return diff_mean, variance, max_deviation, min_deviation


def standard_deviation(diff_mean, variance, max_deviation, min_deviation) -> Tuple[float, float, float, float]:
    """Example:

        ```
        diff_mean, readings = statistics(iterable_readings)
        diff_mean, variance, max_deviation, min_deviation = variance(diff_mean, readings)
        diff_mean, sd, max_deviation, min_deviation = standard_deviation(diff_mean, variance, max_deviation, min_deviation)
        ```

    Alternative example:

        ```
        diff_mean, sd, max_deviation, min_deviation = standard_deviation(*variance(*statistics(iterable_readings)))
        ```

    Args:
        diff_mean (_type_): _description_
        variance (_type_): _description_
        max_deviation (_type_): _description_
        min_deviation (_type_): _description_

    Returns:
        Tuple[float, float, float, float]: _description_
    """    
    return diff_mean, sqrt(variance), max_deviation, min_deviation


def guess_99_95_68(mean, sd, max_deviation, min_deviation) -> Tuple[float, float, float, float, float]:
    """Example:

        ```
        diff_mean, readings = statistics(iterable_readings)
        diff_mean, variance, max_deviation, min_deviation = variance(diff_mean, readings)
        diff_mean, sd, max_deviation, min_deviation = standard_deviation(diff_mean, variance, max_deviation, min_deviation)
        val_99, val_95, val_68, max_deviation, min_deviation = guess_99_95_68(diff_mean, sd, max_deviation, min_deviation)
        ```

    Alternative example:

        ```
        val_99, val_95, val_68, max_deviation, min_deviation = guess_99_95_68(*standard_deviation(*variance(*statistics(iterable_readings)))
        ```

    Args:
        mean (_type_): _description_
        sd (_type_): _description_
        max_deviation (_type_): _description_
        min_deviation (_type_): _description_

    Returns:
        Tuple[float, float, float, float, float]: _description_
    """    
    # See: https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule
    val_68 = mean + sd
    val_95 = mean + 2 * sd
    val_99 = mean + 3 * sd
    return val_99, val_95, val_68, max_deviation, min_deviation


def average(data: Sequence[Number]) -> Number:
    data_len = len(data)
    data_sum = sum(data)
    try:
        return data_sum / data_len
    except ZeroDivisionError:
        return 0


def count_99_95_68(iterable_readings: Iterable[Number], operation: Callable=average) -> Tuple[float, float, float, float, float]:
    """_summary_

    Args:
        iterable_readings (Iterable[Number]): _description_
        operation (Callable, optional): _description_. Defaults to average. You can use other functions like min, max, median, etc.

    Returns:
        Tuple[float, float, float, float, float]: _description_
    """    
    diff_mean, readings = statistics(iterable_readings)
    _, _, max_deviation, min_deviation = variance(diff_mean, readings)
    sorted_readings = sorted(readings)
    readings_qnt = len(sorted_readings)

    def get_slice(data: Sequence, divider: int) -> Sequence:
        data_slice = data[:divider]
        if len(data_slice) == len(data):
            data_slice = data[:len(data)-1]
        return data_slice

    div_68 = round(readings_qnt * 0.68)
    val_68 = operation(get_slice(sorted_readings, div_68))

    div_95 = round(readings_qnt * 0.95)
    val_95 = operation(get_slice(sorted_readings, div_95))

    div_99 = round(readings_qnt * 0.99)
    val_99 = operation(get_slice(sorted_readings, div_99))

    return val_99, val_95, val_68, max_deviation, min_deviation

