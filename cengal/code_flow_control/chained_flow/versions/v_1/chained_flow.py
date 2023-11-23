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
from cengal.code_flow_control.smart_values.versions.v_1.smart_values import *

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


class ChainLinkFailed(Exception): pass


class ChainClosed(Exception):
    """
    link considers it ordinary external exception
    """

    def __init__(self, chain, link_id, link_info):
        super(ChainClosed, self).__init__('Content Holder is closed. '
                                          'Content Holder ID: {}; '
                                          'Content Holder Info: {}; '
                                          'Link ID: {}; '
                                          'Link Info {}'.format(str(chain._chain_id),
                                                                 str(chain._chain_info),
                                                                 str(link_id),
                                                                 str(link_info)))
        self.chain = chain
        self.link_id = link_id
        self.link_info = link_info


class ChainFunctionParameterNeeded(Exception): pass


class CriteriaType(Enum):
    # class CriteriaType():  # much more efficient than Enum inheritance
    needed = 0  # only set of this links is needed (should be already successfully done)
    optional = 1  # all links are needed except of this set of links
    any = 2  # any result will fit criteria
    forbidden = 3  # set of this links should be already failed
    not_successful = 4  # set of this links should not be successfully done (also may not start) at the check time


class IgnoreLinkResultCriteriaType(Enum):
    do_not_ignore = 0
    ignore_if_failed = 1
    ignore_if_successful = 2


class ChainHistoryExport(Exception):
    def __init__(self, history, process_error_result=True):
        super(ChainHistoryExport, self).__init__('')
        self.history = history
        self.process_error_result = process_error_result


class ChainInternalResult:
    def __init__(self, type_id, str_data, data):
        self.type_id = type_id
        self.str_data = str_data
        self.data = data

    def __str__(self):
        return self.str_data


class ChainInternalResultType(Enum):
    # class CriteriaType():  # much more efficient than Enum inheritance
    built_in_exception__chain_link_failed = 0
    built_in_exception__bad_history_import = 1
    external_exception = 2
    link_did_not_returned_an_answer = 3


