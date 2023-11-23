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

import sys
import os
import copy
import traceback
from enum import Enum
from contextlib import contextmanager
from cengal.data_generation.id_generator import IDGenerator, GeneratorType
from cengal.code_flow_control.smart_values.versions.v_0.result_types import *

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


class IsOK_BlockFailed(Exception): pass


class IsOK_Closed(Exception):
    """
    is_ok considers it ordinary external exception
    """
    def __init__(self, context_holder, block_id, block_info):
        super(IsOK_Closed, self).__init__('Content Holder is closed. '
                                          'Content Holder ID: {}; '
                                          'Content Holder Info: {}; '
                                          'Block ID: {}; '
                                          'Block Info {}'.format(str(context_holder._context_holder_id),
                                                                 str(context_holder._context_holder_info),
                                                                 str(block_id),
                                                                 str(block_info)))
        self.context_holder = context_holder
        self.block_id = block_id
        self.block_info = block_info


class IsOKForFunction_ParameterNeeded(Exception): pass


class CriteriaType(Enum):
# class CriteriaType():  # much more efficient than Enum inheritance
    needed = 0  # only set of this blocks is needed (should be already successfully done)
    optional = 1  # all blocks are needed except of this set of blocks
    any = 2  # any result will fit criteria
    forbidden = 3  # set of this blocks should be already failed
    not_successful = 4  # set of this blocks should not be successfully done (also may not start) at the check time


class IgnoreBlockResultCriteriaType(Enum):
    do_not_ignore = 0
    ignore_if_failed = 1
    ignore_if_successful = 2


class IsOK_HistoryExport(Exception):
    def __init__(self, history, process_error_result=True):
        super(IsOK_HistoryExport, self).__init__('')
        self.history = history
        self.process_error_result = process_error_result


class IsOK_IntenalResult:
    def __init__(self, type_id, str_data, data):
        self.type_id = type_id
        self.str_data = str_data
        self.data = data

    def __str__(self):
        return self.str_data


class IsOK_IntenalResultType(Enum):
# class CriteriaType():  # much more efficient than Enum inheritance
    built_in_exception__is_ok_block_failed = 0
    built_in_exception__bad_history_import = 1
    external_exception = 2
    block_did_not_returned_an_answer = 3


