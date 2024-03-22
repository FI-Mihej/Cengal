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
    'CengalGoBuildExtension',
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
from cengal.file_system.directory_manager import current_src_dir, change_current_dir, ensure_dir
from cengal.file_system.directory_manager import filtered_file_list, FilteringType, filtered_file_list_traversal, file_list_traversal, FilteringEntity
from cengal.file_system.file_manager import current_src_file_dir, file_exists, full_ext, file_name, last_ext
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
import sys
import os

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
    return f'`{text}`'


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


class CengalGoBuildExtension(CengalBuildExtension):
    base_class: Optional[Type] = None
    store_as_data: bool = True

    def __init__(self, 
                 module_name: Optional[str] = None, 
                 src_dir: str = './src',
                 out_dir_name: str = 'compiled',
                 flags: Optional[List[str]] = None, 
                 definitions: Optional[Union[Sequence[str], Dict[str, Union[Union[None, bool, int, str], Tuple[bool, Union[None, bool, str, int]]]]]] = None, 
                 additional_build_params: Optional[List[str]] = None, 
                 additional_go_packages: Optional[List[str]] = None, 
                 definitions_module_name: str = 'compile_time_py_definitions', 
                 **kwargs) -> None:
        super().__init__(kwargs)
        self.module_name: str = module_name
        self.out_dir_name: str = out_dir_name
        self._src_dir: str = src_dir
        self.src_dir: str = None
        self.out_dir: str = None
        self.flags: Optional[List[str]] = flags or list()
        self.definitions: Optional[Union[Sequence[str], Dict[str, Union[Union[None, bool, int, str], Tuple[bool, Union[None, bool, str, int]]]]]] = definitions or dict()
        result_flags = adjust_definition_names(list_to_dict(prepare_compile_time_flags()), 'CF_', 'CD_')  # CF is Cengal Flag; CD is Cengal Definition
        self.result_definitions: Optional[Dict[str, Union[None, bool, int, float, str]]] = adjust_definition_names(prepare_compile_time_env(), 'CF_', 'CD_')  # CF is Cengal Flag; CD is Cengal Definition
        self.result_definitions.update(result_flags)
        self.result_definitions.update(dict_of_tuples_to_dict(list_to_dict(definitions)))
        self.result_definitions.update(list_to_dict(flags))
        self.additional_build_params: Optional[List[str]] = additional_build_params
        self.additional_go_packages: Optional[List[str]] = additional_go_packages
        self.definitions_module_name: str = definitions_module_name
        self.definitions_module_file_name: str = f'{definitions_module_name}.go'
    
    @property
    def module_name_str(self):
        if self.module_name:
            return self.module_name
        else:
            namespace = self.name
            namespace_parts = namespace.split('.')
            return'/'.join(namespace_parts[:-1])
    
    def __call__(self):
        try:
            # self.src_dir: str = self._src_dir if os.path.isabs(self._src_dir) else RelativePath(self.dir_path)(self._src_dir)
            self.src_dir: str = self._src_dir
            self.out_dir: str = RelativePath(self.dir_path)(self.out_dir_name)
            print()
            print('==================================================')
            print(f'<<< GO COMPILATION: {self.module_name_str} >>>')
            print('=======================')
            with change_current_dir(self.dir_path):
                params = ['go', 'mod', 'init', self.module_name_str]
                result = subprocess.run(params, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                print(result.stdout)

            env = os.environ.copy()
            additional_env = dict()
            additional_env['LD_LIBRARY_PATH'] = f"{env.get('LD_LIBRARY_PATH', '')}{os.pathsep}."
            env.update(additional_env)
            params = ['gopy', 'build', f'-output={self.out_dir_name}', f'-vm={sys.executable}']
            if self.additional_build_params:
                params.extend(self.additional_build_params)
            
            params.append(self.src_dir)
            params.append(f'./{file_name(self.definitions_module_name)}')
            if self.additional_go_packages:
                params.extend(self.additional_go_packages)
                
            compiler_output: str = str()
            with change_current_dir(self.dir_path):
                self._ensure_gitignore()
                self._generate_definitions_module()
                print('> Go compiler command line:')
                print(prepare_command(params[0], params[1:]))
                print('> Go compiler params:')
                pprint(params)
                print('> Additional environmental variables:')
                pprint(additional_env)
                result = subprocess.run(params, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                compiler_output = result.stdout

            successed: bool = find_text(compiler_output, 'cmd had error:') is None
            print(f'{successed=}')
            print('> Go compiler output:')
            print(compiler_output)
            exported_files_list = self._exported_files_list()
            adjusted_exported_files_list = list()
            for file_path in exported_files_list:
                adjusted_exported_files_list.append(get_relative_path_part(file_path, self.dir_path))
            
            print('> Exported files:')
            print(adjusted_exported_files_list)
            print('==================================================')
            # raise RuntimeError
            return adjusted_exported_files_list if successed else None
        except:
            print('==================================================')
            print('!!! GO COMPILATION EXCEPTION !!!')
            print('==================================================')
            print(get_exception())
            print('==================================================')
            return None
    
    def _exported_files_list(self) -> List[str]:
        def filter(data_type: FilteringEntity, data):
            if FilteringEntity.dirpath == data_type:
                return True
            elif FilteringEntity.dirname == data_type:
                return False
            elif FilteringEntity.filename == data_type:
                _, file_name = data
                if file_name in {'__init__.py', 'go.py'}:
                    return True
                elif file_name in {'build.py', 'Makefile'}:
                    return False
                elif last_ext(file_name) in {'so', 'dylib', 'pyd', 'dll', 'py', 'pyw'}:
                    return True
                else:
                    return False
            elif FilteringEntity.aggregated == data_type:
                result_full_file_names: List[str] = list()
                for dirpath, new_dirnames, new_filenames in data:
                    for file_name in new_filenames:
                        result_full_file_names.append(path_join(dirpath, file_name))
                
                return result_full_file_names
            else:
                raise NotImplementedError
        
        result_full_file_names: List[str] = file_list_traversal(self.out_dir, filter, True)
        return result_full_file_names if result_full_file_names else None

    def _ensure_gitignore(self):
        gitignore_path = self.dir_path_rel('.gitignore')
        if file_exists(gitignore_path):
            with open(gitignore_path, 'r+t') as f:
                content = f.read()
                if self.definitions_module_name not in content:
                    f.write(f'{self.definitions_module_name}/\n')
                
                out_dir_name = basename(self.out_dir)
                out_dir_name_ignorable = f'{out_dir_name}/'
                if out_dir_name_ignorable not in content:
                    f.write(f'{out_dir_name_ignorable}\n')

                if 'go.mod' not in content:
                    f.write(f'go.mod\n')

                if 'go.sum' not in content:
                    f.write(f'go.sum\n')
        else:
            with open(gitignore_path, 'xt') as f:
                f.write(f'{self.definitions_module_name}/\n')
                out_dir_name = basename(self.out_dir)
                out_dir_name_ignorable = f'{out_dir_name}/'
                f.write(f'{out_dir_name_ignorable}\n')
                f.write(f'go.mod\n')
                f.write(f'go.sum\n')
    
    def _generate_definitions_module(self):
        file_content_template: str = """// {config_file_name}
package {config_module_name}

const (
{constants_text}
)
"""
        constants_strings: List[str] = list()
        for name, value in self.result_definitions.items():
            prepared_value = prepare_definition_value_f(value)
            if prepared_value is None:
                continue
            
            constants_strings.append(f'\t{name} = {prepared_value}')
        
        constants_text: str = '\n'.join(constants_strings)
        file_content: str = file_content_template.format(
            config_file_name=self.definitions_module_file_name,
            config_module_name=file_name(self.definitions_module_name),
            constants_text=constants_text,
        )

        definitions_module_dir = self.dir_path_rel(self.definitions_module_name)
        ensure_dir(definitions_module_dir)
        definitions_module_dir_rel = RelativePath(definitions_module_dir)
        with open(self.dir_path_rel(definitions_module_dir_rel(self.definitions_module_file_name)), 'wt') as f:
            f.write(file_content)
