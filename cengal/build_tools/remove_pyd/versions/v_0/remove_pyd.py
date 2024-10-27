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


__all__ = ['pyd_filter_func', 'remove_pyd_from_dir_tree']


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


import os
from typing import List, Tuple, Set
from cengal.file_system.path_manager import RelativePath, get_relative_path_part
from cengal.file_system.file_manager import last_ext, file_exists
from cengal.file_system.directory_manager import current_src_dir
from cengal.file_system.directory_manager import file_list_traversal, FilteringEntity
from cengal.introspection.inspect import exception_to_printable_text, get_exception


pycache_dir_name = '__pycache__'
pyd_file_ext = 'pyd'


def pyd_filter_func(filtering_entity: FilteringEntity, data) -> bool:
    if FilteringEntity.dirpath == filtering_entity:
        return True
    elif FilteringEntity.dirname == filtering_entity:
        return True
    elif FilteringEntity.filename == filtering_entity:
        dirpath, filename = data
        if pyd_file_ext == last_ext(filename):
            return True
    elif FilteringEntity.aggregated == filtering_entity:
        new_data: List[Tuple[str, List[str], List[str]]] = list()
        for dirpath, dirnames, filenames in data:
            if filenames:
                new_data.append((dirpath, list(), filenames))
        
        return new_data
    else:
        return False

    return False


def remove_pyd_from_dir_tree(root_dir_path: str):
    to_be_deleted: Set[str] = set()
    for dirpath, dirnames, filenames in file_list_traversal(root_dir_path, pyd_filter_func, True):
        dirpath_rel: RelativePath = RelativePath(dirpath)
        for filename in filenames:
            pyd_full_path = dirpath_rel(filename)
            to_be_deleted.add(pyd_full_path)
    
    for pyd_full_path in to_be_deleted:
        # print(f'Removing: {pyd_full_path}')
        if file_exists(pyd_full_path):
            print(f'Removing: {pyd_full_path}')
            try:
                os.remove(pyd_full_path)
            except:
                print(exception_to_printable_text(get_exception()))
