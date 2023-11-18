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
__version__ = "3.4.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.entities.bindable_to_type import *


class MyData(BindableToType):
    def __init__(self) -> None:
        super().__init__()
        self.data = 1


class MyGlobalData(BindableToType):
    def __init__(self) -> None:
        super().__init__()
        self.data = 2


class MyStructure:
    global_data = MyGlobalData()
    def __init__(self):
        self.index = 3
        self.data = MyData()

print(f'{MyStructure.global_data.bound_to() = }')  # (<class '__main__.MyStructure'>, 'global_data')

ms = MyStructure()

print(f'{ms.global_data.bound_to() = }')  # (<class '__main__.MyStructure'>, 'global_data')

print(f'{ms.data.bound_to() = }')  # None
try:
    print(f'{MyStructure.data.bound_to() = }')  # raise AttributeError
except AttributeError:
    pass

MyGlobalData().bind(MyStructure, 'global_data_2')

print(f'{ms.global_data_2.bound_to() = }')  # (<class '__main__.MyStructure'>, 'global_data')
print(f'{MyStructure.global_data_2.bound_to() = }')  # (<class '__main__.MyStructure'>, 'global_data')

MyGlobalData().bind(ms, 'global_data_3')

print(f'{ms.global_data_3.bound_to() = }')  # (<class '__main__.MyStructure'>, 'global_data_2')
print(f'{MyStructure.global_data_3.bound_to() = }')  # (<class '__main__.MyStructure'>, 'global_data_2')