class IsOK_ContextHolder:
    def __init__(self, context_holder_id=None, context_holder_info=None, global_block_results_criteria=None,
                 raise_exceptions=False, save_debug_trace=False, closeable=True):
        """

        :param context_holder_id:
        :param context_holder_info:
        :param global_block_results_criteria: will be set to ResultType(CriteriaType.optional, set()) if None;
            in this case all blocks are required.
        :param raise_exceptions:
        :param save_debug_trace:
        :param closeable:
        :return:
        """
        # Use only ResultType(CriteriaType.optional, ...) or ResultType(CriteriaType.needed, set()).
        # Other will be ignored here.
        # You may use global_block_results_criteria=ResultType(CriteriaType.optional, set()) to create criteria
        # "no fails in any block"
        self._context_holder_id = context_holder_id
        self._context_holder_info = context_holder_info
        self._internal_blocks_index = IDGenerator()
        self._reserve_block_id_generator = IDGenerator(GeneratorType.guid_string)
        self._criteria_list = list()
        global_block_results_criteria = global_block_results_criteria or ResultType(CriteriaType.optional, set())
        if global_block_results_criteria is not None:
            self._criteria_list.append(global_block_results_criteria)
        self._raise_exceptions = raise_exceptions
        self._save_debug_trace = save_debug_trace
        self._closeable = closeable
        self._full_history = list()
        self._blocks_library = dict()
        self._all_made_blocks = set()
        self._good_blocks = set()
        self._bad_blocks = set()

        self._current_block_id = None
        self._current_block_info = None
        self._current_block_result = None
        self._closed = False

        self._bool_result = ResultCache()

    # def _push_criteria(self, set_of_needed_blocks=None, set_of_optional_blocks=None):
    def _push_criteria(self, block_results_criteria):
        # Do not use!
        self._bool_result()
        self._criteria_list.append(block_results_criteria)

    def _pop_criteria(self):
        # Do not use!
        # May raise exception if len(self.criteria_list)==0, but this is OK.
        self._bool_result()
        return self._criteria_list.pop()

    def read_criteria(self):
        criteria = None
        if self._criteria_list:
            criteria = self._criteria_list[-1]
        return criteria

    def _push_block_info(self, block_id, block_info=None):
        self._current_block_id = block_id
        self._current_block_info = block_info
        self._current_block_result = None

    def _pop_block_info(self):
        self._current_block_id = None
        self._current_block_info = None
        self._current_block_result = None

    def push_result(self, bool_result, info_or_data=None):
        self._current_block_result = (bool_result, info_or_data)

    def push_result_c(self, result):
        # "class" version: to use when result = ResultExistence()
        self._current_block_result = (result.existence, result.result)

    def read_block_result_link(self, block_id):
        # result is NOT protected from changing!
        original_result_data = self._blocks_library[block_id][3]
        result = ResultExistence(original_result_data[0], original_result_data[1])
        # result = self._blocks_library[block_id][3]
        return result

    def read_block_result_copy(self, block_id):
        original_result_data = self._blocks_library[block_id][3]
        result = ResultExistence(original_result_data[0], copy.copy(original_result_data[1]))
        return result

    def read_block_result_deepcopy(self, block_id):
        original_result_data = self._blocks_library[block_id][3]
        result = ResultExistence(original_result_data[0], copy.deepcopy(original_result_data[1]))
        return result

    def _save_block_result(self, ignore_block_result_criteria=None):
        # ignore_block_result_criteria = ignore_block_result_criteria or IgnoreBlockResultCriteriaType.do_not_ignore
        if ((IgnoreBlockResultCriteriaType.ignore_if_failed == ignore_block_result_criteria) and
                (not self._current_block_result[0])) \
                or ((IgnoreBlockResultCriteriaType.ignore_if_successful == ignore_block_result_criteria) and
                        self._current_block_result[0]):
            return

        self._bool_result()
        import_depth = 0
        full_block_info = (self._internal_blocks_index(), self._current_block_id, self._current_block_info,
                           self._current_block_result, import_depth)
        self._full_history.append(full_block_info)
        self._blocks_library[self._current_block_id] = full_block_info
        self._all_made_blocks.add(self._current_block_id)
        if self._current_block_result[0]:
            self._good_blocks.add(self._current_block_id)
        else:
            self._bad_blocks.add(self._current_block_id)

    def __bool__(self):
        if self._bool_result:
            return self._bool_result.get()
        else:
            current_criteria = self.read_criteria()
            result = True
            if CriteriaType.needed == current_criteria:
                if len(current_criteria.result) != len(current_criteria.result & self._good_blocks):
                    result = False
            elif CriteriaType.optional == current_criteria:
                if len(self._bad_blocks - current_criteria.result) != 0:
                    result = False
            elif CriteriaType.any == current_criteria:
                result = True
            elif CriteriaType.forbidden == current_criteria:
                if len(current_criteria.result) != len(current_criteria.result & self._bad_blocks):
                    result = False
            elif CriteriaType.not_successful == current_criteria:
                if len(current_criteria.result & self._good_blocks) != 0:
                    result = False
            self._bool_result.set(result)
            return result

    def __nonzero__(self):
        return self.__bool__()

    @staticmethod
    def _block_list_to_str(block_list):
        blocks_str = ',\n'.join('(index({}), depth({}), ID({}), INFO({}), RESULT({}))'.format(str(block[0]),
                                                                                              str(block[4]),
                                                                                              str(block[1]),
                                                                                              str(block[2]),
                                                          '({}, {})'.format(str(block[3][0]), str(block[3][1])))
                                for block in block_list)
        return blocks_str

    def _block_str_to_context_holder_str(self, blocks_str):
        full_string = '{{{{CONTEXT_HOLDER_ID({}): CONTEXT_HOLDER_INFO({})}}:[\n{}\n]}}'.format(
            self._context_holder_id, self._context_holder_info, blocks_str)
        return full_string

    def get_bad_blocks(self):
        result = list()
        for block in self._full_history:
            if not block[3][0]:
                result.append(block)
        return result

    def get_bad_blocks_str(self):
        bad_blocks = self.get_bad_blocks()
        full_history_str = self._block_list_to_str(bad_blocks)
        full_string = self._block_str_to_context_holder_str(full_history_str)
        return full_string

    def raise_bad_blocks(self):
        raise IsOK_HistoryExport(self.get_bad_blocks())

    def raise_full_history(self):
        raise IsOK_HistoryExport(self._full_history)

    def process_history_import(self, his_ex):
        history = his_ex.history
        for block in history:
            full_block_info = (self._internal_blocks_index.get_new_ID(), block[1], block[2],
                               block[3], block[4] + 1)
            self._full_history.append(full_block_info)

    def close(self):
        self._closed = True

    def _reopen(self):
        self._closed = False

    def __str__(self):
        full_history_str = self._block_list_to_str(self._full_history)
        full_string = self._block_str_to_context_holder_str(full_history_str)
        return full_string

    def __call__(self, *args, **kwargs):
        return is_ok(self, *args, **kwargs)

    def is_ok(self, *args, **kwargs):
        return self.__call__(*args, **kwargs)


