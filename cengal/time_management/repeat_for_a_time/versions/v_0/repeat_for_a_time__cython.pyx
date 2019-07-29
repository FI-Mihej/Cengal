#!/usr/bin/env python
# coding=utf-8

# Copyright © 2017 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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
    from time import perf_counter
except ImportError:
    pass

try:
    from time import process_time
except ImportError:
    pass

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2017 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "0.0.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
__status__ = "Prototype"
# __status__ = "Development"
# __status__ = "Production"


if cython.compiled:
    print('"{}" - compiled.'.format(__name__))
else:
    print('"{}" - interpreted script.'.format(__name__))


class TimeLimitIsTooSmall(Exception):
    pass


class ClockType(Enum):
    fake = 0
    clock = 1
    perf_counter = 2
    process_time = 3


cdef inline clock_t _fake():
    return 0


cdef inline clock_t _clock():
    return clock()

def c_clock():
    return <float>_clock() / <float>CLOCKS_PER_SEC


cdef inline clock_t _perf_counter():
    return <clock_t>round(perf_counter() * <float>CLOCKS_PER_SEC)


cdef inline clock_t _process_time():
    return <clock_t>round(process_time() * <float>CLOCKS_PER_SEC)


cdef class BaseTracer:
    """
    Base class of all tracers

    Lets assume you have a tracer:

        tr = Tracer(10.0)

    Or a fake tracer:

        tr = TracerCounter(10000, 10.0)

    As result you can use next interfaces

        tr()  # Will return True if tracer has finished it's counting and as a result, the specified time was passed.

        tr.iter_per_time_unit  # Will return counted time of iterations per second (if time() function uses second
            as a time unit)

        tr.iterations_made  # Will return number of all iterations made (including those that were produced after the
            end of the counting)

        tr.time_spent  # Will return time spent (including time that were used after the end of the counting)

        tr.clock_type  # Will return used time function type (ClockType enum)

    """

    cdef:
        clock_t _run_time
        unsigned int _number_of_iterations
        unsigned int _last_tracked_number_of_iterations
        clock_t _start_time
        clock_t _end_time
        clock_t _relevant_stop_time
        bint _last_run_was_made
        object _iter_impl
        object _clock
        object _clock_type

    def __init__(self, float run_time: float, object clock_type=ClockType.perf_counter):
        self._iter_impl = None
        self._number_of_iterations = 0
        self._last_tracked_number_of_iterations = 0
        self._start_time = 0
        self._end_time = 0
        self._relevant_stop_time = 0
        self._last_run_was_made = False
        self._clock_type = clock_type
        self._clock = None
        if ClockType.fake == self._clock_type:
            self._clock = _fake
        elif ClockType.clock == self._clock_type:
            self._clock = _clock
        elif ClockType.perf_counter == self._clock_type:
            self._clock = _perf_counter
        elif ClockType.process_time == self._clock_type:
            self._clock = _process_time
        self._run_time = <clock_t>round(run_time * <float>CLOCKS_PER_SEC)
        if not self._run_time:
            raise TimeLimitIsTooSmall()

    def __call__(self, *args, **kwargs):
        return self._last_run_was_made

    def iter(self):
        raise NotImplemented()

    @property
    def iter_per_time_unit(self):
        raise NotImplemented()

    @property
    def iterations_made(self):
        return self._last_tracked_number_of_iterations

    @property
    def total_number_of_iterations_made(self):
        return self._number_of_iterations

    @property
    def time_spent(self):
        return <float>(self._relevant_stop_time - self._start_time) / <float>CLOCKS_PER_SEC

    @property
    def total_amount_of_time_spent(self):
        return <float>(self._end_time - self._start_time) / <float>CLOCKS_PER_SEC

    @property
    def clock_type(self):
        raise self._clock_type


