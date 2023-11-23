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
from cengal.time_management.load_best_timer import perf_counter, process_time
from cengal.time_management.repeat_for_a_time import Tracer, ClockType
from cengal.math.numbers import RationalNumber
from cengal.introspection.inspect import is_async
from cengal.introspection.inspect import func_name, entity_properties
from typing import Union, Callable, Awaitable

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


def test_function_run_time(
        test_name: str = None,
        iterations_qnt: int = None,
        throw_result: bool = None,
    ):
    """
    Use 'performance_test_lib__iterations_qnt=1000000' parameter to pass number of iterations
    :param testable_function: function
    :return:
    """
    def wrapper(testable_function):
        if is_async(testable_function):
            async def sub_wrapper(*args, **kwargs):
                test_name_ = '' if test_name is None else test_name
                test_full_name = '{}: {}'.format(str(testable_function), test_name_)
                number_of_iterations = 1 if iterations_qnt is None else iterations_qnt
                throw_result_ = False if throw_result is None else throw_result
                with test_run_time(test_full_name, number_of_iterations, throw_result_) as index:
                    while index.value > 0:
                        await testable_function(*args, **kwargs)
                        index.value -= 1
            
            return sub_wrapper
        else:
            def sub_wrapper(*args, **kwargs):
                test_name_ = '' if test_name is None else test_name
                test_full_name = '{}: {}'.format(str(testable_function), test_name_)
                number_of_iterations = 1 if iterations_qnt is None else iterations_qnt
                throw_result_ = False if throw_result is None else throw_result
                with test_run_time(test_full_name, number_of_iterations, throw_result_) as index:
                    while index.value > 0:
                        testable_function(*args, **kwargs)
                        index.value -= 1
            
            return sub_wrapper
    return wrapper


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


def test_function_performance(
        test_name: str = None,
        run_time: RationalNumber = None,
        throw_result: bool = None,
        clock_type: ClockType = None,
    ):
    """
    Use 'performance_test_lib__run_time=1.5' parameter to pass number of seconds to test
    :param testable_function: function
    :return:
    """
    def wrapper(testable_function):
        if is_async(testable_function):
            async def sub_wrapper(*args, **kwargs):
                test_name_ = '' if test_name is None else test_name
                full_test_name = '{}: {}'.format(str(testable_function), test_name_)
                run_time_ = 1.0 if run_time is None else run_time
                throw_result_ = False if throw_result is None else throw_result
                clock_type_ = ClockType.perf_counter if clock_type is None else clock_type
                with test_performance(full_test_name, run_time_, throw_result_, clock_type_) as tracer:
                    while tracer.iter():
                        await testable_function(*args, **kwargs)
            
            return sub_wrapper
        else:
            def sub_wrapper(*args, **kwargs):
                test_name_ = '' if test_name is None else test_name
                full_test_name = '{}: {}'.format(str(testable_function), test_name_)
                run_time_ = 1.0 if run_time is None else run_time
                throw_result_ = False if throw_result is None else throw_result
                clock_type_ = ClockType.perf_counter if clock_type is None else clock_type
                with test_performance(full_test_name, run_time_, throw_result_, clock_type_) as tracer:
                    while tracer.iter():
                        testable_function(*args, **kwargs)
            
            return sub_wrapper
    return wrapper


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


class MeasureTime:
    def __init__(self, name: str=None, do_print: Union[bool, Callable] = True, raise_exceptions: bool = True):
        self.name = name
        self.do_print: Union[bool, Callable] = do_print
        self.raise_exceptions: bool = raise_exceptions
        self.start_time = None
        self.stop_time = None
        self.time_spent = None
        self.exc_type = None
        self.exc_value = None
        self.exc_tb = None

    def __enter__(self):
        self.start_time = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exc_type = exc_type
        self.exc_value = exc_val
        self.exc_tb = exc_tb

        self.stop_time = perf_counter()
        self.time_spent = self.stop_time - self.start_time
        if self.do_print:
            if isinstance(self.do_print, bool):
                if self.name is not None:
                    print(f'>>> "{self.name}"')
                else:
                    print('>>>')

                if self.exc_type is not None:
                    print(f'\t Exception: {self.exc_type}')
                    print(f'\t Exception value: {self.exc_value}')
                    print(f'\t Exception traceback: {self.exc_tb}')
                
                print(f'\t It was used {self.time_spent} seconds')
                if self.time_spent:
                    print(f'\t It is {1 / self.time_spent} iterations/seconds')
                    print()
            else:
                self.do_print(self)
        
        return not self.raise_exceptions


