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
    'append_cflags', 
    'concat_cflags', 
    'wrap_definition_text', 
    'wrap_definition_text_raw', 
    'prepare_definition_value', 
    'prepare_definition_value_raw', 
    'convert_value_to_flag', 
    'convert_value_to_text', 
    'prepare_definition', 
    'list_to_dict', 
    'dict_of_tuples_to_dict', 
    'adjust_definition_names', 
    'prepare_cflags', 
    'prepare_cflags_dict', 
    'prepare_compile_time_env', 
    'prepare_compile_time_flags',
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
from cengal.os.execute import escape_text, escape_param
from cengal.build_tools.current_compiler import compiler_type, compiler_name, compiler_string
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
    CENGAL_VERSION_STR,
    CENGAL_VERSION_MAJOR_STR,
    CENGAL_VERSION_MINOR_STR,
    CENGAL_VERSION_MICRO_STR,
    CENGAL_VERSION_MAJOR,
    CENGAL_VERSION_MINOR,
    CENGAL_VERSION_MICRO,
)
from typing import Set, Sequence, Optional, Sequence, List


def append_cflags(cflags_list: list):
    if 'msvc' == compiler_type:
        compiler_flags_env_var_name = 'CL'
    else:
        compiler_flags_env_var_name = 'CFLAGS'

    environ[compiler_flags_env_var_name] = ' '.join((environ.get(compiler_flags_env_var_name, str()), " ".join(cflags_list)))


def concat_cflags(cflags: str):
    if 'msvc' == compiler_type:
        compiler_flags_env_var_name = 'CL'
    else:
        compiler_flags_env_var_name = 'CFLAGS'

    environ[compiler_flags_env_var_name] = ' '.join((environ.get(compiler_flags_env_var_name, str()), cflags))


def wrap_definition_text(text: str) -> str:
    if 'msvc' == compiler_type:
        return escape_param(f'\\"{text}\\"')
    else:
        return f'\\"{escape_param(text)}\\"'


def wrap_definition_text_raw(text: str) -> str:
    return f'"{text}"'


def prepare_definition_value(value: Union[None, bool, int, str]) -> str:
    if isinstance(value, bool):
        value = str(value)
    
    if value is None:
        return None
    elif isinstance(value, int):
        return value
    elif isinstance(value, str):
        return wrap_definition_text(value)
    else:
        return wrap_definition_text(f'{value}')


def prepare_definition_value_raw(value: Union[None, bool, int, str]) -> str:
    if isinstance(value, bool):
        value = str(value)
    
    if value is None:
        return None
    elif isinstance(value, int):
        return value
    elif isinstance(value, str):
        return wrap_definition_text_raw(value)
    else:
        return wrap_definition_text_raw(f'{value}')


def wrap_definition_pair(name: str, value: Any) -> str:
    if 'msvc' == compiler_type:
        return f'/D{name}={value}' if value is not None else f'/D{name}'
    else:
        return f'-D{name}={value}' if value is not None else f'-D{name}'


def convert_value_to_flag(value: Union[None, bool, int, str]) -> int:
    if value is None:
        return None
    
    try:
        return int(value)
    except:
        return 1


def convert_value_to_text(value: Union[None, bool, int, str]) -> str:
    return f'{value}'


def prepare_definition(name: str, value: Optional[Union[bool, int, str]] = None) -> str:
    return wrap_definition_pair(name, prepare_definition_value(value))


def list_to_dict(additional_cflags: Optional[Sequence[str]] = None) -> Dict[str, Union[None, bool, int, str]]:
    additional_cflags = dict() if additional_cflags is None else additional_cflags
    if not isinstance(additional_cflags, dict):
        additional_cflags = {name: None for name in additional_cflags}
    
    return additional_cflags


def dict_of_tuples_to_dict(additional_cflags: Optional[Dict[str, Tuple[bool, Union[None, bool, str, int]]]] = None) -> Dict[str, Union[None, bool, int, str]]:
    additional_cflags = dict() if additional_cflags is None else additional_cflags
    adjusted_additional_cflags: Dict[str, Union[None, bool, int, str]] = dict()
    for name, value_info in additional_cflags.items():
        if isinstance(value_info, tuple):
            is_flag, value = value_info
            value = convert_value_to_flag(value) if is_flag else convert_value_to_text(value)
        else:
            value = value_info
        
        adjusted_additional_cflags[name] = value
    
    return adjusted_additional_cflags


