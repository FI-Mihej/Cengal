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


__all__ = ['out_of_data_bounds', 'out_of_accessible_data_bounds', 'line_delimiter_n', 'line_delimiter_rn', 'line_delimiter', 'first_line', 'first_visible_line', 'line', 'last_line', 'last_visible_line', 'round_l', 'round_r', 'round', 'square_l', 'square_r', 'square', 'triangle_l', 'triangle_r', 'triangle', 'brace_l', 'brace_r', 'brace', 'quote', 'quotes', 'apostrophe', 'apostrophes', 'backtick', 'backticks']


#!/usr/bin/env python
# coding=utf-8




from enum import Enum
from typing import Optional, Union
from .brackets import *






out_of_data_bounds: Bracket = Bracket(BracketAbsentType.out_of_data_bounds)
out_of_accessible_data_bounds: Bracket = Bracket(BracketAbsentType.out_of_accessible_data_bounds)
out_of_bounds: BracketsList = [out_of_accessible_data_bounds, out_of_data_bounds]

line_delimiter_n: Bracket = Bracket('\n')
line_delimiter_rn: Bracket = Bracket('\r\n')
line_delimiter: BracketsList = [line_delimiter_rn, line_delimiter_n]

line_brake: BracketsList = [line_delimiter_rn, line_delimiter_n, out_of_accessible_data_bounds, out_of_data_bounds]

first_line: BracketPair = BracketPair([out_of_data_bounds], line_delimiter)
first_visible_line: BracketPair = BracketPair([out_of_accessible_data_bounds], line_delimiter)
inner_line: BracketPair = BracketPair(line_delimiter, line_delimiter)
last_visible_line: BracketPair = BracketPair(line_delimiter, [out_of_accessible_data_bounds])
last_line: BracketPair = BracketPair(line_delimiter, [out_of_data_bounds])
line: BracketPair = BracketPair(line_brake, line_brake)

data_body: BracketPair = BracketPair([out_of_data_bounds], [out_of_data_bounds])
visible_body: BracketPair = BracketPair([out_of_accessible_data_bounds], [out_of_accessible_data_bounds])
body: BracketPair = BracketPair(out_of_bounds, out_of_bounds)

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