class Chain:
    def __init__(self, chain_id=None, chain_info=None, global_link_results_criteria=None,
                 raise_exceptions=False, save_debug_trace=False, closeable=True):
        """

        :param chain_id:
        :param chain_info:
        :param global_link_results_criteria: will be set to ValueType(CriteriaType.optional, set()) if None;
            in this case all links are required.
        :param raise_exceptions:
        :param save_debug_trace:
        :param closeable:
        :return:
        """
        # Use only ValueType(CriteriaType.optional, ...) or ValueType(CriteriaType.needed, set()).
        # Other will be ignored here.
        # You may use global_link_results_criteria=ValueType(CriteriaType.optional, set()) to create criteria
        # "no fails in any link"
        self._chain_id = chain_id
        self._chain_info = chain_info
        self._internal_links_index = IDGenerator()
        self._reserve_link_id_generator = IDGenerator(GeneratorType.guid_string)
        self._criteria_list = list()
        global_link_results_criteria = global_link_results_criteria or ValueType(CriteriaType.optional, set())
        if global_link_results_criteria is not None:
            self._criteria_list.append(global_link_results_criteria)
        self._raise_exceptions = raise_exceptions
        self._save_debug_trace = save_debug_trace
        self._closeable = closeable
        self._full_history = list()
        self._links_library = dict()
        self._all_made_links = set()
        self._good_links = set()
        self._bad_links = set()

        self._current_link_id = None
        self._current_link_info = None
        self._current_link_result = None
        self._closed = False

        self._bool_result = ValueCache()

    # def _push_criteria(self, set_of_needed_links=None, set_of_optional_links=None):
    def _push_criteria(self, link_results_criteria):
        # Do not use!
        self._bool_result()
        self._criteria_list.append(link_results_criteria)

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

    def _push_link_info(self, link_id, link_info=None):
        self._current_link_id = link_id
        self._current_link_info = link_info
        self._current_link_result = None

    def _pop_link_info(self):
        self._current_link_id = None
        self._current_link_info = None
        self._current_link_result = None

    def push_result(self, bool_result, info_or_data=None):
        self._current_link_result = (bool_result, info_or_data)

    def push_result_c(self, result):
        # "class" version: to use when result = ValueExistence()
        self._current_link_result = (result.existence, result.result)

    def read_link_result_link(self, link_id):
        # result is NOT protected from changing!
        original_result_data = self._links_library[link_id][3]
        result = ValueExistence(original_result_data[0], original_result_data[1])
        # result = self._links_library[link_id][3]
        return result

    def read_link_result_copy(self, link_id):
        original_result_data = self._links_library[link_id][3]
        result = ValueExistence(original_result_data[0], copy.copy(original_result_data[1]))
        return result

    def read_link_result_deepcopy(self, link_id):
        original_result_data = self._links_library[link_id][3]
        result = ValueExistence(original_result_data[0], copy.deepcopy(original_result_data[1]))
        return result

    def _save_link_result(self, ignore_link_result_criteria=None):
        # ignore_link_result_criteria = ignore_link_result_criteria or IgnoreLinkResultCriteriaType.do_not_ignore
        if ((IgnoreLinkResultCriteriaType.ignore_if_failed == ignore_link_result_criteria) and
            (not self._current_link_result[0])) \
                or ((IgnoreLinkResultCriteriaType.ignore_if_successful == ignore_link_result_criteria) and
                    self._current_link_result[0]):
            return

        self._bool_result()
        import_depth = 0
        full_link_info = (self._internal_links_index.get_new_ID(), self._current_link_id, self._current_link_info,
                           self._current_link_result, import_depth)
        self._full_history.append(full_link_info)
        self._links_library[self._current_link_id] = full_link_info
        self._all_made_links.add(self._current_link_id)
        if self._current_link_result[0]:
            self._good_links.add(self._current_link_id)
        else:
            self._bad_links.add(self._current_link_id)

    def __bool__(self):
        if self._bool_result:
            return self._bool_result.get()
        else:
            current_criteria = self.read_criteria()
            result = True
            if CriteriaType.needed == current_criteria:
                if len(current_criteria.result) != len(current_criteria.result & self._good_links):
                    result = False
            elif CriteriaType.optional == current_criteria:
                if len(self._bad_links - current_criteria.result) != 0:
                    result = False
            elif CriteriaType.any == current_criteria:
                result = True
            elif CriteriaType.forbidden == current_criteria:
                if len(current_criteria.result) != len(current_criteria.result & self._bad_links):
                    result = False
            elif CriteriaType.not_successful == current_criteria:
                if len(current_criteria.result & self._good_links) != 0:
                    result = False
            self._bool_result.set(result)
            return result

    def __nonzero__(self):
        return self.__bool__()

    @staticmethod
    def _link_list_to_str(link_list):
        links_str = ',\n'.join('(index({}), depth({}), ID({}), INFO({}), RESULT({}))'.format(str(another_link[0]),
                                                                                              str(another_link[4]),
                                                                                              str(another_link[1]),
                                                                                              str(another_link[2]),
                                                                                              '({}, {})'.format(
                                                                                                  str(another_link[3][0]),
                                                                                                  str(another_link[3][1])))
                                for another_link in link_list)
        return links_str

    def _link_str_to_chain_str(self, links_str):
        full_string = '{{{{CONTEXT_HOLDER_ID({}): CONTEXT_HOLDER_INFO({})}}:[\n{}\n]}}'.format(
                self._chain_id, self._chain_info, links_str)
        return full_string

    def get_bad_links(self):
        result = list()
        for another_link in self._full_history:
            if not another_link[3][0]:
                result.append(another_link)
        return result

    def get_bad_links_str(self):
        bad_links = self.get_bad_links()
        full_history_str = self._link_list_to_str(bad_links)
        full_string = self._link_str_to_chain_str(full_history_str)
        return full_string

    def raise_bad_links(self):
        raise ChainHistoryExport(self.get_bad_links())

    def raise_full_history(self):
        raise ChainHistoryExport(self._full_history)

    def process_history_import(self, his_ex):
        history = his_ex.history
        for another_link in history:
            full_link_info = (self._internal_links_index.get_new_ID(), another_link[1], another_link[2],
                               another_link[3], another_link[4] + 1)
            self._full_history.append(full_link_info)

    def close(self):
        self._closed = True

    def _reopen(self):
        self._closed = False

    def __str__(self):
        full_history_str = self._link_list_to_str(self._full_history)
        full_string = self._link_str_to_chain_str(full_history_str)
        return full_string

    def __call__(self, *args, **kwargs):
        return link(self, *args, **kwargs)

    def chain(self, *args, **kwargs):
        return self.__call__(*args, **kwargs)


