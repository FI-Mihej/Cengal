#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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

__all__ = ['ValueExistence', 'ValueHolder', 'ValueCache', 'ValueType']

from typing import Any, TypeVar, Generic

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.2.6"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


# TODO: implement Cython version (smart_values are used by our Cython code)


T = TypeVar('T')


class ValueExistence(Generic[T]):
    __slots__ = ('existence', '_value')

    def __init__(self, existence: bool = False, value: Any = None):
        self.existence: bool = existence
        self._value: T = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self.existence = True
        self._value = value

    def __bool__(self):
        return self.existence

    def __nonzero__(self):
        return self.__bool__()

    def __str__(self):
        return f'{type(self).__name__}({repr(self.existence)}, {repr(self.value)})'

    def __repr__(self):
        return self.__str__()

    def __getstate__(self):
        return self.existence, self.value

    def __setstate__(self, state):
        self.existence, self.value = state


ValueHolder = ValueExistence


class ValueCache(ValueExistence):
    __slots__ = tuple()

    def __init__(self):
        super(ValueCache, self).__init__(False, None)

    def __call__(self, *args, **kwargs):
        self.existence = False

    def get(self):
        return self.value

    def set(self, new_value):
        self.existence = True
        self.value = new_value

    def __getstate__(self):
        return self.existence, self.value

    def __setstate__(self, state):
        self.existence, self.value = state


class ValueType:
    __slots__ = ('type_id', 'value')

    def __init__(self, type_id, value):
        self.type_id = type_id
        self.value = value

    def __eq__(self, other):
        # "__ne__() delegates to __eq__() and inverts the value"
        if isinstance(other, ValueType):
            return self.type_id == other.type_id
        else:
            return self.type_id == other

    def __getstate__(self):
        return self.type_id, self.value

    def __setstate__(self, state):
        self.type_id, self.value = state

    def __str__(self):
        return f'{type(self).__name__}({repr(self.type_id)}, {repr(self.value)})'

    def __repr__(self):
        return self.__str__()
