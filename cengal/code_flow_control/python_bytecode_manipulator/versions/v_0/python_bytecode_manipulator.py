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


from collections import namedtuple
from dis import Instruction, dis, get_instructions, _get_code_object, code_info, show_code, findlabels, _unpack_opargs
from opcode import hasjrel, hasjabs, opname, opmap, HAVE_ARGUMENT, EXTENDED_ARG
from cengal.system import PYTHON_VERSION_INT
from enum import Enum
from typing import Optional, Callable, List, Tuple, Dict, Set, Union, Any, Sequence
from types import CodeType
from copy import copy
from cengal.entities.copyable import CopyableMixin
from cengal.data_manipulation.front_triggerable_variable import FrontTriggerableVariableType, FrontTriggerableVariable
import sys


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


BytecodeSequence = Union[bytes, Sequence[Union[int, bytes]]]


def patch_function(func, co_code):
    fn_code = func.__code__
    func.__code__ = CodeType(
        fn_code.co_argcount,
        fn_code.co_kwonlyargcount,
        fn_code.co_nlocals,
        fn_code.co_stacksize,
        fn_code.co_flags,
        co_code,
        fn_code.co_consts,
        fn_code.co_names,
        fn_code.co_varnames,
        fn_code.co_filename,
        fn_code.co_name,
        fn_code.co_firstlineno,
        fn_code.co_lnotab,
        fn_code.co_freevars,
        fn_code.co_cellvars,
    )


CodeParamNames = namedtuple("CodeParamNames", "positional positional_only keyword_only")


def code_param_names(code) -> CodeParamNames:
    pos_count = code.co_argcount
    arg_names = code.co_varnames
    positional = arg_names[:pos_count]
    posonly_count = code.co_posonlyargcount
    positional_only = arg_names[:posonly_count]
    keyword_only_count = code.co_kwonlyargcount
    keyword_only = arg_names[pos_count:pos_count + keyword_only_count]
    return CodeParamNames(positional, positional_only, keyword_only)


def code_name(code: CodeType) -> str:
    return code.co_name


if sys.version_info >= (3, 11):
    def code_qualname(code: CodeType) -> str:
        return code.co_qualname


def get_code(x=None) -> CodeType:
    if x is None:
        return
    
    if isinstance(x, CodeType):
        return x
    
    # Extract functions from methods.
    if hasattr(x, '__func__'):
        x = x.__func__
    # Extract compiled code objects from...
    if hasattr(x, '__code__'):  # ...a function, or
        x = x.__code__
    elif hasattr(x, 'gi_code'):  #...a generator object, or
        x = x.gi_code
    elif hasattr(x, 'ag_code'):  #...an asynchronous generator object, or
        x = x.ag_code
    elif hasattr(x, 'cr_code'):  #...a coroutine, or
        x = x.cr_code
    elif hasattr(x, 'f_code'):  #...a frame.
        x = x.f_code
    # else:
    #     raise TypeError(f'Expected a code object or an entity with code, but got {type(x)}')
    
    return x


class CodeTypeEnum(Enum):
    class_or_module = 0
    code_object = 1
    raw_bytecode = 2
    source_code = 3
    unknown = 4


def code_type(x=None) -> Optional[CodeTypeEnum]:
    """_summary_

    Args:
        x (_type_, optional): result of get_code() function. Defaults to None.

    Returns:
        Optional[CodeTypeEnum]: _description_
    """
    if x is None:
        return
    
    # Perform the disassembly.
    if hasattr(x, '__dict__'):  # Class or module
        return CodeTypeEnum.class_or_module
    elif hasattr(x, 'co_code'): # Code object
        return CodeTypeEnum.code_object
    elif isinstance(x, (bytes, bytearray)): # Raw bytecode
        return CodeTypeEnum.raw_bytecode
    elif isinstance(x, str):    # Source code
        return CodeTypeEnum.source_code
    else:
        return CodeTypeEnum.unknown