@contextmanager
def link(chain, link_id, link_info=None, link_results_criteria=None, ignore_link_result_criteria=None):
    if link_id is None:
        link_id = (chain._reserve_link_id_generator.counter,
                    chain._reserve_link_id_generator.get_new_ID())

    if chain._closeable and chain._closed:
        raise ChainClosed(chain, link_id, link_info)

    chain._push_link_info(link_id, link_info)
    if link_results_criteria is not None:
        chain._push_criteria(link_results_criteria)
    need_to_save_link_result = True
    try:
        yield chain
    except ChainLinkFailed as exc:
        result_info = None
        if exc.args:
            result_info = exc.args[0]
        chain.push_result(False, ChainInternalResult(
                ChainInternalResultType.built_in_exception__chain_link_failed,
                'CHAIN INTERNAL RESULT. BUILT-IN EXCEPTION: ChainLinkFailed ({})'.format(result_info), result_info))
    except ChainHistoryExport as export:
        chain.process_history_import(export)
        if export.process_error_result:
            chain.push_result(False, ChainInternalResult(
                    ChainInternalResultType.built_in_exception__bad_history_import,
                    'CHAIN INTERNAL RESULT. BUILT-IN EXCEPTION: BAD HISTORY IMPORT EXCEPTION', None))
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
        if chain._save_debug_trace:
            result_string = 'CHAIN INTERNAL RESULT. CODE EXCEPTION "{}" AT "{}":{} in {} WITH TRACE: \n' \
                            '{}\n' \
                            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' \
                            ''.format(error_str, tb_full_file_name, tb_line_number, tb_function_name, trace_str)
        else:
            result_string = 'CHAIN INTERNAL RESULT. CODE EXCEPTION "{}" AT "{}":{} in {}'.format(
                    error_str, tb_full_file_name, tb_line_number, tb_function_name)
        chain.push_result(False, ChainInternalResult(
                ChainInternalResultType.external_exception, result_string, exc))
        # print(result_string)
        # _chain_reader_runner__chain.push_result(False, sys.exc_info()[1])
        if chain._raise_exceptions:
            need_to_save_link_result = False
            chain._save_link_result()
            chain.raise_bad_links()
            # raise
    else:
        if chain._current_link_result is None:
            # _chain_reader_runner__chain.push_result(True)
            chain.push_result(False, ChainInternalResult(
                    ChainInternalResultType.link_did_not_returned_an_answer,
                    'CHAIN INTERNAL RESULT. Link DID NOT RETURN RESULT', None))
    finally:
        if need_to_save_link_result:
            chain._save_link_result(ignore_link_result_criteria)
        if link_results_criteria is not None:
            chain._pop_criteria()
        chain._pop_link_info()


