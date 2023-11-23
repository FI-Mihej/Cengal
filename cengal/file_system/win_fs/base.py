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

import ctypes
import ctypes.wintypes as wintypes
from cengal.code_flow_control.chained_flow.versions.v_1.chained_flow import chain_reader, ChainInternalResult, \
    ResultExistence

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


LPDWORD = ctypes.POINTER(wintypes.DWORD)
LPOVERLAPPED = wintypes.LPVOID
LPSECURITY_ATTRIBUTES = wintypes.LPVOID

GENERIC_READ = 0x80000000
GENERIC_WRITE = 0x40000000
GENERIC_EXECUTE = 0x20000000
GENERIC_ALL = 0x10000000

FILE_SHARE_DELETE = 0x00000004
FILE_SHARE_READ = 0x00000001
FILE_SHARE_WRITE = 0x00000002

CREATE_NEW = 1
CREATE_ALWAYS = 2
OPEN_EXISTING = 3
OPEN_ALWAYS = 4
TRUNCATE_EXISTING = 5

FILE_ATTRIBUTE_NORMAL = 0x00000080

INVALID_HANDLE_VALUE = -1
INVALID_HANDLE_VALUE_CTYPES = wintypes.HANDLE(INVALID_HANDLE_VALUE).value

NULL = 0
FALSE = wintypes.BOOL(0)
TRUE = wintypes.BOOL(1)

WIN_UNICODE_PATH_PREFIX = '\\\\?\\'
WUPP = WIN_UNICODE_PATH_PREFIX


def judge(ok_status, result):
    if ok_status:
        return ResultExistence(False, None)
    else:
        return ResultExistence(True, ctypes.WinError())


def verdict_exceptions_consolidator(context, block_results_criteria=None, close=False):
    with chain_reader(context, block_results_criteria, close):
        if not context:
            bad_blocks = context.get_bad_blocks()
            root_exception = None
            last_exception = None
            for block in reversed(bad_blocks):
                block_result = block[3][1]
                if type(block_result) != ChainInternalResult:
                    win_error = block_result[1].result
                    if root_exception is None:
                        root_exception = last_exception = win_error
                    else:
                        last_exception.__context__ = win_error
                        last_exception = win_error
            if root_exception is not None:
                raise root_exception
            else:
                context.raise_bad_blocks()
