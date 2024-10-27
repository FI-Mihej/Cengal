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
    'CodeStartReplType', 
    'LineType', 
    'OutputFields', 
    'AutoLineTracer', 
    'auto_line_tracer', 
    'alt', 

    'trace_result', 
    'tr', 
    'fake_trace_result', 
    'ftr', 

    'trace_line', 
    'tl', 
    'fake_trace_line', 
    'ftl', 

    'trace', 
    't', 
    'fake_trace', 
    'ft', 

    'trace_start', 
    'ts', 
    'fake_trace_start', 
    'fts', 

    'trace_end', 
    'te', 
    'fake_trace_end', 
    'fte', 
]

from cengal.code_inspection.line_tracer import LineTracer
from cengal.data_generation.id_generator import IDGenerator
from cengal.introspection.inspect import intro_func_repr, intro_func_repr_limited, get_multistr_of_data_value, cen, entity_repr_owner_based
from cengal.code_flow_control.python_bytecode_manipulator import CodeParamNames, code_param_names, has_code, get_code, code_name
from cengal.text_processing.optional_formatter import OptionalFormatterHandy, IT, IT0, IT1
from cengal.code_flow_control.args_manager import AK
from cengal.system import PVI
from cengal.time_management.cpu_clock import cpu_clock, cpu_clock_cycles

try:
    import rich
    RICH_PRESENT = True
except ImportError:
    RICH_PRESENT = False

import os
from threading import current_thread, Thread
from multiprocessing import current_process, Process
from datetime import datetime
from time import perf_counter
from enum import Enum, IntEnum
from contextlib import ContextDecorator
from functools import wraps
from typing import Callable, Optional, Any, Set, Tuple, Dict, List, Union

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


class CodeStartReplType(IntEnum):
    general = 0
    general_verbose = 1
    limited = 2
    limited_verbose = 3


class LineType(IntEnum):
    previous_line = 0
    current_line = 1
    next_line = 2
    exact_line = 3
    relative_line = 4


class OutputFields(IntEnum):
    header = 0
    trace_index = 1
    trace_name = 2
    code_start_wrapper = 3
    code_start = 4
    code_end_wrapper = 5
    code_end = 6
    new_line_before_time = 7
    date_time = 8
    perf_counter = 9
    cpu_clock = 10
    cpu_clock_cycles = 11
    new_line_before_process = 12
    process_name = 13
    process_pid = 14
    process_is_deamon = 15
    thread_name = 16
    thread_tid = 17
    thread_ident = 18
    thread_is_deamon = 19
    new_line_before_file_line_func = 20
    delimiter_before_file_line_func = 21
    file_name_line_func_name = 22
    file_path_line_func_name = 23
    blank_delim_line = 24
    code_line = 25
    blank_code_line = 26
    result_type_title = 27
    result_type = 28
    result_type_data = 29
    result_title = 30
    result = 31
    result_pp = 32
    result_data = 33
    new_line_after_end = 34
    rich_blank_line_after_end = 35


class AutoLineTracerCodeStart:
    def __init__(self, auto_line_tracer: 'AutoLineTracer', code_start_repl_type: CodeStartReplType):
        self.auto_line_tracer: 'AutoLineTracer' = auto_line_tracer
        self.code_start_repl_type: CodeStartReplType = code_start_repl_type
        self.code_start_repl_type_buff: CodeStartReplType = None
    
    def __enter__(self):
        self.code_start_repl_type_buff = self.auto_line_tracer.code_start_repl
        self.auto_line_tracer.code_start_repl = self.code_start_repl_type
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.auto_line_tracer.code_start_repl = self.code_start_repl_type_buff


class AutoLineTracerPrint:
    def __init__(self, auto_line_tracer: 'AutoLineTracer', print_enabled: bool):
        self.auto_line_tracer: 'AutoLineTracer' = auto_line_tracer
        self.print_enabled: bool = print_enabled
        self.print_enabled_buff: bool = None
    
    def __enter__(self):
        self.print_enabled_buff = self.auto_line_tracer.print_allowed
        self.auto_line_tracer.print_allowed = self.print_enabled
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.auto_line_tracer.print_allowed = self.print_enabled_buff


class AutoLineTracerRich:
    def __init__(self, auto_line_tracer: 'AutoLineTracer', rich_enabled: bool):
        self.auto_line_tracer: 'AutoLineTracer' = auto_line_tracer
        self.rich_enabled: bool = rich_enabled
        self.rich_enabled_buff: bool = None
    
    def __enter__(self):
        self.rich_enabled_buff = self.auto_line_tracer.rich_allowed
        self.auto_line_tracer.rich_allowed = self.rich_enabled
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.auto_line_tracer.rich_allowed = self.rich_enabled_buff


class AutoLineTracerOutputFields:
    def __init__(self, auto_line_tracer: 'AutoLineTracer', output_fields: Union[Set[OutputFields], Callable[[Set[OutputFields]], Set[OutputFields]]]):
        self.auto_line_tracer: 'AutoLineTracer' = auto_line_tracer
        self.output_fields: Union[Set[OutputFields], Callable[[Set[OutputFields]], Set[OutputFields]]] = output_fields
        self.output_fields_buff: Set[OutputFields] = None
    
    def __enter__(self):
        self.output_fields_buff = self.auto_line_tracer.output_fields
        if callable(self.output_fields):
            self.auto_line_tracer.output_fields = self.output_fields(self.auto_line_tracer.output_fields)
        else:
            self.auto_line_tracer.output_fields = set(self.output_fields)
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.auto_line_tracer.output_fields = self.output_fields_buff


