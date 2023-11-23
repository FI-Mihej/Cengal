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


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""


__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.1.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from dis import Instruction, dis, get_instructions, _get_code_object, code_info, show_code, findlabels, _unpack_opargs, opmap
from opcode import hasjrel, hasjabs, opname, opmap, HAVE_ARGUMENT, EXTENDED_ARG
from operator import index

from xdis import extended_arg_val
from cengal.parallel_execution.coroutines.coro_scheduler import Interface
# from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly
from cengal.system import PYTHON_VERSION_INT
from enum import Enum
from functools import partial
from typing import Optional, Callable, List, Tuple, Dict, Set, Union, Any, Sequence
from types import CodeType
from copy import copy, deepcopy
from cengal.entities.copyable import CopyableMixin
from cengal.data_manipulation.front_triggerable_variable import FrontTriggerableVariableType, FrontTriggerableVariable
from cengal.performance_test_lib.performance_test_lib import test_performance
from cengal.code_flow_control.python_bytecode_manipulator import *
from json.encoder import _make_iterencode


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


def fake_gly_patch(entity: Callable) -> Callable:
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

    co_consts.extend((0, ('pprint',), 'ly = gly()', 'for ly()', 'while ly()'))
    co_names.extend(('pprint',))
    co_varnames.extend(('pprint',))
    co_nlocals = len(co_varnames)

    initialization: List[Instruction] = [
        mi('LOAD_CONST', first_new_const_index + 0),
        mi('LOAD_CONST', first_new_const_index + 1),
        mi('IMPORT_NAME', first_new_name_index + 0),
        mi('IMPORT_FROM', first_new_name_index + 0),
        mi('STORE_FAST', first_new_varname_index + 0),
        mi('POP_TOP'),
        mi('LOAD_FAST', first_new_varname_index + 0),
        mi('LOAD_CONST', first_new_const_index + 2),
        mi('CALL_FUNCTION', 1),
        mi('POP_TOP'),
    ]
    initialization_op_sequence, _, _ = OpSequence.from_instructions(initialization)
    initialization_op_sequence: OpSequence = initialization_op_sequence

    ly_call: List[Instruction] = [
        mi('LOAD_FAST', first_new_varname_index + 0),
        mi('LOAD_CONST', first_new_const_index + 3),
        mi('CALL_FUNCTION', 1),
        mi('POP_TOP'),
    ]
    ly_call_op_sequence, _, _ = OpSequence.from_instructions(ly_call)
    ly_call_op_sequence: OpSequence = ly_call_op_sequence

    ly_call_while: List[Instruction] = [
        mi('LOAD_FAST', first_new_varname_index + 0),
        mi('LOAD_CONST', first_new_const_index + 4),
        mi('CALL_FUNCTION', 1),
        mi('POP_TOP'),
    ]
    ly_call_while_op_sequence, _, _ = OpSequence.from_instructions(ly_call_while)
    ly_call_while_op_sequence: OpSequence = ly_call_while_op_sequence

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
    
    # # while
    # JUMP_ABSOLUTE = opcode('JUMP_ABSOLUTE')

    # index = len(initialization) - 1
    # while True:
    #     index += 1
    #     if index >= len(op_sequence.op_sequence):
    #         break

    #     op, _, _, _, _, _ = op_sequence.op_sequence[index]
    #     arg = op_sequence.get_arg(index)
    #     if JUMP_ABSOLUTE == op:
    #         place_to_insert = op_sequence.op_sequence_offset_map.new_by_original[arg_to_op_index(arg)]
    #         place_to_insert_op, place_to_insert_arg, _, _, _, _ = op_sequence.op_sequence[index]
    #         if FOR_ITER == place_to_insert_op:
    #             continue

    #         op_sequence.insert_op_sequence(place_to_insert, ly_call_while_op_sequence)
    #         index += len(ly_call_while_op_sequence)
    
    # while
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

            op_sequence.insert_op_sequence(index, ly_call_while_op_sequence)
            index += len(ly_call_while_op_sequence)
    
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


