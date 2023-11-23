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
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from typing import Dict, Tuple, Union, Iterable, List, Callable
from cengal.system import CENGAL_IS_IN_BUILD_MODE
from cengal.build_tools.find_and_prepare_cython_modules import find_and_prepare_cython_modules as find_and_prepare_cython_modules_orig, \
    sdist as sdist_orig, build as build_orig, build_ext as build_ext_orig, \
    BuildConfig as BuildConfig_orig, Distribution, \
    find_good_packages as find_good_packages_orig, find_package_data as find_package_data_orig
from cengal.file_system.path_manager import path_relative_to_src, RelativePath, get_relative_path_part, sep


PACKAGE_SRC_RELATIVE_PATH: str = './cengal'
MODULES_TO_IGNORE = {'cengal._template_module'}
PYTHON_2_MODULES = {'cengal.cross_version.console_print.python2'}
EXCLUDE_FROM_PACKAGES = [
            'tests', 'tests.*', 'multiproject', 'multiproject.*', 'examples', 'examples.*', 'docs', 'docs.*', 'benchmarks', 'benchmarks.*', 
            'cengal.egg-info', 'cengal.egg-info.*', 'dist', '.eggs', '.idea', '.vscode', 'package',
        ]


def repo_root_rel() -> RelativePath:
    return RelativePath(path_relative_to_src('../..'))


def cengal_root_rel() -> RelativePath:
    return RelativePath(repo_root_rel()(PACKAGE_SRC_RELATIVE_PATH))


def find_good_packages():
    return find_good_packages_orig(where=repo_root_rel()(''), exclude=EXCLUDE_FROM_PACKAGES, modules_to_ignore=MODULES_TO_IGNORE, python_2_modules=PYTHON_2_MODULES)


def find_package_data() -> Tuple[Dict[str, List[str]], List[str]]:
    return find_package_data_orig(PACKAGE_SRC_RELATIVE_PATH, find_good_packages(), root_rel=repo_root_rel())


def find_and_prepare_cython_modules(depth = 1):
    depth = depth or 0
    depth += 1
    additional_cflags: Dict[str, Tuple[bool, Union[str, int]]] = {
        'CENGAL_IS_IN_BUILD_MODE': CENGAL_IS_IN_BUILD_MODE,
    }
    return find_and_prepare_cython_modules_orig(PACKAGE_SRC_RELATIVE_PATH, additional_cflags, depth, root_rel=repo_root_rel())


class BuildConfig(BuildConfig_orig):
    def __init__(self) -> None:
        super().__init__()
        self.package_build_is_in_debug_mode: str = 'CENGAL_BUILD_IS_IN_DEBUG_MODE'
        self.package_build_is_in_sdist_mode: str = 'CENGAL_BUILD_IS_IN_SDIST_MODE'
        self.additional_cflags: Dict[str, Tuple[bool, Union[str, int]]] = {
            'CENGAL_IS_IN_BUILD_MODE': CENGAL_IS_IN_BUILD_MODE,
        }
        self.find_package_data: Callable = find_package_data
        self.root_rel: RelativePath = repo_root_rel()


class sdist(sdist_orig):
    def __init__(self, dist: Distribution) -> None:
        super().__init__(dist, BuildConfig())


class build(build_orig):
    def __init__(self, dist: Distribution) -> None:
        super().__init__(dist, BuildConfig())


class build_ext(build_ext_orig):
    def __init__(self, dist: Distribution) -> None:
        super().__init__(dist, BuildConfig())
