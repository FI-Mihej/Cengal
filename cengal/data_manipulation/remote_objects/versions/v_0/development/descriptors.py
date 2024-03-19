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
__version__ = "4.2.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import inspect


class Ten:
    def __get__(self, obj, objtype=None):
        return 10


class A:
    x = 5                       # Regular class attribute
    y = Ten()                   # Descriptor instance


class B:
    __slots__ = ('x', 'y')

    def __init__(self) -> None:
        self.x = 5                       # Regular class attribute
        self.y = Ten()                   # Descriptor instance

# a = A()
# print(hasattr(a, '__dict__'))
# print(a.x)
# print(a.y)
# # print(a.__dict__)
# # print(A.__dict__)
# print(set(A.__dict__) - set(a.__dict__))
# # print(a.__slots__)
# # print(dir(a))
# print(getattr(a, 'x'))
# print(hasattr(getattr(a, 'y'), '__get__'))
# print(hasattr(inspect.getattr_static(a, 'y'), '__get__'))

# b = B()
# print(getattr(b, 'x'))
# print(hasattr(getattr(b, 'y'), '__get__'))
# print(hasattr(inspect.getattr_static(b, 'y'), '__get__'))
# print(hasattr(getattr(b, 'x'), '__get__'))
# print(hasattr(inspect.getattr_static(b, 'x'), '__get__'))
# print(b.y)
# # print(b.__dict__)
# print(b.__slots__)
# print(B.__dict__)

class _foo:
    __slots__ = ['foo', 'bar']

    def __init__(self):
        self.bar = 2


from cengal.introspection.inspect import (
    entity_module_importable_str_and_owning_names_path,
    entity_by_name_module_importable_str_and_owning_names_path,
    filled_slots_with_names_gen,
    filled_slots_names_gen,
    is_callable, is_async,
    is_setable_data_descriptor,
)

for name, slot_value in filled_slots_names_gen(_foo()):
    print(name, slot_value)


a = A()
print(hasattr(inspect.getattr_static(a, 'y'), '__get__'))
print(a.x, a.y)
a.x = 15
a.y = 15
print(hasattr(inspect.getattr_static(a, 'y'), '__get__'))
print(a.x, a.y)