@contextmanager
def is_ok(context_holder, block_id, block_info=None, block_results_criteria=None, ignore_block_result_criteria=None):
    if block_id is None:
        block_id = (context_holder._reserve_block_id_generator.counter,
                    context_holder._reserve_block_id_generator.get_new_ID())

    if context_holder._closeable and context_holder._closed:
        raise IsOK_Closed(context_holder, block_id, block_info)

    context_holder._push_block_info(block_id, block_info)
    if block_results_criteria is not None:
        context_holder._push_criteria(block_results_criteria)
    need_to_save_block_result = True
    try:
        yield context_holder
    except IsOK_BlockFailed as exc:
        result_info = None
        if exc.args:
            result_info = exc.args[0]
        context_holder.push_result(False, IsOK_IntenalResult(
                IsOK_IntenalResultType.built_in_exception__is_ok_block_failed,
                'ISOK INTERNAL RESULT. BUILT-IN EXCEPTION: IsOK_BlockFailed ({})'.format(result_info), result_info))
    except IsOK_HistoryExport as export:
        context_holder.process_history_import(export)
        if export.process_error_result:
            context_holder.push_result(False, IsOK_IntenalResult(
                    IsOK_IntenalResultType.built_in_exception__bad_history_import,
                    'ISOK INTERNAL RESULT. BUILT-IN EXCEPTION: BAD HISTORY IMPORT EXCEPTION', None))
    except:
        exc = sys.exc_info()
        exc_type, exc_obj, exc_tb = exc
        tb_full_file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        tb_line_number = exc_tb.tb_lineno
        tb_function_name = str()
        tb_text = str()

        tb_list = traceback.extract_tb(exc_tb, 2)
        if len(tb_list) >= 2:
            actual_tb = tb_list[1]
            tb_full_file_name, tb_line_number, tb_function_name, tb_text = actual_tb

        exception = exc
        error_str = '{} {}'.format(str(exception[0]), str(exception[1].args[0]))
        # print('+++', error_str)
        formatted_traceback = traceback.format_exception(exception[0], exception[1], exception[2])
        exception = exception[:2] + (formatted_traceback,)
        trace_str = ''.join(exception[2])
        if context_holder._save_debug_trace:
            result_string = 'ISOK INTERNAL RESULT. CODE EXCEPTION "{}" AT "{}":{} in {} WITH TRACE: \n' \
                            '{}\n' \
                            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' \
                            ''.format(error_str, tb_full_file_name, tb_line_number, tb_function_name, trace_str)
        else:
            result_string = 'ISOK INTERNAL RESULT. CODE EXCEPTION "{}" AT "{}":{} in {}'.format(
                    error_str, tb_full_file_name, tb_line_number, tb_function_name)
        context_holder.push_result(False, IsOK_IntenalResult(
                IsOK_IntenalResultType.external_exception, result_string, exc))
        # print(result_string)
        # _is_ok_reader_runner__context_holder.push_result(False, sys.exc_info()[1])
        if context_holder._raise_exceptions:
            need_to_save_block_result = False
            context_holder._save_block_result()
            context_holder.raise_bad_blocks()
            # raise
    else:
        if context_holder._current_block_result is None:
            # _is_ok_reader_runner__context_holder.push_result(True)
            context_holder.push_result(False, IsOK_IntenalResult(
                    IsOK_IntenalResultType.block_did_not_returned_an_answer,
                    'ISOK INTERNAL RESULT. BLOCK DID NOT RETURN RESULT', None))
    finally:
        if need_to_save_block_result:
            context_holder._save_block_result(ignore_block_result_criteria)
        if block_results_criteria is not None:
            context_holder._pop_criteria()
        context_holder._pop_block_info()


