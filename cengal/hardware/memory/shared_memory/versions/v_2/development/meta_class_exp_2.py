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
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from collections.abc import MutableMapping


class CustomDict(MutableMapping):
    def __init__(self, init_message):
        print(f"CustomDict initialized with message: {init_message}")
        self.store = {}
        
    def __getitem__(self, key):
        print(f"Getting item: {key}")
        # return self.store[key]
        value = self.store[key]
        if isinstance(value, int):
            return value + 10
        else:
            return value
    
    def __setitem__(self, key, value):
        self.store[key] = value
    
    def __delitem__(self, key):
        del self.store[key]
    
    def __iter__(self):
        return iter(self.store)
    
    def __len__(self):
        return len(self.store)

class CustomType(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        return CustomDict(kwds.get('init_message', 'No message provided'))

    def __new__(cls, name, bases, namespace, **kwds):
        print("Creating class with CustomDict namespace")
        # Ensure the namespace used is an instance of dict for compatibility
        return super().__new__(cls, name, bases, dict(namespace))
    
    def __init__(cls, name, bases, namespace, **kwds):
        super().__init__(name, bases, dict(namespace))

# Correct way to dynamically create the class
namespace = CustomType.__prepare__('MyClass', (object,), init_message='Hello, Dynamic MyClass!')
namespace.update({
    'x': 5,
    'y': 'hello',
    'greeting': lambda self: f"{self.y}, x is {self.x}"
})
MyClass = CustomType('MyClass', (object,), namespace, init_message='Hello, Dynamic MyClass!')

# Testing the created class
instance = MyClass()
print(instance.greeting())  # Output: "hello, x is 5"
