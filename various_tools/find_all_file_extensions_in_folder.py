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

import argparse
import os.path
import sys
import shutil, errno
import subprocess
import time
from help_tools import get_text_in_brackets_offset, \
    parse_cmd_input_dir_list
from file_system import filtered_file_list_traversal, filtered_file_list, FilteringType, change_current_dir
from file_settings_manager.config_manager import *
from check_is_in_pycharm import IS_RUNNING_IN_PYCHARM

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


class GlobalConfig(ConfigManager):
    def __init__(self, immediate_save=True):
        default_content = {
            'find extensions': {
                'last dir': '',
            },
        }
        super(GlobalConfig, self).__init__(['.PythonLibs Settings', 'Various Tools'],
                                           default_content=default_content,
                                           immediate_save=immediate_save)


def check_help_request():
    result = False
    cmd_args = sys.argv[1:]
    need_to_show_help = False
    for argument in cmd_args:
        argument = argument.lower()
        if ('help' in argument) or('h' in argument) or ('?' in argument):
            need_to_show_help = True
            break
    if need_to_show_help:
        help_string = '''
<<FIND IN FILES>>

    DIRS FOR SEARCH.
        Choose a search dir.
        Use (S:\\ome\\Dir\\Name) without brackets for single dir.
        Use (["S:\\ome\\Dir"], ["D:\\ir"], ["K:"]) without brackets for multiple dirs.
        Or leave empty to use last used dir string.
        '''
        print(help_string)
        result = True
    return result


def find_extensions(search_dir):
    extensions_set = set()
    result_list = filtered_file_list_traversal(search_dir, FilteringType.off)

    for result in result_list:
        for filename in result[2]:
            extensions_set.add(os.path.splitext(filename)[1])
    return extensions_set


def main():
    if check_help_request():
        sys.exit(0)

    global_config = GlobalConfig()
    last_dir = global_config.get_property('find extensions', 'last dir') or ''

    # DIRS FOR SEARCH
    search_dir_list_raw = input('Choose a search dir (S:\\ome\\Dir\\Name), (["S:\\ome\\Dir"], ["D:\\ir"], ["K:"]) or '
                                'leave empty to use last used dir ({}): '.format(last_dir))
    if len(search_dir_list_raw) == 0:
        search_dir_list_raw = last_dir
    global_config.set_property('find extensions', 'last dir', search_dir_list_raw)
    search_dir_list = parse_cmd_input_dir_list(search_dir_list_raw)

    # PROCESS SEARCH
    set_of_extensions = set()
    for search_dir in search_dir_list:
        set_of_extensions.update(find_extensions(search_dir))
    set_of_extensions_string = '; '.join(set_of_extensions)
    print()
    print('As set(): ', set_of_extensions)
    print()
    print('As string: [{}]'.format(set_of_extensions_string))

    if not IS_RUNNING_IN_PYCHARM:
        print()
        input('Click Enter to exit')


if __name__ == "__main__":
    main()