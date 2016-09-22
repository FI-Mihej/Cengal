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

import os.path
import shutil, errno
import subprocess
import time
from help_tools import get_text_in_brackets_offset, parse_cmd_input_dir_list
from file_system import filtered_file_list_traversal, filtered_file_list, FilteringType, change_current_dir
import colorama
from check_is_in_pycharm import IS_RUNNING_IN_PYCHARM

"""
Lines Of Code counting
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


def count_loc(search_dir, interested_extensions):
    lines_of_code = 0

    if len(interested_extensions) > 0:
        result_list = filtered_file_list_traversal(search_dir, FilteringType.including, interested_extensions)
    else:
        result_list = filtered_file_list_traversal(search_dir, FilteringType.off)
    print(result_list)

    with change_current_dir(search_dir):
        for result in result_list:
            if not os.path.split(result[0])[1].startswith('.'):
                for filename in result[2]:
                    full_file_name = os.path.join(result[0], filename)
                    try:
                        with open(full_file_name, 'rb') as file:
                            data = file.read()
                            data_lines = data.split(b'\n')
                            in_multiline_comment = False
                            for data_line in data_lines:
                                line = data_line.strip()
                                if len(line) > 0:
                                    is_ok = True
                                    if line.startswith(b'#'):
                                        is_ok = False

                                    if line.startswith(b"'''"):
                                        is_ok = False
                                        if in_multiline_comment:
                                            in_multiline_comment = False
                                        else:
                                            in_multiline_comment = True

                                    if in_multiline_comment:
                                        is_ok = False

                                    if is_ok:
                                        lines_of_code += 1
                    except PermissionError:
                        print('{}PermissionError{}: {}{}{}'.format(colorama.Fore.RED,
                                                                   colorama.Style.RESET_ALL,
                                                                   colorama.Fore.MAGENTA,
                                                                   full_file_name,
                                                                   colorama.Style.RESET_ALL
                                                                   ))

    return lines_of_code


def main():
    if not IS_RUNNING_IN_PYCHARM:
        colorama.init()

    search_dir_list_raw = input('Choose a search dir (S:\\ome\\Dir\\Name) or (["S:\\ome\\Dir"], ["D:\\ir"], ["K:"]): ')
    search_dir_list = parse_cmd_input_dir_list(search_dir_list_raw)
    interested_extensions_raw = input('Enter extentions set (".txt; .u;.;; .jpg") or leave empty: ')
    interested_extensions = None
    if len(interested_extensions_raw.strip()) > 0:
        interested_extensions = set(''.join(interested_extensions_raw.split()).split(';'))
    else:
        interested_extensions = {'.py', '.pyw'}
    lines_of_code = 0
    for search_dir in search_dir_list:
        lines_of_code += count_loc(search_dir, interested_extensions)
    print('LOC = {}'.format(lines_of_code))

    if not IS_RUNNING_IN_PYCHARM:
        print()
        input('Click Enter to exit')


if __name__ == "__main__":
    main()
