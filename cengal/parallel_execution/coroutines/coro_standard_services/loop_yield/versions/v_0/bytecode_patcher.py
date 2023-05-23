#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""


__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.2.2"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from typing import Callable, List
from types import CodeType
from cengal.code_flow_control.python_bytecode_manipulator import *


def gly_patch(entity: Callable) -> Callable:
    # TODO: try to complise strings using _get_code_object() instead of get_code()
    entity_code_type: CodeTypeEnum = code_type(entity)
    if entity_code_type is None:
        raise RuntimeError( 'Entity {entity} cann not be patched')
    
    fn_code = get_code(entity)
    op_sequence, labels, op_by_label = OpSequence.from_bytecode_sequence(fn_code.co_code)
    op_sequence: OpSequence = op_sequence
    co_consts = list(fn_code.co_consts)
    first_new_const_index: int = len(co_consts)
    co_names = list(fn_code.co_names)
    first_new_name_index: int = len(co_names)
    co_varnames = list(fn_code.co_varnames)
    first_new_varname_index: int = len(co_varnames)
    co_nlocals = fn_code.co_nlocals


    co_consts.extend((0, ('gly',)))
    co_names.extend(('cengal.parallel_execution.coroutines.coro_standard_services.loop_yield', 'gly'))
    co_varnames.extend(('gly', 'ly'))
    co_nlocals = len(co_varnames)

    initialization: List[Instruction] = [
        mi('LOAD_CONST', first_new_const_index + 0),
        mi('LOAD_CONST', first_new_const_index + 1),
        mi('IMPORT_NAME', first_new_name_index + 0),
        mi('IMPORT_FROM', first_new_name_index + 1),
        mi('STORE_FAST', first_new_varname_index + 0),
        mi('POP_TOP'),
        mi('LOAD_FAST', first_new_varname_index + 0),
        mi('CALL_FUNCTION', 0),
        mi('STORE_FAST', first_new_varname_index + 1),
    ]
    initialization_op_sequence, _, _ = OpSequence.from_instructions(initialization)
    initialization_op_sequence: OpSequence = initialization_op_sequence

    ly_call: List[Instruction] = [
        mi('LOAD_FAST', first_new_varname_index + 1),
        mi('CALL_FUNCTION', 0),
        mi('POP_TOP'),
    ]
    ly_call_op_sequence, _, _ = OpSequence.from_instructions(ly_call)
    ly_call_op_sequence: OpSequence = ly_call_op_sequence

    op_sequence.insert_op_sequence(0, initialization_op_sequence)

    # for
    FOR_ITER = opcode('FOR_ITER')

    index = len(initialization) - 1
    while True:
        index += 1
        if index >= len(op_sequence.op_sequence):
            break

        op, _, _, _, _, _ = op_sequence.op_sequence[index]
        if FOR_ITER == op:
            place_to_insert = index + 2
            op_sequence.insert_op_sequence(place_to_insert, ly_call_op_sequence)

    JUMP_ABSOLUTE = opcode('JUMP_ABSOLUTE')

    index = len(initialization) - 1
    while True:
        index += 1
        if index >= len(op_sequence.op_sequence):
            break

        op, _, _, _, _, _ = op_sequence.op_sequence[index]
        arg = op_sequence.get_arg(index)
        if JUMP_ABSOLUTE == op:
            place_to_insert = op_sequence.op_sequence_offset_map.new_by_original[arg_to_op_index(arg)]
            place_to_insert_op, place_to_insert_arg, _, _, _, _ = op_sequence.op_sequence[place_to_insert]
            if FOR_ITER == place_to_insert_op:
                continue

            op_sequence.insert_op_sequence(index, ly_call_op_sequence)
            index += len(ly_call_op_sequence)
    
    fix_labels(op_sequence, op_by_label)

    new_code_type = CodeType(
        fn_code.co_argcount,
        fn_code.co_posonlyargcount,
        fn_code.co_kwonlyargcount,
        co_nlocals,
        fn_code.co_stacksize,
        fn_code.co_flags,
        op_sequence.to_bytes(),
        tuple(co_consts),
        tuple(co_names),
        tuple(co_varnames),
        fn_code.co_filename,
        fn_code.co_name,
        fn_code.co_firstlineno,
        fn_code.co_lnotab,
        fn_code.co_freevars,
        fn_code.co_cellvars,
    )
    set_code(entity, new_code_type)
    return fn_code


def gly_patched(func: Callable) -> Callable:
    """Example:
        @gly_patched
        def func():
            for i in range(200):
                print(i)
                for j in range(100):
                    print(j)
            
            i = 100
            while i > 0:
                print(i)
                i -= 1

    Is equivalent to:
        from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly
        def func():
            ly = gly()
            for i in range(200):
                print(i)
                for j in range(100):
                    print(j)
                    ly()
                
                ly()
            
            i = 100
            while i > 0:
                print(i)
                i -= 1
                ly()

    Args:
        func (Callable): _description_

    Returns:
        Callable: _description_
    """    
    gly_patch(func)
    return func


glyp = gly_patched
