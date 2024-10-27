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


__all__ = [
    'intenum_dict_to_list',
    'intenum_kwargs_to_list', 
    'intenum_list_to_dict',
    'IntEnumStruct', 
]


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


from enum import IntEnum

from typing import Any, Optional, List, Dict, Type, Mapping


def intenum_dict_to_list(mapping: Mapping, int_enum_class: Optional[Type[IntEnum]] = None) -> List:
    """Example:
    class MyEnum(IntEnum):
        a = 1
        b = 2
        c = 3

    print(intenum_dict_to_list({MyEnum.a: 'A', MyEnum.b: 'B', MyEnum.c: 'C'}, MyEnum))
    # Output: ['A', 'B', 'C']


    print(intenum_dict_to_list({MyEnum.b: 'B', MyEnum.a: 'A', MyEnum.c: 'C'}, MyEnum))
    # Output: ['A', 'B', 'C']

    print(intenum_dict_to_list({MyEnum.a: 'A', MyEnum.c: 'C'}, MyEnum))
    # Output: ['A', None, 'C']

    Args:
        mapping (Mapping): _description_
        int_enum_class (Optional[Type[IntEnum]], optional): _description_. Defaults to None.

    Returns:
        List: _description_
    """    
    if int_enum_class:
        items_num = len(int_enum_class)
    else:
        first_key_type_detected: bool = False
        for first_key in mapping.keys():
            first_key_type = type(first_key)
            if issubclass(first_key_type, IntEnum):
                items_num = len(first_key_type)
                first_key_type_detected = True
        
        if not first_key_type_detected:
            items_num = max(mapping.keys(), key=lambda value: int(value))
    
    result = [None] * items_num
    for key, value in mapping.items():
        result[int(key)] = value
    
    return result


def intenum_kwargs_to_list(int_enum_class: Type[IntEnum], **kwargs) -> List:
    """Example:
    class MyEnum(IntEnum):
        a = 1
        b = 2
        c = 3

    print(intenum_kwargs_to_list(MyEnum, a='A', b='B', c='C'))
    # Output: ['A', 'B', 'C']


    print(intenum_kwargs_to_list(MyEnum, b='B', a='A', c='C'))
    # Output: ['A', 'B', 'C']

    print(intenum_kwargs_to_list(MyEnum, a='A', c='C'))
    # Output: ['A', None, 'C']


    Args:
        int_enum_class (Type[IntEnum]): _description_

    Returns:
        List: _description_
    """    
    item_per_name = {item.name: item for item in int_enum_class}
    mapping: Dict[IntEnum, object] = {item_per_name[key]: value for key, value in kwargs.items()}
    return intenum_dict_to_list(mapping, int_enum_class)


def intenum_list_to_dict(data_list: List, int_enum_class: Optional[Type] = None) -> Dict:
    if int_enum_class:
        return {int_enum_class(key): value for key, value in enumerate(data_list)}
    else:
        return {key: value for key, value in enumerate(data_list)}


class IntEnumStruct:
    def __init__(self, int_enum_class: Type[IntEnum]):
        self.int_enum_class = int_enum_class
    
    def __call__(self, *args: Any, **kwargs : Any) -> Any:
        if args:
            return intenum_dict_to_list(args[0], self.int_enum_class)
        else:
            return intenum_kwargs_to_list(self.int_enum_class, **kwargs)
    
    def decode_list(self, data_list: List) -> Dict:
        return intenum_list_to_dict(data_list, self.int_enum_class)
    
    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.int_enum_class)})'
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}({str(self.int_enum_class)})'
