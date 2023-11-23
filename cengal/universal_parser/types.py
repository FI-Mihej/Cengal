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

from collections import deque, namedtuple
from enum import Enum
from copy import copy
from collections import deque
from typing import Dict, Hashable, List, Optional, Sequence, Set, Type, Union, Callable, Any, Tuple
from cengal.text_processing.text_processing import Text, BinText, normalize_line_separators
from cengal.text_processing.brackets_processing import Bracket, BracketPair
from cengal.base.exceptions import CengalError, WrongParameterValueError
from cengal.data_containers.simple_tree import *


# === Exceptions ===
class UniversalParserError(CengalError):
    pass


class StrictParentingError(UniversalParserError):
    pass


class StrictParentsConflictError(StrictParentingError):
    pass


class StrictChildrenConflictError(StrictParentingError):
    pass


class WrongOperatorValueError(UniversalParserError, WrongParameterValueError):
    pass


class WrongOperatorParentsValueError(WrongOperatorValueError):
    pass


class WrongOperatorChildrenValueError(WrongOperatorValueError):
    pass


# === Mixins ===
class GrammarLinkMixin:
    def __init__(self) -> None:
        self.grammar: Optional['Grammar'] = None


class GrammarEntityBase(GrammarLinkMixin):
    def __init__(self) -> None:
        super().__init__()


# === Pattern Matchers Base ===
class PatternMatcherBase(GrammarEntityBase):
    def __init__(self):
        super(PatternMatcherBase, self).__init__()


class StaticPatternMatcherBase(GrammarEntityBase):
    def __init__(self):
        super(StaticPatternMatcherBase, self).__init__()


