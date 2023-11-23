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
import os
if 'nt' == os.name:
    import win32console
    import codecs
    import ctypes
    FILE_ATTRIBUTE_HIDDEN = 0x02
    FILE_ATTRIBUTE_READONLY = 0x01
    REMOVABLE_ATTRIBUTES = ~(FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_READONLY)
    WIN_UNICODE_PATH_PREFIX = '\\\\?\\'
    WUPP = WIN_UNICODE_PATH_PREFIX
    INVALID_FILE_ATTRIBUTES = 0xFFFFFFFF
    FILE_ATTRIBUTE_REPARSE_POINT = 0x00400


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


_INSTALLING_BUFFER = {
    'islink': os.path.islink,
}


def islink(path):
    result = ctypes.windll.kernel32.GetFileAttributesW(path)
    if result == INVALID_FILE_ATTRIBUTES:
        raise ctypes.WinError()
    return bool(result & FILE_ATTRIBUTE_REPARSE_POINT)


def install_module():
    os.path.islink = islink


def uninstall_module():
    os.path.islink = _INSTALLING_BUFFER['islink']