def adjust_definition_names(definitions: Dict[str, Union[None, bool, int, str]], flag_name_prefix: str = None, definition_name_prefix: str = None) -> Dict[str, Union[None, bool, int, str]]:
    flag_name_prefix = str() if flag_name_prefix is None else flag_name_prefix
    definition_name_prefix = str() if definition_name_prefix is None else definition_name_prefix
    adjusted_definitions: Dict[str, Union[None, bool, int, str]] = dict()
    for name, value in definitions.items():
        if value is None:
            name = f'{flag_name_prefix}{name}'
        else:
            name = f'{definition_name_prefix}{name}'
        
        adjusted_definitions[name] = value
    
    return adjusted_definitions


def prepare_cflags(additional_cflags: Optional[Union[Sequence[str], Dict[str, Union[Union[None, bool, int, str], Tuple[bool, Union[None, bool, str, int]]]]]] = None) -> List[Union[None, int, str]]:
    adjusted_additional_cflags: Dict[str, Union[None, bool, int, str]] = dict_of_tuples_to_dict(list_to_dict(additional_cflags))
    flags: Dict[str, None] = adjust_definition_names(list_to_dict(prepare_compile_time_flags()), 'CF_', 'CD_')  # CF is Cengal Flag; CD is Cengal Definition
    definitions: Dict[str, Union[None, bool, int, str]] = adjust_definition_names(prepare_compile_time_env(), 'CF_', 'CD_')  # CF is Cengal Flag; CD is Cengal Definition
    definitions.update(flags)
    definitions.update(adjusted_additional_cflags)
    params: List[Union[None, int, str]] = [prepare_definition(name, value) for name, value in definitions.items()]
    
    # from pprint import pprint
    # print('<<< PREPARE_CFLAGS: >>>')
    # pprint(params)
    append_cflags(params)
    return params


def prepare_cflags_dict(additional_cflags: Optional[Union[Sequence[str], Dict[str, Union[Union[None, bool, int, str], Tuple[bool, Union[None, bool, str, int]]]]]] = None) -> Dict[str, Union[None, bool, int, str]]:
    adjusted_additional_cflags: Dict[str, Union[None, bool, int, str]] = dict_of_tuples_to_dict(list_to_dict(additional_cflags))
    flags: Dict[str, None] = adjust_definition_names(list_to_dict(prepare_compile_time_flags()), 'CF_', 'CD_')  # CF is Cengal Flag; CD is Cengal Definition
    definitions: Dict[str, Union[None, bool, int, str]] = adjust_definition_names(prepare_compile_time_env(), 'CF_', 'CD_')  # CF is Cengal Flag; CD is Cengal Definition
    definitions.update(flags)
    definitions.update(adjusted_additional_cflags)
    result: Dict[str, Union[None, bool, int, str]] = {name: prepare_definition_value_raw(value) for name, value in definitions.items()}
    
    # from pprint import pprint
    # print('<<< PREPARE_CFLAGS_DICT: >>>')
    # pprint(result)
    return result


