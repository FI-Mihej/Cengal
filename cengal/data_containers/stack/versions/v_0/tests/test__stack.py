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
from cengal.data_containers.stack import *
from collections import deque

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


def test_stack():
    print()
    print('Stack:')

    number_of_items = 100000
    st = Stack()

    pptt = PrecisePerformanceTestTracer(5.0)

    while pptt.iter():
        for i in range(number_of_items):
            st.push(i)
        for i in range(number_of_items):
            st.pop()

    with pptt as fast_iter:
        for j in fast_iter:
            for i in range(number_of_items):
                st.push(i)
            for i in range(number_of_items):
                st.pop()

    print('{} iter/s; {} seconds; {} iterations'.format(pptt.iter_per_time_unit * number_of_items,
                                                        pptt.time_spent,
                                                        pptt.iterations_made))


def test_deque():
    print()
    print('deque:')

    number_of_items = 100000
    st = deque()

    pptt = PrecisePerformanceTestTracer(5.0)

    while pptt.iter():
        for i in range(number_of_items):
            st.append(i)
        for i in range(number_of_items):
            st.pop()

    with pptt as fast_iter:
        for j in fast_iter:
            for i in range(number_of_items):
                st.append(i)
            for i in range(number_of_items):
                st.pop()

    print('{} iter/s; {} seconds; {} iterations'.format(pptt.iter_per_time_unit * number_of_items,
                                                        pptt.time_spent,
                                                        pptt.iterations_made))


def test_list():
    print()
    print('list:')

    number_of_items = 100000
    st = list()

    pptt = PrecisePerformanceTestTracer(5.0)

    while pptt.iter():
        for i in range(number_of_items):
            st.append(i)
        for i in range(number_of_items):
            st.pop()

    with pptt as fast_iter:
        for j in fast_iter:
            for i in range(number_of_items):
                st.append(i)
            for i in range(number_of_items):
                st.pop()

    print('{} iter/s; {} seconds; {} iterations'.format(pptt.iter_per_time_unit * number_of_items,
                                                        pptt.time_spent,
                                                        pptt.iterations_made))


def main():
    test_stack()
    test_deque()
    test_list()


if __name__ == '__main__':
    main()
