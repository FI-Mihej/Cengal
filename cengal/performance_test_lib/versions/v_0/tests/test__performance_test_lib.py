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

from cengal.performance_test_lib import PrecisePerformanceTestTracer

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


def precise_perfomance_test_tracer():
    pptt = PrecisePerformanceTestTracer(5.0)

    while pptt.iter():
        i = '456'
        k = int('1243' + i)
    print('{} iter/s; {} seconds; {} iterations'.format(pptt.iter_per_time_unit, pptt.time_spent, pptt.iterations_made))

    with pptt as fast_iter:
        for j in fast_iter:
            i = '456'
            k = int('1243' + i)

    print('{} iter/s; {} seconds; {} iterations'.format(pptt.iter_per_time_unit, pptt.time_spent, pptt.iterations_made))

    start_time = pptt._clock()
    for i in range(pptt.iterations_made):
        i = '456'
        k = int('1243' + i)
    end_time = pptt._clock()
    time_diff = end_time - start_time
    speed = 0
    if time_diff:
        speed = pptt.iterations_made / time_diff
    print('{} iter/s; {} seconds; {} iterations'.format(speed, time_diff, pptt.iterations_made))


def main():
    precise_perfomance_test_tracer()


if __name__ == '__main__':
    main()
