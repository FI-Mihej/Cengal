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
    'CengalBuildExtension',
    'CengalSetuptoolsBuildExtension',
    'CengalCythonBuildExtension',
    'CengalGeneratorBuildExtension',
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


class CengalBuildExtension:
    base_class: Optional[Type] = None
    store_as_data: bool = False

    def __init__(self, kwargs) -> None:
        self.kwargs = kwargs
        self._path = None
        self._module_import_str = None
        self._files = list()

    def __call__(self):
        return self.base_class(**self.kwargs) if self.base_class is not None else None
    
    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, value: str):
        self._path = value
    
    @property
    def dir_path(self) -> str:
        return None if self._path is None else dirname(self._path)
    
    @property
    def dir_path_rel(self) -> RelativePath:
        return None if self._path is None else RelativePath(dirname(self._path))

    @property
    def module_import_str(self) -> str:
        return self._module_import_str
    
    @module_import_str.setter
    def module_import_str(self, value: str):
        self._module_import_str = value

    @property
    def name(self) -> str:
        return self._module_import_str

    @property
    def package(self) -> str:
        return '.'.join(self._module_import_str.split('.')[:-1])
    
    @property
    def files(self) -> str:
        return self._files
    
    @files.setter
    def files(self, value: str):
        self._files = value


class CengalSetuptoolsBuildExtension(CengalBuildExtension):
    base_class: Optional[Type] = SetuptoolsExtension

    def __init__(self, **kwargs) -> None:
        super().__init__(kwargs)


class CengalCythonBuildExtension(CengalBuildExtension):
    base_class: Optional[Type] = CythonExtension

    def __init__(self, **kwargs) -> None:
        super().__init__(kwargs)


class CengalGeneratorBuildExtension(CengalBuildExtension):
    base_class: Optional[Type] = None
    store_as_data: bool = True

    def __init__(self, **kwargs) -> None:
        super().__init__(kwargs)
    
    def __call__(self):
        raise NotImplementedError
