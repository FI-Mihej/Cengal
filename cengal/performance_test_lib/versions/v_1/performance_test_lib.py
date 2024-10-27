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
from cengal.code_flow_control.gc import DisableGC
from contextlib import contextmanager
from cengal.code_flow_control.smart_values.versions.v_2 import ValueExistence
from cengal.code_flow_control.context_management import Combine, Conditional
from cengal.time_management.cpu_clock_cycles import perf_counter
from cengal.time_management.load_best_timer import process_time
from cengal.time_management.repeat_for_a_time import Tracer, ClockType
from cengal.math.numbers import RationalNumber
from cengal.introspection.inspect import func_name, is_async, entity_properties, current_entity, entity_class
# from cengal.code_inspection.auto_line_tracer.versions.v_0 import alt, LineType, OutputFields, AutoLineTracer
from cengal.code_inspection.auto_line_tracer import tr, alt, LineType, OutputFields, AutoLineTracer
from cengal.code_inspection.line_tracer import cln

from typing import Union, Callable, Awaitable, List, Optional, Type, Set

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


class PerformanceTestResult(Exception):
    def __init__(self, result):
        super(PerformanceTestResult, self).__init__()
        self.result = result


@contextmanager
def test_run_time(test_name: str, number_of_iterations: int, throw_result: bool=False, throw_result_anyway: bool=True, ignore_index=False):
    from cengal.parallel_execution.coroutines.coro_standard_services.lazy_print.versions.v_0.lazy_print import lprint

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
            text_result = f'>>> "{test_name}"\n\tIt took {result_time} seconds to process {number_of_iterations} iterations.\n\tThere are {number_of_iterations / result_time} iterations per second\n'
        else:
            text_result = f'>>> "{test_name}"\n\tIt took {result_time} seconds to process {number_of_iterations} iterations.\n'

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


def measure_time(test_name: str = str()):
    return test_run_time(test_name, 1, ignore_index=True)


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
    print('\t' + 'It took', result_time, 'seconds to process', number_of_iterations, 'iterations.')
    print('\t' + 'There are', iterations_per_time_unit, 'iterations per second')

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

    __slots__ = ('suppress_exceptions', 'turn_off_gc', 'gc_was_enabled', 'while_phase', '_last_tracked_number_of_iterations_buff')

    def __init__(self,
                 run_time: float,
                 clock_type: ClockType=ClockType.perf_counter,
                 suppress_exceptions: bool=False,
                 turn_off_gc: bool=False
                 ):
        super().__init__(run_time, clock_type)
        self.suppress_exceptions = suppress_exceptions
        self.turn_off_gc = turn_off_gc
        self.gc_was_enabled = None
        self.while_phase: int = 0
        self._last_tracked_number_of_iterations_buff: int = None

    def __enter__(self):
        self._relevant_start_time = self._start_time = self._relevant_stop_time = self._end_time = self._clock()
        self._relevant_number_of_iterations_at_start = 0
        if self.turn_off_gc:
            self.gc_was_enabled = gc.isenabled()
            gc.disable()
        
        return range(self._last_tracked_number_of_iterations)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._relevant_stop_time = self._end_time = self._clock()
        if self.turn_off_gc and self.gc_was_enabled:
            gc.enable()
        
        if self.suppress_exceptions:
            return True


class PreciseWhilePerformanceTestTracer(Tracer):
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

    __slots__ = ('suppress_exceptions', 'turn_off_gc', 'gc_was_enabled', 'while_phase', '_last_tracked_number_of_iterations_buff')

    def __init__(self,
                 run_time: float,
                 clock_type: ClockType=ClockType.perf_counter,
                 suppress_exceptions: bool=False,
                 turn_off_gc: bool=False
                 ):
        super().__init__(run_time, clock_type)
        self.suppress_exceptions = suppress_exceptions
        self.turn_off_gc = turn_off_gc
        self.gc_was_enabled = None
        self.while_phase: int = 0
        self._last_tracked_number_of_iterations_buff: int = None

    def __enter__(self):
        self._relevant_start_time = self._start_time = self._relevant_stop_time = self._end_time = self._clock()
        self._relevant_number_of_iterations_at_start = 0
        if self.turn_off_gc:
            self.gc_was_enabled = gc.isenabled()
            gc.disable()
        
        return range(1, 1 + self._last_tracked_number_of_iterations).__iter__().__next__

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._relevant_stop_time = self._end_time = self._clock()
        exception_handled: bool = False
        if exc_type is not None:
            exception_handled = issubclass(exc_type, StopIteration)
        
        if self.turn_off_gc and self.gc_was_enabled:
            gc.enable()
        
        if exception_handled or self.suppress_exceptions:
            return True


