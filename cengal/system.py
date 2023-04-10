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


__all__ = ['PLATFORM_NAME', 'PYTHON_VERSION', 'PYTHON_VERSION_INT', 'IS_RUNNING_IN_PYCHARM', 'IS_RUNNING_IN_EMSCRIPTEN', 'IS_RUNNING_IN_PYODIDE', 'IS_BUILDING_FOR_PYODIDE']


import platform
import sys
import os
from typing import Tuple


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.1.9"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


PLATFORM_NAME: str = platform.python_implementation()  # can be 'PyPy', 'CPython', etc.
PYTHON_VERSION: Tuple[str, str, str] = platform.python_version_tuple()  # tuple() of str(); for example: ('3', '5', '1')
PYTHON_VERSION_INT = sys.version_info  # named typle sys.version_info(major=3, minor=7, micro=9, releaselevel='final', serial=0)
#   Usage: 
#       sys.version_info[0] == 3
#       (3,) > sys.version_info  # Is Python 2
#       (3, 6) <= sys.version_info  # Is Python 3.6+

IS_RUNNING_IN_PYCHARM: bool = "PYCHARM_HOSTED" in os.environ
IS_RUNNING_IN_EMSCRIPTEN: bool = 'emscripten' == sys.platform
IS_RUNNING_IN_PYODIDE: bool = "pyodide" in sys.modules
IS_BUILDING_FOR_PYODIDE: bool = "PYODIDE" in os.environ  # for setup.py execution time