def link__function(target_function):
    """
    Parameters: chain__chain= (required)
        , chain__link_id= (required)
        , chain__link_info= (optional)
        , chain__link_results_criteria= (optional)
        , chain__ignore_link_result_criteria= (optional).
    Parameters passed to the target_function: chain__chain (after local link configuration).
    :param target_function: function
    :return:
    """

    def new_target_function(*args, **kwargs):
        chain = None
        if 'chain__chain' in kwargs:
            chain = kwargs['chain__chain']
            del kwargs['chain__chain']
        else:
            raise ChainFunctionParameterNeeded('chain__chain')

        link_id = None
        if 'chain__link_id' in kwargs:
            link_id = kwargs['chain__link_id']
            del kwargs['chain__link_id']
        else:
            raise ChainFunctionParameterNeeded('chain__link_id')

        link_info = None
        if 'chain__link_info' in kwargs:
            link_info = kwargs['chain__link_info']
            del kwargs['chain__link_info']

        link_results_criteria = None
        if 'chain__link_results_criteria' in kwargs:
            link_results_criteria = kwargs['chain__link_results_criteria']
            del kwargs['chain__link_results_criteria']

        ignore_link_result_criteria = None
        if 'chain__ignore_link_result_criteria' in kwargs:
            ignore_link_result_criteria = kwargs['chain__ignore_link_result_criteria']
            del kwargs['chain__ignore_link_result_criteria']

        target_function_result = None
        with link(chain, link_id, link_info, link_results_criteria, ignore_link_result_criteria) as \
                context:
            kwargs['chain__chain'] = context
            target_function_result = target_function(*args, **kwargs)

        return target_function_result

    return new_target_function


class _ChainRunner:
    def __init__(self, current_globals, chain, link_id=None, link_info=None, link_results_criteria=None,
                 ignore_link_result_criteria=None, function_result_criteria=None):
        self._chain_runner__current_globals = current_globals
        self._chain_runner__chain = chain
        self._chain_runner__link_id = link_id
        self._chain_runner__link_info = link_info
        self._chain_runner__link_results_criteria = link_results_criteria
        self._chain_runner__ignore_link_result_criteria = ignore_link_result_criteria

    def __getattr__(self, name):
        target_functor = None
        if name in self._chain_runner__current_globals:
            target_functor = self._chain_runner__current_globals[name]
        else:
            raise AttributeError(name)

        def new_target_function(*args, **kwargs):
            target_function_result = None
            link_id = self._chain_runner__link_id or str(target_functor)
            with link(self._chain_runner__chain, link_id, self._chain_runner__link_info,
                      self._chain_runner__link_results_criteria,
                      self._chain_runner__ignore_link_result_criteria) as context:
                kwargs['chain__chain'] = context
                target_function_result = target_functor(*args, **kwargs)

            return target_function_result

        return new_target_function


class ChainRunner:
    def __init__(self, current_globals, chain):
        self.current_globals = current_globals
        self.chain = chain

    def __call__(self, link_id=None, link_info=None, link_results_criteria=None,
                 ignore_link_result_criteria=None):
        result = _ChainRunner(self.current_globals, self.chain, link_id, link_info, link_results_criteria,
                              ignore_link_result_criteria)
        return result


class _ChainCallRunner:
    def __init__(self, chain, link_id=None, link_info=None, link_results_criteria=None,
                 ignore_link_result_criteria=None, function_result_criteria=None):
        self._chain_runner__chain = chain
        self._chain_runner__link_id = link_id
        self._chain_runner__link_info = link_info
        self._chain_runner__link_results_criteria = link_results_criteria
        self._chain_runner__ignore_link_result_criteria = ignore_link_result_criteria

    def __call__(self, target_functor, *args, **kwargs):
        target_function_result = None
        link_id = self._chain_runner__link_id or str(target_functor)
        with link(self._chain_runner__chain, link_id, self._chain_runner__link_info,
                  self._chain_runner__link_results_criteria,
                  self._chain_runner__ignore_link_result_criteria) as context:
            kwargs['chain__chain'] = context
            target_function_result = target_functor(*args, **kwargs)

        return target_function_result


class ChainCallRunner:
    def __init__(self, chain):
        self.chain = chain

    def __call__(self, link_id=None, link_info=None, link_results_criteria=None,
                 ignore_link_result_criteria=None):
        result = _ChainCallRunner(self.chain, link_id, link_info, link_results_criteria,
                                  ignore_link_result_criteria)
        return result