def is_ok__function(target_function):
    """
    Parameters: is_ok__context_holder= (required)
        , is_ok__block_id= (required)
        , is_ok__block_info= (optional)
        , is_ok__block_results_criteria= (optional)
        , is_ok__ignore_block_result_criteria= (optional).
    Parameters passed to the target_function: is_ok__context_holder (after local block configuration).
    :param target_function: function
    :return:
    """
    def new_target_function(*args, **kwargs):
        context_holder = None
        if 'is_ok__context_holder' in kwargs:
            context_holder = kwargs['is_ok__context_holder']
            del kwargs['is_ok__context_holder']
        else:
            raise IsOKForFunction_ParameterNeeded('is_ok__context_holder')

        block_id = None
        if 'is_ok__block_id' in kwargs:
            block_id = kwargs['is_ok__block_id']
            del kwargs['is_ok__block_id']
        else:
            raise IsOKForFunction_ParameterNeeded('is_ok__block_id')

        block_info = None
        if 'is_ok__block_info' in kwargs:
            block_info = kwargs['is_ok__block_info']
            del kwargs['is_ok__block_info']

        block_results_criteria = None
        if 'is_ok__block_results_criteria' in kwargs:
            block_results_criteria = kwargs['is_ok__block_results_criteria']
            del kwargs['is_ok__block_results_criteria']

        ignore_block_result_criteria = None
        if 'is_ok__ignore_block_result_criteria' in kwargs:
            ignore_block_result_criteria = kwargs['is_ok__ignore_block_result_criteria']
            del kwargs['is_ok__ignore_block_result_criteria']

        target_function_result = None
        with is_ok(context_holder, block_id, block_info, block_results_criteria, ignore_block_result_criteria) as \
                context:
            kwargs['is_ok__context_holder'] = context
            target_function_result = target_function(*args, **kwargs)

        return target_function_result

    return new_target_function


class _IsOkRunner:
    def __init__(self, current_globals, context_holder, block_id=None, block_info=None, block_results_criteria=None,
                 ignore_block_result_criteria=None, function_result_criteria=None):
        self._is_ok_runner__current_globals = current_globals
        self._is_ok_runner__context_holder = context_holder
        self._is_ok_runner__block_id = block_id
        self._is_ok_runner__block_info = block_info
        self._is_ok_runner__block_results_criteria = block_results_criteria
        self._is_ok_runner__ignore_block_result_criteria = ignore_block_result_criteria

    def __getattr__(self, name):
        target_functor = None
        if name in self._is_ok_runner__current_globals:
            target_functor = self._is_ok_runner__current_globals[name]
        else:
            raise AttributeError(name)

        def new_target_function(*args, **kwargs):
            target_function_result = None
            block_id = self._is_ok_runner__block_id or str(target_functor)
            with is_ok(self._is_ok_runner__context_holder, block_id, self._is_ok_runner__block_info,
                       self._is_ok_runner__block_results_criteria,
                       self._is_ok_runner__ignore_block_result_criteria) as context:
                kwargs['is_ok__context_holder'] = context
                target_function_result = target_functor(*args, **kwargs)

            return target_function_result

        return new_target_function


class IsOkRunner:
    def __init__(self, current_globals, context_holder):
        self.current_globals = current_globals
        self.context_holder = context_holder

    def __call__(self, block_id=None, block_info=None, block_results_criteria=None,
                 ignore_block_result_criteria=None):
        result = _IsOkRunner(self.current_globals, self.context_holder, block_id, block_info, block_results_criteria,
                             ignore_block_result_criteria)
        return result


class _IsOkCallRunner:
    def __init__(self, context_holder, block_id=None, block_info=None, block_results_criteria=None,
                 ignore_block_result_criteria=None, function_result_criteria=None):
        self._is_ok_runner__context_holder = context_holder
        self._is_ok_runner__block_id = block_id
        self._is_ok_runner__block_info = block_info
        self._is_ok_runner__block_results_criteria = block_results_criteria
        self._is_ok_runner__ignore_block_result_criteria = ignore_block_result_criteria

    def __call__(self, target_functor, *args, **kwargs):
        target_function_result = None
        block_id = self._is_ok_runner__block_id or str(target_functor)
        with is_ok(self._is_ok_runner__context_holder, block_id, self._is_ok_runner__block_info,
                   self._is_ok_runner__block_results_criteria,
                   self._is_ok_runner__ignore_block_result_criteria) as context:
            kwargs['is_ok__context_holder'] = context
            target_function_result = target_functor(*args, **kwargs)

        return target_function_result