class PreciseAutoWhilePerformanceTestTracer:
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

    __slots__ = ('__call__', 'tr', 'suppress_exceptions', 'turn_off_gc', 'gc_was_enabled', 'while_phase', '_beginning_time', '_start_time', '_end_time')

    def __init__(self,
                 run_time: float,
                 clock_type: ClockType=ClockType.perf_counter,
                 suppress_exceptions: bool=False,
                 turn_off_gc: bool=False
                 ):
        print('PreciseAutoWhilePerformanceTestTracer')
        self.tr: Tracer = Tracer(run_time, clock_type)
        self.suppress_exceptions: bool = suppress_exceptions
        self.turn_off_gc = turn_off_gc
        self.gc_was_enabled = None
        self.while_phase: int = 0
        # self._iterations_made_buf = None
        self._beginning_time: float = perf_counter()
        self._start_time: float = None
        self._end_time: float = None
        self.__call__ = self._call_first

    def __enter__(self):
        self.__call__ = self._call_first
        self._beginning_time = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._end_time = perf_counter()
        exception_handled: bool = False
        if exc_type is not None:
            exception_handled = issubclass(exc_type, StopIteration)
        
        if self.turn_off_gc and self.gc_was_enabled:
            gc.enable()

        if exception_handled or self.suppress_exceptions:
            return True

    def _call_first(self):
        result: bool = self.tr.iter()
        if result:
            return result
        else:
            self.while_phase = 1
            # self._iterations_made_buf = self.tr._last_tracked_number_of_iterations
            if self.turn_off_gc:
                self.gc_was_enabled = gc.isenabled()
                gc.disable()
            
            _next = range(1, 1 + self.tr._last_tracked_number_of_iterations).__iter__().__next__
            self.__call__ = _next
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


# try:
#     from .performance_test_lib__cython import PreciseAutoWhilePerformanceTestTracer
# except ImportError:
#     pass


class MeasurePerformanceTraceLine:
    """Example:
        with MeasurePerformanceTraceLine(0.5, turn_off_gc=True) as pt:
            while pt():
                i = '456'
                k = int('1243' + i)


    Returns:
        _type_: _description_
    """    
    __slots__ = ('name', 'measuring_obj', 'depth', 'output_fields', 'line_type', 'line_num', 'do_print', 'auto_line_tracer', 'first_line_num')

    def __init__(self, measuring_time: float, name: str=None, clock_type: ClockType=ClockType.perf_counter, turn_off_gc: bool=False, raise_exceptions: bool = True, 
                 line_type: Optional[LineType] = None, line_num: Optional[Union[int, slice]] = None, output_fields: Optional[Set[OutputFields]] = None, 
                 do_print: Union[bool, Callable] = True, auto_line_tracer: AutoLineTracer = None, depth: int = 1) -> None:
        self.name: str = name
        self.measuring_obj: PreciseAutoWhilePerformanceTestTracer = PreciseAutoWhilePerformanceTestTracer(measuring_time, clock_type, not raise_exceptions, turn_off_gc)
        self.depth: int = depth
        self.output_fields: Set[OutputFields] = None if output_fields is None else output_fields
        self.line_type: LineType = line_type
        self.line_num: Optional[Union[int, slice]] = line_num
        self.do_print: bool = do_print
        self.auto_line_tracer: AutoLineTracer = alt if auto_line_tracer is None else auto_line_tracer
        self.first_line_num: int = None

    def __enter__(self):
        self.first_line_num = cln(self.depth + 1) + 1
        return self.measuring_obj.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        last_line_num = cln(self.depth + 1)
        # last_line_num += 2
        suppress_exc: bool = self.measuring_obj.__exit__(exc_type, exc_val, exc_tb)
        if not self.do_print:
            return suppress_exc

        # print('='*70)
        # if self.name is not None:
        #     print(f'>>> "{self.name}"')

        line_num: Optional[Union[int, slice]] = self.line_num
        line_type: LineType = self.line_type
        if line_type is None:
            if line_num is None:
                line_type = LineType.exact_line
                fln: int = min(self.first_line_num, last_line_num)
                lln: int = max(self.first_line_num, last_line_num)
                line_num = slice(fln, lln)
            else:
                line_type = LineType.relative_line
        
        with Combine(self.auto_line_tracer.different_output_fields(alt.default_output_fields), self.auto_line_tracer.different_print_setting(True)):
            self.auto_line_tracer.pl(self.name, line_type=line_type, line_num=line_num, output_fields=self.output_fields, depth=self.depth + 1)

        if (exc_type is not None) and (not suppress_exc):
            print(f'\t{alt.additional_lines_prefix}Exception: {exc_type}')
            print(f'\t{alt.additional_lines_prefix}Exception value: {exc_val}')
            print(f'\t{alt.additional_lines_prefix}Exception traceback: {exc_tb}')
        
        if self.measuring_obj.iterations_made > 1:
            print(f'{alt.additional_lines_prefix}It took {self.measuring_obj.time_spent} seconds to process {self.measuring_obj.iterations_made} iterations')
        else:
            print(f'{alt.additional_lines_prefix}It took {self.measuring_obj.time_spent} seconds')
        
        if self.measuring_obj.time_spent:
            print(f'{alt.additional_lines_prefix}There are {self.measuring_obj.iterations_made / self.measuring_obj.time_spent} iterations/seconds')
        
        print()
        return suppress_exc


