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
    'CengalNimBuildExtension',
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


# from distutils.dist import Distribution
from os import environ

from setuptools._distutils.dist import Distribution

from cengal.file_system.path_manager import path_relative_to_src, RelativePath, get_relative_path_part, sep
from cengal.file_system.directory_manager import current_src_dir, change_current_dir
from cengal.file_system.directory_manager import filtered_file_list, FilteringType, filtered_file_list_traversal, file_list_traversal, FilteringEntity
from cengal.file_system.file_manager import current_src_file_dir, file_exists
from cengal.build_tools.prepare_cflags import prepare_cflags, concat_cflags, prepare_compile_time_env, adjust_definition_names, \
    dict_of_tuples_to_dict, list_to_dict
from cengal.introspection.inspect import get_exception, entity_repr_limited_try_qualname, pifrl, pdi
from cengal.text_processing.text_processing import find_text
from cengal.system import OS_TYPE, TEMPLATE_MODULE_NAME
from shutil import rmtree
from os import remove
from os.path import splitext, normpath, join as path_join, basename, split
from setuptools import Extension as SetuptoolsExtension
from Cython.Distutils import Extension as CythonExtension
from distutils.command.build import build as build_orig
from distutils.command.build_ext import build_ext as build_ext_orig
from setuptools.command.sdist import sdist as sdist_orig
import json
import importlib

from os.path import isdir, exists, isfile, dirname

import setuptools
import platform

from cengal.file_system.path_manager import RelativePath, get_relative_path_part
from cengal.file_system.directory_manager import current_src_dir
from cengal.file_system.directory_manager import file_list_traversal, FilteringEntity
from cengal.build_tools.prepare_cflags import prepare_compile_time_flags, prepare_compile_time_env
from cengal.os.execute import prepare_params, escape_text, escape_param, prepare_command
from setuptools.discovery import find_package_path
import subprocess
from pprint import pprint
from typing import List, Dict, Optional, Iterable, Callable, Sequence, Tuple, Union, Type, Any

from .build_extensions import CengalBuildExtension


def wrap_definition_text(text: str) -> str:
    return text


def wrap_definition_text_v(text: str) -> str:
    return escape_param(text)


def wrap_definition_text_f(text: str) -> str:
    return f'"""{text}"""'


def prepare_definition_value(value: Union[None, bool, int, str]) -> Union[None, str]:
    if value is None:
        return None
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif isinstance(value, int):
        return str(value)
    elif isinstance(value, str):
        return wrap_definition_text(value)
    else:
        return wrap_definition_text(f'{value}')


def prepare_definition_value_v(value: Union[None, bool, int, str]) -> Union[None, str]:
    if value is None:
        return None
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif isinstance(value, int):
        return str(value)
    elif isinstance(value, str):
        return wrap_definition_text_v(value)
    else:
        return wrap_definition_text_v(f'{value}')


def prepare_definition_value_f(value: Union[None, bool, int, str]) -> Union[None, str]:
    if value is None:
        return None
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, str):
        return wrap_definition_text_f(value)
    else:
        return wrap_definition_text_f(f'{value}')


def wrap_definition_pair(name: str, value: Any) -> str:
    return f'-d:{name}' if value is None else f'-d:{name}={value}'


def prepare_definition(name: str, value: Optional[Union[bool, int, str]] = None) -> str:
    return wrap_definition_pair(name, prepare_definition_value(value))


def prepare_definition_v(name: str, value: Optional[Union[bool, int, str]] = None) -> str:
    return wrap_definition_pair(name, prepare_definition_value_v(value))