class IsOkCallRunner:
    def __init__(self, context_holder):
        self.context_holder = context_holder

    def __call__(self, block_id=None, block_info=None, block_results_criteria=None,
                 ignore_block_result_criteria=None):
        result = _IsOkCallRunner(self.context_holder, block_id, block_info, block_results_criteria,
                                 ignore_block_result_criteria)
        return result


def is_ok__function__simple(target_function):
    """
    Parameters: is_ok__context_holder= (required)
        , is_ok__block_id= (optional) (default value == str(target_function))
        , is_ok__block_results_criteria= (optional)
        , is_ok__ignore_block_result_criteria= (optional).
    Parameters passed to the target_function: .
    :param target_function: function
    :return:
    """
    def new_target_function(*args, **kwargs):
        context_holder = None
        if 'is_ok__context_holder' in kwargs:
            context_holder = kwargs['is_ok__context_holder']
            del kwargs['is_ok__context_holder']
        else:
            raise IsOKForFunction_ParameterNeeded('is_ok__context_holder')

        # block_id = '__UNNAMED_FUNCTION_SIMPLE_BLOCK__'
        block_id = str(target_function)
        if 'is_ok__block_id' in kwargs:
            block_id = kwargs['is_ok__block_id']
            del kwargs['is_ok__block_id']

        block_results_criteria = None
        if 'is_ok__block_results_criteria' in kwargs:
            block_results_criteria = kwargs['is_ok__block_results_criteria']
            del kwargs['is_ok__block_results_criteria']

        ignore_block_result_criteria = None
        if 'is_ok__ignore_block_result_criteria' in kwargs:
            ignore_block_result_criteria = kwargs['is_ok__ignore_block_result_criteria']
            del kwargs['is_ok__ignore_block_result_criteria']

        target_function_result = None
        with is_ok(context_holder, block_id, None, block_results_criteria, ignore_block_result_criteria) as context:
            if context:
                target_function_result = target_function(*args, **kwargs)
                context.push_result(True, target_function_result)

        return target_function_result

    return new_target_function


class _IsOkRunnerSimple:
    def __init__(self, current_globals, context_holder, block_id=None, block_info=None, block_results_criteria=None,
                 ignore_block_result_criteria=None, function_result_criteria=None):
        self._is_ok_runner_simple__current_globals = current_globals
        self._is_ok_runner_simple__context_holder = context_holder
        self._is_ok_runner_simple__block_id = block_id
        self._is_ok_runner_simple__block_info = block_info
        self._is_ok_runner_simple__block_results_criteria = block_results_criteria
        self._is_ok_runner_simple__ignore_block_result_criteria = ignore_block_result_criteria
        self._is_ok_runner_simple__function_result_criteria = function_result_criteria or (lambda result: True)

    def __getattr__(self, name):
        target_functor = None
        if name in self._is_ok_runner_simple__current_globals:
            target_functor = self._is_ok_runner_simple__current_globals[name]
        else:
            raise AttributeError(name)

        def new_target_function(*args, **kwargs):
            target_function_result = None
            block_id = self._is_ok_runner_simple__block_id or str(target_functor)
            with is_ok(self._is_ok_runner_simple__context_holder, block_id, self._is_ok_runner_simple__block_info,
                       self._is_ok_runner_simple__block_results_criteria,
                       self._is_ok_runner_simple__ignore_block_result_criteria) as context:
                if context:
                    target_function_result = target_functor(*args, **kwargs)
                    is_good_result = self._is_ok_runner_simple__function_result_criteria(target_function_result)
                    context.push_result(is_good_result, target_function_result)

            return target_function_result

        return new_target_function


class IsOkUniRunner:
    def __init__(self, current_globals, context_holder, simple_mode=False, function_result_criteria=None):
        self.current_globals = current_globals
        self.context_holder = context_holder
        self.simple_mode = simple_mode
        self.default_function_result_criteria = function_result_criteria or (lambda result: True)
        self.function_result_criteria = self.default_function_result_criteria

        self.runner_class = _IsOkRunner
        if self.simple_mode:
            self.runner_class = _IsOkRunnerSimple

    def set_function_result_criteria(self, result_criteria_computer):
        self.function_result_criteria = result_criteria_computer

    def reset_function_result_criteria(self):
        self.function_result_criteria = self.default_function_result_criteria

    def __call__(self, block_id=None, block_info=None, block_results_criteria=None,
                 ignore_block_result_criteria=None):
        result = self.runner_class(self.current_globals, self.context_holder, block_id, block_info,
                                   block_results_criteria, ignore_block_result_criteria, self.function_result_criteria)
        return result


