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
__version__ = "4.4.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.time_management.run_time import RT
from cengal.statistics.normal_distribution import statistics, variance as cengal_variance, standard_deviation, guess_99_95_68, count_99_95_68, average
from statistics import stdev, variance as py_variance, mean, pstdev, pvariance, median, median_low, median_high
from unittest import TestCase, main


class TestNormalDistrubution(TestCase):
    def test_compare_performance(self):
        from random import randint
        from time import time

        int_range = (0, 1000)
        sample_number = 1000000
        readings = [randint(*int_range) for _ in range(sample_number)]
        print(f'readings generated: ints in range {int_range}, {sample_number} samples')

        with RT() as rt:
            diff_mean, readings = statistics(readings)
        print(f'statistics: {rt.rt}')

        with RT() as rt:
            diff_mean, variance, max_deviation, min_deviation = cengal_variance(diff_mean, readings)
        print(f'variance: {rt.rt}')

        with RT() as rt:
            diff_mean, sd, max_deviation, min_deviation = standard_deviation(diff_mean, variance, max_deviation, min_deviation)
        print(f'standard_deviation: {rt.rt}')

        with RT() as rt:
            val_99, val_95, val_68, max_deviation, min_deviation = guess_99_95_68(diff_mean, sd, max_deviation, min_deviation)
        print(f'guess_99_95_68: {rt.rt}')

        with RT() as rt:
            val_99, val_95, val_68, max_deviation, min_deviation = count_99_95_68(readings, median)
        print(f'count_99_95_68 median: {rt.rt}')

        with RT() as rt:
            val_99, val_95, val_68, max_deviation, min_deviation = count_99_95_68(readings, average)
        print(f'count_99_95_68 average: {rt.rt}')

        with RT() as rt:
            val_99, val_95, val_68, max_deviation, min_deviation = count_99_95_68(readings, min)
        print(f'count_99_95_68 min: {rt.rt}')

        with RT() as rt:
            val_99, val_95, val_68, max_deviation, min_deviation = count_99_95_68(readings, max)
        print(f'count_99_95_68 max: {rt.rt}')

        with RT() as rt:
            average_value = average(readings)
        print(f'average: {rt.rt}')

        with RT() as rt:
            py_mean = mean(readings)
        print(f'mean: {rt.rt}')

        with RT() as rt:
            result = median(readings)
        print(f'median: {rt.rt}')

        with RT() as rt:
            result = median_low(readings)
        print(f'median_low: {rt.rt}')

        with RT() as rt:
            result = median_high(readings)
        print(f'median_high: {rt.rt}')

        with RT() as rt:
            result = py_variance(readings)
        print(f'variance: {rt.rt}')

        with RT() as rt:
            result = stdev(readings)
        print(f'stdev: {rt.rt}')

        with RT() as rt:
            result = pstdev(readings)
        print(f'pstdev: {rt.rt}')

        with RT() as rt:
            result = py_variance(readings, py_mean)
        print(f'variance with mean: {rt.rt}')

        with RT() as rt:
            result = stdev(readings, py_mean)
        print(f'stdev with mean: {rt.rt}')

        with RT() as rt:
            result = pstdev(readings, py_mean)
        print(f'pstdev with mean: {rt.rt}')


if __name__ == '__main__':
    main()
