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


class TimeLimitIsTooSmall(Exception):
    def __init__(self, min_time, *args):
        super().__init__(*args)
        self.min_time = min_time


# TODO: add support for cpu_ticks_count
class ClockType(Enum):
    fake = 0
    clock = 1
    perf_counter = 2
    process_time = 3


cdef inline unsigned long long _fake():
    return 0


cdef inline unsigned long long _cpython__clock():
    return <unsigned long long>clock()


cdef c_clock():
    return <double>_cpython__clock() / <double>CLOCKS_PER_SEC


cdef inline unsigned long long _perf_counter():
    return <unsigned long long>round(perf_counter() * <double>CLOCKS_PER_SEC)


cdef inline unsigned long long _process_time():
    return <unsigned long long>round(process_time() * <double>CLOCKS_PER_SEC)


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
        unsigned long long _cpython__run_time
        unsigned long long _cpython__number_of_iterations
        unsigned long long _cpython__last_tracked_number_of_iterations
        unsigned long long _cpython__start_time
        unsigned long long _cpython__end_time
        unsigned long long _cpython__relevant_stop_time
        bint _cpython__last_run_was_made
        object _iter_impl
        object _cpython__clock
        object _cpython__clock_type

    def __init__(self, double run_time, object clock_type=ClockType.perf_counter):
        self._iter_impl = None
        self._cpython__number_of_iterations = 0
        self._cpython__last_tracked_number_of_iterations = 0
        self._cpython__start_time = 0
        self._cpython__end_time = 0
        self._cpython__relevant_stop_time = 0
        self._cpython__last_run_was_made = False
        self._cpython__clock_type = clock_type
        self._cpython__clock = None
        self._init_clock()
        self._cpython__run_time = <unsigned long long>round(run_time * <double>CLOCKS_PER_SEC)
        if not self._cpython__run_time:
            raise TimeLimitIsTooSmall(1.0 / <double>CLOCKS_PER_SEC)

    def __call__(self, *args, **kwargs):
        return self._cpython__last_run_was_made
    
    def _init_clock(self):
        if ClockType.fake == self._cpython__clock_type:
            self._cpython__clock = _fake
        elif ClockType.clock == self._cpython__clock_type:
            self._cpython__clock = _cpython__clock
        elif ClockType.perf_counter == self._cpython__clock_type:
            self._cpython__clock = _perf_counter
        elif ClockType.process_time == self._cpython__clock_type:
            self._cpython__clock = _process_time

    def iter(self):
        raise NotImplemented()

    @property
    def iter_per_time_unit(self):
        raise NotImplemented()

    @property
    def iterations_made(self):
        return self._cpython__last_tracked_number_of_iterations

    @property
    def total_number_of_iterations_made(self):
        return self._cpython__number_of_iterations

    @property
    def time_spent(self):
        return <double>(self._cpython__relevant_stop_time - self._cpython__start_time) / <double>CLOCKS_PER_SEC

    @property
    def total_amount_of_time_spent(self):
        return <double>(self._cpython__end_time - self._cpython__start_time) / <double>CLOCKS_PER_SEC

    @property
    def clock_type(self):
        return self._cpython__clock_type

    # ===============
    @property
    def _clock_type(self):
        return self._cpython__clock_type

    @property
    def _last_tracked_number_of_iterations(self):
        return self._cpython__last_tracked_number_of_iterations

    @property
    def _number_of_iterations(self):
        return self._cpython__number_of_iterations
    
    @property
    def _start_time(self):
        return <double>self._cpython__start_time / <double>CLOCKS_PER_SEC
    
    @property
    def _end_time(self):
        return <double>self._cpython__end_time / <double>CLOCKS_PER_SEC
    
    @property
    def _relevant_stop_time(self):
        return <double>self._cpython__relevant_stop_time / <double>CLOCKS_PER_SEC
    
    @property
    def _last_run_was_made(self):
        return self._cpython__last_run_was_made
    
    def _clock_py(self):
        return <double>self._cpython__clock() / <double>CLOCKS_PER_SEC
    
    @property
    def _clock(self):
        return self._clock_py
    
    @property
    def _run_time(self):
        return <double>self._cpython__run_time / <double>CLOCKS_PER_SEC

    @clock_type.setter
    def clock_type(self, value: ClockType):
        self._cpython__clock_type = value
        self._init_clock()

    @_last_tracked_number_of_iterations.setter
    def _last_tracked_number_of_iterations(self, value):
        self._cpython__last_tracked_number_of_iterations = value

    @_number_of_iterations.setter
    def _number_of_iterations(self, value):
        self._cpython__number_of_iterations = value

    @_clock_type.setter
    def _clock_type(self, value: ClockType):
        self._cpython__clock_type = value
    
    @_start_time.setter
    def _start_time(self, value):
        self._cpython__start_time = <unsigned long long>round(value * <double>CLOCKS_PER_SEC)
    
    @_end_time.setter
    def _end_time(self, value):
        self._cpython__end_time = <unsigned long long>round(value * <double>CLOCKS_PER_SEC)
    
    @_relevant_stop_time.setter
    def _relevant_stop_time(self, value):
        self._cpython__relevant_stop_time = <unsigned long long>round(value * <double>CLOCKS_PER_SEC)
    
    @_last_run_was_made.setter
    def _last_run_was_made(self, value):
        self._cpython__last_run_was_made = value
    
    @_run_time.setter
    def _run_time(self, value):
        self._cpython__run_time = <unsigned long long>round(value * <double>CLOCKS_PER_SEC)


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
        unsigned long long _cpython__half_of_the_run_time
        unsigned long long _cpython__relevant_start_time
        unsigned long long _cpython__relevant_number_of_iterations_at_start
        unsigned long long _cpython__relevant_number_of_iterations_at_end
        unsigned long long _cpython__next_test_stop_on
        object _cpython__testing_worker

    def __init__(self, double run_time, object clock_type=ClockType.perf_counter):
        super().__init__(run_time, clock_type)
        self._iter_impl = self._first_run
        self._cpython__testing_worker = self._test_runs
        self._cpython__relevant_start_time = 0
        self._cpython__relevant_number_of_iterations_at_start = 0
        self._cpython__relevant_number_of_iterations_at_end = 0
        self._cpython__next_test_stop_on = 1
        self._cpython__half_of_the_run_time = <unsigned long long>round(<double>self._cpython__run_time / 2.0)
        if not self._cpython__half_of_the_run_time:
            raise TimeLimitIsTooSmall(2.0 / <double>CLOCKS_PER_SEC)

    def iter(self):
        return self._iter_impl()

    @property
    def iter_per_time_unit(self):
        cdef:
            double divider

        if self._cpython__last_run_was_made:
            divider = <double>(self._cpython__relevant_stop_time - self._cpython__relevant_start_time) / <double>CLOCKS_PER_SEC
            if 0.0 != divider:
                return <double>(self._cpython__relevant_number_of_iterations_at_end - self._cpython__relevant_number_of_iterations_at_start) \
                       / divider
            return 0.0
        else:
            divider = <double>(self._cpython__end_time - self._cpython__start_time) / <double>CLOCKS_PER_SEC
            if 0.0 != divider:
                return <double>self._cpython__last_tracked_number_of_iterations / divider
            return 0.0

    def _first_run(self):
        self._cpython__number_of_iterations += 1
        self._cpython__relevant_start_time = self._cpython__start_time = self._cpython__clock()
        self._iter_impl = self._subsequent_runs
        return self._test_sub_runs(self._cpython__start_time)

    def _subsequent_runs(self):
        self._cpython__number_of_iterations += 1
        if self._cpython__number_of_iterations >= self._cpython__next_test_stop_on:
            return self._cpython__testing_worker()
        return True

    def _test_runs(self):
        return self._test_sub_runs(self._cpython__clock())

    def _test_sub_runs(self, unsigned long long current_time):
        cdef:
            unsigned long long delta_time
            unsigned long long time_left
            double iterations_per_second
            unsigned long long iterations_left

        self._cpython__relevant_stop_time = self._cpython__end_time = current_time
        self._cpython__last_tracked_number_of_iterations = self._cpython__number_of_iterations
        delta_time = current_time - self._cpython__start_time
        # print()
        # print('delta_time: ', delta_time, '; self._cpython__half_of_the_run_time: ', self._cpython__half_of_the_run_time)
        if delta_time >= self._cpython__half_of_the_run_time:
            if delta_time >= self._cpython__run_time:
                time_left = 0
            else:
                time_left = self._cpython__run_time - delta_time
            
            # No need to:
            # if time_left < 0:
            #     time_left = 0
            iterations_per_second = <double>self._cpython__number_of_iterations / <double>delta_time
            iterations_left = <unsigned long long>(round(iterations_per_second * time_left))
            # print('iterations_left: ', iterations_left, '; iterations_per_second: ', iterations_per_second, '; time_left: ', time_left)
            if iterations_left > 0:
                self._cpython__next_test_stop_on = self._cpython__number_of_iterations + iterations_left
                self._cpython__testing_worker = self._last_run
                self._cpython__relevant_start_time = current_time
                self._cpython__relevant_number_of_iterations_at_start = self._cpython__number_of_iterations
                return True
            else:
                return self._last_sub_run(current_time)
        
        self._cpython__next_test_stop_on *= 2
        return True

    def _last_run(self):
        return self._last_sub_run(self._cpython__clock())

    def _last_sub_run(self, unsigned long long current_time):
        self._cpython__relevant_stop_time = self._cpython__end_time = current_time
        self._cpython__last_tracked_number_of_iterations = self._cpython__number_of_iterations
        self._cpython__relevant_number_of_iterations_at_end = self._cpython__number_of_iterations
        self._cpython__testing_worker = self._after_last_runs
        self._cpython__last_run_was_made = 1
        return False

    def _after_last_runs(self):
        self._cpython__end_time = self._cpython__clock()
        return False
    
    @property
    def _testing_worker(self):
        return self._cpython__testing_worker
    
    @property
    def _relevant_start_time(self):
        return <double>self._cpython__relevant_start_time / <double>CLOCKS_PER_SEC
    
    @property
    def _relevant_number_of_iterations_at_start(self):
        return self._cpython__relevant_number_of_iterations_at_start
    
    @property
    def _relevant_number_of_iterations_at_end(self):
        return self._cpython__relevant_number_of_iterations_at_end
    
    @property
    def _next_test_stop_on(self):
        return self._cpython__next_test_stop_on
    
    @property
    def _half_of_the_run_time(self):
        return <double>self._cpython__half_of_the_run_time / <double>CLOCKS_PER_SEC
    
    @_testing_worker.setter
    def _testing_worker(self, value):
        self._cpython__testing_worker = value
    
    @_relevant_start_time.setter
    def _relevant_start_time(self, value):
        self._cpython__relevant_start_time = <unsigned long long>round(value * <double>CLOCKS_PER_SEC)
    
    @_relevant_number_of_iterations_at_start.setter
    def _relevant_number_of_iterations_at_start(self, value):
        self._cpython__relevant_number_of_iterations_at_start = value
    
    @_relevant_number_of_iterations_at_end.setter
    def _relevant_number_of_iterations_at_end(self, value):
        self._cpython__relevant_number_of_iterations_at_end = value
    
    @_next_test_stop_on.setter
    def _next_test_stop_on(self, value):
        self._cpython__next_test_stop_on = value
    
    @_half_of_the_run_time.setter
    def _half_of_the_run_time(self, value):
        self._cpython__half_of_the_run_time = <unsigned long long>round(value * <double>CLOCKS_PER_SEC)


