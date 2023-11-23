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

from cengal.code_inspection.line_tracer import LineTracer
from cengal.data_generation.id_generator import IDGenerator
from cengal.introspection.inspect import intro_func_repr, intro_func_repr_limited
from enum import Enum
from typing import Callable, Optional, Any

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


class CodeStartReplType(Enum):
    general = 0
    general_verbose = 1
    limited = 2
    limited_verbose = 3


class AutoLineTracer:
    def __init__(self, code_start_repl_type: CodeStartReplType, print_allowed: bool = True, *args, **kwargs):
        self.code_start_repl_type: CodeStartReplType = code_start_repl_type
        self.print_allowed: bool = print_allowed
        if CodeStartReplType.general == code_start_repl_type:
            self.code_start_repl = self._start_impl_general
        elif CodeStartReplType.general_verbose == code_start_repl_type:
            self.code_start_repl = self._start_impl_general_verbose
        elif CodeStartReplType.limited == code_start_repl_type:
            self.code_start_repl = self._start_impl_limited
        elif CodeStartReplType.limited_verbose == code_start_repl_type:
            self.code_start_repl = self._start_impl_limited_verbose
        
        self.lt: LineTracer = LineTracer(*args, **kwargs)
        self._index: IDGenerator = IDGenerator()
        self.line_template: str = '#{index:<4n}| <[{name}]> | <file \'{file_name}\' line {line}>.{func_name}()\n\t| {code_line}'
        self.line_template_name_less: str = '#{index:<4n}| <file \'{file_name}\' line {line}>.{func_name}()\n\t| {code_line}'
        # self.start_template: str = '#{index:<4n}| <+[{name}]+>'
        self.start_template: str = '#{index:<4n}| <+[{short_name}]+>\n\t|<+[{name}]+>'
        self.end_template: str = '#{index:<4n}| <-[{short_name}]->\n\t|<-[{name}]->'

        self.s = self.start
        self.e = self.end
        self.p = self.previous_line
        self.n = self.next_line

        self.ps = self.print_start
        self.pe = self.print_end
        self.pp = self.print_previous_line
        self.pn = self.print_next_line
    
    @property
    def index(self):
        return self._index()

    def _start_impl_general(self, depth: int = 1):
        return intro_func_repr(False, depth + 1)

    def _start_impl_general_verbose(self, depth: int = 1):
        return intro_func_repr(True, depth + 1)

    def _start_impl_limited(self, depth: int = 1):
        return intro_func_repr_limited(False, depth + 1)

    def _start_impl_limited_verbose(self, depth: int = 1):
        return intro_func_repr_limited(True, depth + 1)
    
    def start(self, depth: int = 1):
        short_name = self._start_impl_limited(depth + 1)
        name = self.code_start_repl(depth + 1)
        return self.start_template.format(index=self.index, short_name=short_name, name=name)

    def print_start(self, depth: int = 1):
        if self.print_allowed:
            print(self.start(depth + 1))

    def end(self, depth: int = 1):
        short_name = self._start_impl_limited(depth + 1)
        name = self.code_start_repl(depth + 1)
        return self.end_template.format(index=self.index, short_name=short_name, name=name)

    def print_end(self, depth: int = 1):
        if self.print_allowed:
            print(self.end(depth + 1))

    def previous_line(self, name: Optional[str] = None, depth: int = 1):
        filename, function_name, line_number, lines, index = self.lt.trace(depth + 1)
        lines = lines.strip()
        if name is None:
            return self.line_template_name_less.format(index=self.index, file_name=filename, line=line_number, func_name=function_name, code_line=lines)
        else:
            return self.line_template.format(index=self.index, name=name, file_name=filename, line=line_number, func_name=function_name, code_line=lines)

    def print_previous_line(self, name: Optional[str] = None, depth: int = 1):
        if self.print_allowed:
            print(self.previous_line(name, depth + 1))
    
    def next_line(self, name: Optional[str] = None, depth: int = 1):
        filename, function_name, line_number, lines, index = self.lt.trace_next(depth + 1)
        lines = lines.strip()
        if name is None:
            return self.line_template_name_less.format(index=self.index, file_name=filename, line=line_number, func_name=function_name, code_line=lines)
        else:
            return self.line_template.format(index=self.index, name=name, file_name=filename, line=line_number, func_name=function_name, code_line=lines)

    def print_next_line(self, name: Optional[str] = None, depth: int = 1):
        if self.print_allowed:
            print(self.next_line(name, depth + 1))
    
    def __call__(self, depth: int = 1):
        _, _, prev_line_number, prev_lines, _ = self.lt.trace(depth + 1)
        filename, function_name, next_line_number, next_lines, _ = self.lt.trace_next(depth + 1)
        return filename, function_name, prev_line_number, next_line_number, prev_lines, next_lines
