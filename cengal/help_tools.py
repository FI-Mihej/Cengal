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

from cengal.system import PLATFORM_NAME, PYTHON_VERSION, PYTHON_VERSION_INT
from cengal.text_processing.help_tools import get_text_in_brackets_offset
from cengal.system import PLATFORM_NAME
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
from cengal.modules_management.alternative_import import alt_import

with alt_import('lzma') as lzma:
    if lzma is None:
        import lzmaffi.compat
        lzmaffi.compat.register()
        import lzma

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


def join_path_example(a, b):
    """
    k = os.path.join('D:\\Dev\\Workspace\\My', 'XCOM Modding\\NewHitDamageCalc', 'Long War\\15f\\.hg\\store', '00changelog.i')
    k == 'D:\\Dev\\Workspace\\My\\XCOM Modding\\NewHitDamageCalc\\Long War\\15f\\.hg\\store\\00changelog.i'
    :param a:
    :param b:
    :return:
    """
    os.path.join(a, b)


def json_to_printable_string(json_obj):
    result = json.dumps(json_obj, sort_keys=True, indent=4, separators=(',', ': '))
    return result


def make_readable_json(json_string):
    result = json.dumps(json.loads(json_string), indent=4)
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


def current_line():
    (frame, filename, line_number, function_name, lines, index) = getouterframes(currentframe())[1]
    result = (filename, function_name, line_number, lines, index)
    return result


def isn(parameter, value):
    """
    usage: k = isn(k, 'default')
    alternative: if k is not None: k = 'default'
    :param parameter:
    :param value:
    :return:
    """
    # if parameter is None:
    #     return value
    # else:
    #     return parameter
    return parameter or value


def parse_cmd_input_dir_list(search_dir_list_raw):
    """
    :param search_dir_list_raw: search_dir_list_raw = input('Choose a search dir (S:\\ome\\Dir\\Name) or
        (["S:\\ome\\Dir"], ["D:\\ir"], ["K:"]): ')
    :return:
    """
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