class AutoLineTracerStartEndDecorator(ContextDecorator):
    def __init__(self, auto_line_tracer: 'AutoLineTracer', name: Optional[str] = None, depth: int = 1) -> None:
        self.auto_line_tracer: 'AutoLineTracer' = auto_line_tracer
        self.name: Optional[str] = name
        self.depth: int = depth
        self.wrapper: bool = None
        self.func: Callable = None
        self.line_trace: Tuple = None
        self.wrapper_args = None
        self.wrapper_kwargs = None
        self.wrapper_result = None
        super().__init__()
    
    def __call__(self, func):
        self.wrapper = True
        self.func = func
        code = get_code(func)
        file_path = code.co_filename
        filename = os.path.basename(file_path)
        function_name = code_name(code)
        line_number = code.co_firstlineno
        lines = self.auto_line_tracer.lt.get_file_line(file_path, line_number)
        index = 0
        self.line_trace = filename, file_path, function_name, line_number, lines, index
        @wraps(func)
        def inner(*args, **kwds):
            self.wrapper_args = args
            self.wrapper_kwargs = kwds
            with self._recreate_cm():
                self.wrapper_result = func(*args, **kwds)
                return self.wrapper_result
        
        return inner
    
    def __enter__(self):
        if self.func is not None:
            if self.name is None:
                name = f'{entity_repr_owner_based(self.func, False)}'
            else:
                name = f'{self.name} | {entity_repr_owner_based(self.func, False)}'

            if self.wrapper_args:
                name += f' | args={self.wrapper_args}'

            if self.wrapper_kwargs:
                name += f' | kwds={self.wrapper_kwargs}'
        else:
            name = self.name
        
        self.auto_line_tracer.ps(name, line_trace=self.line_trace, depth=self.depth + 1, wrapper=self.wrapper)
        return self

    def __exit__(self, *exc):
        if self.func is not None:
            if self.name is None:
                name = f'{entity_repr_owner_based(self.func, False)}'
            else:
                name = f'{self.name} | {entity_repr_owner_based(self.func, False)}'

            if self.wrapper_args:
                name += f' | args={self.wrapper_args}'

            if self.wrapper_kwargs:
                name += f' | kwds={self.wrapper_kwargs}'

            name += f' | result={self.wrapper_result}'
        else:
            name = self.name
        
        self.auto_line_tracer.pe(name, line_trace=self.line_trace, depth=self.depth + 1, wrapper=self.wrapper)
        return False


