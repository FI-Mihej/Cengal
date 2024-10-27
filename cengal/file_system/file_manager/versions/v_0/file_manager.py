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
    'get_file_hash', 
    'get_file_modification_date', 
    'get_executable_src_path',
    'current_src_file_dir', 
    'path_relative_to_current_src', 
    'path_relative_to_current_dir', 
    'file_exists', 
    'full_ext', 
    'full_ext_parts', 
    'last_ext', 
    'has_ext', 
    'file_name', 
    'gen_random_file_name', 
    'gen_random_file_path', 
    'AtomicFileCreator', 
    'atomic_file_creator', 
    'RemoveFileAfterUsage', 
    'remove_file_after_usage', 
]


import sys
import hashlib
import datetime
import inspect
import uuid

from os import getcwd, extsep, rename, remove
from os.path import exists, isfile, isdir, normpath, dirname, getmtime, realpath, join, basename, abspath
from typing import Optional

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


def get_executable_src_path():
    if getattr(sys, 'frozen', False):
        # If the application is run as a frozen executable (e.g., with PyInstaller)
        return normpath(realpath(abspath(sys.executable)))
    else:
        # If the application is run as a normal Python script
        return normpath(realpath(abspath(sys.argv[0])))


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


def full_ext(file_path: str) -> str:
    return extsep.join(basename(normpath(file_path)).split(extsep)[1:])


def full_ext_parts(file_path: str) -> str:
    return basename(normpath(file_path)).split(extsep)[1:]


def last_ext(file_path: str) -> str:
    return basename(normpath(file_path)).split(extsep)[-1]


def has_ext(file_path: str) -> str:
    return extsep in basename(normpath(file_path))


def file_name(file_path: str) -> str:
    return basename(normpath(file_path)).split(extsep)[0]


def gen_random_file_name(dir_path: str, prefix: str = str(), ext: Optional[str] = None) -> str:
    """Returns a random file name (without path) that does not exist in the specified directory.
    Does not create a file.

    Args:
        dir_path (str): _description_
        prefix (str, optional): _description_. Defaults to str().
        ext (Optional[str], optional): _description_. Defaults to None.

    Raises:
        ValueError: _description_

    Returns:
        str: _description_
    """
    if exists(dir_path):
        if isdir(dir_path):
            pass
        else:
            raise ValueError('dir_path is not a directory')
    
    if ext is not None:
        if not ext.startswith(extsep):
            ext = extsep + ext
    else:
        ext = str()
    
    file_name: str = str()
    while True:
        file_name = prefix + str(uuid.uuid4()) + ext
        if not exists(join(dir_path, file_name)):
            break
    
    return file_name


def gen_random_file_path(dir_path: str, prefix: str = str(), ext: Optional[str] = None) -> str:
    """Returns a random full file name (with given path) that does not exist in the specified directory.
    Does not create a file.

    Args:
        dir_path (str): _description_
        prefix (str, optional): _description_. Defaults to str().
        ext (Optional[str], optional): _description_. Defaults to None.

    Raises:
        ValueError: _description_

    Returns:
        str: _description_
    """
    file_name: str = gen_random_file_name(dir_path, prefix, ext)
    return join(dir_path, file_name)


class AtomicFileCreator:
    def __init__(self, file_path: str, prefix: str = str(), ext: Optional[str] = None):
        self.file_path: str = normpath(file_path)
        self.dir_path: str = dirname(self.file_path)
        self.prefix: str = prefix if prefix else 'atomic__'
        self.ext: str = 'tmp' if ext is None else ext
        self.temp_file_path: str = None
    
    def __enter__(self):
        self.temp_file_path = join(self.dir_path, gen_random_file_name(self.dir_path, self.prefix, self.ext))
        return self.temp_file_path
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            if self.temp_file_path is not None:
                if file_exists(self.temp_file_path):
                    rename(self.temp_file_path, self.file_path)
        else:
            if self.temp_file_path is not None:
                if file_exists(self.temp_file_path):
                    remove(self.temp_file_path)

        return False


atomic_file_creator = AtomicFileCreator


class RemoveFileAfterUsage:
    def __init__(self, file_path: str):
        self.file_path: str = file_path
    
    def __enter__(self):
        return self.file_path
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if file_exists(self.file_path):
            remove(self.file_path)
        
        return False


remove_file_after_usage = RemoveFileAfterUsage