def link__function__simple(target_function):
    """
    Parameters: chain__chain= (required)
        , chain__link_id= (optional) (default value == str(target_function))
        , chain__link_results_criteria= (optional)
        , chain__ignore_link_result_criteria= (optional).
    Parameters passed to the target_function: .
    :param target_function: function
    :return:
    """

    def new_target_function(*args, **kwargs):
        chain = None
        if 'chain__chain' in kwargs:
            chain = kwargs['chain__chain']
            del kwargs['chain__chain']
        else:
            raise ChainFunctionParameterNeeded('chain__chain')

        # link_id = '__UNNAMED_FUNCTION_SIMPLE_LINK__'
        link_id = str(target_function)
        if 'chain__link_id' in kwargs:
            link_id = kwargs['chain__link_id']
            del kwargs['chain__link_id']

        link_results_criteria = None
        if 'chain__link_results_criteria' in kwargs:
            link_results_criteria = kwargs['chain__link_results_criteria']
            del kwargs['chain__link_results_criteria']

        ignore_link_result_criteria = None
        if 'chain__ignore_link_result_criteria' in kwargs:
            ignore_link_result_criteria = kwargs['chain__ignore_link_result_criteria']
            del kwargs['chain__ignore_link_result_criteria']

        target_function_result = None
        with link(chain, link_id, None, link_results_criteria, ignore_link_result_criteria) as context:
            if context:
                target_function_result = target_function(*args, **kwargs)
                context.push_result(True, target_function_result)

        return target_function_result

    return new_target_function


class _ChainRunnerSimple:
    def __init__(self, current_globals, chain, link_id=None, link_info=None, link_results_criteria=None,
                 ignore_link_result_criteria=None, function_result_criteria=None):
        self._chain_runner_simple__current_globals = current_globals
        self._chain_runner_simple__chain = chain
        self._chain_runner_simple__link_id = link_id
        self._chain_runner_simple__link_info = link_info
        self._chain_runner_simple__link_results_criteria = link_results_criteria
        self._chain_runner_simple__ignore_link_result_criteria = ignore_link_result_criteria
        self._chain_runner_simple__function_result_criteria = function_result_criteria or (lambda result: True)

    def __getattr__(self, name):
        target_functor = None
        if name in self._chain_runner_simple__current_globals:
            target_functor = self._chain_runner_simple__current_globals[name]
        else:
            raise AttributeError(name)

        def new_target_function(*args, **kwargs):
            target_function_result = None
            link_id = self._chain_runner_simple__link_id or str(target_functor)
            with link(self._chain_runner_simple__chain, link_id, self._chain_runner_simple__link_info,
                      self._chain_runner_simple__link_results_criteria,
                      self._chain_runner_simple__ignore_link_result_criteria) as context:
                if context:
                    target_function_result = target_functor(*args, **kwargs)
                    is_good_result = self._chain_runner_simple__function_result_criteria(target_function_result)
                    context.push_result(is_good_result, target_function_result)

            return target_function_result

        return new_target_function


class ChainUniRunner:
    def __init__(self, current_globals, chain, simple_mode=False, function_result_criteria=None):
        self.current_globals = current_globals
        self.chain = chain
        self.simple_mode = simple_mode
        self.default_function_result_criteria = function_result_criteria or (lambda result: True)
        self.function_result_criteria = self.default_function_result_criteria

        self.runner_class = _ChainRunner
        if self.simple_mode:
            self.runner_class = _ChainRunnerSimple

    def set_function_result_criteria(self, result_criteria_computer):
        self.function_result_criteria = result_criteria_computer

    def reset_function_result_criteria(self):
        self.function_result_criteria = self.default_function_result_criteria

    def __call__(self, link_id=None, link_info=None, link_results_criteria=None,
                 ignore_link_result_criteria=None):
        result = self.runner_class(self.current_globals, self.chain, link_id, link_info,
                                   link_results_criteria, ignore_link_result_criteria, self.function_result_criteria)
        return result


