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
from help_tools import get_text_in_brackets_offset, parse_cmd_input_dir_list
from file_system import filtered_file_list_traversal, filtered_file_list, FilteringType, change_current_dir
from file_settings_manager.config_manager import *
from check_is_in_pycharm import IS_RUNNING_IN_PYCHARM
from progress.bar import Bar

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
            'list simlinks': {
                'last search string': '',
                'last dir': '',
                'last extensions': ''
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

    SEARCH REQUEST.
        Enter (*) to search files with any names.
        Enter file name (with * and ? filters) to search name templates.
        Or leave empty to use last used value.

    DIRS FOR SEARCH.
        Choose a search dir.
        Use (S:\\ome\\Dir\\Name) without brackets for single dir.
        Use (["S:\\ome\\Dir"], ["D:\\ir"], ["K:"]) without brackets for multiple dirs.
        Or leave empty to use last used dir string.

    EXTENSIONS TO SEARCH.
        Enter (*) without brackets for any extension.
        Enter (;) or (.) or (.;) without brackets for files without extensions.
        Enter extension (.doc) without brackets for single extension.
        Enter extensions set (.txt.; .u;.;; .jpg) without brackets for a multiple extensions.
        Or leave empty to use last used value.

        '''
        print(help_string)
        result = True
    return result


def find_files(search_dir, interested_extensions):
    result_list = None
    if len(interested_extensions) > 0:
        result_list = filtered_file_list_traversal(search_dir, FilteringType.including, interested_extensions,
                                                   use_spinner=True)
    else:
        result_list = filtered_file_list_traversal(search_dir, FilteringType.off, use_spinner=True)

    # os.chdir(search_dir)

    index = 0
    for result in result_list:
        index += len(result[2])
    print('Qnt of files:', index)

    bar = Bar('Processing', max=index)
    bar_index = 0
    for result in result_list:
        for filename in result[2]:
            full_file_name = os.path.join(result[0], filename)
            if os.path.islink(full_file_name):
                link_relative_destination = os.readlink(full_file_name)
                link_destination = os.path.join(os.path.dirname(full_file_name), link_relative_destination)
                print('>> {} ===> {}'.format(full_file_name, link_destination))
            bar_index += 0
            if bar_index >= 1000:
                bar_index = 0
                bar.next(1000)
    bar.finish()


def filter_to_commands_list(input_filter):
    input_list = list(input_filter)
    input_list_len = len(input_list)
    input_list.reverse()
    index = 0
    while index < input_list_len:
        input_list.index()
        pass
    # input_list.reverse()
    # for item in input_list:
    #     if '*' == item:
    #         pass
    #     elif '?' == item:
    #         pass
    #     else:
    #         pass


def main():
    if check_help_request():
        sys.exit(0)

    global_config = GlobalConfig()
    last_dir = global_config.get_property('list simlinks', 'last dir') or ''
    last_extensions = global_config.get_property('list simlinks', 'last extensions') or ''

    # DIRS FOR SEARCH
    search_dir_list_raw = input('Choose a search dir (S:\\ome\\Dir\\Name), (["S:\\ome\\Dir"], ["D:\\ir"], ["K:"]) or '
                                'leave empty to use last used dir ({}): '.format(last_dir))
    if len(search_dir_list_raw) == 0:
        search_dir_list_raw = last_dir
    global_config.set_property('list simlinks', 'last dir', search_dir_list_raw)
    search_dir_list = parse_cmd_input_dir_list(search_dir_list_raw)

    # EXTENSIONS TO SEARCH
    interested_extensions_raw = input('Enter extensions set (".txt.; .u;.;; .jpg"), (";"), ("*") '
                                      'or leave empty to use last used value ({}): '.format(last_extensions))
    interested_extensions = None
    if len(interested_extensions_raw.strip()) == 0:
        interested_extensions_raw = last_extensions.strip()
    global_config.set_property('list simlinks', 'last extensions', interested_extensions_raw)
    if '*' == interested_extensions_raw.strip():
        interested_extensions = set()
    else:
        interested_extensions = set(''.join(interested_extensions_raw.split()).split(';'))

    # PROCESS SEARCH
    for search_dir in search_dir_list:
        find_files(search_dir, interested_extensions)

    if not IS_RUNNING_IN_PYCHARM:
        print()
        input('Click Enter to exit')


if __name__ == "__main__":
    main()
