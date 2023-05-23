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

from typing import Any

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.2.2"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


class ValueExistence:
    __slots__ = ('existence', 'result')

    def __init__(self, existence: bool, result: Any):
        self.existence: bool = existence
        self.result = result

    def __bool__(self):
        return self.existence

    def __nonzero__(self):
        return self.__bool__()

    def __str__(self):
        return 'ValueExistence({}, {})'.format(self.existence, self.result)

    def __getstate__(self):
        return self.existence, self.result

    def __setstate__(self, state):
        self.existence, self.result = state


class ValueCache(ValueExistence):
    __slots__ = tuple()

    def __init__(self):
        super(ValueCache, self).__init__(False, None)

    def __call__(self, *args, **kwargs):
        self.existence = False

    def get(self):
        return self.result

    def set(self, new_result):
        self.existence = True
        self.result = new_result

    def __getstate__(self):
        return self.existence, self.result

    def __setstate__(self, state):
        self.existence, self.result = state


class ValueType:
    __slots__ = ('type_id', 'result')

    def __init__(self, type_id, result):
        self.type_id = type_id
        self.result = result

    def __eq__(self, other):
        # "__ne__() delegates to __eq__() and inverts the result"
        if isinstance(other, ValueType):
            return self.type_id == other.type_id
        else:
            return self.type_id == other

    def __getstate__(self):
        return self.type_id, self.result

    def __setstate__(self, state):
        self.type_id, self.result = state
