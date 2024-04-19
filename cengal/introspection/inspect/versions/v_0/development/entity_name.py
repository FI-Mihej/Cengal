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
__version__ = "4.3.4"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.parallel_execution.coroutines.coro_standard_services.wait_coro import WaitCoroRequest
from cengal.introspection.inspect import current_entity_name, print_intro_func_repr, current_entity_owner_name, \
    entity_owning_module_info_and_owning_path, frame, entity_class, entity_owner, entity_name, \
    entity_is_unbound_method, entity_is_method, entity_is_function, entity_properties, get_code, pdi, \
    entity_name, find_entity


print(current_entity_name())
print(entity_name(frame()))
print(current_entity_owner_name())
print(entity_owning_module_info_and_owning_path(frame()))
print(repr(entity_class(frame())))
print(repr(entity_owner(frame())))
print(dir(entity_owner(frame())))
print(pdi(get_code(entity_owner(frame()))))
# print(pdi(entity_owner(frame()).__code__))  # `module '__main__' has no attribute '__code__'`
print()
print('~~~~~~~~~~~~~~~~~~~~~~')
print()


def my_func():
    print(entity_is_unbound_method(my_func))
    print(entity_is_unbound_method(frame()))
    print(entity_is_function(my_func))
    print(entity_is_function(frame()))
    print(entity_is_method(my_func))
    print(entity_is_method(frame()))
    print(current_entity_name())
    print(entity_name(my_func))
    print(entity_name(frame()))
    print(current_entity_owner_name())
    print(entity_owning_module_info_and_owning_path(my_func))
    print(entity_owning_module_info_and_owning_path(frame()))
    print(repr(entity_class(my_func)))
    print(repr(entity_class(frame())))
    print(repr(entity_owner(my_func)))
    print(repr(entity_owner(frame())))
    print()
    print_intro_func_repr()
    print_intro_func_repr(verbose=True)
    print('---------------------')

my_func()


class MyClass:
    def __init__(self) -> None:
        entity_instance = find_entity(frame())
        print('find_entity:', entity_name(entity_instance))
        print('entity_class(entity_instance):', entity_class(entity_instance))
        print(entity_is_unbound_method(self.__init__))
        print(entity_is_unbound_method(frame()))
        print(entity_is_method(self.__init__))
        print(entity_is_method(frame()))
        print(entity_is_function(self.__init__))
        print(entity_is_function(frame()))
        print(current_entity_name())
        print(entity_name(self.__init__))
        print(entity_name(frame()))
        print(current_entity_owner_name())
        print(entity_owning_module_info_and_owning_path(self.__init__))
        print(entity_owning_module_info_and_owning_path(frame()))
        print(repr(entity_class(self.__init__)))
        print(repr(entity_class(frame())))
        print(repr(entity_owner(self.__init__)))
        print(repr(entity_owner(frame())))
        print()
        print_intro_func_repr()
        print_intro_func_repr(verbose=True)
        print('---------------------')
    
    def my_method(self):
        print(entity_is_unbound_method(self.my_method))
        print(entity_is_unbound_method(frame()))
        print(entity_is_method(self.my_method))
        print(entity_is_method(frame()))
        print(entity_is_function(self.my_method))
        print(entity_is_function(frame()))
        print(current_entity_name())
        print(entity_name(self.my_method))
        print(entity_name(frame()))
        print(current_entity_owner_name())
        print(entity_owning_module_info_and_owning_path(self.my_method))
        print(entity_owning_module_info_and_owning_path(frame()))
        print(repr(entity_class(self.my_method)))
        print(repr(entity_class(frame())))
        print(repr(entity_owner(self.my_method)))
        print(repr(entity_owner(frame())))
        print()
        print_intro_func_repr()
        print_intro_func_repr(verbose=True)
        print('---------------------')
    
    # def my_method_keyword(*, self=None):
    #     print(entity_is_unbound_method(self.my_method_keyword))
    #     print(entity_is_unbound_method(frame()))
    #     print(entity_is_method(self.my_method_keyword))
    #     print(entity_is_method(frame()))
    #     print(entity_is_function(self.my_method_keyword))
    #     print(entity_is_function(frame()))
    #     print(current_entity_name())
    #     print(entity_name(self.my_method_keyword))
    #     print(entity_name(frame()))
    #     print(current_entity_owner_name())
    #     print(entity_owning_module_info_and_owning_path(self.my_method_keyword))
    #     print(entity_owning_module_info_and_owning_path(frame()))
    #     print(repr(entity_class(self.my_method_keyword)))
    #     print(repr(entity_class(frame())))
    #     print(repr(entity_owner(self.my_method_keyword)))
    #     print(repr(entity_owner(frame())))
    #     print()
    #     print_intro_func_repr()
    #     print_intro_func_repr(verbose=True)
    #     print('---------------------')
    
    @staticmethod
    def my_static_method():
        print(entity_is_unbound_method(MyClass.my_static_method))
        print(entity_is_unbound_method(frame()))
        print(entity_is_method(MyClass.my_static_method))
        print(entity_is_method(frame()))
        print(entity_is_function(MyClass.my_static_method))
        print(entity_is_function(frame()))
        print(current_entity_name())
        print(entity_name(MyClass.my_static_method))
        print(entity_name(frame()))
        print(current_entity_owner_name())
        print(entity_owning_module_info_and_owning_path(MyClass.my_static_method))
        print(entity_owning_module_info_and_owning_path(frame()))
        print(repr(entity_class(MyClass.my_static_method)))
        print(repr(entity_class(frame())))
        print(repr(entity_owner(MyClass.my_static_method)))
        print(repr(entity_owner(frame())))
        print()
        print_intro_func_repr()
        print_intro_func_repr(verbose=True)
        print('---------------------')


MyClass().my_method()
MyClass.my_static_method()
MyClass().my_static_method()
# MyClass().my_method_keyword()