class _ChainCallRunnerSimple:
    def __init__(self, chain, link_id=None, link_info=None, link_results_criteria=None,
                 ignore_link_result_criteria=None, function_result_criteria=None):
        self._chain_runner_simple__chain = chain
        self._chain_runner_simple__link_id = link_id
        self._chain_runner_simple__link_info = link_info
        self._chain_runner_simple__link_results_criteria = link_results_criteria
        self._chain_runner_simple__ignore_link_result_criteria = ignore_link_result_criteria
        self._chain_runner_simple__function_result_criteria = function_result_criteria or (lambda result: True)

    def __call__(self, target_functor, *args, **kwargs):
        target_function_result = None
        link_id = self._chain_runner_simple__link_id or str(target_functor)
        with link(self._chain_runner_simple__chain, link_id, self._chain_runner_simple__link_info,
                  self._chain_runner_simple__link_results_criteria,
                  self._chain_runner_simple__ignore_link_result_criteria) as context:
            if context:
                target_function_result = target_functor(*args, **kwargs)
                is_good_result = self._chain_runner_simple__function_result_criteria(target_function_result)
                context.push_result(is_good_result, target_function_result)

        return target_function_result


class ChainUniCallRunner:
    def __init__(self, chain, simple_mode=False, function_result_criteria=None):
        self.chain = chain
        self.simple_mode = simple_mode
        self.default_function_result_criteria = function_result_criteria or (lambda result: True)
        self.function_result_criteria = self.default_function_result_criteria

        self.runner_class = _ChainCallRunner
        if self.simple_mode:
            self.runner_class = _ChainCallRunnerSimple

    def set_function_result_criteria(self, result_criteria_computer):
        self.function_result_criteria = result_criteria_computer

    def reset_function_result_criteria(self):
        self.function_result_criteria = self.default_function_result_criteria

    def __call__(self, link_id=None, link_info=None, link_results_criteria=None,
                 ignore_link_result_criteria=None):
        result = self.runner_class(self.chain, link_id, link_info,
                                   link_results_criteria, ignore_link_result_criteria, self.function_result_criteria)
        return result


class _ChainValRunner:
    def __init__(self, chain, link_id=None, link_info=None, link_results_criteria=None,
                 ignore_link_result_criteria=None, function_result_criteria=None, reaction_to_the_result=None):
        self._chain_runner_simple__chain = chain
        self._chain_runner_simple__link_id = link_id
        self._chain_runner_simple__link_info = link_info
        self._chain_runner_simple__link_results_criteria = link_results_criteria
        self._chain_runner_simple__ignore_link_result_criteria = ignore_link_result_criteria
        self._chain_runner_simple__function_result_criteria = function_result_criteria or (lambda result: True)
        self._chain_runner_simple__reaction_to_the_result = reaction_to_the_result

    def __call__(self, functor_result):
        target_function_result = functor_result
        link_id = self._chain_runner_simple__link_id
        with link(self._chain_runner_simple__chain, link_id, self._chain_runner_simple__link_info,
                  self._chain_runner_simple__link_results_criteria,
                  self._chain_runner_simple__ignore_link_result_criteria) as context:
            if context:
                is_good_result = self._chain_runner_simple__function_result_criteria(target_function_result)
                if self._chain_runner_simple__reaction_to_the_result is not None:
                    verdict = self._chain_runner_simple__reaction_to_the_result(is_good_result, target_function_result)
                    target_function_result = (target_function_result, verdict)
                context.push_result(is_good_result, target_function_result)

        return functor_result


