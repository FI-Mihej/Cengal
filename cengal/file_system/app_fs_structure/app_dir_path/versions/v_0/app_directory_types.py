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


__all__ = ['AppDirectoryType']


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


from enum import IntEnum


class AppDirectoryType(IntEnum):
    local_data = 0  # local data is data that is not shared between users
    local_low_data = 1  # local data is data that is not shared between users. This folder is intended to be used by applications that require a low privilege level to operate, such as web browsers or sandboxed applications.
    roaming_data = 2  # roaming data is data that is not shared between users but might be shared and synchronised between devices of this user. On Mac OS X, automatic system backup for a small (few kbytes) files is used
    
    local_cache = 3  # Where user-specific non-essential (cached) data should be written
    local_low_cache = 4  # Where user-specific non-essential (cached) data should be written
    roaming_cache = 5  # Where user-specific non-essential (cached) data should be written. Might be shared and synchronised between devices of this user
    
    local_temp = 6
    local_low_temp = 7
    roaming_temp = 8
    
    local_log = 9
    local_low_log = 10
    roaming_log = 11
    
    local_config = 12
    local_low_config = 13
    roaming_config = 14
    
    local_runtime = 15  # Used for non-essential, user-specific data files such as sockets, named pipes, etc.
    local_low_runtime = 16  # Used for non-essential, user-specific data files such as sockets, named pipes, etc.
    roaming_runtime = 17  # Used for non-essential, user-specific data files such as sockets, named pipes, etc. Might be shared and synchronised between devices of this user

    program_files = 18  # program files is program static data that is shared between users
    program_files_common = 19  # program files common is program static data that is shared between applications and users. For example libraries 

    program_data = 20  # program data is non-static data that is shared between users
    program_cache = 21  # Where non-essential (cached) data should be written
    program_temp = 22
    program_log = 23
    program_config = 24
    program_runtime = 25  # Used for non-essential, data files such as sockets, named pipes, etc.

    user_profile_data = 28  # App data in user home directory. It is usually hidden directory
    user_profile_program_files = 29  # program files is program static data that is shared between users
    user_profile_program_files_common = 30  # program files common is program static data that is shared between applications and users. For example libraries 

    local_static_data = 31
    local_low_static_data = 32
    roaming_static_data = 33
    program_static_data = 34
