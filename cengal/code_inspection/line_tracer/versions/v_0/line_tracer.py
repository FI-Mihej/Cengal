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

from inspect import getouterframes, currentframe
from cengal.web_tools.request_cache import RequestCache
from typing import Optional
from cengal.introspection.inspect import frame
import os

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


class LineTracer:
    def __init__(self, print_full_file_name=False, trace_allowed=True):
        self.print_full_file_name = print_full_file_name
        self.trace_allowed = trace_allowed
        self._file_cache = RequestCache(999999)
        pass

    def _get_file_data(self, path):
        file_data = self._file_cache.try_to_get_data_for_request(path)
        if not file_data:
            with open(path) as file:
                file_data = file.readlines()
                file_data = [line.rstrip('\n') for line in file_data]
                self._file_cache.put_new_request(path, file_data)
        return file_data

    def _get_file_line(self, path, line_num):
        line_num -= 1  # make line numbers start from 0 - not from 1
        default_answer = None
        if line_num < 0:
            return default_answer
        
        file_data = self._get_file_data(path)
        max_line = len(file_data) - 1
        if line_num > max_line:
            return default_answer

        return file_data[line_num]
    
    def _frame_info(self, depth: Optional[int] = 1):
        fr = frame(depth + 1)
        filename = fr.f_code.co_filename
        line_number = fr.f_lineno
        function_name = fr.f_code.co_name
        lines = str()
        index = fr.f_code.co_firstlineno
        return fr, filename, line_number, function_name, lines, index

    def trace(self, depth: Optional[int] = 1):
        if not self.trace_allowed:
            result = (None, None, None, None, None)
            return result
        
        frame, filename, line_number, function_name, lines, index = self._frame_info(depth + 1)
        previous_line_num = line_number - 1
        lines = self._get_file_line(filename, previous_line_num)
        if not self.print_full_file_name:
            filename = os.path.basename(filename)
        
        result = (filename, function_name, previous_line_num, lines, index)
        return result

    def trace_next(self, depth: Optional[int] = 1):
        if not self.trace_allowed:
            result = (None, None, None, None, None)
            return result
        
        frame, filename, line_number, function_name, lines, index = self._frame_info(depth + 1)
        next_line_num = line_number + 1
        lines = self._get_file_line(filename, next_line_num)
        if not self.print_full_file_name:
            filename = os.path.basename(filename)
        
        result = (filename, function_name, next_line_num, lines, index)
        return result

    def __call__(self, depth: Optional[int] = 1):
        if not self.trace_allowed:
            return
        
        print(self.trace(depth=depth))

    def n(self, name: str = '', depth: Optional[int] = 1):
        if not self.trace_allowed:
            return
        
        if name:
            print(f'<< {name} >>', self.trace(depth=depth))
        else:
            print(self.trace(depth=depth))
