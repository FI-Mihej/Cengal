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
__version__ = "3.2.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from os import environ
if 'CENGAL_BUILD_IS_IN_DEBUG_MODE' in environ:
    import debugpy


from cengal.file_system.path_manager import path_relative_to_src, RelativePath, get_relative_path_part, sep
from cengal.file_system.directory_manager import current_src_dir
from cengal.file_system.directory_manager import filtered_file_list, FilteringType, filtered_file_list_traversal, file_list_traversal, FilteringEntity
from cengal.build_tools.prepare_cflags import prepare_cflags, concat_cflags, prepare_compile_time_env
from cengal.introspection.inspect import get_exception
from cengal.system import OS_TYPE, TEMPLATE_MODULE_NAME
from shutil import rmtree
from os import remove
from os.path import splitext, normpath, join as path_join, basename, splitext
from setuptools import Extension
from distutils.command.build import build as build_orig
from distutils.command.build_ext import build_ext as build_ext_orig
from setuptools.command.sdist import sdist as sdist_orig
import json
import importlib
from typing import Sequence


BUILD_CONFIG_FILENAME: str = '__build_config.py'


cython_file_ext = '.pyx'
cython_transpiled_ext = {'.c'}
compilable_ext = {'.pyx', '.cpp', '.c++', '.cxx', '.cc'}
headers_ext = {'.h', '.hpp', '.h++', '.hh', '.hxx'}
libs_ext = {'.lib', '.dll', '.so'}
all_ext = cython_transpiled_ext | compilable_ext | headers_ext | libs_ext


def get_file_name_without_extension(path):
    file_name = basename(path)  # Get the base name from the path
    file_name_without_extension = splitext(file_name)[0]  # Split the file name and extension, and take only the file name part
    return file_name_without_extension


def remove_header_files(ext_modules: Sequence[Extension]) -> Sequence[Extension]:
    for ext_module in ext_modules:
        if isinstance(ext_module, Extension):
            new_sources = list()
            for source in ext_module.sources:
                _, file_extension = splitext(source)
                if file_extension not in headers_ext:
                    new_sources.append(source)
            
            ext_module.sources = new_sources
    
    return ext_modules