def prepare_compile_time_env(additional_cflags: Optional[Union[Sequence[str], Dict[str, Union[Union[None, bool, int, str], Tuple[bool, Union[None, bool, str, int]]]]]] = None):
    result = {
        'UNAME_SYSNAME': uname_sysname,  # see: https://en.wikipedia.org/wiki/Uname
        'UNAME_MACHINE': uname_machine,  # see: https://en.wikipedia.org/wiki/Uname
        'CPU_ARCH': cpu_info().arch,  # 'X86_32', 'X86_64', 'ARM_8', 'ARM_7', 'PPC_32', 'PPC_64', 'SPARC_32', 'SPARC_64', 'S390X', 'MIPS_32', 'MIPS_64', 'RISCV_32', 'RISCV_64'
        'CPU_ARCH_RAW_STRING': cpu_info().arch_string_raw,
        'CPU_BITS': cpu_info().bits,  # '32', '64'
        'IS_X86_BOOL': cpu_info().is_x86,  # 'True', 'False'
        'IS_ARM_BOOL': cpu_info().is_arm,  # 'True', 'False'
        'IS_X86': int(cpu_info().is_x86),  # '1', '0'
        'IS_ARM': int(cpu_info().is_arm),  # '1', '0'
        'COMPILER_TYPE': compiler_type,  # 'gcc', 'msvc', 'clang', 'icc', 'llvm', 'intel', 'arm', 'mingw', 'unknown'
        'COMPILER_NAME': compiler_name,  # 'x86_64-linux-gnu-gcc'
        'COMPILER_STRING': compiler_string,  # 'x86_64-linux-gnu-gcc -pthread'
        'PYTHON_IMPLEMENTATION': PYTHON_IMPLEMENTATION,  # 'CPython', 'PyPy', 'IronPython', 'Jython'
        'PYTHON_VERSION_STR': PYTHON_VERSION_STR,  # '3.5.1', ...
        'PYTHON_VERSION_MAJOR_STR': str(PYTHON_VERSION_INT.major),  # '3', ...
        'PYTHON_VERSION_MINOR_STR': str(PYTHON_VERSION_INT.minor),  # '5', ...
        'PYTHON_VERSION_MICRO_STR': str(PYTHON_VERSION_INT.micro),  # '1', ...
        'PYTHON_VERSION_MAJOR': PYTHON_VERSION_INT.major,  # '3', ...
        'PYTHON_VERSION_MINOR': PYTHON_VERSION_INT.minor,  # '5', ...
        'PYTHON_VERSION_MICRO': PYTHON_VERSION_INT.micro,  # '1', ...
        'IS_RUNNING_IN_PYCHARM_BOOL': IS_RUNNING_IN_PYCHARM,  # 'True', 'False'
        'IS_RUNNING_IN_PYCHARM': int(IS_RUNNING_IN_PYCHARM),  # '1', '0'
        'RAW_OS_PLATFORM': RAW_OS_PLATFORM,  # 'emscripten', 'wasi', 'darwin', 'win32', 'cygwin', 'linux', 'linux2', 'linux3', 'darwin', 'freebsd8', 'aix', aix5', 'aix7', ...
        'OS_API_TYPE': OS_API_TYPE,  # 'posix', 'nt', 'java'. Android and iOS will return 'posix'.
        'OS_TYPE': OS_TYPE,  # 'Linux', 'Windows', 'Darwin'
        'IS_RUNNING_IN_EMSCRIPTEN_BOOL': IS_RUNNING_IN_EMSCRIPTEN,  # 'True', 'False'
        'IS_RUNNING_IN_WASI_BOOL': IS_RUNNING_IN_WASI,  # 'True', 'False'
        'IS_RUNNING_IN_PYODIDE_BOOL': IS_RUNNING_IN_PYODIDE,  # 'True', 'False'
        'IS_BUILDING_FOR_PYODIDE_BOOL': IS_BUILDING_FOR_PYODIDE,  # 'True', 'False'
        'IS_INSIDE_OR_FOR_WEB_BROWSER_BOOL': IS_INSIDE_OR_FOR_WEB_BROWSER,  # 'True', 'False'
        'IS_RUNNING_IN_EMSCRIPTEN': int(IS_RUNNING_IN_EMSCRIPTEN),  # '1', '0'
        'IS_RUNNING_IN_WASI': int(IS_RUNNING_IN_WASI),  # '1', '0'
        'IS_RUNNING_IN_PYODIDE': int(IS_RUNNING_IN_PYODIDE),  # '1', '0'
        'IS_BUILDING_FOR_PYODIDE': int(IS_BUILDING_FOR_PYODIDE),  # '1', '0'
        'IS_INSIDE_OR_FOR_WEB_BROWSER': int(IS_INSIDE_OR_FOR_WEB_BROWSER),  # '1', '0'
        'CENGAL_VERSION_STR': CENGAL_VERSION_STR,
        'CENGAL_VERSION_MAJOR_STR': CENGAL_VERSION_MAJOR_STR,
        'CENGAL_VERSION_MINOR_STR': CENGAL_VERSION_MINOR_STR,
        'CENGAL_VERSION_MICRO_STR': CENGAL_VERSION_MICRO_STR,
        'CENGAL_VERSION_MAJOR': CENGAL_VERSION_MAJOR,
        'CENGAL_VERSION_MINOR': CENGAL_VERSION_MINOR,
        'CENGAL_VERSION_MICRO': CENGAL_VERSION_MICRO,
    }
    result.update(dict_of_tuples_to_dict(list_to_dict(additional_cflags)))
    return result