cdef class Tracer(BaseTracer):
    """
    Main tracer.
    Its task is to find out the speed of code execution, and to stop the counting at about the specified time.

    Example of use:

        tr = Tracer(10.0)
        while tr.iter():
            i = '456'
            k = int('1243' + i)

        print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))

    """

    cdef:
        clock_t _half_of_the_run_time
        clock_t _relevant_start_time
        unsigned int _relevant_number_of_iterations_at_start
        unsigned int _relevant_number_of_iterations_at_end
        unsigned int _next_test_stop_on
        object _testing_worker

    def __init__(self, float run_time: float, object clock_type=ClockType.clock):
        super().__init__(run_time, clock_type)
        self._iter_impl = self._first_run
        self._testing_worker = self._test_runs
        self._relevant_start_time = 0
        self._relevant_number_of_iterations_at_start = 0
        self._relevant_number_of_iterations_at_end = 0
        self._next_test_stop_on = 1
        self._half_of_the_run_time = <clock_t>round(<float>self._run_time / 2.0)
        if not self._half_of_the_run_time:
            raise TimeLimitIsTooSmall()

    def iter(self):
        return self._iter_impl()

    @property
    def iter_per_time_unit(self):
        cdef:
            float divider

        if self._last_run_was_made:
            divider = <float>(self._relevant_stop_time - self._relevant_start_time) / <float>CLOCKS_PER_SEC
            if 0.0 != divider:
                return <float>(self._relevant_number_of_iterations_at_end - self._relevant_number_of_iterations_at_start) \
                       / divider
            return 0.0
        else:
            divider = <float>(self._end_time - self._start_time) / <float>CLOCKS_PER_SEC
            if 0.0 != divider:
                return <float>self._last_tracked_number_of_iterations / divider
            return 0.0

    def _first_run(self):
        self._number_of_iterations += 1
        self._relevant_start_time = self._start_time = self._clock()
        self._iter_impl = self._subsequent_runs
        return self._test_sub_runs(self._start_time)

    def _subsequent_runs(self):
        self._number_of_iterations += 1
        if self._number_of_iterations >= self._next_test_stop_on:
            return self._testing_worker()
        return True

    def _test_runs(self):
        return self._test_sub_runs(self._clock())

    def _test_sub_runs(self, clock_t current_time):
        cdef:
            clock_t delta_time
            clock_t time_left
            float iterations_per_second
            float iterations_left

        self._relevant_stop_time = self._end_time = current_time
        self._last_tracked_number_of_iterations = self._number_of_iterations
        delta_time = current_time - self._start_time
        if delta_time >= self._half_of_the_run_time:
            time_left = self._run_time - delta_time
            # No need to:
            # if time_left < 0:
            #     time_left = 0
            iterations_per_second = <float>self._number_of_iterations / <float>delta_time
            iterations_left = iterations_per_second * time_left
            if iterations_left > 0.0:
                self._next_test_stop_on = self._number_of_iterations + round(iterations_left)
                self._testing_worker = self._last_run
                self._relevant_start_time = current_time
                self._relevant_number_of_iterations_at_start = self._number_of_iterations
                return True
            else:
                return self._last_sub_run(current_time)
        self._next_test_stop_on *= 2
        return True

    def _last_run(self):
        return self._last_sub_run(self._clock())

    def _last_sub_run(self, clock_t current_time):
        self._relevant_stop_time = self._end_time = current_time
        self._last_tracked_number_of_iterations = self._number_of_iterations
        self._relevant_number_of_iterations_at_end = self._number_of_iterations
        self._testing_worker = self._after_last_runs
        self._last_run_was_made = 1
        return False

    def _after_last_runs(self):
        self._end_time = self._clock()
        return False


cdef class GreedyTracer(BaseTracer):
    """
    Greedy Main tracer.
    Its task is to find out the speed of code execution, and to stop the counting at about the specified time.
    The difference is that he checks time every single iteration.

    Example of use is the same as for the Tracer()

    """

    def __init__(self, run_time: float, clock_type=ClockType.perf_counter):
        super().__init__(run_time, clock_type)
        self._iter_impl = self._first_run

    def iter(self):
        return self._iter_impl()

    def _first_run(self):
        self._start_time = self._clock()
        self._iter_impl = self._subsequent_runs
        return self._subsequent_runs()

    def _subsequent_runs(self):
        self._relevant_stop_time = self._end_time = self._clock()
        self._number_of_iterations += 1
        self._last_tracked_number_of_iterations = self._number_of_iterations

        if (self._relevant_stop_time - self._start_time) < self._run_time:
            return True
        else:
            self._last_run_was_made = True
            self._iter_impl = self._after_last_runs
            return False

    def _after_last_runs(self):
        self._number_of_iterations += 1
        self._end_time = self._clock()
        return False

    @property
    def iter_per_time_unit(self):
        cdef:
            float divider

        divider = <float>(self._relevant_stop_time - self._start_time) / <float>CLOCKS_PER_SEC
        if 0 != divider:
            return <float>self._last_tracked_number_of_iterations / divider
        return 0


