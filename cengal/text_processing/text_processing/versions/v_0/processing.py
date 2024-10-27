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


__all__ = [
    'Text', 
    'BinText', 
    'DEFAULT_ENCODING', 
    'EncodingRequired', 
    'NotSupportedDataType', 
    'NotSupportedDesiredTextType', 
    'normalize_text', 
    'normalize_text_to_data', 
    'find_text', 
    'rfind_text', 

    'find_word_impl', 
    'find_word', 
    'find_dev_word', 
    'rfind_word_impl', 
    'rfind_word', 
    'rfind_dev_word', 

    'find_characters_impl', 
    'find_any_spaces', 
    'find_spaces_or_tabs', 
    'find_spaces', 
    'find_tabs', 
    'find_universal_line_delimiter', 
    'find_line_delimiter', 

    'rfind_characters_impl', 
    'rfind_any_spaces', 
    'rfind_spaces_or_tabs', 
    'rfind_spaces', 
    'rfind_tabs', 
    'rfind_universal_line_delimiter', 
    'rfind_line_delimiter', 

    'startswith_characters_impl', 
    'startswith_any_spaces', 
    'startswith_spaces_or_tabs', 
    'startswith_spaces', 
    'startswith_tabs', 
    'startswith_universal_line_delimiter', 
    'startswith_line_delimiter', 

    'endswith_characters_impl', 
    'endswith_any_spaces', 
    'endswith_spaces_or_tabs', 
    'endswith_spaces', 
    'endswith_tabs', 
    'endswith_universal_line_delimiter', 
    'endswith_line_delimiter', 

    'iterlines_impl', 
    'iterlines', 
    'iterlines_universal', 
    
    'replace_slice', 
    'replace_text', 
    'replace_word', 
    'replace_dev_word', 
    'normalize_line_separators', 
    'normalize_line_separators_and_tabs', 
    'removeprefix', 
    'removesuffix', 
    'to_identifier', 
    'remove_repetitive', 

    'ascii_newline_characters', 
    'ascii_newline_characters_set', 
    'unicode_newline_characters', 
    'unicode_newline_characters_set', 

    'ascii_space_characters', 
    'ascii_space_characters_set', 
    'ascii_special_characters', 
    'ascii_special_characters_set', 
    'ascii_punctuation_characters', 
    'ascii_punctuation_characters_set', 
    'ascii_digits', 
    'ascii_digits_set', 
    'unicode_space_characters', 
    'unicode_space_characters_set', 
    'unicode_space_characters_set_bytes', 
    'unicode_space_characters_list_bytearray', 

    'unicode_space_chars_sets_set_str', 
    'unicode_space_chars_sets_set_bytes', 
    'unicode_space_chars_sets_list_bytearray', 

    'space_or_tab_chars_sets_set_str', 
    'space_or_tab_chars_sets_set_bytes', 
    'space_or_tab_chars_sets_list_bytearray', 

    'space_chars_sets_set_str', 
    'space_chars_sets_set_bytes', 
    'space_chars_sets_list_bytearray', 

    'tab_chars_sets_set_str', 
    'tab_chars_sets_set_bytes', 
    'tab_chars_sets_list_bytearray', 

    'universal_line_delimiter_chars_sets_set_str', 
    'universal_line_delimiter_chars_sets_set_bytes', 
    'universal_line_delimiter_chars_sets_list_bytearray', 

    'line_delimiter_chars_sets_set_str', 
    'line_delimiter_chars_sets_set_bytes', 
    'line_delimiter_chars_sets_list_bytearray', 

    'forbidden_initial_chars_set', 
    'forbidden_initial_ascii_chars_set', 
    'forbidden_initial_chars_list', 
    'forbidden_initial_ascii_chars_list', 
    'forbidden_initial_chars', 
    'forbidden_initial_ascii_chars_bytes', 
    'forbidden_initial_ascii_chars_bytearray', 

    'forbidden_initial_chars_set_bytes', 
    'forbidden_initial_chars_list_bytearray', 

    'forbidden_final_chars_set', 
    'forbidden_final_ascii_chars_set', 
    'forbidden_final_chars_list', 
    'forbidden_final_ascii_chars_list', 
    'forbidden_final_chars', 
    'forbidden_final_ascii_chars_bytes', 
    'forbidden_final_ascii_chars_bytearray', 

    'forbidden_final_chars_set_bytes', 
    'forbidden_final_chars_list_bytearray', 

    'ascii_dev_punctuation_characters', 
    'ascii_dev_punctuation_characters_set', 

    'dev_forbidden_initial_chars_set', 
    'dev_forbidden_initial_ascii_chars_set', 
    'dev_forbidden_initial_chars_list', 
    'dev_forbidden_initial_ascii_chars_list', 
    'dev_forbidden_initial_chars', 
    'dev_forbidden_initial_ascii_chars_bytes', 
    'dev_forbidden_initial_ascii_chars_bytearray', 

    'dev_forbidden_initial_chars_set_bytes', 
    'dev_forbidden_initial_chars_list_bytearray', 

    'dev_forbidden_final_chars_set', 
    'dev_forbidden_final_ascii_chars_set', 
    'dev_forbidden_final_chars_list', 
    'dev_forbidden_final_ascii_chars_list', 
    'dev_forbidden_final_chars', 
    'dev_forbidden_final_ascii_chars_bytes', 
    'dev_forbidden_final_ascii_chars_bytearray', 

    'dev_forbidden_final_chars_set_bytes', 
    'dev_forbidden_final_chars_list_bytearray', 
]


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


from cengal.system import PYTHON_VERSION_INT

import string
import keyword

from typing import Optional, Tuple, Union, Type, Callable, Set, List, Sequence


Text = Union[bytes, bytearray, str]
BinText = Union[bytes, bytearray]
DEFAULT_ENCODING = 'utf-8'


class EncodingRequired(Exception):
    pass


class NotSupportedDesiredTextType(Exception):
    pass


class NotSupportedDataType(Exception):
    pass


