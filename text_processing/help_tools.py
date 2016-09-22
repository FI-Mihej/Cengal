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

from code_flow_control import ResultExistence

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


def detach_slice_from_string(string, substring, offset=0):
    slice_index = string.index(substring, offset)
    slice_size = len(substring)
    end_of_slice = slice_index + slice_size
    string_before = string[:slice_index]
    string_slice = string[slice_index:end_of_slice]
    string_after = string[end_of_slice:]
    result = (string_before, string_slice, string_after, end_of_slice)
    return result


def detach_slice_from_string__case_insensitive(string, substring, offset=0):
    lowercase_string = string.lower()
    lowercase_substring = substring.lower()
    slice_index = lowercase_string.index(lowercase_substring, offset)
    slice_size = len(substring)
    end_of_slice = slice_index + slice_size
    string_before = string[:slice_index]
    string_slice = string[slice_index:end_of_slice]
    string_after = string[end_of_slice:]
    result = (string_before, string_slice, string_after, end_of_slice)
    return result


def check_is_slice_is_in_string(substring, string):
    return substring in string


def check_is_slice_is_in_string__case_insensitive(substring, string):
    return substring.lower() in string.lower()


def detach_all_slices_from_string(string, substring, function__detach=None, function__check_is_in=None):
    '''
    :param string: input string
    :param substring: desired substring
    :param function__detach: detach_slice_from_string (when None) or detach_slice_from_string__case_insensitive
    :param function__check_is_in: check_is_slice_is_in_string (when None) or
        check_is_slice_is_in_string__case_insensitive
    :return: ([(original_string_part_0, string_slice), (original_string_part_1, string_slice), ...,
        (original_string_part_N, string_slice)], string_after)
    '''
    function__detach = function__detach or detach_slice_from_string
    function__check_is_in = function__check_is_in or check_is_slice_is_in_string

    result_list = list()
    result = function__detach(string, substring)
    last_string_after = result[2]
    new_result = (result[0], result[1])
    result_list.append(new_result)
    while function__check_is_in(substring, result[2]):
        result = function__detach(result[2], substring)
        last_string_after = result[2]
        new_result = (result[0], result[1])
        result_list.append(new_result)
    result = (result_list, last_string_after)
    return result


def detach_all_slices_from_string__case_insensitive(string, substring):
    return detach_all_slices_from_string(
        string, substring, detach_slice_from_string__case_insensitive, check_is_slice_is_in_string__case_insensitive)


def bytes_to_printable(bytes_data):
    result = str(bytes_data)[2:-1]
    return result


def levenshtein_distance(a, b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n

    current_row = range(n+1) # Keep current and previous row, not entire matrix
    for i in range(1, m+1):
        previous_row, current_row = current_row, [i]+[0]*n
        for j in range(1,n+1):
            add, delete, change = previous_row[j]+1, current_row[j-1]+1, previous_row[j-1]
            if a[j-1] != b[i-1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]
