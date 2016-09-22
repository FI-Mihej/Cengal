#!/usr/bin/env python

# Copyright © 2016 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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

import platform
import requests
import binascii
import os, os.path
import pickle
import datetime
import base64
import json
from inspect import currentframe, getframeinfo, getouterframes
import traceback
import sys
import struct

from modules_management import alt_import

with alt_import('lzma') as module:
    if module is None:
        import lzmaffi.compat
        lzmaffi.compat.register()
        import lzma

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2016 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "1.0.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


PLATFORM_NAME = platform.python_implementation()  # can be 'PyPy', 'CPython', etc.
PYTHON_VERSION = platform.python_version_tuple()  # tuple() of str(); for example: ('3', '5', '1')
PYTHON_VERSION_INT = sys.version_info  # sys.version_info == (major=3, minor=2, micro=5, releaselevel='final', serial=0)
#   Usage: sys.version_info[0] == 3


def remove_percent_encoding_from_the_URI(string, plus=True):
    try:
        string = str(string)
        if plus:
            string = string.replace('+', ' ')
        string = string.encode(encoding='utf-8')
        percentTypes = ((b'%u', 6, (False, None)), (b'%', 3, (True, tuple(range(32)) + (34, 42, 58, 60, 62, 63, 124, 127))))
        # (prefix, full size, (allowed type or not at all, list of disallowed characters like backspace etc.))
        for percType in percentTypes:
            isDone = False
            while not isDone:
                index = string.find(percType[0])
                if index > -1:
                    ind2 = index+percType[1]
                    if ind2 > len(string):
                        ind2 = len(string)
                    hexString = string[index:ind2]
                    hexString = hexString[len(percType[0]):]
                    decodedString = b''
                    if percType[2][0]:
                        try:
                            decodedStringBuff = binascii.unhexlify(hexString)
                            if int.from_bytes(decodedStringBuff, byteorder='little') not in percType[2][1]:
                                decodedString = decodedStringBuff
                        except binascii.Error:
                            pass
                    string = string[:index] + decodedString + string[ind2:]
                else:
                    isDone = True
            if percType[2][0]:
                if (len(string) > 0) and (len(set(string).intersection(set(percType[2][1]))) > 0):
                    index = 0
                    isDone = False
                    while not isDone:
                        if string[index] in percType[2][1]:
                            string = string[:index] + string[index+1:]
                        else:
                            index += 1
                        if index >= len(string):
                            isDone = True
        string = string.decode(encoding='utf-8')
    except UnicodeDecodeError:
        string = None
    except UnicodeEncodeError:
        string = None
    return string


def get_standard_folder_separator():
    return '/'


def unify_folder_separators(string):
    string = str(string)
    string = string.replace('\\', get_standard_folder_separator())
    return string


def remove_forbidden_file_names_from_the_URI(string):
    # replace forbidden file names with slash ('/'). Also will unify folder separators (replace '\' with '/')
    forbiddenFileNames = {'con', 'prn', 'aux', 'nul', 'com1', 'com2', 'com3', 'com4', 'com5', 'com6', 'com7', 'com8'
        , 'com9', 'lpt1', 'lpt2', 'lpt3', 'lpt4', 'lpt5', 'lpt6', 'lpt7', 'lpt8', 'lpt9'}
    string = unify_folder_separators(str(string))
    strBuffer = string
    string = string.lower()
    for forbFile in forbiddenFileNames:
        string = string.replace(get_standard_folder_separator() + forbFile + get_standard_folder_separator(), '/')
        string = string.replace(get_standard_folder_separator() + forbFile + '.', '/')
    isStrWasChanged = False
    if strBuffer.lower() != string:
        isStrWasChanged = True
    else:
        string = strBuffer
    result = (string, isStrWasChanged)
    return result


def remove_path_to_the_parent_of_the_current_directory(string):
    string = unify_folder_separators(str(string))
    string = string.replace('../', '/')
    string = string.replace('/..', '/')
    return string


def is_path_is_trying_to_leave_site_sandbox(string):
    itemsList = string.split(get_standard_folder_separator())
    while '' in itemsList:
        itemsList.remove('')
    counter = 0
    for item in itemsList:
        if item == '..':
            counter -= 1
        elif item == '.':
            pass
        else:
            counter += 1
        if counter < 0:
            return True
    return False


def is_path_is_not_safe(string):
    # return tuple (decoded string, is_path_is_not_safe)
    result = tuple()
    string = remove_percent_encoding_from_the_URI(string)
    if string is None:
        result = (string, True)
        return result
    string = remove_forbidden_file_names_from_the_URI(string)
    if string[1]:
        result = (string[0], True)
        return result
    is_not_safe = is_path_is_trying_to_leave_site_sandbox(string[0])
    result = (string[0], is_not_safe)
    return result


def web_server__is_redirection_to_the_main_domain_needed(httpParser, prefix=None):
    functionResult = False

    host = httpParser.get_headers()['Host']
    domain = host
    if ':' in host:
        host = host.split(':')
        while '' in host:
            host.remove('')
        domain = host[0]
    if '.' in domain:
        domain = domain.split('.')
        if domain[0] == '':
            del domain[0]
            functionResult = True
        if prefix is not None:
            if domain[0] != prefix:
                domain.insert(0, prefix)
                functionResult = True
        lastDLen = len(domain) - 1
        if domain[lastDLen] == '':
            del domain[lastDLen]
            functionResult = True
        domain = '.'.join(domain)
    if host.__class__ is list:
        if len(host) > 1:
            host[0] = domain
            domain = ':'.join(host)

    functionResult = (functionResult, domain)
    return functionResult


