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


__all__ = ['CallState', 'ResultAlreadyRegisteredError', 'ExceptionAlreadyRegisteredError', 'CallStackIsNotEqualError', 
           'ExpectedTestCaseStateIsNotLoadedError', 'TEST_CASE_STATE', 'get_test_case_state', 'TestCaseState']


import datetime
import inspect
import json
import logging
import os
import traceback
import unittest
import pickle
from contextlib import contextmanager
from types import FrameType
from typing import Any, Dict, List, NoReturn, Optional, Set, Tuple, Union, Hashable, cast, ContextManager, Callable, Awaitable, OrderedDict
from cengal.code_flow_control.smart_values import ValueHolder
from cengal.introspection.inspect import CodeParamsWithValues, intro_func_params_with_values, find_current_entity, find_entity, is_async, \
    intro_frame_params_with_values, entity_class, get_exception, func_params_with_values
from cengal.file_system.path_manager import relative_to_src, RelativePath
from collections import namedtuple, OrderedDict
from functools import wraps, update_wrapper


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


VarName = str
VarValue = Any
MeasurementId = int
StageId = Hashable


def param(param_name: str) -> str:
    """
    Returns a formatted full name of the parameter: 'ClassName__m__MethodName__p__ParameterName'

    Returns:
    str: furmatted full name of the parameter
    """
    frame = cast(FrameType, inspect.currentframe()).f_back
    real_func = cast(FrameType, inspect.currentframe()).f_back.f_code
    func_name = real_func.co_name
    args, _, _, values = inspect.getargvalues(frame)
    parent_obj = None
    for par_name, par_val in [(i, values[i]) for i in args]:
        if 'self' == par_name:
            parent_obj = par_val
            break  # TODO: check if it is needed
    
    class_name = str()
    if parent_obj is not None:
        class_name = type(parent_obj).__name__
    
    param_full_name = f'{class_name}__m__{func_name}__p__{param_name}'
    return param_full_name


def param2(param_name: str) -> str:
    raise NotImplementedError


FAKE_RESULTS: 'FakeResults' = cast('FakeResults', None)


def get_fake_results() -> 'FakeResults':
    global FAKE_RESULTS
    if FAKE_RESULTS is None:
        FAKE_RESULTS = FakeResults()
    return FAKE_RESULTS


class ParameterIsNotInNotInTheListOfExpectedResultsError(Exception):
    """
    Will be raised by FakeResults.check_result() when `param_name not in self.expected_results`
    """
    pass


class ResultNumberIsNotValidError(Exception):
    """
    Will be raised by FakeResults.check_result() when `result_number not in self.expected_results[param_name]`
    """
    pass