def set_code(x, code: CodeType):
    # Extract functions from methods.
    if hasattr(x, '__func__'):
        x.__func__ = code
    # Extract compiled code objects from...
    if hasattr(x, '__code__'):  # ...a function, or
        x.__code__ = code
    elif hasattr(x, 'gi_code'):  #...a generator object, or
        x.gi_code = code
    elif hasattr(x, 'ag_code'):  #...an asynchronous generator object, or
        x.ag_code = code
    elif hasattr(x, 'cr_code'):  #...a coroutine.
        x.cr_code = code
    
    return x


if (3, 11) > PYTHON_VERSION_INT[:1]:
    def modify_code(original_code: CodeType, co_code, co_consts, co_names, co_varnames):
        co_nlocals = len(co_varnames)
        return CodeType(
            original_code.co_argcount,
            original_code.co_posonlyargcount,
            original_code.co_kwonlyargcount,
            co_nlocals,
            original_code.co_stacksize,
            original_code.co_flags,
            co_code,
            tuple(co_consts),
            tuple(co_names),
            tuple(co_varnames),
            original_code.co_filename,
            original_code.co_name,
            original_code.co_firstlineno,
            original_code.co_lnotab,
            original_code.co_freevars,
            original_code.co_cellvars,
        )


    # def unpack_opargs_original(code, denormalize_values: bool = False):
    #     ftv: FrontTriggerableVariable = FrontTriggerableVariable(FrontTriggerableVariableType.equal, EXTENDED_ARG)
    #     extended_arg = 0
    #     real_op_index: Optional[int] = None
    #     real_byte_index: Optional[int] = None
    #     need_to_clear_real_data: bool = False

    #     op_index = -1
    #     for i in range(0, len(code), 2):
    #         op_index += 1
    #         op = code[i]
    #         if op >= HAVE_ARGUMENT:
    #             ftv_result: Optional[bool] = ftv(op)
    #             if ftv_result is True:
    #                 real_op_index = op_index
    #                 real_byte_index = i
    #             elif ftv_result is False:
    #                 need_to_clear_real_data = True

    #             arg = code[i+1] | extended_arg
    #             if denormalize_values:
    #                 extended_arg = (arg << 8) if op == EXTENDED_ARG else 0
    #         else:
    #             arg = None
            
    #         yield (op, arg, op_index, i, real_op_index, real_byte_index)
    #         if need_to_clear_real_data:
    #             real_op_index = None
    #             real_byte_index = None
    #             need_to_clear_real_data = False

    def unpack_opargs(code: BytecodeSequence, denormalize_values: bool = False):
        ftv: FrontTriggerableVariable = FrontTriggerableVariable(FrontTriggerableVariableType.equal, EXTENDED_ARG)
        extended_arg = 0
        real_op_index: Optional[int] = None
        real_offset: Optional[int] = None
        need_to_clear_real_data: bool = False

        op = None
        arg = None
        offset = -1
        op_index = -1
        i = -1
        for item in code:
            if isinstance(item, bytes):
                item = int.from_bytes(item, byteorder='little')
            
            i += 1
            if not i % 2:
                op = item
                op_index += 1
                offset = i
                continue
            
            if op >= HAVE_ARGUMENT:
                ftv_result: Optional[bool] = ftv(op)
                if ftv_result is True:
                    real_op_index = op_index
                    real_offset = offset
                elif ftv_result is False:
                    need_to_clear_real_data = True

                arg = item | extended_arg
                if denormalize_values:
                    extended_arg = (arg << 8) if op == EXTENDED_ARG else 0
            else:
                arg = None
            
            yield (op, arg, op_index, offset, real_op_index, real_offset)
            if need_to_clear_real_data:
                real_op_index = None
                real_offset = None
                need_to_clear_real_data = False

    def find_ops_with_labels(code: BytecodeSequence) -> Tuple[List[int], Dict[int, List[Tuple[int, int, int, int]]]]:
        labels: List[int] = list()
        op_by_label: Dict[int, List[Tuple[int, int, int, int]]] = dict()
        for op, arg, op_index, offset, real_op_index, real_offset in unpack_opargs(code, True):
            if arg is not None:
                if op in hasjrel:
                    label = offset + 2 + arg
                elif op in hasjabs:
                    label = arg
                else:
                    continue

                if label not in op_by_label:
                    labels.append(label)
                    op_by_label[label] = list()
                
                op_by_label[label].append((op, arg, op_index, offset, real_op_index, real_offset))

        return labels, op_by_label
    
    
    def op_index_to_arg(op_index: int) -> int:
        return op_index * 2
    

    def arg_to_op_index(arg: int) -> int:
        return arg // 2