def sample1():
    for i in range(40):
        print(i)


def sample2():
    k = 40
    print(f'{k}')
    for i in range(k):
        t = i ** 2 + k
        print(t)


def sample3(interface: Interface):
    k = 40
    print(f'{k}')
    for i in range(k):
        t = i ** 2 + k
        print(t)


def sample4(interface: Interface, data: str):
    k = 40
    print(f'{k}')
    for i in range(k):
        t = i ** 2 + k
        print(t)


def sample1_gly():
    from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly
    ly = gly()
    for i in range(40):
        ly()
        print(i)

    i = -1
    while True:
        ly()
        i += 1
        t = i ** 2 + k
        print(t)


def sample2_gly():
    from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly
    ly = gly()
    k = 40
    print(f'{k}')
    for i in range(k):
        ly()
        t = i ** 2 + k
        print(t)

    i = -1
    while True:
        ly()
        i += 1
        t = i ** 2 + k
        print(t)


def sample3_gly(interface: Interface):
    from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly
    ly = gly()
    k = 40
    print(f'{k}')
    for i in range(k):
        ly()
        t = i ** 2 + k
        print(t)

    i = -1
    while True:
        ly()
        i += 1
        t = i ** 2 + k
        print(t)


def sample4_gly(interface: Interface, data: str):
    from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly
    ly = gly()
    k = 40
    print(f'{k}')
    for i in range(k):
        ly()
        t = i ** 2 + k
        print(t)

    i = -1
    while True:
        ly()
        i += 1
        t = i ** 2 + k
        print(t)


def sample5_gly(interface: Interface, data: str, arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6, arg_7, arg_8, arg_9, arg_10, arg_11, arg_12, arg_13, arg_14, arg_15, arg_16, arg_17, arg_18, arg_19, arg_20, arg_21, arg_22, arg_23, arg_24, arg_25, arg_26, arg_27, arg_28, arg_29, arg_30, arg_31, arg_32, arg_33, arg_34, arg_35, arg_36, arg_37, arg_38, arg_39, arg_40, arg_41, arg_42, arg_43, arg_44, arg_45, arg_46, arg_47, arg_48, arg_49, arg_50, arg_51, arg_52, arg_53, arg_54, arg_55, arg_56, arg_57, arg_58, arg_59, arg_60, arg_61, arg_62, arg_63, arg_64, arg_65, arg_66, arg_67, arg_68, arg_69, arg_70, arg_71, arg_72, arg_73, arg_74, arg_75, arg_76, arg_77, arg_78, arg_79, arg_80, arg_81, arg_82, arg_83, arg_84, arg_85, arg_86, arg_87, arg_88, arg_89, arg_90, arg_91, arg_92, arg_93, arg_94, arg_95, arg_96, arg_97, arg_98, arg_99, arg_100, arg_101, arg_102, arg_103, arg_104, arg_105, arg_106, arg_107, arg_108, arg_109, arg_110, arg_111, arg_112, arg_113, arg_114, arg_115, arg_116, arg_117, arg_118, arg_119, arg_120, arg_121, arg_122, arg_123, arg_124, arg_125, arg_126, arg_127, arg_128, arg_129, arg_130, arg_131, arg_132, arg_133, arg_134, arg_135, arg_136, arg_137, arg_138, arg_139, arg_140, arg_141, arg_142, arg_143, arg_144, arg_145, arg_146, arg_147, arg_148, arg_149, arg_150, arg_151, arg_152, arg_153, arg_154, arg_155, arg_156, arg_157, arg_158, arg_159, arg_160, arg_161, arg_162, arg_163, arg_164, arg_165, arg_166, arg_167, arg_168, arg_169, arg_170, arg_171, arg_172, arg_173, arg_174, arg_175, arg_176, arg_177, arg_178, arg_179, arg_180, arg_181, arg_182, arg_183, arg_184, arg_185, arg_186, arg_187, arg_188, arg_189, arg_190, arg_191, arg_192, arg_193, arg_194, arg_195, arg_196, arg_197, arg_198, arg_199, arg_200, arg_201, arg_202, arg_203, arg_204, arg_205, arg_206, arg_207, arg_208, arg_209, arg_210, arg_211, arg_212, arg_213, arg_214, arg_215, arg_216, arg_217, arg_218, arg_219, arg_220, arg_221, arg_222, arg_223, arg_224, arg_225, arg_226, arg_227, arg_228, arg_229, arg_230, arg_231, arg_232, arg_233, arg_234, arg_235, arg_236, arg_237, arg_238, arg_239, arg_240, arg_241, arg_242, arg_243, arg_244, arg_245, arg_246, arg_247, arg_248, arg_249, arg_250, arg_251, arg_252, arg_253, arg_254, arg_255, arg_256, arg_257, arg_258, arg_259, arg_260, arg_261, arg_262, arg_263, arg_264, arg_265, arg_266, arg_267, arg_268, arg_269, arg_270, arg_271, arg_272, arg_273, arg_274, arg_275, arg_276, arg_277, arg_278, arg_279, arg_280, arg_281, arg_282, arg_283, arg_284, arg_285, arg_286, arg_287, arg_288, arg_289, arg_290, arg_291, arg_292, arg_293, arg_294, arg_295, arg_296, arg_297, arg_298, arg_299):
    from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly
    ly = gly()
    k = 40
    print(f'{k}')
    for i in range(k):
        ly()
        t = i ** 2 + k
        print(t)

    i = -1
    while True:
        ly()
        i += 1
        t = i ** 2 + k
        print(t)