def load_cache_from_file(fileName, originalCache):
    fileName = unify_folder_separators(fileName)
    cache = originalCache
    if os.path.exists(fileName):
        if os.path.isfile(fileName):
            cacheDataFile = None
            dataBuff = originalCache
            try:
                # cacheDataFile = open(fileName, 'rb')
                cacheDataFile = lzma.open(fileName, 'rb')
                cache = pickle.load(cacheDataFile)
                dataBuff.update(cache)
                cache = dataBuff
            except(EnvironmentError, pickle.PicklingError) as err:
                cache = dataBuff
            finally:
                if cacheDataFile is not None:
                    cacheDataFile.close()
    return cache


def save_cache_to_file(fileName, cache):
    fileName = unify_folder_separators(fileName)
    if cache.isWasChanged:
        isRenamedToBak = False
        if os.path.exists(fileName):
            try:
                if os.path.exists(fileName+'.bak'):
                    try:
                        os.remove(fileName+'.bak')
                    except IOError:
                        pass
                os.rename(fileName, fileName+'.bak')
                isRenamedToBak = True
            except IOError:
                pass

        isDumped = False
        cacheDataFile = None
        try:
            # cacheDataFile = open(fileName, 'wb')
            cacheDataFile = lzma.open(fileName, 'wb', format=lzma.FORMAT_XZ, check=lzma.CHECK_CRC64, preset=1)
            pickle.dump(cache, cacheDataFile)
            cache.isWasChanged = False
            isDumped = True
        except(EnvironmentError, pickle.PicklingError) as err:
            pass
        finally:
            if cacheDataFile is not None:
                cacheDataFile.close()

        if isRenamedToBak and isDumped:
            try:
                os.remove(fileName+'.bak')
            except IOError:
                pass


class CachedRequestError(Exception): pass


def make_cached_request__get(cache, request, useOnlyCachedResults=False):
    result = cache.try_to_get_data_for_request(request)
    if (result is None) or (not result.ok):
        if useOnlyCachedResults:
            raise CachedRequestError()
        result = requests.get(unify_folder_separators(request))
        result = SerializableHttpResponseFromRequests(result)
        cache.put_new_request(request, result)

    return result


def make_cached_request__universal(cache, request, workerFunction, useOnlyCachedResults=False, **workerFunctionParams):
    result = cache.try_to_get_data_for_request(request)
    if result is None:
        if useOnlyCachedResults:
            raise CachedRequestError()
        result = workerFunction(**workerFunctionParams)
        cache.put_new_request(request, result)

    return result


def make_a_copy_of_cached_request_with_another_keyname(cache, current_name, new_name, make_first_copy_only=False):
    is_copy_avaliable = True
    if make_first_copy_only:
        test = cache.try_to_get_data_for_request(current_name)
        if test is not None:
            is_copy_avaliable = False
    if is_copy_avaliable:
        result = cache.try_to_get_data_for_request(current_name)
        if result is not None:
            cache.put_new_request(new_name, result)


class SerializableHttpResponseFromRequests:
    def __init__(self, request, isBinaryFile=False):
        super(SerializableHttpResponseFromRequests, self).__init__()
        self.isBinaryFile = isBinaryFile
        self.url = request.url
        self.ok = request.ok
        self.reason = request.reason
        self.status_code = request.status_code
        self.headers = request.headers
        self.encoding = request.encoding

        if 'content' in dir(request):
            self.content = request.content
        else:
            self.content = None

        # if not isBinaryFile:
        #     if 'apparent_encoding' in dir(request):
        #         self.apparent_encoding = request.apparent_encoding
        #     else:
        #         self.apparent_encoding = None
        # else:
        #     self.apparent_encoding = None
        self.apparent_encoding = None

        # if (self.encoding is not None) or (self.apparent_encoding is not None):
        #     self.text = request.text
        # else:
        #     self.text = None
        self.text = None

    def getResultEncoding(self):
        if self.encoding is not None:
            return self.encoding
        elif self.apparent_encoding is not None:
            return self.apparent_encoding
        else:
            return 'utf-8'

    def getBytesContent(self):
        if self.content is not None:
            return self.content
        elif self.text is not None:
            bData = bytes(self.text, self.getResultEncoding())
            return bData
        else:
            print("Can't get data from the request object on url ", self.url)
            raise Exception


def saveRequestedFileToFS(folderName, requestResult):
    fileName = folderName + os.path.basename(requestResult.url)
    fileName = unify_folder_separators(fileName)
    with open(fileName, 'wb') as file:
        if requestResult.content is not None:
            file.write(requestResult.content)
        elif requestResult.text is not None:
            bData = bytes(requestResult.text, requestResult.getResultEncoding())
            file.write(bData)
        else:
            ex_text = "Can't save object from {} to the fie. Can't get data to save".format(requestResult.url)
            print(ex_text)
            raise Exception(ex_text)


def getFileModificationDate(fileName):
    fileName = unify_folder_separators(fileName)
    t = os.path.getmtime(fileName)
    return datetime.datetime.fromtimestamp(t)


