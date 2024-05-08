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
__version__ = "4.4.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from collections.abc import MutableMapping
from cengal.introspection.inspect import pdi
from dataclasses import dataclass
from types import MappingProxyType


class CustomDict(MutableMapping):
    def __init__(self, init_message):
        print(f"CustomDict initialized with message: {init_message}")
        self.store = {}
        
    def __getitem__(self, key):
        print(f"Getting item: {key=}")
        # return self.store[key]
        value = self.store[key]
        if isinstance(value, int):
            return value + 10
        else:
            return value
    
    def __setitem__(self, key, value):
        print(f"Setting item: {key} to {value}")
        self.store[key] = value
    
    def __delitem__(self, key):
        del self.store[key]
    
    def __iter__(self):
        return iter(self.store)
    
    def __len__(self):
        return len(self.store)

# class CustomType(type):
#     @classmethod
#     def __prepare__(metacls, name, bases, **kwds):
#         return kwds['custom_dict']

#     def __new__(cls, name, bases, namespace, **kwds):
#         print("Creating class with CustomDict namespace")
#         # Ensure the namespace used is an instance of dict for compatibility
#         return super().__new__(cls, name, bases, dict(namespace))
    
#     def __init__(cls, name, bases, namespace, **kwds):
#         super().__init__(name, bases, dict(namespace))

class CustomType(type):
    def __new__(cls, name, bases, namespace):
        print("Creating class with CustomDict namespace")
        # Ensure the namespace used is an instance of dict for compatibility
        return super().__new__(cls, name, bases, dict(namespace))
    
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, dict(namespace))


@dataclass
class MyClassOrig():
    x = 5
    y = 'hello'

    def greeting(self):
        return f"{self.y}, x is {self.x}"
    
    def increase_x(self):
        self.x += 1


# # Correct way to dynamically create the class
# custom_dict = CustomDict('Hello, Dynamic MyClass!')
# namespace = CustomType.__prepare__('MyClass', (MyClassOrig,), custom_dict=custom_dict)
# namespace.update({
#     'x': 5,
#     'y': 'hello',
#     # 'greeting': lambda self: f"{self.y}, x is {self.x}"
# })
# pdi(namespace)
# MyClass = CustomType('MyClass', (MyClassOrig,), namespace, custom_dict=custom_dict)

namespace = CustomDict('Hello, Dynamic MyClass!')
namespace.update({
    'x': 5,
    'y': 'hello',
    # 'greeting': lambda self: f"{self.y}, x is {self.x}"
})
MyClass = CustomType('MyClass', (MyClassOrig,), namespace)

# Testing the created class
instance = MyClass()
print(instance.greeting())  # Output: "hello, x is 15"
print(instance.greeting())  # Output: "hello, x is 15"
instance.increase_x()
print(instance.greeting())  # Output: "hello, x is 15"
instance.x += 1
print(instance.greeting())  # Output: "hello, x is 15"
instance.x = 9
print(instance.greeting())  # Output: "hello, x is 15"
pdi(instance.__dict__)

print('=========================')
original_instance = MyClassOrig()
original_instance.__class__ = MyClass
print(original_instance.greeting())  # Output: "hello, x is 15"
print(original_instance.greeting())  # Output: "hello, x is 15"
original_instance.increase_x()
print(original_instance.greeting())  # Output: "hello, x is 15"
original_instance.x += 1
print(original_instance.greeting())  # Output: "hello, x is 15"
original_instance.x = 9
print(original_instance.greeting())  # Output: "hello, x is 15"
pdi(original_instance.__dict__)

print('=========================')
original_instance.x = 10
print(f'{original_instance.greeting()=}')  # Output: "hello, x is 15"
print(f'{instance.greeting()=}')  # Output: "hello, x is 15"

print('=========================')
instance.x = 20
print(f'{original_instance.greeting()=}')  # Output: "hello, x is 15"
print(f'{instance.greeting()=}')  # Output: "hello, x is 15"


mco = MyClassOrig()
cud = CustomDict('Hello, Dynamic MyClassOrig!')
for key, val in mco.__dict__.items():
    cud[key] = val

mco.__dict__ = MappingProxyType(cud)