measure_performance_tl = MeasurePerformanceTraceLine
measure_performance_trace_line = MeasurePerformanceTraceLine
measure_performance_tl = MeasurePerformanceTraceLine
mperformance_tl = MeasurePerformanceTraceLine
mperformancetl = MeasurePerformanceTraceLine


class MeasureTime:
    __slots__ = ('name', 'iterations', 'do_print', 'raise_exceptions', 'start_time', 'stop_time', 'time_spent', 'exc_type', 'exc_value', 'exc_tb')

    def __init__(self, name: str=None, iterations: int = 1, do_print: Union[bool, Callable] = True, raise_exceptions: bool = True):
        self.name: str = name
        self.iterations: int = 1 if iterations < 1 else iterations
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
        self.stop_time = perf_counter()

        self.exc_type = exc_type
        self.exc_value = exc_val
        self.exc_tb = exc_tb

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
                
                if self.iterations > 1:
                    print(f'\t It took {self.time_spent} seconds to process {self.iterations} iterations')
                else:
                    print(f'\t It took {self.time_spent} seconds')
                
                if self.time_spent:
                    print(f'\t There are {self.iterations / self.time_spent} iterations/seconds')
                    print()
            else:
                self.do_print(self)
        
        return not self.raise_exceptions


class MeasureTimeTraceLine:
    __slots__ = ('measuring_class', 'measuring_obj', 'depth', 'output_fields', 'line_type', 'line_num', 'auto_line_tracer', 'first_line_num', 'last_line_num')

    def __init__(self, name: str=None, iterations: int = 1, raise_exceptions: bool = True, measuring_class: Type = MeasureTime, 
                 line_type: Optional[LineType] = None, line_num: Optional[Union[int, slice]] = None, output_fields: Optional[Set[OutputFields]] = None, 
                 do_print: Union[bool, Callable] = True, auto_line_tracer: AutoLineTracer = None, depth: int = 1):
        self.measuring_class: Type = measuring_class
        self.measuring_obj: MeasureTime = self.measuring_class(name, iterations, self.printer if do_print is True else do_print, raise_exceptions)
        self.depth: int = depth
        self.output_fields: Set[OutputFields] = None if output_fields is None else output_fields
        self.line_type: LineType = line_type
        self.line_num: Optional[Union[int, slice]] = line_num
        self.auto_line_tracer: AutoLineTracer = alt if auto_line_tracer is None else auto_line_tracer
        self.first_line_num: int = None
        self.last_line_num: int = None
    
    def printer(self, measuring_obj: MeasureTime) -> None:
        # print('='*70)
        # if self.measuring_obj.name is not None:
        #     print(f'>>> "{measuring_obj.name}"')

        line_num: Optional[Union[int, slice]] = self.line_num
        line_type: LineType = self.line_type
        if line_type is None:
            if line_num is None:
                line_type = LineType.exact_line
                fln: int = min(self.first_line_num, self.last_line_num)
                lln: int = max(self.first_line_num, self.last_line_num)
                line_num = slice(fln, lln)
            else:
                line_type = LineType.relative_line
        
        with Combine(self.auto_line_tracer.different_output_fields(alt.default_output_fields), self.auto_line_tracer.different_print_setting(True)):
            self.auto_line_tracer.pl(measuring_obj.name, line_type=line_type, line_num=line_num, output_fields=self.output_fields, depth=self.depth + 3)

        if measuring_obj.exc_type is not None:
            print(f'\t{alt.additional_lines_prefix}Exception: {measuring_obj.exc_type}')
            print(f'\t{alt.additional_lines_prefix}Exception value: {measuring_obj.exc_value}')
            print(f'\t{alt.additional_lines_prefix}Exception traceback: {measuring_obj.exc_tb}')
        
        if measuring_obj.iterations > 1:
            print(f'{alt.additional_lines_prefix}It took {measuring_obj.time_spent} seconds to process {measuring_obj.iterations} iterations')
        else:
            print(f'{alt.additional_lines_prefix}It took {measuring_obj.time_spent} seconds')
        
        if measuring_obj.time_spent:
            print(f'{alt.additional_lines_prefix}There are {measuring_obj.iterations / measuring_obj.time_spent} iterations/seconds')
        
        print()

    def __enter__(self):
        self.first_line_num = cln(self.depth + 1) + 1
        return self.measuring_obj.__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.last_line_num = cln(self.depth + 1)
        return self.measuring_obj.__exit__(exc_type, exc_val, exc_tb)


