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


__all__ = ['prepare_cflags', 'append_cflags', 'concat_cflags', 'prepare_compile_time_env']


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


from typing import Dict, Any, Tuple, Union
from os import environ
try:
    from os import uname
    uname_sysname: str = uname().sysname
    uname_machine: str = uname().machine
except ImportError:
    from platform import uname
    uname_sysname: str = uname().system
    uname_machine: str = uname().machine

from cengal.hardware.info.cpu import cpu_info
from cengal.build_tools.current_compiler import compiler_type, compiler_name
from cengal.system import (
    PYTHON_IMPLEMENTATION,
    PYTHON_VERSION,
    PYTHON_VERSION_STR,
    PYTHON_VERSION_INT,
    IS_RUNNING_IN_PYCHARM,
    RAW_OS_PLATFORM,
    OS_API_TYPE,
    OS_TYPE,
    IS_RUNNING_IN_EMSCRIPTEN,
    IS_RUNNING_IN_WASI,
    IS_RUNNING_IN_PYODIDE,
    IS_BUILDING_FOR_PYODIDE,
    IS_INSIDE_OR_FOR_WEB_BROWSER,
)


def append_cflags(cflags_list: list):
    if 'msvc' == compiler_type:
        compiler_flags_env_var_name = 'CL'
    else:
        compiler_flags_env_var_name = 'CFLAGS'

    environ[compiler_flags_env_var_name] = f'{environ.get(compiler_flags_env_var_name, str())} {" ".join(cflags_list)}'


def concat_cflags(cflags: str):
    if 'msvc' == compiler_type:
        compiler_flags_env_var_name = 'CL'
    else:
        compiler_flags_env_var_name = 'CFLAGS'

    environ[compiler_flags_env_var_name] = f'{environ.get(compiler_flags_env_var_name, str())} {cflags}'


