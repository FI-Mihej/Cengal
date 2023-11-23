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


__all__ = ['compiler_type', 'compiler_name']


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


from distutils import sysconfig


compiler_name_raw: str = sysconfig.get_config_var("CC")
if compiler_name_raw is None:
    if sysconfig.get_config_var("VSINSTALLDIR") is None:
        compiler_name_raw = str()
    else:
        compiler_name_raw = 'msvc'

compiler_name: str = compiler_name_raw.replace(' ', '\ ')

if "gcc" in compiler_name_raw.lower():
    compiler_type: str = 'gcc'
elif "msvc" in compiler_name_raw.lower():
    compiler_type = 'msvc'
elif "clang" in compiler_name_raw.lower():
    compiler_type = 'clang'
elif "icc" in compiler_name_raw.lower():
    compiler_type = 'icc'
elif "llvm" in compiler_name_raw.lower():
    compiler_type = 'llvm'
elif "intel" in compiler_name_raw.lower():
    compiler_type = 'intel'
elif "arm" in compiler_name_raw.lower():
    compiler_type = 'arm'
elif "mingw" in compiler_name_raw.lower():
    compiler_type = 'mingw'
else:
    compiler_type = 'unknown'