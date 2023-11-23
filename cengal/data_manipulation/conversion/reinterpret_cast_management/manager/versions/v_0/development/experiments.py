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
__version__ = "4.1.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


class A:
    ...

class B(A):
    ...

class C(A):
    ...

class D(B, C):
    ...

d = D()
print(D.__mro__)

class Vehicle0:
    __slots__ = ('id_number', 'make', 'model')

class Vehicle:
    __slots__ = ('id_number', 'make', 'model')

    def method(self):
        ...

auto = Vehicle()
from cengal.introspection.inspect import entity_properties
print(f'{dir(auto) = }')
print(f'{entity_properties(type(auto)) = }')
print(f'{type(auto).__slots__ = }')
print(f'{entity_properties(auto) = }')
print(f'{auto.__slots__ = }')
# print(f'{auto.__dict__ = }')
# print(f'{vars(auto) = }')
print(f'{type(auto) = }')
print(f'{type(type(auto)) = }')
print(f'{entity_properties(type(type(auto))) = }')
print(f'{dir(type(type(auto))) = }')
