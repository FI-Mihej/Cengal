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

import cython
from enum import Enum
from libc.time cimport clock, CLOCKS_PER_SEC, clock_t
perf_counter = process_time = clock

try:
    from cengal.time_management.cpu_clock_cycles import perf_counter
except ImportError:
    try:
        from time import perf_counter
    except ImportError:
        pass

try:
    from time import process_time
except ImportError:
    pass

import gc
from cengal.time_management.repeat_for_a_time import Tracer, ClockType

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


if cython.compiled:
    # print('"{}" - compiled.'.format(__name__))
    pass
else:
    print('"{}" - interpreted script.'.format(__name__))


cdef class PreciseAutoWhilePerformanceTestTracer:
    cdef public object tr
    cdef public bint suppress_exceptions
    cdef public bint turn_off_gc
    cdef public bint gc_was_enabled
    cdef public int while_phase
    cdef public double _beginning_time
    cdef public double _start_time
    cdef public double _end_time
    cdef public object _call_impl

    def __init__(self, double run_time, object clock_type=ClockType.perf_counter, bint suppress_exceptions=False, bint turn_off_gc=False):
        self.tr = Tracer(run_time, clock_type)
        self.suppress_exceptions = suppress_exceptions
        self.turn_off_gc = turn_off_gc
        self.gc_was_enabled = False
        self.while_phase = 0
        self._beginning_time = perf_counter()
        self._start_time = 0
        self._end_time = 0
        self._call_impl = self._call_first

    def __enter__(self):
        self._call_impl = self._call_first
        self._beginning_time = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._end_time = perf_counter()
        exception_handled = False
        if exc_type is not None:
            exception_handled = issubclass(exc_type, StopIteration)
        
        if self.turn_off_gc and self.gc_was_enabled:
            gc.enable()

        if exception_handled or self.suppress_exceptions:
            return True
    
    def __call__(self):
        return self._call_impl()

    cdef bint _call_first(self):
        result = self.tr.iter()
        if result:
            return result
        else:
            self.while_phase = 1
            if self.turn_off_gc:
                self.gc_was_enabled = gc.isenabled()
                gc.disable()
            
            _next = range(1, 1 + self.tr._last_tracked_number_of_iterations).__iter__().__next__
            self._call_impl = _next
            self._start_time = perf_counter()
            return _next()

    @property
    def iter_per_time_unit(self):
        if self.time_spent:
            return self.iterations_made / self.time_spent
        else:
            return 0

    @property
    def iterations_made(self):
        return self.tr._last_tracked_number_of_iterations

    @property
    def total_number_of_iterations_made(self):
        return self.tr._number_of_iterations

    @property
    def time_spent(self):
        return self._end_time - self._start_time

    @property
    def total_time_spent(self):
        return self._beginning_time - self._start_time
