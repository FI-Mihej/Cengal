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


__all__ = [
    'flush_mmap', 
    'find_in_mmap', 
    'find_in_mmap_within_boundaries', 
]


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


import sys
from mmap import mmap, PAGESIZE
from typing import Optional


IS_MSWINDOWS = (sys.platform == "win32")


# class SmartMap:
#     def __init__(self):
#         self.pagesize = mmap.PAGESIZE
#         self.is_mswindows = ('Windows' == OS_TYPE)
#         pass

#     def flush(self):
#         pass

#     def generate_temp_file_name(self)->str:
#         pass


def flush_mmap(mmap_obj: mmap, offset, size):
    """ Note:
            If you want to create a memory-mapping for a writable, buffered file, you should flush() 
            the file first. This is necessary to ensure that local modifications to the buffers are 
            actually available to the mapping.
            (https://docs.python.org/3/library/mmap.html)

    Args:
        mmap_obj (mmap): _description_
        offset (_type_): _description_
        size (_type_): _description_
    """    
    if IS_MSWINDOWS:
        mmap_obj.flush(offset, size)
    else:
        n_x_pagesize = PAGESIZE * (offset // PAGESIZE)
        bytes_delta = offset - n_x_pagesize
        result_offset = n_x_pagesize
        result_size = size + bytes_delta
        mmap_obj.flush(result_offset, result_size)


def find_in_mmap(mmap_obj: mmap, request: bytes, search_offset, mmap_size=None):
    mmap_size = mmap_obj.size() if mmap_size is None else mmap_size
    if (mmap_size - 1 - search_offset) >= len(request):
        return mmap_obj.find(request, search_offset)
    else:
        return -1


def find_in_mmap_within_boundaries(mmap_obj: mmap, request: bytes, search_relative_offset: int = 0, start_offset: int = 0, stop_offset: int = -1, 
                                   mmap_size: Optional[int] = None, request_len: Optional[int] = None):
    request_len = len(request) if request_len is None else request_len
    mmap_size = mmap_obj.size() if mmap_size is None else mmap_size
    offset_after_end = (mmap_size + 1 + stop_offset) if stop_offset < 0 else (stop_offset + 1)
    if search_relative_offset < 0:
        search_relative_offset = 0
    
    if start_offset < 0:
        start_offset = 0
    
    search_start = start_offset + search_relative_offset

    if search_start + request_len <= offset_after_end:
        return mmap_obj.find(request, search_start)
    else:
        return -1
