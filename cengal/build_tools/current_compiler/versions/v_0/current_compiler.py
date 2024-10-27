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


__all__ = ['compiler_type', 'compiler_name', 'compiler_string', 'compiler_string_escaped', 'assume_compiler']


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.os.process.prepare_cmd_line import escape_text

import os
from distutils import sysconfig
from contextlib import contextmanager
from typing import Union, Dict, Optional


compiler_name_raw: Union[str, None] = None
compiler_name: str = str()
compiler_string: str = str()
compiler_string_escaped: str = str()
compiler_type: str = str()


def check_compiler():
    global compiler_name_raw, compiler_name, compiler_string, compiler_string_escaped, compiler_type
    compiler_name_raw = sysconfig.get_config_var("CC")
    if compiler_name_raw is None:
        if sysconfig.get_config_var("VSINSTALLDIR") is None:
            if 'VSCMD_ARG_TGT_ARCH' in os.environ:
                compiler_name_raw = 'msvc'
            else:
                compiler_name_raw = str()
        else:
            compiler_name_raw = 'msvc'

    compiler_name = compiler_name_raw.split()[0] if compiler_name_raw else str()
    compiler_string = compiler_name_raw
    compiler_string_escaped = escape_text(compiler_name_raw)

    if "gcc" in compiler_name_raw.lower():
        compiler_type = 'gcc'
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


@contextmanager
def assume_compiler(env: Optional[Dict[str, str]] = None):
    env = env or dict()
    old_env = os.environ
    os.environ = env
    try:
        check_compiler()
        yield
    finally:
        os.environ = old_env
        check_compiler()


check_compiler()