def sample6_gly(interface: Interface, data: str):
    from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly
    ly = gly()
    k = 40
    print(f'{k}')
    if input():
        d = k + 2
    
    for i in range(k):
        ly()
        t = i ** 2 + k
        print(t)

    i = -1
    while i < 4:
        ly()
        i += 1
        t = i ** 2 + k
        print(t)


def sample7(interface: Interface, data: str):
    k = 40
    print(f'{k}')
    if input('Input: '):
        d = k + 2
    
    for i in range(k):
        t = i ** 2 + k
        print(t)

    i = -1
    while i < k:
        i += 1
        t = i ** 2 + k
        print(t)


sample7__original_code = fake_gly_patch(sample7)
sample7_test_fake_gly_patch = sample7
# set_code(sample7, sample7__original_code)
# sample7_test_fake_gly_patch = sample7


def sample7_fake_gly(interface: Interface, data: str):
    from pprint import pprint
    pprint('ly = gly()')

    k = 40
    print(f'{k}')
    if input():
        d = k + 2
    
    for i in range(k):
        pprint('for ly()')
        t = i ** 2 + k
        print(t)

    i = -1
    while i < k:
        pprint('while ly()')
        i += 1
        t = i ** 2 + k
        print(t)


def main():
    functions_for_dis = [
        # # print,
        # sample1,
        # sample1_gly,
        # sample2,
        # sample2_gly,
        # sample3,
        # sample3_gly,
        # sample4,
        # sample4_gly,
        # sample5_gly,
        # sample6_gly,
        # sample7,
        # sample7_fake_gly,
        # sample7_test_fake_gly_patch,
        _make_iterencode
    ]
    for func_for_dis in functions_for_dis:
        print()
        print('==========================')
        print(f'>>> {str(func_for_dis)}')
        code_bytes = _get_code_object(func_for_dis).co_code
        print(code_bytes)
        # print('---')
        # print(code_bytes[0:6])
        print('---')
        dis(func_for_dis)
        print('---')
        print(find_ops_with_labels(code_bytes))
        print('---')
        show_code(func_for_dis)
        print('---')
        code_info(func_for_dis)
        print('---')
        
        # dis(func_for_dis)
        # print(code_info(func_for_dis))
        # show_code(func_for_dis)
        for instruction in get_instructions(func_for_dis):
            print(instruction)


if __name__ == '__main__':
    main()
    # sample7_test_fake_gly_patch(None, list())
