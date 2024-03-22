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


IF CD_IS_ARM == 1:
    from libc.stdint cimport uint64_t

    cdef extern from "cpu_clock_cycles.h":
        uint64_t c_cpu_clock_cycles() nogil

    cpdef uint64_t cpu_clock_cycles():
        cdef uint64_t result = c_cpu_clock_cycles()
        return result

ELSE:
    cdef extern from "cpu_clock_cycles.h":
        unsigned long long c_cpu_clock_cycles() nogil

    cpdef unsigned long long cpu_clock_cycles():
        return c_cpu_clock_cycles()


cdef double _cycles_per_second = 1e9


cpdef void set_cycles_per_second(double cycles_per_second):
    global _cycles_per_second
    _cycles_per_second = cycles_per_second


cpdef double cpu_clock():
    return c_cpu_clock_cycles() / _cycles_per_second