def json_to_printable_string(json_obj):
    result = json.dumps(json_obj, sort_keys=True, indent=4, separators=(',', ': '))
    return result


def print_exception_traceback_info():
    exception = sys.exc_info()
    formattedTraceback = traceback.format_exception(exception[0], exception[1], exception[2])
    exception = exception[:2] + (formattedTraceback,)
    trace = ''
    for line in exception[2]:
        trace += line
    print(trace, file=sys.stderr)
    print(exception[0])
    print(exception[1])


# def load_old_class_to_the_new_one(oldStyleObject, newStyleObject, copyAllUnnecessaryMethods=False):
#     old_style_members = members = [attr for attr in dir(oldStyleObject) if not callable(attr) and not attr.startswith("__")]
#     new_style_members = members = [attr for attr in dir(newStyleObject) if not callable(attr) and not attr.startswith("__")]
#
#     for method in old_style_members:
#         method_allowed = False
#         if copyAllUnnecessaryMethods:
#             method_allowed = True
#         else:
#             if method in new_style_members:
#                 method_allowed = True
#             else:
#                 method_allowed = False
#
#         if method_allowed:
#             data = getattr(oldStyleObject, method)
#             setattr(newStyleObject, method, data)

def load_old_class_to_the_new_one(source_object_of_old_class,
                                  destination_object_of_new_class,
                                  copy_all_unnecessary_methods=False,
                                  has_list_of_methods=False,
                                  ignore_protected_methods=False):
    new_style_members = None
    if not copy_all_unnecessary_methods:
        if has_list_of_methods:
            new_style_members = destination_object_of_new_class.previouslyKnownSetOfMethodsToCopyAnObject
        else:
            new_style_members = dir(destination_object_of_new_class)

    list_of_old_style_object_methods = None
    if has_list_of_methods:
        list_of_old_style_object_methods = source_object_of_old_class.previouslyKnownSetOfMethodsToCopyAnObject
    else:
        list_of_old_style_object_methods = dir(source_object_of_old_class)

    template = None
    template_size = 0
    if ignore_protected_methods:
        template = '_'
        template_size = 1
    else:
        template = '__'
        template_size = 2
    method_allowed = False
    for attr in list_of_old_style_object_methods:
        if has_list_of_methods:
            method_allowed = True
        else:
            if (not callable(attr)) and (template != attr[:template_size]):
                method_allowed = True

        if method_allowed:
            if copy_all_unnecessary_methods:
                method_allowed = True
            else:
                if attr in new_style_members:
                    method_allowed = True
                else:
                    method_allowed = False

        if method_allowed:
            data = getattr(source_object_of_old_class, attr)
            setattr(destination_object_of_new_class, attr, data)


def bisect_search(data, max_value):
    result = tuple()

    min_tags_qnt = 2
    needed_items_qnt = 100
    left_bound = 0
    previous_left_bound = left_bound
    right_bound = len(data) - 1
    previous_right_bound = right_bound

    if (right_bound - left_bound) >= 1:
        # find right boundary
        while (right_bound - left_bound) > 0:
            if data[right_bound] > max_value:
                right_bound = previous_right_bound
                break
            previous_right_bound = right_bound
            diff = round(abs(right_bound - left_bound) / 2)
            if diff < 1:
                diff = 1
            right_bound -= diff
            if right_bound < left_bound:
                right_bound = left_bound

        # find left boundary
        while (right_bound - left_bound) > 0:
            if data[left_bound] <= max_value:
                left_bound = previous_left_bound
                break
            previous_left_bound = left_bound
            diff = round(abs(right_bound - left_bound) / 2)
            if diff < 1:
                diff = 1
            left_bound += diff
            if left_bound > right_bound:
                left_bound = right_bound

    if (right_bound - left_bound) > 1:
        # recursive
        result = bisect_search(data[left_bound:right_bound], max_value)
    else:
        result = (left_bound, right_bound)

    return result


def str_to_base64str(string_data):
    result = base64.b64encode(str(string_data).encode()).decode()
    return result


def base64str_to_str(base64string_data):
    result = base64.b64decode(str(base64string_data).encode()).decode()
    return result


def make_readable_json(json_string):
    result = json.dumps(json.loads(json_string), indent=4)
    return result


def current_line():
    (frame, filename, line_number, function_name, lines, index) = getouterframes(currentframe())[1]
    result = (filename, function_name, line_number, lines, index)
    return result


