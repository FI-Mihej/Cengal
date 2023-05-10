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
__version__ = "3.1.17"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.introspection.inspect import CodeParamsWithValues, intro_func_params_with_values, intro_func_all_params_with_values, intro_func_all_params_with_values_as_ordered_dict, code_params_with_values_to_code, entity_repr, entity_owner_repr, entity_class, entity_repr_owner_based, intro_func_repr
from cengal.parallel_execution.coroutines.coro_scheduler import full_func_info_to_dict, CoroScheduler, current_interface
from pprint import pprint
import inspect


def equation(x , y , / , z, * , b, k, l = None):
    print(intro_func_repr())
    # code_params_with_values = intro_func_params_with_values()
    # print()
    # pprint(code_params_with_values)
    # pprint(intro_func_all_params_with_values())
    # pprint(intro_func_all_params_with_values_as_ordered_dict())
    return x * y + z


class Equation:
    def equation(self, x , y , / , z, * , b, k, l = None):
        print(intro_func_repr())
        # code_params_with_values = intro_func_params_with_values()
        # print()
        # pprint(code_params_with_values)
        # pprint(intro_func_all_params_with_values())
        # pprint(intro_func_all_params_with_values_as_ordered_dict())
        return x * y + z

    @staticmethod
    def equation_staticmethod(x , y , / , z, * , b, k, l = None):
        print(intro_func_repr())
        # code_params_with_values = intro_func_params_with_values()
        # print()
        # pprint(code_params_with_values)
        # pprint(intro_func_all_params_with_values())
        # pprint(intro_func_all_params_with_values_as_ordered_dict())
        return x * y + z


print(Equation.__name__)


print()
print('=== equation ===')
print(entity_repr_owner_based(equation))
print(entity_repr(equation))
# print(repr(equation))
# print(str(equation))
# print(equation.__annotations__)
# pprint(full_func_info_to_dict(equation))
# print(entity_repr(equation))
equation(1, 2, 3, b='b', k='k')
# m = inspect.getmodule(equation)
# print(m)
# print(m.__name__)


eq: Equation = Equation()

print()
print('=== Equation.equation ===')
print(entity_repr_owner_based(eq.equation))
print(entity_repr(eq.equation))
# pprint(full_func_info_to_dict(eq.equation))
# print(entity_repr(eq.equation))
eq.equation(1, 2, 3, b='b', k='k')

print()
print('=== eq<Equation>.equation_staticmethod ===')
print(entity_repr_owner_based(eq.equation_staticmethod))
print(entity_repr(eq.equation_staticmethod))
# pprint(full_func_info_to_dict(eq.equation_staticmethod))
# print(entity_repr(eq.equation_staticmethod))
eq.equation_staticmethod(1, 2, 3, b='b', k='k')

print()
print('=== Equation.equation ===')
print(entity_repr_owner_based(Equation.equation_staticmethod))
print(entity_repr(Equation.equation_staticmethod))
# pprint(full_func_info_to_dict(Equation.equation_staticmethod))
# print(entity_repr(Equation.equation_staticmethod))
Equation.equation_staticmethod(1, 2, 3, b='b', k='k')


print()
print('=== CoroScheduler.current_loop ===')
print(entity_repr_owner_based(CoroScheduler.current_loop))
print(entity_repr(CoroScheduler.current_loop))
# pprint(full_func_info_to_dict(CoroScheduler.current_loop))
# print(entity_repr(CoroScheduler.current_loop))
# CoroScheduler.current_loop()
# print(inspect.getmodule(CoroScheduler.current_loop))
# print(type(inspect.getmodule(CoroScheduler.current_loop)))
# # print(inspect.getmodule(CoroScheduler.current_loop.__func__))
# # print(type(inspect.getmodule(CoroScheduler.current_loop.__func__)))


print()
print('=== current_interface ===')
print(entity_repr_owner_based(current_interface))
print(entity_repr(current_interface))
# pprint(full_func_info_to_dict(current_interface))
# print(entity_repr(current_interface))
# # current_interface()
# m = inspect.getmodule(current_interface)
# print(m)
# print(m.__name__)
# print(repr(m))
# print(str(m))
# print(type(m))
# # print(inspect.getsourcefile(type(inspect.getmodule(current_interface))))
# f_code = current_interface.__code__
# print(entity_repr_owner_based(f_code))
# # print(f_code.__class__)
# # pprint(dir(f_code))
# # print(inspect.getmodule(f_code))
# # print(entity_owner_repr(f_code))

