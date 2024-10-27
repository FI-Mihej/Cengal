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

from cengal.web_tools.request_cache import RequestCache
from cengal.introspection.inspect import frame

from inspect import getouterframes, currentframe
import os
from typing import Optional, List, Tuple, Union

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

    def _get_file_line(self, path, line_num) -> Optional[str]:
        line_num -= 1  # make line numbers start from 0 - not from 1
        default_answer = None
        if line_num < 0:
            return default_answer
        
        file_data = self._get_file_data(path)
        max_line = len(file_data) - 1
        if line_num > max_line:
            return default_answer

        return file_data[line_num]

    def get_file_line(self, path, line_num) -> Optional[str]:
        return self._get_file_line(path, line_num)

    def _get_file_lines(self, path, first_line_num: int, last_line_num: int) -> Optional[List[str]]:
        first_line_num -= 1  # make line numbers start from 0 - not from 1
        last_line_num -= 1  # make line numbers start from 0 - not from 1
        default_answer = None
        if (first_line_num < 0) or (last_line_num < 0):
            return default_answer
        
        file_data = self._get_file_data(path)
        max_line = len(file_data) - 1
        if (first_line_num > max_line) or (last_line_num > max_line):
            return default_answer

        if first_line_num > last_line_num:
            last_line_num_buff = last_line_num
            last_line_num = first_line_num
            first_line_num = last_line_num_buff
        
        last_line_num += 1
        return file_data[first_line_num:last_line_num]

    def get_file_lines(self, path, first_line_num: int, last_line_num: int, strip_empty_lines: bool = False) -> Optional[List[str]]:
        lines = self._get_file_lines(path, first_line_num, last_line_num)
        if strip_empty_lines and True:
            if lines:
                index = 0
                first_is_empty: bool = not lines[index]
                while first_is_empty:
                    index += 1
                    first_is_empty = not lines[index]
                
                lines = lines[index:]

            if lines:
                index = 0
                first_is_empty: bool = not lines[index]
                while first_is_empty:
                    index -= 1
                    first_is_empty = not lines[index]
                
                lines = lines[0: None if 0 == index else index]
        
        return '\n'.join(lines)
    
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
        
        frame, file_path, line_number, function_name, lines, index = self._frame_info(depth + 1)
        previous_line_num = line_number - 1
        lines = self._get_file_line(file_path, previous_line_num)
        filename = os.path.basename(file_path)
        result = (filename, file_path, function_name, previous_line_num, lines, index)
        return result

    def trace_self(self, depth: Optional[int] = 1):
        if not self.trace_allowed:
            result = (None, None, None, None, None)
            return result
        
        frame, file_path, line_number, function_name, lines, index = self._frame_info(depth + 1)
        current_line_num = line_number
        lines = self._get_file_line(file_path, current_line_num)
        filename = os.path.basename(file_path)
        result = (filename, file_path, function_name, current_line_num, lines, index)
        return result

    def trace_next(self, depth: Optional[int] = 1):
        if not self.trace_allowed:
            result = (None, None, None, None, None)
            return result
        
        frame, file_path, line_number, function_name, lines, index = self._frame_info(depth + 1)
        next_line_num = line_number + 1
        lines = self._get_file_line(file_path, next_line_num)
        filename = os.path.basename(file_path)
        result = (filename, file_path, function_name, next_line_num, lines, index)
        return result

    def trace_exact(self, line_num: Union[int, slice], strip_empty_lines: bool = False, depth: Optional[int] = 1):
        if not self.trace_allowed:
            result = (None, None, None, None, None)
            return result
        
        frame, file_path, line_number, function_name, lines, index = self._frame_info(depth + 1)
        if isinstance(line_num, int):
            exact_line_num = line_num
            lines = self._get_file_line(file_path, line_num)
            filename = os.path.basename(file_path)
            result = (filename, file_path, function_name, exact_line_num, lines, index)
            return result
        else:
            exact_line_num = min(line_num.start, line_num.stop)
            lines = self.get_file_lines(file_path, line_num.start, line_num.stop, strip_empty_lines)
            filename = os.path.basename(file_path)
            result = (filename, file_path, function_name, exact_line_num, lines, index)
            return result

    def trace_relative(self, line_num_offset: Union[int, slice], strip_empty_lines: bool = False, depth: Optional[int] = 1):
        if not self.trace_allowed:
            result = (None, None, None, None, None)
            return result
        
        frame, file_path, line_number, function_name, lines, index = self._frame_info(depth + 1)
        if isinstance(line_num_offset, int):
            exact_line_num = line_number + line_num_offset
            lines = self._get_file_line(file_path, exact_line_num)
            filename = os.path.basename(file_path)
            result = (filename, file_path, function_name, exact_line_num, lines, index)
            return result
        else:
            exact_line_num = line_number + min(line_num_offset.start, line_num_offset.stop)
            lines = self.get_file_lines(file_path, line_number + line_num_offset.start, line_number + line_num_offset.stop, strip_empty_lines)
            filename = os.path.basename(file_path)
            result = (filename, file_path, function_name, exact_line_num, lines, index)
            return result

    def __call__(self, print_full_file_name=None, depth: Optional[int] = 1):
        if not self.trace_allowed:
            return
        
        print_full_file_name = self.print_full_file_name if print_full_file_name is None else print_full_file_name
        filename, file_path, function_name, exact_line_num, lines, index = self.trace(depth=depth)
        if print_full_file_name:
            print(filename, file_path, function_name, exact_line_num, lines, index)
        else:
            print(filename, function_name, exact_line_num, lines, index)

    def n(self, name: str = '', print_full_file_name=None, depth: Optional[int] = 1):
        if not self.trace_allowed:
            return
        
        print_full_file_name = self.print_full_file_name if print_full_file_name is None else print_full_file_name
        filename, file_path, function_name, exact_line_num, lines, index = self.trace(depth=depth)
        if print_full_file_name:
            for_print = (filename, file_path, function_name, exact_line_num, lines, index)
        else:
            for_print = (filename, function_name, exact_line_num, lines, index)

        if name:
            print(f'<< {name} >>', *for_print)
        else:
            print(*for_print)


line_tracer = LineTracer()
line_tracer_full_file_name = LineTracer(print_full_file_name=True)


def previous_line_number(depth: Optional[int] = 1) -> int:
    return line_tracer.trace(depth + 1)[3]


def current_line_number(depth: Optional[int] = 1) -> int:
    return line_tracer.trace_self(depth + 1)[3]


def next_line_number(depth: Optional[int] = 1) -> int:
    return line_tracer.trace_next(depth + 1)[3]


pln = previous_line_number
cln = current_line_number
nln = next_line_number