# class IsOK_BlockFailed(Exception): pass
#
#
# class IsOK_Closed(Exception):
#     '''
#     is_ok considers it ordinary external exception
#     '''
#     def __init__(self, _is_ok_runner__context_holder, _is_ok_runner__block_id, _is_ok_runner__block_info):
#         super(IsOK_Closed, self).__init__('Content Holder is closed. '
#                                           'Content Holder ID: {}; '
#                                           'Content Holder Info: {}; '
#                                           'Block ID: {}; '
#                                           'Block Info {}'.format(str(_is_ok_runner__context_holder._context_holder_id),
#                                                                  str(_is_ok_runner__context_holder._context_holder_info),
#                                                                  str(_is_ok_runner__block_id),
#                                                                  str(_is_ok_runner__block_info)))
#         self._is_ok_runner__context_holder = _is_ok_runner__context_holder
#         self._is_ok_runner__block_id = _is_ok_runner__block_id
#         self._is_ok_runner__block_info = _is_ok_runner__block_info
#
#
# class ResultExistence:
#     def __init__(self, existence, result):
#         self.existence = existence
#         self.result = result
#
#     def __bool__(self):
#         return self.existence
#
#     def __nonzero__(self):
#         return self.__bool__()
#
#     def __str__(self):
#         return '{}: {}'.format(self.existence, self.result)
#
#
# class ResultCache(ResultExistence):
#     def __init__(self):
#         super(ResultCache, self).__init__(False, None)
#
#     def __call__(self, *args, **kwargs):
#         self.existence = False
#
#     def get(self):
#         return self.result
#
#     def set(self, new_result):
#         self.existence = True
#         self.result = new_result
#
#
# class ResultType:
#     def __init__(self, type_id, result):
#         self.type_id = type_id
#         self.result = result
#
#     def __eq__(self, other):
#         # "__ne__() delegates to __eq__() and inverts the result"
#         # if type(other) == ResultType:
#         if isinstance(other, ResultType):
#             return self.type_id == other.type_id
#         else:
#             return self.type_id == other
#
#
# class CriteriaType(Enum):
# # class CriteriaType():  # much more efficient than Enum inheritance
#     needed = 0  # only set of this blocks is needed
#     optional = 1  # all blocks are needed except of this set of blocks
#     any = 2  # any result will fit criteria
#     forbidden = 3  # set of this blocks should not be done
#
#
# class IsOK_HistoryExport(Exception):
#     def __init__(self, history, process_error_result=True):
#         super(IsOK_HistoryExport, self).__init__('')
#         self.history = history
#         self.process_error_result = process_error_result
#
#
# class IsOK_IntenalResult():
#     def __init__(self, type_id, str_data, data):
#         self.type_id = type_id
#         self.str_data = str_data
#         self.data = data
#
#     def __str__(self):
#         return self.str_data
#
#
# class IsOK_IntenalResultType(Enum):
# # class CriteriaType():  # much more efficient than Enum inheritance
#     built_in_exception__is_ok_block_failed = 0
#     built_in_exception__bad_history_import = 1
#     external_exception = 2
#     block_did_not_returned_an_answer = 3
#
#
# class IsOK_ContextHolder:
#     def __init__(self, context_holder_id=None, context_holder_info=None, global_block_results_criteria=None,
#                  raise_exceptions=False, save_debug_trace=False, closeable=True):
#         '''
#
#         :param context_holder_id:
#         :param context_holder_info:
#         :param global_block_results_criteria: will be set to ResultType(CriteriaType.optional, set()) if None;
#             in this case all blocks are required.
#         :param raise_exceptions:
#         :param save_debug_trace:
#         :param closeable:
#         :return:
#         '''
#         # Use only ResultType(CriteriaType.optional, ...) or ResultType(CriteriaType.needed, set()).
#         # Other will be ignored here.
#         # You may use global_block_results_criteria=ResultType(CriteriaType.optional, set()) to create criteria
#         # "no fails in any block"
#         self._context_holder_id = context_holder_id
#         self._context_holder_info = context_holder_info
#         self._internal_blocks_index = IDGenerator.IDGenerator()
#         self._criteria_list = list()
#         global_block_results_criteria = global_block_results_criteria or ResultType(CriteriaType.optional, set())
#         if global_block_results_criteria is not None:
#             self._criteria_list.append(global_block_results_criteria)
#         self._raise_exceptions = raise_exceptions
#         self._save_debug_trace = save_debug_trace
#         self._closeable = closeable
#         self._full_history = list()
#         self._blocks_library = dict()
#         self._all_made_blocks = set()
#         self._good_blocks = set()
#         self._bad_blocks = set()
#
#         self._current_block_id = None
#         self._current_block_info = None
#         self._current_block_result = None
#         self._closed = False
#
#         self._bool_result = ResultCache()
#
#     # def _push_criteria(self, set_of_needed_blocks=None, set_of_optional_blocks=None):
#     def _push_criteria(self, _is_ok_runner__block_results_criteria):
#         # Do not use!
#         self._bool_result()
#         self._criteria_list.append(_is_ok_runner__block_results_criteria)
#
#     def _pop_criteria(self):
#         # Do not use!
#         # May raise exception if len(self.criteria_list)==0, but this is OK.
#         self._bool_result()
#         return self._criteria_list.pop()
#
#     def read_criteria(self):
#         criteria = None
#         if self._criteria_list:
#             criteria = self._criteria_list[-1]
#         return criteria
#
#     def _push_block_info(self, _is_ok_runner__block_id, _is_ok_runner__block_info=None):
#         self._current_block_id = _is_ok_runner__block_id
#         self._current_block_info = _is_ok_runner__block_info
#         self._current_block_result = None
#
#     def _pop_block_info(self):
#         self._current_block_id = None
#         self._current_block_info = None
#         self._current_block_result = None
#
#     def push_result(self, bool_result, info_or_data=None):
#         self._current_block_result = (bool_result, info_or_data)
#
#     def push_result_c(self, result):
#         # "class" version: to use when result = ResultExistence()
#         self._current_block_result = (result.existence, result.result)
#
#     def read_block_result_link(self, _is_ok_runner__block_id):
#         # result is NOT protected from changing!
#         original_result_data = self._blocks_library[_is_ok_runner__block_id][3]
#         result = ResultExistence(original_result_data[0], original_result_data[1])
#         # result = self._blocks_library[_is_ok_runner__block_id][3]
#         return result
#
#     def read_block_result_copy(self, _is_ok_runner__block_id):
#         original_result_data = self._blocks_library[_is_ok_runner__block_id][3]
#         result = ResultExistence(original_result_data[0], copy.copy(original_result_data[1]))
#         return result
#
#     def read_block_result_deepcopy(self, _is_ok_runner__block_id):
#         original_result_data = self._blocks_library[_is_ok_runner__block_id][3]
#         result = ResultExistence(original_result_data[0], copy.deepcopy(original_result_data[1]))
#         return result
#
#     def _save_block_result(self):
#         self._bool_result()
#         import_depth = 0
#         full_block_info = (self._internal_blocks_index.get_new_ID(), self._current_block_id, self._current_block_info,
#                            self._current_block_result, import_depth)
#         self._full_history.append(full_block_info)
#         self._blocks_library[self._current_block_id] = full_block_info
#         self._all_made_blocks.add(self._current_block_id)
#         if self._current_block_result[0]:
#             self._good_blocks.add(self._current_block_id)
#         else:
#             self._bad_blocks.add(self._current_block_id)
#
#     def __bool__(self):
#         if self._bool_result:
#             return self._bool_result.get()
#         else:
#             current_criteria = self.read_criteria()
#             result = True
#             if CriteriaType.needed == current_criteria:
#                 if len(current_criteria.result) != len(current_criteria.result & self._good_blocks):
#                     result = False
#             elif CriteriaType.optional == current_criteria:
#                 if len(self._bad_blocks - current_criteria.result) != 0:
#                     result = False
#             elif CriteriaType.any == current_criteria:
#                 result = True
#             elif CriteriaType.forbidden == current_criteria:
#                 if len(current_criteria.result) != len(current_criteria.result & self._bad_blocks):
#                     result = False
#             self._bool_result.set(result)
#             return result
#
#     def __nonzero__(self):
#         return self.__bool__()
#
#     @staticmethod
#     def _block_list_to_str(block_list):
#         blocks_str = ',\n'.join('(index({}), depth({}), ID({}), INFO({}), RESULT({}))'.format(str(block[0]),
#                                                                                               str(block[4]),
#                                                                                               str(block[1]),
#                                                                                               str(block[2]),
#                                                           '({}, {})'.format(str(block[3][0]), str(block[3][1])))
#                                 for block in block_list)
#         return blocks_str
#
#     def _block_str_to_context_holder_str(self, blocks_str):
#         full_string = '{{{{CONTEXT_HOLDER_ID({}): CONTEXT_HOLDER_INFO({})}}:[\n{}\n]}}'.format(
#             self._context_holder_id, self._context_holder_info, blocks_str)
#         return full_string
#
#     def get_bad_blocks(self):
#         result = list()
#         for block in self._full_history:
#             if not block[3][0]:
#                 result.append(block)
#         return result
#
#     def get_bad_blocks_str(self):
#         bad_blocks = self.get_bad_blocks()
#         full_history_str = self._block_list_to_str(bad_blocks)
#         full_string = self._block_str_to_context_holder_str(full_history_str)
#         return full_string
#
#     def raise_bad_blocks(self):
#         raise IsOK_HistoryExport(self.get_bad_blocks())
#
#     def raise_full_history(self):
#         raise IsOK_HistoryExport(self._full_history)
#
#     def process_history_import(self, his_ex):
#         history = his_ex.history
#         for block in history:
#             full_block_info = (self._internal_blocks_index.get_new_ID(), block[1], block[2],
#                                block[3], block[4] + 1)
#             self._full_history.append(full_block_info)
#
#     def _is_ok_reader_runner__close(self):
#         self._closed = True
#
#     def _reopen(self):
#         self._closed = False
#
#     def __str__(self):
#         full_history_str = self._block_list_to_str(self._full_history)
#         full_string = self._block_str_to_context_holder_str(full_history_str)
#         return full_string
#
#
# @contextmanager
# def is_ok(_is_ok_runner__context_holder, _is_ok_runner__block_id, _is_ok_runner__block_info=None, _is_ok_runner__block_results_criteria=None):
#     # _is_ok_runner__context_holder=IsGood_ContextHolder()
#
#     if _is_ok_runner__context_holder._closeable and _is_ok_runner__context_holder._closed:
#         raise IsOK_Closed(_is_ok_runner__context_holder, _is_ok_runner__block_id, _is_ok_runner__block_info)
#
#     _is_ok_runner__context_holder._push_block_info(_is_ok_runner__block_id, _is_ok_runner__block_info)
#     if _is_ok_runner__block_results_criteria is not None:
#         _is_ok_runner__context_holder._push_criteria(_is_ok_runner__block_results_criteria)
#     try:
#         # yield _is_ok_runner__context_holder
#         # yield (bool(_is_ok_runner__context_holder), _is_ok_runner__context_holder)
#         # yield ResultExistence(bool(_is_ok_runner__context_holder), _is_ok_runner__context_holder)
#         # yield _is_ok_runner__context_holder  # bool result is cached inside the object
#         # yield  # just use _is_ok_runner__context_holder
#
#         # if _is_ok_runner__context_holder:
#         #     yield _is_ok_runner__context_holder
#         # else:
#         #     pass  # Will raise RuntimeError("generator didn't yield") !
#
#         yield _is_ok_runner__context_holder
#     except IsOK_BlockFailed as exc:
#         result_info = None
#         if exc.args:
#             result_info = exc.args[0]
#         _is_ok_runner__context_holder.push_result(False, IsOK_IntenalResult(
#                 IsOK_IntenalResultType.built_in_exception__is_ok_block_failed,
#                 'ISOK. BUILT-IN EXCEPTION: IsOK_BlockFailed ({})'.format(result_info), result_info))
#     except IsOK_HistoryExport as export:
#         _is_ok_runner__context_holder.process_history_import(export)
#         if export.process_error_result:
#             _is_ok_runner__context_holder.push_result(False, IsOK_IntenalResult(
#                     IsOK_IntenalResultType.built_in_exception__bad_history_import,
#                     'ISOK. BUILT-IN EXCEPION: BAD HISTORY IMPORT EXCEPTION', None))
#     except:
#         exc = sys.exc_info()
#         exception = exc
#         error_str = '{} {}'.format(str(exception[0]), str(exception[1].args[0]))
#         # print('+++', error_str)
#         formattedTraceback = traceback.format_exception(exception[0], exception[1], exception[2])
#         exception = exception[:2] + (formattedTraceback,)
#         trace_str = ''.join(exception[2])
#         if _is_ok_runner__context_holder._save_debug_trace:
#             result_string = 'ISOK. EXTERNAL EXCEPION WITH TRACE:{} TRACE:{}'.format(error_str, trace_str)
#         else:
#             result_string = 'ISOK. EXTERNAL EXCEPION: {} '.format(error_str)
#         _is_ok_runner__context_holder.push_result(False, IsOK_IntenalResult(
#                 IsOK_IntenalResultType.external_exception, result_string, exc))
#         # print(result_string)
#         # _is_ok_runner__context_holder.push_result(False, sys.exc_info()[1])
#         if _is_ok_runner__context_holder._raise_exceptions:
#             _is_ok_runner__context_holder.raise_bad_blocks()
#             # raise
#     else:
#         if _is_ok_runner__context_holder._current_block_result is None:
#             # _is_ok_runner__context_holder.push_result(True)
#             _is_ok_runner__context_holder.push_result(False, IsOK_IntenalResult(
#                     IsOK_IntenalResultType.block_did_not_returned_an_answer,
#                     'ISOK. BLOCK DID NOT RETURNED AN ANSWER', None))
#     finally:
#         _is_ok_runner__context_holder._save_block_result()
#         if _is_ok_runner__block_results_criteria is not None:
#             _is_ok_runner__context_holder._pop_criteria()
#         _is_ok_runner__context_holder._pop_block_info()
#
#
# @contextmanager
# def is_ok_reader(_is_ok_runner__context_holder, _is_ok_runner__block_results_criteria=None, _is_ok_reader_runner__close=False):
#     if _is_ok_runner__block_results_criteria is not None:
#         _is_ok_runner__context_holder._push_criteria(_is_ok_runner__block_results_criteria)
#     try:
#         yield _is_ok_runner__context_holder
#     except:
#         raise
#     finally:
#         if _is_ok_runner__block_results_criteria is not None:
#             _is_ok_runner__context_holder._pop_criteria()
#         if _is_ok_reader_runner__close:
#             _is_ok_runner__context_holder._is_ok_reader_runner__close()
#
#
# def with_chain_example():
#     function_context = IsOK_ContextHolder('Test Holder', 'Some holder', ResultType(CriteriaType.optional, set()))
#
#     with is_ok(function_context, 'main loop'):
#         if function_context:
#             for index in range(10):
#                 context = IsOK_ContextHolder('Test Holder', 'Some holder', ResultType(CriteriaType.forbidden, {'1'}))
#
#                 with is_ok(context, 0):
#                     if context:
#                         result = 2*3
#                         context.push_result(True, result)
#
#                 try:
#                     with is_ok(context, '1'):
#                         if context:
#                             result = 54 / 0
#                             context.push_result(True, result)
#                 except ZeroDivisionError:
#                     print('Ops: ZeroDivisionError')
#
#                 with is_ok(context, 2):
#                     if context:
#                         result = 14
#                         context.push_result(True, result)
#                     else:
#                         raise IsOK_BlockFailed('Something went wrong.')
#
#                 try:
#                     with is_ok(context, '2'):
#                         if context:
#                             result = 54 / index
#                             context.push_result(True, result)
#                 except ZeroDivisionError:
#                     print('Ops: ZeroDivisionError')
#
#                 with is_ok(context, 'Hello', None, ResultType(CriteriaType.needed, set())):
#                     if context:
#                         result = 100 / 5
#                         context.push_result(True, result)
#
#                 with is_ok(context, 'Sum', None, ResultType(CriteriaType.forbidden, {0, 2})):
#                     if context:
#                         result = context.read_block_result_link(0).result + context.read_block_result_link(2).result
#                         context.push_result(True, result)
#                     else:
#                         context.push_result(False, 'Did not fit criteria because of "{}" in 2 block'.format(
#                             context.read_block_result_link(2).result))
#
#                 with is_ok(context, 'Mul', None, ResultType(CriteriaType.needed, {0, 'Hello'})):
#                     if context:
#                         result = context.read_block_result_link(0).result * context.read_block_result_link('Hello').result
#                         context.push_result(True, result)
#
#                 with is_ok(context, 'print1', None, ResultType(CriteriaType.needed, {'Sum'})):
#                     if context:
#                         print('Sum: {}'.format(context.read_block_result_link('Sum').result))
#                     else:
#                         print('Sum was not computed because of "{}" in "Sum" block.'.format(
#                             context.read_block_result_link('Sum').result
#                         ))
#
#                 with is_ok(context, 'print2', None, ResultType(CriteriaType.needed, {'Mul'})):
#                     if context:
#                         print('Mul: {}'.format(context.read_block_result_link('Mul').result))
#
#                 with is_ok(context, 'GlobalSum', None, ResultType(CriteriaType.needed, set())):
#                     if context:
#                         interesting_results = {0, 'Sum', 'Mul'}
#                         global_sum = 0
#                         for interesting_result in interesting_results:
#                             if context.read_block_result_link(interesting_result):
#                                 global_sum += context.read_block_result_link(interesting_result).result
#
#                         print('GlobalSum of ({}): {}'.format(', '.join(str(x) for x in interesting_results), global_sum))
#                         context.push_result(True, global_sum)
#
#                 with is_ok(context, 'GlobalSum2'):
#                     interesting_results = {0, 'Sum', 'Mul'}
#                     global_sum = 0
#                     for interesting_result in interesting_results:
#                         if context.read_block_result_link(interesting_result):
#                             global_sum += context.read_block_result_link(interesting_result).result
#
#                     print('GlobalSum2 of ({}): {}'.format(', '.join(str(x) for x in interesting_results), global_sum))
#                     context.push_result(True, global_sum)
#
#                 print('>> {}'.format(index))
#                 print(str(context))
#                 print()
#
#                 with is_ok_reader(context):
#                     if context:
#                         print()
#                         print('Everything is fine: result fit criteria of current reader block: '
#                               '"ResultType(CriteriaType.forbidden, {\'1\'})"!')
#                         print()
#                     else:
#                         context.raise_bad_blocks()
#
#                 with is_ok_reader(context, ResultType(CriteriaType.forbidden, {'2'})):
#                     if context:
#                         print()
#                         print('Everything is fine: result fit criteria of current reader block: '
#                               '"ResultType(CriteriaType.forbidden, {\'2\'})"!')
#                         print()
#                     else:
#                         print()
#                         print('Everything is NOT fine: did not fit default criteria set in context constructor: '
#                               '"ResultType(CriteriaType.optional, set())"!')
#                         print()
#                         context.raise_bad_blocks()
#
#     with is_ok_reader(function_context):
#         if function_context:
#             print()
#             print('Everything is fine!')
#             print()
#         else:
#             print()
#             print('Oh! There are errors in Main Loop! Interesting!')
#             print()
#             print(str(function_context))
#             print()


