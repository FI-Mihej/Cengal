#!/usr/bin/env python

# Copyright © 2016 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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

import pip
import platform
import sys
import os.path
from contextlib import contextmanager
from cross_version.console_print.universal import cross_print

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2016 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "1.0.0"
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
    '''
    :param root_dir: str(); r'C:\XComGame\CookedPCConsole'
    :param filtering_type: FilteringType()
    :param extentions_set: set(); {'.upk', '.txt'}
    :return: list() of tuple(); list of (dirpath, dirnames, new_filenames)
    '''

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


def install(name_or_path, type_of_installation):
    '''
    Will exit(1) on error (done by pip.main() itself)!
    :param name_or_path: 'tornado', './python-lzf-master-python3.zip', './InstallSourcess/Python3/', etc.
    :param type_of_installation: {FROM_PYPI, FROM_ZIP, FROM_FOLDER_WITH_ZIP_FILES}
    :return:
    '''
    if FROM_PYPI == type_of_installation:
        pip.main(['install', name_or_path])
        cross_print('')
    elif FROM_ZIP == type_of_installation:
        pip.main(['install', name_or_path])
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
                    pip.main(['install', relative_file_name])
                    cross_print('')