class _IsOkCallRunnerSimple:
    def __init__(self, context_holder, block_id=None, block_info=None, block_results_criteria=None,
                 ignore_block_result_criteria=None, function_result_criteria=None):
        self._is_ok_runner_simple__context_holder = context_holder
        self._is_ok_runner_simple__block_id = block_id
        self._is_ok_runner_simple__block_info = block_info
        self._is_ok_runner_simple__block_results_criteria = block_results_criteria
        self._is_ok_runner_simple__ignore_block_result_criteria = ignore_block_result_criteria
        self._is_ok_runner_simple__function_result_criteria = function_result_criteria or (lambda result: True)

    def __call__(self, target_functor, *args, **kwargs):
        target_function_result = None
        block_id = self._is_ok_runner_simple__block_id or str(target_functor)
        with is_ok(self._is_ok_runner_simple__context_holder, block_id, self._is_ok_runner_simple__block_info,
                   self._is_ok_runner_simple__block_results_criteria,
                   self._is_ok_runner_simple__ignore_block_result_criteria) as context:
            if context:
                target_function_result = target_functor(*args, **kwargs)
                is_good_result = self._is_ok_runner_simple__function_result_criteria(target_function_result)
                context.push_result(is_good_result, target_function_result)

        return target_function_result


class IsOkUniCallRunner:
    def __init__(self, context_holder, simple_mode=False, function_result_criteria=None):
        self.context_holder = context_holder
        self.simple_mode = simple_mode
        self.default_function_result_criteria = function_result_criteria or (lambda result: True)
        self.function_result_criteria = self.default_function_result_criteria

        self.runner_class = _IsOkCallRunner
        if self.simple_mode:
            self.runner_class = _IsOkCallRunnerSimple

    def set_function_result_criteria(self, result_criteria_computer):
        self.function_result_criteria = result_criteria_computer

    def reset_function_result_criteria(self):
        self.function_result_criteria = self.default_function_result_criteria

    def __call__(self, block_id=None, block_info=None, block_results_criteria=None,
                 ignore_block_result_criteria=None):
        result = self.runner_class(self.context_holder, block_id, block_info,
                                   block_results_criteria, ignore_block_result_criteria, self.function_result_criteria)
        return result


class _IsOkValRunner:
    def __init__(self, context_holder, block_id=None, block_info=None, block_results_criteria=None,
                 ignore_block_result_criteria=None, function_result_criteria=None, reaction_to_the_result=None):
        self._is_ok_runner_simple__context_holder = context_holder
        self._is_ok_runner_simple__block_id = block_id
        self._is_ok_runner_simple__block_info = block_info
        self._is_ok_runner_simple__block_results_criteria = block_results_criteria
        self._is_ok_runner_simple__ignore_block_result_criteria = ignore_block_result_criteria
        self._is_ok_runner_simple__function_result_criteria = function_result_criteria or (lambda result: True)
        self._is_ok_runner_simple__reaction_to_the_result = reaction_to_the_result

    def __call__(self, functor_result):
        target_function_result = functor_result
        block_id = self._is_ok_runner_simple__block_id
        with is_ok(self._is_ok_runner_simple__context_holder, block_id, self._is_ok_runner_simple__block_info,
                   self._is_ok_runner_simple__block_results_criteria,
                   self._is_ok_runner_simple__ignore_block_result_criteria) as context:
            if context:
                is_good_result = self._is_ok_runner_simple__function_result_criteria(target_function_result)
                if self._is_ok_runner_simple__reaction_to_the_result is not None:
                    verdict = self._is_ok_runner_simple__reaction_to_the_result(is_good_result, target_function_result)
                    target_function_result = (target_function_result, verdict)
                context.push_result(is_good_result, target_function_result)

        return functor_result