class MeasureProcessTime:
    def __init__(self, name: str=None, do_print: Union[bool, Callable] = False, raise_exceptions: bool = True):
        self.name = name
        self.do_print: Union[bool, Callable] = do_print
        self.raise_exceptions: bool = raise_exceptions
        self.start_time = None
        self.stop_time = None
        self.time_spent = None
        self.exc_type = None
        self.exc_value = None
        self.exc_tb = None

    def __enter__(self):
        self.start_time = process_time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exc_type = exc_type
        self.exc_value = exc_val
        self.exc_tb = exc_tb

        self.stop_time = process_time()
        self.time_spent = self.stop_time - self.start_time
        if self.do_print:
            if isinstance(self.do_print, bool):
                if self.name is not None:
                    print(f'>>> "{self.name}"')
                else:
                    print('>>>')

                if self.exc_type is not None:
                    print(f'\t Exception: {self.exc_type}')
                    print(f'\t Exception value: {self.exc_value}')
                    print(f'\t Exception traceback: {self.exc_tb}')
                
                print(f'\t It was used {self.time_spent} seconds')
                if self.time_spent:
                    print(f'\t It is {1 / self.time_spent} iterations/seconds')
                    print()
            else:
                self.do_print(self)
        
        return not self.raise_exceptions


def measure_func_performance(func: Callable, 
                    run_time: float,
                    name: str=None, 
                    do_print: Union[bool, Callable] = False, 
                    clock_type: ClockType=ClockType.perf_counter,
                    suppress_exceptions: bool=False,
                    turn_off_gc: bool=False
                   ):
    tr = PrecisePerformanceTestTracer(run_time, clock_type, suppress_exceptions, turn_off_gc)
    try:
        if turn_off_gc:
            gc.disable()
        
        while tr.iter():
            func()

        with tr as fast_iter:
            for i in fast_iter:
                func()
    finally:
        if turn_off_gc:
            gc.enable()

    if do_print:
        if isinstance(do_print, bool):
            if name is not None:
                print(f'>>> "{name}": {func_name(func)}()')
            else:
                print(f'>>> {func_name(func)}()')

            print(f'\t It was used {tr.time_spent} seconds to make {tr.iterations_made} iterations. Performance: {tr.iter_per_time_unit} iterations/seconds')
        else:
            do_print(func, run_time, name, clock_type, tr)


async def measure_afunc_performance(afunc: Awaitable, 
                    run_time: float,
                    name: str=None, 
                    do_print: Union[bool, Callable] = False, 
                    clock_type: ClockType=ClockType.perf_counter,
                    suppress_exceptions: bool=False,
                    turn_off_gc: bool=False
                   ):
    tr = PrecisePerformanceTestTracer(run_time, clock_type, suppress_exceptions, turn_off_gc)
    try:
        if turn_off_gc:
            gc.disable()
        
        while tr.iter():
            await afunc

        with tr as fast_iter:
            for i in fast_iter:
                await afunc
    finally:
        if turn_off_gc:
            gc.enable()

    if do_print:
        if isinstance(do_print, bool):
            if name is not None:
                print(f'>>> "{name}": {func_name(afunc)}()')
            else:
                print(f'>>> {func_name(afunc)}()')

            print(f'\t It was used {tr.time_spent} seconds to make {tr.iterations_made} iterations. Performance: {tr.iter_per_time_unit} iterations/seconds')
        else:
            do_print(afunc, run_time, name, clock_type, tr)