def isn(parameter, value):
    '''
    usage: k = isn(k, 'default')
    alternative: if k is not None: k = 'default'
    :param parameter:
    :param value:
    :return:
    '''
    # if parameter is None:
    #     return value
    # else:
    #     return parameter
    return parameter or value


def bytes__to__hex_string(input_data, delimiter=None):
    delimiter = none_or(delimiter, ' ')
    # 48508.80358249831 inputs per second
    fake_start = '00'
    fake_start_len = len(fake_start)
    hex_string = fake_start + binascii.hexlify(input_data).decode()
    result = delimiter.join(map(''.join, zip(*[iter(hex_string)]*2)))[fake_start_len:]
    result = result.strip()
    return result


if 'PyPy' == PLATFORM_NAME:
    def hex_string__to__bytes(input_data, delimiter=None):
        delimiter = none_or(delimiter, ' ')
        result = b''.join(binascii.unhexlify(b.encode()) for b in input_data.split(delimiter))
        return result
else:
    def hex_string__to__bytes(input_data, delimiter=None):
        delimiter = none_or(delimiter, ' ')
        result = b''.join(binascii.unhexlify(b) for b in input_data.split(delimiter))
        return result


if 'PyPy' == PLATFORM_NAME:
    def solid_hex_string__to__bytes(input_data):
        return binascii.unhexlify(input_data.encode())
