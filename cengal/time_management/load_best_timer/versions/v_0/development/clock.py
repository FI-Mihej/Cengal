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
__version__ = "4.3.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


def t0():
    from cengal.time_management.cpu_clock import perf_counter
    dtime = perf_counter() - perf_counter()
    print(dtime, (1 / dtime) if dtime else 0)


def t1():
    from cengal.time_management.cpu_clock import cpu_clock
    dtime = cpu_clock() - cpu_clock()
    print(dtime, (1 / dtime) if dtime else 0)


def t2():
    from cengal.time_management.cpu_clock_cycles import perf_counter
    dtime = perf_counter() - perf_counter()
    print(dtime, (1 / dtime) if dtime else 0)


def t3():
    from cengal.time_management.cpu_clock_cycles import cpu_clock
    dtime = cpu_clock() - cpu_clock()
    print(dtime, (1 / dtime) if dtime else 0)


def t4():
    from cengal.time_management.cpu_clock_cycles import cpu_clock_cycles
    dtime = cpu_clock_cycles() - cpu_clock_cycles()
    print(dtime, (1 / dtime) if dtime else 0)


def t5():
    from cengal.time_management.load_best_timer import perf_counter
    dtime = perf_counter() - perf_counter()
    print(dtime, (1 / dtime) if dtime else 0)


def t6():
    from time import perf_counter
    dtime = perf_counter() - perf_counter()
    print(dtime, (1 / dtime) if dtime else 0)


if __name__ == '__main__':
    t0()
    t1()
    t2()
    t3()
    t4()
    t5()
    t6()
