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


class ResultExistence:
    __slots__ = ('existence', 'result')

    def __init__(self, existence, result):
        self.existence = existence
        self.result = result

    def __bool__(self):
        return self.existence

    def __nonzero__(self):
        return self.__bool__()

    def __str__(self):
        return '{}: {}'.format(self.existence, self.result)

    def __getstate__(self):
        return self.existence, self.result

    def __setstate__(self, state):
        existence, value = state
        self.value = value
        self.existence = existence
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, ResultExistence):
            return (self.existence == __value.existence) and (self.value == __value.value)
        else:
            if self.existence:
                return self.value == __value
            else:
                return False
    
    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)


class ResultCache(ResultExistence):
    __slots__ = tuple()

    def __init__(self):
        super(ResultCache, self).__init__(False, None)

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
        existence, value = state
        self.value = value
        self.existence = existence
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, ResultExistence):
            return (self.existence == __value.existence) and (self.value == __value.value)
        else:
            if self.existence:
                return self.value == __value
            else:
                return False
    
    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)


class ResultType:
    __slots__ = ('type_id', 'result')

    def __init__(self, type_id, result):
        self.type_id = type_id
        self.result = result

    def __eq__(self, other):
        # "__ne__() delegates to __eq__() and inverts the result"
        # if type(other) == ResultType:
        if isinstance(other, ResultType):
            return self.type_id == other.type_id
        else:
            return self.type_id == other

    def __getstate__(self):
        return self.type_id, self.result

    def __setstate__(self, state):
        self.type_id, self.result = state
