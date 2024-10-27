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


__all__ = [
    'BracketAbsentType', 
    'BracketSpecialType', 
    'BracketType', 
    'WrongBracketId', 
    'Word', 
    'SetOfStrings', 
    'Regex', 
    'Re', 
    'CustomTextFinder',  
    'Bracket', 
    'BracketsList', 
    'BracketPair', 
]


from cengal.text_processing.text_processing import Text, DEFAULT_ENCODING, normalize_text_to_data

import re

from enum import IntEnum
from typing import Optional, Union, List, Set, Sequence, Tuple, Callable


class BracketAbsentType(IntEnum):
    data_bounds = 0
    accessible_data_bounds = 1
    data_bounds_start = 2
    data_bounds_end = 3
    accessible_data_bounds_start = 4
    accessible_data_bounds_end = 5


class BracketSpecialType(IntEnum):
    any_spaces = 0
    spaces_or_tabs = 1
    spaces = 2
    tabs = 3
    universal_line_delimiter = 4
    line_delimiter = 5


class BracketType(IntEnum):
    text = 0
    word = 1
    regex = 2
    absent = 3
    special = 4
    set_of_strings = 5
    custom_text_finder = 6


class WrongBracketId(Exception):
    pass


class Word:
    def __init__(self, text: Text, 
                 forbidden_initial_chars: Optional[Union[Text, Set[Text]]] = None, 
                 forbidden_final_chars: Optional[Union[Text, Sequence[Text]]] = None, 
                 normalize_forbidden_chars: bool = False, 
                 is_dev_word: bool = False, 
                 ):
        self.text: Text = text
        self.forbidden_initial_chars: Optional[Union[Text, Set[Text]]] = forbidden_initial_chars
        self.forbidden_final_chars: Optional[Union[Text, Sequence[Text]]] = forbidden_final_chars
        self.normalize_forbidden_chars: bool = normalize_forbidden_chars
        self.is_dev_word: bool = is_dev_word


class SetOfStrings:
    def __init__(self, sets_of_strings: Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]], 
                 max_chars: Optional[int] = None, 
                 sort_required_chars: bool = False,
                 normalize_chars: bool = False, 
                 encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
        self.sets_of_strings: Sequence[Union[Union[Text, Set[Text], List[Text]], Tuple[Optional[int], Union[Text, Set[Text], List[Text]]]]] = sets_of_strings
        self.max_chars: Optional[int] = max_chars
        self.sort_required_chars: bool = sort_required_chars
        self.normalize_chars: bool = normalize_chars
        self.encoding: Optional[str] = encoding
        self.normalizer: Optional[Callable] = normalizer


class Regex:
    def __init__(self, regex_template: Text, 
                 encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None):
        self.regex_template: str = normalize_text_to_data(str(), regex_template, encoding, normalizer)
        self.compiled_regex = re.compile(self.regex_template)


Re = Regex


CustomTextFinder = Callable[[Text, int, int, Optional[str], Optional[Callable]], Optional[slice]]


class Bracket:
    __slots__ = ('bracket_id', '_type')

    def __init__(self, bracket_id: Union[Text, Word, BracketAbsentType, BracketSpecialType, SetOfStrings, CustomTextFinder], 
                 ):
        self.bracket_id: Union[Text, BracketAbsentType] = bracket_id
        if isinstance(bracket_id, Word):
            self._type = BracketType.word
        elif isinstance(bracket_id, Regex):
            self._type = BracketType.regex
        elif isinstance(bracket_id, BracketAbsentType):
            self._type = BracketType.absent
        elif isinstance(bracket_id, BracketSpecialType):
            self._type = BracketType.special
        elif isinstance(bracket_id, SetOfStrings):
            self._type = BracketType.set_of_strings
        elif callable(bracket_id):
            self._type = BracketType.custom_text_finder
        else:
            self._type = BracketType.text
    
    def text(self) -> bool:
        return BracketType.text == self._type

    def word(self) -> bool:
        return BracketType.word == self._type

    def regex(self) -> bool:
        return BracketType.regex == self._type
    
    def absent(self) -> bool:
        return BracketType.absent == self._type
    
    def special(self) -> bool:
        return BracketType.special == self._type
    
    def set_of_strings(self) -> bool:
        return BracketType.set_of_strings == self._type
    
    def custom_text_finder(self) -> bool:
        return BracketType.custom_text_finder == self._type


BracketsList = List[Bracket]


class BracketPair:
    def __init__(self, left: BracketsList, right: Optional[BracketsList] = None):
        self.left: BracketsList = left
        self.right: BracketsList = right