l = lambda k: print(k)
print(entity_repr_owner_based(l))
print(entity_repr(l))
# pprint(full_func_info_to_dict(l))
# print(entity_owner_repr(l))
# print(entity_owner_repr(l.__code__))

ll = lambda k, v: print(k, v)
print(entity_repr_owner_based(ll))
print(entity_repr(ll))
# pprint(full_func_info_to_dict(ll))


def equation_2(x , y , / , z, * , b, k, l = None):
    # code_params_with_values = intro_func_params_with_values()
    # print()
    # pprint(code_params_with_values)
    # pprint(intro_func_all_params_with_values())
    # pprint(intro_func_all_params_with_values_as_ordered_dict())
    def sub_equation(x , y , / , z):
        return x * y + z
    
    print(entity_repr_owner_based(sub_equation))
    print(entity_repr(sub_equation))
    # pprint(full_func_info_to_dict(sub_equation))
    # print(entity_owner_repr(sub_equation))
    # print(inspect.getmodule(sub_equation))

    lll = lambda k, v, f: print(k, v, f)
    
    print(entity_repr_owner_based(lll))
    print(entity_repr(lll))
    # pprint(full_func_info_to_dict(lll))
    # print(entity_owner_repr(lll))
    # print(inspect.getmodule(lll))

    return sub_equation(x, y, z)


equation_2(1, 2, 3, b='b', k='k')



class Equation2:
    class Equation3:
        @staticmethod
        def equation_3(x , y , / , z, * , b, k, l = None):
            # code_params_with_values = intro_func_params_with_values()
            # print()
            # pprint(code_params_with_values)
            # pprint(intro_func_all_params_with_values())
            # pprint(intro_func_all_params_with_values_as_ordered_dict())
            def sub_equation(x , y , / , z):
                return x * y + z
            
            # pprint(full_func_info_to_dict(sub_equation))
            # print(entity_owner_repr(sub_equation))
            # print(inspect.getmodule(sub_equation))
            print(entity_repr(sub_equation))

            lll = lambda k, v, f: print(k, v, f)
            
            # pprint(full_func_info_to_dict(lll))
            # print(entity_owner_repr(lll))
            # print(inspect.getmodule(lll))
            print(entity_repr(lll))

            return sub_equation(x, y, z)

        def equation_4(self, x , y , / , z, * , b, k, l = None):
            print(intro_func_repr())
            # code_params_with_values = intro_func_params_with_values()
            # print()
            # pprint(code_params_with_values)
            # pprint(intro_func_all_params_with_values())
            # pprint(intro_func_all_params_with_values_as_ordered_dict())
            def sub_equation(x , y , / , z):
                print(intro_func_repr())
                return x * y + z
            
            # pprint(full_func_info_to_dict(sub_equation))
            # print(entity_owner_repr(sub_equation))
            # print(inspect.getmodule(sub_equation))
            print(entity_repr(sub_equation))
            # print(entity_class(sub_equation))
            # print(sub_equation.__qualname__)

            lll = lambda k, v, f: print(intro_func_repr())
            
            # pprint(full_func_info_to_dict(lll))
            # print(entity_owner_repr(lll))
            # print(inspect.getmodule(lll))
            print(entity_repr(lll))
            # print(entity_class(lll))
            # print(lll.__qualname__)

            lll(1, 2, 3)
            return sub_equation(x, y, z)


Equation2.Equation3.equation_3(1, 2, 3, b='b', k='k')
eq3 = Equation2.Equation3()
print(entity_repr_owner_based(Equation2.Equation3.equation_3))
print(entity_repr(Equation2.Equation3.equation_3))
# print(entity_class(Equation2.Equation3.equation_3))
print(entity_repr_owner_based(Equation2.Equation3.equation_4))
print(entity_repr(Equation2.Equation3.equation_4))
# print(entity_class(Equation2.Equation3.equation_4))
# # pprint(dir(Equation2.Equation3.equation_3))
# pprint(Equation2.Equation3.equation_3.__qualname__)
# pprint(Equation2.Equation3.equation_3.__subclasshook__.__name__)
# # pprint(dir(Equation2.Equation3.equation_4))


print()
print(entity_repr_owner_based(eq3.equation_3))
print(entity_repr(eq3.equation_3))
# # print(entity_class(eq3.equation_3))
print()
print(entity_repr_owner_based(eq3.equation_4))
print(entity_repr(eq3.equation_4))
print()
# print(entity_class(eq3.equation_4))
# # pprint(dir(eq3.equation_3))
# # pprint(dir(eq3.equation_4))
# print(inspect.getmodule(eq3.equation_4))
print()
eq3.equation_4(1, 2, 3, b='b', k='k')
