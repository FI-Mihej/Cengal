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


from cengal.introspection.inspect import *
from inspect import isfunction, ismethod, isclass, ismethoddescriptor, getattr_static
from collections.abc import MutableMapping
from dataclasses import dataclass
from pprint import pprint
from types import MappingProxyType


class CustomDict(MutableMapping):
    def __init__(self):
        self.store = {}
        
    def __getitem__(self, key):
        value = self.store[key]
        print(f"Getting item: {key=} {value=}")
        return value
    
    def __setitem__(self, key, value):
        print(f"Setting item: {key=} to {value=}")
        self.store[key] = value
    
    def __delitem__(self, key):
        del self.store[key]
    
    def __iter__(self):
        return iter(self.store)
    
    def __len__(self):
        return len(self.store)


def tgeneralobject_custom_getattribute(self, name):
    if name == '_tgeneralobject_imutablemapping_attributes' or name.startswith('__'):
        return object.__getattribute__(self, name)
    
    try:
        return self._tgeneralobject_imutablemapping_attributes[name]
    except KeyError:
        pass
    
    return object.__getattribute__(self, name)


def tgeneralobject_custom_setattr(self, name, value):
    has_value_static: bool = False
    value_static = None
    try:
        value_static = getattr_static(self, name)
        has_value_static = True
    except AttributeError:
        pass

    try:
        if has_value_static and isfunction(value_static) or ismethod(value_static) or isinstance(value_static, FrameType) or isinstance(value_static, CodeType) or ismethoddescriptor(value_static):
            object.__setattr__(self, name, value)
            return
    except AttributeError:
        pass

    if name == '_tgeneralobject_imutablemapping_attributes' or name.startswith('__'):
        object.__setattr__(self, name, value)
    else:
        try:
            if has_value_static and is_setable_data_descriptor(value_static):
                object.__setattr__(self, name, value)
        except AttributeError:
            pass
        
        self._tgeneralobject_imutablemapping_attributes[name] = value


def tgeneralobject_custom_delattr(self, name):
    has_value_static: bool = False
    value_static = None
    try:
        value_static = getattr_static(self, name)
        has_value_static = True
    except AttributeError:
        pass

    try:
        if has_value_static and isfunction(value_static) or ismethod(value_static) or isinstance(value_static, FrameType) or isinstance(value_static, CodeType) or ismethoddescriptor(value_static):
            object.__delattr__(self, name)
    except AttributeError:
        pass

    if name == '_tgeneralobject_imutablemapping_attributes' or name.startswith('__'):
        object.__delattr__(self, name)
    else:
        try:
            if has_value_static and (not isclass(value_static)) and hasattr(value_static, "__delete__"):
                object.__delattr__(self, name)
        except AttributeError:
            pass
        
        try:
            del self._tgeneralobject_imutablemapping_attributes[name]
        except KeyError:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")


def tgeneralobject_create_wrapping_class(base):
    # Create the class dynamically with type()
    return type(
        'Wrapped' + base.__name__,
        (base,),
        {
            '__getattribute__': tgeneralobject_custom_getattribute,
            '__setattr__': tgeneralobject_custom_setattr,
            '__delattr__': tgeneralobject_custom_delattr,
            '__init__': lambda self: setattr(self, '_tgeneralobject_imutablemapping_attributes', CustomDict()),
        }
    )

def tgeneralobject_wrap_obj(obj, mapped_obj_dict: CustomDict, init_mapped_obj_dict: bool):
    base = obj.__class__
    if init_mapped_obj_dict:
        object_fields = set(dir(object))
        obj_fields = set(dir(obj)) - object_fields
        for key in obj_fields:
            value = getattr_static(obj, key)
            if key == '_tgeneralobject_imutablemapping_attributes' or key.startswith('__'):
                continue

            if isfunction(value) or ismethod(value) or isinstance(value, FrameType) or isinstance(value, CodeType) or ismethoddescriptor(value):
                continue

            if (not isclass(value)) and (hasattr(value, "__get__") and (not (hasattr(value, "__set__") or hasattr(value, "__delete__")))):
                continue

            mapped_obj_dict[key] = getattr(obj, key)
    
    setattr(obj, '_tgeneralobject_imutablemapping_attributes', mapped_obj_dict)
    NewClass = type(
        base.__name__ + 'WrappedByTGeneralObject',
        (base,),
        {
            '__getattribute__': tgeneralobject_custom_getattribute,
            '__setattr__': tgeneralobject_custom_setattr,
            '__delattr__': tgeneralobject_custom_delattr,
        }
    )
    obj.__class__ = NewClass

# Example usage with a base class
@dataclass
class BaseClass:
    a = 5
    b = 'hello'

    def base_method(self):
        return "This method is from the base class."


obj = BaseClass()
print('__DATACLASS_PARAMS__:', dir(obj.__dataclass_params__))
print(f"{hasattr(getattr_static(obj, '__dataclass_params__'), '__get__')=}")
print(f"{hasattr(obj.a, '__get__')=}")
print(f"{hasattr(getattr_static(obj, 'a'), '__get__')=}")
print(f'{hasattr(obj, "__dict__")=}')
pprint(obj.__dict__)
print(f'{hasattr(obj, "_tgeneralobject_imutablemapping_attributes")=}')
tgeneralobject_wrap_obj(obj, CustomDict(), True)
print(f'{hasattr(obj, "__dict__")=}')
pprint(obj.__dict__)
print(f'{hasattr(obj, "_tgeneralobject_imutablemapping_attributes")=}')
pprint(dict(obj._tgeneralobject_imutablemapping_attributes))
obj.some_attr = "Test"
print(obj.some_attr)  # Output: "Test"
print(obj.base_method())  # Output: "This method is from the base class."
obj.a += 4
print(obj.a)  # Output: "Test"
obj.a = 34
print(obj.a)  # Output: "Test"
obj.b = 'world'
print(obj.b)  # Output: "Test"

pprint(obj.__dict__)
pprint(dict(obj._tgeneralobject_imutablemapping_attributes))

print('=====================================')

# Example usage with a base class
class BaseClass1:
    __slots__ = ('a', 'b')

    def __init__(self) -> None:
        self.a = 5
        self.b = 'hello'

    def base_method(self):
        return "This method is from the base class."


obj = BaseClass1()
print(f"{hasattr(obj.__slots__, '__get__')=}")
print(f"{hasattr(getattr(obj, '__slots__'), '__get__')=}")
print(f"{hasattr(getattr_static(obj, '__slots__'), '__get__')=}")
print(f"{hasattr(obj.a, '__get__')=}")
print(f"{hasattr(getattr(obj, 'a'), '__get__')=}")
print(f"{hasattr(getattr_static(obj, 'a'), '__get__')=}")
print(f'{hasattr(obj, "__dict__")=}')
