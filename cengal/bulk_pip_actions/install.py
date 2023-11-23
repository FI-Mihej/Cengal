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

# import pip
# from pip._internal import main as pip_main
import platform
import sys
import os.path
from contextlib import contextmanager
from cengal.cross_version.console_print.universal import cross_print

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


PLATFORM_NAME = platform.python_implementation()  # can be 'PyPy', 'CPython', etc.
PYTHON_VERSION = platform.python_version_tuple()  # tuple() of str(); for example: ('3', '5', '1')
PYTHON_VERSION_INT = sys.version_info  # sys.version_info == (major=3, minor=2, micro=5, releaselevel='final', serial=0)
#   Usage: sys.version_info[0] == 3


# On Python < 3.4 you should install enum backport module before you will be able to use it. So:
FROM_PYPI = 0
FROM_ZIP = 1
FROM_FOLDER_WITH_ZIP_FILES = 2
FROM_EXTERNAL_GIT = 3


_FILTERING_TYPE__OFF = 0
_FILTERING_TYPE__INCLUDING = 1
_FILTERING_TYPE__EXCLUDING = 2


# Do not import this function from THIS module!
@contextmanager
def _change_current_dir(new_current_dir):
    cur_dir = os.getcwd()
    os.chdir(new_current_dir)
    try:
        yield
    except:
        raise
    finally:
        os.chdir(cur_dir)


# Do not import this function from THIS module!
def _filtered_file_list_traversal(root_dir, filtering_type, extentions_set=None, remove_empty_items=False):
    """
    :param root_dir: str(); r'C:\dir\path'
    :param filtering_type: FilteringType()
    :param extentions_set: set(); {'.upk', '.txt'}
    :return: list() of tuple(); list of (dirpath, dirnames, new_filenames)
    """

    if (_FILTERING_TYPE__OFF != filtering_type) and (extentions_set is None):
        raise Exception('extentions_set can\'t be None with this filtering type')

    result_list = list()
    for raw_result in os.walk(root_dir):
        dirpath = raw_result[0]
        dirnames = raw_result[1]
        filenames = raw_result[2]

        new_filenames = list()
        for filename in filenames:
            if _FILTERING_TYPE__OFF == filtering_type:
                new_filenames.append(filename)
            elif _FILTERING_TYPE__INCLUDING == filtering_type:
                extention = os.path.splitext(filename)[1]
                if extention in extentions_set:
                    new_filenames.append(filename)
            elif _FILTERING_TYPE__EXCLUDING == filtering_type:
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

    return result_list


# def pip_install(name_or_path):
#     command_line = None
#     pip_name = None
#     if 'nt' == os.name:
#         path_to_interpreter = sys.executable
#         interpreter_root_dir_name = os.path.dirname(path_to_interpreter)
#         path_to_pip = os.path.join(interpreter_root_dir_name, 'Scripts', 'pip.exe')
#         pip_name_template = '"{}"'
#         pip_name = pip_name_template.format(path_to_pip)
#     else:
#         if '2' == PYTHON_VERSION[0]:
#             pip_name = 'pip'
#         elif '3' == PYTHON_VERSION[0]:
#             pip_name = 'pip3'
#     command_line_template = '{pip_name} install --upgrade {package_name_or_path}'
#     command_line = command_line_template.format(pip_name=pip_name, package_name_or_path=name_or_path)
#     os.system(command_line)


def pip_install(name_or_path):
    path_to_interpreter = sys.executable
    if 'nt' == os.name:
        path_to_interpreter_template = '"{}"'
        path_to_interpreter = path_to_interpreter_template.format(path_to_interpreter)

    command_line_template = '{path_to_interpreter} -m pip install --upgrade {package_name_or_path}'
    command_line = command_line_template.format(path_to_interpreter=path_to_interpreter, package_name_or_path=name_or_path)
    os.system(command_line)


def install(name_or_path, type_of_installation):
    """
    Will exit(1) on error (done by pip_main() itself)!
    :param name_or_path: 'tornado', './python-lzf-master-python3.zip', './InstallSourcess/Python3/', etc.
    :param type_of_installation: {FROM_PYPI, FROM_ZIP, FROM_FOLDER_WITH_ZIP_FILES}
    :return:
    """
    if FROM_PYPI == type_of_installation:
        # pip_main(['install', name_or_path])
        pip_install(name_or_path)
        cross_print('')
    elif FROM_ZIP == type_of_installation:
        # pip_main(['install', name_or_path])
        pip_install(name_or_path)
        cross_print('')
    elif FROM_FOLDER_WITH_ZIP_FILES == type_of_installation:
        interested_extensions = {'.zip'}
        result_list = _filtered_file_list_traversal(name_or_path, _FILTERING_TYPE__INCLUDING, interested_extensions)
        for result in result_list:
            for filename in result[2]:
                # I'm not sure now, but I think I remember that there was some troubles when you trying to install
                # some zipped modules with full path under PyPy. So:
                relative_file_name = os.path.join('.', filename)
                with _change_current_dir(result[0]):
                    # pip_main(['install', relative_file_name])
                    pip_install(relative_file_name)
                    cross_print('')
