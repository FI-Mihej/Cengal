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


__all__ = ['module_dir', 'module_rel_path', 'module_import_str', 'current_module_dir', 'current_module_rel_path', 'current_module_import_str']


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


from cengal.introspection.inspect import entity_owning_module_info_and_owning_path, get_module_importable_str_and_path, frame
from cengal.introspection.inspect import entity_name
from cengal.file_system.path_manager import get_relative_path_part
from cengal.text_processing.text_processing import removesuffix
import os
from typing import Optional


def module_dir(library_module) -> str:
    module_file_full_path = get_module_importable_str_and_path(library_module)[1]
    return os.path.dirname(module_file_full_path)


def module_rel_path(library_top_module, library_module) -> str:
    module_file_full_path = get_module_importable_str_and_path(library_module)[1]
    top_init_file_full_path: str = get_module_importable_str_and_path(library_top_module)[1]
    library_dir_full_path: str = os.path.dirname(top_init_file_full_path)
    return get_relative_path_part(module_file_full_path, library_dir_full_path)


def module_import_str(library_top_module, library_module) -> str:
    result: str = f'{entity_name(library_top_module)}/{module_rel_path(library_top_module, library_module)}'
    result = result.replace('\\', '/')
    result = result.replace('//', '/')
    result = result.strip('/')
    result = removesuffix(result, '.py')
    result = result.strip('/')
    result = result.replace('/', '.')
    return result


def current_module_dir(depth: Optional[int] = 1) -> str:
    _, _, module_file_full_path, _ = entity_owning_module_info_and_owning_path(frame(depth + 1))
    return os.path.dirname(module_file_full_path)


def current_module_rel_path(library_top_module, depth: Optional[int] = 1) -> str:
    _, _, module_file_full_path, _ = entity_owning_module_info_and_owning_path(frame(depth + 1))
    top_init_file_full_path: str = get_module_importable_str_and_path(library_top_module)[1]
    library_dir_full_path: str = os.path.dirname(top_init_file_full_path)
    return get_relative_path_part(module_file_full_path, library_dir_full_path)


def current_module_import_str(library_top_module, depth: Optional[int] = 1) -> str:
    result: str = f'{entity_name(library_top_module)}/{current_module_rel_path(library_top_module, depth + 1)}'
    result = result.replace('\\', '/')
    result = result.replace('//', '/')
    result = result.strip('/')
    result = removesuffix(result, '.py')
    result = result.strip('/')
    result = result.replace('/', '.')
    return result
