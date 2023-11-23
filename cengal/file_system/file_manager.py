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

import hashlib
# import os
import datetime
import inspect
from typing import Optional
from os import getcwd
from os.path import exists, isfile, normpath, dirname, getmtime, realpath, join

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


def get_file_hash(full_file_name, hash_format_string=None):
    hash_format_string = hash_format_string or '{} {}'
    file_content = None
    with open(full_file_name, 'rb') as file:
        file_content = file.read()
    file_hash = hash_format_string.format(hashlib.sha512(file_content).hexdigest(), hex(len(file_content))[2:])
    return file_hash


def get_file_modification_date(full_file_name):
    time_stamp = getmtime(full_file_name)
    return datetime.datetime.fromtimestamp(time_stamp)


def current_src_file_dir() -> str:
    return dirname(realpath(inspect.currentframe().f_back.f_code.co_filename))


def path_relative_to_current_src(relative_path: Optional[str]=None) -> str:
    relative_path = relative_path or str()
    return normpath(join(dirname(realpath(inspect.currentframe().f_back.f_code.co_filename)), normpath(relative_path)))


def path_relative_to_current_dir(relative_path: Optional[str]=None) -> str:
    relative_path = relative_path or str()
    return normpath(join(getcwd(), normpath(relative_path)))


def file_exists(file_path: str) -> bool:
    return exists(file_path) and isfile(file_path)