class AutoLineTracer:
    def __init__(self, code_start_repl_type: CodeStartReplType = CodeStartReplType.general, print_allowed: bool = True, rich_allowed: bool = True, 
                 output_fields: Optional[Set[OutputFields]] = None, 
                 line_optional_formatter: Optional[OptionalFormatterHandy] = None,
                 line_optional_formatter_rich_0: Optional[OptionalFormatterHandy] = None,
                 line_optional_formatter_rich_1: Optional[OptionalFormatterHandy] = None,
                 *args, **kwargs):
        self.code_start_repl_type: CodeStartReplType = code_start_repl_type
        self.print_allowed: bool = print_allowed
        self.rich_allowed: bool = rich_allowed
        self._code_start_repl: CodeStartReplType = None
        self.code_start_repl = code_start_repl_type
        self.lt: LineTracer = LineTracer(*args, **kwargs)
        self._index: IDGenerator = IDGenerator()
        self.line_optional_formatter: OptionalFormatterHandy = OptionalFormatterHandy(
            *[value.name for value in OutputFields], 
            header=IT0('_'*70),
            trace_index=IT1('\n', '#{:<7n}'),
            trace_name=IT1(' | ', '<[ {} ]>', r_delimiter='\n\t'),
            code_start_wrapper=IT1(' | ', '+++ START{}'),
            code_start=IT1(' | ', '+++ START={name}() : {info} '),
            code_end_wrapper=IT1(' | ', '--- END{}'),
            code_end=IT1(' | ', '--- END={name}() : {info} '),
            new_line_before_time=IT1('\n\t'),
            date_time=IT1(' | ', 'DT={}'),
            perf_counter=IT1(' | ', 'PC={}'),
            cpu_clock=IT1(' | ', 'CC={}'),
            cpu_clock_cycles=IT1(' | ', 'CCC={}'),
            new_line_before_process=IT1('\n\t'),
            process_pid=IT1(' | ', 'PID={}'),
            process_name=IT1(' | ', 'PNAME={}'),
            process_is_deamon=IT1(' | ', 'PisD={}'),
            thread_tid=IT1(' | ', 'TID={}'),
            thread_ident=IT1(' | ', 'TIDENT={}'),
            thread_name=IT1(' | ', 'TNAME={}'),
            thread_is_deamon=IT1(' | ', 'TisD={}'),
            new_line_before_file_line_func=IT1('\n\t | '),
            delimiter_before_file_line_func=IT1(' | '),
            file_name_line_func_name=IT0('<file \'{file_name}\' line {line}>.{func_name}()'),
            file_path_line_func_name=IT1('\n\t | ', 'File "{file_path}", line {line}, in {func_name}'),
            code_line=IT1('\n\t | '),
            blank_code_line=IT(),
            blank_delim_line=IT(),
            result_type=IT1('\n\t\t | ', 'ResultType= {}'),
            result_type_title=IT1('\n\t\t | ', 'ResultType={}'),
            result_type_data=IT(),
            result=IT1('\n\t\t | ', 'Result= {}'),
            result_pp=IT1('\n\t\t | ', 'Result= {}'),
            result_title=IT1('\n\t\t | ', 'Result={}'),
            result_data=IT(),
            new_line_after_end=IT1('\n'),
            rich_blank_line_after_end=IT1(''),
            ) if line_optional_formatter is None else line_optional_formatter
        self.line_optional_formatter_rich_0: OptionalFormatterHandy = OptionalFormatterHandy(
            *[value.name for value in OutputFields], 
            header=IT0('_'*70 + '{}'),
            trace_index=IT1('\n', '#{:<7n}'),
            trace_name=IT1(' | ', '<[ {} ]>', r_delimiter='\n\t'),
            code_start_wrapper=IT1(' | ', '+++ START{}'),
            code_start=IT1(' | ', '+++ START={name}() : {info} '),
            code_end_wrapper=IT1(' | ', '--- END{}'),
            code_end=IT1(' | ', '--- END={name}() : {info} '),
            new_line_before_time=IT1('\n\t'),
            date_time=IT1(' | ', 'DT={}'),
            perf_counter=IT1(' | ', 'PC={}'),
            cpu_clock=IT1(' | ', 'CC={}'),
            cpu_clock_cycles=IT1(' | ', 'CCC={}'),
            new_line_before_process=IT1('\n\t'),
            process_pid=IT1(' | ', 'PID={}'),
            process_name=IT1(' | ', 'PNAME={}'),
            process_is_deamon=IT1(' | ', 'PisD={}'),
            thread_tid=IT1(' | ', 'TID={}'),
            thread_ident=IT1(' | ', 'TIDENT={}'),
            thread_name=IT1(' | ', 'TNAME={}'),
            thread_is_deamon=IT1(' | ', 'TisD={}'),
            new_line_before_file_line_func=IT1('\n\t | '),
            delimiter_before_file_line_func=IT1(' | '),
            file_name_line_func_name=IT0('<file \'{file_name}\' line {line}>.{func_name}()'),
            file_path_line_func_name=IT1('\n\t | ', 'File "{file_path}", line {line}, in {func_name}'),
            blank_code_line=IT(),
            blank_delim_line=IT(),
            ) if line_optional_formatter_rich_0 is None else line_optional_formatter_rich_0
        self.line_optional_formatter_rich_1: OptionalFormatterHandy = OptionalFormatterHandy(
            *[value.name for value in OutputFields], 
            blank_code_line=IT(),
            blank_delim_line=IT(),
            result_type=IT1('\n\t\t | ', 'ResultType= {}'),
            result_type_title=IT1('\n\t\t | ', 'ResultType={}'),
            result_type_data=IT0(None),
            result=IT1('\n\t\t | ', 'Result= {}'),
            result_pp=IT1('\n\t\t | ', 'Result= {}'),
            result_title=IT1('\n\t\t | ', 'Result={}'),
            result_data=IT0(None),
            new_line_after_end=IT1('\n'),
            rich_blank_line_after_end=IT1(''),
            ) if line_optional_formatter_rich_1 is None else line_optional_formatter_rich_1
        # self.start_template: str = '#{index:<7n}| <+[{name}]+>'
        # self.start_template: str = '#{index:<7n}| <+[{short_name}]+>\n\t |<+[{name}]+>'
        # self.end_template: str = '#{index:<7n}| <-[{short_name}]->\n\t |<-[{name}]->'
        # self.start_template: str = ' +++ START={name}() : {info} '
        # self.end_template: str = ' --- END={name}() : {info} '
        self.additional_lines_prefix: str = '\t | '

        self.default_output_fields: Set[OutputFields] = {
                OutputFields.header, 
                OutputFields.trace_index, 
                OutputFields.trace_name, 
                OutputFields.date_time,
                OutputFields.cpu_clock_cycles,
                OutputFields.new_line_before_process,
                OutputFields.process_name,
                OutputFields.thread_name,
                # OutputFields.delimiter_before_file_line_func,
                OutputFields.new_line_before_file_line_func,
                OutputFields.file_name_line_func_name,
                OutputFields.file_path_line_func_name,
                OutputFields.code_line,
                OutputFields.result_type,
                OutputFields.result_pp,
                OutputFields.new_line_after_end,
            }

        self.output_fields: Set[OutputFields] = self.default_output_fields if output_fields is None else output_fields

        self.rich_output_fields_0: Set[OutputFields] = set()
        self.rich_output_fields_1: Set[OutputFields] = set()
        code_line_field_found: bool = False
        for field in OutputFields:
            if OutputFields.code_line == field:
                code_line_field_found = True
                continue

            if code_line_field_found:
                self.rich_output_fields_1.add(field)
            else:
                self.rich_output_fields_0.add(field)

        self.s = self.start
        self.ps = self.print_start

        self.e = self.end
        self.pe = self.print_end

        self.ls = self.line_str
        self.pls = self.previous_line_str
        self.nls = self.next_line_str
        self.els = self.exact_line_str
        self.rls = self.relative_line_str

        self.lrs = self.line_result_str
        self.plrs = self.previous_line_result_str
        self.nlrs = self.next_line_result_str
        self.elrs = self.exact_line_result_str
        self.rlrs = self.relative_line_result_str

        self.lrsf = self.line_result_str_fast
        self.plrsf = self.previous_line_result_str_fast
        self.nlrsf = self.next_line_result_str_fast
        self.elrsf = self.exact_line_result_str_fast
        self.rlrsf = self.relative_line_result_str_fast

        self.pl = self.print_line
        self.ppl = self.print_previous_line
        self.pnl = self.print_next_line
        self.pel = self.print_exact_line
        self.prl = self.print_relative_line

        self.plr = self.print_line_result
        self.pplr = self.print_previous_line_result
        self.pnlr = self.print_next_line_result
        self.pelr = self.print_exact_line_result
        self.prlr = self.print_relative_line_result

        self.plrf = self.print_line_result_fast
        self.pplrf = self.print_previous_line_result_fast
        self.pnlrf = self.print_next_line_result_fast
        self.pelrf = self.print_exact_line_result_fast
        self.prlrf = self.print_relative_line_result_fast
    
    @property
    def index(self):
        return self._index()
    
    @property
    def code_start_repl(self) -> CodeStartReplType:
        return self._code_start_repl
    
    @code_start_repl.setter
    def code_start_repl(self, code_start_repl_type: CodeStartReplType):
        if CodeStartReplType.general == code_start_repl_type:
            self._code_start_repl = self._start_impl_general
        elif CodeStartReplType.general_verbose == code_start_repl_type:
            self._code_start_repl = self._start_impl_general_verbose
        elif CodeStartReplType.limited == code_start_repl_type:
            self._code_start_repl = self._start_impl_limited
        elif CodeStartReplType.limited_verbose == code_start_repl_type:
            self._code_start_repl = self._start_impl_limited_verbose
    
    def different_code_start_repl(self, code_start_repl_type: CodeStartReplType) -> AutoLineTracerCodeStart:
        return AutoLineTracerCodeStart(self, code_start_repl_type)
    
    def different_output_fields(self, output_fields: Union[Set[OutputFields], Callable[[Set[OutputFields]], Set[OutputFields]]]) -> AutoLineTracerOutputFields:
        return AutoLineTracerOutputFields(self, output_fields)
    
    def different_print_setting(self, print_enabled: bool) -> AutoLineTracerPrint:
        return AutoLineTracerPrint(self, print_enabled)
    
    def different_rich_setting(self, rich_enabled: bool) -> AutoLineTracerRich:
        return AutoLineTracerRich(self, rich_enabled)
    
    def start_end(self, name: Optional[str] = None) -> AutoLineTracerStartEndDecorator:
        return AutoLineTracerStartEndDecorator(self, name)

    def _start_impl_general(self, depth: int = 1):
        return intro_func_repr(False, depth + 1)

    def _start_impl_general_verbose(self, depth: int = 1):
        return intro_func_repr(True, depth + 1)

    def _start_impl_limited(self, depth: int = 1):
        return intro_func_repr_limited(False, depth + 1)

    def _start_impl_limited_verbose(self, depth: int = 1):
        return intro_func_repr_limited(True, depth + 1)
    
    # def start(self, depth: int = 1):
    #     short_name = self._start_impl_limited(depth + 1)
    #     name = self._code_start_repl(depth + 1)
    #     return self.start_template.format(index=self.index, short_name=short_name, name=name)

    def start(self, name: Optional[str] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, 
                     output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None,
                     depth: int = 1, wrapper: bool = False) -> str:
        # name = self.start_template.format(name=cen(depth + 1), info=self._code_start_repl(depth + 1))
        if output_fields is None:
            output_fields = set(self.output_fields)
        
        if wrapper:
            output_fields.add(OutputFields.code_start_wrapper)
        else:
            output_fields.add(OutputFields.code_start)

        output_fields.add(OutputFields.new_line_before_time)
        output_fields.discard(OutputFields.new_line_before_file_line_func)
        output_fields.discard(OutputFields.delimiter_before_file_line_func)
        output_fields.discard(OutputFields.file_name_line_func_name)
        output_fields.discard(OutputFields.code_line)
        output_fields.discard(OutputFields.blank_code_line)
        output_fields.discard(OutputFields.result_type)
        output_fields.discard(OutputFields.result_type_title)
        output_fields.discard(OutputFields.result_type_data)
        output_fields.discard(OutputFields.result)
        output_fields.discard(OutputFields.result_pp)
        output_fields.discard(OutputFields.result_title)
        output_fields.discard(OutputFields.result_data)
        return self.line_str(name, line_type, line_num, output_fields, line_trace, depth + 1)

    # def print_start(self, depth: int = 1):
    #     if self.print_allowed:
    #         print(self.start(depth + 1) + '\n')

    def print_start(self, name: Optional[str] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, 
                     output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None,
                     depth: int = 1, wrapper: bool = False) -> str:
        # name = self.start_template.format(name=cen(depth + 1), info=self._code_start_repl(depth + 1))
        if output_fields is None:
            output_fields = set(self.output_fields)
        
        if wrapper:
            output_fields.add(OutputFields.code_start_wrapper)
        else:
            output_fields.add(OutputFields.code_start)

        output_fields.add(OutputFields.new_line_before_time)
        output_fields.discard(OutputFields.new_line_before_file_line_func)
        output_fields.discard(OutputFields.delimiter_before_file_line_func)
        output_fields.discard(OutputFields.file_name_line_func_name)
        output_fields.discard(OutputFields.code_line)
        output_fields.discard(OutputFields.blank_code_line)
        output_fields.discard(OutputFields.result_type)
        output_fields.discard(OutputFields.result_type_title)
        output_fields.discard(OutputFields.result_type_data)
        output_fields.discard(OutputFields.result)
        output_fields.discard(OutputFields.result_pp)
        output_fields.discard(OutputFields.result_title)
        output_fields.discard(OutputFields.result_data)
        return self.print_line(name, line_type, line_num, output_fields, line_trace, depth + 1)

    # def end(self, depth: int = 1):
    #     short_name = self._start_impl_limited(depth + 1)
    #     name = self._code_start_repl(depth + 1)
    #     return self.end_template.format(index=self.index, short_name=short_name, name=name)

    def end(self, name: Optional[str] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, 
                     output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None,
                     depth: int = 1, wrapper: bool = False) -> str:
        # name = self.end_template.format(name=cen(depth + 1), info=self._code_start_repl(depth + 1))
        if output_fields is None:
            output_fields = set(self.output_fields)
        
        if wrapper:
            output_fields.add(OutputFields.code_end_wrapper)
        else:
            output_fields.add(OutputFields.code_end)

        output_fields.add(OutputFields.new_line_before_time)
        output_fields.discard(OutputFields.new_line_before_file_line_func)
        output_fields.discard(OutputFields.delimiter_before_file_line_func)
        output_fields.discard(OutputFields.file_name_line_func_name)
        output_fields.discard(OutputFields.code_line)
        output_fields.discard(OutputFields.blank_code_line)
        output_fields.discard(OutputFields.result_type)
        output_fields.discard(OutputFields.result_type_title)
        output_fields.discard(OutputFields.result_type_data)
        output_fields.discard(OutputFields.result)
        output_fields.discard(OutputFields.result_pp)
        output_fields.discard(OutputFields.result_title)
        output_fields.discard(OutputFields.result_data)
        return self.line_str(name, line_type, line_num, output_fields, line_trace, depth + 1)

    # def print_end(self, depth: int = 1):
    #     if self.print_allowed:
    #         print(self.end(depth + 1) + '\n')

    def print_end(self, name: Optional[str] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, 
                     output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None,
                     depth: int = 1, wrapper: bool = False) -> str:
        # name = self.end_template.format(name=cen(depth + 1), info=self._code_start_repl(depth + 1))
        if output_fields is None:
            output_fields = set(self.output_fields)
        
        if wrapper:
            output_fields.add(OutputFields.code_end_wrapper)
        else:
            output_fields.add(OutputFields.code_end)

        output_fields.add(OutputFields.new_line_before_time)
        output_fields.discard(OutputFields.new_line_before_file_line_func)
        output_fields.discard(OutputFields.delimiter_before_file_line_func)
        output_fields.discard(OutputFields.file_name_line_func_name)
        output_fields.discard(OutputFields.code_line)
        output_fields.discard(OutputFields.blank_code_line)
        output_fields.discard(OutputFields.result_type)
        output_fields.discard(OutputFields.result_type_title)
        output_fields.discard(OutputFields.result_type_data)
        output_fields.discard(OutputFields.result)
        output_fields.discard(OutputFields.result_pp)
        output_fields.discard(OutputFields.result_title)
        output_fields.discard(OutputFields.result_data)
        return self.print_line(name, line_type, line_num, output_fields, line_trace, depth + 1)

    def line_fields(self, line_result, name: Optional[Union[str, Callable]] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, 
                     output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None,
                     depth: int = 1):
        if output_fields is None:
            output_fields = set(self.output_fields)
        
        if callable(name):
            name = name()

        if isinstance(name, str):
            output_fields.add(OutputFields.trace_name)
        else:
            output_fields.discard(OutputFields.trace_name)
        
        trace_requiring_fields: Set[OutputFields] = {
            OutputFields.file_name_line_func_name,
            OutputFields.file_path_line_func_name,
            OutputFields.code_line,
        }

        if line_trace is None:
            if trace_requiring_fields & output_fields:
                if LineType.current_line == line_type:
                    line_trace = self.lt.trace_self(depth + 1)
                elif LineType.exact_line == line_type:
                    line_trace = self.lt.trace_exact(line_num, True, depth + 1)
                elif LineType.relative_line == line_type:
                    line_trace = self.lt.trace_relative(line_num, True, depth + 1)
                elif LineType.previous_line == line_type:
                    line_trace = self.lt.trace(depth + 1)
                elif LineType.next_line == line_type:
                    line_trace = self.lt.trace_next(depth + 1)
                
                filename, file_path, function_name, line_number, lines, index = line_trace
            else:
                filename = file_path = function_name = line_number = lines = index = None
        else:
            filename, file_path, function_name, line_number, lines, index = line_trace
        
        process_info_requiring_fields: Set[OutputFields] = {
            OutputFields.process_pid,
            OutputFields.process_name,
            OutputFields.process_is_deamon,
        }

        if process_info_requiring_fields & output_fields:
            current_process_instance: Process = current_process()
        
        thread_info_requiring_fields: Set[OutputFields] = {
            OutputFields.thread_tid,
            OutputFields.thread_ident,
            OutputFields.thread_name,
            OutputFields.process_is_deamon,
        }

        if thread_info_requiring_fields & output_fields:
            current_thread_instance: Thread = current_thread()
        
        fields: Dict[str, Any] = dict()
        if OutputFields.header in output_fields:
            fields[OutputFields.header.name] = ''

        if OutputFields.trace_index in output_fields:
            fields[OutputFields.trace_index.name] = self.index

        if OutputFields.trace_name in output_fields:
            fields[OutputFields.trace_name.name] = name

        if OutputFields.code_start_wrapper in output_fields:
            fields[OutputFields.code_start_wrapper.name] = ''

        if OutputFields.code_start in output_fields:
            fields[OutputFields.code_start.name] = AK(name=cen(depth + 1), info=self._code_start_repl(depth + 1))

        if OutputFields.code_end_wrapper in output_fields:
            fields[OutputFields.code_end_wrapper.name] = ''

        if OutputFields.code_end in output_fields:
            fields[OutputFields.code_end.name] = AK(name=cen(depth + 1), info=self._code_start_repl(depth + 1))

        if OutputFields.new_line_before_process in output_fields:
            fields[OutputFields.new_line_before_process.name] = ''

        if OutputFields.process_pid in output_fields:
            fields[OutputFields.process_pid.name] = current_process_instance.pid

        if OutputFields.process_name in output_fields:
            fields[OutputFields.process_name.name] = current_process_instance.name

        if OutputFields.process_is_deamon in output_fields:
            fields[OutputFields.process_is_deamon.name] = current_process_instance.daemon

        if OutputFields.thread_tid in output_fields:
            fields[OutputFields.thread_tid.name] = current_thread_instance.native_id if PVI >= (3, 8) else None  # Available in Python 3.8+

        if OutputFields.thread_ident in output_fields:
            fields[OutputFields.thread_ident.name] = current_thread_instance.ident

        if OutputFields.thread_name in output_fields:
            fields[OutputFields.thread_name.name] = current_thread_instance.name

        if OutputFields.thread_is_deamon in output_fields:
            fields[OutputFields.thread_is_deamon.name] = current_thread_instance.daemon

        if OutputFields.new_line_before_time in output_fields:
            fields[OutputFields.new_line_before_time.name] = ''

        if OutputFields.date_time in output_fields:
            fields[OutputFields.date_time.name] = datetime.now()

        if OutputFields.perf_counter in output_fields:
            fields[OutputFields.perf_counter.name] = perf_counter()

        if OutputFields.cpu_clock in output_fields:
            fields[OutputFields.cpu_clock.name] = cpu_clock()

        if OutputFields.cpu_clock_cycles in output_fields:
            fields[OutputFields.cpu_clock_cycles.name] = cpu_clock_cycles()

        if OutputFields.new_line_before_file_line_func in output_fields:
            fields[OutputFields.new_line_before_file_line_func.name] = ''

        if OutputFields.delimiter_before_file_line_func in output_fields:
            fields[OutputFields.delimiter_before_file_line_func.name] = ''

        if OutputFields.file_name_line_func_name in output_fields:
            fields[OutputFields.file_name_line_func_name.name] = AK(
                file_name=filename, line=line_number, func_name=function_name
            )

        if OutputFields.file_path_line_func_name in output_fields:
            fields[OutputFields.file_path_line_func_name.name] = AK(
                file_path=file_path, line=line_number, func_name=function_name
            )

        if OutputFields.code_line in output_fields:
            if '\n' in lines:
                fields[OutputFields.code_line.name] = f'\n{lines}'
            else:
                fields[OutputFields.code_line.name] = lines.strip()

        if OutputFields.blank_code_line in output_fields:
            fields[OutputFields.blank_code_line.name] = ''

        if OutputFields.blank_delim_line in output_fields:
            fields[OutputFields.blank_delim_line.name] = ''

        if OutputFields.result_type in output_fields:
            fields[OutputFields.result_type.name] = type(line_result)

        if OutputFields.result_type_title in output_fields:
            fields[OutputFields.result_type_title.name] = ''

        if OutputFields.result_type_data in output_fields:
            fields[OutputFields.result_type_data.name] = type(line_result)

        if OutputFields.result in output_fields:
            fields[OutputFields.result.name] = line_result

        if OutputFields.result_pp in output_fields:
            fields[OutputFields.result_pp.name] = get_multistr_of_data_value(line_result, 3).lstrip(' \t')

        if OutputFields.result_title in output_fields:
            fields[OutputFields.result_title.name] = ''

        if OutputFields.result_data in output_fields:
            fields[OutputFields.result_data.name] = line_result

        if OutputFields.new_line_after_end in output_fields:
            fields[OutputFields.new_line_after_end.name] = ''
        
        return fields

    def line_result_str(self, line_result, name: Optional[str] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, 
                     output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None,
                     depth: int = 1) -> str:
        fields: Dict[str, Any] = self.line_fields(line_result, name, line_type, line_num, output_fields, line_trace, depth + 1)
        return self.line_optional_formatter(**fields)

    def previous_line_result_str(self, line_result, name: Optional[str] = None, 
                           output_fields: Optional[Set[OutputFields]] = None, 
                           line_trace: Optional[Tuple] = None, 
                           depth: int = 1) -> Any:
        return self.line_result_str(line_result, name, LineType.previous_line, None, output_fields, line_trace, depth + 1)

    def next_line_result_str(self, line_result, name: Optional[str] = None, 
                      output_fields: Optional[Set[OutputFields]] = None, 
                      line_trace: Optional[Tuple] = None, 
                      depth: int = 1) -> Any:
        return self.line_result_str(line_result, name, LineType.next_line, None, output_fields, line_trace, depth + 1)

    def exact_line_result_str(self, line_result, name: Optional[str] = None, 
                       line_num: Optional[Union[int, slice]] = None, 
                       output_fields: Optional[Set[OutputFields]] = None, 
                       line_trace: Optional[Tuple] = None, 
                       depth: int = 1) -> Any:
        return self.line_result_str(line_result, name, LineType.exact_line, line_num, output_fields, line_trace, depth + 1)

    def relative_line_result_str(self, line_result, name: Optional[str] = None, 
                      line_num: Optional[Union[int, slice]] = None, 
                      output_fields: Optional[Set[OutputFields]] = None, 
                      line_trace: Optional[Tuple] = None, 
                      depth: int = 1) -> Any:
        return self.line_result_str(line_result, name, LineType.relative_line, line_num, output_fields, line_trace, depth + 1)

    def line_result_str_fast(self, line_result, name: Optional[str] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, 
                           output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None, 
                           depth: int = 1) -> Any:
        if output_fields is None:
            output_fields = set(self.output_fields)
        
        if OutputFields.result_pp in output_fields:
            output_fields.discard(OutputFields.result_pp)
            output_fields.add(OutputFields.result)

        return self.line_result_str(line_result, name, line_type, line_num, output_fields, line_trace, depth + 1)

    def previous_line_result_str_fast(self, line_result, name: Optional[str] = None, 
                           output_fields: Optional[Set[OutputFields]] = None, 
                           line_trace: Optional[Tuple] = None, 
                           depth: int = 1) -> Any:
        return self.line_result_str_fast(line_result, name, LineType.previous_line, None, output_fields, line_trace, depth + 1)

    def next_line_result_str_fast(self, line_result, name: Optional[str] = None, 
                      output_fields: Optional[Set[OutputFields]] = None, 
                      line_trace: Optional[Tuple] = None, 
                      depth: int = 1) -> Any:
        return self.line_result_str_fast(line_result, name, LineType.next_line, None, output_fields, line_trace, depth + 1)

    def exact_line_result_str_fast(self, line_result, name: Optional[str] = None, 
                       line_num: Optional[Union[int, slice]] = None, 
                       output_fields: Optional[Set[OutputFields]] = None, 
                       line_trace: Optional[Tuple] = None, 
                       depth: int = 1) -> Any:
        return self.line_result_str_fast(line_result, name, LineType.exact_line, line_num, output_fields, line_trace, depth + 1)

    def relative_line_result_str_fast(self, line_result, name: Optional[str] = None, 
                      line_num: Optional[Union[int, slice]] = None, 
                      output_fields: Optional[Set[OutputFields]] = None, 
                      line_trace: Optional[Tuple] = None, 
                      depth: int = 1) -> Any:
        return self.line_result_str_fast(line_result, name, LineType.relative_line, line_num, output_fields, line_trace, depth + 1)

    def line_str(self, name: Optional[str] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, 
                     output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None,
                     depth: int = 1) -> str:
        if output_fields is None:
            output_fields = set(self.output_fields)
        
        output_fields.discard(OutputFields.result_type)
        output_fields.discard(OutputFields.result_type_title)
        output_fields.discard(OutputFields.result_type_data)
        output_fields.discard(OutputFields.result)
        output_fields.discard(OutputFields.result_pp)
        output_fields.discard(OutputFields.result_title)
        output_fields.discard(OutputFields.result_data)
        return self.line_result_str(None, name, line_type, line_num, output_fields, line_trace, depth + 1)

    def previous_line_str(self, name: Optional[str] = None, 
                           output_fields: Optional[Set[OutputFields]] = None, 
                           line_trace: Optional[Tuple] = None, 
                           depth: int = 1) -> Any:
        return self.line_str(name, LineType.previous_line, None, output_fields, line_trace, depth + 1)

    def next_line_str(self, name: Optional[str] = None, 
                      output_fields: Optional[Set[OutputFields]] = None, 
                      line_trace: Optional[Tuple] = None, 
                      depth: int = 1) -> Any:
        return self.line_str(name, LineType.next_line, None, output_fields, line_trace, depth + 1)

    def exact_line_str(self, name: Optional[str] = None, 
                       line_num: Optional[Union[int, slice]] = None, 
                       output_fields: Optional[Set[OutputFields]] = None, 
                       line_trace: Optional[Tuple] = None, 
                       depth: int = 1) -> Any:
        return self.line_str(name, LineType.exact_line, line_num, output_fields, line_trace, depth + 1)

    def relative_line_str(self, name: Optional[str] = None, 
                      line_num: Optional[Union[int, slice]] = None, 
                      output_fields: Optional[Set[OutputFields]] = None, 
                      line_trace: Optional[Tuple] = None, 
                      depth: int = 1) -> Any:
        return self.line_str(name, LineType.relative_line, line_num, output_fields, line_trace, depth + 1)

    def print_line_result(self, line_result, name: Optional[str] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, 
                           output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None, 
                           depth: int = 1) -> Any:
        if output_fields is None:
            output_fields = self.output_fields

        if self.print_allowed:
            if RICH_PRESENT and self.rich_allowed:
                from rich.console import Console
                from rich.syntax import Syntax

                trace_requiring_fields: Set[OutputFields] = {
                    OutputFields.file_name_line_func_name,
                    OutputFields.file_path_line_func_name,
                    OutputFields.code_line,
                }

                if line_trace is None:
                    if trace_requiring_fields & output_fields:
                        if LineType.current_line == line_type:
                            line_trace = self.lt.trace_self(depth + 1)
                        elif LineType.exact_line == line_type:
                            line_trace = self.lt.trace_exact(line_num, True, depth + 1)
                        elif LineType.relative_line == line_type:
                            line_trace = self.lt.trace_relative(line_num, True, depth + 1)
                        elif LineType.previous_line == line_type:
                            line_trace = self.lt.trace(depth + 1)
                        elif LineType.next_line == line_type:
                            line_trace = self.lt.trace_next(depth + 1)
                        
                        filename, file_path, function_name, line_number, lines, index = line_trace
                    else:
                        filename = file_path = function_name = line_number = lines = index = None
                else:
                    filename, file_path, function_name, line_number, lines, index = line_trace
                
                output_fields_0: Set[OutputFields] = output_fields & self.rich_output_fields_0
                output_fields_1: Set[OutputFields] = (output_fields & self.rich_output_fields_1) - {OutputFields.new_line_after_end}
                code_line_field_found: bool = OutputFields.code_line in output_fields
                new_line_after_end_field_found: bool = OutputFields.new_line_after_end in output_fields
                if output_fields_0 and (code_line_field_found or output_fields_1):
                    output_fields_0.add(OutputFields.blank_code_line)
                
                if output_fields_1 and (code_line_field_found or output_fields_0):
                    output_fields_1.add(OutputFields.blank_code_line)
                
                if code_line_field_found and new_line_after_end_field_found:
                    output_fields_1.add(OutputFields.blank_code_line)
                
                if output_fields_0 and (not output_fields_1) and new_line_after_end_field_found:
                    output_fields_1.add(OutputFields.blank_delim_line)
                    output_fields_1.add(OutputFields.new_line_after_end)
                
                console = Console()
                joined_printing_list: List[Union[str, Any]] = list()

                if output_fields_0:
                    prepared_fields_0: Dict[str, Any] = self.line_fields(line_result, name, line_type, line_num, output_fields_0, line_trace, depth + 1)
                    joined_printing_list.extend(self.line_optional_formatter_rich_0.to_joined_list(**prepared_fields_0))

                if code_line_field_found:
                    joined_printing_list.append(Syntax(lines, "python", theme="monokai", line_numbers=True, start_line=line_number))

                if OutputFields.result_type in output_fields_1:
                    output_fields_1.discard(OutputFields.result_type)
                    output_fields_1.add(OutputFields.result_type_title)
                    output_fields_1.add(OutputFields.result_type_data)

                if (OutputFields.result in output_fields_1) or (OutputFields.result_pp in output_fields_1):
                    if isinstance(line_result, str):
                        output_fields_1.discard(OutputFields.result_pp)
                        output_fields_1.discard(OutputFields.result_title)
                        output_fields_1.discard(OutputFields.result_data)
                        output_fields_1.add(OutputFields.result)
                    else:
                        output_fields_1.discard(OutputFields.result)
                        output_fields_1.discard(OutputFields.result_pp)
                        output_fields_1.add(OutputFields.result_title)
                        output_fields_1.add(OutputFields.result_data)

                if output_fields_1:
                    prepared_fields_1: Dict[str, Any] = self.line_fields(line_result, None, line_type, line_num, output_fields_1, line_trace, depth + 1)
                    ignored_field_names: Set[str] = {OutputFields.new_line_after_end.name, OutputFields.rich_blank_line_after_end.name, OutputFields.blank_delim_line.name}
                    for field_name in reversed(self.line_optional_formatter_rich_1.of._item_positions):
                        if field_name in ignored_field_names:
                            continue

                        if field_name in prepared_fields_1:
                            filed_value = prepared_fields_1[field_name]
                            if isinstance(filed_value, str) and (OutputFields.blank_code_line.name != field_name):
                                break

                            if (not isinstance(filed_value, str)) or (OutputFields.blank_code_line.name == field_name):
                                if OutputFields.new_line_after_end.name in prepared_fields_1:
                                    prepared_fields_1[OutputFields.rich_blank_line_after_end.name] = ''
                                    prepared_fields_1.pop(OutputFields.new_line_after_end.name, None)
                                
                                break

                joined_printing_list.extend(self.line_optional_formatter_rich_1.to_joined_list(**prepared_fields_1))
                console.print(*joined_printing_list, soft_wrap=True)
            else:
                print(self.line_result_str(line_result, name, line_type, line_num, output_fields, line_trace, depth + 1))
        
        return line_result

    def print_previous_line_result(self, line_result, name: Optional[str] = None, 
                           output_fields: Optional[Set[OutputFields]] = None, 
                           line_trace: Optional[Tuple] = None, 
                           depth: int = 1) -> Any:
        return self.print_line_result(line_result, name, LineType.previous_line, None, output_fields, line_trace, depth + 1)

    def print_next_line_result(self, line_result, name: Optional[str] = None, 
                      output_fields: Optional[Set[OutputFields]] = None, 
                      line_trace: Optional[Tuple] = None, 
                      depth: int = 1) -> Any:
        return self.print_line_result(line_result, name, LineType.next_line, None, output_fields, line_trace, depth + 1)

    def print_exact_line_result(self, line_result, name: Optional[str] = None, 
                       line_num: Optional[Union[int, slice]] = None, 
                       output_fields: Optional[Set[OutputFields]] = None, 
                       line_trace: Optional[Tuple] = None, 
                       depth: int = 1) -> Any:
        return self.print_line_result(line_result, name, LineType.exact_line, line_num, output_fields, line_trace, depth + 1)

    def print_relative_line_result(self, line_result, name: Optional[str] = None, 
                      line_num: Optional[Union[int, slice]] = None, 
                      output_fields: Optional[Set[OutputFields]] = None, 
                      line_trace: Optional[Tuple] = None, 
                      depth: int = 1) -> Any:
        return self.print_line_result(line_result, name, LineType.relative_line, line_num, output_fields, line_trace, depth + 1)

    def print_line_result_fast(self, line_result, name: Optional[str] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, 
                           output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None, 
                           depth: int = 1) -> Any:
        if output_fields is None:
            output_fields = set(self.output_fields)
        
        if OutputFields.result_pp in output_fields:
            output_fields.discard(OutputFields.result_pp)
            output_fields.add(OutputFields.result)

        return self.print_line_result(line_result, name, line_type, line_num, output_fields, line_trace, depth + 1)

    def print_previous_line_result_fast(self, line_result, name: Optional[str] = None, 
                           output_fields: Optional[Set[OutputFields]] = None, 
                           line_trace: Optional[Tuple] = None, 
                           depth: int = 1) -> Any:
        return self.print_line_result_fast(line_result, name, LineType.previous_line, None, output_fields, line_trace, depth + 1)

    def print_next_line_result_fast(self, line_result, name: Optional[str] = None, 
                      output_fields: Optional[Set[OutputFields]] = None, 
                      line_trace: Optional[Tuple] = None, 
                      depth: int = 1) -> Any:
        return self.print_line_result_fast(line_result, name, LineType.next_line, None, output_fields, line_trace, depth + 1)

    def print_exact_line_result_fast(self, line_result, name: Optional[str] = None, 
                       line_num: Optional[Union[int, slice]] = None, 
                       output_fields: Optional[Set[OutputFields]] = None, 
                       line_trace: Optional[Tuple] = None, 
                       depth: int = 1) -> Any:
        return self.print_line_result_fast(line_result, name, LineType.exact_line, line_num, output_fields, line_trace, depth + 1)

    def print_relative_line_result_fast(self, line_result, name: Optional[str] = None, 
                      line_num: Optional[Union[int, slice]] = None, 
                      output_fields: Optional[Set[OutputFields]] = None, 
                      line_trace: Optional[Tuple] = None, 
                      depth: int = 1) -> Any:
        return self.print_line_result_fast(line_result, name, LineType.relative_line, line_num, output_fields, line_trace, depth + 1)

    def print_line(self, name: Optional[str] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, 
                           output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None, 
                           depth: int = 1) -> Any:
        if output_fields is None:
            output_fields = set(self.output_fields)
        
        output_fields.discard(OutputFields.result_type)
        output_fields.discard(OutputFields.result_type_title)
        output_fields.discard(OutputFields.result_type_data)
        output_fields.discard(OutputFields.result)
        output_fields.discard(OutputFields.result_pp)
        output_fields.discard(OutputFields.result_title)
        output_fields.discard(OutputFields.result_data)
        return self.print_line_result(None, name, line_type, line_num, output_fields, line_trace, depth + 1)

    def print_previous_line(self, name: Optional[str] = None, 
                           output_fields: Optional[Set[OutputFields]] = None, 
                           line_trace: Optional[Tuple] = None, 
                           depth: int = 1) -> Any:
        return self.print_line(name, LineType.previous_line, None, output_fields, line_trace, depth + 1)

    def print_next_line(self, name: Optional[str] = None, 
                      output_fields: Optional[Set[OutputFields]] = None, 
                      line_trace: Optional[Tuple] = None, 
                      depth: int = 1) -> Any:
        return self.print_line(name, LineType.next_line, None, output_fields, line_trace, depth + 1)

    def print_exact_line(self, name: Optional[str] = None, 
                       line_num: Optional[Union[int, slice]] = None, 
                       output_fields: Optional[Set[OutputFields]] = None, 
                       line_trace: Optional[Tuple] = None, 
                       depth: int = 1) -> Any:
        return self.print_line(name, LineType.exact_line, line_num, output_fields, line_trace, depth + 1)

    def print_relative_line(self, name: Optional[str] = None, 
                      line_num: Optional[Union[int, slice]] = None, 
                      output_fields: Optional[Set[OutputFields]] = None, 
                      line_trace: Optional[Tuple] = None, 
                      depth: int = 1) -> Any:
        return self.print_line(name, LineType.relative_line, line_num, output_fields, line_trace, depth + 1)
    
    # def __call__(self, depth: int = 1):
    #     _, _, _, prev_line_number, prev_lines, _ = self.lt.trace(depth + 1)
    #     filename, file_path, function_name, next_line_number, next_lines, _ = self.lt.trace_next(depth + 1)
    #     return filename, file_path, function_name, prev_line_number, next_line_number, prev_lines, next_lines


