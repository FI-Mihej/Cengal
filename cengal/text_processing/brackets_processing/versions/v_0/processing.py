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


__all__ = ['find_brackets', 'find_text_in_brackets', 'find_text_with_brackets', 'replace_text_in_brackets', 'replace_text_with_brackets']


from cengal.text_processing.text_processing import (
    Text, 
    find_text, 
    replace_slice, 
    DEFAULT_ENCODING, 
    find_word, 
    find_dev_word, 
    find_characters_impl, 
    find_any_spaces, 
    find_spaces_or_tabs, 
    find_spaces, 
    find_tabs, 
    find_universal_line_delimiter, 
    find_line_delimiter, 
    normalize_text_to_data, 
    )

from .brackets import *

import re

from typing import Optional, Tuple, Callable, List


def find_brackets(data: Text, brackets: BracketPair, 
                  start: Optional[int] = None, stop: Optional[int] = None, 
                  start_r: Optional[int] = None,
                  week_boundaries: bool = True,
                  encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Tuple[Optional[slice], Optional[slice]]:
    data_start_slice: slice = slice(0, 0)
    start: int = 0 if start is None else start
    end = len(data)
    data_end_slice: slice = slice(end, end)
    stop: int = end if stop is None else stop
    start_r = 0 if start_r is None else start_r
    if start_r < 0:
        start_r = end + start_r

    max_start = max(start, 0)
    max_start_slice = slice(max_start, max_start)
    min_end = min(end, stop)
    min_end_slice = slice(min_end, min_end)

    l_place = None
    for l_bracket in brackets.left:
        if l_bracket.text():
            temp_l_place = find_text(data, l_bracket.bracket_id, start, stop, encoding, normalizer)
            
            if l_place is None:
                l_place = temp_l_place
            elif temp_l_place is not None:
                if temp_l_place.start < l_place.start:
                    l_place = temp_l_place
                elif temp_l_place.start == l_place.start:
                    if temp_l_place.stop > l_place.stop:
                        l_place = temp_l_place
        elif l_bracket.word():
            word: Word = l_bracket.bracket_id
            if word.is_dev_word:
                temp_l_place = find_dev_word(data, word.text, start, stop, week_boundaries, word.forbidden_initial_chars, word.forbidden_final_chars, word.normalize_forbidden_chars, encoding, normalizer)
            else:
                temp_l_place = find_word(data, word.text, start, stop, week_boundaries, word.forbidden_initial_chars, word.forbidden_final_chars, word.normalize_forbidden_chars, encoding, normalizer)
            
            if l_place is None:
                l_place = temp_l_place
            elif temp_l_place is not None:
                if temp_l_place.start < l_place.start:
                    l_place = temp_l_place
                elif temp_l_place.start == l_place.start:
                    if temp_l_place.stop > l_place.stop:
                        l_place = temp_l_place
        elif l_bracket.regex():
            regex: Regex = l_bracket.bracket_id
            data_part_str: str = normalize_text_to_data(str(), data[start: stop], encoding, normalizer)
            result: re.Match = regex.compiled_regex.search(data_part_str)
            if result is None:
                temp_l_place = None
            else:
                result_span: Tuple[int, int] = result.span()
                data_part_left_str: str = data_part_str[:result_span[0]]
                data_part_left: Text = normalize_text_to_data(data, data_part_left_str, encoding, normalizer)
                data_part_left_len: int = len(data_part_left)
                data_part_middle_str: str = data_part_str[result_span[0]: result_span[1]]
                data_part_middle: Text = normalize_text_to_data(data, data_part_middle_str, encoding, normalizer)
                temp_l_place = slice(data_part_left_len, data_part_left_len + len(data_part_middle))
            
            if l_place is None:
                l_place = temp_l_place
            elif temp_l_place is not None:
                if temp_l_place.start < l_place.start:
                    l_place = temp_l_place
                elif temp_l_place.start == l_place.start:
                    if temp_l_place.stop > l_place.stop:
                        l_place = temp_l_place
        elif l_bracket.set_of_strings():
            set_of_strings: SetOfStrings = l_bracket.bracket_id
            temp_l_place = find_characters_impl(data, set_of_strings.sets_of_strings, set_of_strings.max_chars, start, stop, set_of_strings.sort_required_chars, set_of_strings.normalize_chars, encoding, normalizer)
            
            if l_place is None:
                l_place = temp_l_place
            elif temp_l_place is not None:
                if temp_l_place.start < l_place.start:
                    l_place = temp_l_place
                elif temp_l_place.start == l_place.start:
                    if temp_l_place.stop > l_place.stop:
                        l_place = temp_l_place
        elif l_bracket.special():
            special_type: BracketSpecialType = l_bracket.bracket_id
            if BracketSpecialType.any_spaces == special_type:
                temp_l_place = find_any_spaces(data, None, start, stop, encoding=encoding, normalizer=normalizer)
            elif BracketSpecialType.spaces_or_tabs == special_type:
                temp_l_place = find_spaces_or_tabs(data, None, start, stop, encoding=encoding, normalizer=normalizer)
            elif BracketSpecialType.spaces == special_type:
                temp_l_place = find_spaces(data, None, start, stop, encoding=encoding, normalizer=normalizer)
            elif BracketSpecialType.tabs == special_type:
                temp_l_place = find_tabs(data, None, start, stop, encoding=encoding, normalizer=normalizer)
            elif BracketSpecialType.universal_line_delimiter == special_type:
                temp_l_place = find_universal_line_delimiter(data, 1, start, stop, encoding=encoding, normalizer=normalizer)
            elif BracketSpecialType.line_delimiter == special_type:
                temp_l_place = find_line_delimiter(data, 1, start, stop, encoding=encoding, normalizer=normalizer)
            else:
                raise NotImplementedError(f'Wrong bracket id: {special_type} of type {type(special_type)}')
            
            if l_place is None:
                l_place = temp_l_place
            elif temp_l_place is not None:
                if temp_l_place.start < l_place.start:
                    l_place = temp_l_place
                elif temp_l_place.start == l_place.start:
                    if temp_l_place.stop > l_place.stop:
                        l_place = temp_l_place
        elif l_bracket.custom_text_finder():
            custom_text_finder: CustomTextFinder = l_bracket.bracket_id
            temp_l_place = custom_text_finder(data, start, stop, encoding, normalizer)
            
            if l_place is None:
                l_place = temp_l_place
            elif temp_l_place is not None:
                if temp_l_place.start < l_place.start:
                    l_place = temp_l_place
                elif temp_l_place.start == l_place.start:
                    if temp_l_place.stop > l_place.stop:
                        l_place = temp_l_place
        elif l_bracket.absent():
            if l_place is not None:
                break

            absent_type: BracketAbsentType = l_bracket.bracket_id
            if BracketAbsentType.data_bounds == absent_type:
                if 0 == start:
                    l_place = data_start_slice
                else:
                    l_place = None
            elif BracketAbsentType.accessible_data_bounds == absent_type:
                l_place = max_start_slice
            elif BracketAbsentType.data_bounds_start == absent_type:
                l_place = data_start_slice
            elif BracketAbsentType.data_bounds_end == absent_type:
                l_place = data_end_slice
            elif BracketAbsentType.accessible_data_bounds_start == absent_type:
                l_place = max_start_slice
            elif BracketAbsentType.accessible_data_bounds_end == absent_type:
                l_place = min_end_slice
            else:
                raise NotImplementedError(f'Wrong bracket id: {absent_type} of type {type(absent_type)}')

            if l_place is not None:
                break

    if brackets.right is None:
        if l_place is None:
            return None, None
        else:
            return l_place, slice(l_place.stop, l_place.stop)

    r_place = None
    for r_bracket in brackets.right:
        # if r_bracket.text():
        #     r_start: int = max((l_place or max_start_slice).stop, start_r)
        #     if r_bracket.is_word:
        #         if r_bracket.is_dev_word:
        #             temp_r_place = find_dev_word(data, r_bracket.bracket_id, r_start, stop, r_bracket.forbidden_initial_chars, r_bracket.forbidden_final_chars, r_bracket.normalize_forbidden_chars, encoding, normalizer)
        #         else:
        #             temp_r_place = find_word(data, r_bracket.bracket_id, r_start, stop, r_bracket.forbidden_initial_chars, r_bracket.forbidden_final_chars, r_bracket.normalize_forbidden_chars, encoding, normalizer)
        #     else:
        #         temp_r_place = find_text(data, r_bracket.bracket_id, r_start, stop, encoding, normalizer)
            
        #     if r_place is None:
        #         r_place = temp_r_place
        #     elif temp_r_place.start < r_place.start:
        #         r_place = temp_r_place
        #     elif temp_r_place.start == r_place.start:
        #         if temp_r_place.stop > r_place.stop:
        #             r_place = temp_r_place
        # else:
        if r_bracket.text():
            r_start: int = max((l_place or max_start_slice).stop, start_r)
            temp_r_place = find_text(data, r_bracket.bracket_id, r_start, stop, encoding, normalizer)
            
            if r_place is None:
                r_place = temp_r_place
            elif temp_r_place is not None:
                if temp_r_place.start < r_place.start:
                    r_place = temp_r_place
                elif temp_r_place.start == r_place.start:
                    if temp_r_place.stop > r_place.stop:
                        r_place = temp_r_place
        elif r_bracket.word():
            word: Word = r_bracket.bracket_id
            r_start: int = max((l_place or max_start_slice).stop, start_r)
            if word.is_dev_word:
                temp_r_place = find_dev_word(data, word.text, r_start, stop, week_boundaries, word.forbidden_initial_chars, word.forbidden_final_chars, word.normalize_forbidden_chars, encoding, normalizer)
            else:
                temp_r_place = find_word(data, word.text, r_start, stop, week_boundaries, word.forbidden_initial_chars, word.forbidden_final_chars, word.normalize_forbidden_chars, encoding, normalizer)
            
            if r_place is None:
                r_place = temp_r_place
            elif temp_r_place is not None:
                if temp_r_place.start < r_place.start:
                    r_place = temp_r_place
                elif temp_r_place.start == r_place.start:
                    if temp_r_place.stop > r_place.stop:
                        r_place = temp_r_place
        elif r_bracket.regex():
            regex: Regex = r_bracket.bracket_id
            r_start: int = max((l_place or max_start_slice).stop, start_r)
            data_part_str: str = normalize_text_to_data(str(), data[r_start: stop], encoding, normalizer)
            result: re.Match = regex.compiled_regex.search(data_part_str)
            if result is None:
                temp_r_place = None
            else:
                result_span: Tuple[int, int] = result.span()
                data_part_left_str: str = data_part_str[:result_span[0]]
                data_part_left: Text = normalize_text_to_data(data, data_part_left_str, encoding, normalizer)
                data_part_left_len: int = len(data_part_left)
                data_part_middle_str: str = data_part_str[result_span[0]: result_span[1]]
                data_part_middle: Text = normalize_text_to_data(data, data_part_middle_str, encoding, normalizer)
                temp_r_place = slice(data_part_left_len, data_part_left_len + len(data_part_middle))
            
            if l_place is None:
                l_place = temp_r_place
            elif temp_r_place is not None:
                if temp_r_place.start < l_place.start:
                    l_place = temp_r_place
                elif temp_r_place.start == l_place.start:
                    if temp_r_place.stop > l_place.stop:
                        l_place = temp_r_place
        elif r_bracket.set_of_strings():
            set_of_strings: SetOfStrings = r_bracket.bracket_id
            r_start: int = max((l_place or max_start_slice).stop, start_r)
            temp_r_place = find_characters_impl(data, set_of_strings.sets_of_strings, set_of_strings.max_chars, r_start, stop, set_of_strings.sort_required_chars, set_of_strings.normalize_chars, encoding, normalizer)
            
            if r_place is None:
                r_place = temp_r_place
            elif temp_r_place is not None:
                if temp_r_place.start < r_place.start:
                    r_place = temp_r_place
                elif temp_r_place.start == r_place.start:
                    if temp_r_place.stop > r_place.stop:
                        r_place = temp_r_place
        elif r_bracket.custom_text_finder():
            custom_text_finder: CustomTextFinder = l_bracket.bracket_id
            r_start: int = max((l_place or max_start_slice).stop, start_r)
            temp_r_place = custom_text_finder(data, r_start, stop, encoding, normalizer)
            
            if r_place is None:
                r_place = temp_r_place
            elif temp_r_place is not None:
                if temp_r_place.start < r_place.start:
                    r_place = temp_r_place
                elif temp_r_place.start == r_place.start:
                    if temp_r_place.stop > r_place.stop:
                        r_place = temp_r_place
        elif r_bracket.special():
            special_type: BracketSpecialType = r_bracket.bracket_id
            r_start: int = max((l_place or max_start_slice).stop, start_r)
            if BracketSpecialType.any_spaces == special_type:
                temp_r_place = find_any_spaces(data, None, r_start, stop, encoding=encoding, normalizer=normalizer)
            elif BracketSpecialType.spaces_or_tabs == special_type:
                temp_r_place = find_spaces_or_tabs(data, None, r_start, stop, encoding=encoding, normalizer=normalizer)
            elif BracketSpecialType.spaces == special_type:
                temp_r_place = find_spaces(data, None, r_start, stop, encoding=encoding, normalizer=normalizer)
            elif BracketSpecialType.tabs == special_type:
                temp_r_place = find_tabs(data, None, r_start, stop, encoding=encoding, normalizer=normalizer)
            elif BracketSpecialType.universal_line_delimiter == special_type:
                temp_r_place = find_universal_line_delimiter(data, 1, r_start, stop, encoding=encoding, normalizer=normalizer)
            elif BracketSpecialType.line_delimiter == special_type:
                temp_r_place = find_line_delimiter(data, 1, r_start, stop, encoding=encoding, normalizer=normalizer)
            else:
                raise NotImplementedError(f'Wrong bracket id: {special_type} of type {type(special_type)}')
            
            if r_place is None:
                r_place = temp_r_place
            elif temp_r_place is not None:
                if temp_r_place.start < r_place.start:
                    r_place = temp_r_place
                elif temp_r_place.start == r_place.start:
                    if temp_r_place.stop > r_place.stop:
                        r_place = temp_r_place
        elif r_bracket.absent():
            if r_place is not None:
                break

            if BracketAbsentType.data_bounds == r_bracket.bracket_id:
                if end <= start:
                    r_place = data_end_slice
                else:
                    r_place = None
            elif BracketAbsentType.accessible_data_bounds == r_bracket.bracket_id:
                if min_end <= start:
                    r_place = min_end_slice if min_end >= start_r else None
                else:
                    r_place = None
            elif BracketAbsentType.data_bounds_start == r_bracket.bracket_id:
                r_place = data_start_slice
            elif BracketAbsentType.data_bounds_end == r_bracket.bracket_id:
                r_place = data_end_slice if end >= start_r else None
            elif BracketAbsentType.accessible_data_bounds_start == r_bracket.bracket_id:
                r_place = max_start_slice if max_start >= start_r else None
            elif BracketAbsentType.accessible_data_bounds_end == r_bracket.bracket_id:
                r_place = min_end_slice if min_end >= start_r else None
            else:
                raise NotImplementedError(f'Wrong bracket id: {r_bracket.bracket_id} of type {type(r_bracket.bracket_id)}')

            if r_place is not None:
                break
    
    return l_place, r_place


def find_text_in_brackets(data: Text, 
                          brackets: BracketPair, 
                          start: int = 0, stop: Optional[int] = None, 
                          start_r: Optional[int] = None, 
                          week_boundaries: bool = True,
                          encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    l_place, r_place = find_brackets(data, brackets, start, stop, start_r, week_boundaries, encoding, normalizer)
    if (l_place is None) or (r_place is None):
        return None
    
    return slice(l_place.stop, r_place.start)


def find_text_with_brackets(data: Text, 
                            brackets: BracketPair, 
                            start: int = 0, stop: Optional[int] = None, 
                            start_r: Optional[int] = None, 
                            week_boundaries: bool = True,
                            encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    l_place, r_place = find_brackets(data, brackets, start, stop, start_r, week_boundaries, encoding, normalizer)
    if (l_place is None) or (r_place is None):
        return None
    
    return slice(l_place.start, r_place.stop)


def replace_text_in_brackets(data: Text, brackets: BracketPair, text: Text, count: int = -1, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Tuple[Text, List[Tuple[slice, slice]]]:
    """_summary_

    Args:
        data (Text): _description_
        brackets (BracketPair): _description_
        text (Text): _description_
        count (int, optional): The same purpose and behaviour as in str().replace(), bytes().replace(), bytearray().replace(). Defaults to -1.
        encoding (Optional[str], optional): _description_. Defaults to DEFAULT_ENCODING.
        normalizer (Optional[Callable], optional): _description_. Defaults to None.

    Returns:
        Tuple[Text, List[Tuple[slice, slice]]]: Result text and a list with replacements logs (an old slice, a new slice)
    """
    result: List[slice] = list()
    parts: List[Text] = list()
    iter = None if count < 0 else count
    while (iter is None) or (iter > 0):
        old_text_slice = find_text_in_brackets(data, brackets, encoding=encoding, normalizer=normalizer)
        if old_text_slice is None:
            break

        data, new_text_slice = replace_slice(data, old_text_slice, text, encoding=encoding, normalizer=normalizer)
        result.append((old_text_slice, new_text_slice))
        parts.append(data[:new_text_slice.stop])
        data = data[new_text_slice.stop:]
        iter = None if count < 0 else iter - 1
    
    parts.append(data)
    data = type(data)().join(parts)
    return data, result


def replace_text_with_brackets(data: Text, brackets: BracketPair, text: Text, count: int = -1, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Tuple[Text, List[Tuple[slice, slice]]]:
    """_summary_

    Args:
        data (Text): _description_
        brackets (BracketPair): _description_
        text (Text): _description_
        count (int, optional): The same purpose and behaviour as in str().replace(), bytes().replace(), bytearray().replace(). Defaults to -1.
        encoding (Optional[str], optional): _description_. Defaults to DEFAULT_ENCODING.
        normalizer (Optional[Callable], optional): _description_. Defaults to None.

    Returns:
        Tuple[Text, List[Tuple[slice, slice]]]: Result text and a list with replacements logs (an old slice, a new slice)
    """
    result: List[slice] = list()
    parts: List[Text] = list()
    iter = None if count < 0 else count
    while (iter is None) or (iter > 0):
        old_text_slice = find_text_with_brackets(data, brackets, encoding=encoding, normalizer=normalizer)
        if old_text_slice is None:
            break

        data, new_text_slice = replace_slice(data, old_text_slice, text, encoding=encoding, normalizer=normalizer)
        result.append((old_text_slice, new_text_slice))
        parts.append(data[:new_text_slice.stop])
        data = data[new_text_slice.stop:]
        iter = None if count < 0 else iter - 1

    parts.append(data)
    data = type(data)().join(parts)
    return data, result
