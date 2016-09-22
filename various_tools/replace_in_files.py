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
import sys
import colorama
from check_is_in_pycharm import IS_RUNNING_IN_PYCHARM
from help_tools import get_text_in_brackets_offset, \
    parse_cmd_input_dir_list, bytes__to__hex_string, hex_string__to__bytes
from file_system import filtered_file_list_traversal, filtered_file_list, FilteringType, change_current_dir
from file_settings_manager.config_manager import *
from text_processing.help_tools import detach_all_slices_from_string, detach_all_slices_from_string__case_insensitive, \
    bytes_to_printable, check_is_slice_is_in_string, check_is_slice_is_in_string__case_insensitive
from code_flow_control.result_types import *
from code_flow_control.smart_chain import *
from various_tools.find_in_files import FindInFilesGlobalConfig, \
    highlight_slice_in_a_bytes_array_with_colorama

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


class ReplaceInFilesGlobalConfig(ConfigManager):
    def __init__(self, immediate_save=True):
        default_content = {
            'replace in files': {
                'last search string': '',
                'last replace string': ''
            },
        }
        super(ReplaceInFilesGlobalConfig, self).__init__(['.PythonLibs Settings', 'Various Tools'],
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
        Enter search text with prefix:
            s - for Unicode strings. For example (s Some Unicode string request);
            se - for Unicode string with Escape characters. For example (se Some line\nSome new line);
            h - for HEX values. For example (h 4F 94 AD 00 FF);
        or leave empty to use last used value

    DIRS FOR SEARCH.
        Choose a search dir.
        Use (S:\\ome\\Dir\\Name) without brackets for single dir.
        Use (["S:\\ome\\Dir"], ["D:\\ir"], ["K:"]) without brackets for multiple dirs.
        Or leave empty to use last used dir string.

    EXTENSIONS TO SEARCH.
        Enter (*) without brackets for any extension.
        Enter (;) without brackets or (.) without brackets for files without extensions.
        Enter extension (.doc) without brackets for single extension.
        Enter extensions set (.txt.; .u;.;; .jpg) without brackets for a multiple extensions.
        Or leave empty to use last used value.

        '''
        print(help_string)
        result = True
    return result


def replace_in_folder(search_string, replace_string, search_dir, interested_extensions, preview=False,
                      case_insensitive=True):
    function__detach = detach_all_slices_from_string
    if case_insensitive:
        function__detach = detach_all_slices_from_string__case_insensitive

    function__check_is_in = check_is_slice_is_in_string
    if case_insensitive:
        function__check_is_in = check_is_slice_is_in_string__case_insensitive

    result_list = None
    if len(interested_extensions) > 0:
        result_list = filtered_file_list_traversal(search_dir, FilteringType.including, interested_extensions)
    else:
        result_list = filtered_file_list_traversal(search_dir, FilteringType.off)

    with change_current_dir(search_dir):
        for result in result_list:
            for filename in result[2]:
                full_file_name = os.path.join(result[0], filename)
                try:
                    need_to_rewrite_file = False
                    result_data = None
                    with open(full_file_name, 'rb') as file:
                        data = file.read()

                        if function__check_is_in(search_string, data):
                            print('>> {}{}{}'.format(colorama.Fore.YELLOW,
                                                     full_file_name,
                                                     colorama.Style.RESET_ALL))
                            split_data_line = function__detach(
                                data, search_string)
                            result_data_lines = list()
                            for part in split_data_line[0]:
                                result_data_lines.append(part[0])
                                result_data_lines.append(replace_string)
                            result_data_lines.append(split_data_line[1])
                            result_data = b''.join(result_data_lines)
                            if preview:
                                data_string = highlight_slice_in_a_bytes_array_with_colorama(
                                    result_data, replace_string, colorama.Fore.CYAN, case_insensitive)
                                print(data_string)
                            else:
                                need_to_rewrite_file = True
                            print('    {}Quantity{}: {}'.format(
                                colorama.Fore.MAGENTA,
                                colorama.Style.RESET_ALL,
                                len(split_data_line[0])
                            ))
                            print()
                    if need_to_rewrite_file:
                        with open(full_file_name, 'wb') as file:
                            file.write(result_data)
                except PermissionError:
                    print('{}PermissionError{}: {}{}{}'.format(colorama.Fore.RED,
                                                               colorama.Style.RESET_ALL,
                                                               colorama.Fore.MAGENTA,
                                                               full_file_name,
                                                               colorama.Style.RESET_ALL
                                                               ))


def main():
    if not IS_RUNNING_IN_PYCHARM:
        colorama.init()

    if check_help_request():
        sys.exit(0)

    context = IsOK_ContextHolder('Replace In Files', 'main', ResultType(CriteriaType.optional, set()))

    global_config = ReplaceInFilesGlobalConfig()
    last_search_string = global_config.get_property('replace in files', 'last search string') or ''
    last_replace_string = global_config.get_property('replace in files', 'last replace string') or ''

    find_in_files_global_config = FindInFilesGlobalConfig()
    last_dir = find_in_files_global_config.get_property('find in files', 'last dir') or ''
    last_extensions = find_in_files_global_config.get_property('find in files', 'last extensions') or ''

    print('Search dirs (taken from the {}"Find In Files"{} tool): {}{}{}'.format(
        colorama.Fore.YELLOW,
        colorama.Style.RESET_ALL,
        colorama.Fore.GREEN,
        last_dir,
        colorama.Style.RESET_ALL,
    ))
    print('Extensions (taken from the {}"Find In Files"{} tool): {}{}{}'.format(
        colorama.Fore.YELLOW,
        colorama.Style.RESET_ALL,
        colorama.Fore.GREEN,
        last_extensions,
        colorama.Style.RESET_ALL
    ))

    with is_ok(context, 'search request'):
        if context:
            # SEARCH REQUEST
            print()
            search_string = input('Enter SEARCH text with "s ", "se " or "h " prefix '
                                  'or leave empty to use last used value ({}): '.format(last_search_string))
            if len(search_string) == 0:
                search_string = last_search_string
            global_config.set_property('replace in files', 'last search string', search_string)
            first_space_end_position = search_string.find(' ') + 1
            search_type = search_string[:first_space_end_position]
            search_string = search_string[first_space_end_position:]
            if 's ' == search_type.lower():
                search_string = search_string.encode()
            elif 'se ' == search_type.lower():
                search_string = eval("'{}'".format(search_string))
                search_string = search_string.encode()
            elif 'h ' == search_type.lower():
                search_string = hex_string__to__bytes(search_string)
            else:
                raise Exception('Unknown search string type! Use "s " prefix for string value or "h " for HEX value!')
            context.push_result(True, search_string)

    with is_ok(context, 'replace request'):
        if context:
            # SEARCH REQUEST
            print()
            replace_string = input('Enter REPLACING text with "s ", "se " or "h " prefix '
                                  'or leave empty to use last used value ({}): '.format(last_replace_string))
            if len(replace_string) == 0:
                replace_string = last_replace_string
            global_config.set_property('replace in files', 'last replace string', replace_string)
            first_space_end_position = replace_string.find(' ') + 1
            search_type = replace_string[:first_space_end_position]
            replace_string = replace_string[first_space_end_position:]
            if 's ' == search_type.lower():
                replace_string = replace_string.encode()
            elif 'se ' == search_type.lower():
                replace_string = eval("'{}'".format(replace_string))
                replace_string = replace_string.encode()
            elif 'h ' == search_type.lower():
                replace_string = hex_string__to__bytes(replace_string)
            else:
                raise Exception('Unknown replace string type! Use "s " prefix for string value or "h " for HEX value!')
            context.push_result(True, replace_string)

    with is_ok(context, 'dirs for search'):
        if context:
            # DIRS FOR SEARCH
            search_dir_list_raw = last_dir
            search_dir_list = parse_cmd_input_dir_list(search_dir_list_raw)
            context.push_result(True, search_dir_list)

    with is_ok(context, 'extensions to search'):
        if context:
            # EXTENSIONS TO SEARCH
            interested_extensions_raw = last_extensions.strip()
            if '*' == interested_extensions_raw.strip():
                interested_extensions = set()
            else:
                interested_extensions = set(''.join(interested_extensions_raw.split()).split(';'))
            context.push_result(True, interested_extensions)

    with is_ok(context, 'process replace'):
        if context:
            # PROCESS SEARCH
            print()
            print()
            for search_dir in context.read_block_result_link('dirs for search').result:
                replace_in_folder(
                    context.read_block_result_link('search request').result,
                    context.read_block_result_link('replace request').result,
                    search_dir,
                    context.read_block_result_link('extensions to search').result
                )
            context.push_result(True, None)

    with is_ok_reader(context):
        if context:
            print()
            print('Replace is finished!')
            print()
        else:
            print()
            print('Oh! There are errors!')
            print()
            print(str(context))
            print()

    if not IS_RUNNING_IN_PYCHARM:
        print()
        input('Click Enter to exit')


if __name__ == "__main__":
    main()
