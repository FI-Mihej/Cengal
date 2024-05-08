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


# Define the CustomDict as before
class CustomDict(MutableMapping):
    def __init__(self, init_message):
        self.store = {}
        self.init_message = init_message
        print(f"CustomDict initialized: {init_message}")

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

# Define the CustomType metaclass as before
class CustomType(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        init_message = kwds.get('init_message', 'Default message')
        return CustomDict(init_message)

    def __new__(cls, name, bases, namespace, **kwds):
        return super().__new__(cls, name, bases, dict(namespace))

    def __init__(cls, name, bases, namespace, **kwds):
        super().__init__(name, bases, namespace)

class MyClassM(metaclass=CustomType, init_message='Hello, this is MyClass!'):
    x = 5
    y = 'hello'

    def greeting(self):
        return f"{self.y}, x is {self.x}"


class MyClass():
    x = 5
    y = 'hello'

    def greeting(self):
        return f"{self.y}, x is {self.x}"


# Dynamically creating MyClass using type()
MyClassD = type(
    'MyClassD',  # Name of the class
    (object,),  # Tuple of the base classes (can be other bases as needed)
    {
        '__metaclass__': CustomType,
        'init_message': 'Hello, Dynamic MyClass!',
        'x': 5,
        'y': 'hello',
        'greeting': lambda self: f"{self.y}, x is {self.x}"
    }
)

# Example of using the dynamically created class
instance = MyClassM()
print(instance.greeting())  # Should work as defined in the lambda function

print('==================================================')

# Assuming CustomDict and CustomType are defined as previously discussed

# Use the CustomType metaclass directly to create the class
MyClassC = CustomType(
    'MyClassC',  # Name of the class
    (object,),  # Tuple of the base classes
    {},         # Namespace, initially empty
    init_message='Hello, Dynamic MyClass!'  # Custom initialization message passed to __prepare__
)

# Adding class attributes after the class has been created
MyClassC.x = 5
MyClassC.y = 'hello'
MyClassC.greeting = lambda self: f"{self.y}, x is {self.x}"

# Example of using the dynamically created class
instance = MyClassC()
print(instance.greeting())  # Output should reflect the lambda function defined above
