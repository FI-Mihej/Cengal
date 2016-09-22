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
    parse_cmd_input_dir_list, bytes__to__hex_string, hex_string__to__bytes, int_to_hex_dword
from file_system import filtered_file_list_traversal, filtered_file_list, FilteringType, change_current_dir
from file_settings_manager.config_manager import *
from text_processing.help_tools import detach_all_slices_from_string, detach_all_slices_from_string__case_insensitive, \
    bytes_to_printable, check_is_slice_is_in_string, check_is_slice_is_in_string__case_insensitive
from code_flow_control.result_types import *
from code_flow_control.smart_chain import *
from IDGenerator import IDGenerator
from various_tools.tools_global_config import KnownExternalEditors
import subprocess

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


mswindows = (sys.platform == "win32")


class FindInFilesGlobalConfig(ConfigManager):
    def __init__(self, immediate_save=True):
        default_content = {
            'find in files': {
                'last search string': '',
                'last dir': '',
                'last extensions': ''
            },
        }
        super(FindInFilesGlobalConfig, self).__init__(['.PythonLibs Settings', 'Various Tools'],
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


def highlight_slice_in_a_bytes_array_with_colorama(data_line, search_string, colorama_color, case_insensitive=True):
    function__detach = detach_all_slices_from_string
    if case_insensitive:
        function__detach = detach_all_slices_from_string__case_insensitive

    split_data_line = function__detach(data_line, search_string)
    data_string = str()
    for part in split_data_line[0]:
        data_string += '{}{}{}{}'.format(
            bytes_to_printable(part[0]),
            colorama_color,
            bytes_to_printable(part[1]),
            colorama.Style.RESET_ALL)
    data_string += bytes_to_printable(split_data_line[1])
    return data_string


def search_in_folder(search_string, search_dir, interested_extensions, line_id_generator, lines_dict,
                     case_insensitive=True):
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
                    with open(full_file_name, 'rb') as file:
                        data = file.read()
                        # print(data[0:30])
                        if function__check_is_in(search_string, data):
                            print('>> {}{}{}'.format(colorama.Fore.YELLOW,
                                                     full_file_name,
                                                     colorama.Style.RESET_ALL))
                            data_lines = data.split(b'\n')
                            index = 1
                            for data_line in data_lines:
                                if function__check_is_in(search_string, data_line):
                                    data_string = highlight_slice_in_a_bytes_array_with_colorama(
                                        data_line, search_string, colorama.Fore.CYAN, case_insensitive)
                                    current_line_id = int_to_hex_dword(line_id_generator.get_new_ID()).lstrip('0')
                                    current_line_info = (full_file_name, index)
                                    lines_dict[current_line_id] = current_line_info
                                    line_text_template = '    # {}{}{}   Line {}{}{}: {}'
                                    print(line_text_template.format(colorama.Fore.MAGENTA,
                                                                    current_line_id,
                                                                    colorama.Style.RESET_ALL,
                                                                    colorama.Fore.GREEN,
                                                                    index,
                                                                    colorama.Style.RESET_ALL,
                                                                    data_string
                                                                    ))
                                index += 1
                            print()
                except PermissionError:
                    print('{}PermissionError{}: {}{}{}'.format(colorama.Fore.RED,
                                                               colorama.Style.RESET_ALL,
                                                               colorama.Fore.MAGENTA,
                                                               full_file_name,
                                                               colorama.Style.RESET_ALL
                                                               ))


def run_editor_on_line(cmd_template, editor_path, file_path, line):
    line = str(line)
    if '%exe%' in cmd_template:
        cmd_template = cmd_template.replace('%exe%', editor_path)
    if '%file%' in cmd_template:
        cmd_template = cmd_template.replace('%file%', file_path)
    if '%line%' in cmd_template:
        cmd_template = cmd_template.replace('%line%', line)

    creation_flags = None
    if mswindows:
        creation_flags = subprocess.CREATE_NEW_CONSOLE
    call_result = subprocess.Popen(cmd_template,
                                   stdout=subprocess.DEVNULL,
                                   stdin=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL,
                                   creationflags=creation_flags
                                   )
    return call_result


def main():
    if not IS_RUNNING_IN_PYCHARM:
        colorama.init()

    # if check_help_request():
    #     sys.exit(0)
    check_help_request()

    context = IsOK_ContextHolder('Find In Files', 'main',
                                 ResultType(CriteriaType.optional,
                                            {'get editor',
                                             'run editor',
                                             'wait for last user input'}))

    global_config = FindInFilesGlobalConfig()
    last_search_string = global_config.get_property('find in files', 'last search string') or ''
    last_dir = global_config.get_property('find in files', 'last dir') or ''
    last_extensions = global_config.get_property('find in files', 'last extensions') or ''

    with is_ok(context, 'get editor'):
        if context:
            known_external_editors = KnownExternalEditors()
            default_editor = known_external_editors.get_property('known external editors', 'default editor')
            path_to_editor_exe = known_external_editors.get_property(
                'known external editors', 'path to {} exe'.format(default_editor))
            editor_cmd_template = known_external_editors.get_property(
                'known external editors', '{} cmd template'.format(default_editor))
            if (len(path_to_editor_exe) > 0) and (len(editor_cmd_template) > 0):
                block_result = (path_to_editor_exe, editor_cmd_template, default_editor)
                context.push_result(True, block_result)

    with is_ok(context, 'search request'):
        if context:
            print()
            search_string = input('Enter search text with "s ", "se " or "h " prefix '
                                  'or leave empty to use last used value ({}): '.format(last_search_string))
            if len(search_string) == 0:
                search_string = last_search_string
            global_config.set_property('find in files', 'last search string', search_string)
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

    with is_ok(context, 'dirs for search'):
        if context:
            print()
            search_dir_list_raw = input('Choose a search dir (S:\\ome\\Dir\\Name), (["S:\\ome\\Dir"], ["D:\\ir"], ["K:"]) or '
                                        'leave empty to use last used dir ({}): '.format(last_dir))
            if len(search_dir_list_raw) == 0:
                search_dir_list_raw = last_dir
            global_config.set_property('find in files', 'last dir', search_dir_list_raw)
            search_dir_list = parse_cmd_input_dir_list(search_dir_list_raw)
            context.push_result(True, search_dir_list)

    with is_ok(context, 'extensions to search'):
        if context:
            print()
            interested_extensions_raw = input('Enter extensions set (".txt.; .u;.;; .jpg"), (";"), ("*") '
                                              'or leave empty to use last used value ({}): '.format(last_extensions))
            interested_extensions = None
            if len(interested_extensions_raw.strip()) == 0:
                interested_extensions_raw = last_extensions.strip()
            global_config.set_property('find in files', 'last extensions', interested_extensions_raw)
            if '*' == interested_extensions_raw.strip():
                interested_extensions = set()
            else:
                interested_extensions = set(''.join(interested_extensions_raw.split()).split(';'))
            context.push_result(True, interested_extensions)

    with is_ok(context, 'process search'):
        if context:
            print()
            print()
            lines_dict = dict()
            line_id_generator = IDGenerator()
            line_id_generator.counter = 1
            for search_dir in context.read_block_result_link('dirs for search').result:
                search_in_folder(
                    context.read_block_result_link('search request').result,
                    search_dir,
                    context.read_block_result_link('extensions to search').result,
                    line_id_generator,
                    lines_dict
                    )
            context.push_result(True, lines_dict)

    with is_ok_reader(context):
        if context:
            print()
            print('Search is finished!')
            print()
        else:
            print()
            print('Oh! There are errors!')
            print()
            print(str(context))
            print()

    with is_ok(context, 'run editor', None, ResultType(CriteriaType.needed, {'get editor', 'process search'})):
        if context:
            lines_dict = context.read_block_result_link('process search').result
            if len(lines_dict) > 0:
                while True:
                    print()
                    print('{}Enter Line ID{} {}#{} {}to open in editor (or press Enter to exit):{}'.format(
                        colorama.Fore.YELLOW, colorama.Style.RESET_ALL, colorama.Fore.MAGENTA, colorama.Style.RESET_ALL,
                        colorama.Fore.YELLOW, colorama.Style.RESET_ALL))
                    line_id = input().strip()
                    if len(line_id) == 0:
                        break

                    try:
                        path_to_editor_exe, editor_cmd_template, default_editor = \
                            context.read_block_result_link('get editor').result
                        full_file_name, line_number = lines_dict[line_id]
                        with change_current_dir(os.path.dirname(full_file_name)):
                            run_editor_on_line(editor_cmd_template,
                                               path_to_editor_exe,
                                               os.path.basename(full_file_name),
                                               line_number)
                    except KeyError:
                        print()
                        print('{}Wrong Line ID{} (# {}{}{})!'.format(
                            colorama.Fore.LIGHTRED_EX,
                            colorama.Style.RESET_ALL,
                            colorama.Fore.MAGENTA,
                            line_id,
                            colorama.Style.RESET_ALL))
                    except OSError as err:
                        default_editor = context.read_block_result_link('get editor').result[2].upper()
                        print()
                        print('{}Error in launching editor{} "{}": {}!'.format(
                            colorama.Fore.LIGHTRED_EX,
                            colorama.Style.RESET_ALL,
                            default_editor,
                            err))

                context.push_result(True, None)

    with is_ok(context, 'wait for last user input', None, ResultType(CriteriaType.forbidden, {'run editor'})):
        if context:
            if not IS_RUNNING_IN_PYCHARM:
                print()
                input('Click Enter to exit')
            context.push_result(True, None)

    with is_ok_reader(context, close=True):
        good_exit = False
        if context:
            if context.read_block_result_link('run editor').existence or \
                    context.read_block_result_link('wait for last user input').existence:
                good_exit = True

        if good_exit:
            print()
            print('App is finished!')
            print()
        else:
            print()
            print('Oh! There are errors!')
            print()
            print(str(context))
            print()


if __name__ == "__main__":
    main()
