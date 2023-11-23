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

import errno
from contextlib import contextmanager
import shutil
import os
import os.path
from enum import Enum
import hashlib
from cengal.introspection.inspect import frame
from typing import Optional, Callable, Set, Tuple

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


class FilteringType(Enum):
    including = 0  # include only files with extensions within the set of extensions
    excluding = 1  # filter out files with extensions within the set of extensions
    off = 2  # any file will fit criteria


def filtered_file_list(root_dir: str, filtering_type: FilteringType, extentions_set: Optional[Set] = None) -> Tuple:
    """_summary_

    Args:
        root_dir (str): r'C:\dir\path'
        filtering_type (FilteringType): _description_
        extentions_set (Optional[Set], optional): {'.upk', '.txt'}. Defaults to None.

    Raises:
        Exception: _description_

    Returns:
        Tuple: (dirpath, dirnames, new_filenames)
    """

    if (FilteringType.off != filtering_type) and (extentions_set is None):
        raise Exception('extentions_set can\'t be None with this filtering type')

    result = None
    raw_result = next(os.walk(root_dir))
    dirpath = raw_result[0]
    dirnames = raw_result[1]
    filenames = raw_result[2]

    new_filenames = list()
    for filename in filenames:
        if FilteringType.off == filtering_type:
            new_filenames.append(filename)
        elif FilteringType.including == filtering_type:
            extention = os.path.splitext(filename)[1]
            if extention in extentions_set:
                new_filenames.append(filename)
        elif FilteringType.excluding == filtering_type:
            extention = os.path.splitext(filename)[1]
            if extention not in extentions_set:
                new_filenames.append(filename)

    result = (dirpath, dirnames, new_filenames)
    return result


def filtered_file_list_traversal(root_dir: str, filtering_type: FilteringType, extentions_set: Optional[Set] = None, 
                                 remove_empty_items: bool =False, use_spinner: bool = False):
    """
    :param root_dir: str(); r'C:\dir\path'
    :param filtering_type: FilteringType()
    :param extentions_set: set(); {'.upk', '.txt'}
    :return: list() of tuple(); list of (dirpath, dirnames, new_filenames)
    """

    if (FilteringType.off != filtering_type) and (extentions_set is None):
        raise Exception('extentions_set can\'t be None with this filtering type')

    spinner = None
    spinner_index = 0
    if use_spinner:
        from progress.spinner import Spinner
        spinner = Spinner('Loading ')
    result_list = list()
    for raw_result in os.walk(root_dir):
        dirpath = raw_result[0]
        dirnames = raw_result[1]
        filenames = raw_result[2]

        new_filenames = list()
        for filename in filenames:
            if FilteringType.off == filtering_type:
                new_filenames.append(filename)
            elif FilteringType.including == filtering_type:
                extention = os.path.splitext(filename)[1]
                if extention in extentions_set:
                    new_filenames.append(filename)
            elif FilteringType.excluding == filtering_type:
                extention = os.path.splitext(filename)[1]
                if extention not in extentions_set:
                    new_filenames.append(filename)
        if remove_empty_items:
            if len(new_filenames) > 0:
                result = (dirpath, dirnames, new_filenames)
                result_list.append(result)
        else:
            result = (dirpath, dirnames, new_filenames)
            result_list.append(result)

        if use_spinner:
            spinner_index += 1
            if spinner_index >= 1000:
                spinner_index = 0
                spinner.next()
    if use_spinner:
        print()

    return result_list


class FilteringEntity(Enum):
    dirpath = 0
    dirname = 1
    filename = 2
    aggregated = 3


def file_list_traversal(root_dir, filter: Callable = None, remove_empty_dirpaths=False):
    """
    :param root_dir: str(); r'C:\dir\path'
    :param filtering_type: FilteringType()
    :param extentions_set: set(); {'.upk', '.txt'}
    :return: list() of tuple(); list of (dirpath, dirnames, new_filenames)
    """

    if filter is None:
        def default_filter(filtering_entity: FilteringEntity, data):
            if FilteringEntity.aggregated == filtering_entity:
                return data
            else:
                return True

        filter = default_filter

    result_list = list()
    for raw_result in os.walk(root_dir):
        dirpath = raw_result[0]
        dirnames = raw_result[1]
        filenames = raw_result[2]

        if not filter(FilteringEntity.dirpath, (dirpath, dirnames, filenames)):
            continue

        new_dirnames = list()
        for dirname in dirnames:
            if filter(FilteringEntity.dirname, (dirpath, dirname)):
                new_dirnames.append(dirname)

        new_filenames = list()
        for filename in filenames:
            if filter(FilteringEntity.filename, (dirpath, filename)):
                new_filenames.append(filename)
        
        if remove_empty_dirpaths:
            if not new_filenames and not new_dirnames:
                continue

        result = (dirpath, new_dirnames, new_filenames)
        result_list.append(result)

    return filter(FilteringEntity.aggregated, result_list)


def clear_dir(full_dir_path):
    full_dir_path = os.path.normpath(full_dir_path)
    if (os.path.exists(full_dir_path) and os.path.isdir(full_dir_path)):
        dir_path, sub_dir_names, file_names = filtered_file_list(full_dir_path, FilteringType.off)
        for sub_dir in sub_dir_names:
            full_sub_dir_path = os.path.join(dir_path, sub_dir)
            shutil.rmtree(full_sub_dir_path, ignore_errors=True)
        for file in file_names:
            full_file_name = os.path.join(dir_path, file)
            os.remove(full_file_name)


@contextmanager
def change_current_dir(new_current_dir):
    new_current_dir = os.path.normpath(new_current_dir)
    cur_dir = os.getcwd()
    os.chdir(new_current_dir)
    try:
        yield
    except:
        raise
    finally:
        os.chdir(cur_dir)


def get_dir_hash(full_dir_path, hash_format_string=None):
    hash_format_string = hash_format_string or '{} {}'
    result_list = filtered_file_list_traversal(full_dir_path, FilteringType.off)

    dir_content = list()
    for dirpath, dirnames, new_filenames in result_list:
        for filename in new_filenames:
            full_file_name = os.path.join(dirpath, filename)
            with open(full_file_name, 'rb') as file:
                file_content = file.read()
                dir_content.append(file_content)
    dir_content = b''.join(dir_content)
    dir_hash = hash_format_string.format(hashlib.sha512(dir_content).hexdigest(), hex(len(dir_content))[2:])
    return dir_hash


def current_src_dir(depth: Optional[int] = 1):
    """

    :param depth: 0 - path of this file, 1 - path of the caller's file, etc.
    :return:
    """
    depth = depth or 0
    depth += 1
    return os.path.dirname(os.path.realpath(frame(depth).f_code.co_filename))


def ensure_dir(dir_path):
    dir_path = os.path.normpath(dir_path)
    if not (os.path.exists(dir_path) and os.path.isdir(dir_path)):
        try:
            os.makedirs(dir_path, exist_ok=True)
        except OSError as er:
            # Windows can raise spurious ENOTEMPTY errors. See https://github.com/pypa/pip/issues/6426
            if (errno.EEXIST != er.errno) and (errno.ENOTEMPTY != er.errno):
                raise


def ensure_empty_dir(dir_path):
    ensure_dir(dir_path)
    clear_dir(dir_path)


def dir_exists(dir_path) -> bool:
    dir_path = os.path.normpath(dir_path)
    return os.path.exists(dir_path) and os.path.isdir(dir_path)