else:
    def solid_hex_string__to__bytes(input_data):
        return binascii.unhexlify(input_data)


# def bytes_to_int(data):
#     int_data = int.from_bytes(data, byteorder='little', signed=False)
#     return int_data


def int_to_bytes(int_data):
    '''
    For a 32 bit signed int in little endian
    :param int_data:
    :return: bytes(); len == 4
    '''
    result = struct.pack('<i', int_data)
    return result


def bytes_to_int(bytes_data):
    '''
    For a 32 bit signed int in little endian
    :param bytes_data:
    :return:
    '''
    result = struct.unpack('<i', bytes_data)[0]
    return result


def short_to_bytes(short_data):
    '''
    For a 16 bit signed short in little endian
    :param short_data:
    :return: bytes(); len == 2
    '''
    result = struct.pack('<h', short_data)
    return result


def bytes_to_short(bytes_data):
    '''
    For a 16 bit signed short in little endian
    :param bytes_data:
    :return:
    '''
    result = struct.unpack('<h', bytes_data)[0]
    return result


def byte_to_bytes(byte_data):
    '''
    For a 8 bit signed byte
    :param byte_data:
    :return: bytes(); len == 2
    '''
    result = struct.pack('<b', byte_data)
    return result


def bytes_to_byte(bytes_data):
    '''
    For a 8 bit signed byte
    :param bytes_data:
    :return:
    '''
    result = struct.unpack('<b', bytes_data)[0]
    return result