def prepare_compile_time_flags(additional_cflags: Sequence[str] = None):
    additional_cflags = [] if additional_cflags is None else additional_cflags
    macro_flags_list: Set = set()

    if 32 == cpu_info().bits:
        macro_flags_list.add('32_bit_CPU')
    
    if 64 == cpu_info().bits:
        macro_flags_list.add('64_bit_CPU')

    if cpu_info().is_x86:
        macro_flags_list.add('IS_X86')
    
    if cpu_info().is_arm:
        macro_flags_list.add('IS_ARM')

    if 'X86_32' == cpu_info().arch:
        macro_flags_list.add('X86_32')
    elif 'X86_64' == cpu_info().arch:
        macro_flags_list.add('X86_64')
    elif 'ARM_8' == cpu_info().arch:
        macro_flags_list.add('ARM_8')
    elif 'ARM_7' == cpu_info().arch:
        macro_flags_list.add('ARM_7')
    elif 'PPC_32' == cpu_info().arch:
        macro_flags_list.add('PPC_32')
    elif 'PPC_64' == cpu_info().arch:
        macro_flags_list.add('PPC_64')
    elif 'SPARC_32' == cpu_info().arch:
        macro_flags_list.add('SPARC_32')
    elif 'SPARC_64' == cpu_info().arch:
        macro_flags_list.add('SPARC_64')
    elif 'S390X' == cpu_info().arch:
        macro_flags_list.add('S390X')
    elif 'MIPS_32' == cpu_info().arch:
        macro_flags_list.add('MIPS_32')
    elif 'MIPS_64' == cpu_info().arch:
        macro_flags_list.add('MIPS_64')
    elif 'RISCV_32' == cpu_info().arch:
        macro_flags_list.add('RISCV_32')
    elif 'RISCV_64' == cpu_info().arch:
        macro_flags_list.add('RISCV_64')
    
    if 'CPython' == PYTHON_IMPLEMENTATION:
        macro_flags_list.add('CPython')
    elif 'PyPy' == PYTHON_IMPLEMENTATION:
        macro_flags_list.add('PyPy')
    elif 'IronPython' == PYTHON_IMPLEMENTATION:
        macro_flags_list.add('IronPython')
    elif 'Jython' == PYTHON_IMPLEMENTATION:
        macro_flags_list.add('Jython')
    
    if 'gcc' == compiler_type:
        macro_flags_list.add('gcc')
    elif 'msvc' == compiler_type:
        macro_flags_list.add('msvc')
    elif 'clang' == compiler_type:
        macro_flags_list.add('clang')
    elif 'icc' == compiler_type:
        macro_flags_list.add('icc')
    elif 'llvm' == compiler_type:
        macro_flags_list.add('llvm')
    elif 'intel' == compiler_type:
        macro_flags_list.add('intel')
    elif 'arm' == compiler_type:
        macro_flags_list.add('arm')
    elif 'mingw' == compiler_type:
        macro_flags_list.add('mingw')
    elif 'unknown' == compiler_type:
        macro_flags_list.add('unknown_compiler')
    
    if 'Linux' == OS_TYPE:
        macro_flags_list.add('Linux')
    elif 'Windows' == OS_TYPE:
        macro_flags_list.add('Windows')
    elif 'Darwin' == OS_TYPE:
        macro_flags_list.add('Darwin')
    
    if 'posix' == OS_API_TYPE:
        macro_flags_list.add('posix')
    elif 'nt' == OS_API_TYPE:
        macro_flags_list.add('nt')
    elif 'java' == OS_API_TYPE:
        macro_flags_list.add('java')
    
    if IS_RUNNING_IN_EMSCRIPTEN:
        macro_flags_list.add('IS_RUNNING_IN_EMSCRIPTEN')
    
    if IS_RUNNING_IN_WASI:
        macro_flags_list.add('IS_RUNNING_IN_WASI')
    
    if IS_RUNNING_IN_PYODIDE:
        macro_flags_list.add('IS_RUNNING_IN_PYODIDE')
    
    if IS_BUILDING_FOR_PYODIDE:
        macro_flags_list.add('IS_BUILDING_FOR_PYODIDE')
    
    if IS_INSIDE_OR_FOR_WEB_BROWSER:
        macro_flags_list.add('IS_INSIDE_OR_FOR_WEB_BROWSER')
    
    if IS_RUNNING_IN_PYCHARM:
        macro_flags_list.add('IS_RUNNING_IN_PYCHARM')

    macro_flags_list.update(additional_cflags)
    return macro_flags_list
