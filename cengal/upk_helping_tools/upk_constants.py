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

from enum import Enum

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.2.6"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


class FileExtensions:
    various_info = '.txt'
    mod_uninstall_info = '.uninstall.txt'
    upk_file = '.upk'
    unpacked_upk_file = '.u'
    backup_file = '.bak'
    decompiled_c_pseudocode = '.c'
    ucb_source_code = '.ucb'  # "Unreal engine Compilable Bytecode" (UCB) - compilable source code
    reformatted_ucb_source_code = '.reformatted.ucb'  # original source was compiled and decompiled to this file
    full_function_bytecode = '.ffbc'
    function_content_bytecode = '.fbc'


class UpkHexFilesInternals:
    function_object_header_size = 48
    function_object_tail_size = 15