measure_time_trace_line = MeasureTimeTraceLine
measure_time_tl = MeasureTimeTraceLine
mtime_tl = MeasureTimeTraceLine
mtimetl = MeasureTimeTraceLine


class MeasureProcessTime:
    __slots__ = ('name', 'iterations', 'do_print', 'raise_exceptions', 'start_time', 'stop_time', 'time_spent', 'exc_type', 'exc_value', 'exc_tb')

    def __init__(self, name: str=None, iterations: int = 1, do_print: Union[bool, Callable] = False, raise_exceptions: bool = True, depth: int = 1):
        self.name: str = name
        self.iterations: int = 1 if iterations < 1 else iterations
        self.do_print: Union[bool, Callable] = do_print
        self.raise_exceptions: bool = raise_exceptions
        self.depth: int = depth
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
                
                if self.iterations > 1:
                    print(f'\t It took {self.time_spent} seconds to process {self.iterations} iterations')
                else:
                    print(f'\t It took {self.time_spent} seconds')
                
                if self.time_spent:
                    print(f'\t There are {self.iterations / self.time_spent} iterations/seconds')
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
            gc_was_enabled = gc.isenabled()
            gc.disable()
        
        while tr.iter():
            func()

        with tr as fast_iter:
            for i in fast_iter:
                func()
    finally:
        if turn_off_gc and gc_was_enabled:
            gc.enable()

    if do_print:
        if isinstance(do_print, bool):
            if name is not None:
                print(f'>>> "{name}": {func_name(func)}()')
            else:
                print(f'>>> {func_name(func)}()')

            print(f'\t It took {tr.time_spent} seconds to make {tr.iterations_made} iterations. Performance: {tr.iter_per_time_unit} iterations/seconds')
        else:
            do_print(func, run_time, name, clock_type, tr)
    
    return tr


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
            gc_was_enabled = gc.isenabled()
            gc.disable()
        
        while tr.iter():
            await afunc

        with tr as fast_iter:
            for i in fast_iter:
                await afunc
    finally:
        if turn_off_gc and gc_was_enabled:
            gc.enable()

    if do_print:
        if isinstance(do_print, bool):
            if name is not None:
                print(f'>>> "{name}": {func_name(afunc)}()')
            else:
                print(f'>>> {func_name(afunc)}()')

            print(f'\t It took {tr.time_spent} seconds to make {tr.iterations_made} iterations. Performance: {tr.iter_per_time_unit} iterations/seconds')
        else:
            do_print(afunc, run_time, name, clock_type, tr)
    
    return tr


