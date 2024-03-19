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
    'ASM',
    'c_uint8',
    'c_uint16',
    'c_uint32',
    'c_uint64',
    'c_float',
    'c_double',
    'asm_func',
    'asm_func_guard',
    'asm_funcs_guard',
    'run_asm',
    'run_asm__c_uint8',
    'run_asm__c_uint16',
    'run_asm__c_uint32',
    'run_asm__c_uint64',
    'run_asm__c_float',
    'run_asm__c_double',
    'run_asm__no_result',
    'asm_func_declaration',
    'declare_asm_function',
    'daf',
    'compile_asm_function',
    'caf',
    'run_asm_func',
]


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.2.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.modules_management.alternative_import import alt_import
with alt_import('cpuinfo') as cpuinfo:
    if cpuinfo is None:
        CPUINFO_PRESENT: bool = False
    else:
        CPUINFO_PRESENT = True

if not CPUINFO_PRESENT:
    raise RuntimeError('Package "py-cpuinfo" is not present. Please, install it. Version 7.0.0 or higher is required.')

if not hasattr(cpuinfo, 'ASM'):
    raise RuntimeError('Package "py-cpuinfo" is not the latest version. Please, update it. Version 7.0.0 or higher is required.')

import ctypes
from collections import namedtuple
from typing import Callable, Generator, Sequence, NamedTuple


class ASM(cpuinfo.ASM):
    def __init__(self, restype = None, argtypes = None, machine_code = None):
        # cpuinfo.ASM.__init__ has mutable default parameter which is not safe. So we fixing it here.
        argtypes = argtypes if argtypes is not None else ()
        machine_code = machine_code if machine_code is not None else []
        self.destroyed: bool = True
        super().__init__(restype, argtypes, machine_code)
    
    def compile(self):
        try:
            super().compile()
        finally:
            self.destroyed = False
    
    def __call__(self, *args):
        return self.func(*args)
    
    def free(self):
        if self.destroyed:
            return
        
        try:
            super().free()
        finally:
            self.destroyed = True
    
    def __del__(self):
        self.free()


c_uint8 = ctypes.c_uint8
c_uint16 = ctypes.c_uint16
c_uint32 = ctypes.c_uint32
c_uint64 = ctypes.c_uint64
c_float = ctypes.c_float
c_double = ctypes.c_double


def asm_func(restype = None, argtypes = None, machine_code = None) -> ASM:
    asm = ASM(restype, argtypes, machine_code)
    asm.compile()
    return asm


def asm_func_guard(asm: ASM) -> Generator[Callable, None, None]:
    try:
        yield asm.func
    finally:
        asm.free()


def asm_funcs_guard(asm_functions: Sequence[ASM]) -> Generator[Sequence[Callable], None, None]:
    try:
        yield [asm.func for asm in asm_functions]
    finally:
        for asm in asm_functions:
            asm.free()


def run_asm(restype, *machine_code):
    asm = ASM(restype, (), machine_code)
    asm.compile()
    try:
        retval = asm.func()
    finally:
        asm.free()
    
    return retval


def run_asm__c_uint8(*machine_code):
    return run_asm(c_uint8, *machine_code)


def run_asm__c_uint16(*machine_code):
    return run_asm(c_uint16, *machine_code)


def run_asm__c_uint32(*machine_code):
    return run_asm(c_uint32, *machine_code)


def run_asm__c_uint64(*machine_code):
    return run_asm(c_uint64, *machine_code)


def run_asm__c_float(*machine_code):
    return run_asm(c_float, *machine_code)


def run_asm__c_double(*machine_code):
    return run_asm(c_double, *machine_code)


def run_asm__no_result(*machine_code):
    return run_asm(None, *machine_code)


asm_func_declaration: NamedTuple = namedtuple('asm_func_declaration', ['restype', 'argtypes', 'machine_code'])  


def declare_asm_function(restype, argtypes, *machine_code) -> NamedTuple:
    return asm_func_declaration(restype, argtypes, machine_code)


daf = declare_asm_function


def compile_asm_function(declaration: NamedTuple) -> ASM:
    asm = ASM(declaration.restype, declaration.argtypes, declaration.machine_code)
    asm.compile()
    return asm


caf = compile_asm_function


def run_asm_func(declaration: NamedTuple, *args):
    asm = ASM(declaration.restype, declaration.argtypes, declaration.machine_code)
    asm.compile()
    try:
        retval = asm.func(*args)
    finally:
        asm.free()
    
    return retval
