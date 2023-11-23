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


from typing import Dict
from cengal.build_tools.current_compiler import compiler_type
from cengal.hardware.info.cpu import cpu_info
from cengal.system import (
    PYTHON_IMPLEMENTATION,
    PYTHON_VERSION,
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
    CENGAL_IS_IN_BUILD_MODE,
)


# See: https://docs.python.org/3/distutils/apiref.html?highlight=extension#distutils.core.Extension
def build_config() -> Dict:
    result = {
        'name': 'cython_module_name',
        'language': 'c'
    }
    
    return result