class FakeResults:
    """
    Holds a both an actual and a refference (an expected) results and compares them

    Saves a taken results as a refference 'expected_results' to a json file on FakeResults.try_to_save_expected_results() if 
    this file was not already loaded by the FakeResults.try_to_load_expected_results() method.

    So if FakeResults.try_to_load_expected_results() will be called before all tests and FakeResults.try_to_save_expected_results()
    will be called after all tests:
        1) At a first iteration it will take all generated results and will save them to the json file as a refference (as an expected_results).
        This step must be made on a developers' machine. Resulting json file must be added to the repository.
        2) At all further calls it will find json file exists and will load it's content as a refference (as an expected_results).
    
    Can be used as a 'with' context manager which will try to load json file at the start and will try to save a refference to the json file
    at the end (if json file wasn't loaded at the start).

    Raises:
        NotImplementedError: _description_
        NotImplementedError: _description_
        NotImplementedError: _description_
        NotImplementedError: _description_
        NotImplementedError: _description_
        NotImplementedError: _description_
        NotImplementedError: _description_
    """
    
    def __init__(self, content_full_file_name: str) -> None:
        self.was_loaded = False
        self.results: Dict[str, Dict[int, str]] = dict()
        self.expected_results: Dict[str, Dict[int, str]] = dict()
        self.content_full_file_name = content_full_file_name
        self.old_global_fake_result: 'FakeResults' = cast('FakeResults', None)
    
    def add_result(self, param_name: str, result: Any) -> None:
        """
        Will add a result to a list of the results for a requested parameter

        For example we have a function:
            def add_int(a: int, b: int) -> int:
                return a + b
        
        Then we can change it in the next way:
            def add_int(a: int, b: int) -> int:
                result = a + b
                get_fake_results().add_result(param('a'), a)
                get_fake_results().add_result(param('b'), b)
                # get_fake_results().add_result(param('->'), result)  # TODO: check if it is needed
                return result
        
        As result we will save all 'a' and 'b' parameters of an each 'add_int()' call to an ordered sequence and will
        be able to compare them with a refference values by the calling FakeResults.check_result(), FakeResults.check_results_range() or FakeResults.check_all_results()

        Parameters:
        param_name (str): your parameter name
        result (Any): current parameters' content
        """
        result = str(result)
        if param_name not in self.results:
            self.results[param_name] = dict()
        
        index = 0
        if self.results[param_name]:
            index = max(self.results[param_name].keys()) + 1
        
        self.results[param_name][index] = result
    
    def add_expected_result(self, param_name: str, expected_result: Any) -> None:
        """
        Will add single expected result for the parameter
        
        Parameters:
        param_name (str): your parameter name
        expected_result (Any): expected parameters' content
        """
        expected_result = str(expected_result)
        if param_name not in self.expected_results:
            self.expected_results[param_name] = dict()
        
        index = 0
        if self.expected_results[param_name]:
            index = max(self.expected_results[param_name].keys()) + 1
        
        self.expected_results[param_name][index] = expected_result

    def register_param_expected_results(self, param_name: str, expected_results: List[Any]) -> None:
        """
        Will register a list of expected results for the parameter
        Will add a list of expected results for the parameter
        
        Parameters:
        param_name (str): your parameter name
        expected_results (List[Any]): list of expected parameters' content
        """
        for expected_result in expected_results:
            self.add_expected_result(param_name, expected_result)
    
    def register_expected_results(self, expected_results: Dict[str, Dict[int, str]]) -> None:
        """
        Will register a dict of expected results for all requested parameters

        Parameters:
        expected_results (Dict[str, Dict[int, str]]): key - parameter name; value.key - index of the expected parameter's
        content; value.value - expected parameter's content
        """
        self.expected_results = expected_results
    
    def check_result(self, param_name: str, result_number: Optional[int] = None) -> bool:
        """
        Will compare requested parameter's result with an expected result. if result_number is not None -  will compare
        exact items in a sequence instead of comparing all expected results.
        Will return True to an each call until json file will be loaded with a 'FakeResults.try_to_load_expected_results()' call.

        Returns:
        bool: True if result is equal to an expected result
        """
        if not self.was_loaded:
            return True
        
        if param_name not in self.expected_results:
            raise ParameterIsNotInNotInTheListOfExpectedResultsError(param_name)
        
        if param_name not in self.results:
            print(f'ERROR: PARAM NOT IN RESULTS: {param_name}')
            return False

        if result_number is not None:
            if result_number not in self.expected_results[param_name]:
                raise ResultNumberIsNotValidError((param_name, result_number))
            
            if result_number not in self.results[param_name]:
                print(f'ERROR: PARAM\'S RESULT NUMBER {result_number} NOT IN RESULTS: {param_name}')
                return False

        if result_number is None:
            returned_val: Any = self.results[param_name]
            expected_val: Any = self.expected_results[param_name]
        else:
            returned_val: Any = self.results[param_name][result_number]
            expected_val: Any = self.expected_results[param_name][result_number]
        
        if returned_val == expected_val:
            return True
        else:
            print(f'ERROR: PARAM IS NOT EQUAL TO EXPECTED: {param_name}\n\tRETURNED VAL: {returned_val}\n\tEXPECTED VAL: {expected_val}\n~~~~~~~~~~~~~~~~~~~~~~~~~')
            # return False  # TODO: check if it is needed
    
    def check_results_range(self, param_name: str, result_number_from: int, result_number_up_to: int) -> bool:
        """
        Will compare a range of requested parameters' results with an expected results.
        Will return True to an each call until json file will be loaded with a 'FakeResults.try_to_load_expected_results()' call.
        Behavior of the 'results_number_from' and 'results_number_up_to' parameters is the same as in the 'range()' call.

        Parameters:
        param_name (str): your parameter name
        result_number_from (int): start index of the results range
        result_number_up_to (int): end index of the results range

        Returns:
        bool: True if all results in the range are equal to an expected results
        """
        for result_number in range(result_number_from, result_number_up_to):
            if not self.check_result(param_name, result_number=result_number):
                return False
        
        return True

    def check_current_results(self) -> bool:
        """
        Will compare all requested parameters' results with an expected results.
        Will return True to an each call until json file will be loaded with a 'FakeResults.try_to_load_expected_results()' call.

        Returns:
        bool: True if all results are equal to an expected results
        """
        for param_name, _ in self.results.items():
            if not self.check_result(param_name):
                return False
        
        return True

    def check_all_results(self) -> bool:
        """
        Will compare all requested parameters' results with an expected results.
        Will return True to an each call until json file will be loaded with a 'FakeResults.try_to_load_expected_results()' call.

        Returns:
        bool: True if all results are equal to an expected results
        """
        for param_name, _ in self.expected_results.items():
            if not self.check_result(param_name):
                return False
        
        return True

    def try_to_load_expected_results(self, full_file_name: str) -> None:
        """
        Will try to load a json file with a refference results (an expected_results)
        
        Parameters:
        full_file_name (str): full file name of the json file with a refference results (an expected_results)
        """
        if os.path.exists(full_file_name) and os.path.isfile(full_file_name):
            content = None
            with open(full_file_name, 'rb') as file:
                content = file.read()
            
            if content:
                content_str = content.decode('utf-8')
                expected_results = json.loads(content_str)
                for param, values in expected_results.items():
                    if param not in self.expected_results:
                        self.expected_results[param] = dict()
                    
                    for index_str, value in values.items():
                        index = int(index_str)
                        self.expected_results[param][index] = value
                
                self.was_loaded = True
    
    def try_to_save_expected_results(self, full_file_name: str) -> None:
        """
        Will try to save a refference results (an expected_results) to a json file. Will not save them if 
        json file was already successfully loaded with a 'FakeResults.try_to_load_expected_results()' call.

        Parameters:
        full_file_name (str): full file name of the json file with a refference results (an expected_results)
        """
        if self.was_loaded:
            return
        
        if not (os.path.exists(full_file_name) and os.path.isfile(full_file_name)):
            content = json.dumps(self.results)
            content = json.dumps(json.loads(content), indent=4)
            content_bytes = content.encode('utf-8')
            with open(full_file_name, 'wb+') as file:  # TODO: check if '+' in 'wb+' is needed
                file.write(content_bytes)
    
    def register(self):
        """
        Will register current instance to a global 'FAKE_RESULTS' variable. Will save a previous value
        """
        self.try_to_load_expected_results(self.content_full_file_name)

        global FAKE_RESULTS
        self.old_global_fake_result = FAKE_RESULTS
        FAKE_RESULTS = self
    
    def __enter__(self):
        self.register()
        return self

    def unregister(self, should_be_saved: bool):
        """
        Will restore a previous value of the global 'FAKE_RESULTS' variable
        """
        global FAKE_RESULTS
        FAKE_RESULTS = self.old_global_fake_result

        if should_be_saved:
            self.try_to_save_expected_results(self.content_full_file_name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.unregister((exc_type is None) and (exc_val is None) and (exc_tb is None))
        return False


CallState = namedtuple("CallState", "entity params_with_values args kwargs result_holder exception_holder")


class ResultAlreadyRegisteredError(Exception):
    pass


class ExceptionAlreadyRegisteredError(Exception):
    pass


class CallStackIsNotEqualError(Exception):
    pass


class ExpectedTestCaseStateIsNotLoadedError(Exception):
    pass


TEST_CASE_STATE: 'TestCaseState' = cast('TestCaseState', None)


def get_test_case_state() -> 'TestCaseState':
    global TEST_CASE_STATE
    if TEST_CASE_STATE is None:
        TEST_CASE_STATE = TestCaseState('Default')
    
    return TEST_CASE_STATE


class TestCaseState:
    def __init__(self, name: Optional[str] = None, raise_exceptions: bool = True, register: bool = True, depth: Optional[int] = 1):
        if name is None:
            parent_entity = find_current_entity(depth + 1)
            parent_class = entity_class(parent_entity)
            parent_class_name: str = parent_class.__name__

        self.name: str = name or parent_class_name
        self.raise_exceptions: bool = raise_exceptions
        self._current_test_id: Hashable = None
        self.call_stack_per_test: OrderedDict[Hashable, List[CallState]] = OrderedDict({
            None: list()
        })
        self.expected_call_stack_per_test: OrderedDict[Hashable, List[CallState]] = OrderedDict({
            None: list()
        })
        self.loaded: bool = False
        self.content_file_name: str = f'{self.name}__test_case_state.pickle'
        self.readable_content_file_name: str = f'{self.name}__test_case_state.md'
        self.content_dir_rel: RelativePath = relative_to_src(depth + 1)
        self.content_full_file_name: str = self.content_dir_rel(self.content_file_name)
        self.readable_content_full_file_name: str = self.content_dir_rel(self.readable_content_file_name)
        self.old_global_fake_result: 'TestCaseState' = cast('TestCaseState', None)
        if register:
            self.register()

    @property
    def current_test_id(self) -> Hashable:
        return self._current_test_id
    
    @current_test_id.setter
    def current_test_id(self, value: Hashable) -> None:
        self._current_test_id = value
        if value not in self.call_stack_per_test:
            self.call_stack_per_test[value] = list()
    
    @property
    def call_stack(self) -> List[CallState]:
        return self.call_stack_per_test[self.current_test_id]
    
    @property
    def expected_call_stack(self) -> List[CallState]:
        try:
            return self.expected_call_stack_per_test[self.current_test_id]
        except KeyError:
            return list()

    def is_loaded(self) -> bool:
        if not self.loaded:
            raise ExpectedTestCaseStateIsNotLoadedError(f'Expected test case state is not loaded: {self.name}')
    
    def check_current_state_item(self):
        self.is_loaded()
        call_stack_item: CallState = self.call_stack[-1]
        expected_call_stack_item: CallState = self.expected_call_stack[len(self.call_stack) - 1]
        if call_stack_item != expected_call_stack_item:
            raise CallStackIsNotEqualError(f'Expected call stack item: {expected_call_stack_item}\nCurrent call stack item: {call_stack_item}')
    
    def check_state_item(self, item_index: int):
        self.is_loaded()
        call_stack_item: CallState = self.call_stack[item_index]
        expected_call_stack_item: CallState = self.expected_call_stack[item_index]
        if call_stack_item != expected_call_stack_item:
            raise CallStackIsNotEqualError(f'Index: {item_index}\nExpected call stack item: {expected_call_stack_item}\nActual call stack item: {call_stack_item}')
    
    def check_state_range(self, item_start_index: int, item_end_index: int):
        self.is_loaded()
        call_stack_part: List[CallState] = self.call_stack[item_start_index: item_end_index]
        expected_call_stack_part: List[CallState] = self.expected_call_stack[item_start_index: item_end_index]
        if call_stack_part != expected_call_stack_part:
            raise CallStackIsNotEqualError(f'Index: [{item_start_index}:{item_end_index}]\nExpected call stack part: {expected_call_stack_part}\nActual call stack part: {call_stack_part}')
    
    def check_current_state(self):
        self.is_loaded()
        expected_call_stack_part: List[CallState] = self.expected_call_stack[:len(self.call_stack)]
        if self.call_stack != expected_call_stack_part:
            raise CallStackIsNotEqualError(f'Expected call stack: {expected_call_stack_part}\nActual call stack: {self.call_stack}')

    def check_whole_state(self):
        self.is_loaded()
        if self.call_stack != self.expected_call_stack:
            raise CallStackIsNotEqualError(f'Expected call stack: {self.expected_call_stack}\nActual call stack: {self.call_stack}')

    def check_all_tests_state(self):
        self.is_loaded()
        if self.call_stack_per_test != self.expected_call_stack_per_test:
            raise CallStackIsNotEqualError(f'Expected call stacks: {self.expected_call_stack_per_test}\nActual call stacks: {self.call_stack_per_test}')

    def register_intro(self, raise_exceptions: Optional[bool] = None) -> ContextManager:
        def context_manager(self: 'TestCaseState'):
            current_entity: Callable = find_current_entity(2)
            code_params_with_values: CodeParamsWithValues = intro_func_params_with_values(2)
            result_holder: ValueHolder = ValueHolder()
            exception_holder: ValueHolder = ValueHolder()
            try:
                yield result_holder
            except:
                exception_holder.value = get_exception()
                if raise_exceptions or ((raise_exceptions is None) and self.raise_exceptions):
                    raise
            finally:
                current_call_state: CallState = CallState(current_entity, code_params_with_values, result_holder, exception_holder)
                self.call_stack.append(current_call_state)
                self.check_current_state_item()
        
        return context_manager(self)
    
    ri = register_intro
    
    def register_outro(self, func: Callable, raise_exceptions: Optional[bool] = None) -> Callable:
        original_func: Callable = func
        if hasattr(original_func, 'cr_frame'):
            original_func = find_entity(original_func.cr_frame)

        if is_async(func):
            if inspect.isawaitable(func):
                async def awaitable_wrapper() -> Any:
                    current_entity: Awaitable = func
                    if hasattr(current_entity, 'cr_frame'):
                        # code_params_with_values: CodeParamsWithValues = intro_frame_params_with_values(current_entity.cr_frame)
                        code_params_with_values, result_args, result_kwargs = func_params_with_values(find_entity(original_func.cr_frame), tuple(), dict())
                        code_params_with_values: CodeParamsWithValues = cast(CodeParamsWithValues, code_params_with_values)
                    else:
                        code_params_with_values: CodeParamsWithValues = CodeParamsWithValues()
                        result_args = tuple()
                        result_kwargs = dict()
                    
                    result_holder: ValueHolder = ValueHolder()
                    exception_holder: ValueHolder = ValueHolder()
                    try:
                        result = await func
                        result_holder.value = result
                        return result
                    except:
                        exception_holder.value = get_exception()
                        if raise_exceptions or ((raise_exceptions is None) and self.raise_exceptions):
                            raise
                    finally:
                        current_call_state: CallState = CallState(current_entity, code_params_with_values, result_args, result_kwargs, result_holder, exception_holder)
                        self.call_stack.append(current_call_state)
                        self.check_current_state_item()
                
                wrapper = awaitable_wrapper()
            else:
                async def async_wrapper(*args, **kwargs) -> Any:
                    current_entity: Callable = func
                    code_params_with_values, result_args, result_kwargs = func_params_with_values(func, args, kwargs)
                    code_params_with_values: CodeParamsWithValues = cast(CodeParamsWithValues, code_params_with_values)
                    result_holder: ValueHolder = ValueHolder()
                    exception_holder: ValueHolder = ValueHolder()
                    try:
                        result = await func(*args, **kwargs)
                        result_holder.value = result
                        return result
                    except:
                        exception_holder.value = get_exception()
                        if raise_exceptions or ((raise_exceptions is None) and self.raise_exceptions):
                            raise
                    finally:
                        current_call_state: CallState = CallState(current_entity, code_params_with_values, result_args, result_kwargs, result_holder, exception_holder)
                        self.call_stack.append(current_call_state)
                        self.check_current_state_item()
                
                wrapper = async_wrapper
        else:
            def sync_wrapper(*args, **kwargs) -> Any:
                current_entity: Callable = func
                code_params_with_values, result_args, result_kwargs = func_params_with_values(func, args, kwargs)
                code_params_with_values: CodeParamsWithValues = cast(CodeParamsWithValues, code_params_with_values)
                result_holder: ValueHolder = ValueHolder()
                exception_holder: ValueHolder = ValueHolder()
                try:
                    result = func(*args, **kwargs)
                    result_holder.value = result
                    return result
                except:
                    exception_holder.value = get_exception()
                    if raise_exceptions or ((raise_exceptions is None) and self.raise_exceptions):
                        raise
                finally:
                    current_call_state: CallState = CallState(current_entity, code_params_with_values, result_args, result_kwargs, result_holder, exception_holder)
                    self.call_stack.append(current_call_state)
                    self.check_current_state_item()
            
            wrapper = sync_wrapper
        
        original_func_sign: inspect.Signature = inspect.signature(original_func)
        update_wrapper(wrapper, original_func)
        wrapper.__signature__ = original_func_sign.replace(parameters=tuple(original_func_sign.parameters.values()), return_annotation=original_func_sign.return_annotation)
        return wrapper
    
    ro = register_outro
    
    def register_last_result(self, result: Any) -> None:
        last_call_state: CallState = self.call_stack[-1]
        result_holder: ValueHolder = last_call_state.result_holder
        if result_holder:
            raise ResultAlreadyRegisteredError(f'For last call state: {last_call_state}')
        
        result_holder.value = result

    rls = register_last_result
    
    def register_last_exception(self, result: Any) -> None:
        last_call_state: CallState = self.call_stack[-1]
        exception_holder: ValueHolder = last_call_state.result_holder
        if exception_holder:
            raise ExceptionAlreadyRegisteredError(f'For last call state: {last_call_state}')
        
        exception_holder.value = result

    rle = register_last_exception

    def try_to_load_expected_call_stack(self) -> None:
        """
        Will try to load a pickle file with a refference results (an expected_results)
        """
        if os.path.exists(self.content_full_file_name) and os.path.isfile(self.content_full_file_name):
            with open(self.content_full_file_name, 'rb') as file:
                self.expected_call_stack_per_test = pickle.load(file)
                self.loaded = True
    
    def try_to_save_expected_call_stack(self) -> None:
        """
        Will try to save a refference results (an expected_results) to a pickle file. Will not save them if 
        pickle file was already successfully loaded with a 'FakeResults.try_to_load_expected_call_stack()' call.
        """
        if self.loaded:
            return
        
        if not (os.path.exists(self.content_full_file_name) and os.path.isfile(self.content_full_file_name)):
            with open(self.content_full_file_name, 'wb') as file:
                pickle.dump(self.call_stack_per_test, file)
        
        if not (os.path.exists(self.readable_content_full_file_name) and os.path.isfile(self.readable_content_full_file_name)):
            with open(self.readable_content_full_file_name, 'wb') as file:
                file.write(self.prepare_readable_content().encode('utf-8'))
    
    def prepare_readable_content(self) -> str:
        content: str = str()
        content += f'# Test Case: {self.name}\n'
        for test_id, call_stack in self.call_stack_per_test.items():
            content += f'\n\n## Test ID: {test_id}\n'
            for index, call_state in enumerate(call_stack):
                content += f'\n\t{index}: {call_state.entity.__name__}\n'
                content += f'\t\t{call_state.params_with_values}\n'
                content += f'\t\targs: {call_state.args}\n'
                content += f'\t\tkwargs: {call_state.kwargs}\n'
                if call_state.result_holder:
                    content += f'\t\tresult: {call_state.result_holder.value}\n'
                if call_state.exception_holder:
                    content += f'\t\texception: {call_state.exception_holder.value}\n'
        
        return content
    
    def register(self):
        """
        Will register current instance to a global 'TEST_CASE_STATE' variable. Will save a previous value
        """
        self.try_to_load_expected_call_stack()

        global TEST_CASE_STATE
        self.old_global_fake_result = TEST_CASE_STATE
        TEST_CASE_STATE = self
    
    def __enter__(self):
        self.register()
        return self

    def unregister(self, should_be_saved: bool = True):
        """
        Will restore a previous value of the global 'TEST_CASE_STATE' variable
        """
        global TEST_CASE_STATE
        TEST_CASE_STATE = self.old_global_fake_result

        if should_be_saved:
            self.try_to_save_expected_call_stack()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.unregister((exc_type is None) and (exc_val is None) and (exc_tb is None))
        return False



class StateBase:
    def add(self, var_name: VarName, var_value: VarValue, stage_id: StageId = None):
        raise NotImplementedError
    
    def add_set(self, vars: Dict[VarName, VarValue]):
        raise NotImplementedError
    
    def check_var(self, var_name: VarName):
        raise NotImplementedError
    
    def check_var_measurement(self, var_name: VarName, measurement_id_from: MeasurementId, measuremente_id_up_to: MeasurementId):
        raise NotImplementedError
    
    def check_var_current_state(self, var_name: VarName):
        raise NotImplementedError
    
    def check_all(self):
        raise NotImplementedError
    
    def check_all_current_state(self):
        raise NotImplementedError
