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


from cengal.parallel_execution.coroutines.coro_standard_services.wait_coro import WaitCoroRequest
from cengal.introspection.inspect import entity_properties, entity_repr, entity_properties_values, entity_repr_limited_try_qualname


print(f'{dir(WaitCoroRequest)=}')
print()

print(f'{dir(WaitCoroRequest())=}')
print()


print(f'{entity_properties(WaitCoroRequest)=}')
print()


print(f'{entity_properties(WaitCoroRequest())=}')
print()

print(f'{entity_repr(WaitCoroRequest())=}')
print()

print(f'{entity_repr_limited_try_qualname(WaitCoroRequest())=}')
print()

print(f'{entity_properties_values(WaitCoroRequest())=}')
print()

def my_func(a, b, *, c, d):
    return a + b + c + d

my_func.my_property = 2

print(f'{entity_repr(my_func)=}')
print()

print(f'{entity_repr_limited_try_qualname(my_func)=}')
print()

print(f'{entity_properties(my_func)=}')
print()
