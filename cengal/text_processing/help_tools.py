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

from cengal.code_flow_control.smart_values.versions.v_0 import ResultExistence
import string
from cengal.data_manipulation.help_tools import ubyte_to_bytes, get_slice_from_array
from typing import Tuple, Union

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


class AbstractSetOfSymbols:
    def __init__(self):
        self.ascii_word_delimiters = None
        self.ascii_word_delimiters__bytes = None
        self.ascii_word_delimiters__set = None
        self.ascii_word_delimiters__set_bytes = None

        # without "_" symbol
        self.ascii_modern_word_delimiters = None
        self.ascii_modern_word_delimiters__bytes = None
        self.ascii_modern_word_delimiters__set = None
        self.ascii_modern_word_delimiters__set_bytes = None


class SetOfSymbols(AbstractSetOfSymbols):
    def __init__(self):
        super(SetOfSymbols, self).__init__()
        self.ascii_word_delimiters = string.punctuation + string.whitespace
        self.ascii_word_delimiters__bytes = self.ascii_word_delimiters.encode()
        self.ascii_word_delimiters__set = set(self.ascii_word_delimiters)
        self.ascii_word_delimiters__set_bytes = set()
        for delim_char in self.ascii_word_delimiters__set:
            self.ascii_word_delimiters__set_bytes.add(delim_char.encode())

        self.ascii_modern_word_delimiters__set = set(self.ascii_word_delimiters__set)
        self.ascii_modern_word_delimiters__set.remove('_')
        self.ascii_modern_word_delimiters = ''.join(self.ascii_modern_word_delimiters__set)
        self.ascii_modern_word_delimiters__bytes = self.ascii_modern_word_delimiters.encode()
        self.ascii_modern_word_delimiters__set_bytes = set()
        for delim_char in self.ascii_modern_word_delimiters__set:
            self.ascii_modern_word_delimiters__set_bytes.add(delim_char.encode())


SET_OF_SYMBOLS = SetOfSymbols()


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


def find_substring(full_string: bytes, substring: bytes, offset: int=0)\
        ->Tuple[Union[None, int], Union[None, int]]:
    start_index = full_string.find(substring, offset)
    word_start = True
    if 0 > start_index:
        word_start = False

    end_index = start_index + len(substring)

    if not word_start:
        start_index = None
        end_index = None

    return start_index, end_index


def find_substring_full_word(full_string: bytes, substring: bytes, offset: int=0, smart_word_bounds: bool=False)\
        ->Tuple[ResultExistence, ResultExistence]:
    start_index = ResultExistence(False, 0)
    end_index = ResultExistence(False, None)

    while start_index.result is not None:
        start_index, end_index = find_substring_full_word__one_shot(full_string, substring, offset, smart_word_bounds)
        if start_index.result is not None:
            # substring was found
            if start_index and end_index:
                # full word was found
                break
            else:
                # need to continue search from the new offset
                offset = end_index.result
        else:
            # substring wasn't found
            break

    if start_index:
        start_index = start_index.result
    else:
        start_index = None

    if end_index:
        end_index = end_index.result
    else:
        end_index = None

    return start_index, end_index


class FindSubstringErrorFullStringCanNotBeEmpty(Exception):
    pass


class FindSubstringErrorSubstringCanNotBeEmpty(Exception):
    pass


def find_substring_full_word__one_shot(full_string: bytes, substring: bytes, offset: int=0,
                                       smart_word_bounds: bool=False)\
        ->Tuple[ResultExistence, ResultExistence]:
    delimiters = SET_OF_SYMBOLS.ascii_modern_word_delimiters__set_bytes

    word_start = ResultExistence(False, None)
    word_end = ResultExistence(False, None)

    if not full_string:
        return word_start, word_end
    if not substring:
        return word_start, word_end

    is_word_start_is_delimiter = False
    is_word_end_is_delimiter = False
    if smart_word_bounds:
        if ubyte_to_bytes(substring[0]) in delimiters:
            is_word_start_is_delimiter = True
        if ubyte_to_bytes(substring[-1]) in delimiters:
            is_word_end_is_delimiter = True

    word_start = ResultExistence(False, full_string.find(substring, offset))
    word_end = ResultExistence(False, None)

    if 0 > word_start.result:
        word_start.existence = False
        word_start.result = None
    else:
        if is_word_start_is_delimiter:
            word_start.existence = True
        elif 0 == word_start.result:
            word_start.existence = True
        elif ubyte_to_bytes(full_string[word_start.result - 1]) in delimiters:
            word_start.existence = True

    if word_start.result is not None:
        word_end.result = word_start.result + len(substring)
        full_string_len = len(full_string)
        if is_word_end_is_delimiter:
            word_start.existence = True
        elif word_end.result > full_string_len:
            word_end.existence = False
        elif word_end.result == full_string_len:
            word_end.existence = True
        elif ubyte_to_bytes(full_string[word_end.result]) in delimiters:
            word_end.existence = True

    return word_start, word_end


def check_is_slice_is_in_string(substring: bytes, full_string: bytes, check_whole_word=False,
                                smart_word_bounds: bool=False):
    if check_whole_word:
        word_start, word_end = find_substring_full_word(full_string, substring, smart_word_bounds=smart_word_bounds)
        if (word_start is not None) and (word_end is not None):
            return True
        else:
            return False
    else:
        return substring in full_string


def check_is_slice_is_in_string__case_insensitive(substring: bytes, full_string: bytes, check_whole_word=False,
                                                  smart_word_bounds: bool=False):
    return check_is_slice_is_in_string(substring.lower(), full_string.lower(), check_whole_word, smart_word_bounds)


def detach_all_slices_from_string(string, substring, function__detach=None, function__check_is_in=None):
    """
    :param string: input string
    :param substring: desired substring
    :param function__detach: detach_slice_from_string (when None) or detach_slice_from_string__case_insensitive
    :param function__check_is_in: check_is_slice_is_in_string (when None) or
        check_is_slice_is_in_string__case_insensitive
    :return: ([(original_string_part_0, string_slice), (original_string_part_1, string_slice), ...,
        (original_string_part_N, string_slice)], string_after)
    """
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


def is_printable(s, codec='utf8'):
    try:
        s.decode(codec)
    except UnicodeDecodeError:
        return False
    else: 
        return True


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