class DynamicPatternMatcherBase(GrammarEntityBase):
    def __init__(self):
        super(DynamicPatternMatcherBase, self).__init__()

    def __call__(self, text: Text, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        """[summary]

        Args:
            text (Text): full text's memoryview
            place (slice): place of text peace in the whole text
            entity_path (List[Tuple[GrammarEntityBase, int]]): list of Tuple[GrammarEntityBase, index_of_sub_entity]

        Raises:
            NotImplementedError: [description]

        Returns:
            Optional[slice]: [description]
        """        
        raise NotImplementedError

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        raise NotImplementedError

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        raise NotImplementedError

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        raise NotImplementedError

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        raise NotImplementedError


class StaticTextPatternMatcherBase(StaticPatternMatcherBase, PatternMatcherBase):
    def __init__(self):
        super(StaticTextPatternMatcherBase, self).__init__()
    
    @property
    def text(self):
        raise NotImplementedError


class DynamicTextPatternMatcherBase(DynamicPatternMatcherBase, PatternMatcherBase):
    def __init__(self):
        super(DynamicTextPatternMatcherBase, self).__init__()

    def __call__(self, text: Text, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        raise NotImplementedError

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        raise NotImplementedError

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        raise NotImplementedError

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        raise NotImplementedError

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        raise NotImplementedError


class RegexpPatternMatcherBase(DynamicPatternMatcherBase, PatternMatcherBase):
    def __init__(self):
        super(RegexpPatternMatcherBase, self).__init__()

    def __call__(self, text: Text, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        raise NotImplementedError


class StaticGrammarPatternMatcherBase(StaticPatternMatcherBase, PatternMatcherBase):
    def __init__(self):
        super(StaticGrammarPatternMatcherBase, self).__init__()


class DynamicGrammarPatternMatcherBase(DynamicPatternMatcherBase, PatternMatcherBase):
    def __init__(self):
        super(DynamicGrammarPatternMatcherBase, self).__init__()

    def __call__(self, text: Text, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        raise NotImplementedError


class AnyTextPatternMatcherBase(StaticPatternMatcherBase, PatternMatcherBase):
    def __init__(self):
        super(AnyTextPatternMatcherBase, self).__init__()


class SpacePatternMatcherMixin:
    pass


class StaticSpacePatternMatcherBase(StaticTextPatternMatcherBase, SpacePatternMatcherMixin):
    def __init__(self):
        super(StaticSpacePatternMatcherBase, self).__init__()
    
    @property
    def space_symbols(self):
        raise NotImplementedError


class DynamicSpacePatternMatcherBase(DynamicTextPatternMatcherBase, SpacePatternMatcherMixin):
    def __init__(self):
        super(DynamicSpacePatternMatcherBase, self).__init__()

    def __call__(self, text: Text, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        raise NotImplementedError


FixedPattern = Union[StaticTextPatternMatcherBase, StaticGrammarPatternMatcherBase, AnyTextPatternMatcherBase]
DynamicPattern = Union[DynamicTextPatternMatcherBase, RegexpPatternMatcherBase, DynamicGrammarPatternMatcherBase]
Pattern = Union[FixedPattern, DynamicPattern, PatternMatcherBase]


# === Pattern Matchers ===
class AnyTextPatternMatcher(AnyTextPatternMatcherBase):
    def __init__(self):
        super(AnyTextPatternMatcher, self).__init__()


class StaticTextPatternMatcher(StaticTextPatternMatcherBase):
    def __init__(self, text: Text):
        super(StaticTextPatternMatcher, self).__init__()
        self.text = text
        self.text_len = len(text)


class DynamicTextPatternMatcher(DynamicTextPatternMatcherBase):
    def __init__(self, text: Text):
        super(DynamicTextPatternMatcher, self).__init__()
        self._text = text
        self._text_len = len(text)

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        start = place.start
        end = start + self._text_len
        if text[slice(start, end)] == self._text:
            return slice(start, end)
        else:
            return None

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        start = place.stop - self._text_len
        end = place.stop
        if text[slice(start, end)] == self._text:
            return slice(start, end)
        else:
            return None

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        start = text.find(self._text, place.start, place.stop)
        if -1 == start:
            return None
        else:
            return slice(start, start + self._text_len)

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        start = text.rfind(self._text, place.start, place.stop)
        if -1 == start:
            return None
        else:
            return slice(start, start + self._text_len)


class DataStartPattern(DynamicTextPatternMatcherBase):
    def __init__(self):
        super(DataStartPattern, self).__init__()

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if 0 == place.start:
            return slice(0, 0)
        else:
            return None

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if 0 == place.stop == text_len:
            return slice(0, 0)
        else:
            return None

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)


class DataEndPattern(DynamicTextPatternMatcherBase):
    def __init__(self):
        super(DataEndPattern, self).__init__()

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if place.start == text_len:
            return slice(text_len, text_len)
        else:
            return None

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if place.stop == text_len:
            return slice(text_len, text_len)
        else:
            return None

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.endswith(text, text_len, place, entity_path)

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.endswith(text, text_len, place, entity_path)


class LineStartPattern(DynamicTextPatternMatcherBase):
    def __init__(self):
        super(LineStartPattern, self).__init__()

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if (0 == place.start) or ('\n' == text[place.start - 1]):
            return slice(0, 0)
        else:
            return None

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if 0 == place.stop == text_len:
            return slice(0, 0)
        elif (place.start == place.stop) and ((0 == place.start) or ('\n' == text[place.start - 1])):
            return slice(place.start, place.start)
        elif (place.stop >= 1) and ('\n' == text[place.stop - 1]):
            return slice(place.stop, place.stop)
        else:
            return None

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.startswith(text, text_len, place, entity_path)
        if result is None:
            start = text.find('\n', place.start, place.stop)
            if -1 < start:
                start += 1
                return slice(start, start)
            else:
                return None
        else:
            return result

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.endswith(text, text_len, place, entity_path)
        if result is None:
            start = text.rfind('\n', place.start, place.stop)
            if -1 < start:
                start += 1
                return slice(start, start)
            else:
                return None
        else:
            return result


class LineEndPattern(DynamicTextPatternMatcherBase):
    def __init__(self):
        super(LineEndPattern, self).__init__()

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if 0 == text_len:
            return slice(0, 0)
        elif (place.start < place.stop) and ('\n' == text[place.start]):
            return slice(place.start, place.start + 1)
        else:
            return None

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if place.stop == text_len:
            return slice(text_len, text_len)
        elif (place.start < place.stop) and ('\n' == text[place.stop - 1]):
            return slice(place.stop - 1, place.stop)
        else:
            return None

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.startswith(text, text_len, place, entity_path)
        if result is None:
            start = text.find('\n', place.start, place.stop)
            if -1 < start:
                stop = start + 1
                return slice(start, stop)
            else:
                return None
        else:
            return result

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.endswith(text, text_len, place, entity_path)
        if result is None:
            start = text.rfind('\n', place.start, place.stop)
            if -1 < start:
                stop = start + 1
                return slice(start, stop)
            else:
                return None
        else:
            return result


class UniLineStartPattern(DynamicTextPatternMatcherBase):
    def __init__(self, line_separator: Text = '\n'):
        super(UniLineStartPattern, self).__init__()
        self.line_separator = line_separator
        self.line_separator_len = len(line_separator)

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if (0 == place.start) or ((place.start >= self.line_separator_len) and (self.line_separator == text[slice(place.start - self.line_separator_len, place.start)])):
            return slice(0, 0)
        else:
            return None

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if 0 == place.stop == text_len:
            return slice(0, 0)
        elif (place.start == place.stop) and ((0 == place.start) or ((place.start >= self.line_separator_len) and (self.line_separator == text[slice(place.start - self.line_separator_len, place.start)]))):
            return slice(place.start, place.start)
        elif ((place.stop - place.start) >= self.line_separator_len) and (self.line_separator == text[slice(place.stop - self.line_separator_len, place.stop)]):
            return slice(place.stop, place.stop)
        else:
            return None

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.startswith(text, text_len, place, entity_path)
        if result is None:
            start = text.find(self.line_separator, place.start, place.stop)
            if -1 < start:
                start += self.line_separator_len
                return slice(start, start)
            else:
                return None
        else:
            return result

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.endswith(text, text_len, place, entity_path)
        if result is None:
            start = text.rfind(self.line_separator, place.start, place.stop)
            if -1 < start:
                start += self.line_separator_len
                return slice(start, start)
            else:
                return None
        else:
            return result


class UniLineEndPattern(DynamicTextPatternMatcherBase):
    def __init__(self, line_separator: Text = '\n'):
        super(UniLineEndPattern, self).__init__()
        self.line_separator = line_separator
        self.line_separator_len = len(line_separator)

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if 0 == text_len:
            return slice(0, 0)
        elif ((place.stop - place.start) >= self.line_separator_len) and (self.line_separator == text[slice(place.start, place.start + self.line_separator_len)]):
            return slice(place.start, place.start + self.line_separator_len)
        else:
            return None

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if place.stop == text_len:
            return slice(text_len, text_len)
        elif ((place.stop - place.start) >= self.line_separator_len) and (self.line_separator == text[slice(place.stop - self.line_separator_len, place.stop)]):
            return slice(place.stop - self.line_separator_len, place.stop)
        else:
            return None

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.startswith(text, text_len, place, entity_path)
        if result is None:
            start = text.find(self.line_separator, place.start, place.stop)
            if -1 < start:
                stop = start + self.line_separator_len
                return slice(start, stop)
            else:
                return None
        else:
            return result

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.endswith(text, text_len, place, entity_path)
        if result is None:
            start = text.rfind(self.line_separator, place.start, place.stop)
            if -1 < start:
                stop = start + self.line_separator_len
                return slice(start, stop)
            else:
                return None
        else:
            return result


class LineStartOnlyPattern(DynamicTextPatternMatcherBase):
    def __init__(self):
        super(LineStartOnlyPattern, self).__init__()

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if (1 <= place.start) and ('\n' == text[place.start - 1]):
            return slice(0, 0)
        else:
            return None

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if (place.start == place.stop) and ((1 <= place.start) and ('\n' == text[place.start - 1])):
            return slice(place.start, place.start)
        elif (place.stop >= 1) and ('\n' == text[place.stop - 1]):
            return slice(place.stop, place.stop)
        else:
            return None

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.startswith(text, text_len, place, entity_path)
        if result is None:
            start = text.find('\n', place.start, place.stop)
            if -1 < start:
                start += 1
                return slice(start, start)
            else:
                return None
        else:
            return result

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.endswith(text, text_len, place, entity_path)
        if result is None:
            start = text.rfind('\n', place.start, place.stop)
            if -1 < start:
                start += 1
                return slice(start, start)
            else:
                return None
        else:
            return result


class LineEndOnlyPattern(DynamicTextPatternMatcherBase):
    def __init__(self):
        super(LineEndOnlyPattern, self).__init__()

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if (place.start < place.stop) and ('\n' == text[place.start]):
            return slice(place.start, place.start + 1)
        else:
            return None

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if (place.start < place.stop) and ('\n' == text[place.stop - 1]):
            return slice(place.stop - 1, place.stop)
        else:
            return None

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.startswith(text, text_len, place, entity_path)
        if result is None:
            start = text.find('\n', place.start, place.stop)
            if -1 < start:
                stop = start + 1
                return slice(start, stop)
            else:
                return None
        else:
            return result

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.endswith(text, text_len, place, entity_path)
        if result is None:
            start = text.rfind('\n', place.start, place.stop)
            if -1 < start:
                stop = start + 1
                return slice(start, stop)
            else:
                return None
        else:
            return result


class UniLineStartOnlyPattern(DynamicTextPatternMatcherBase):
    def __init__(self, line_separator: Text = '\n'):
        super(UniLineStartOnlyPattern, self).__init__()
        self.line_separator = line_separator
        self.line_separator_len = len(line_separator)

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if (place.start >= self.line_separator_len) and (self.line_separator == text[slice(place.start - self.line_separator_len, place.start)]):
            return slice(0, 0)
        else:
            return None

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if (place.start == place.stop) and ((place.start >= self.line_separator_len) and (self.line_separator == text[slice(place.start - self.line_separator_len, place.start)])):
            return slice(place.start, place.start)
        elif ((place.stop - place.start) >= self.line_separator_len) and (self.line_separator == text[slice(place.stop - self.line_separator_len, place.stop)]):
            return slice(place.stop, place.stop)
        else:
            return None

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.startswith(text, text_len, place, entity_path)
        if result is None:
            start = text.find(self.line_separator, place.start, place.stop)
            if -1 < start:
                start += self.line_separator_len
                return slice(start, start)
            else:
                return None
        else:
            return result

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.endswith(text, text_len, place, entity_path)
        if result is None:
            start = text.rfind(self.line_separator, place.start, place.stop)
            if -1 < start:
                start += self.line_separator_len
                return slice(start, start)
            else:
                return None
        else:
            return result


class UniLineEndOnlyPattern(DynamicTextPatternMatcherBase):
    def __init__(self, line_separator: Text = '\n'):
        super(UniLineEndOnlyPattern, self).__init__()
        self.line_separator = line_separator
        self.line_separator_len = len(line_separator)

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if ((place.stop - place.start) >= self.line_separator_len) and (self.line_separator == text[slice(place.start, place.start + self.line_separator_len)]):
            return slice(place.start, place.start + self.line_separator_len)
        else:
            return None

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if ((place.stop - place.start) >= self.line_separator_len) and (self.line_separator == text[slice(place.stop - self.line_separator_len, place.stop)]):
            return slice(place.stop - self.line_separator_len, place.stop)
        else:
            return None

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.startswith(text, text_len, place, entity_path)
        if result is None:
            start = text.find(self.line_separator, place.start, place.stop)
            if -1 < start:
                stop = start + self.line_separator_len
                return slice(start, stop)
            else:
                return None
        else:
            return result

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.endswith(text, text_len, place, entity_path)
        if result is None:
            start = text.rfind(self.line_separator, place.start, place.stop)
            if -1 < start:
                stop = start + self.line_separator_len
                return slice(start, stop)
            else:
                return None
        else:
            return result


class LineSeparatorPattern(DynamicTextPatternMatcherBase):
    def __init__(self):
        super(LineSeparatorPattern, self).__init__()

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if (place.start < place.stop) and ('\n' == text[place.start]):
            return slice(place.start, place.start + 1)
        else:
            return None

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if (place.start < place.stop) and ('\n' == text[place.stop - 1]):
            return slice(place.stop - 1, place.stop)
        else:
            return None

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.startswith(text, text_len, place, entity_path)
        if result is None:
            start = text.find('\n', place.start, place.stop)
            if -1 < start:
                stop = start + 1
                return slice(start, stop)
            else:
                return None
        else:
            return result

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.endswith(text, text_len, place, entity_path)
        if result is None:
            start = text.rfind('\n', place.start, place.stop)
            if -1 < start:
                stop = start + 1
                return slice(start, stop)
            else:
                return None
        else:
            return result


class UniWordPattern(DynamicTextPatternMatcherBase):
    def __init__(self, word: Text):
        super(UniWordPattern, self).__init__()
        self.word = word
        self.word_len = len(word)

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if ((place.stop - place.start) >= self.word_len) and (self.word == text[slice(place.start, place.start + self.word_len)]):
            return slice(place.start, place.start + self.word_len)
        else:
            return None

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if ((place.stop - place.start) >= self.word_len) and (self.word == text[slice(place.stop - self.word_len, place.stop)]):
            return slice(place.stop - self.word_len, place.stop)
        else:
            return None

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.startswith(text, text_len, place, entity_path)
        if result is None:
            start = text.find(self.word, place.start, place.stop)
            if -1 < start:
                stop = start + self.word_len
                return slice(start, stop)
            else:
                return None
        else:
            return result

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.endswith(text, text_len, place, entity_path)
        if result is None:
            start = text.rfind(self.word, place.start, place.stop)
            if -1 < start:
                stop = start + self.word_len
                return slice(start, stop)
            else:
                return None
        else:
            return result


class UniLineSeparatorPattern(UniWordPattern):
    def __init__(self, line_separator: Text = '\n'):
        super(UniLineSeparatorPattern, self).__init__(line_separator)


class StaticSpacePattern(StaticSpacePatternMatcherBase):
    def __init__(self, space_symbols: Union[Set[Text], Text]):
        super(StaticSpacePattern, self).__init__()
        
        if not isinstance(space_symbols, set):
            space_symbols = {space_symbols}
        
        self.space_symbols = space_symbols


class SingleSpacePattern(DynamicSpacePatternMatcherBase):
    def __init__(self):
        super(SingleSpacePattern, self).__init__()

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if (place.start < place.stop) and (' ' == text[place.start]):
            return slice(place.start, place.start + 1)
        else:
            return None

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        if (place.start < place.stop) and (' ' == text[place.stop - 1]):
            return slice(place.stop - 1, place.stop)
        else:
            return None

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.startswith(text, text_len, place, entity_path)
        if result is None:
            start = text.find(' ', place.start, place.stop)
            if -1 < start:
                stop = start + 1
                return slice(start, stop)
            else:
                return None
        else:
            return result

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        result = self.endswith(text, text_len, place, entity_path)
        if result is None:
            start = text.rfind(' ', place.start, place.stop)
            if -1 < start:
                stop = start + 1
                return slice(start, stop)
            else:
                return None
        else:
            return result


class UniSingleSpacePattern(UniWordPattern):
    def __init__(self, space_symbol: Text = ' '):
        super(UniSingleSpacePattern, self).__init__(space_symbol)


def find_nearest_symbol_position(text: Text, boundaries: slice, symbols: Set[Text]) -> int:
    start = -1
    for symbol in symbols:
        another_start = text.find(symbol, boundaries.start, boundaries.stop)
        if -1 == start:
            start = another_start
        elif another_start < start:
            start = another_start
    
    return start


def rfind_nearest_symbol_position(text: Text, boundaries: slice, symbols: Set[Text]) -> int:
    start = -1
    for symbol in symbols:
        another_start = text.find(symbol, boundaries.start, boundaries.stop)
        if -1 == start:
            start = another_start
        elif another_start > start:
            start = another_start
    
    return start


def trace_continuous_symbols_sequence(text: Text, boundaries: slice, symbols: Set[Text], initial_position: int, increment: int) -> Optional[slice]:
    symbols = list(symbols)
    symbols.sort(key=lambda text: len(text), reverse=True)
    
    if increment >= 0:
        index = initial_position
        while index < boundaries.stop:
            available_space = boundaries.stop - index
            current_found_symbol = None
            current_found_symbol_len = None
            for symbol in symbols:
                current_found_symbol_len = len(symbol)
                if current_found_symbol_len <= available_space:
                    if symbol == text[slice(index, index + current_found_symbol_len)]:
                        current_found_symbol = symbol
                        break
            
            if current_found_symbol is None:
                break
            else:
                index += current_found_symbol_len
        
        if initial_position == index:
            return None
        else:
            return slice(initial_position, index)
    else:
        index = initial_position
        while index >= boundaries.start:
            available_space = index - boundaries.start
            current_found_symbol = None
            current_found_symbol_len = None
            for symbol in symbols:
                current_found_symbol_len = len(symbol)
                if current_found_symbol_len <= available_space:
                    if symbol == text[slice(index - current_found_symbol_len, index)]:
                        current_found_symbol = symbol
                        break
            
            if current_found_symbol is None:
                break
            else:
                index -= current_found_symbol_len
        
        if initial_position == index:
            return None
        else:
            return slice(index, initial_position)


def trace_continuous_symbol_sequence(text: Text, boundaries: slice, single_char: Text, initial_position: int, increment: int) -> Optional[slice]:
    if increment >= 0:
        index = initial_position
        while index < boundaries.stop:
            available_space = boundaries.stop - index
            if 1 <= available_space:
                if single_char == text[slice(index, index + 1)]:
                    index += 1
                else:
                    break
        
        if initial_position == index:
            return None
        else:
            return slice(initial_position, index)
    else:
        index = initial_position
        while index >= boundaries.start:
            available_space = index - boundaries.start
            if 1 <= available_space:
                if single_char == text[slice(index - 1, index)]:
                    index -= 1
                else:
                    break
        
        if initial_position == index:
            return None
        else:
            return slice(index, initial_position)


class SpacesPattern(DynamicSpacePatternMatcherBase):
    def __init__(self, space_char: Text = ' '):
        super(SpacesPattern, self).__init__()
        self.space_char = space_char

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return trace_continuous_symbol_sequence(text, place, self.space_char, place.start, 1)

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return trace_continuous_symbol_sequence(text, place, self.space_char, place.stop, -1)

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        start = text.find(self.space_char, place.start, place.stop)
        if -1 == start:
            return None
        
        return trace_continuous_symbol_sequence(text, place, self.space_char, start, 1)

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        start = text.rfind(self.space_char, place.start, place.stop)
        if -1 == start:
            return None
        
        return trace_continuous_symbol_sequence(text, place, self.space_char, start, -1)


class UniSpacesPattern(DynamicSpacePatternMatcherBase):
    def __init__(self, space_symbols: Union[Set[Text], Text]):
        super(UniSpacesPattern, self).__init__()
        
        if not isinstance(space_symbols, set):
            space_symbols = {space_symbols}
        
        self.space_symbols = space_symbols

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return trace_continuous_symbols_sequence(text, place, self.space_symbols, place.start, 1)

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return trace_continuous_symbols_sequence(text, place, self.space_symbols, place.stop, -1)

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        start = find_nearest_symbol_position(text, place, self.space_symbols)
        if -1 == start:
            return None
        
        return trace_continuous_symbols_sequence(text, place, self.space_symbols, start, 1)

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        start = rfind_nearest_symbol_position(text, place, self.space_symbols)
        if -1 == start:
            return None
        
        return trace_continuous_symbols_sequence(text, place, self.space_symbols, start, -1)


class NumeralIntTextPattern(DynamicTextPatternMatcherBase):
    def __init__(self):
        super(NumeralIntTextPattern, self).__init__()
        self.numeral_chars = set('0123456789')

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return trace_continuous_symbols_sequence(text, place, self.numeral_chars, place.start, 1)

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return trace_continuous_symbols_sequence(text, place, self.numeral_chars, place.stop, -1)

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        start = find_nearest_symbol_position(text, place, self.numeral_chars)
        if -1 == start:
            return None
        
        return trace_continuous_symbols_sequence(text, place, self.numeral_chars, start, 1)

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        start = rfind_nearest_symbol_position(text, place, self.numeral_chars)
        if -1 == start:
            return None
        
        return trace_continuous_symbols_sequence(text, place, self.numeral_chars, start, -1)


class AbsentPattern(DynamicTextPatternMatcherBase):
    def __init__(self):
        super(AbsentPattern, self).__init__()

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return None

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return None

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return None

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return None


class AnyTextPattern(DynamicTextPatternMatcherBase):
    def __init__(self, left_bracket: DynamicTextPatternMatcherBase, escaped_left_bracket: DynamicTextPatternMatcherBase, right_bracket: DynamicTextPatternMatcherBase, escaped_right_bracket: DynamicTextPatternMatcherBase):
        super(AnyTextPattern, self).__init__()
        self.left_bracket: DynamicTextPatternMatcherBase = left_bracket
        self.escaped_left_bracket: DynamicTextPatternMatcherBase = escaped_left_bracket
        self.right_bracket: DynamicTextPatternMatcherBase = right_bracket
        self.escaped_right_bracket: DynamicTextPatternMatcherBase = escaped_right_bracket

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        return self.startswith(text, text_len, place, entity_path)

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        index = place.start
        stop = None
        while index < place.stop:
            sub_place: slice = slice(index, place.stop)
            escaped_stop = self.escaped_right_bracket.find(text, text_len, sub_place, entity_path)
            stop = self.right_bracket.find(text, text_len, sub_place, entity_path)
            if stop is None:
                break
            
            if escaped_stop is None:
                index = stop.stop
                break
            
            if escaped_stop.start <= stop.start:
                index = escaped_stop.stop
                continue
        
        if index == place.start:
            return None
        else:
            return slice(place.start, stop.start)

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        index = place.stop
        stop = None
        while index > place.start:
            sub_place: slice = slice(place.start, index)
            escaped_stop = self.escaped_left_bracket.rfind(text, text_len, sub_place, entity_path)
            stop = self.left_bracket.rfind(text, text_len, sub_place, entity_path)
            if stop is None:
                break
            
            if escaped_stop is None:
                index = stop.start
                break
            
            if escaped_stop.stop >= stop.stop:
                index = escaped_stop.start
                continue
        
        if index == place.stop:
            return None
        else:
            return slice(stop.stop, place.stop)

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        left_bracket_place = self.left_bracket.find(text, text_len, place, entity_path)
        if left_bracket_place is None:
            return None
        
        return self.startswith(text, text_len, slice(left_bracket_place.stop, place.stop), entity_path)

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        right_bracket_place = self.right_bracket.rfind(text, text_len, place, entity_path)
        if right_bracket_place is None:
            return None
        
        return self.endswith(text, text_len, slice(place.start, right_bracket_place.start), entity_path)


class UniAnyTextPattern(DynamicTextPatternMatcherBase):
    def __init__(self, left_brackets_with_escapes: Dict[DynamicTextPatternMatcherBase, DynamicTextPatternMatcherBase], right_brackets_with_escapes: Dict[DynamicTextPatternMatcherBase, DynamicTextPatternMatcherBase]):
        """[summary]

        Args:
            left_brackets_with_escapes (Dict[DynamicTextPatternMatcherBase, DynamicTextPatternMatcherBase]): key: left bracket; value: escaped left bracket
            right_brackets_with_escapes (Dict[DynamicTextPatternMatcherBase, DynamicTextPatternMatcherBase]): key: right bracket; value: escaped right bracket
        """        
        super(UniAnyTextPattern, self).__init__()
        self.left_brackets_with_escapes: Dict[DynamicTextPatternMatcherBase, DynamicTextPatternMatcherBase] = left_brackets_with_escapes
        self.right_brackets_with_escapes: Dict[DynamicTextPatternMatcherBase, DynamicTextPatternMatcherBase] = right_brackets_with_escapes

    def __call__(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        raise NotImplementedError

    def startswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        raise NotImplementedError

    def endswith(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        raise NotImplementedError

    def find(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        raise NotImplementedError

    def rfind(self, text: Text, text_len: int, place: slice, entity_path: List[Tuple[GrammarEntityBase, int]]) -> Optional[slice]:
        raise NotImplementedError


# === Nuclei ===
class NucleusBase(GrammarEntityBase):
    def __init__(self,
                 pattern: Type[PatternMatcherBase],
                 handler: Callable
                 ):
        super(NucleusBase, self).__init__()
        self.pattern = pattern
        self.handler = handler


class FixedNucleus(NucleusBase):
    def __init__(self,
                 pattern: Type[FixedPattern],
                 handler: Callable
                 ):
        super(FixedNucleus, self).__init__(
                pattern,
                handler)


class DynamicNucleus(NucleusBase):
    def __init__(self,
                 pattern: Type[DynamicPattern],
                 handler: Callable
                 ):
        super(DynamicNucleus, self).__init__(
                pattern,
                handler)


Nucleus = Union[FixedNucleus, DynamicNucleus]


# === Atoms ===
class AtomBase(GrammarEntityBase):
    def __init__(self,
                 nucleus: Type[NucleusBase],
                 left_space_required: bool,
                 right_space_required: bool,
                 allowed_to_be_prefix: bool,
                 allowed_to_be_the_middle: bool,
                 allowed_to_be_suffix: bool,
                 handler: Callable
                 ):
        super(AtomBase, self).__init__()
        self.nucleus = nucleus
        self.left_space_required = left_space_required
        self.right_space_required = right_space_required
        self.allowed_to_be_prefix = allowed_to_be_prefix  # allowed nucleus to be a prefix of another nucleus
        self.allowed_to_be_the_middle = allowed_to_be_the_middle  # allowed nucleus to be a middle of another nucleus
        self.allowed_to_be_suffix = allowed_to_be_suffix  # allowed nucleus to be a suffix of another nucleus
        self.handler = handler


class FixedAtom(AtomBase):
    def __init__(self,
                 nucleus: Type[FixedNucleus],
                 left_space_required: bool,
                 right_space_required: bool,
                 allowed_to_be_prefix: bool,
                 allowed_to_be_the_middle: bool,
                 allowed_to_be_suffix: bool,
                 handler: Callable
                 ):
        super(FixedAtom, self).__init__(
                nucleus,
                left_space_required,
                right_space_required,
                allowed_to_be_prefix,
                allowed_to_be_the_middle,
                allowed_to_be_suffix,
                handler)


class DynamicAtom(AtomBase):
    def __init__(self,
                 nucleus: Type[DynamicNucleus],
                 left_space_required: bool,
                 right_space_required: bool,
                 allowed_to_be_prefix: bool,
                 allowed_to_be_the_middle: bool,
                 allowed_to_be_suffix: bool,
                 handler: Callable
                 ):
        super(DynamicAtom, self).__init__(
                nucleus,
                left_space_required,
                right_space_required,
                allowed_to_be_prefix,
                allowed_to_be_the_middle,
                allowed_to_be_suffix,
                handler)


Atom = Union[FixedAtom, DynamicAtom]


# === Monomers ===
class Monomer(GrammarEntityBase):
    def __init__(self,
                 atom_sequence: List[Type[Atom]],
                 handler: Callable
                 ):
        super(Monomer, self).__init__()
        self.atom_sequence = atom_sequence
        self.handler = handler


# === Oligomers ===
class Oligomer(GrammarEntityBase):
    def __init__(self,
                 monomer: Union[Type[Monomer], Set[Type[Monomer]]],
                 repeating_range: Optional[slice],
                 handler: Callable
                 ) -> None:
        super(Oligomer, self).__init__()
        if isinstance(monomer, set):
            self.monomer = monomer
        else:
            self.monomer = {monomer}
        
        self.repeating_range = repeating_range
        self.handler = handler


# === Polymers ===
class Polymer(GrammarEntityBase):
    def __init__(self,
                 oligomer_sequence: List[Union[Type[Oligomer], Set[Type[Oligomer]]]],
                 handler: Callable
                 ):
        super(Polymer, self).__init__()
        self.oligomer_sequence = list()
        for oligomer in oligomer_sequence:
            if not isinstance(oligomer, set):
                oligomer = {oligomer}
            
            self.oligomer_sequence.append(oligomer)
        
        self.handler = handler


# === Operators ===
class Operator(GrammarEntityBase):
    def __init__(self,
                 polymer: Type[Polymer],
                 parents: Union[None, Set[Union[None, Type['Operator']]], Type['Operator']],
                 children: Union[None, Set[Type['Operator']], Type['Operator']],
                 handler: Callable,
                 strict_parents: bool = False,
                 strict_children: bool = False) -> None:
        super(Operator, self).__init__()
        self.polymer = polymer
        
        self.strict_parents = strict_parents
        self._parents = self._check_parents(parents)
        
        self.strict_children = strict_children
        self._children = self._check_children(children)
        
        self.handler = handler
        self._result_id: Optional[Hashable] = None
    
    def _check_parents(self, parents) -> Set[Union[None, Type['Operator']]]:
        if not isinstance(parents, set):
            if (parents is None) or (isinstance(parents, type) and issubclass(parents, Operator)):
                parents = {parents}
            else:
                raise WrongOperatorParentsValueError('Wrong "parents" parameter value. Must be one of the {None, Set[Operator], Operator}')
        
        return parents
    
    def _check_children(self, children) -> Set[Type['Operator']]:
        if not isinstance(children, set):
            if children is None:
                children = set()
            elif isinstance(children, type) and issubclass(children, Operator):
                children = {children}
            else:
                raise WrongOperatorChildrenValueError('Wrong "children" parameter value. Must be one of the {None, Set[Operator], Operator}')
        
        return children
        
    @property
    def parents(self):
        return self._parents
    
    def register_parents(self, parents: Union[None, Set[Union[None, Type['Operator']]], Type['Operator']], test_only: bool = False, force_registering: bool = False):
        parents = self._check_parents(parents)
        new_parents = parents - self.parents
        if (not force_registering) and self.strict_parents and new_parents:
            raise StrictParentsConflictError
        
        if not test_only:
            self._parents.update(new_parents)
        
    @property
    def children(self):
        return self._children
    
    def register_children(self, children: Union[None, Set[Type['Operator']], Type['Operator']], test_only: bool = False, force_registering: bool = False):
        children = self._check_children(children)
        new_children = children - self.children
        if (not force_registering) and self.strict_children and new_children:
            raise StrictChildrenConflictError
        
        if not test_only:
            self._children.update(new_children)
    
    @property
    def result_id(self) -> Optional[Hashable]:
        return self._result_id
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        raise NotImplementedError
    
    def result(self) -> Any:
        raise NotImplementedError


# === Operator Pattern Matchers ===
class OperatorPatternMatcher(StaticGrammarPatternMatcherBase):
    def __init__(self,
                 operator: Union[Type[Operator], Set[Type[Operator]]]):
        super(OperatorPatternMatcher, self).__init__()
        if isinstance(operator, set):
            self.operator = operator
        else:
            self.operator = {operator}


class AnyOperatorPatternMatcher(StaticGrammarPatternMatcherBase):
    def __init__(self,
                 except_operator: Union[Type[Operator], Set[Type[Operator]]],
                 obey_strict_parenting_rules: bool):
        super(AnyOperatorPatternMatcher, self).__init__()
        if isinstance(except_operator, set):
            self.except_operator = except_operator
        else:
            self.except_operator = {except_operator}
        
        self.obey_strict_parenting_rules = obey_strict_parenting_rules


# === Grammars ===
class Grammar:
    def __init__(self,
                 space_pattern: Type[SpacePatternMatcherMixin],
                 patterns_types: Set[Type[Pattern]],
                 nuclei_types: Set[Type[Nucleus]],
                 atoms_types: Set[Type[Atom]],
                 monomers_types: Set[Type[Monomer]],
                 oligomers_types: Set[Type[Oligomer]],
                 polymers_types: Set[Type[Polymer]],
                 operators_types: Set[Type[Operator]]
                 ):
        self.space_pattern_type = space_pattern
        self.patterns_types = patterns_types
        self.nuclei_types = nuclei_types
        self.atoms_types = atoms_types
        self.monomers_types = monomers_types
        self.oligomers_types = oligomers_types
        self.polymers_types = polymers_types
        self.operators_types = operators_types

        self.space_pattern = None
        self.patterns: Dict[Type, Pattern] = dict()
        self.nuclei: Dict[Type, Nucleus] = dict()
        self.atoms: Dict[Type, Atom] = dict()
        self.monomers: Dict[Type, Monomer] = dict()
        self.oligomers: Dict[Type, Oligomer] = dict()
        self.polymers: Dict[Type, Polymer] = dict()
        self.operators: Dict[Type, Operator] = dict()
        
        self.nuclei_by_patterns: Dict[Type, Set[Type]] = dict()
        self.patterns_by_nuclei: Dict[Type, Set[Type]] = dict()
        self.atoms_by_nuclei: Dict[Type, Set[Type]] = dict()
        self.nuclei_by_atoms: Dict[Type, Set[Type]] = dict()
        self.monomers_by_atoms: Dict[Type, Set[Type]] = dict()
        self.atoms_by_monomers: Dict[Type, Set[Type]] = dict()
        self.oligomers_by_monomers: Dict[Type, Set[Type]] = dict()
        self.monomers_by_oligomers: Dict[Type, Set[Type]] = dict()
        self.polymers_by_oligomers: Dict[Type, Set[Type]] = dict()
        self.oligomers_by_polymers: Dict[Type, Set[Type]] = dict()
        self.operators_by_polymers: Dict[Type, Set[Type]] = dict()
        self.polymers_by_operators: Dict[Type, Set[Type]] = dict()
        
        self.operator_children: Dict[Type, Set[Type]] = dict()
        self.operator_parents: Dict[Type, Set[Type]] = dict()
    
    def init(self):
        self.make_space_pattern()
        self.make_entity_dicts()
        self.make_types_by_type_dicts()
        self.travers_grammar()
        
        self.make_operators_trees()
    
    # --- Space pattern ---
    def make_space_pattern(self):
        self.space_pattern = self.space_pattern_type()
    
    # --- Entity Dicts ---
    def make_entity_dicts(self):
        self.make_entity_dict_from_types_sequence(self.patterns_types, self.patterns)
        self.make_entity_dict_from_types_sequence(self.nuclei_types, self.nuclei)
        self.make_entity_dict_from_types_sequence(self.atoms_types, self.atoms)
        self.make_entity_dict_from_types_sequence(self.monomers_types, self.monomers)
        self.make_entity_dict_from_types_sequence(self.oligomers_types, self.oligomers)
        self.make_entity_dict_from_types_sequence(self.polymers_types, self.polymers)
        self.make_entity_dict_from_types_sequence(self.operators_types, self.operators)
    
    def make_entity_dict_from_types_sequence(self, sequence: Sequence, destination: Dict):
        for entity_type in sequence:
            entity = entity_type()
            entity.grammar = self
            destination[entity_type] = entity
    
    # --- Type by Type Dicts ---
    def make_types_by_type_dicts(self):
        self.make_patterns_nuclei_pair_dicts()
        self.make_nuclei_atoms_pair_dicts()
        self.make_atoms_monomers_pair_dicts()
        self.make_monomers_oligomers_pair_dicts()
        self.make_oligomers_polymers_pair_dicts()
        self.make_polymers_operators_pair_dicts()
    
    def make_patterns_nuclei_pair_dicts(self):
        for nucleus in self.nuclei:
            pattern = nucleus.pattern
            self.nuclei_by_patterns.setdefault(pattern, set()).add(nucleus)
            self.patterns_by_nuclei.setdefault(nucleus, set()).add(pattern)
    
    def make_nuclei_atoms_pair_dicts(self):
        for atom in self.atoms:
            nucleus = atom.nucleus
            self.atoms_by_nuclei.setdefault(nucleus, set()).add(atom)
            self.nuclei_by_atoms.setdefault(atom, set()).add(nucleus)
    
    def make_atoms_monomers_pair_dicts(self):
        for monomer in self.monomers:
            for atom in monomer.atom_sequence:
                self.monomers_by_atoms.setdefault(atom, set()).add(monomer)
                self.atoms_by_monomers.setdefault(monomer, set()).add(atom)
    
    def make_monomers_oligomers_pair_dicts(self):
        for oligomer in self.oligomers:
            monomer_union = oligomer.monomer
            for monomer in monomer_union:
                self.oligomers_by_monomers.setdefault(monomer, set()).add(oligomer)
                self.monomers_by_oligomers.setdefault(oligomer, set()).add(monomer)
    
    def make_oligomers_polymers_pair_dicts(self):
        for polymer in self.polymers:
            oligomer_sequence = polymer.oligomer_sequence
            for oligomer_union in oligomer_sequence:
                for oligomer in oligomer_union:
                    self.polymers_by_oligomers.setdefault(oligomer, set()).add(polymer)
                    self.oligomers_by_polymers.setdefault(polymer, set()).add(oligomer)
    
    def make_polymers_operators_pair_dicts(self):
        for operator in self.operators:
            polymer = operator.polymer
            self.operators_by_polymers.setdefault(polymer, set()).add(operator)
            self.polymers_by_operators.setdefault(operator, set()).add(polymer)
    
    # --- Operators Trees ---
    def make_operators_trees(self):
        for operator in self.operators:
            for parent in operator.parents:
                self.operator_children.setdefault(parent, set()).add(operator)
                self.operator_parents.setdefault(operator, set()).add(parent)
            for child in operator.children:
                self.operator_children.setdefault(operator, set()).add(child)
                self.operator_parents.setdefault(child, set()).add(operator)
    
    # --- Static Grammar Patterns ---
    def travers_grammar(self):
        for operator_type, operator in self.operators.items():
            for parent_operator_type in operator.parents:
                if parent_operator_type is not None:
                    parent = self.operators[parent_operator_type]
                    try:
                        parent.register_children(operator_type)
                    except StrictParentsConflictError:
                        raise StrictParentingError(f'Operator {operator_type} has {parent_operator_type} in it\'s list of parents, however  {parent_operator_type} has strict list of children and {operator_type} is not in this strict children list.')
            
            for child_operator_type in operator.children:
                child = self.operators[child_operator_type]
                try:
                    child.register_parents(operator_type)
                except StrictChildrenConflictError:
                    raise StrictParentingError(f'Operator {operator_type} has {child_operator_type} in it\'s list of children, however  {child_operator_type} has strict list of parents and {operator_type} is not in this strict parents list.')
            
            polymer_type = operator.polymer
            polymer = self.polymers[polymer_type]
            oligomer_sequence = polymer.oligomer_sequence
            for oligomer_union in oligomer_sequence:
                for oligomer_type in oligomer_union:
                    oligomer = self.oligomers[oligomer_type]
                    monomer_union = oligomer.monomer
                    for monomer_type in monomer_union:
                        monomer = self.monomers[monomer_type]
                        atom_sequence = monomer.atom_sequence
                        for atom_type in atom_sequence:
                            atom = self.atoms[atom_type]
                            nucleus_type = atom.nucleus
                            nucleus = self.nuclei[nucleus_type]
                            pattern_type = nucleus.pattern
                            pattern = self.patterns[pattern_type]
                            if issubclass(pattern_type, StaticGrammarPatternMatcherBase):
                                if issubclass(pattern_type, OperatorPatternMatcher):
                                    children_operators = pattern.operator
                                    for child_operator_type in children_operators:
                                        child_operator = self.operators[child_operator_type]
                                        
                                        # We must force editing parents and children here since this is the part of the autogeneration mechanism:
                                        child_operator.register_parents(operator_type, force_registering=True)
                                        operator.register_children(child_operator_type, force_registering=True)
                                elif issubclass(pattern_type, AnyOperatorPatternMatcher):
                                    not_children_operators = pattern.except_operator
                                    children_operators = self.operators_types - not_children_operators
                                    for child_operator_type in children_operators:
                                        child_operator = self.operators[child_operator_type]
                                        ok_to_register = True
                                        if pattern.obey_strict_parenting_rules:
                                            try:
                                                child_operator.register_parents(operator_type, test_only=True)
                                                operator.register_children(child_operator_type, test_only=True)
                                            except StrictParentingError:
                                                ok_to_register = False
                                        
                                        if ok_to_register:
                                            # We must force editing parents and children here since this is the part of the autogeneration mechanism:
                                            child_operator.register_parents(operator_type, force_registering=True)
                                            operator.register_children(child_operator_type, force_registering=True)


class AutoGrammar(Grammar):
    def __init__(self,
                 space_pattern: Type[SpacePatternMatcherMixin],
                 operators_types: Set[Type[Operator]]):
        patterns_types: Set[Type[Pattern]] = set()
        nuclei_types: Set[Type[Nucleus]] = set()
        atoms_types: Set[Type[Atom]] = set()
        monomers_types: Set[Type[Monomer]] = set()
        oligomers_types: Set[Type[Oligomer]] = set()
        polymers_types: Set[Type[Polymer]] = set()
        
        additional_operator_types: Set[Type[Operator]] = set()
        while operators_types:
            for operator_type in operators_types:
                operator = operator_type()
                polymers_types.add(operator.polymer)
                additional_operator_types.update(operator.parents)
                additional_operator_types.update(operator.children)
                del operator
            
            for polymer_type in polymers_types:
                polymer = polymer_type()
                oligomer_sequence = polymer.oligomer_sequence
                for oligomer_union in oligomer_sequence:
                    oligomers_types.update(oligomer_union)
                    # for oligomer_type in oligomer_union:
                    #     oligomers_types.add(oligomer_type)
                del polymer
            
            for oligomer_type in oligomers_types:
                oligomer = oligomer_type()
                monomer_union = oligomer.monomer
                monomers_types.update(monomer_union)
                # for monomer_type in monomer_union:
                #     monomers_types.add(monomer_type)
                del oligomer
            
            for monomer_type in monomers_types:
                monomer = monomer_type()
                for atom_type in monomer.atom_sequence:
                    atoms_types.add(atom_type)
                del monomer
            
            for atom_type in atoms_types:
                atom = atom_type()
                nuclei_types.add(atom.nucleus)
                del atom
            
            for nucleus_type in nuclei_types:
                nucleus = nucleus_type()
                patterns_types.add(nucleus.pattern)
                del nucleus
            
            for pattern_type in patterns_types:
                if issubclass(pattern_type, StaticGrammarPatternMatcherBase):
                    if issubclass(pattern_type, OperatorPatternMatcher):
                        pattern = pattern_type()
                        additional_operator_types.update(pattern.operator)
                        del pattern
                    elif issubclass(pattern_type, AnyOperatorPatternMatcher):
                        pattern = pattern_type()
                        additional_operator_types.update(pattern.except_operator)                    
                        del pattern
            
            if None in additional_operator_types:
                additional_operator_types.remove(None)
            
            operators_types = additional_operator_types - operators_types
            additional_operator_types = set()
            
        super().__init__(space_pattern, patterns_types, nuclei_types, atoms_types, monomers_types, oligomers_types, polymers_types, operators_types)


# === Grammar Pattern Matchers
class GrammarPatternMatcher(StaticGrammarPatternMatcherBase):
    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        super().__init__()


class ParserContext:
    def __init__(self, tree: Optional[Tree], path: Optional[Sequence[Tuple[Tuple[GrammarEntityBase, int], Any]]]) -> None:
        self.tree = tree or Tree()
        self.path = path or deque()


class ParseResultFound(Exception):
    pass


# === Parsers ===
class Parser:
    def __init__(self,
                 data: Text,
                 grammar: Grammar) -> None:
        self.data: Text = data
        self.grammar: Grammar = grammar
        self.parsing_paths: Dict[Hashable, ParserContext] = dict()
        self.parsing_path_last_id = -1
        self.successful_paths: Dict[Hashable, ParserContext] = dict()
        self.try_alternative_paths: bool = False
    
    def add_parsing_path(self, context: ParserContext) -> Hashable:
        self.parsing_path_last_id += 1
        self.parsing_paths[self.parsing_path_last_id] = context
        return self.parsing_path_last_id
    
    # def __call__(self, *args: Any, **kwds: Any) -> Any:
    #     initial_tree = Tree()
    #     children_bunches = self.find_children(None, self.data, len(self.data), slice(-1, -1), ParserContext())
    #     try:
    #         for children_bunch in children_bunches:
    #             for child in children_bunch:
    #                 result = self.parse_path()
    #                 if result is not None:
    #                     self.successful_paths[]  # TODO: not implemented yet
    #                     if not self.try_alternative_paths:
    #                         raise ParseResultFound
    #     except ParseResultFound:
    #         pass
    
    def find_children(self, current_root_operator: Union[None, Type[Operator]]) -> Tuple[Set[Operator], Set[Operator]]:
        allowed_children: Set = self.grammar.operator_children.get(current_root_operator, set())
        possible_children: Set = self.grammar.operators_types - allowed_children
        return allowed_children, possible_children
    
    def enter_operator(self, text: Text, text_len: int, place: slice, context: ParserContext):
        pass
    
    def parse_path(self) -> Optional[Any]:
        pass
            


# class Sentence:
#     def __init__(self):
#         self.phrase: Monomer


# class Idiom:
#     def __init__(self):
#         self.phrase: Monomer
