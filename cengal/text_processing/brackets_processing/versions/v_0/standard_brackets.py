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
    'data_bounds', 
    'accessible_data_bounds', 
    'data_bounds_start', 
    'data_bounds_end', 
    'accessible_data_bounds_start', 
    'accessible_data_bounds_end', 
    'out_of_bounds', 
    'line_delimiter__n', 
    'line_delimiter__r', 
    'line_delimiter__rn', 
    'line_delimiter__line_tabulation', 
    'line_delimiter__form_feed', 
    'line_delimiter__file_separator', 
    'line_delimiter__group_separator', 
    'line_delimiter__record_separator', 
    'line_delimiter__next_line_c1_control_code', 
    'line_delimiter__line_separator', 
    'line_delimiter__paragraph_separator', 
    'line_delimiter_1_byte', 
    'line_delimiter_2_bytes', 
    'line_delimiter_1_to_2_bytes', 
    'line_delimiter_1_to_3_bytes', 
    'universal_line_delimiter_1_byte', 
    'universal_line_delimiter_2_bytes', 
    'universal_newlines', 
    'newlines', 
    'universal_newlines_bytes', 
    'newlines_bytes', 
    'universal_newlines_bytearray', 
    'newlines_bytearray', 
    'tabulation_bracket', 
    'space_bracket', 
    'space_or_tab_bracket', 
    'tabulations_bracket', 
    'spaces_bracket', 
    'spaces_or_tabs_bracket', 
    'single_space', 
    'single_any_space', 
    'single_any_ascii_space', 
    'spaces', 
    'all_spaces', 
    'all_ascii_spaces', 
    'line_break_l', 
    'line_break_l_accessible_bounds', 
    'line_break_l_bounds', 
    'line_break_r', 
    'line_break_r_accessible_bounds', 
    'line_break_r_bounds', 
    'first_accessible_line', 
    'first_line', 
    'inner_line', 
    'last_accessible_line', 
    'last_line', 
    'line', 
    'line_bytes', 
    'line_bytearray', 
    'word', 
    'word_ascii', 
    'word_in_line', 
    'whole_body', 
    'accessible_body', 
    'body', 
    'round_l', 
    'round_r', 
    'round', 
    'square_l', 
    'square_r', 
    'square', 
    'triangle_l', 
    'triangle_r', 
    'triangle', 
    'brace_l', 
    'brace_r', 
    'brace', 
    'quote', 
    'quotes', 
    'apostrophe', 
    'apostrophes', 
    'backtick', 
    'backticks', 
]


from cengal.text_processing.text_processing import normalize_text_to_data

from enum import Enum
from typing import Optional, Union
from .brackets import *


data_bounds: Bracket = Bracket(BracketAbsentType.data_bounds)
accessible_data_bounds: Bracket = Bracket(BracketAbsentType.accessible_data_bounds)
data_bounds_start: Bracket = Bracket(BracketAbsentType.data_bounds_start)
data_bounds_end: Bracket = Bracket(BracketAbsentType.data_bounds_end)
accessible_data_bounds_start: Bracket = Bracket(BracketAbsentType.accessible_data_bounds_start)
accessible_data_bounds_end: Bracket = Bracket(BracketAbsentType.accessible_data_bounds_end)
out_of_bounds: BracketsList = [data_bounds, accessible_data_bounds]

line_delimiter__n: Bracket = Bracket('\n')  # See: https://docs.python.org/3/library/stdtypes.html#str.splitlines
line_delimiter__r: Bracket = Bracket('\r')
line_delimiter__rn: Bracket = Bracket('\r\n')
line_delimiter__line_tabulation: Bracket = Bracket('\x0b')
line_delimiter__form_feed: Bracket = Bracket('\x0c')
line_delimiter__file_separator: Bracket = Bracket('\x1c')
line_delimiter__group_separator: Bracket = Bracket('\x1d')
line_delimiter__record_separator: Bracket = Bracket('\x1e')
line_delimiter__next_line_c1_control_code: Bracket = Bracket('\x85')
line_delimiter__line_separator: Bracket = Bracket('\u2028')
line_delimiter__paragraph_separator: Bracket = Bracket('\u2029')

line_delimiter_1_byte: Bracket = Bracket(SetOfStrings([(1, {'\n', '\r', '\x0b', '\x0c', '\x1c', '\x1d', '\x1e'})], 1))
line_delimiter_2_bytes: Bracket = Bracket(SetOfStrings([(2, {'\r\n'})], 1))
line_delimiter_1_to_2_bytes: Bracket = Bracket(SetOfStrings([(0, {'\x85'})], 1))
line_delimiter_1_to_3_bytes: Bracket = Bracket(SetOfStrings([(0, {'\u2028', '\u2029'})], 1))

universal_line_delimiter_1_byte: Bracket = Bracket(SetOfStrings([(1, {'\n', '\r'})], 1))
universal_line_delimiter_2_bytes: Bracket = Bracket(SetOfStrings([(2, {'\r\n'})], 1))

universal_newlines: BracketsList = [
    Bracket(SetOfStrings([
        (2, {'\r\n'}), 
        (1, {'\n', '\r'}), 
    ], 1)),
    ]
newlines: BracketsList = [
    Bracket(SetOfStrings([
        (2, {'\r\n'}), 
        (1, {'\u2028', '\u2029'}), 
        (1, {'\x85'}), 
        (1, {'\n', '\r', '\x0b', '\x0c', '\x1c', '\x1d', '\x1e'}), 
    ], 1)),
    ]