def measure_func_isolated_performance(func: Callable, 
                    run_time: float,
                    name: str=None, 
                    do_print: Union[bool, Callable] = False, 
                    clock_type: ClockType=ClockType.perf_counter,
                    suppress_exceptions: bool=False,
                    turn_off_gc: bool=False
                   ):
    """Measure functions best/top/isolated performance. Hopefully isolated from an interference with other threads executed on the same CPU core

    Args:
        func (Callable): _description_
        run_time (float): _description_
        name (str, optional): _description_. Defaults to None.
        do_print (Union[bool, Callable], optional): _description_. Defaults to False.
        clock_type (ClockType, optional): _description_. Defaults to ClockType.perf_counter.
        suppress_exceptions (bool, optional): _description_. Defaults to False.
        turn_off_gc (bool, optional): _description_. Defaults to False.
    """    
    tr = PrecisePerformanceTestTracer(run_time, clock_type, suppress_exceptions, turn_off_gc)
    measurements: List[float] = list()
    try:
        if turn_off_gc:
            gc_was_enabled = gc.isenabled()
            gc.disable()
        
        while tr.iter():
            func()

        with tr as fast_iter:
            for i in fast_iter:
                start_time = perf_counter()
                func()
                measurements.append(perf_counter() - start_time)
    finally:
        if turn_off_gc and gc_was_enabled:
            gc.enable()

    if do_print:
        best_measurement: float = min(measurements)
        best_performance: Optional[float] = (1 / best_measurement) if best_measurement else None
        if isinstance(do_print, bool):
            if name is not None:
                print(f'>>> "{name}": {func_name(func)}()')
            else:
                print(f'>>> {func_name(func)}()')

            print(f'\t It took {tr.time_spent} seconds to make {tr.iterations_made} iterations. Performance: {tr.iter_per_time_unit} iterations/seconds')
            print(f'\t Isolated run time: {best_measurement} seconds; Isolated performance: {best_performance} iterations/seconds')
        else:
            do_print(func, run_time, name, clock_type, tr, best_measurement, best_performance)
    
    return tr


async def measure_afunc_isolated_performance(afunc: Awaitable, 
                    run_time: float,
                    name: str=None, 
                    do_print: Union[bool, Callable] = False, 
                    clock_type: ClockType=ClockType.perf_counter,
                    suppress_exceptions: bool=False,
                    turn_off_gc: bool=False
                   ):
    """Measure functions best/top/isolated performance. Hopefully isolated from an interference with other threads executed on the same CPU core

    Args:
        afunc (Awaitable): _description_
        run_time (float): _description_
        name (str, optional): _description_. Defaults to None.
        do_print (Union[bool, Callable], optional): _description_. Defaults to False.
        clock_type (ClockType, optional): _description_. Defaults to ClockType.perf_counter.
        suppress_exceptions (bool, optional): _description_. Defaults to False.
        turn_off_gc (bool, optional): _description_. Defaults to False.
    """    
    tr = PrecisePerformanceTestTracer(run_time, clock_type, suppress_exceptions, turn_off_gc)
    measurements: List[float] = list()
    try:
        if turn_off_gc:
            gc_was_enabled = gc.isenabled()
            gc.disable()
        
        while tr.iter():
            await afunc

        with tr as fast_iter:
            for i in fast_iter:
                start_time = perf_counter()
                await afunc
                measurements.append(perf_counter() - start_time)
    finally:
        if turn_off_gc and gc_was_enabled:
            gc.enable()

    if do_print:
        best_measurement: float = min(measurements)
        best_performance: Optional[float] = (1 / best_measurement) if best_measurement else None
        if isinstance(do_print, bool):
            if name is not None:
                print(f'>>> "{name}": {func_name(afunc)}()')
            else:
                print(f'>>> {func_name(afunc)}()')

            print(f'\t It took {tr.time_spent} seconds to make {tr.iterations_made} iterations. Performance: {tr.iter_per_time_unit} iterations/seconds')
            print(f'\t Isolated run time: {best_measurement} seconds; Isolated performance: {best_performance} iterations/seconds')
        else:
            do_print(afunc, run_time, name, clock_type, tr, best_measurement, best_performance)
    
    return tr