auto_line_tracer: AutoLineTracer = AutoLineTracer()
alt: AutoLineTracer = auto_line_tracer


# Trace Result
def trace_result(line_result, name: Optional[str] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None, depth: int = 1) -> Any:
    return auto_line_tracer.print_line_result(line_result, name, line_type, line_num, output_fields, line_trace, depth + 1)


tr = trace_result


def fake_trace_result(line_result, name: Optional[str] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None, depth: int = 1):
    return line_result


ftr = fake_trace_result


# Trace
def trace(name: Optional[str] = None, output_fields: Optional[Set[OutputFields]] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, line_trace: Optional[Tuple] = None, depth: int = 1) -> Any:
    output_fields: Set[OutputFields] = set(auto_line_tracer.output_fields)
    output_fields.discard(OutputFields.code_line)
    output_fields.discard(OutputFields.blank_code_line)
    return auto_line_tracer.print_line(name, line_type, line_num, output_fields, line_trace, depth + 1)


t = trace


def fake_trace(name: Optional[str] = None, output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None, depth: int = 1):
    return


ft = fake_trace


# Trace Line
def trace_line(name: Optional[str] = None, output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None, depth: int = 1) -> Any:
    return auto_line_tracer.print_next_line(name, output_fields, line_trace, depth + 1)


tl = trace_line


def fake_trace_line(name: Optional[str] = None, output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None, depth: int = 1):
    return


ftl = fake_trace_line


# Trace Start
def trace_start(name: Optional[str] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None, depth: int = 1) -> Any:
    return auto_line_tracer.print_start(name, line_type, line_num, output_fields, line_trace, depth + 1)


ts = trace_start


def fake_trace_start(line_result, name: Optional[str] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None, depth: int = 1):
    return line_result


fts = fake_trace_start


# Trace End
def trace_end(name: Optional[str] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None, depth: int = 1) -> Any:
    return auto_line_tracer.print_end(name, line_type, line_num, output_fields, line_trace, depth + 1)


te = trace_end


def fake_trace_end(line_result, name: Optional[str] = None, line_type: LineType = LineType.current_line, line_num: Optional[Union[int, slice]] = None, output_fields: Optional[Set[OutputFields]] = None, line_trace: Optional[Tuple] = None, depth: int = 1):
    return line_result


fte = fake_trace_end