universal_newlines_bytes: BracketsList = [
    Bracket(SetOfStrings([
        (2, set([normalize_text_to_data(bytes(), char) for char in {'\r\n'}]) ), 
        (1, set([normalize_text_to_data(bytes(), char) for char in {'\n', '\r'}]) ), 
    ], 1)),
    ]
newlines_bytes: BracketsList = [
    Bracket(SetOfStrings([
        (3, set([normalize_text_to_data(bytes(), char) for char in {'\u2028', '\u2029'}]) ), 
        (2, set([normalize_text_to_data(bytes(), char) for char in {'\r\n'}]) ), 
        (2, set([normalize_text_to_data(bytes(), char) for char in {'\x85'}]) ), 
        (1, set([normalize_text_to_data(bytes(), char) for char in {'\n', '\r', '\x0b', '\x0c', '\x1c', '\x1d', '\x1e'}]) ), 
    ], 1)),
    ]

universal_newlines_bytearray: BracketsList = [
    Bracket(SetOfStrings([
        (2, list([normalize_text_to_data(bytearray(), char) for char in {'\r\n'}]) ), 
        (1, list([normalize_text_to_data(bytearray(), char) for char in {'\n', '\r'}]) ), 
    ], 1)),
    ]
newlines_bytearray: BracketsList = [
    Bracket(SetOfStrings([
        (3, list([normalize_text_to_data(bytearray(), char) for char in {'\u2028', '\u2029'}]) ), 
        (2, list([normalize_text_to_data(bytearray(), char) for char in {'\r\n'}]) ), 
        (2, list([normalize_text_to_data(bytearray(), char) for char in {'\x85'}]) ), 
        (1, list([normalize_text_to_data(bytearray(), char) for char in {'\n', '\r', '\x0b', '\x0c', '\x1c', '\x1d', '\x1e'}]) ), 
    ], 1)),
    ]

tabulation_bracket: Bracket = Bracket(SetOfStrings([(1, {'\t'})], 1))
space_bracket: Bracket = Bracket(SetOfStrings([(1, {' '})], 1))
space_or_tab_bracket: Bracket = Bracket(SetOfStrings([(1, {' ', '\t'})], 1))

tabulations_bracket: Bracket = Bracket(SetOfStrings([(1, {'\t'})], None))
spaces_bracket: Bracket = Bracket(SetOfStrings([(1, {' '})], None))
spaces_or_tabs_bracket: Bracket = Bracket(SetOfStrings([(1, {' ', '\t'})], None))

single_space: BracketsList = [space_bracket]
single_any_space: BracketsList = [space_bracket] + newlines
single_any_ascii_space: BracketsList = [space_bracket] + universal_newlines

spaces: BracketsList = [spaces_bracket]
all_spaces: BracketsList = [spaces_bracket] + newlines
all_ascii_spaces: BracketsList = [spaces_bracket] + universal_newlines

line_break_l: BracketsList = newlines
line_break_l_accessible_bounds: BracketsList = [accessible_data_bounds]
line_break_l_bounds: BracketsList = [data_bounds] + newlines

line_break_r: BracketsList = newlines
line_break_r_accessible_bounds: BracketsList = newlines + [accessible_data_bounds_end]
line_break_r_bounds: BracketsList = newlines + [data_bounds_end]

first_accessible_line: BracketPair = BracketPair(line_break_l_accessible_bounds, line_break_r_accessible_bounds)
first_line: BracketPair = BracketPair(line_break_l_bounds, line_break_r_bounds)
inner_line: BracketPair = BracketPair(line_break_l, line_break_r)
last_accessible_line: BracketPair = BracketPair(line_break_l_accessible_bounds, [accessible_data_bounds])  # will return slice only if current line is the last accessible one
last_line: BracketPair = BracketPair(line_break_l_accessible_bounds, [data_bounds])  # will return slice only if current line is the last one
line: BracketPair = first_accessible_line
line_bytes: BracketPair = BracketPair(line_break_l_accessible_bounds, newlines_bytes + [accessible_data_bounds_end])
line_bytearray: BracketPair = BracketPair(line_break_l_accessible_bounds, newlines_bytearray + [accessible_data_bounds_end])

word: BracketPair = BracketPair(all_spaces, all_spaces)
word_ascii: BracketPair = BracketPair(all_ascii_spaces, all_ascii_spaces)
word_in_line: BracketPair = BracketPair(spaces, spaces)

whole_body: BracketPair = BracketPair([data_bounds_start], [data_bounds_end])
accessible_body: BracketPair = BracketPair([accessible_data_bounds_start], [accessible_data_bounds_end])
body: BracketPair = accessible_body

round_l: Bracket = Bracket('(')
round_r: Bracket = Bracket(')')
round: BracketPair = BracketPair([round_l], [round_r])

square_l: Bracket = Bracket('[')
square_r: Bracket = Bracket(']')
square: BracketPair = BracketPair([square_l], [square_r])

triangle_l: Bracket = Bracket('<')
triangle_r: Bracket = Bracket('>')
triangle: BracketPair = BracketPair([triangle_l], [triangle_r])

brace_l: Bracket = Bracket('{')
brace_r: Bracket = Bracket('}')
brace: BracketPair = BracketPair([brace_l], [brace_r])

quote: Bracket = Bracket('"')
quotes: BracketPair = BracketPair([quote], [quote])

apostrophe: Bracket = Bracket("'")
apostrophes: BracketPair = BracketPair([apostrophe], [apostrophe])

backtick: Bracket = Bracket('`')
backticks: BracketPair = BracketPair([backtick], [backtick])