class ChainValRunner:
    def __init__(self, chain, function_result_criteria=None, reaction_to_the_result=None):
        self.chain = chain
        self.default_function_result_criteria = function_result_criteria or (lambda result: True)
        self.function_result_criteria = self.default_function_result_criteria
        self.reaction_to_the_result = reaction_to_the_result

    def set_function_result_criteria(self, result_criteria_computer):
        self.function_result_criteria = result_criteria_computer

    def reset_function_result_criteria(self):
        self.function_result_criteria = self.default_function_result_criteria

    def __call__(self, link_id=None, link_info=None, link_results_criteria=None,
                 ignore_link_result_criteria=None):
        result = _ChainValRunner(self.chain, link_id, link_info,
                                 link_results_criteria, ignore_link_result_criteria,
                                 self.function_result_criteria, self.reaction_to_the_result)
        return result


@contextmanager
def chain_reader(chain, link_results_criteria=None, close=False):
    if link_results_criteria is not None:
        chain._push_criteria(link_results_criteria)
    try:
        yield chain
    except:
        raise
    finally:
        if link_results_criteria is not None:
            chain._pop_criteria()
        if close:
            chain.close()


def chain_reader__function(target_function):
    """
    Parameters: chain__chain= (required), chain__link_results_criteria= (optional), chain__close= (optional).
    Parameters passed to the target_function: chain__chain (after local link configuration).
    :param target_function: function
    :return:
    """

    def new_target_function(*args, **kwargs):
        chain = None
        if 'chain__chain' in kwargs:
            chain = kwargs['chain__chain']
            del kwargs['chain__chain']
        else:
            raise ChainFunctionParameterNeeded('chain__chain')

        link_results_criteria = None
        if 'chain__link_results_criteria' in kwargs:
            link_results_criteria = kwargs['chain__link_results_criteria']
            del kwargs['chain__link_results_criteria']

        close = None
        if 'chain__close' in kwargs:
            close = kwargs['chain__close']
            del kwargs['chain__close']

        target_function_result = None
        with chain_reader(chain, link_results_criteria, close) as context:
            kwargs['chain__chain'] = context
            target_function_result = target_function(*args, **kwargs)

        return target_function_result

    return new_target_function


class _ChainReaderRunner:
    def __init__(self, current_globals, chain, link_results_criteria=None, close=False):
        self._chain_reader_runner__current_globals = current_globals
        self._chain_reader_runner__chain = chain
        self._chain_reader_runner__link_results_criteria = link_results_criteria
        self._chain_reader_runner__close = close

    def __getattr__(self, name):
        target_functor = None
        if name in self._chain_reader_runner__current_globals:
            target_functor = self._chain_reader_runner__current_globals[name]
        else:
            raise AttributeError(name)

        def new_target_function(*args, **kwargs):
            target_function_result = None
            with chain_reader(self._chain_reader_runner__chain,
                              self._chain_reader_runner__link_results_criteria,
                              self._chain_reader_runner__close) as context:
                kwargs['chain__chain'] = context
                target_function_result = target_functor(*args, **kwargs)

            return target_function_result

        return new_target_function


class ChainReaderRunner:
    def __init__(self, current_globals, chain):
        self.current_globals = current_globals
        self.chain = chain

    def __call__(self, link_results_criteria=None, close=False):
        result = _ChainReaderRunner(self.current_globals, self.chain, link_results_criteria, close)
        return result


class _ChainReaderCallRunner:
    def __init__(self, chain, link_results_criteria=None, close=False):
        self._chain_reader_runner__chain = chain
        self._chain_reader_runner__link_results_criteria = link_results_criteria
        self._chain_reader_runner__close = close

    def __call__(self, target_functor, *args, **kwargs):
        target_function_result = None
        with chain_reader(self._chain_reader_runner__chain,
                          self._chain_reader_runner__link_results_criteria,
                          self._chain_reader_runner__close) as context:
            kwargs['chain__chain'] = context
            target_function_result = target_functor(*args, **kwargs)

        return target_function_result


class ChainReaderCallRunner:
    def __init__(self, chain):
        self.chain = chain

    def __call__(self, link_results_criteria=None, close=False):
        result = _ChainReaderCallRunner(self.chain, link_results_criteria, close)
        return result
