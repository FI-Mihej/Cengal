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


__all__ = ['get_dict_item', 'get_dict_item_default', 'set_dict_item', 'del_dict_item', 'try_del_dict_item', 'srt_to_dict_path', 'dict_path_to_str']


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


from typing import Hashable, Dict, List


def get_dict_item(data: Dict, keys: List[Hashable]):
    rv = data
    for key in keys:
        rv = rv[key]
    
    return rv


def get_dict_item_default(data: Dict, keys: List[Hashable], default=None):
    rv = data
    for key in keys:
        try:
            rv = rv[key]
        except KeyError:
            return default
    
    return rv


def set_dict_item(data: Dict, keys: List[Hashable], value):
    rv = data
    path_len = len(keys)
    for index, key in enumerate(keys):
        if index == path_len - 1:
            rv[key] = value
            break

        rv = rv[key]
        

def del_dict_item(data: Dict, keys: List[Hashable]):
    rv = data
    path_len = len(keys)
    for index, key in enumerate(keys):
        rv = rv[key]
        if index == path_len - 2:
            del rv[keys[-1]]
            break
    
    return rv
        

def try_del_dict_item(data: Dict, keys: List[Hashable]):
    try:
        del_dict_item(data, keys)
    except KeyError:
        pass


def srt_to_dict_path(str_path) -> List[str]:
    return eval(str_path)


def dict_path_to_str(path: List[str]) -> str:
    path_str = ', '.join([f"'{sub_path}'" for sub_path in path])
    return f'[{path_str}]'
