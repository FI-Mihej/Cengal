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


__all__ = ['SHGetKnownFolderPathError', 'SHGetKnownFolderPath']


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""


import os
from ctypes import POINTER, byref, c_wchar_p
from cengal.ctypes_tools.types import GUID
from cengal.ctypes_tools.constants import KnownfolderidConstants, S_OK
from cengal.ctypes_tools.function_prototypes import SHGetKnownFolderPath as proto_SHGetKnownFolderPath, CoTaskMemFree
from .result_api_exceptions import CtypesToolsResultAPIError
from cengal.file_system.directory_manager import ensure_dir as ensure_dir_exists
from typing import Union, Sequence, Any


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


class CtypesToolsWinResultAPIError(CtypesToolsResultAPIError):
    pass


class SHGetKnownFolderPathError(CtypesToolsWinResultAPIError):
    pass


def SHGetKnownFolderPath(dir_guid: GUID):
    """Example:

        from cengal.ctypes_tools.constants import KnownfolderidConstants
        dir_path: str = SHGetKnownFolderPath(KnownfolderidConstants.FOLDERID_LocalAppData)

    Args:
        dir_guid (GUID): One of KnownfolderidConstants constants. `from cengal.ctypes_tools.constants import KnownfolderidConstants`

    Raises:
        SHGetKnownFolderPathError: _description_

    Returns:
        _type_: _description_
    """
    result_path = None
    path_ptr = POINTER(c_wchar_p)()
    try:
        result = proto_SHGetKnownFolderPath(byref(dir_guid), 0, None, byref(path_ptr))
        if result != S_OK:
            raise SHGetKnownFolderPathError(result)
        
        result_path = path_ptr.value
    finally:
        CoTaskMemFree(path_ptr)
    
    return result_path
