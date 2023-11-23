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

__all__ = ['RelativePath', 'relative_to_src', 'path_relative_to_src', 'relative_to_cwd', 
           'path_relative_to_cwd', 'WrongBaseDirError', 'get_relative_path_part', 'sep', 
           'canonical_path']

import os
from os.path import normpath, expanduser, realpath, abspath, normcase, sep
from typing import Optional
from cengal.file_system.directory_manager import current_src_dir
from cengal.text_processing.text_processing import removeprefix

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


class RelativePath:
    def __init__(self, base_path: str):
        self.base_path: str = base_path

    def __call__(self, relative_path: str):
        return normpath(os.path.join(self.base_path, relative_path))


def relative_to_src(depth: Optional[int] = 1) -> RelativePath:
    """

    :param depth: 0 - path of this file, 1 - path of the caller's file, etc.
    :return:
    """
    depth = depth or 0
    depth += 1
    return RelativePath(current_src_dir(depth))


def path_relative_to_src(relative_path: str, depth: Optional[int] = 1):
    """

    :param relative_path:
    :param depth: 0 - path of this file, 1 - path of the caller's file, etc.
    :return:
    """
    depth = depth or 0
    depth += 1
    return RelativePath(current_src_dir(depth))(relative_path)


def relative_to_cwd() -> RelativePath:
    return RelativePath(os.getcwd())


def path_relative_to_cwd(relative_path: str):
    return RelativePath(os.getcwd())(relative_path)


class WrongBaseDirError(Exception):
    pass


def get_relative_path_part(path: str, base_dir: str) -> str:
    path = normpath(path)
    base_dir = normpath(base_dir)
    if not path.startswith(base_dir):
        raise WrongBaseDirError
    
    relative_part = removeprefix(path, base_dir)
    if relative_part.startswith(sep):
        relative_part = removeprefix(relative_part, sep)
    
    return relative_part


def canonical_path(path: str, resolve_symlinks: bool = True) -> str:
    """
    Convert a path to its canonical, case-normalized, absolute version.
    """

    path = expanduser(path)
    if resolve_symlinks:
        path = realpath(path)
    else:
        path = abspath(path)
    
    return normcase(path)
