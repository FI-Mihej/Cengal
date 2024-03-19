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
from pprint import pprint
from cengal.introspection.inspect import current_entity_name, print_intro_func_repr, current_entity_owner_name, \
    entity_owning_module_info_and_owning_path, frame as frame_func, entity_class, entity_owner, entity_properties, pdi, \
    find_current_entity, entity_repr_owner_based


def method_decorator(method):
    frame = inspect.currentframe()
    method_name = frame.f_code.co_name
    pprint(frame.f_globals)
    pprint(dir(entity_owner(frame)))
    print(entity_owner(frame).__dict__)
    print(set(dir(entity_owner(frame))) == set(entity_owner(frame).__dict__.keys()))
    pprint(frame.f_locals)

    def wrapper(*args, **kwargs):
        print('Decorator')
        return method(*args, **kwargs)
    
    return wrapper

class MyClass:
    class MySubclass:
        def subclass_instance_method(self):
            print(repr(find_current_entity()))
            print(entity_repr_owner_based(find_current_entity()))
            frame = inspect.currentframe()
            method_name = frame.f_code.co_name
            pprint(frame.f_globals)
            pprint(dir(entity_owner(frame)))
            print(entity_owner(frame).__dict__)
            print(set(dir(entity_owner(frame))) == set(entity_owner(frame).__dict__.keys()))
            pprint(frame.f_locals)
            # method = frame.f_globals[method_name]
            # method_link = getattr(method.__self__, method_name)
            print("This is an instance method!")
            # return method_link

    def instance_method(self):
        print(repr(find_current_entity()))
        print(entity_repr_owner_based(find_current_entity()))
        pprint(entity_properties(MyClass))
        pdi(MyClass.__weakref__)
        pprint(entity_properties(MyClass.MySubclass))
        pdi(MyClass.MySubclass.__weakref__)
        frame = inspect.currentframe()
        method_name = frame.f_code.co_name
        pprint(frame.f_globals)
        pprint(dir(entity_owner(frame)))
        print('entity_properties(entity_owner(frame)):')
        pprint(entity_properties(entity_owner(frame)))
        print(entity_owner(frame).__dict__)
        print(set(dir(entity_owner(frame))) == set(entity_owner(frame).__dict__.keys()))
        pprint(frame.f_locals)
        # method = frame.f_globals[method_name]
        # method_link = getattr(method.__self__, method_name)
        print("This is an instance method!")
        # return method_link

    @method_decorator
    def decorated_instance_method(self):
        print(repr(find_current_entity()))
        print(entity_repr_owner_based(find_current_entity()))
        frame = inspect.currentframe()
        method_name = frame.f_code.co_name
        pprint(frame.f_globals)
        pprint(dir(entity_owner(frame)))
        print(entity_owner(frame).__dict__)
        print(set(dir(entity_owner(frame))) == set(entity_owner(frame).__dict__.keys()))
        pprint(frame.f_locals)
        # method = frame.f_globals[method_name]
        # method_link = getattr(method.__self__, method_name)
        print("This is an instance method!")
        # return method_link

    @classmethod
    def class_method(cls):
        print(repr(find_current_entity()))
        print(entity_repr_owner_based(find_current_entity()))
        frame = inspect.currentframe()
        method_name = frame.f_code.co_name
        pprint(frame.f_globals)
        pprint(dir(entity_owner(frame)))
        print(entity_owner(frame).__dict__)
        print(set(dir(entity_owner(frame))) == set(entity_owner(frame).__dict__.keys()))
        pprint(frame.f_locals)
        # method = frame.f_globals[method_name]
        # method_link = getattr(method.__self__, method_name)
        print("This is a class method!")
        # return method_link

    @staticmethod
    def static_method():
        print(repr(find_current_entity()))
        print(entity_repr_owner_based(find_current_entity()))
        frame = inspect.currentframe()
        method_name = frame.f_code.co_name
        pprint(frame.f_globals)
        pprint(dir(entity_owner(frame)))
        print(entity_owner(frame).__dict__)
        print(set(dir(entity_owner(frame))) == set(entity_owner(frame).__dict__.keys()))
        pprint(frame.f_locals)
        # method = frame.f_globals[method_name]
        # method_link = getattr(method.__self__, method_name)
        print("This is a class method!")
        # return method_link


sub_obj = MyClass.MySubclass()
print()
print('--------------------- sub_obj.subclass_instance_method(): ---------------------')
sub_obj.subclass_instance_method()
print()
print('---------------------')


obj = MyClass()
print()
print('--------------------- obj.instance_method(): ---------------------')
instance_method_link = obj.instance_method()  # Outputs: "This is an instance method!"
# instance_method_link()  # Outputs: "This is an instance method!"
print()
print('--------------------- MyClass.class_method(): ---------------------')

class_method_link = MyClass.class_method()  # Outputs: "This is a class method!"
# class_method_link()  # Outputs: "This is a class method!"
print()
print('--------------------- MyClass.static_method(): ---------------------')

class_method_link = MyClass.static_method()  # Outputs: "This is a class method!"
# class_method_link()  # Outputs: "This is a class method!"


class MyClass2:
    def instance_method(self):
        frame = inspect.currentframe()
        method_name = frame.f_code.co_name
        pprint(frame.f_globals)
        pprint(dir(entity_owner(frame)))
        print(entity_owner(frame).__dict__)
        print(set(dir(entity_owner(frame))) == set(entity_owner(frame).__dict__.keys()))
        pprint(frame.f_locals)
        # method = frame.f_globals[method_name]
        # method_link = getattr(method.__self__, method_name)
        print("This is an instance method!")
        # return method_link

    @classmethod
    def class_method(cls):
        frame = inspect.currentframe()
        method_name = frame.f_code.co_name
        pprint(frame.f_globals)
        pprint(dir(entity_owner(frame)))
        print(entity_owner(frame).__dict__)
        print(set(dir(entity_owner(frame))) == set(entity_owner(frame).__dict__.keys()))
        pprint(frame.f_locals)
        # method = frame.f_globals[method_name]
        # method_link = getattr(method.__self__, method_name)
        print("This is a class method!")
        # return method_link

obj = MyClass2()
print()
print('--------------------- obj.instance_method(): ---------------------')
instance_method_link = obj.instance_method()  # Outputs: "This is an instance method!"
# instance_method_link()  # Outputs: "This is an instance method!"
print()
print('--------------------- MyClass2.class_method(): ---------------------')

class_method_link = MyClass2.class_method()  # Outputs: "This is a class method!"
# class_method_link()  # Outputs: "This is a class method!"
print()
print('---------------------')