def prepare_cflags(additional_cflags: Dict[str, Tuple[bool, Union[str, int]]]):
    if 'msvc' == compiler_type:
        macros_string_template: str = '/D{macro_name}="{macro_value}"'
        macros_flag_template: str = '/D{macro_name}={macro_value}'
    else:
        macros_string_template: str = '-D{macro_name}=\\"{macro_value}\\"'
        macros_flag_template: str = '-D{macro_name}={macro_value}'
    
    macro_flags_list = [
        # Cython
        macros_string_template.format(macro_name='UNAME_SYSNAME', macro_value=uname_sysname),  # see: https://en.wikipedia.org/wiki/Uname
        macros_string_template.format(macro_name='UNAME_MACHINE', macro_value=uname_machine),  # see: https://en.wikipedia.org/wiki/Uname
        macros_string_template.format(macro_name='CPU_ARCH', macro_value=cpu_info().arch),  # 'X86_32', 'X86_64', 'ARM_8', 'ARM_7', 'PPC_32', 'PPC_64', 'SPARC_32', 'SPARC_64', 'S390X', 'MIPS_32', 'MIPS_64', 'RISCV_32', 'RISCV_64'
        macros_string_template.format(macro_name='CPU_ARCH_RAW_STRING', macro_value=cpu_info().arch_string_raw),
        macros_string_template.format(macro_name='CPU_BITS', macro_value=cpu_info().bits),  # '32', '64'
        macros_string_template.format(macro_name='IS_X86', macro_value=int(cpu_info().is_x86)),  # 'True', 'False'
        macros_string_template.format(macro_name='IS_ARM', macro_value=int(cpu_info().is_arm)),  # 'True', 'False'
        macros_string_template.format(macro_name='COMPILER_TYPE', macro_value=compiler_type),  # 'gcc', 'msvc', 'clang', 'icc', 'llvm', 'intel', 'arm', 'mingw', 'unknown'
        macros_string_template.format(macro_name='COMPILER_NAME', macro_value=compiler_name),  # 'x86_64-linux-gnu-gcc_-pthread'
        macros_string_template.format(macro_name='PYTHON_IMPLEMENTATION', macro_value=PYTHON_IMPLEMENTATION),  # 'CPython', 'PyPy', 'IronPython', 'Jython'
        macros_string_template.format(macro_name='PYTHON_VERSION_STR', macro_value=PYTHON_VERSION_STR),  # '3.5.1', ...
        macros_string_template.format(macro_name='PYTHON_VERSION_MAJOR', macro_value=PYTHON_VERSION_INT.major),  # '3', ...
        macros_string_template.format(macro_name='PYTHON_VERSION_MINOR', macro_value=PYTHON_VERSION_INT.minor),  # '5', ...
        macros_string_template.format(macro_name='PYTHON_VERSION_MICRO', macro_value=PYTHON_VERSION_INT.micro),  # '1', ...
        macros_string_template.format(macro_name='IS_RUNNING_IN_PYCHARM', macro_value=IS_RUNNING_IN_PYCHARM),  # 'True', 'False'
        macros_string_template.format(macro_name='RAW_OS_PLATFORM', macro_value=RAW_OS_PLATFORM),  # 'emscripten', 'wasi', 'darwin', 'win32', 'cygwin', 'linux', 'linux2', 'linux3', 'darwin', 'freebsd8', 'aix', aix5', 'aix7', ...
        macros_string_template.format(macro_name='OS_API_TYPE', macro_value=OS_API_TYPE),  # 'posix', 'nt', 'java'. Android and iOS will return 'posix'.
        macros_string_template.format(macro_name='OS_TYPE', macro_value=OS_TYPE),  # 'Linux', 'Windows', 'Darwin'
        macros_string_template.format(macro_name='IS_RUNNING_IN_EMSCRIPTEN', macro_value=IS_RUNNING_IN_EMSCRIPTEN),  # 'True', 'False'
        macros_string_template.format(macro_name='IS_RUNNING_IN_WASI', macro_value=IS_RUNNING_IN_WASI),  # 'True', 'False'
        macros_string_template.format(macro_name='IS_RUNNING_IN_PYODIDE', macro_value=IS_RUNNING_IN_PYODIDE),  # 'True', 'False'
        macros_string_template.format(macro_name='IS_BUILDING_FOR_PYODIDE', macro_value=IS_BUILDING_FOR_PYODIDE),  # 'True', 'False'
        macros_string_template.format(macro_name='IS_INSIDE_OR_FOR_WEB_BROWSER', macro_value=IS_INSIDE_OR_FOR_WEB_BROWSER),  # 'True', 'False'

        # C preprocessor
        macros_flag_template.format(macro_name='C__PYTHON_VERSION_MAJOR', macro_value=PYTHON_VERSION_INT.major),  # '3', ...
        macros_flag_template.format(macro_name='C__PYTHON_VERSION_MINOR', macro_value=PYTHON_VERSION_INT.minor),  # '5', ...
        macros_flag_template.format(macro_name='C__PYTHON_VERSION_MICRO', macro_value=PYTHON_VERSION_INT.micro),  # '1', ...
    ]
    for key, data in additional_cflags.items():
        is_flag, value = data
        if is_flag:
            macro_flags_list.append(macros_flag_template.format(macro_name=key, macro_value=value))
        else:
            macro_flags_list.append(macros_string_template.format(macro_name=key, macro_value=value))

    
    # C preprocessor
    if 32 == cpu_info().bits:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__32_bit_CPU', macro_value=1))
    
    if 64 == cpu_info().bits:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__64_bit_CPU', macro_value=1))

    if cpu_info().is_x86:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__IS_X86', macro_value=1))
    
    if cpu_info().is_arm:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__IS_ARM', macro_value=1))

    if 'X86_32' == cpu_info().arch:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__X86_32', macro_value=1))
    elif 'X86_64' == cpu_info().arch:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__X86_64', macro_value=1))
    elif 'ARM_8' == cpu_info().arch:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__ARM_8', macro_value=1))
    elif 'ARM_7' == cpu_info().arch:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__ARM_7', macro_value=1))
    elif 'PPC_32' == cpu_info().arch:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__PPC_32', macro_value=1))
    elif 'PPC_64' == cpu_info().arch:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__PPC_64', macro_value=1))
    elif 'SPARC_32' == cpu_info().arch:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__SPARC_32', macro_value=1))
    elif 'SPARC_64' == cpu_info().arch:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__SPARC_64', macro_value=1))
    elif 'S390X' == cpu_info().arch:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__S390X', macro_value=1))
    elif 'MIPS_32' == cpu_info().arch:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__MIPS_32', macro_value=1))
    elif 'MIPS_64' == cpu_info().arch:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__MIPS_64', macro_value=1))
    elif 'RISCV_32' == cpu_info().arch:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__RISCV_32', macro_value=1))
    elif 'RISCV_64' == cpu_info().arch:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__RISCV_64', macro_value=1))
    
    if 'CPython' == PYTHON_IMPLEMENTATION:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__CPython', macro_value=1))
    elif 'PyPy' == PYTHON_IMPLEMENTATION:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__PyPy', macro_value=1))
    elif 'IronPython' == PYTHON_IMPLEMENTATION:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__IronPython', macro_value=1))
    elif 'Jython' == PYTHON_IMPLEMENTATION:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__Jython', macro_value=1))
    
    if 'gcc' == compiler_type:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__gcc', macro_value=1))
    elif 'msvc' == compiler_type:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__msvc', macro_value=1))
    elif 'clang' == compiler_type:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__clang', macro_value=1))
    elif 'icc' == compiler_type:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__icc', macro_value=1))
    elif 'llvm' == compiler_type:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__llvm', macro_value=1))
    elif 'intel' == compiler_type:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__intel', macro_value=1))
    elif 'arm' == compiler_type:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__arm', macro_value=1))
    elif 'mingw' == compiler_type:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__mingw', macro_value=1))
    elif 'unknown' == compiler_type:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__unknown', macro_value=1))
    
    if 'Linux' == OS_TYPE:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__Linux', macro_value=1))
    elif 'Windows' == OS_TYPE:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__Windows', macro_value=1))
    elif 'Darwin' == OS_TYPE:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__Darwin', macro_value=1))
    
    if 'posix' == OS_API_TYPE:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__posix', macro_value=1))
    elif 'nt' == OS_API_TYPE:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__nt', macro_value=1))
    elif 'java' == OS_API_TYPE:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__java', macro_value=1))
    
    if IS_RUNNING_IN_EMSCRIPTEN:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__IS_RUNNING_IN_EMSCRIPTEN', macro_value=1))
    
    if IS_RUNNING_IN_WASI:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__IS_RUNNING_IN_WASI', macro_value=1))
    
    if IS_RUNNING_IN_PYODIDE:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__IS_RUNNING_IN_PYODIDE', macro_value=1))
    
    if IS_BUILDING_FOR_PYODIDE:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__IS_BUILDING_FOR_PYODIDE', macro_value=1))
    
    if IS_INSIDE_OR_FOR_WEB_BROWSER:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__IS_INSIDE_OR_FOR_WEB_BROWSER', macro_value=1))
    
    if IS_RUNNING_IN_PYCHARM:
        macro_flags_list.append(macros_flag_template.format(macro_name='C__IS_RUNNING_IN_PYCHARM', macro_value=1))
    
    append_cflags(macro_flags_list)