elif (3, 11) >= PYTHON_VERSION_INT[:1]:
    from dis import _is_backward_jump

    def find_ops_with_labels(code):
        labels = list()
        op_by_label = dict()
        index = -1
        for offset, op, arg in _unpack_opargs(code):
            index += 1
            if arg is not None:
                if op in hasjrel:
                    if _is_backward_jump(op):  # inefficient implementation of the _is_backward_jump() function. Need to use set or list instead of string manipulations
                        arg = -arg

                    label = offset + 2 + arg*2  # In 3.10: this is an instruction index - not a byte index. Need to be fixed and tested
                elif op in hasjabs:
                    label = arg*2
                else:
                    continue

                if label not in op_by_label:
                    labels.append(label)
                    op_by_label[label] = list()
                
                op_by_label[label].append((index, offset, op, arg))

        return labels, op_by_label
else:
    import warnings
    warnings.warn(f'Unsupported Python Version: {PYTHON_VERSION_INT}')
    # raise RuntimeError(f'Unsupported Python Version: {PYTHON_VERSION_INT}')


class OpSequenceOffsetMap(CopyableMixin):
    def __init__(self, op_num: int = 0):
        self.op_num: int = op_num
        self.range: Optional[slice] = slice(0, op_num) if op_num else None
        self.new_by_original: Dict[int, int] = dict()
        self.original_by_new: Dict[int, int] = dict()
        if op_num < 0:
            op_num = 0
        
        for index in range(op_num):
            # bindex = index * 2
            bindex = index
            self.new_by_original[bindex] = bindex
            self.original_by_new[bindex] = bindex
    
    def mapped_range(self) -> slice:
        return slice(min(self.original_by_new), max(self.original_by_new))

    
    def remove_slice(self, op_index: int, op_num: int, preserver_index_for_first_x_op: int = 0):
        if not op_num:
            return
        
        offset_change_start = op_index
        del_start = op_index
        del_stop = op_index + op_num

        new_by_original_buff = self.new_by_original
        self.new_by_original = type(self.new_by_original)()
        to_be_deleted: List[Tuple[int, int]] = list()
        for original, new in new_by_original_buff.items():
            if del_start <= new < del_stop:
                to_be_deleted.append((original, new))
        
        to_be_deleted.sort(key=lambda x: x[1])
        if preserver_index_for_first_x_op:
            to_be_deleted = to_be_deleted[preserver_index_for_first_x_op:]
        
        for original, new in to_be_deleted:
            del self.new_by_original[original]
        
        original_by_new_buff = self.original_by_new
        self.original_by_new = type(self.original_by_new)()
        to_be_deleted = list()
        for new, original in original_by_new_buff.items():
            if del_start <= new < del_stop:
                to_be_deleted.append((new, original))
        
        to_be_deleted.sort(key=lambda x: x[0])
        if preserver_index_for_first_x_op:
            ignored = to_be_deleted[:preserver_index_for_first_x_op]
            if ignored:
                last_ignored = ignored[-1]
                last_ignored_new = last_ignored[0]
                offset_change_start = last_ignored_new + 1
            
            to_be_deleted = to_be_deleted[preserver_index_for_first_x_op:]
        
        for new, original in to_be_deleted:
            del self.original_by_new[new]
        
        self.add_offset(-op_num, offset_change_start)
        self.op_num -= op_num
        self.range = slice(self.range.start, self.range.stop - op_num)
    
    def insert_slice(self, op_index: int, op_num: int, preserver_index_for_first_x_op: int = 0):
        if not op_num:
            return
        
        self.add_offset(op_num, op_index + preserver_index_for_first_x_op)
        self.op_num += op_num
        self.range = slice(self.range.start, self.range.stop + op_num)
    
    def insert_op_sequence_offset(self, op_index: int, op_sequence_offset_map: 'OpSequenceOffsetMap', insertion_id: Any, preserver_index_for_first_x_op: int = 0):
        op_num: int = op_sequence_offset_map.op_num
        if not op_num:
            return
        
        sequence_range: slice = op_sequence_offset_map.range
        offset = op_index - sequence_range.start
        self.insert_slice(op_index, op_num, preserver_index_for_first_x_op)
        for new, original in op_sequence_offset_map.original_by_new.items():
            self.original_by_new[new + offset] = (insertion_id, new)
    
    def add_offset(self, op_offset: int, op_start: int = 0):
        if not op_offset:
            return
        
        new_by_original_buff = self.new_by_original
        self.new_by_original = type(self.new_by_original)()
        for original, new in new_by_original_buff.items():
            if new >= op_start:
                new += op_offset
            
            self.new_by_original[original] = new
        
        original_by_new_buff = self.original_by_new
        self.original_by_new = type(self.original_by_new)()
        for new, original in original_by_new_buff.items():
            if new >= op_start:
                new += op_offset
            
            self.original_by_new[new] = original
    
    def shift(self, op_offset: int):
        self.add_offset(op_offset)
        self.range = slice(self.range.start + op_offset, self.range.stop + op_offset)
    
    def shift_to_absolute(self, op_index: int):
        op_offset: int = op_index - self.range.start
        self.add_offset(op_offset)
        self.range = slice(self.range.start + op_offset, self.range.stop + op_offset)
    
    def update(self, op_sequence_offset_map: 'OpSequenceOffsetMap', op_offset: int = 0):
        if op_offset:
            op_sequence_offset_map = op_sequence_offset_map.copy()
            op_sequence_offset_map.add_offset(op_offset)
        
        self.new_by_original.update(op_sequence_offset_map.new_by_original)
        self.original_by_new.update(op_sequence_offset_map.original_by_new)
    
    def __getitem__(self, index: Union[int, slice]) -> 'OpSequenceOffsetMap':
        if isinstance(index, int):
            index = slice(index, index + 1)
        
        op_num = index.stop - index.start

        new_by_original_buff = self.new_by_original
        new_by_original = type(new_by_original_buff)()
        for original, new in new_by_original_buff.items():
            if index.start <= new < index.stop:
                new_by_original[original] = new
        
        original_by_new_buff = self.original_by_new
        original_by_new = type(original_by_new_buff)()
        for new, original in original_by_new_buff.items():
            if index.start <= new < index.stop:
                original_by_new[new] = original

        result = OpSequenceOffsetMap()
        result.op_num = op_num
        result.range = index
        result.new_by_original = new_by_original
        result.original_by_new = original_by_new
        return result

    def copy(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__['new_by_original'] = copy(self.new_by_original)
        result.__dict__['original_by_new'] = copy(self.original_by_new)
        result.__dict__['op_num'] = self.op_num
        result.__dict__['range'] = copy(self.range)
        return result


def opcode(name: str) -> int:
    name = name.upper()
    return opmap[name]


def opcode_name(opcode: int) -> str:
    return opname[opcode]


class OpSequence:
    extended_arg_opcode_int = opcode('EXTENDED_ARG')
    extended_arg_opcode_byte = extended_arg_opcode_int.to_bytes(1, byteorder='little')

    def __init__(self, op_sequence: Optional[List[Tuple[int, int, int, int, int, int]]] = None):
        self.op_sequence: List[Tuple[int, int, int, int, int, int]] = list() if op_sequence is None else op_sequence
        self.op_sequence_offset_map: OpSequenceOffsetMap = OpSequenceOffsetMap(len(self.op_sequence))
    
    def __len__(self):
        return len(self.op_sequence)
    
    def read_slice(self, place: slice) -> 'OpSequence':
        result = OpSequence()
        result.op_sequence = self.op_sequence[place]
        result.op_sequence_offset_map = self.op_sequence_offset_map[place]
        result.op_sequence_offset_map.shift_to_absolute(0)
        return result
    
    def remove_slice(self, place: slice, preserver_index_for_first_x_op: int = 0):
        self.op_sequence[place] = []
        self.op_sequence_offset_map.remove_slice(place.start, place.stop - place.start, preserver_index_for_first_x_op)
    
    def insert_op_sequence(self, index: int, op_sequence: 'OpSequence', preserver_index_for_first_x_op: int = 0):
        self.op_sequence[index: index] = op_sequence.op_sequence
        op_sequence.op_sequence_offset_map.shift_to_absolute(index)
        self.op_sequence_offset_map.insert_op_sequence_offset(index, op_sequence.op_sequence_offset_map, op_sequence, preserver_index_for_first_x_op)
        return op_sequence
    
    def normalize_instructions_arg(self):
        index = -1
        while True:
            index += 1
            if index >= len(self.op_sequence):
                break

            op, arg, op_index, offset, real_op_index, real_offset = self.op_sequence[index]
            if arg is not None:
                if arg > 255:
                    arg = arg_to_bytes(arg)
                    if real_op_index is not None:
                        real_op_index_delta = real_op_index - op_index
                        real_op_index = index - real_op_index_delta
                        slice_to_delete = slice(real_op_index, index)
                        self.remove_slice(slice_to_delete, 1)
                        index = real_op_index

                    extended_arg: bytes = arg[1:]
                    extended_arg_len = len(extended_arg)
                    arg = arg[0]
                    self.op_sequence[index] = (op, arg, index + extended_arg_len, (index + extended_arg_len) * 2, index, index * 2)
                    op_sub_sequence_instructions = list()
                    for extended_arg_int in reversed(extended_arg):
                        op_sub_sequence_instructions.append(make_instruction('EXTENDED_ARG', extended_arg_int))
                    
                    sub_op_sequence: 'OpSequence' = OpSequence.from_instructions_fast(op_sub_sequence_instructions)
                    self.insert_op_sequence(index, sub_op_sequence, 1)
                    index += len(sub_op_sequence.op_sequence)
    
    def denormalize_instructions_arg(self):
        raise NotImplementedError
    
    def find_op(self, op_index: int) -> Optional[slice]:
        start_index = None
        end_index = None

        index = op_index - 1
        while True:
            index += 1
            if index >= len(self.op_sequence):
                break

            current_op, current_arg, _, _, _, _ = self.op_sequence[index]
            if current_op == OpSequence.extended_arg_opcode_int:
                continue
            else:
                end_index = index + 1
                break
        
        previous_op_is_extended_arg = None
        index = op_index
        while True:
            index -= 1
            if index < 0:
                if previous_op_is_extended_arg:
                    start_index = 0
                
                break
            
            current_op, current_arg, _, _, _, _ = self.op_sequence[index]
            if current_op == OpSequence.extended_arg_opcode_int:
                previous_op_is_extended_arg = True
                continue
            else:
                previous_op_is_extended_arg = False
                start_index = index + 1
                break
        
        if (start_index is None) or (end_index is None):
            return None
        
        return slice(start_index, end_index)
    
    def get_arg(self, op_index: Union[int, slice]) -> bytes:
        if isinstance(op_index, int):
            op_index = self.find_op(op_index)
        
        if (op_index is None) or ((op_index.stop - op_index.start) < 1):
            raise RuntimeError('OP not found by index')
        
        op_slice = self.op_sequence[op_index]
        if (op_index.stop - op_index.start) > 1:
            arg_list = list()
            for op, arg, _, _, _, _ in reversed(op_slice):
                arg_list.append(arg)
            
            return arg_to_int(bytes(arg_list))
        else:
            return op_slice[0][1]
    
    def set_arg(self, op_index: Union[int, slice], new_arg: Union[None, int, bytes]):
        if isinstance(op_index, int):
            op_index = self.find_op(op_index)
        
        op_index_len = op_index.stop - op_index.start
        if (op_index is None) or (op_index_len < 1):
            raise RuntimeError('OP not found by index')
        
        new_arg = arg_to_int(new_arg)
        current_op, current_arg, current_op_index, current_offset, current_real_op_index, current_real_offset = self.op_sequence[op_index.stop - 1]
        sub_op_sequence_bytes = [current_op, new_arg]
        sub_op_sequence: OpSequence = OpSequence(list(unpack_opargs(sub_op_sequence_bytes)))
        sub_op_sequence.normalize_instructions_arg()
        real_arg = sub_op_sequence.op_sequence[-1][1]
        sub_op_sequence_len = len(sub_op_sequence.op_sequence)
        extended_args_len = sub_op_sequence_len - 1
        if extended_args_len:
            current_real_op_index = op_index.start
            current_real_offset = current_real_op_index * 2
            current_op_index = current_real_op_index + extended_args_len
            current_offset = current_op_index * 2
        else:
            current_op_index = op_index.start
            current_offset = current_op_index * 2
            current_real_op_index = None
            current_real_offset = None

        self.op_sequence[op_index.stop - 1] = (current_op, real_arg, current_op_index, current_offset, current_real_op_index, current_real_offset)

        if sub_op_sequence_len > 1:
            sub_op_sequence.remove_slice(slice(sub_op_sequence_len - 1, sub_op_sequence_len))
            if op_index_len > 1:
                self.remove_slice(slice(op_index.start, op_index.stop - 1), 1)
            
            self.insert_op_sequence(op_index.start, sub_op_sequence, 1)

    def fix_labels(self, op_by_label: Dict[int, List[int]]):
        labels = list(op_by_label.keys())
        labels.sort()
        for label, data in op_by_label.items():
            data.sort()
        
        for label in labels:
            labeled_op_index_new = self.op_sequence_offset_map.new_by_original[label]
            label_data = op_by_label[label]
            while True:
                for op_index in label_data:
                    op_index_new = self.op_sequence_offset_map.new_by_original[op_index]
                    op = self.op_sequence[op_index_new][0]
                    new_arg = op_index_to_arg(labeled_op_index_new)
                    if op in hasjrel:
                        new_arg = new_arg - (op_index_to_arg(op_index_new) + 2)
                    
                    self.set_arg(op_index_new, new_arg)
                
                labeled_op_index_new_after_value_change = self.op_sequence_offset_map.new_by_original[label]
                if labeled_op_index_new_after_value_change == labeled_op_index_new:
                    break
                else:
                    labeled_op_index_new = labeled_op_index_new_after_value_change

    def to_sequence_of_ints(self):
        for op, arg, _, _, _, _ in self.op_sequence:
            yield op
            if arg is None:
                yield 0
            else:
                yield arg

    def to_bytes(self) -> bytes:
        return bytes(self.to_sequence_of_ints())
        
    @staticmethod
    def from_bytecode_sequence(code: BytecodeSequence):
        labels, op_by_label = find_ops_with_labels(code)
        return OpSequence(list(unpack_opargs(code))), labels, op_by_label
    
    @staticmethod
    def from_entity(entity):
        code_bytes: BytecodeSequence = _get_code_object(entity).co_code
        return OpSequence.from_bytecode_sequence(code_bytes)
    
    @staticmethod
    def from_instructions(instructions: Sequence[Instruction]):
        op_sequence: List = list()
        for instruction in instructions:
            arg = instruction.arg
            if arg is None:
                arg = 0

            op_sequence.extend((instruction.opcode, arg))

        labels, op_by_label = find_ops_with_labels(op_sequence)
        result = OpSequence(list(unpack_opargs(op_sequence)))
        result.normalize_instructions_arg()
        return result, labels, op_by_label
    
    @staticmethod
    def from_instructions_fast(instructions: Sequence[Instruction]):
        return OpSequence(list(unpack_opargs(instructions_to_sequence_of_ints(normalize_instructions_arg(instructions)))))


def arg_to_bytes(arg: Union[int, bytes]) -> bytes:
    if isinstance(arg, int):
        arg = arg.to_bytes(4, byteorder='little')
        if len(arg) > 1:
            arg = arg.rstrip(b'\x00')
            
        if not arg:
            arg = b'\x00'
    
    return arg


def arg_to_int(arg: Union[int, bytes]) -> int:
    if isinstance(arg, bytes):
        arg = int.from_bytes(arg, byteorder='little')
    
    return arg


def get_raw_instructions(x, *, first_line=None):
    readable_instructions = get_instructions(x, first_line)
    for instruction in readable_instructions:
        arg = instruction.arg
        if arg is not None:
            if isinstance(arg, int):
                arg = arg.to_bytes(4, byteorder='little')
            
            arg = arg[0]

        yield Instruction(instruction.opname, instruction.opcode, arg, instruction.argval, instruction.argrepr, instruction.offset, instruction.starts_line, instruction.is_jump_target)


def normalize_instructions_arg(instructions: Sequence[Instruction]):
    for instruction in instructions:
        arg = instruction.arg
        if arg is not None:
            arg = arg_to_bytes(arg)
            extended_arg = arg[1:]
            arg = arg[0]
            for extended_arg_int in reversed(extended_arg):
                yield make_instruction('EXTENDED_ARG', extended_arg_int)

        yield Instruction(instruction.opname, instruction.opcode, arg, instruction.argval, instruction.argrepr, instruction.offset, instruction.starts_line, instruction.is_jump_target)


def instructions_to_sequence_of_ints(instructions: Sequence[Instruction]):
    for instruction in instructions:
        op = instruction.opcode
        yield op
        arg = instruction.arg
        yield 0 if arg is None else arg


def instructions_to_bytes(instructions: Sequence[Instruction]) -> bytes:
    return bytes(instructions_to_sequence_of_ints(instructions))


def make_instruction(name: str, arg: Union[None, int, bytes] = None) -> Instruction:
    name = name.upper()
    op = opmap[name]
    arg = arg_to_int(arg)
    return Instruction(name, op, arg, None, None, None, None, None)


mi = make_instruction


def fix_labels(op_sequence: OpSequence, op_by_label: Dict[int, List[Tuple[int, int, int, int, int, int]]]):
    op_sequence.fix_labels({arg_to_op_index(label): [op_info[2] for op_info in data] for label, data in op_by_label.items()})


def code_info(x):
    """Formatted details of methods, functions, or code."""
    return _format_code_info(_get_code_object(x))


def _pr(name, data):
    print(f'<<{name}>> type: {type(data)}; value: {data}')


def _format_code_info(co):
    _pr('Name', co.co_name)
    _pr('Filename', co.co_filename)
    _pr('Argument count', co.co_argcount)
    _pr('Positional-only arguments', co.co_posonlyargcount)
    _pr('Kw-only arguments', co.co_kwonlyargcount)
    _pr('Number of locals', co.co_nlocals)
    _pr('Stack size', co.co_stacksize)
    _pr('Flags', co.co_flags)
    _pr('Constants', co.co_consts)
    _pr('Names', co.co_names)
    _pr('Variable names', co.co_varnames)
    _pr('Free variables', co.co_freevars)
    _pr('Cell variables', co.co_cellvars)
