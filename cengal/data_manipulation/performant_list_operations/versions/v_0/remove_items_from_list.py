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

__all__ = ['remove_items_from_list', 'is_need_to_convert_list_to_set_and_back_to_list', 'is_need_to_convert_list_to_set', 'is_need_to_convert_removable_list_to_set']

from typing import List, Set, Union

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


def is_need_to_convert_list_to_set_and_back_to_list(list_len: int, iterations_num: int) -> bool:
    convert_list_to_set = False
    if list_len < 100:
        convert_list_to_set = False
    elif list_len <= 1000:
        if iterations_num < 4:
            convert_list_to_set = False
        else:
            convert_list_to_set = True
    elif list_len <= 10000:
        if iterations_num < 2:
            convert_list_to_set = False
        else:
            convert_list_to_set = True
    elif list_len <= 100000:
        if iterations_num < 3:
            convert_list_to_set = False
        else:
            convert_list_to_set = True
    elif list_len <= 1000000:
        if iterations_num < 4:
            convert_list_to_set = False
        else:
            convert_list_to_set = True
    elif list_len <= 10000000:
        if iterations_num < 5:
            convert_list_to_set = False
        else:
            convert_list_to_set = True
    elif list_len <= 100000000:
        if iterations_num < 6:
            convert_list_to_set = False
        else:
            convert_list_to_set = True
    else:
        if iterations_num < 7:
            convert_list_to_set = False
        else:
            convert_list_to_set = True
    
    return convert_list_to_set


def is_need_to_convert_list_to_set(list_len: int, iterations_num: int) -> bool:
    convert_list_to_set = False
    if list_len < 100:
        convert_list_to_set = False
    elif list_len <= 1000:
        if iterations_num < 3:
            convert_list_to_set = False
        else:
            convert_list_to_set = True
    elif list_len <= 10000:
        if iterations_num < 2:
            convert_list_to_set = False
        else:
            convert_list_to_set = True
    elif list_len <= 100000:
        if iterations_num < 3:
            convert_list_to_set = False
        else:
            convert_list_to_set = True
    elif list_len <= 1000000:
        if iterations_num < 3:
            convert_list_to_set = False
        else:
            convert_list_to_set = True
    elif list_len <= 10000000:
        if iterations_num < 4:
            convert_list_to_set = False
        else:
            convert_list_to_set = True
    elif list_len <= 100000000:
        if iterations_num < 4:
            convert_list_to_set = False
        else:
            convert_list_to_set = True
    else:
        if iterations_num < 4:
            convert_list_to_set = False
        else:
            convert_list_to_set = True
    
    return convert_list_to_set


def is_need_to_convert_removable_list_to_set(source_list_len: int, removable_list_len: int) -> bool:
    convert_removable_list_to_set = False
    if source_list_len == 1:
        if removable_list_len < 21:
            convert_removable_list_to_set = False
        else:
            convert_removable_list_to_set = True
    elif source_list_len == 2:
        if removable_list_len < 20:
            convert_removable_list_to_set = False
        else:
            convert_removable_list_to_set = True
    elif source_list_len == 3:
        if removable_list_len < 25:
            convert_removable_list_to_set = False
        else:
            convert_removable_list_to_set = True
    elif source_list_len == 4:
        if removable_list_len < 30:
            convert_removable_list_to_set = False
        else:
            convert_removable_list_to_set = True
    elif source_list_len == 5:
        if removable_list_len < 31:
            convert_removable_list_to_set = False
        else:
            convert_removable_list_to_set = True
    elif source_list_len == 6:
        if removable_list_len < 35:
            convert_removable_list_to_set = False
        else:
            convert_removable_list_to_set = True
    elif source_list_len == 7:
        if removable_list_len < 42:
            convert_removable_list_to_set = False
        else:
            convert_removable_list_to_set = True
    elif source_list_len == 8:
        if removable_list_len < 47:
            convert_removable_list_to_set = False
        else:
            convert_removable_list_to_set = True
    elif source_list_len == 9:
        if removable_list_len < 52:
            convert_removable_list_to_set = False
        else:
            convert_removable_list_to_set = True
    elif source_list_len == 10:
        if removable_list_len < 60:
            convert_removable_list_to_set = False
        else:
            convert_removable_list_to_set = True
    elif source_list_len == 11:
        if removable_list_len < 70:
            convert_removable_list_to_set = False
        else:
            convert_removable_list_to_set = True
    elif source_list_len == 12:
        if removable_list_len < 81:
            convert_removable_list_to_set = False
        else:
            convert_removable_list_to_set = True
    elif source_list_len == 13:
        if removable_list_len < 85:
            convert_removable_list_to_set = False
        else:
            convert_removable_list_to_set = True
    elif source_list_len == 14:
        if removable_list_len < 90:
            convert_removable_list_to_set = False
        else:
            convert_removable_list_to_set = True
    else:
        convert_removable_list_to_set = False
    
    return convert_removable_list_to_set


def remove_items_from_list(source: Union[List, Set], removable: Union[List, Set], preserve_source_order: bool = False, remove_duplicates: bool = False) -> List:
    """[Will choose most fast algorithm according to given datasets lengths]

    Args:
        source (Union[List, Set]): [Input data set. Original external value may be modified inside this function. Use `copy.copy(source)`, `list(source)` or `set(source)` when you need to prevent modification of the original data set]
        removable (Union[List, Set]): [list of items which should be removed out from source data set]
        preserve_source_order (bool, optional): [Will always preserve source's data order on True (not a fastest choose in some cases)]. Defaults to False.
        remove_duplicates (bool, optional): [Will always remove duplicates out from source's data set on True (not a fastest choose in some cases)]. Defaults to False.

    Returns:
        List: [resulting data set]
    """    
    convert_removable_list_to_set = preserve_source_order or is_need_to_convert_removable_list_to_set(len(source), len(removable))
    
    if convert_removable_list_to_set:
        if remove_duplicates:
            new_source = set()
            convert_list_to_set = is_need_to_convert_list_to_set_and_back_to_list(len(removable), len(source))
            if convert_list_to_set:
                if not isinstance(removable, set):
                    removable = set(removable)
                
            for item in source:
                if item in removable:
                    continue
                new_source.add(item)
            
            return list(new_source)
        else:
            new_source = list()
            convert_list_to_set = is_need_to_convert_list_to_set_and_back_to_list(len(removable), len(source))
            if convert_list_to_set:
                if not isinstance(removable, set):
                    removable = set(removable)
                
            for item in source:
                if item in removable:
                    continue
                new_source.append(item)
            
            return new_source
    
    convert_source_list_to_set = remove_duplicates or is_need_to_convert_list_to_set_and_back_to_list(len(source), len(removable))
    if convert_source_list_to_set:
        if not isinstance(source, set):
            source = set(source)

    for removed in removable:
        if removed in source:
            source.remove(removed)
    
    if convert_source_list_to_set:
        return list(source)
    else:
        return source