def float_to_bytes(float_data):
    '''
    For a 32 bit signed ieee 754 floating points
    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python
    :param float_data:
    :return: bytes() with len == 4
    '''
    result = struct.pack('f', float_data)
    return result


def bytes_to_float(bytes_data):
    '''
    For a 32 bit signed ieee 754 floating points
    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python
    :param bytes_data: bytes() with len == 4
    :return:
    '''
    result = struct.unpack('f', bytes_data)[0]
    return result


def hex_dword_to_int(dword, byteorder=None, signed=False):
    '''
    "0x008A151D" is big endian; so dword = '008A151D', byteorder = 'big'
    :param dword: str(); '008A151D'
    :param byteorder: str(); 'big' / 'little'
    :param signed: bool();
    :return: 9049373
    '''
    byteorder = byteorder or 'big'
    bin_dword = binascii.unhexlify(dword)
    result = int.from_bytes(bin_dword, byteorder=byteorder, signed=signed)
    return result


def int_to_hex_dword(int_value, byteorder=None, signed=False):
    byteorder = byteorder or 'big'
    result = (binascii.hexlify(int_value.to_bytes(4, byteorder=byteorder, signed=signed))).decode()
    return result


def split_solid_hex_string(hex_string, delimiter=None):
    delimiter = none_or(delimiter, ' ')
    fake_start = '00'
    fake_start_len = len(fake_start)
    hex_string = fake_start + hex_string
    result = delimiter.join(map(''.join, zip(*[iter(hex_string)]*2)))[fake_start_len:]
    result = result.strip()
    return result


