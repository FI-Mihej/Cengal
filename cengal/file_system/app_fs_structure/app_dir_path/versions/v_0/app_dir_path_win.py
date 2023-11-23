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


__all__ = ['app_dir_path', 'app_dir_path_cached', 'AppDirPath', 'SHGetKnownFolderPathError']


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


# More info:
# https://docs.microsoft.com/en-us/windows/win32/shell/knownfolderid
# https://docs.microsoft.com/en-us/windows/win32/api/shlobj_core/nf-shlobj_core-shgetknownfolderpath


import os
from ctypes import POINTER, byref, c_wchar_p
from cengal.ctypes_tools.types import GUID
from cengal.ctypes_tools.constants import KnownfolderidConstants
from cengal.ctypes_tools.result_api import SHGetKnownFolderPathError, SHGetKnownFolderPath
from cengal.file_system.directory_manager import ensure_dir as ensure_dir_exists
from .app_directory_types import AppDirectoryType
from .app_dir_path_base import AppDirPathBase, DirTypeMappingItem, DirTypeMappingItem, BaseDirID, DirNameOrPath, norm_dir_name_or_path
from typing import Optional, Tuple, Dict
from functools import lru_cache


dir_type_mapping: Dict[AppDirectoryType, Tuple[GUID, Optional[DirNameOrPath], Optional[DirNameOrPath]]] = {
    AppDirectoryType.local_data: (KnownfolderidConstants.FOLDERID_LocalAppData, None, 'data'),
    AppDirectoryType.local_cache: (KnownfolderidConstants.FOLDERID_LocalAppData, None, 'cache'),
    AppDirectoryType.local_config: (KnownfolderidConstants.FOLDERID_LocalAppData, None, 'config'),
    AppDirectoryType.local_log: (KnownfolderidConstants.FOLDERID_LocalAppData, None, 'log'),
    AppDirectoryType.local_temp: (KnownfolderidConstants.FOLDERID_LocalAppData, None, 'temp'),
    AppDirectoryType.local_runtime: (KnownfolderidConstants.FOLDERID_LocalAppData, None, 'runtime'),

    AppDirectoryType.local_low_data: (KnownfolderidConstants.FOLDERID_LocalAppDataLow, None, 'data'),
    AppDirectoryType.local_low_cache: (KnownfolderidConstants.FOLDERID_LocalAppDataLow, None, 'cache'),
    AppDirectoryType.local_low_config: (KnownfolderidConstants.FOLDERID_LocalAppDataLow, None, 'config'),
    AppDirectoryType.local_low_log: (KnownfolderidConstants.FOLDERID_LocalAppDataLow, None, 'log'),
    AppDirectoryType.local_low_temp: (KnownfolderidConstants.FOLDERID_LocalAppDataLow, None, 'temp'),
    AppDirectoryType.local_low_runtime: (KnownfolderidConstants.FOLDERID_LocalAppDataLow, None, 'runtime'),

    AppDirectoryType.roaming_data: (KnownfolderidConstants.FOLDERID_RoamingAppData, None, 'data'),
    AppDirectoryType.roaming_cache: (KnownfolderidConstants.FOLDERID_RoamingAppData, None, 'cache'),
    AppDirectoryType.roaming_config: (KnownfolderidConstants.FOLDERID_RoamingAppData, None, 'config'),
    AppDirectoryType.roaming_log: (KnownfolderidConstants.FOLDERID_RoamingAppData, None, 'log'),
    AppDirectoryType.roaming_temp: (KnownfolderidConstants.FOLDERID_RoamingAppData, None, 'temp'),
    AppDirectoryType.roaming_runtime: (KnownfolderidConstants.FOLDERID_RoamingAppData, None, 'runtime'),

    AppDirectoryType.program_data: (KnownfolderidConstants.FOLDERID_ProgramData, None, 'data'),
    AppDirectoryType.program_cache: (KnownfolderidConstants.FOLDERID_ProgramData, None, 'cache'),
    AppDirectoryType.program_config: (KnownfolderidConstants.FOLDERID_ProgramData, None, 'config'),
    AppDirectoryType.program_log: (KnownfolderidConstants.FOLDERID_ProgramData, None, 'log'),
    AppDirectoryType.program_temp: (KnownfolderidConstants.FOLDERID_ProgramData, None, 'temp'),
    AppDirectoryType.program_runtime: (KnownfolderidConstants.FOLDERID_ProgramData, None, 'runtime'),

    AppDirectoryType.program_files: (KnownfolderidConstants.FOLDERID_ProgramFiles, None, None),
    AppDirectoryType.program_files_common: (KnownfolderidConstants.FOLDERID_ProgramFilesCommon, None, None),

    AppDirectoryType.user_profile_data: (KnownfolderidConstants.FOLDERID_Profile, None, None),
    AppDirectoryType.user_profile_program_files: (KnownfolderidConstants.FOLDERID_UserProgramFiles, None, None),
    AppDirectoryType.user_profile_program_files_common: (KnownfolderidConstants.FOLDERID_UserProgramFilesCommon, None, None),

    AppDirectoryType.local_static_data: (KnownfolderidConstants.FOLDERID_LocalAppData, None, 'static_data'),
    AppDirectoryType.local_low_static_data: (KnownfolderidConstants.FOLDERID_LocalAppDataLow, None, 'static_data'),
    AppDirectoryType.roaming_static_data: (KnownfolderidConstants.FOLDERID_RoamingAppData, None, 'static_data'),
    AppDirectoryType.program_static_data: (KnownfolderidConstants.FOLDERID_ProgramData, None, 'static_data'),
}


def app_dir_path(dir_type: AppDirectoryType, app_name_or_path: DirNameOrPath, with_structure: bool = True, ensure_dir: bool = True) -> str:
    if AppDirectoryType.user_profile_data == dir_type:
        app_name_or_path = '.' + norm_dir_name_or_path(app_name_or_path)

    mapping: Tuple[GUID, Optional[DirNameOrPath], Optional[DirNameOrPath]] = dir_type_mapping[dir_type]
    base_dir_path = SHGetKnownFolderPath(mapping[0])
    result_list = [base_dir_path]
    result_list.extend(norm_dir_name_or_path(mapping[1]))
    result_list.append(norm_dir_name_or_path(app_name_or_path))
    if with_structure:
        result_list.extend(norm_dir_name_or_path(mapping[2]))
    
    result_path = os.path.normpath(os.path.join(*result_list))
    if ensure_dir:
        ensure_dir_exists(result_path)
    
    return result_path


@lru_cache(maxsize=len(AppDirectoryType) * 2 * 10, typed=True)
def app_dir_path_cached(dir_type: AppDirectoryType, app_name_or_path: DirNameOrPath, with_structure: bool = True, ensure_dir: bool = True):
    return app_dir_path(dir_type, app_name_or_path, with_structure, ensure_dir)


class AppDirPath(AppDirPathBase):
    def __init__(self, max_cache_size: Optional[int] = None) -> None:
        super().__init__(max_cache_size)
    
    def dir_type_mapping(self, dir_type: AppDirectoryType) -> DirTypeMappingItem:
        return dir_type_mapping[dir_type]
    
    def base_dir_id_to_path(self, base_dir_id: BaseDirID) -> str:
        return SHGetKnownFolderPath(base_dir_id)
