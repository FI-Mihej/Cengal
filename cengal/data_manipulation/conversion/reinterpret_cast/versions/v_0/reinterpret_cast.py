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


__all__ = ['reinterpret_cast_attempt', 'reinterpret_cast', 'temporary_reinterpret_cast', 'TemporaryReinterpretCast']


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


from contextlib import contextmanager
from typing import Type, Any, Generator, TypeVar


T = TypeVar('T')


def reinterpret_cast_attempt(new_type: Type[T], value: Any) -> bool:
    result: bool = True
    try:
        value.__class__ = new_type
    except TypeError:
        result = False
    
    return result


def reinterpret_cast(new_type: Type[T], value: Any) -> T:
    value.__class__ = new_type
    return value


@contextmanager
def temporary_reinterpret_cast(temporary_type: Type[T], value: Any) -> Generator[T, None, None]:
    original_class = value.__class__
    value.__class__ = temporary_type
    try:
        yield value
    finally:
        value.__class__ = original_class


class TemporaryReinterpretCast:
    def __init__(self, temporary_type: Type[T], value: Any):
        self.temporary_type: Type[T] = temporary_type
        self.value: Any = value
        self.original_class = value.__class__
    
    def __enter__(self):
        value = self.value
        value.__class__ = self.temporary_type
        return value
    
    def __exit__(self, type, value, traceback):
        self.value.__class__ = self.original_class