class CengalNimBuildExtension(CengalBuildExtension):
    base_class: Optional[Type] = None
    store_as_data: bool = True

    def __init__(self, 
                 module_name: str = 'main.nim', 
                 flags: Optional[List[str]] = None, 
                 definitions: Optional[Union[Sequence[str], Dict[str, Union[Union[None, bool, int, str], Tuple[bool, Union[None, bool, str, int]]]]]] = None, 
                 additional_compilation_params: Optional[List[str]] = None, 
                 definitions_module_name: str = 'compile_time_py_definitions.nim', 
                 **kwargs) -> None:
        self.module_name: str = module_name
        self.flags: Optional[List[str]] = flags or list()
        self.definitions: Optional[Union[Sequence[str], Dict[str, Union[Union[None, bool, int, str], Tuple[bool, Union[None, bool, str, int]]]]]] = definitions or dict()
        result_flags = adjust_definition_names(list_to_dict(prepare_compile_time_flags()), 'CF_', 'CD_')  # CF is Cengal Flag; CD is Cengal Definition
        self.result_definitions: Optional[Dict[str, Union[None, bool, int, float, str]]] = adjust_definition_names(prepare_compile_time_env(), 'CF_', 'CD_')  # CF is Cengal Flag; CD is Cengal Definition
        self.result_definitions.update(result_flags)
        self.result_definitions.update(dict_of_tuples_to_dict(list_to_dict(definitions)))
        self.result_definitions.update(list_to_dict(flags))
        self.additional_compilation_params: Optional[List[str]] = additional_compilation_params
        self.definitions_module_name: str = definitions_module_name
        super().__init__(kwargs)
    
    def __call__(self):
        try:
            out_file_name: str = f'{self.module_name}.pyd' if 'Windows' == OS_TYPE else f'{self.module_name}.so'
            print()
            print('==================================================')
            print(f'<<< NIM COMPILATION: {self.module_name} -> {out_file_name} >>>')
            print('=======================')
            params = ['nim', 'c', '--forceBuild:on', '--app:lib', f'--out:{out_file_name}', '--threads:on']
            params_v = ['nim', 'c', '--forceBuild:on', '--app:lib', f'--out:{out_file_name}', '--threads:on']
            for name, value in self.result_definitions.items():
                params.append(prepare_definition(name, value))
                params_v.append(prepare_definition_v(name, value))

            if self.additional_compilation_params:
                params.extend(self.additional_compilation_params)
                params_v.extend(self.additional_compilation_params)
            
            if 'Windows' == OS_TYPE:
                params.extend(['--tlsEmulation:off', '--passL:-static', self.module_name])
                params_v.extend(['--tlsEmulation:off', '--passL:-static', self.module_name])
            else:
                params.extend([self.module_name,])
                params_v.extend([self.module_name,])
                
            with change_current_dir(self.dir_path):
                self._ensure_gitignore()
                self._generate_definitions_module()
                print('> NIM compiler command line:')
                print(prepare_command(params_v[0], params_v[1:]))
                print('> NIM compiler params:')
                pprint(params)
                result = subprocess.run(params, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            
            successed: bool = find_text(result.stdout, '[SuccessX]') is not None
            print(f'{successed=}')
            result_str = result.stdout
            print('> NIM compiler output:')
            print(result_str)
            print('> Exported files:')
            exported_files_list = [out_file_name,]
            print(exported_files_list)
            print('==================================================')
            return exported_files_list if successed else None
        except:
            print('==================================================')
            print('!!! NIM COMPILATION EXCEPTION !!!')
            print('==================================================')
            print(get_exception())
            print('==================================================')
            return None
    
    def _ensure_gitignore(self):
        gitignore_path = self.dir_path_rel('.gitignore')
        if file_exists(gitignore_path):
            with open(gitignore_path, 'r+t') as f:
                content = f.read()
                if f'{self.module_name}.pyd' not in content:
                    f.write(f'{self.module_name}.pyd\n')
                
                if f'{self.module_name}.so' not in content:
                    f.write(f'{self.module_name}.so\n')
                
                if f'{self.module_name}.dll' not in content:
                    f.write(f'{self.module_name}.dll\n')
                
                if f'{self.module_name}.dylib' not in content:
                    f.write(f'{self.module_name}.dylib\n')
                
                if self.definitions_module_name not in content:
                    f.write(f'{self.definitions_module_name}\n')
        else:
            with open(gitignore_path, 'xt') as f:
                f.write(f'{self.module_name}.pyd\n')
                f.write(f'{self.module_name}.so\n')
                f.write(f'{self.module_name}.dll\n')
                f.write(f'{self.module_name}.dylib\n')
                f.write(f'{self.definitions_module_name}\n')
    
    def _generate_definitions_module(self):
        with open(self.dir_path_rel(self.definitions_module_name), 'wt') as f:
            f.write(f'# {self.definitions_module_name}\n\n')
            for name, value in self.result_definitions.items():
                prepared_value = prepare_definition_value_f(value)
                if prepared_value is None:
                    continue
                
                f.write(f'const {name}* = {prepared_value}\n')
