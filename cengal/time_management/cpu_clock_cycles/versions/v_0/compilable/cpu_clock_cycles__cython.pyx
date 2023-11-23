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
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


IF IS_ARM == "True":
    cdef extern from "cpu_clock_cycles.h":
        u64 c_cpu_clock_cycles() nogil

    cpdef u64 cpu_clock_cycles():
        cdef u64 result = c_cpu_clock_cycles()
        return result

ELSE:
    cdef extern from "cpu_clock_cycles.h":
        unsigned long long c_cpu_clock_cycles() nogil

    cpdef unsigned long long cpu_clock_cycles() nogil:
        return c_cpu_clock_cycles()


cdef double _cycles_per_second = 1e9


cpdef void set_cycles_per_second(double cycles_per_second) nogil:
    global _cycles_per_second
    _cycles_per_second = cycles_per_second


cpdef double cpu_clock() nogil:
    return c_cpu_clock_cycles() / _cycles_per_second