class IsOkValRunner:
    def __init__(self, context_holder, function_result_criteria=None, reaction_to_the_result=None):
        self.context_holder = context_holder
        self.default_function_result_criteria = function_result_criteria or (lambda result: True)
        self.function_result_criteria = self.default_function_result_criteria
        self.reaction_to_the_result = reaction_to_the_result

    def set_function_result_criteria(self, result_criteria_computer):
        self.function_result_criteria = result_criteria_computer

    def reset_function_result_criteria(self):
        self.function_result_criteria = self.default_function_result_criteria

    def __call__(self, block_id=None, block_info=None, block_results_criteria=None,
                 ignore_block_result_criteria=None):
        result = _IsOkValRunner(self.context_holder, block_id, block_info,
                                block_results_criteria, ignore_block_result_criteria,
                                self.function_result_criteria, self.reaction_to_the_result)
        return result


@contextmanager
def is_ok_reader(context_holder, block_results_criteria=None, close=False):
    if block_results_criteria is not None:
        context_holder._push_criteria(block_results_criteria)
    try:
        yield context_holder
    except:
        raise
    finally:
        if block_results_criteria is not None:
            context_holder._pop_criteria()
        if close:
            context_holder.close()


def is_ok_reader__function(target_function):
    """
    Parameters: is_ok__context_holder= (required), is_ok__block_results_criteria= (optional), is_ok__close= (optional).
    Parameters passed to the target_function: is_ok__context_holder (after local block configuration).
    :param target_function: function
    :return:
    """
    def new_target_function(*args, **kwargs):
        context_holder = None
        if 'is_ok__context_holder' in kwargs:
            context_holder = kwargs['is_ok__context_holder']
            del kwargs['is_ok__context_holder']
        else:
            raise IsOKForFunction_ParameterNeeded('is_ok__context_holder')

        block_results_criteria = None
        if 'is_ok__block_results_criteria' in kwargs:
            block_results_criteria = kwargs['is_ok__block_results_criteria']
            del kwargs['is_ok__block_results_criteria']

        close = None
        if 'is_ok__close' in kwargs:
            close = kwargs['is_ok__close']
            del kwargs['is_ok__close']

        target_function_result = None
        with is_ok_reader(context_holder, block_results_criteria, close) as context:
            kwargs['is_ok__context_holder'] = context
            target_function_result = target_function(*args, **kwargs)

        return target_function_result

    return new_target_function


class _IsOkReaderRunner:
    def __init__(self, current_globals, context_holder, block_results_criteria=None, close=False):
        self._is_ok_reader_runner__current_globals = current_globals
        self._is_ok_reader_runner__context_holder = context_holder
        self._is_ok_reader_runner__block_results_criteria = block_results_criteria
        self._is_ok_reader_runner__close = close

    def __getattr__(self, name):
        target_functor = None
        if name in self._is_ok_reader_runner__current_globals:
            target_functor = self._is_ok_reader_runner__current_globals[name]
        else:
            raise AttributeError(name)

        def new_target_function(*args, **kwargs):
            target_function_result = None
            with is_ok_reader(self._is_ok_reader_runner__context_holder,
                              self._is_ok_reader_runner__block_results_criteria,
                              self._is_ok_reader_runner__close) as context:
                kwargs['is_ok__context_holder'] = context
                target_function_result = target_functor(*args, **kwargs)

            return target_function_result

        return new_target_function


class IsOkReaderRunner:
    def __init__(self, current_globals, context_holder):
        self.current_globals = current_globals
        self.context_holder = context_holder

    def __call__(self, block_results_criteria=None, close=False):
        result = _IsOkReaderRunner(self.current_globals, self.context_holder, block_results_criteria, close)
        return result


class _IsOkReaderCallRunner:
    def __init__(self, context_holder, block_results_criteria=None, close=False):
        self._is_ok_reader_runner__context_holder = context_holder
        self._is_ok_reader_runner__block_results_criteria = block_results_criteria
        self._is_ok_reader_runner__close = close

    def __call__(self, target_functor, *args, **kwargs):
        target_function_result = None
        with is_ok_reader(self._is_ok_reader_runner__context_holder,
                          self._is_ok_reader_runner__block_results_criteria,
                          self._is_ok_reader_runner__close) as context:
            kwargs['is_ok__context_holder'] = context
            target_function_result = target_functor(*args, **kwargs)

        return target_function_result


class IsOkReaderCallRunner:
    def __init__(self, context_holder):
        self.context_holder = context_holder

    def __call__(self, block_results_criteria=None, close=False):
        result = _IsOkReaderCallRunner(self.context_holder, block_results_criteria, close)
        return result
