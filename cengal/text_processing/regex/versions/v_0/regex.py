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
    'regex_escape_mapping', 
    'regex_escape_translation_table', 
    'escape_regex', 
    'eregex', 
    'er', 
    'multiple_escape_regex', 
    'meregex', 
    'mer', 

    'ascii_space__chars', 
    'ascii_space', 
    'not_ascii_space', 

    'unicode_space__chars', 
    'unicode_space', 
    'not_unicode_space', 

    'space_or_tab__chars', 
    'space_or_tab', 
    'not_space_or_tab', 

    'universal_line_delimiter__chars', 
    'universal_line_delimiter__group', 
    'not_universal_line_delimiter_character', 

    'line_delimiter__chars', 
    'line_delimiter__group', 
    'not_line_delimiter_character', 

    'ascii_text_word_character', 
    'not_ascii_text_word_character', 

    'ascii_dev_word_character', 
    'not_ascii_dev_word_character', 

    'ascii_special__chars', 
    'ascii_special_character', 
    'not_ascii_special_character', 

    'ascii_punctuation_chars', 
    'ascii_punctuation_character', 
    'not_ascii_punctuation_character', 

    'ascii_dev_punctuation_chars', 
    'ascii_dev_punctuation_character', 
    'not_ascii_dev_punctuation_character', 

    'text_word_character', 
    'not_text_word_character', 

    'dev_word_character', 
    'not_dev_word_character', 
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


from string import whitespace, punctuation

from typing import Dict, Sequence, List


regex_escape_mapping: Dict = {
    '\\': '\\\\', 
    '.': '\\.', 
    '^': '\\^', 
    '$': '\\$', 
    '*': '\\*', 
    '+': '\\+', 
    '?': '\\?', 
    '-': '\\-', 
    '|': '\\|', 
    '[': '\\[', 
    ']': '\\]', 
    '{': '\\{', 
    '}': '\\}', 
    '(': '\\(', 
    ')': '\\)', 
}
regex_escape_translation_table: Dict = str.maketrans(regex_escape_mapping)


def escape_regex(text: str) -> str:
    return text.translate(regex_escape_translation_table)


eregex = escape_regex
er = escape_regex


def multiple_escape_regex(text_pieces: Sequence[str]) -> List[str]:
    return [text.translate(regex_escape_translation_table) for text in text_pieces]


meregex = multiple_escape_regex
mer = multiple_escape_regex


ascii_space__chars = '\\s\t\n\r\x0b\x0c'
ascii_space = f'[{ascii_space__chars}]'
not_ascii_space = f'[^{ascii_space__chars}]'


unicode_space__chars = '\\s\t\n\r\x0b\x0c\x1c\x1d\x1e\x85\u2028\u2029'
unicode_space = f'[{unicode_space__chars}]'
not_unicode_space = f'[^{unicode_space__chars}]'


space_or_tab__chars = '\\s\t'
space_or_tab = f'[{space_or_tab__chars}]'
not_space_or_tab = f'[^{space_or_tab__chars}]'


universal_line_delimiter__chars = '\r\n'
universal_line_delimiter__group = f'({universal_line_delimiter__chars}|[{universal_line_delimiter__chars}])'
not_universal_line_delimiter_character = f'[^{universal_line_delimiter__chars}]'


line_delimiter__chars = f'{universal_line_delimiter__chars}\x0b\x0c\x1c\x1d\x1e\x85\u2028\u2029'
line_delimiter__group = f'({universal_line_delimiter__chars}|[{line_delimiter__chars}])'
not_line_delimiter_character = f'[^{line_delimiter__chars}]'


ascii_text_word_character = '[a-zA-Z0-9]'
not_ascii_text_word_character = '[^a-zA-Z0-9]'


ascii_dev_word_character = '\w'
not_ascii_dev_word_character = '\W'


ascii_special__chars = ''.join(multiple_escape_regex([chr(i) for i in range(32) if chr(i) not in whitespace] + [chr(127)]))
ascii_special_character = f'[{ascii_special__chars}]'
not_ascii_special_character = f'[^{ascii_special__chars}]'


ascii_punctuation_chars = punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
ascii_punctuation_character = f'[{ascii_punctuation_chars}]'
not_ascii_punctuation_character = f'[^{ascii_punctuation_chars}]'


ascii_dev_punctuation_chars = list(punctuation)
ascii_dev_punctuation_chars.remove('_')
ascii_dev_punctuation_chars = ''.join(ascii_dev_punctuation_chars)  # !"#$%&'()*+,-./:;<=>?@[\]^`{|}~
ascii_dev_punctuation_character = f'[{ascii_dev_punctuation_chars}]'
not_ascii_dev_punctuation_character = f'[^{ascii_dev_punctuation_chars}]'


text_word_character = f'[^{unicode_space__chars}{ascii_special__chars}{ascii_punctuation_chars}]'
not_text_word_character = f'[{unicode_space__chars}{ascii_special__chars}{ascii_punctuation_chars}]'


dev_word_character = f'[^{unicode_space__chars}{ascii_special__chars}{ascii_dev_punctuation_chars}]'
not_dev_word_character = f'[{unicode_space__chars}{ascii_special__chars}{ascii_dev_punctuation_chars}]'