cdef class GreedyTracer(BaseTracer):
    """
    Greedy Main tracer.
    Its task is to find out the speed of code execution, and to stop the counting at about the specified time.
    The difference is that he checks time every single iteration.

    Example of use is the same as for the Tracer()

    """

    def __init__(self, run_time: double, clock_type=ClockType.perf_counter):
        super().__init__(run_time, clock_type)
        self._iter_impl = self._first_run

    def iter(self):
        return self._iter_impl()

    def _first_run(self):
        self._cpython__start_time = self._cpython__clock()
        self._iter_impl = self._subsequent_runs
        return self._subsequent_runs()

    def _subsequent_runs(self):
        self._cpython__relevant_stop_time = self._cpython__end_time = self._cpython__clock()
        self._cpython__number_of_iterations += 1
        self._cpython__last_tracked_number_of_iterations = self._cpython__number_of_iterations

        if (self._cpython__relevant_stop_time - self._cpython__start_time) < self._cpython__run_time:
            return True
        else:
            self._cpython__last_run_was_made = True
            self._iter_impl = self._after_last_runs
            return False

    def _after_last_runs(self):
        self._cpython__number_of_iterations += 1
        self._cpython__end_time = self._cpython__clock()
        return False

    @property
    def iter_per_time_unit(self):
        cdef:
            double divider

        divider = <double>(self._cpython__relevant_stop_time - self._cpython__start_time) / <double>CLOCKS_PER_SEC
        if 0 != divider:
            return <double>self._cpython__last_tracked_number_of_iterations / divider
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
        double _cpython__iter_per_time_unit
        unsigned long long _cpython__number_of_iterations_needed

    def __init__(self, iter_per_time_unit: double, run_time: double, object clock_type=ClockType.fake):
        super().__init__(run_time, clock_type)
        self._cpython__iter_per_time_unit = iter_per_time_unit
        self._iter_impl = self._first_run
        self._cpython__number_of_iterations_needed = <unsigned long long>round(self._cpython__iter_per_time_unit * (<double>self._cpython__run_time / <double>CLOCKS_PER_SEC))

    def iter(self):
        return self._iter_impl()

    def _first_run(self):
        self._cpython__start_time = self._cpython__clock()
        self._iter_impl = self._subsequent_runs
        return self._subsequent_runs()

    def _subsequent_runs(self):
        self._cpython__number_of_iterations += 1
        self._cpython__last_tracked_number_of_iterations = self._cpython__number_of_iterations
        if self._cpython__number_of_iterations < self._cpython__number_of_iterations_needed:
            return True
        else:
            self._cpython__relevant_stop_time = self._cpython__end_time = self._cpython__clock()
            self._cpython__last_run_was_made = True
            self._iter_impl = self._after_last_runs
            return False

    def _after_last_runs(self):
        self._cpython__number_of_iterations += 1
        self._cpython__end_time = self._cpython__clock()
        return False

    @property
    def iter_per_time_unit(self):
        cdef:
            double divider

        if self._cpython__last_run_was_made:
            divider = <double>(self._cpython__relevant_stop_time - self._cpython__start_time) / <double>CLOCKS_PER_SEC
            if 0.0 != divider:
                return <double>self._cpython__last_tracked_number_of_iterations / divider
            return 0.0
        else:
            return self._cpython__iter_per_time_unit

    @property
    def _iter_per_time_unit(self):
        return self._cpython__iter_per_time_unit
    
    @property
    def _number_of_iterations_needed(self):
        return self._cpython__number_of_iterations_needed

    @_iter_per_time_unit.setter
    def _iter_per_time_unit(self, value):
        self._cpython__iter_per_time_unit = value
    
    @_number_of_iterations_needed.setter
    def _number_of_iterations_needed(self, value):
        self._cpython__number_of_iterations_needed = value


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
