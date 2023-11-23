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

import argparse
import os.path
import shutil, errno
import subprocess
import time
from ..file_system import filtered_file_list, FilteringType
import shutil
from . import upk_constants

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


def unpack_upk_files(upk_utils_dir, xcom_upk_dir, output_dir, copy_if_error=True, copy_already_unpacked_files=True):
    """
    :param upk_utils_dir:
    :param xcom_upk_dir:
    :param output_dir:
    :param copy_if_error:
    :param copy_already_unpacked_files:
    :return:
    """

    original_current_dir = os.getcwd()
    try:
        set_of_ext = {'.upk'}
        if copy_already_unpacked_files:
            set_of_ext.add('.u')
        file_list_result = filtered_file_list(xcom_upk_dir, FilteringType.including, set_of_ext)

        os.chdir(output_dir)

        for filename in file_list_result[2]:
            full_file_name = os.path.join(file_list_result[0], filename)
            call_result = subprocess.call([os.path.join(upk_utils_dir, 'DecompressLZO'), full_file_name, filename])
            print('RESULT: {}; FROM: {}; TO {}'.format(call_result, full_file_name, filename))
            if call_result == 1:  # "Package is already decompressed!"
                if copy_if_error:
                    shutil.copyfile(full_file_name, filename)
    finally:
        os.chdir(original_current_dir)


def unpack_single_upk_file(upk_utils_dir, full_file_path, output_dir, copy_if_error=True):
    original_current_dir = os.getcwd()
    try:
        os.chdir(output_dir)

        call_result = subprocess.call([os.path.join(upk_utils_dir, 'DecompressLZO'), full_file_name, filename])
        print('RESULT: {}; FROM: {}; TO {}'.format(call_result, full_file_name, filename))
        if call_result == 1:  # "Package is already decompressed!"
            if copy_if_error:
                shutil.copyfile(full_file_name, filename)
    finally:
        os.chdir(original_current_dir)


def deserialize_upk_files(upk_utils_dir, xcom_unpacked_upk_dir, output_dir):
    """
    :param upk_utils_dir:
    :param xcom_unpacked_upk_dir:
    :param output_dir:
    :return:
    """

    original_current_dir = os.getcwd()
    try:
        file_list_result = filtered_file_list(xcom_unpacked_upk_dir, FilteringType.including, {'.upk', '.u'})

        os.chdir(output_dir)

        for filename in file_list_result[2]:
            full_file_name = os.path.join(file_list_result[0], filename)
            call_result = subprocess.call([os.path.join(upk_utils_dir, 'DeserializeAll'), full_file_name])
    finally:
        os.chdir(original_current_dir)


def deserialize_single_upk_file(upk_utils_dir, upk_file_filename, output_dir):
    """
    :param upk_utils_dir:
    :param xcom_unpacked_upk_dir:
    :param output_dir:
    :return:
    """

    call_result = None
    original_current_dir = os.getcwd()
    try:
        os.chdir(output_dir)

        call_result = subprocess.call([os.path.join(upk_utils_dir, 'DeserializeAll'), upk_file_filename])
    finally:
        os.chdir(original_current_dir)

    return call_result


def patch_upk_file(upk_utils_dir, xcom_unpacked_upk_dir, patch_file, uninstall_instead_of_installation=False):
    """
    :param upk_utils_dir:
    :param xcom_unpacked_upk_dir:
    :param output_dir:
    :return:
    """

    call_result = None
    original_current_dir = os.getcwd()
    try:
        if uninstall_instead_of_installation:
            patch_file = ''.join([patch_file, upk_constants.FileExtensions.mod_uninstall_info])

        patch_file_path, patch_file_name = os.path.split(patch_file)
        os.chdir(patch_file_path)

        call_result = subprocess.call([os.path.join(upk_utils_dir, 'PatchUPK'), patch_file_name, xcom_unpacked_upk_dir])
        print(call_result)
    finally:
        os.chdir(original_current_dir)

    return call_result


def export_from_upk_to_pseudo_code(upk_utils_dir, upk_file_full_name, object_full_name, output_mod_full_file_name=None):
    """
    :param upk_utils_dir:
    :param upk_file_full_name:
    :param object_full_name:
    :param output_mod_full_file_name:
    :return: None or bytes()
    """
    mod_file_with_pseudo_code_data = None
    call_result = None
    original_current_dir = os.getcwd()
    try:
        output_mod_dir, output_mod_file_name_only = os.path.split(output_mod_full_file_name)
        os.chdir(output_mod_dir)

        upk_utility_file_name = os.path.join(upk_utils_dir, 'HexToPseudoCode')
        process = subprocess.Popen([upk_utility_file_name,
                                             upk_file_full_name,
                                             object_full_name,
                                             # '/d'
                                    ],
                                   stdout=subprocess.PIPE)
        call_result = process.returncode
        call_res_stdout, call_res_strerr = process.communicate()
        if call_result:
            # some error:
            print('ERROR:', call_res_strerr)
        else:
            # executed without errors:
            mod_file_with_pseudo_code_data = call_res_stdout
            if output_mod_full_file_name is not None:
                with open(output_mod_full_file_name, 'bw') as file:
                    file.write(call_res_stdout)
    finally:
        os.chdir(original_current_dir)

    return mod_file_with_pseudo_code_data