def get_text_in_brackets(data, left_b, right_b):
    # TODO: если в строке не найдена закрывающая скобка - последний символ строки будет удален. Проверить, не ломает ли
    # такое поведение алгоритмы в частности в upk-утилитах и в UCB-компиляторе
    left_offset = data.find(left_b)
    data = data[left_offset + len(left_b):]
    right_offset = data.find(right_b)
    data = data[:right_offset]
    return data


def get_text_in_brackets_offset(data, left_b, right_b, offset=0):
    # TODO: если в строке не найдена закрывающая скобка - последний символ строки будет удален. Проверить, не ломает ли
    # такое поведение алгоритмы в частности в upk-утилитах и в UCB-компиляторе
    result = None
    result_data = None
    result_offset = None
    if offset > 0:
        data = data[offset:]
    left_b_len = len(left_b)
    right_b_len = len(right_b)
    left_offset = data.find(left_b)
    data = data[left_offset + left_b_len:]
    right_offset = data.find(right_b)
    result_data = data[:right_offset]
    result_offset = offset + left_offset + left_b_len + right_offset + right_b_len
    result = (result_data, result_offset)
    return result


def get_slice_from_array(data, offset, size):
    result = data[offset: offset + size]
    return result


def parse_cmd_input_dir_list(search_dir_list_raw):
    '''
    :param search_dir_list_raw: search_dir_list_raw = input('Choose a search dir (S:\\ome\\Dir\\Name) or
        (["S:\\ome\\Dir"], ["D:\\ir"], ["K:"]): ')
    :return:
    '''
    search_dir_list = list()
    if '"' in search_dir_list_raw:
        while '"' in search_dir_list_raw:
            result = get_text_in_brackets_offset(search_dir_list_raw, '["', '"]')
            another_dir_name = result[0].strip()
            offset = result[1]
            if len(another_dir_name) > 0:
                search_dir_list.append(another_dir_name)
            search_dir_list_raw = search_dir_list_raw[offset:]
    else:
        search_dir_list.append(search_dir_list_raw.strip())
    return search_dir_list


def dict_by_id_list_limiter(dict_data, list_data, limit, max_limit):
    result_dict = dict_data
    result_list = list_data
    list_data_len = len(list_data)
    keys_to_delete = None
    if list_data_len > max_limit:
        keys_to_delete = list_data[:list_data_len - limit]
        result_list = list_data[list_data_len - limit:]
    if keys_to_delete is not None:
        for key_to_delete in keys_to_delete:
            # del result_dict[key_to_delete]
            if key_to_delete in result_dict:
                del result_dict[key_to_delete]
            else:
                # print('WRONG:', key_to_delete, '; ', result_dict.items())
                pass
    result_data = (result_dict, result_list)
    return result_data


def check_int_value(value, value_size=4):
    hi_value = 0
    lo_value = 0
    if value_size == 1:
        hi_value = 127
        lo_value = -128
    elif value_size == 2:
        hi_value = 32767
        lo_value = -32768
    elif value_size == 3:
        hi_value = 8388607
        lo_value = -8388608
    elif value_size == 4:
        hi_value = 2147483647
        lo_value = -2147483648
    if value < lo_value:
        value = lo_value
    if value > hi_value:
        value = hi_value
    return value


class BaseClassSettings:
    def check(self):
        pass


def none_or(input_value, default_value):
    '''
    {value = input_value or default_value} will not work when for example {value = '' or b''}
    :param input_value:
    :param default_value:
    :return:
    '''
    if input_value is None:
        return default_value
    else:
        return input_value