def _default_normalizer(text: Text, desired_type: Type, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Text:
    raise NotImplementedError


def normalize_text(text: Text, desired_type: Type, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Text:
    normalizer = normalizer or _default_normalizer
    
    need_to_use_normalizer = False
    if issubclass(desired_type, bytes):
        if isinstance(text, bytes):
            pass
        elif isinstance(text, bytearray):
            text = bytes(text)
        elif isinstance(text, str):
            if encoding:
                text = text.encode(encoding)
            else:
                raise EncodingRequired
        else:
            need_to_use_normalizer = True
    elif issubclass(desired_type, bytearray):
        if isinstance(text, bytearray):
            pass
        elif isinstance(text, bytes):
            text = bytearray(text)
        elif isinstance(text, str):
            if encoding:
                text = bytearray(text, encoding)
            else:
                raise EncodingRequired
        else:
            need_to_use_normalizer = True
    elif issubclass(desired_type, str):
        if isinstance(text, str):
            pass
        elif isinstance(text, bytes) or isinstance(text, bytearray):
            if encoding:
                text = text.decode(encoding)
            else:
                raise EncodingRequired
        else:
            need_to_use_normalizer = True
    else:
        need_to_use_normalizer = True
    
    if need_to_use_normalizer:
        text = normalizer(text, desired_type, encoding)

    return text


def normalize_text_to_data(data: Text, text: Text, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Text:
    data_type = type(data)
    if not isinstance(text, data_type):
        text = normalize_text(text, data_type, encoding, normalizer)
    
    return text


def find_text(data: Text, text: Text, start: Optional[int] = None, stop: Optional[int] = None, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    text = normalize_text_to_data(data, text, encoding, normalizer)
    start = data.find(text, start, stop)
    if -1 == start:
        return None
    
    return slice(start, start + len(text))


def rfind_text(data: Text, text: Text, start: Optional[int] = None, stop: Optional[int] = None, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    text = normalize_text_to_data(data, text, encoding, normalizer)
    start = data.rfind(text, start, stop)
    if -1 == start:
        return None
    
    return slice(start, start + len(text))














#==================================================================================================================
#=================================================   FIND WORD   ======================================
#==================================================================================================================











def find_word_impl(data: Text, word: Optional[Text] = None, 
                  start: Optional[int] = None, stop: Optional[int] = None, 
                  week_boundaries: bool = True,
                  forbidden_init_chars: Optional[Union[Text, Set[Text], List[Text]]] = None, 
                  forbidden_fin_chars: Optional[Union[Text, Set[Text], List[Text]]] = None, 
                  normalize_forbidden_init_chars: bool = False, normalize_forbidden_fin_chars: bool = False, 
                  encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    """_summary_

    Args:
        data (Text): _description_
        word (Optional[Text], optional): _description_. Defaults to None.
        start (Optional[int], optional): _description_. Defaults to None.
        stop (Optional[int], optional): _description_. Defaults to None.
        week_boundaries (bool, optional): When `True`: will check characters around the word for spaces even if that character is out of `start-stop` range. Defaults to True.
        forbidden_init_chars (Optional[Union[Text, Set[Text], List[Text]]], optional): _description_. Defaults to None.
        forbidden_fin_chars (Optional[Union[Text, Set[Text], List[Text]]], optional): _description_. Defaults to None.
        normalize_forbidden_init_chars (bool, optional): _description_. Defaults to False.
        normalize_forbidden_fin_chars (bool, optional): _description_. Defaults to False.
        encoding (Optional[str], optional): _description_. Defaults to DEFAULT_ENCODING.
        normalizer (Optional[Callable], optional): _description_. Defaults to None.

    Returns:
        Optional[slice]: _description_
    """    
    word = str() if word is None else word
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    
    if normalize_forbidden_init_chars:
        if isinstance(forbidden_init_chars, (set, list)):
            forbidden_init_chars = [normalize_text_to_data(data, char, encoding, normalizer) for char in forbidden_init_chars]
            if isinstance(data, (str, bytes)):
                forbidden_init_chars = set(forbidden_init_chars)
        else:
            forbidden_init_chars = normalize_text_to_data(data, forbidden_init_chars, encoding, normalizer)
    
    if normalize_forbidden_fin_chars:
        if isinstance(forbidden_fin_chars, (set, list)):
            forbidden_fin_chars = [normalize_text_to_data(data, char, encoding, normalizer) for char in forbidden_fin_chars]
            if isinstance(data, (str, bytes)):
                forbidden_fin_chars = set(forbidden_fin_chars)
        else:
            forbidden_fin_chars = normalize_text_to_data(data, forbidden_fin_chars, encoding, normalizer)

    text = normalize_text_to_data(data, word, encoding, normalizer)
    data_len: int = len(data)
    text_len: int = len(text)

    if 0 == text_len:
        while start < stop:
            if data[start] in forbidden_init_chars:
                start += 1
                continue
            
            break
        else:
            return None

        word_end = start
        while word_end < stop:
            if data[word_end] in forbidden_fin_chars:
                break
            
            word_end += 1
        
        return slice(start, word_end)
    else:
        global_start = start
        while True:
            if start + text_len > stop:
                return None
            
            start = data.find(text, start, stop)
            if -1 == start:
                return None
            
            if week_boundaries:
                if 0 != start:
                    if data[start - 1] not in forbidden_init_chars:
                        start += 1
                        continue
            else:
                if global_start < start:
                    if data[start - 1] not in forbidden_init_chars:
                        start += 1
                        continue
            
            if week_boundaries:
                if data_len != start + text_len:
                    if data[start + text_len] not in forbidden_fin_chars:
                        start += 1
                        continue
            else:
                if stop > start + text_len:
                    if data[start + text_len] not in forbidden_fin_chars:
                        start += 1
                        continue

            return slice(start, start + text_len)


def find_word(data: Text, word: Optional[Text] = None, 
              start: Optional[int] = None, stop: Optional[int] = None, 
              week_boundaries: bool = True,
              forbidden_init_chars: Optional[Union[Text, Set[Text], List[Text]]] = None, 
              forbidden_fin_chars: Optional[Union[Text, Set[Text], List[Text]]] = None, 
              normalize_forbidden_init_chars: bool = False, normalize_forbidden_fin_chars: bool = False, 
              encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    word = str() if word is None else word
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        forbidden_init_chars = forbidden_initial_chars_set if forbidden_init_chars is None else forbidden_init_chars
        forbidden_fin_chars = forbidden_final_chars_set if forbidden_fin_chars is None else forbidden_fin_chars
    elif isinstance(data, bytes):
        forbidden_init_chars = forbidden_initial_chars_set_bytes if forbidden_init_chars is None else forbidden_init_chars
        forbidden_fin_chars = forbidden_final_chars_set_bytes if forbidden_fin_chars is None else forbidden_fin_chars
    elif isinstance(data, bytearray):
        forbidden_init_chars = forbidden_initial_chars_list_bytearray if forbidden_init_chars is None else forbidden_init_chars
        forbidden_fin_chars = forbidden_final_chars_list_bytearray if forbidden_fin_chars is None else forbidden_fin_chars
    else:
        if forbidden_init_chars is None:
            normalize_forbidden_init_chars = True
        
        if forbidden_fin_chars is None:
            normalize_forbidden_fin_chars = True
        
        forbidden_init_chars = forbidden_initial_chars_set if forbidden_init_chars is None else forbidden_init_chars
        forbidden_fin_chars = forbidden_final_chars_set if forbidden_fin_chars is None else forbidden_fin_chars
    
    return find_word_impl(data, word, start, stop, week_boundaries, forbidden_init_chars, forbidden_fin_chars, normalize_forbidden_init_chars, normalize_forbidden_fin_chars, encoding, normalizer)


def find_dev_word(data: Text, word: Optional[Text] = None, 
                  start: Optional[int] = None, stop: Optional[int] = None, 
                  week_boundaries: bool = True,
                  forbidden_init_chars: Optional[Union[Text, Set[Text], List[Text]]] = None, 
                  forbidden_fin_chars: Optional[Union[Text, Set[Text], List[Text]]] = None, 
                  normalize_forbidden_init_chars: bool = False, normalize_forbidden_fin_chars: bool = False, 
                  encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    word = str() if word is None else word
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        forbidden_init_chars = dev_forbidden_initial_chars_set if forbidden_init_chars is None else forbidden_init_chars
        forbidden_fin_chars = dev_forbidden_final_chars_set if forbidden_fin_chars is None else forbidden_fin_chars
    elif isinstance(data, bytes):
        forbidden_init_chars = dev_forbidden_initial_chars_set_bytes if forbidden_init_chars is None else forbidden_init_chars
        forbidden_fin_chars = dev_forbidden_final_chars_set_bytes if forbidden_fin_chars is None else forbidden_fin_chars
    elif isinstance(data, bytearray):
        forbidden_init_chars = dev_forbidden_initial_chars_list_bytearray if forbidden_init_chars is None else forbidden_init_chars
        forbidden_fin_chars = dev_forbidden_final_chars_list_bytearray if forbidden_fin_chars is None else forbidden_fin_chars
    else:
        if forbidden_init_chars is None:
            normalize_forbidden_init_chars = True
        
        if forbidden_fin_chars is None:
            normalize_forbidden_fin_chars = True
        
        forbidden_init_chars = dev_forbidden_initial_chars_set if forbidden_init_chars is None else forbidden_init_chars
        forbidden_fin_chars = dev_forbidden_final_chars_set if forbidden_fin_chars is None else forbidden_fin_chars
    
    return find_word_impl(data, word, start, stop, week_boundaries, forbidden_init_chars, forbidden_fin_chars, normalize_forbidden_init_chars, normalize_forbidden_fin_chars, encoding, normalizer)














#==================================================================================================================
#=================================================   RFIND WORD   ======================================
#==================================================================================================================











def rfind_word_impl(data: Text, word: Optional[Text] = None, 
                  start: Optional[int] = None, stop: Optional[int] = None, 
                  week_boundaries: bool = True,
                  forbidden_init_chars: Optional[Union[Text, Set[Text], List[Text]]] = None, 
                  forbidden_fin_chars: Optional[Union[Text, Set[Text], List[Text]]] = None, 
                  normalize_forbidden_init_chars: bool = False, normalize_forbidden_fin_chars: bool = False, 
                  encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    word = str() if word is None else word
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    
    if normalize_forbidden_init_chars:
        if isinstance(forbidden_init_chars, (set, list)):
            forbidden_init_chars = [normalize_text_to_data(data, char, encoding, normalizer) for char in forbidden_init_chars]
            if isinstance(data, (str, bytes)):
                forbidden_init_chars = set(forbidden_init_chars)
        else:
            forbidden_init_chars = normalize_text_to_data(data, forbidden_init_chars, encoding, normalizer)
    
    if normalize_forbidden_fin_chars:
        if isinstance(forbidden_fin_chars, (set, list)):
            forbidden_fin_chars = [normalize_text_to_data(data, char, encoding, normalizer) for char in forbidden_fin_chars]
            if isinstance(data, (str, bytes)):
                forbidden_fin_chars = set(forbidden_fin_chars)
        else:
            forbidden_fin_chars = normalize_text_to_data(data, forbidden_fin_chars, encoding, normalizer)

    text = normalize_text_to_data(data, word, encoding, normalizer)
    data_len: int = len(data)
    text_len: int = len(text)

    if 0 == text_len:
        word_stop = stop - 1
        while start <= word_stop:
            if data[word_stop] in forbidden_init_chars:
                word_stop -= 1
                continue
            
            break
        else:
            return None

        word_start = word_stop
        word_stop += 1
        while start <= word_start:
            if data[word_start] in forbidden_fin_chars:
                break
            
            word_start -= 1
        
        return slice(word_start, word_stop)
    else:
        while True:
            global_start = start
            global_stop = stop

            if stop - text_len < global_start:
                return None
            
            start = data.rfind(text, global_start, stop)
            if -1 == start:
                return None
            
            stop = start + text_len
            if week_boundaries:
                if 0 != start:
                    if data[start - 1] not in forbidden_init_chars:
                        stop -= 1
                        continue
            else:
                if global_start < start:
                    if data[start - 1] not in forbidden_init_chars:
                        stop -= 1
                        continue
            
            if week_boundaries:
                if data_len != stop:
                    if data[stop] not in forbidden_fin_chars:
                        stop -= 1
                        continue
            else:
                if global_stop > stop:
                    if data[stop] not in forbidden_fin_chars:
                        stop -= 1
                        continue

            return slice(start, stop)


def rfind_word(data: Text, word: Optional[Text] = None, 
              start: Optional[int] = None, stop: Optional[int] = None, 
              week_boundaries: bool = True,
              forbidden_init_chars: Optional[Union[Text, Set[Text], List[Text]]] = None, 
              forbidden_fin_chars: Optional[Union[Text, Set[Text], List[Text]]] = None, 
              normalize_forbidden_init_chars: bool = False, normalize_forbidden_fin_chars: bool = False, 
              encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    word = str() if word is None else word
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        forbidden_init_chars = forbidden_initial_chars_set if forbidden_init_chars is None else forbidden_init_chars
        forbidden_fin_chars = forbidden_final_chars_set if forbidden_fin_chars is None else forbidden_fin_chars
    elif isinstance(data, bytes):
        forbidden_init_chars = forbidden_initial_chars_set_bytes if forbidden_init_chars is None else forbidden_init_chars
        forbidden_fin_chars = forbidden_final_chars_set_bytes if forbidden_fin_chars is None else forbidden_fin_chars
    elif isinstance(data, bytearray):
        forbidden_init_chars = forbidden_initial_chars_list_bytearray if forbidden_init_chars is None else forbidden_init_chars
        forbidden_fin_chars = forbidden_final_chars_list_bytearray if forbidden_fin_chars is None else forbidden_fin_chars
    else:
        if forbidden_init_chars is None:
            normalize_forbidden_init_chars = True
        
        if forbidden_fin_chars is None:
            normalize_forbidden_fin_chars = True
        
        forbidden_init_chars = forbidden_initial_chars_set if forbidden_init_chars is None else forbidden_init_chars
        forbidden_fin_chars = forbidden_final_chars_set if forbidden_fin_chars is None else forbidden_fin_chars
    
    return rfind_word_impl(data, word, start, stop, week_boundaries, forbidden_init_chars, forbidden_fin_chars, normalize_forbidden_init_chars, normalize_forbidden_fin_chars, encoding, normalizer)


def rfind_dev_word(data: Text, word: Optional[Text] = None, 
                  start: Optional[int] = None, stop: Optional[int] = None, 
                  week_boundaries: bool = True,
                  forbidden_init_chars: Optional[Union[Text, Set[Text], List[Text]]] = None, 
                  forbidden_fin_chars: Optional[Union[Text, Set[Text], List[Text]]] = None, 
                  normalize_forbidden_init_chars: bool = False, normalize_forbidden_fin_chars: bool = False, 
                  encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    word = str() if word is None else word
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        forbidden_init_chars = dev_forbidden_initial_chars_set if forbidden_init_chars is None else forbidden_init_chars
        forbidden_fin_chars = dev_forbidden_final_chars_set if forbidden_fin_chars is None else forbidden_fin_chars
    elif isinstance(data, bytes):
        forbidden_init_chars = dev_forbidden_initial_chars_set_bytes if forbidden_init_chars is None else forbidden_init_chars
        forbidden_fin_chars = dev_forbidden_final_chars_set_bytes if forbidden_fin_chars is None else forbidden_fin_chars
    elif isinstance(data, bytearray):
        forbidden_init_chars = dev_forbidden_initial_chars_list_bytearray if forbidden_init_chars is None else forbidden_init_chars
        forbidden_fin_chars = dev_forbidden_final_chars_list_bytearray if forbidden_fin_chars is None else forbidden_fin_chars
    else:
        if forbidden_init_chars is None:
            normalize_forbidden_init_chars = True
        
        if forbidden_fin_chars is None:
            normalize_forbidden_fin_chars = True
        
        forbidden_init_chars = dev_forbidden_initial_chars_set if forbidden_init_chars is None else forbidden_init_chars
        forbidden_fin_chars = dev_forbidden_final_chars_set if forbidden_fin_chars is None else forbidden_fin_chars
    
    return rfind_word_impl(data, word, start, stop, week_boundaries, forbidden_init_chars, forbidden_fin_chars, normalize_forbidden_init_chars, normalize_forbidden_fin_chars, encoding, normalizer)














#==================================================================================================================
#=================================================   FIND CHARACTERS   ======================================
#==================================================================================================================











def find_characters_impl(data: Text, 
                         required_chars: Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Union[Text, Set[Text], List[Text]], Optional[int]]]], 
                         max_chars: Optional[int] = None, 
                         start: Optional[int] = None, stop: Optional[int] = None, 
                         sort_required_chars: bool = True,
                         normalize_chars: bool = False, 
                         encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    
    new_required_chars: List[Union[Text, Set[Text], List[Text]]] = list()
    if normalize_chars:
        for char_set in required_chars:
            char_size: int = None
            if isinstance(char_set, tuple):
                char_size, char_set = char_set
            
            if isinstance(char_set, (set, list)):
                char_set = [normalize_text_to_data(data, char, encoding, normalizer) for char in char_set]
                if isinstance(data, (str, bytes)):
                    char_set = set(char_set)
            else:
                char_set = normalize_text_to_data(data, char_set, encoding, normalizer)

            new_required_chars.append((char_size, char_set))
            
        required_chars = new_required_chars

    new_required_chars = list()
    for char_set in required_chars:
        char_size: int = None
        if isinstance(char_set, tuple):
            char_size, char_set = char_set
        
        if not char_size:
            for char in char_set:
                char_size = len(char)
                break
        
        if char_size is not None:
            new_required_chars.append((char_size, char_set))
        
    required_chars = new_required_chars
    if sort_required_chars:
        required_chars = sorted(required_chars, key=lambda x: x[0], reverse=True)

    max_chars: int = 0 if max_chars is None else max_chars
    max_chars = 0 if max_chars < 0 else max_chars

    chars_found: int = 0
    start_pos:int = None
    stop_pos: int = None
    for i in range(start, stop):
        if max_chars and (chars_found >= max_chars):
            break
        
        char_found: bool = False
        for chars_set_tuple in required_chars:
            char_size, char_set = chars_set_tuple
            possible_stop_pos: int = i + char_size
            if data[i: possible_stop_pos] in char_set:
                if start_pos is None:
                    start_pos = i
                
                stop_pos = possible_stop_pos
                char_found = True
                break
        
        if char_found:
            chars_found += 1
            continue
        else:
            if start_pos is not None:
                break
    
    if stop_pos is not None:
        return slice(start_pos, stop_pos)
    else:
        return None


def find_any_spaces(data: Text, 
                    max_chars: Optional[int] = None, 
                    start: Optional[int] = None, stop: Optional[int] = None, 
                    required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                    sort_required_chars: bool = False,
                    normalize_chars: bool = False, 
                    encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = unicode_space_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = unicode_space_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = unicode_space_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = unicode_space_chars_sets_set_str if required_chars is None else required_chars
    
    return find_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def find_spaces_or_tabs(data: Text, 
                        max_chars: Optional[int] = None, 
                        start: Optional[int] = None, stop: Optional[int] = None, 
                        required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                        sort_required_chars: bool = False,
                        normalize_chars: bool = False, 
                        encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = space_or_tab_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = space_or_tab_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = space_or_tab_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = space_or_tab_chars_sets_set_str if required_chars is None else required_chars
    
    return find_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def find_spaces(data: Text, 
                max_chars: Optional[int] = None, 
                start: Optional[int] = None, stop: Optional[int] = None, 
                required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                sort_required_chars: bool = False,
                normalize_chars: bool = False, 
                encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = space_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = space_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = space_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = space_chars_sets_set_str if required_chars is None else required_chars
    
    return find_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def find_tabs(data: Text, 
              max_chars: Optional[int] = None, 
              start: Optional[int] = None, stop: Optional[int] = None, 
              required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
              sort_required_chars: bool = False,
              normalize_chars: bool = False, 
              encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = tab_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = tab_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = tab_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = tab_chars_sets_set_str if required_chars is None else required_chars
    
    return find_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def find_universal_line_delimiter(data: Text, 
                                  max_chars: Optional[int] = 1, 
                                  start: Optional[int] = None, stop: Optional[int] = None, 
                                  required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                                  sort_required_chars: bool = False,
                                  normalize_chars: bool = False, 
                                  encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = universal_line_delimiter_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = universal_line_delimiter_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = universal_line_delimiter_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = universal_line_delimiter_chars_sets_set_str if required_chars is None else required_chars
    
    return find_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def find_line_delimiter(data: Text, 
                        max_chars: Optional[int] = 1, 
                        start: Optional[int] = None, stop: Optional[int] = None, 
                        required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                        sort_required_chars: bool = False, 
                        normalize_chars: bool = False, 
                        encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = line_delimiter_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = line_delimiter_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = line_delimiter_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = line_delimiter_chars_sets_set_str if required_chars is None else required_chars
    
    return find_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)

















#==================================================================================================================
#=================================================   RFIND CHARACTERS   ======================================
#==================================================================================================================


















def rfind_characters_impl(data: Text, 
                         required_chars: Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Union[Text, Set[Text], List[Text]], Optional[int]]]], 
                         max_chars: Optional[int] = None, 
                         start: Optional[int] = None, stop: Optional[int] = None, 
                         sort_required_chars: bool = True,
                         normalize_chars: bool = False, 
                         encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    
    new_required_chars: List[Union[Text, Set[Text], List[Text]]] = list()
    if normalize_chars:
        for char_set in required_chars:
            char_size: int = None
            if isinstance(char_set, tuple):
                char_size, char_set = char_set
            
            if isinstance(char_set, (set, list)):
                char_set = [normalize_text_to_data(data, char, encoding, normalizer) for char in char_set]
                if isinstance(data, (str, bytes)):
                    char_set = set(char_set)
            else:
                char_set = normalize_text_to_data(data, char_set, encoding, normalizer)

            new_required_chars.append((char_size, char_set))
            
        required_chars = new_required_chars

    new_required_chars = list()
    for char_set in required_chars:
        char_size: int = None
        if isinstance(char_set, tuple):
            char_size, char_set = char_set
        
        if not char_size:
            for char in char_set:
                char_size = len(char)
                break
        
        if char_size is not None:
            new_required_chars.append((char_size, char_set))
        
    required_chars = new_required_chars
    if sort_required_chars:
        required_chars = sorted(required_chars, key=lambda x: x[0], reverse=True)

    max_chars: int = 0 if max_chars is None else max_chars
    max_chars = 0 if max_chars < 0 else max_chars

    chars_found: int = 0
    start_pos:int = None
    stop_pos: int = None
    current_stop_pos: int = None
    for current_stop_pos in range(stop, start, -1):
        if max_chars and (chars_found >= max_chars):
            break
        
        char_found: bool = False
        for chars_set_tuple in required_chars:
            char_size, char_set = chars_set_tuple
            possible_start_pos: int = current_stop_pos - char_size
            if data[possible_start_pos: current_stop_pos] in char_set:
                start_pos = possible_start_pos
                
                if stop_pos is None:
                    stop_pos = current_stop_pos
                
                char_found = True
                break
        
        if char_found:
            chars_found += 1
            continue
        else:
            if stop_pos is not None:
                break
    
    if stop_pos is not None:
        return slice(start_pos, stop_pos)
    else:
        return None


def rfind_any_spaces(data: Text, 
                    max_chars: Optional[int] = None, 
                    start: Optional[int] = None, stop: Optional[int] = None, 
                    required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                    sort_required_chars: bool = False,
                    normalize_chars: bool = False, 
                    encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = unicode_space_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = unicode_space_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = unicode_space_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = unicode_space_chars_sets_set_str if required_chars is None else required_chars
    
    return rfind_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def rfind_spaces_or_tabs(data: Text, 
                        max_chars: Optional[int] = None, 
                        start: Optional[int] = None, stop: Optional[int] = None, 
                        required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                        sort_required_chars: bool = False,
                        normalize_chars: bool = False, 
                        encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = space_or_tab_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = space_or_tab_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = space_or_tab_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = space_or_tab_chars_sets_set_str if required_chars is None else required_chars
    
    return rfind_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def rfind_spaces(data: Text, 
                max_chars: Optional[int] = None, 
                start: Optional[int] = None, stop: Optional[int] = None, 
                required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                sort_required_chars: bool = False,
                normalize_chars: bool = False, 
                encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = space_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = space_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = space_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = space_chars_sets_set_str if required_chars is None else required_chars
    
    return rfind_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def rfind_tabs(data: Text, 
              max_chars: Optional[int] = None, 
              start: Optional[int] = None, stop: Optional[int] = None, 
              required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
              sort_required_chars: bool = False,
              normalize_chars: bool = False, 
              encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = tab_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = tab_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = tab_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = tab_chars_sets_set_str if required_chars is None else required_chars
    
    return rfind_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def rfind_universal_line_delimiter(data: Text, 
                                  max_chars: Optional[int] = 1, 
                                  start: Optional[int] = None, stop: Optional[int] = None, 
                                  required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                                  sort_required_chars: bool = False,
                                  normalize_chars: bool = False, 
                                  encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = universal_line_delimiter_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = universal_line_delimiter_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = universal_line_delimiter_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = universal_line_delimiter_chars_sets_set_str if required_chars is None else required_chars
    
    return rfind_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def rfind_line_delimiter(data: Text, 
                        max_chars: Optional[int] = 1, 
                        start: Optional[int] = None, stop: Optional[int] = None, 
                        required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                        sort_required_chars: bool = False, 
                        normalize_chars: bool = False, 
                        encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = line_delimiter_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = line_delimiter_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = line_delimiter_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = line_delimiter_chars_sets_set_str if required_chars is None else required_chars
    
    return rfind_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)














#==================================================================================================================
#=================================================   STARTSWITH CHARACTERS   ======================================
#==================================================================================================================











def startswith_characters_impl(data: Text, 
                         required_chars: Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Union[Text, Set[Text], List[Text]], Optional[int]]]], 
                         max_chars: Optional[int] = None, 
                         start: Optional[int] = None, stop: Optional[int] = None, 
                         sort_required_chars: bool = True,
                         normalize_chars: bool = False, 
                         encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    
    new_required_chars: List[Union[Text, Set[Text], List[Text]]] = list()
    if normalize_chars:
        for char_set in required_chars:
            char_size: int = None
            if isinstance(char_set, tuple):
                char_size, char_set = char_set
            
            if isinstance(char_set, (set, list)):
                char_set = [normalize_text_to_data(data, char, encoding, normalizer) for char in char_set]
                if isinstance(data, (str, bytes)):
                    char_set = set(char_set)
            else:
                char_set = normalize_text_to_data(data, char_set, encoding, normalizer)

            new_required_chars.append((char_size, char_set))
            
        required_chars = new_required_chars

    new_required_chars = list()
    for char_set in required_chars:
        char_size: int = None
        if isinstance(char_set, tuple):
            char_size, char_set = char_set
        
        if not char_size:
            for char in char_set:
                char_size = len(char)
                break
        
        if char_size is not None:
            new_required_chars.append((char_size, char_set))
        
    required_chars = new_required_chars
    if sort_required_chars:
        required_chars = sorted(required_chars, key=lambda x: x[0], reverse=True)

    max_chars: int = 0 if max_chars is None else max_chars
    max_chars = 0 if max_chars < 0 else max_chars

    chars_found: int = 0
    start_pos:int = None
    stop_pos: int = None
    for i in range(start, stop):
        if max_chars and (chars_found >= max_chars):
            break
        
        char_found: bool = False
        for chars_set_tuple in required_chars:
            char_size, char_set = chars_set_tuple
            possible_stop_pos: int = i + char_size
            if data[i: possible_stop_pos] in char_set:
                if start_pos is None:
                    start_pos = i
                
                stop_pos = possible_stop_pos
                char_found = True
                break
        
        if char_found:
            chars_found += 1
            continue
        else:
            break
    
    if stop_pos is not None:
        return slice(start_pos, stop_pos)
    else:
        return None


def startswith_any_spaces(data: Text, 
                    max_chars: Optional[int] = None, 
                    start: Optional[int] = None, stop: Optional[int] = None, 
                    required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                    sort_required_chars: bool = False,
                    normalize_chars: bool = False, 
                    encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = unicode_space_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = unicode_space_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = unicode_space_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = unicode_space_chars_sets_set_str if required_chars is None else required_chars
    
    return startswith_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def startswith_spaces_or_tabs(data: Text, 
                        max_chars: Optional[int] = None, 
                        start: Optional[int] = None, stop: Optional[int] = None, 
                        required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                        sort_required_chars: bool = False,
                        normalize_chars: bool = False, 
                        encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = space_or_tab_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = space_or_tab_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = space_or_tab_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = space_or_tab_chars_sets_set_str if required_chars is None else required_chars
    
    return startswith_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def startswith_spaces(data: Text, 
                max_chars: Optional[int] = None, 
                start: Optional[int] = None, stop: Optional[int] = None, 
                required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                sort_required_chars: bool = False,
                normalize_chars: bool = False, 
                encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = space_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = space_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = space_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = space_chars_sets_set_str if required_chars is None else required_chars
    
    return startswith_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def startswith_tabs(data: Text, 
              max_chars: Optional[int] = None, 
              start: Optional[int] = None, stop: Optional[int] = None, 
              required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
              sort_required_chars: bool = False,
              normalize_chars: bool = False, 
              encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = tab_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = tab_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = tab_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = tab_chars_sets_set_str if required_chars is None else required_chars
    
    return startswith_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def startswith_universal_line_delimiter(data: Text, 
                                  max_chars: Optional[int] = 1, 
                                  start: Optional[int] = None, stop: Optional[int] = None, 
                                  required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                                  sort_required_chars: bool = False,
                                  normalize_chars: bool = False, 
                                  encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = universal_line_delimiter_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = universal_line_delimiter_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = universal_line_delimiter_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = universal_line_delimiter_chars_sets_set_str if required_chars is None else required_chars
    
    return startswith_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def startswith_line_delimiter(data: Text, 
                        max_chars: Optional[int] = 1, 
                        start: Optional[int] = None, stop: Optional[int] = None, 
                        required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                        sort_required_chars: bool = False, 
                        normalize_chars: bool = False, 
                        encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = line_delimiter_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = line_delimiter_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = line_delimiter_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = line_delimiter_chars_sets_set_str if required_chars is None else required_chars
    
    return startswith_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)

















#==================================================================================================================
#=================================================   ENDSWITH CHARACTERS   ======================================
#==================================================================================================================
















def endswith_characters_impl(data: Text, 
                         required_chars: Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Union[Text, Set[Text], List[Text]], Optional[int]]]], 
                         max_chars: Optional[int] = None, 
                         start: Optional[int] = None, stop: Optional[int] = None, 
                         sort_required_chars: bool = True,
                         normalize_chars: bool = False, 
                         encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    
    new_required_chars: List[Union[Text, Set[Text], List[Text]]] = list()
    if normalize_chars:
        for char_set in required_chars:
            char_size: int = None
            if isinstance(char_set, tuple):
                char_size, char_set = char_set
            
            if isinstance(char_set, (set, list)):
                char_set = [normalize_text_to_data(data, char, encoding, normalizer) for char in char_set]
                if isinstance(data, (str, bytes)):
                    char_set = set(char_set)
            else:
                char_set = normalize_text_to_data(data, char_set, encoding, normalizer)

            new_required_chars.append((char_size, char_set))
            
        required_chars = new_required_chars

    new_required_chars = list()
    for char_set in required_chars:
        char_size: int = None
        if isinstance(char_set, tuple):
            char_size, char_set = char_set
        
        if not char_size:
            for char in char_set:
                char_size = len(char)
                break
        
        if char_size is not None:
            new_required_chars.append((char_size, char_set))
        
    required_chars = new_required_chars
    if sort_required_chars:
        required_chars = sorted(required_chars, key=lambda x: x[0], reverse=True)

    max_chars: int = 0 if max_chars is None else max_chars
    max_chars = 0 if max_chars < 0 else max_chars

    chars_found: int = 0
    start_pos:int = None
    stop_pos: int = None
    current_stop_pos: int = None
    for current_stop_pos in range(stop, start, -1):
        if max_chars and (chars_found >= max_chars):
            break
        
        char_found: bool = False
        for chars_set_tuple in required_chars:
            char_size, char_set = chars_set_tuple
            possible_start_pos: int = current_stop_pos - char_size
            if data[possible_start_pos: current_stop_pos] in char_set:
                start_pos = possible_start_pos
                
                if stop_pos is None:
                    stop_pos = current_stop_pos
                
                char_found = True
                break
        
        if char_found:
            chars_found += 1
            continue
        else:
            break
    
    if stop_pos is not None:
        return slice(start_pos, stop_pos)
    else:
        return None


def endswith_any_spaces(data: Text, 
                    max_chars: Optional[int] = None, 
                    start: Optional[int] = None, stop: Optional[int] = None, 
                    required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                    sort_required_chars: bool = False,
                    normalize_chars: bool = False, 
                    encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = unicode_space_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = unicode_space_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = unicode_space_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = unicode_space_chars_sets_set_str if required_chars is None else required_chars
    
    return endswith_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def endswith_spaces_or_tabs(data: Text, 
                        max_chars: Optional[int] = None, 
                        start: Optional[int] = None, stop: Optional[int] = None, 
                        required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                        sort_required_chars: bool = False,
                        normalize_chars: bool = False, 
                        encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = space_or_tab_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = space_or_tab_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = space_or_tab_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = space_or_tab_chars_sets_set_str if required_chars is None else required_chars
    
    return endswith_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def endswith_spaces(data: Text, 
                max_chars: Optional[int] = None, 
                start: Optional[int] = None, stop: Optional[int] = None, 
                required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                sort_required_chars: bool = False,
                normalize_chars: bool = False, 
                encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = space_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = space_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = space_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = space_chars_sets_set_str if required_chars is None else required_chars
    
    return endswith_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def endswith_tabs(data: Text, 
              max_chars: Optional[int] = None, 
              start: Optional[int] = None, stop: Optional[int] = None, 
              required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
              sort_required_chars: bool = False,
              normalize_chars: bool = False, 
              encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = tab_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = tab_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = tab_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = tab_chars_sets_set_str if required_chars is None else required_chars
    
    return endswith_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def endswith_universal_line_delimiter(data: Text, 
                                  max_chars: Optional[int] = 1, 
                                  start: Optional[int] = None, stop: Optional[int] = None, 
                                  required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                                  sort_required_chars: bool = False,
                                  normalize_chars: bool = False, 
                                  encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = universal_line_delimiter_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = universal_line_delimiter_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = universal_line_delimiter_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = universal_line_delimiter_chars_sets_set_str if required_chars is None else required_chars
    
    return endswith_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)


def endswith_line_delimiter(data: Text, 
                        max_chars: Optional[int] = 1, 
                        start: Optional[int] = None, stop: Optional[int] = None, 
                        required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
                        sort_required_chars: bool = False, 
                        normalize_chars: bool = False, 
                        encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    if isinstance(data, str):
        required_chars = line_delimiter_chars_sets_set_str if required_chars is None else required_chars
    elif isinstance(data, bytes):
        required_chars = line_delimiter_chars_sets_set_bytes if required_chars is None else required_chars
    elif isinstance(data, bytearray):
        required_chars = line_delimiter_chars_sets_list_bytearray if required_chars is None else required_chars
    else:
        if required_chars is None:
            normalize_chars = True
        
        required_chars = line_delimiter_chars_sets_set_str if required_chars is None else required_chars
    
    return endswith_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)














#==================================================================================================================
#==================================================================================================================
#==================================================================================================================















def iterlines_impl(data: Text, 
              start: Optional[int] = None, stop: Optional[int] = None, 
              max_chars: Optional[int] = 1, 
              required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
              sort_required_chars: bool = False, 
              normalize_chars: bool = False, 
              encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None):
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    
    while True:
        line_end: Optional[slice] = find_characters_impl(data, required_chars, max_chars, start, stop, sort_required_chars, normalize_chars, encoding, normalizer)
        if line_end is None:
            line = slice(start, stop)
            line_content = slice(start, stop)
            yield (line, line_content, line_end)
            break
        
        line = slice(start, line_end.stop)
        line_content = slice(start, line_end.start)
        yield (line, line_content, line_end)
        start = line_end.stop


def iterlines(data: Text, 
              start: Optional[int] = None, stop: Optional[int] = None, 
              max_chars: Optional[int] = 1, 
              required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
              sort_required_chars: bool = False, 
              normalize_chars: bool = False, 
              encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None):
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    
    while True:
        line_end: Optional[slice] = find_line_delimiter(data, max_chars, start, stop, required_chars, sort_required_chars, normalize_chars, encoding, normalizer)
        if line_end is None:
            line = slice(start, stop)
            line_content = slice(start, stop)
            yield (line, line_content, line_end)
            break
        
        line = slice(start, line_end.stop)
        line_content = slice(start, line_end.start)
        yield (line, line_content, line_end)
        start = line_end.stop


def iterlines_universal(data: Text, 
              start: Optional[int] = None, stop: Optional[int] = None, 
              max_chars: Optional[int] = 1, 
              required_chars: Optional[Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]]] = None, 
              sort_required_chars: bool = False, 
              normalize_chars: bool = False, 
              encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None):
    start: int = 0 if start is None else start
    stop: int = len(data) if stop is None else stop
    
    while True:
        line_end: Optional[slice] = find_universal_line_delimiter(data, max_chars, start, stop, required_chars, sort_required_chars, normalize_chars, encoding, normalizer)
        if line_end is None:
            line = slice(start, stop)
            line_content = slice(start, stop)
            yield (line, line_content, line_end)
            break
        
        line = slice(start, line_end.stop)
        line_content = slice(start, line_end.start)
        yield (line, line_content, line_end)
        start = line_end.stop


def replace_slice(data: Text, place: slice, text: Text, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Tuple[Text, slice]:
    text = normalize_text_to_data(data, text, encoding, normalizer)
    l_text = data[:place.start]
    r_text = data[place.stop:]
    result_text = l_text + text + r_text
    result_place = slice(place.start, place.start + len(text))
    return result_text, result_place


def replace_text(data: Text, old_text: Text, new_text: Text, count: int = -1, start: Optional[int] = None, stop: Optional[int] = None, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[Text]:
    old_text = normalize_text_to_data(data, old_text, encoding, normalizer)
    new_text = normalize_text_to_data(data, new_text, encoding, normalizer)
    if (start is None) and (stop is None):
        return data.replace(old_text, new_text, count)
    else:
        replaces_num: int = 0
        while replaces_num != count:
            place = find_text(data, old_text, start, stop, encoding, normalizer)
            if place is None:
                break
            
            data, result_place = replace_slice(data, place, new_text, encoding, normalizer)
            start = result_place.stop
            replaces_num += 1
        
        return data


def replace_word(data: Text, 
                 old_text: Text, new_text: Text, count: int = -1, 
                 start: Optional[int] = None, stop: Optional[int] = None, 
                 week_boundaries: bool = True,
                 forbidden_init_chars: Optional[Union[Text, Set[Text]]] = None, 
                 forbidden_fin_chars: Optional[Union[Text, Sequence[Text]]] = None, 
                 normalize_forbidden_chars: bool = False, 
                 encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[Text]:
    old_text = normalize_text_to_data(data, old_text, encoding, normalizer)
    new_text = normalize_text_to_data(data, new_text, encoding, normalizer)
    replaces_num: int = 0
    while replaces_num != count:
        place = find_word(data, old_text, start, stop, week_boundaries, forbidden_init_chars, forbidden_fin_chars, normalize_forbidden_chars, encoding, normalizer)
        if place is None:
            break
        
        data, result_place = replace_slice(data, place, new_text, encoding, normalizer)
        start = result_place.stop
        replaces_num += 1
    
    return data


def replace_dev_word(data: Text, 
                     old_text: Text, new_text: Text, count: int = -1, 
                     start: Optional[int] = None, stop: Optional[int] = None, 
                     week_boundaries: bool = True,
                     forbidden_init_chars: Optional[Union[Text, Set[Text]]] = None, 
                     forbidden_fin_chars: Optional[Union[Text, Sequence[Text]]] = None, 
                     normalize_forbidden_chars: bool = False, 
                     encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[Text]:
    old_text = normalize_text_to_data(data, old_text, encoding, normalizer)
    new_text = normalize_text_to_data(data, new_text, encoding, normalizer)
    replaces_num: int = 0
    while replaces_num != count:
        place = find_dev_word(data, old_text, start, stop, week_boundaries, forbidden_init_chars, forbidden_fin_chars, normalize_forbidden_chars, encoding, normalizer)
        if place is None:
            break
        
        data, result_place = replace_slice(data, place, new_text, encoding, normalizer)
        start = result_place.stop
        replaces_num += 1
    
    return data


def normalize_line_separators(text: Text, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Text:
    lines = text.splitlines()
    line_separator = '\n'
    return normalize_text(line_separator, type(text), encoding, normalizer).join(lines)


def normalize_line_separators_and_tabs(text: Text, tabsize=4, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Text:
    text = normalize_line_separators(text, encoding, normalizer)
    return text.expandtabs(tabsize)


def removeprefix(data: Text, prefix: Text, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Text:
    prefix = normalize_text_to_data(data, prefix, encoding, normalizer)
    if (3, 9) <= PYTHON_VERSION_INT:
        return data.removeprefix(prefix)
    else:
        if data.startswith(prefix):
            return data[len(prefix):]
        else:
            return data
        

def removesuffix(data: Text, suffix: Text, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Text:
    suffix = normalize_text_to_data(data, suffix, encoding, normalizer)
    if (3, 9) <= PYTHON_VERSION_INT:
        return data.removesuffix(suffix)
    else:
        if data.endswith(suffix):
            return data[:-len(suffix):]
        else:
            return data
        

def to_identifier(text: Text, need_to_remove_repetitive: bool = True, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Text:
    original_text = text
    text = normalize_text_to_data(str(), text, encoding, normalizer)
    valid_initial_chars = string.ascii_letters + '_'
    valid_chars = valid_initial_chars + string.digits
    text_chars: Set[str] = set(text)

    trans = str.maketrans({
        char: '_' for char in text_chars if char not in valid_chars
    })
    identifier = text.translate(trans)
    if need_to_remove_repetitive:
        identifier = remove_repetitive(identifier, '_')
    
    if not identifier or identifier[0] not in valid_initial_chars:
        identifier = '_' + identifier

    while keyword.iskeyword(identifier):
        identifier += '_'

    return normalize_text_to_data(original_text, text, encoding, normalizer)
        

def remove_repetitive(data: Text, sub_str: Text, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Text:
    normalized_data: str = normalize_text_to_data(str(), data, encoding, normalizer)
    normalized_sub_str: str = normalize_text_to_data(str(), sub_str, encoding, normalizer)
    normalized_data.strip(normalized_sub_str)
    split_normalized_data: List[str] = normalized_data.split(normalized_sub_str)
    result: str = normalized_sub_str.join((piece for piece in split_normalized_data if piece))
    return normalize_text_to_data(data, result, encoding, normalizer)


# General known characters
ascii_newline_characters: List[str] = ['\n', '\r', '\r\n', '\x0b', '\x0c', '\x1c', '\x1d', '\x1e', '\x85']  # See: https://docs.python.org/3/library/stdtypes.html#str.splitlines
ascii_newline_characters_set: Set[str] = set(ascii_newline_characters)

unicode_newline_characters: List[str] = ['\n', '\r', '\r\n', '\x0b', '\x0c', '\x1c', '\x1d', '\x1e', '\x85', '\u2028', '\u2029']  # See: https://docs.python.org/3/library/stdtypes.html#str.splitlines
unicode_newline_characters_set: Set[str] = set(unicode_newline_characters)

ascii_space_characters: List[str] = list(string.whitespace)  # ' ', '\t', '\n', '\r', '\x0b', '\x0c'
ascii_space_characters_set: Set[str] = set(ascii_space_characters)

ascii_special_characters: List[str] = [chr(i) for i in range(32) if chr(i) not in ascii_space_characters_set] + [chr(127)]
ascii_special_characters_set: Set[str] = set(ascii_special_characters)

ascii_punctuation_characters: List[str] = list(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
ascii_punctuation_characters_set: Set[str] = set(ascii_punctuation_characters)

ascii_digits: List[str] = list(string.digits)
ascii_digits_set: Set[str] = set(ascii_digits)

unicode_space_characters: List[str] = ['\u0020', '\u0009', '\u000A', '\u000B', '\u000C', '\u000D', '\x0c', '\x1c', '\x1d', '\x1e', '\u0085', '\u2028', '\u2029']  # ' ', '\t', '\n', '\r', '\x0b', '\x0c', '\x85', '\u2028', '\u2029'
unicode_space_characters_set: Set[str] = set(unicode_space_characters)
unicode_space_characters_set_bytes: Set[bytes] = set([normalize_text_to_data(bytes(), char) for char in unicode_space_characters_set])
unicode_space_characters_list_bytearray: List[bytearray] = list([normalize_text_to_data(bytearray(), char) for char in unicode_space_characters_set])  # bytearray is not hashable

unicode_space_chars_sets_set_str: List[Tuple[Optional[int], Set[str]]] = [
    (0, {'\u2028', '\u2029'}), 
    (0, {'\x85'}), 
    (1, {' ', '\t', '\n', '\r', '\x0b', '\x0c', '\x1c', '\x1d', '\x1e'}), 
]
unicode_space_chars_sets_set_bytes: List[Tuple[Optional[int], Set[bytes]]] = [
    (0, set([normalize_text_to_data(bytes(), char) for char in {'\u2028', '\u2029'}])), 
    (0, set([normalize_text_to_data(bytes(), char) for char in {'\x85'}])), 
    (1, set([normalize_text_to_data(bytes(), char) for char in {' ', '\t', '\n', '\r', '\x0b', '\x0c', '\x1c', '\x1d', '\x1e'}])), 
]
unicode_space_chars_sets_list_bytearray: List[Tuple[Optional[int], List[bytearray]]] = [
    (0, list([normalize_text_to_data(bytearray(), char) for char in {'\u2028', '\u2029'}])),  # bytearray is not hashable
    (0, list([normalize_text_to_data(bytearray(), char) for char in {'\x85'}])),  # bytearray is not hashable
    (1, list([normalize_text_to_data(bytearray(), char) for char in {' ', '\t', '\n', '\r', '\x0b', '\x0c', '\x1c', '\x1d', '\x1e'}])),  # bytearray is not hashable
]

space_or_tab_chars_sets_set_str: List[Tuple[Optional[int], Set[str]]] = [
    (1, {' ', '\t'}),
]
space_or_tab_chars_sets_set_bytes: List[Tuple[Optional[int], Set[bytes]]] = [
    (1, set([normalize_text_to_data(bytes(), char) for char in {' ', '\t'}])),
]
space_or_tab_chars_sets_list_bytearray: List[Tuple[Optional[int], List[bytearray]]] = [
    (1, list([normalize_text_to_data(bytearray(), char) for char in {' ', '\t'}])),  # bytearray is not hashable
]

space_chars_sets_set_str: List[Tuple[Optional[int], Set[str]]] = [
    (1, {' '}),
]
space_chars_sets_set_bytes: List[Tuple[Optional[int], Set[bytes]]] = [
    (1, set([normalize_text_to_data(bytes(), char) for char in {' '}])),
]
space_chars_sets_list_bytearray: List[Tuple[Optional[int], List[bytearray]]] = [
    (1, list([normalize_text_to_data(bytearray(), char) for char in {' '}])),  # bytearray is not hashable
]

tab_chars_sets_set_str: List[Tuple[Optional[int], Set[str]]] = [
    (1, {'\t'}),
]
tab_chars_sets_set_bytes: List[Tuple[Optional[int], Set[bytes]]] = [
    (1, set([normalize_text_to_data(bytes(), char) for char in {'\t'}])),
]
tab_chars_sets_list_bytearray: List[Tuple[Optional[int], List[bytearray]]] = [
    (1, list([normalize_text_to_data(bytearray(), char) for char in {'\t'}])),  # bytearray is not hashable
]

universal_line_delimiter_chars_sets_set_str: List[Tuple[Optional[int], Set[str]]] = [
    (2, {'\r\n'}), 
    (1, {'\n', '\r'}), 
]
universal_line_delimiter_chars_sets_set_bytes: List[Tuple[Optional[int], Set[bytes]]] = [
    (2, set([normalize_text_to_data(bytes(), char) for char in {'\r\n'}])), 
    (1, set([normalize_text_to_data(bytes(), char) for char in {'\n', '\r'}])), 
]
universal_line_delimiter_chars_sets_list_bytearray: List[Tuple[Optional[int], List[bytearray]]] = [
    (2, list([normalize_text_to_data(bytearray(), char) for char in {'\r\n'}])),  # bytearray is not hashable
    (1, list([normalize_text_to_data(bytearray(), char) for char in {'\n', '\r'}])),  # bytearray is not hashable
]

line_delimiter_chars_sets_set_str: List[Tuple[Optional[int], Set[str]]] = [
    (2, {'\r\n'}), 
    (0, {'\u2028', '\u2029'}), 
    (0, {'\x85'}), 
    (1, {'\n', '\r', '\x0b', '\x0c', '\x1c', '\x1d', '\x1e'}), 
]
line_delimiter_chars_sets_set_bytes: List[Tuple[Optional[int], Set[bytes]]] = [
    (0, set([normalize_text_to_data(bytes(), char) for char in {'\u2028', '\u2029'}])), 
    (2, set([normalize_text_to_data(bytes(), char) for char in {'\r\n'}])), 
    (0, set([normalize_text_to_data(bytes(), char) for char in {'\x85'}])), 
    (1, set([normalize_text_to_data(bytes(), char) for char in {'\n', '\r', '\x0b', '\x0c', '\x1c', '\x1d', '\x1e'}])), 
]
line_delimiter_chars_sets_list_bytearray: List[Tuple[Optional[int], List[bytearray]]] = [
    (0, list([normalize_text_to_data(bytearray(), char) for char in {'\u2028', '\u2029'}])),  # bytearray is not hashable
    (2, list([normalize_text_to_data(bytearray(), char) for char in {'\r\n'}])),  # bytearray is not hashable
    (0, list([normalize_text_to_data(bytearray(), char) for char in {'\x85'}])),  # bytearray is not hashable
    (1, list([normalize_text_to_data(bytearray(), char) for char in {'\n', '\r', '\x0b', '\x0c', '\x1c', '\x1d', '\x1e'}])),  # bytearray is not hashable
]

forbidden_initial_chars_set: Set[str] = unicode_space_characters_set | ascii_space_characters_set | ascii_special_characters_set | ascii_punctuation_characters_set
forbidden_initial_ascii_chars_set: Set[str] = ascii_space_characters_set | ascii_special_characters_set | ascii_punctuation_characters_set
forbidden_initial_chars_list: List[str] = list(sorted(forbidden_initial_chars_set))
forbidden_initial_ascii_chars_list: List[str] = list(sorted(forbidden_initial_ascii_chars_set))
forbidden_initial_chars: str = ''.join(forbidden_initial_chars_list)
forbidden_initial_ascii_chars_bytes: bytes = normalize_text_to_data(bytes(), ''.join(forbidden_initial_ascii_chars_list))
forbidden_initial_ascii_chars_bytearray: bytearray = normalize_text_to_data(bytearray(), forbidden_initial_ascii_chars_bytes)

forbidden_initial_chars_set_bytes: Set[bytes] = set([normalize_text_to_data(bytes(), char) for char in forbidden_initial_chars_set])
forbidden_initial_chars_list_bytearray: List[bytearray] = list([normalize_text_to_data(bytearray(), char) for char in forbidden_initial_chars_set])  # bytearray is not hashable

forbidden_final_chars_set: Set[str] = unicode_space_characters_set | ascii_space_characters_set | ascii_special_characters_set | ascii_punctuation_characters_set
forbidden_final_ascii_chars_set: Set[str] = ascii_space_characters_set | ascii_special_characters_set | ascii_punctuation_characters_set
forbidden_final_chars_list: List[str] = list(sorted(forbidden_final_chars_set))
forbidden_final_ascii_chars_list: List[str] = list(sorted(forbidden_final_ascii_chars_set))
forbidden_final_chars: str = ''.join(forbidden_final_chars_list)
forbidden_final_ascii_chars_bytes: bytes = normalize_text_to_data(bytes(), ''.join(forbidden_final_ascii_chars_list))
forbidden_final_ascii_chars_bytearray: bytearray = normalize_text_to_data(bytearray(), forbidden_final_ascii_chars_bytes)

forbidden_final_chars_set_bytes: Set[bytes] = set([normalize_text_to_data(bytes(), char) for char in forbidden_final_chars_set])
forbidden_final_chars_list_bytearray: List[bytearray] = list([normalize_text_to_data(bytearray(), char) for char in forbidden_final_chars_set])  # bytearray is not hashable

# Programming known characters
ascii_dev_punctuation_characters: List[str] = list(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
ascii_dev_punctuation_characters.remove('_')  #  !"#$%&'()*+,-./:;<=>?@[\]^`{|}~
ascii_dev_punctuation_characters_set: Set[str] = set(ascii_dev_punctuation_characters)

dev_forbidden_initial_chars_set: Set[str] = unicode_space_characters_set | ascii_space_characters_set | ascii_special_characters_set | ascii_dev_punctuation_characters_set | ascii_digits_set
dev_forbidden_initial_ascii_chars_set: Set[str] = ascii_space_characters_set | ascii_special_characters_set | ascii_punctuation_characters_set
dev_forbidden_initial_chars_list: List[str] = list(sorted(dev_forbidden_initial_chars_set))
dev_forbidden_initial_ascii_chars_list: List[str] = list(sorted(dev_forbidden_initial_ascii_chars_set))
dev_forbidden_initial_chars: str = ''.join(dev_forbidden_initial_chars_list)
dev_forbidden_initial_ascii_chars_bytes: bytes = normalize_text_to_data(bytes(), ''.join(dev_forbidden_initial_ascii_chars_list))
dev_forbidden_initial_ascii_chars_bytearray: bytearray = normalize_text_to_data(bytearray(), dev_forbidden_initial_ascii_chars_bytes)

dev_forbidden_initial_chars_set_bytes: Set[bytes] = set([normalize_text_to_data(bytes(), char) for char in dev_forbidden_initial_chars_set])
dev_forbidden_initial_chars_list_bytearray: List[bytearray] = list([normalize_text_to_data(bytearray(), char) for char in dev_forbidden_initial_chars_set])  # bytearray is not hashable

dev_forbidden_final_chars_set: Set[str] = unicode_space_characters_set | ascii_space_characters_set | ascii_special_characters_set | ascii_dev_punctuation_characters_set
dev_forbidden_final_ascii_chars_set: Set[str] = ascii_space_characters_set | ascii_special_characters_set | ascii_punctuation_characters_set
dev_forbidden_final_chars_list: List[str] = list(sorted(dev_forbidden_final_chars_set))
dev_forbidden_final_ascii_chars_list: List[str] = list(sorted(dev_forbidden_final_ascii_chars_set))
dev_forbidden_final_chars: str = ''.join(dev_forbidden_final_chars_list)
dev_forbidden_final_ascii_chars_bytes: bytes = normalize_text_to_data(bytes(), ''.join(dev_forbidden_final_ascii_chars_list))
dev_forbidden_final_ascii_chars_bytearray: bytearray = normalize_text_to_data(bytearray(), dev_forbidden_final_ascii_chars_bytes)

dev_forbidden_final_chars_set_bytes: Set[bytes] = set([normalize_text_to_data(bytes(), char) for char in dev_forbidden_final_chars_set])
dev_forbidden_final_chars_list_bytearray: List[bytearray] = list([normalize_text_to_data(bytearray(), char) for char in dev_forbidden_final_chars_set])  # bytearray is not hashable