def find_and_prepare_cython_modules(depth = 1):
    depth = depth or 0
    depth += 1
    root = RelativePath(current_src_dir(depth))
    root_path = root('')
    cengal = RelativePath(root('./cengal'))
    cengal_path = cengal('')

    travers_result = filtered_file_list_traversal(cengal_path, FilteringType.off, None, remove_empty_items=True, use_spinner=False)
    for dir_path, dirs, files in travers_result:
        if '__pycache__' in dirs:
            pycache_path = RelativePath(dir_path)('__pycache__')
            try:
                rmtree(pycache_path)
            except OSError as e:
                print(get_exception())


    def filter(filtering_entity: FilteringEntity, data):
        if FilteringEntity.dirpath == filtering_entity:
            # Ignore cengal/_template_module
            dirpath, dirnames, filenames = data
            rel_path = get_relative_path_part(dirpath, cengal_path)
            rel_path = rel_path.strip()
            if rel_path:
                rel_path_parts = rel_path.split(sep)
                if rel_path_parts and TEMPLATE_MODULE_NAME == rel_path_parts[0]:
                    return False
            
            return True
        elif FilteringEntity.dirname == filtering_entity:
            return True
        elif FilteringEntity.filename == filtering_entity:
            dirpath, filename = data
            if BUILD_CONFIG_FILENAME == filename:
                return True
            
            file_name, file_extension = splitext(filename)
            if file_extension in all_ext:
                return True
            
            return False
        elif FilteringEntity.aggregated == filtering_entity:
            return data
        else:
            raise NotImplementedError()
        
    travers_result = file_list_traversal(cengal_path, filter, remove_empty_dirpaths=True)
    # travers_result = filtered_file_list_traversal(cengal_path, FilteringType.including, {'.pyx', '.c', '.lib', '.dll', '.so'}, remove_empty_items=True, use_spinner=False)
    
    result = list()
    for dir_path, dirs, files in travers_result:
        # Ignore cengal/_template_module
        rel_path = get_relative_path_part(dir_path, cengal_path)
        rel_path = rel_path.strip()
        if rel_path:
            rel_path_parts = rel_path.split(sep)
            if rel_path_parts and TEMPLATE_MODULE_NAME == rel_path_parts[0]:
                continue

        dir_path_obj = RelativePath(dir_path)
        extensions = dict()
        for file in files:
            filename, file_extension = splitext(file)
            if file_extension not in extensions:
                extensions[file_extension] = set()
            
            extensions[file_extension].add(file)
        
        is_exctension: bool = False
        build_config: dict = None
        if BUILD_CONFIG_FILENAME in files:
            build_config_module_name, _ = splitext(BUILD_CONFIG_FILENAME)
            build_config_full_path: str = dir_path_obj(build_config_module_name)
            name = get_relative_path_part(build_config_full_path, root(''))
            name_parts = name.split(sep)
            module_full_name = '.'.join([name_part for name_part in name_parts if name_part])
            build_config_module = importlib.import_module(module_full_name)
            build_config = build_config_module.build_config()

        sub_result = list()
        if (cython_file_ext in extensions) or (build_config is not None):
            for file_extension, files in extensions.items():
                for file in files:
                    if file_extension.lower() in (compilable_ext | headers_ext):
                        is_exctension = True
                        sub_result.append(path_join('.', get_relative_path_part(dir_path_obj(file), root_path)))
                    
                    if '.c' == file_extension.lower():
                        filename, _ = splitext(file)
                        if filename.endswith('__cython'):
                            try:
                                remove(dir_path_obj(file))
                            except OSError as e:
                                print(get_exception())
                        else:
                            is_exctension = True
                            sub_result.append(path_join('.', get_relative_path_part(dir_path_obj(file), root_path)))
                    
                    if file_extension.lower() in libs_ext:
                        try:
                            remove(dir_path_obj(file))
                        except OSError as e:
                            print(get_exception())
        
        if is_exctension:
            name = get_relative_path_part(dir_path_obj(''), root(''))
            name_parts = name.split(sep)
            if build_config is None:
                if 1 == len(sub_result) and sub_result[0].endswith(cython_file_ext):
                    name_parts.append(get_file_name_without_extension(sub_result[0]))
                else:
                    name_parts.append('cython_module')
                
                name = '.'.join([name_part for name_part in name_parts if name_part])
                extension: Extension = Extension(
                    name, 
                    sources=sub_result,
                    language="c",
                    cython_compile_time_env=prepare_compile_time_env(),
                )
            else:
                if 'Windows' == OS_TYPE:
                    # Extension :raises setuptools.errors.PlatformError: if 'runtime_library_dirs' is specified on Windows. (since v63)
                    build_config.pop('runtime_library_dirs', None)
                
                name_parts.append(build_config['name'])
                name = '.'.join([name_part for name_part in name_parts if name_part])
                build_config.pop('name', None)

                cython_compile_time_env=prepare_compile_time_env()
                if 'cython_compile_time_env' in build_config:
                    cython_compile_time_env.update(build_config['cython_compile_time_env'])
                    build_config.pop('cython_compile_time_env', None)
                
                extension: Extension = Extension(
                    name, 
                    sources=sub_result,
                    cython_compile_time_env=cython_compile_time_env,
                    **build_config
                )
            
            result.append(extension)
        else:
            result.extend(sub_result)
    
    return result


class sdist(sdist_orig):
    def run(self):
        if 'CENGAL_BUILD_IS_IN_DEBUG_MODE' in environ:
            debugpy.breakpoint()
        
        print("sdist command is currently being run")
        environ['CENGAL_BUILD_IS_IN_SDIST_MODE'] = 'True'
        super().run()


class build(build_orig):
    def finalize_options(self):
        if 'CENGAL_BUILD_IS_IN_DEBUG_MODE' in environ:
            debugpy.breakpoint()
        
        super().finalize_options()
        if 'CENGAL_BUILD_IS_IN_SDIST_MODE' not in environ:
            from Cython.Build import cythonize
            self.distribution.ext_modules = remove_header_files(cythonize(self.distribution.ext_modules,
                                                compiler_directives={'language_level': '3'},
                                                compile_time_env = prepare_compile_time_env(),
                                                ))
            if 'CENGAL_BUILD_IS_IN_DEBUG_MODE' in environ:
                debugpy.breakpoint()
                print()


class build_ext(build_ext_orig):
    def finalize_options(self):
        if 'CENGAL_BUILD_IS_IN_DEBUG_MODE' in environ:
            debugpy.breakpoint()
        
        super().finalize_options()
        if 'CENGAL_BUILD_IS_IN_SDIST_MODE' not in environ:
            from Cython.Build import cythonize
            self.distribution.ext_modules = remove_header_files(cythonize(self.distribution.ext_modules,
                                                compiler_directives={'language_level': '3'},
                                                compile_time_env = prepare_compile_time_env(),
                                                ))
            if 'CENGAL_BUILD_IS_IN_DEBUG_MODE' in environ:
                debugpy.breakpoint()
                print()
