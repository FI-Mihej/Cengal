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


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""


__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.1.18"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


# from cengal.math.numbers import RationalNumber
from typing import Callable, Hashable, List, Dict, Set, Any, Union, TypeVar, Generic, Tuple, TYPE_CHECKING, cast

from pyrsistent import b


T = TypeVar('T')
HT = TypeVar('HT', bound=Hashable)
class MultipleNamedFields(Dict[HT, Set[T]]):
    pass

class MultipleNamedFieldsSet(Set[Tuple[HT, Set[T]]]):
    pass

CommunicationMethod = MultipleNamedFields[int, bytes]

cm = CommunicationMethod()
cm['hello'] = set(('world', '!'))
val = cm['hello']
for key, val in cm.items():
    print(key, val)

cms = MultipleNamedFieldsSet[int, bytes]()
if TYPE_CHECKING:
    cmsv = cms.pop()

dcm: Dict[Hashable, Set[str]] = dict()
dcm['hello'] = set(('world', '!'))

class A:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b

class B:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    
    def add(self):
        return -(self.a + self.b)
    
    def mul(self):
        return self.a * self.b

class C(A):
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    
    def add(self):
        # return -(A.add(self))
        return -(super().add())
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b

class D(C):
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    
    def div(self):
        # return -(C.div(self))
        return -(super().div())
    
    def sub(self):
        return self.a - self.b


a = A(2, 3)
print('--- A ---:')
print(a.add())

a.__class__ = B
print('--- B ---:')
print(a.add())
print(a.mul())

a.__class__ = C
print('--- C ---:')
print(a.add())
print(a.mul())
print(a.div())

a.__class__ = D
print('--- D ---:')
print(a.add())
print(a.mul())
print(a.div())
print(a.sub())

aa = a
aa.__class__ = A
print('--- A ---:')
print(aa.add())
print('--- D ---:')
print(a.add())
try:
    print(a.mul())  # AttributeError: 'A' object has no attribute 'mul'
except AttributeError as ex:
    print(repr(ex))

from contextlib import contextmanager
from typing import Type, Any, Generator, TypeVar

TT = TypeVar('TT')
@contextmanager
def temporary_reinterpret_cast(temporary_type: Type[TT], value: Any) -> Generator[TT, None, None]:
    original_class = value.__class__
    value.__class__ = temporary_type
    try:
        yield value
    finally:
        value.__class__ = original_class

with temporary_reinterpret_cast(D, a) as a:
    print('--- temporary D ---:')
    print(a.add())
    print(a.mul())
    print(a.div())
    print(a.sub())


print('--- A ---:')
print(a.add())
print('--- D ---:')
print(a.add())
try:
    print(a.mul())  # AttributeError: 'A' object has no attribute 'mul'
except AttributeError as ex:
    print(repr(ex))

try:
    with temporary_reinterpret_cast(float, 1) as f:
        print('--- temporary float ---:')
        print(f)
except TypeError as ex:
    print(repr(ex))
