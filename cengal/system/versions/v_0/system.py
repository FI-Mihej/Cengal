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
            'PLATFORM_NAME', 'PYTHON_IMPLEMENTATION', 'PYTHON_VERSION', 'PYTHON_VERSION_STR', 
            'PYTHON_VERSION_INT', 'IS_RUNNING_IN_PYCHARM', 'RAW_OS_PLATFORM', 'OS_API_TYPE', 
            'OS_TYPE', 'KIVY_PLATFORM', 'KIVY_TARGET_PLATFORM', 'IS_RUNNING_IN_EMSCRIPTEN', 'IS_RUNNING_IN_PYODIDE', 'IS_BUILDING_FOR_PYODIDE', 
            'CENGAL_IS_IN_BUILD_MODE', 'TEMPLATE_MODULE_NAME', 'cengal_module_rel_path', 
            'cengal_module_import_str', 'current_cengal_module_rel_path', 'current_cengal_module_import_str',
            'CENGAL_UNITTESTS_DISCOVER_IS_RUNNING', 'IS_INSIDE_OR_FOR_WEB_BROWSER', 'IS_RUNNING_IN_WASI', 
            'CENGAL_VERSION_STR', 'CENGAL_VERSION_MAJOR_STR', 'CENGAL_VERSION_MINOR_STR', 
            'CENGAL_VERSION_MICRO_STR', 'CENGAL_VERSION', 'CENGAL_VERSION_MAJOR', 'CENGAL_VERSION_MINOR', 
            'CENGAL_VERSION_MICRO',
           ]


import platform
import sys
import os
from typing import Tuple, Optional


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.4.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


PLATFORM_NAME: str = platform.python_implementation()  # TODO: deprecated. Can be 'CPython', 'PyPy', 'IronPython', 'Jython'.
PYTHON_IMPLEMENTATION: str = platform.python_implementation()  # can be 'CPython', 'PyPy', 'IronPython', 'Jython'.
PYTHON_VERSION: Tuple[str, str, str] = platform.python_version_tuple()  # tuple() of str(); for example: ('3', '5', '1')
PYTHON_VERSION_STR: str = '.'.join(PYTHON_VERSION)
PYTHON_VERSION_INT: Tuple[int, int, int, str, int] = sys.version_info  # named typle sys.version_info(major=3, minor=7, micro=9, releaselevel='final', serial=0)
#   Usage: 
#       sys.version_info[0] == 3
#       (3,) > sys.version_info  # Is Python 2
#       (3, 6) <= sys.version_info  # Is Python 3.6+

IS_RUNNING_IN_PYCHARM: bool = "PYCHARM_HOSTED" in os.environ

RAW_OS_PLATFORM: str = sys.platform  # 'emscripten', 'wasi', 'darwin', 'win32', 'cygwin', 'linux', 'linux2', 'linux3', 'darwin', 'freebsd8', 'aix', aix5', 'aix7', ...
OS_API_TYPE: str = os.name  # The following names have currently been registered: 'posix', 'nt', 'java'. Android and iOS will return 'posix'.
OS_TYPE: str = platform.system()  # 'Linux', 'Windows', 'Darwin', 'Java'
try:
    from kivy.utils import platform as kivy_platform
    KIVY_PLATFORM: str = kivy_platform  # 'win', 'linux', 'android', 'macosx', 'ios', 'unknown'
except ImportError:
    KIVY_PLATFORM = 'unknown'  # 'win', 'linux', 'android', 'macosx', 'ios', 'unknown'

KIVY_TARGET_PLATFORM: str = os.environ.get('KIVY_TARGET_PLATFORM', default='unknown')  # It is required for the developer to manually set the 'KIVY_TARGET_PLATFORM' environment variable prior to the build process to ensure accurate platform detection.

IS_RUNNING_IN_EMSCRIPTEN: bool = 'emscripten' == sys.platform
IS_RUNNING_IN_WASI: bool = 'wasi' == sys.platform
IS_RUNNING_IN_PYODIDE: bool = "pyodide" in sys.modules
IS_BUILDING_FOR_PYODIDE: bool = "PYODIDE" in os.environ  # for setup.py execution time
IS_INSIDE_OR_FOR_WEB_BROWSER: bool = IS_RUNNING_IN_EMSCRIPTEN or IS_RUNNING_IN_WASI or IS_BUILDING_FOR_PYODIDE or IS_RUNNING_IN_PYODIDE

CENGAL_IS_IN_BUILD_MODE: bool = ('CENGAL_IS_IN_BUILD_MODE' in os.environ) and ('true' == os.environ['CENGAL_IS_IN_BUILD_MODE'].casefold())

TEMPLATE_MODULE_NAME: str = '_template_module'

CENGAL_UNITTESTS_DISCOVER_IS_RUNNING: bool = ('CENGAL_UNITTESTS_DISCOVER_IS_RUNNING' in os.environ) and ('true' == os.environ['CENGAL_UNITTESTS_DISCOVER_IS_RUNNING'].casefold())

CENGAL_VERSION_STR = __version__
CENGAL_VERSION = tuple([int(part) for part in CENGAL_VERSION_STR.split('.')])
CENGAL_VERSION_MAJOR = CENGAL_VERSION[0]
CENGAL_VERSION_MINOR = CENGAL_VERSION[1]
CENGAL_VERSION_MICRO = CENGAL_VERSION[2]
CENGAL_VERSION_MAJOR_STR = str(CENGAL_VERSION_MAJOR)
CENGAL_VERSION_MINOR_STR = str(CENGAL_VERSION_MINOR)
CENGAL_VERSION_MICRO_STR = str(CENGAL_VERSION_MICRO)

def cengal_module_rel_path(cengal_module) -> str:
    from cengal.modules_management.module_rel_path import module_rel_path
    import cengal
    return module_rel_path(cengal, cengal_module)


def cengal_module_import_str(cengal_module) -> str:
    from cengal.modules_management.module_rel_path import module_import_str
    import cengal
    return module_import_str(cengal, cengal_module)


def current_cengal_module_rel_path(depth: Optional[int] = 1) -> str:
    from cengal.modules_management.module_rel_path import current_module_rel_path
    import cengal
    return current_module_rel_path(cengal, depth + 1)


def current_cengal_module_import_str(depth: Optional[int] = 1) -> str:
    from cengal.modules_management.module_rel_path import current_module_import_str
    import cengal
    return current_module_import_str(cengal, depth + 1)
