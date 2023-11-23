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

import copy
import gc
from contextlib import contextmanager
from cengal.code_flow_control.smart_values.versions.v_2 import ValueExistence
from cengal.parallel_execution.coroutines.coro_standard_services.lazy_print.versions.v_0.lazy_print import lprint
from cengal.time_management.load_best_timer import perf_counter
from cengal.time_management.repeat_for_a_time import Tracer, ClockType

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


class PerformanceTestResult(Exception):
    def __init__(self, result):
        super(PerformanceTestResult, self).__init__()
        self.result = result


@contextmanager
def test_run_time(test_name: str, number_of_iterations: int, throw_result: bool=False, throw_result_anyway: bool=True, ignore_index=False):
    index = ValueExistence(True, copy.copy(number_of_iterations))
    start_time = perf_counter()
    exception_occures = False
    try:
        yield index
    except:
        if not throw_result_anyway:
            exception_occures = True
        raise
    finally:
        if not ignore_index:
            number_of_iterations -= index.value
        
        end_time = perf_counter()
        result_time = end_time - start_time
        if result_time > 0:
            text_result = f'>>> "{test_name}"\n\tIt was used {result_time} seconds to process {number_of_iterations} iterations.\n\tThere is {number_of_iterations / result_time} iterations per second\n'
        else:
            text_result = f'>>> "{test_name}"\n\tIt was used {result_time} seconds to process {number_of_iterations} iterations.\n'

        lprint(text_result)

        if (not exception_occures) and throw_result:
            result_data = dict()
            result_data['test_name'] = test_name
            result_data['result_time'] = result_time
            if result_time > 0:
                result_data['iterations_per_time_unit'] = number_of_iterations / result_time
            else:
                result_data['iterations_per_time_unit'] = None
            raise PerformanceTestResult(result_data)


def test_function_run_time(testable_function):
    """
    Use 'performance_test_lib__iterations_qnt=1000000' parameter to pass number of iterations
    :param testable_function: function
    :return:
    """
    def run_time_test_func(*args, **kwargs):

        test_name = ''
        if 'performance_test_lib__test_name' in kwargs:
            test_name = str(kwargs['performance_test_lib__test_name'])
            del kwargs['performance_test_lib__test_name']
        test_name = '{}: {}'.format(str(testable_function), test_name)

        number_of_iterations = 1
        if 'performance_test_lib__iterations_qnt' in kwargs:
            number_of_iterations = int(kwargs['performance_test_lib__iterations_qnt'])
            del kwargs['performance_test_lib__iterations_qnt']

        throw_result = False
        if 'performance_test_lib__throw_result' in kwargs:
            throw_result = kwargs['performance_test_lib__throw_result']
            del kwargs['performance_test_lib__throw_result']

        with test_run_time(test_name, number_of_iterations, throw_result) as index:
            while index.value > 0:
                testable_function(*args, **kwargs)
                index.value -= 1
    return run_time_test_func


def process_performance_test_results(tracer: Tracer, test_name: str, throw_result: bool=False):
    number_of_iterations = tracer.iterations_made
    result_time = tracer.time_spent
    iterations_per_time_unit = tracer.iter_per_time_unit
    print('>>> "{}"'.format(test_name))
    print('\t' + 'It was used', result_time, 'seconds to process', number_of_iterations, 'iterations.')
    print('\t' + 'There is', iterations_per_time_unit, 'iterations per second')

    if throw_result:
        result_data = (test_name, result_time, iterations_per_time_unit)
        raise PerformanceTestResult(result_data)


@contextmanager
def test_performance(test_name: str, run_time: float, throw_result: bool=False, clock_type=ClockType.perf_counter):
    tracer = Tracer(run_time, clock_type)
    try:
        yield tracer
    except:
        raise
    finally:
        process_performance_test_results(tracer, test_name, throw_result)


def test_function_performance(testable_function):
    """
    Use 'performance_test_lib__run_time=1.5' parameter to pass number of seconds to test
    :param testable_function: function
    :return:
    """
    def run_time_test_func(*args, **kwargs):

        test_name = ''
        if 'performance_test_lib__test_name' in kwargs:
            test_name = str(kwargs['performance_test_lib__test_name'])
            del kwargs['performance_test_lib__test_name']
        test_name = '{}: {}'.format(str(testable_function), test_name)

        run_time = 0
        if 'performance_test_lib__run_time' in kwargs:
            run_time = int(kwargs['performance_test_lib__run_time'])
            del kwargs['performance_test_lib__run_time']

        throw_result = False
        if 'performance_test_lib__throw_result' in kwargs:
            throw_result = kwargs['performance_test_lib__throw_result']
            del kwargs['performance_test_lib__throw_result']

        clock_type = ClockType.perf_counter
        if 'performance_test_lib__clock_type' in kwargs:
            clock_type = kwargs['performance_test_lib__clock_type']
            del kwargs['performance_test_lib__clock_type']

        with test_performance(test_name, run_time, throw_result, clock_type) as tracer:
            while tracer.iter():
                testable_function(*args, **kwargs)

    return run_time_test_func


class PrecisePerformanceTestTracer(Tracer):
    """
    Precise tracer.
    At first you need to use it as a usual Tracer. After tracing was done - use it as a fast `for i in range(...)` block

    Example of use:

        tr = PrecisePerformanceTestTracer(10.0)
        while tr.iter():
            i = '456'
            k = int('1243' + i)

        with tr as fast_iter:
            for i in fast_iter:
                i = '456'
                k = int('1243' + i)

        print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))

    """

    def __init__(self,
                 run_time: float,
                 clock_type: ClockType=ClockType.perf_counter,
                 suppress_exceptions: bool=False,
                 turn_off_gc: bool=False
                 ):
        super().__init__(run_time, clock_type)
        self.suppress_exceptions = suppress_exceptions
        self.turn_off_gc = turn_off_gc

    def __enter__(self):
        self._relevant_start_time = self._start_time = self._relevant_stop_time = self._end_time = self._clock()
        self._relevant_number_of_iterations_at_start = 0
        if self.turn_off_gc:
            gc.disable()
        return range(self._last_tracked_number_of_iterations)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._relevant_stop_time = self._end_time = self._clock()
        if self.turn_off_gc:
            gc.enable()
        if self.suppress_exceptions:
            return True
