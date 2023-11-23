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


__all__ = ['Bracket', 'BracketPair', 'BracketsList', 'BracketAbsentType']


#!/usr/bin/env python
# coding=utf-8




from enum import Enum
from typing import Optional, Union, List
from cengal.text_processing.text_processing import Text







class BracketAbsentType(Enum):
    out_of_data_bounds = 0
    out_of_accessible_data_bounds = 1


class BracketType(Enum):
    absent = 0
    text = 1


_BRACKET_TYPE_ABSENT = 0
_BRACKET_TYPE_TEXT = 1


class WrongBracketId(Exception):
    pass


class Bracket:
    def __init__(self, bracket_id: Union[Text, BracketAbsentType]):
        self.bracket_id: Union[Text, BracketAbsentType] = bracket_id
        if isinstance(bracket_id, BracketAbsentType):
            self._type = _BRACKET_TYPE_ABSENT
        else:
            self._type = _BRACKET_TYPE_TEXT
    
    def text(self) -> bool:
        return _BRACKET_TYPE_TEXT == self._type
    
    def absent(self) -> bool:
        return _BRACKET_TYPE_ABSENT == self._type


BracketsList = List[Bracket]


class BracketPair:
    def __init__(self, left: BracketsList, right: BracketsList):
        self.left = left
        self.right = right