def prepare_compile_time_env(additional_cflags: Dict[str, Tuple[bool, Union[str, int]]]):
    result = {
        'UNAME_SYSNAME': uname_sysname,  # see: https://en.wikipedia.org/wiki/Uname
        'UNAME_MACHINE': uname_machine,  # see: https://en.wikipedia.org/wiki/Uname
        'CPU_ARCH': cpu_info().arch,  # 'X86_32', 'X86_64', 'ARM_8', 'ARM_7', 'PPC_32', 'PPC_64', 'SPARC_32', 'SPARC_64', 'S390X', 'MIPS_32', 'MIPS_64', 'RISCV_32', 'RISCV_64'
        'CPU_ARCH_RAW_STRING': cpu_info().arch_string_raw,
        'CPU_BITS': cpu_info().bits,  # '32', '64'
        'IS_X86': int(cpu_info().is_x86),  # 'True', 'False'
        'IS_ARM': int(cpu_info().is_arm),  # 'True', 'False'
        'COMPILER_TYPE': compiler_type,  # 'gcc', 'msvc', 'clang', 'icc', 'llvm', 'intel', 'arm', 'mingw', 'unknown'
        'COMPILER_NAME': compiler_name,  # 'x86_64-linux-gnu-gcc_-pthread'
        'PYTHON_IMPLEMENTATION': PYTHON_IMPLEMENTATION,  # 'CPython', 'PyPy', 'IronPython', 'Jython'
        'PYTHON_VERSION_STR': PYTHON_VERSION_STR,  # '3.5.1', ...
        'PYTHON_VERSION_MAJOR': PYTHON_VERSION_INT.major,  # '3', ...
        'PYTHON_VERSION_MINOR': PYTHON_VERSION_INT.minor,  # '5', ...
        'PYTHON_VERSION_MICRO': PYTHON_VERSION_INT.micro,  # '1', ...
        'IS_RUNNING_IN_PYCHARM': IS_RUNNING_IN_PYCHARM,  # 'True', 'False'
        'RAW_OS_PLATFORM': RAW_OS_PLATFORM,  # 'emscripten', 'wasi', 'darwin', 'win32', 'cygwin', 'linux', 'linux2', 'linux3', 'darwin', 'freebsd8', 'aix', aix5', 'aix7', ...
        'OS_API_TYPE': OS_API_TYPE,  # 'posix', 'nt', 'java'. Android and iOS will return 'posix'.
        'OS_TYPE': OS_TYPE,  # 'Linux', 'Windows', 'Darwin'
        'IS_RUNNING_IN_EMSCRIPTEN': IS_RUNNING_IN_EMSCRIPTEN,  # 'True', 'False'
        'IS_RUNNING_IN_WASI': IS_RUNNING_IN_WASI,  # 'True', 'False'
        'IS_RUNNING_IN_PYODIDE': IS_RUNNING_IN_PYODIDE,  # 'True', 'False'
        'IS_BUILDING_FOR_PYODIDE': IS_BUILDING_FOR_PYODIDE,  # 'True', 'False'
        'IS_INSIDE_OR_FOR_WEB_BROWSER': IS_INSIDE_OR_FOR_WEB_BROWSER,  # 'True', 'False'
    }
    result.update(additional_cflags)
    return result
