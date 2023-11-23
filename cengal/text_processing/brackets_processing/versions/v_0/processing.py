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
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


__all__ = ['find_brackets', 'find_text_in_brackets', 'find_text_with_brackets', 'replace_text_in_brackets', 'replace_text_with_brackets']


#!/usr/bin/env python
# coding=utf-8



from typing import Optional, Tuple, Callable, List
from cengal.text_processing.text_processing import Text, find_text, replace_slice, DEFAULT_ENCODING
from .brackets import *







def find_brackets(data: Text, brackets: BracketPair, start: int = 0, stop: Optional[int] = None, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Tuple[Optional[slice], Optional[slice]]:
    max_start = max(start, 0)
    max_start_slice = slice(max_start, max_start)
    end = len(data)
    stop = end if stop is None else stop
    min_end = min(end, stop)

    for l_bracket in brackets.left:
        if l_bracket.text():
            l_place = find_text(data, l_bracket.bracket_id, start, stop, encoding, normalizer)
        else:
            l_place = max_start_slice
        
        if l_place is not None:
            break
    
    for r_bracket in brackets.right:
        if r_bracket.text():
            r_place = find_text(data, r_bracket.bracket_id, (l_place or max_start_slice).stop, stop, encoding, normalizer)
        else:
            r_place = slice(min_end, min_end)
        
        if r_place is not None:
            break
    
    return l_place, r_place


def find_text_in_brackets(data: Text, brackets: BracketPair, start: int = 0, stop: Optional[int] = None, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    l_place, r_place = find_brackets(data, brackets, start, stop, encoding, normalizer)
    if (l_place is None) or (r_place is None):
        return None
    
    return slice(l_place.stop, r_place.start)


def find_text_with_brackets(data: Text, brackets: BracketPair, start: int = 0, stop: Optional[int] = None, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    l_place, r_place = find_brackets(data, brackets, start, stop, encoding, normalizer)
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
