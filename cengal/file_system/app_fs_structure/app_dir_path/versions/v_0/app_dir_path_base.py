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


__all__ = ['DirNameOrPath', 'BaseDirID', 'DirTypeMapping', 'DirTypeMappingItem', 'norm_dir_name_or_path', 'AppDirPathBase']


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


import os
from cengal.file_system.directory_manager import ensure_dir as ensure_dir_exists
from .app_directory_types import AppDirectoryType
from typing import Union, Sequence, Any, Optional, Tuple, Dict
from functools import lru_cache


DirNameOrPath = Union[str, Sequence[str], None]
BaseDirID = Any
DirTypeMapping = Dict[AppDirectoryType, Tuple[BaseDirID, Optional[DirNameOrPath], Optional[DirNameOrPath]]]
DirTypeMappingItem = Tuple[BaseDirID, Optional[DirNameOrPath], Optional[DirNameOrPath]]


def norm_dir_name_or_path(dir_name_or_path: DirNameOrPath) -> Tuple[str, ...]:
    if dir_name_or_path is None:
        return ()
    elif isinstance(dir_name_or_path, str):
        return (dir_name_or_path,)
    elif isinstance(dir_name_or_path, (list, tuple)):
        # return tuple(dir_name_or_path)
        return dir_name_or_path
    else:
        raise TypeError('dir_name_or_path must be str, list or tuple')


class AppDirPathBase:
    def __init__(self, max_cache_size: Optional[int] = None) -> None:
        if max_cache_size is None:
            max_cache_size = len(AppDirectoryType) * 2 * 2 * 10  # 10 - is a number of applications; 2 - is `with_structure` [True/False]; 2 - is `ensure_dir` [True/False]

        self._max_cache_size = max_cache_size
        self._cached = self.__call__
        self.set_cache_size(max_cache_size)
    
    def get_cache_size(self) -> int:
        return self._max_cache_size
    
    def set_cache_size(self, max_cache_size: int) -> None:
        self._max_cache_size = max_cache_size
        del self._cached
        self._cached = lru_cache(maxsize=max_cache_size, typed=True)(self.__call__)
    
    def dir_type_mapping(self, dir_type: AppDirectoryType) -> DirTypeMappingItem:
        raise NotImplementedError
    
    def base_dir_id_to_path(self, base_dir_id: BaseDirID) -> str:
        raise NotImplementedError

    def __call__(self, dir_type: AppDirectoryType, app_name_or_path: DirNameOrPath, with_structure: bool = True, ensure_dir: bool = True) -> str:
        if AppDirectoryType.user_profile_data == dir_type:
            app_name_or_path = '.' + os.path.join(*norm_dir_name_or_path(app_name_or_path))

        mapping: DirTypeMappingItem = self.dir_type_mapping(dir_type)
        base_dir_path = self.base_dir_id_to_path(mapping[0])
        result_list = [base_dir_path]
        result_list.extend(norm_dir_name_or_path(mapping[1]))
        result_list.extend(norm_dir_name_or_path(app_name_or_path))
        if with_structure:
            result_list.extend(norm_dir_name_or_path(mapping[2]))
        
        result_path = os.path.normpath(os.path.join(*result_list))
        if ensure_dir:
            ensure_dir_exists(result_path)
        
        return result_path

    def cached(self, dir_type: AppDirectoryType, app_name_or_path: DirNameOrPath, with_structure: bool = True, ensure_dir: bool = True) -> str:
        return self._cached(dir_type, app_name_or_path, with_structure, ensure_dir)
