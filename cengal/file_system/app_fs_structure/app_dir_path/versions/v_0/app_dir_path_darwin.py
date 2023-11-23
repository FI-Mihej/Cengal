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


__all__ = ['AppDirPath']


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
# https://developer.apple.com/documentation/foundation/1414224-nssearchpathfordirectoriesindoma
# https://developer.apple.com/documentation/foundation/filemanager/searchpathdomainmask
# https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory


from cengal.file_system.directory_manager import ensure_dir as ensure_dir_exists
from .app_directory_types import AppDirectoryType
from .app_dir_path_base import AppDirPathBase, DirTypeMappingItem, DirTypeMappingItem, BaseDirID, DirNameOrPath, norm_dir_name_or_path
from typing import Optional, Tuple, Dict
from functools import lru_cache
from enum import Enum
from AppKit import NSSearchPathForDirectoriesInDomains


class FileManagerSearchPathDirectory(Enum):
    applicationDirectory = 1
    userDirectory = 7
    cachesDirectory = 13
    applicationSupportDirectory = 14
    allApplicationsDirectory = 100


class FileManagerSearchPathDomainMask(Enum):
    userDomainMask = 1
    localDomainMask = 4
    systemDomainMask = 8
    networkDomainMask = 16
    allDomainsMask = 65535


dir_type_mapping: Dict[AppDirectoryType, Tuple[Tuple[FileManagerSearchPathDomainMask, FileManagerSearchPathDirectory], Optional[DirNameOrPath], Optional[DirNameOrPath]]] = {
    AppDirectoryType.local_data: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, ('local_low', 'data')),
    AppDirectoryType.local_static_data: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, ('local_low', 'static_data')),
    AppDirectoryType.local_cache: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.cachesDirectory), None, ('local_low', 'cache')),
    AppDirectoryType.local_config: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, ('local_low', 'config')),
    AppDirectoryType.local_log: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, ('local_low', 'log')),
    AppDirectoryType.local_temp: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.cachesDirectory), None, ('local_low', 'temp')),
    AppDirectoryType.local_runtime: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, ('local_low', 'runtime')),

    AppDirectoryType.local_low_data: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, ('local_low', 'data')),
    AppDirectoryType.local_low_static_data: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, ('local_low', 'static_data')),
    AppDirectoryType.local_low_cache: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.cachesDirectory), None, ('local_low', 'cache')),
    AppDirectoryType.local_low_config: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, ('local_low', 'config')),
    AppDirectoryType.local_low_log: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, ('local_low', 'log')),
    AppDirectoryType.local_low_temp: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.cachesDirectory), None, ('local_low', 'temp')),
    AppDirectoryType.local_low_runtime: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, ('local_low', 'runtime')),

    AppDirectoryType.roaming_data: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, ('roaming', 'data')),
    AppDirectoryType.roaming_static_data: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, ('roaming', 'static_data')),
    AppDirectoryType.roaming_cache: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.cachesDirectory), None, ('roaming', 'cache')),
    AppDirectoryType.roaming_config: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, ('roaming', 'config')),
    AppDirectoryType.roaming_log: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, ('roaming', 'log')),
    AppDirectoryType.roaming_temp: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.cachesDirectory), None, ('roaming', 'temp')),
    AppDirectoryType.roaming_runtime: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, ('roaming', 'runtime')),

    AppDirectoryType.program_data: ((FileManagerSearchPathDomainMask.localDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, 'data'),
    AppDirectoryType.program_static_data: ((FileManagerSearchPathDomainMask.localDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, 'static_data'),
    AppDirectoryType.program_cache: ((FileManagerSearchPathDomainMask.localDomainMask, FileManagerSearchPathDirectory.cachesDirectory), None, None),
    AppDirectoryType.program_config: ((FileManagerSearchPathDomainMask.localDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, 'config'),
    AppDirectoryType.program_log: ((FileManagerSearchPathDomainMask.localDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, 'log'),
    AppDirectoryType.program_temp: ((FileManagerSearchPathDomainMask.localDomainMask, FileManagerSearchPathDirectory.cachesDirectory), None, 'temp'),
    AppDirectoryType.program_runtime: ((FileManagerSearchPathDomainMask.localDomainMask, FileManagerSearchPathDirectory.applicationSupportDirectory), None, 'runtime'),

    AppDirectoryType.program_files: ((FileManagerSearchPathDomainMask.localDomainMask, FileManagerSearchPathDirectory.allApplicationsDirectory), None, None),
    AppDirectoryType.program_files_common: ((FileManagerSearchPathDomainMask.localDomainMask, FileManagerSearchPathDirectory.allApplicationsDirectory), None, None),

    AppDirectoryType.user_profile_data: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.userDirectory), None, None),
    AppDirectoryType.user_profile_program_files: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.applicationDirectory), None, None),
    AppDirectoryType.user_profile_program_files_common: ((FileManagerSearchPathDomainMask.userDomainMask, FileManagerSearchPathDirectory.applicationDirectory), None, None),
}


class AppDirPath(AppDirPathBase):
    def __init__(self, max_cache_size: Optional[int] = None) -> None:
        super().__init__(max_cache_size)
    
    def dir_type_mapping(self, dir_type: AppDirectoryType) -> DirTypeMappingItem:
        return dir_type_mapping[dir_type]
    
    def base_dir_id_to_path(self, base_dir_id: BaseDirID) -> str:
        domain_mask, directory = base_dir_id
        result_path = NSSearchPathForDirectoriesInDomains(directory, domain_mask, True)[0]
        return result_path
