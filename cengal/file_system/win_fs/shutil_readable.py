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

from .base import *
import ctypes
import ctypes.wintypes as wintypes
from ctypes import windll
import shutil
from cengal.code_flow_control.chained_flow.versions.v_1.chained_flow import ResultType, Chain, \
    ChainValRunner, CriteriaType, chain_reader, \
    ChainInternalResult, ResultExistence

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
    'copy': shutil.copy,
    'copy2': shutil.copy2,
}


def copy(src_name, dst_name):
    cont = Chain('copy2', None, ResultType(CriteriaType.optional, set()))
    c_ret = ChainValRunner(cont, lambda result: result != 0, judge)
    c_handle = ChainValRunner(cont, lambda result: result.value != INVALID_HANDLE_VALUE_CTYPES, judge)

    c_ret()(ctypes.windll.kernel32.CopyFileW(src_name, dst_name, False))
    c_ret()(ctypes.windll.kernel32.SetFileAttributesW(dst_name, FILE_ATTRIBUTE_NORMAL))
    destination_file_handle = c_handle('open Destination file')(
        create_file(dst_name, GENERIC_WRITE, FILE_SHARE_WRITE, NULL, OPEN_EXISTING, 0, NULL))
    try:
        creation_time = ctypes.wintypes.FILETIME()
        last_access_time = ctypes.wintypes.FILETIME()
        last_write_time = ctypes.wintypes.FILETIME()
        c_ret()(ctypes.windll.kernel32.SetFileTime(destination_file_handle,
                                                 ctypes.byref(creation_time),
                                                 ctypes.byref(last_access_time),
                                                 ctypes.byref(last_write_time)))
    except:
        raise
    finally:
        c_ret(block_results_criteria=ResultType(CriteriaType.needed, {'open Destination file'}))(
            ctypes.windll.kernel32.CloseHandle(destination_file_handle))

    verdict_exceptions_consolidator(cont, close=True)


def copy2(src_name, dst_name):
    ret = ctypes.windll.kernel32.CopyFileW(src_name, dst_name, False)
    if not ret:
        raise ctypes.WinError()


def create_file(filename, access, mode, security_attributes, creation, flags, template_file_handle):
    """See: CreateFile function
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa363858(v=vs.85).aspx
    """
    create_file_spec = windll.kernel32.CreateFileW
    create_file_spec.argtypes = [
        wintypes.LPWSTR,  # _In_ - LPCTSTR lpFileName
        wintypes.DWORD,  # _In_ - DWORD dwDesiredAccess
        wintypes.DWORD,  # _In_ - DWORD dwShareMode
        LPSECURITY_ATTRIBUTES,  # _In_opt_ - LPSECURITY_ATTRIBUTES lpSecurityAttributes
        wintypes.DWORD,  # _In_ - DWORD dwCreationDisposition
        wintypes.DWORD,  # _In_ - DWORD dwFlagsAndAttributes
        wintypes.HANDLE]  # _In_opt_ - HANDLE hTemplateFile
    create_file_spec.restype = wintypes.HANDLE

    return wintypes.HANDLE(create_file_spec(filename,
                                         access,
                                         mode,
                                         security_attributes,
                                         creation,
                                         flags,
                                         template_file_handle))


def install_module():
    shutil.copy = copy
    shutil.copy2 = copy2


def uninstall_module():
    shutil.copy = _INSTALLING_BUFFER['copy']
    shutil.copy2 = _INSTALLING_BUFFER['copy2']
