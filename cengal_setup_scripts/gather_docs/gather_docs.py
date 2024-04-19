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
__version__ = "4.3.4"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.file_system.directory_manager import FilteringEntity, file_list_traversal, file_list_traversal_ex, ensure_empty_dir, ensure_dir
from cengal.file_system.file_manager import last_ext
from cengal.file_system.path_manager import relative_to_src, get_relative_path_part, RelativePath
from shutil import copyfile
from os.path import join as path_join, dirname, basename
from pprint import pprint
from typing import Any, List, Set, Optional
from pathlib import Path
import shutil

from pdoc import pdoc
from pdoc import render
from cengal.build_tools.gather_docs import gather_docs as gather_docs_orig


def cengal_repo_root_dir() -> str:
    return relative_to_src()('../..')


def cengal_docs_dir() -> str:
    return RelativePath(cengal_repo_root_dir())('docs')


def cengal_src_root_dir() -> str:
    return RelativePath(cengal_repo_root_dir())('cengal')


def ignored_modules() -> Set[str]:
    return {
        'cengal/_examples', 
        'cengal/_template_module', 
        'cengal/code_flow_control/none_or', 
        'cengal/code_inspection/line_profiling', 
        'cengal/cross_version/console_print', 
        'cengal/help_tools', 
        'cengal/os/help_tools', 
        'cengal/parallel_execution/coroutines/coro_standard_services/cpu_tick_count_per_second', 
        'cengal/testing_lib', 
        'cengal/text_processing/docten', 
        'cengal/time_management/server_clock', 
        'cengal/universal_parser', 
        'cengal/upk_helping_tools', 
        'cengal/user_interface/console/chooser', 
    }


def gather_docs():
    gather_docs_orig(
        cengal_repo_root_dir(), 
        cengal_src_root_dir(),
        cengal_docs_dir(),
        ignored_modules(),
    )


if '__main__' == __name__:
    gather_docs()