cdef class TracerCounter(BaseTracer):
    """
    Counting tracer. Pseudo-tracer.
    Its don't have an overhead of periodic calling time() function.
    Its task is to count down within a given time, using the speed information already counted by the real tracer
    (by the Tracer class).

    Example of use:

        trc = TracerCounter(10000, 10.0)
        while trc.iter():
            i = '456'
            k = int('1243' + i)

        print('{} iter/s; {} seconds; {} iters'.format(trc.iter_per_time_unit, trc.time_spent, trc.iterations_made))

    or:
        def made_tests()->Tracer:
            tr = Tracer(0.1)  # Run for about 0.1 of second.
            while tr.iter():
                some_my_code()
            return tr

        def run(run_time: float, tests_result: Tracer):
            trc = TracerCounter(tests_result.iter_per_time_unit, run_time)
            while trc.iter():
                some_my_code()

            print('{} iter/s; {} seconds; {} iterations'.format(trc.iter_per_time_unit, trc.time_spent,
                    trc.iterations_made))

        def main():
            tests_result = made_tests()
            ...
            while True:
                time_to_rur_str = input('Enter run time: ')
                if not time_to_run_str:
                    break
                run(float(time_to_rur_str), tests_result)

    """

    cdef:
        float _iter_per_time_unit
        unsigned int _number_of_iterations_needed

    def __init__(self, iter_per_time_unit: float, run_time: float, object clock_type=ClockType.fake):
        super().__init__(run_time, clock_type)
        self._iter_per_time_unit = iter_per_time_unit
        self._iter_impl = self._first_run
        self._number_of_iterations_needed = <clock_t>round(self._iter_per_time_unit * (<float>self._run_time / <float>CLOCKS_PER_SEC))

    def iter(self):
        return self._iter_impl()

    def _first_run(self):
        self._start_time = self._clock()
        self._iter_impl = self._subsequent_runs
        return self._subsequent_runs()

    def _subsequent_runs(self):
        self._number_of_iterations += 1
        self._last_tracked_number_of_iterations = self._number_of_iterations
        if self._number_of_iterations < self._number_of_iterations_needed:
            return True
        else:
            self._relevant_stop_time = self._end_time = self._clock()
            self._last_run_was_made = True
            self._iter_impl = self._after_last_runs
            return False

    def _after_last_runs(self):
        self._number_of_iterations += 1
        self._end_time = self._clock()
        return False

    @property
    def iter_per_time_unit(self):
        cdef:
            float divider

        if self._last_run_was_made:
            divider = <float>(self._relevant_stop_time - self._start_time) / <float>CLOCKS_PER_SEC
            if 0.0 != divider:
                return <float>self._last_tracked_number_of_iterations / divider
            return 0.0
        else:
            return self._iter_per_time_unit


cdef class TracerIterator:
    """
    An iterator class. It converts any type of given tracer into an iterator.

    As result you have an option to use constructions like this:

        for i in TracerIterator(Tracer(20.0)):
            k = int('1243')

    But keep in mind that in this case there will be a bigger overhead. And there will be less CPU time for the payload.

    """

    cdef object _tracer

    def __init__(self, tracer):
        self._tracer = tracer

    def __iter__(self):
        return self

    def __next__(self):
        if self._tracer.iter():
            return self._tracer.iterations_made
        else:
            raise StopIteration()

    def next(self):
        return self.__next__()

    @property
    def tracer(self):
        return self._tracer
