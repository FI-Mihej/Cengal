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
__version__ = "4.1.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import inspect
from cengal.introspection.inspect import is_async

async def func(a: int, b: bool) -> str:
    return f'{a} {b}'

print(inspect.isawaitable(func))
print(is_async(func))

awaitable = func(1, True)
print(inspect.isawaitable(awaitable))
print(is_async(awaitable))

print(func.__annotations__)
print(func.__code__.co_varnames)
print(func.__code__.co_argcount)
print(func.__code__.co_kwonlyargcount)
print(func.__code__.co_posonlyargcount)
print(func.__code__.co_nlocals)
print(func.__code__.co_stacksize)
print(func.__code__.co_flags)
print(func.__code__.co_code)
print(func.__code__.co_consts)
print(func.__code__.co_names)
print(func.__code__.co_varnames)
print(func.__code__.co_freevars)
print(func.__code__.co_cellvars)
print(func.__defaults__)
print(func.__kwdefaults__)
print(func.__closure__)
print(func.__annotations__)
print(func.__globals__)
print(func.__name__)
print(func.__qualname__)
print(func.__module__)
print(func.__doc__)
print(func.__dict__)
print(func.__wrapped__)
print(func.__code__)
