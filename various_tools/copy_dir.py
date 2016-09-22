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
import os
import stat
import os.path
import sys
import shutil, errno
import subprocess
import time
from help_tools import get_text_in_brackets_offset, parse_cmd_input_dir_list, bytes__to__hex_string, \
    hex_string__to__bytes, current_line
from file_system import filtered_file_list_traversal, filtered_file_list, FilteringType, change_current_dir
from file_settings_manager.config_manager import *
from check_is_in_pycharm import IS_RUNNING_IN_PYCHARM
import pickle
import shutil
from file_system.win_fs.global_install_uninstall import global_install as win_fs_global_install, \
    global_uninstall as win_fs_global_uninstall
import traceback
from contextlib import contextmanager
from code_flow_control import ResultExistence
from progress.spinner import Spinner
if 'nt' == os.name:
    import win32console
    import codecs
    import ctypes
    FILE_ATTRIBUTE_HIDDEN = 0x02
    FILE_ATTRIBUTE_READONLY = 0x01
    REMOVABLE_ATTRIBUTES = ~(FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_READONLY)
    WIN_UNICODE_PATH_PREFIX = '\\\\?\\'
    WUPP = WIN_UNICODE_PATH_PREFIX

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
            'copy dir': {
                'dir\'s list': '',
                'destination dir': '',
                'errors dict': '',
                'exceptions dict': '',
                'copied files': ''
            },
        }
        super(GlobalConfig, self).__init__(['.PythonLibs Settings', 'Various Tools'],
                                           default_content=default_content,
                                           immediate_save=immediate_save)


class CopyTreeResult:
    def __init__(self):
        self.errors = list()
        self.exceptions = list()
        self.copied_files = set()

    def extend(self, source):
        self.errors.extend(source.errors)
        self.exceptions.extend(source.exceptions)
        self.copied_files.update(source.copied_files)


def copytree(src, dst, already_copied_files, spinner=None):
    result = CopyTreeResult()

    # WIN_UNICODE_PATH_PREFIX = ''
    # src = WIN_UNICODE_PATH_PREFIX + src
    # dst = WIN_UNICODE_PATH_PREFIX + dst

    names = list()
    try:
        names = os.listdir(src)
        if not os.path.exists(dst):
            # print('LISTDIR "{}"'.format(dst))
            os.makedirs(dst)
            pass
    except:
        exception = sys.exc_info()
        # formatted_traceback = traceback.format_exception(exception[0], exception[1], exception[2])
        # exception = exception[:2] + (formatted_traceback,)
        exception = exception[:2]
        print()
        print('EXCEPTION LISTDIR, when "{}":'.format(src.encode()))
        print(exception)
        print()
        result.exceptions.append((src, exception))

    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            try:
                # print(current_line())
                if os.path.isdir(srcname):
                    # print(current_line())
                    subresult = copytree(srcname, dstname, already_copied_files, spinner=spinner)
                    # print(current_line())
                    result.extend(subresult)
                    # print(current_line())
                else:
                    # print(current_line())
                    if srcname not in already_copied_files:
                        # print(current_line())
                        # print('COPY2 FILE "{}" TO "{}'.format(srcname, dstname))
                        if os.path.exists(dstname) and os.path.isfile(dstname):
                            # print(current_line())
                            if 'nt' == os.name:
                                # print(current_line())
                                file_att = ctypes.windll.kernel32.GetFileAttributesW(WUPP + dstname)
                                # print(current_line())
                                file_att &= REMOVABLE_ATTRIBUTES
                                # print(current_line())

                                ret = ctypes.windll.kernel32.SetFileAttributesW(WUPP + dstname, file_att)
                                # print(current_line())
                                if not ret:
                                    # print(current_line())
                                    # return code of zero indicates failure, raise Windows error
                                    print(ctypes.WinError())
                                    raise ctypes.WinError()
                                # print(current_line())

                                # ret = ctypes.windll.kernel32.DeleteFile(WUPP + dstname)
                                # if not ret:
                                #     # return code of zero indicates failure, raise Windows error
                                #     print(ctypes.WinError())
                                #     raise ctypes.WinError()
                            else:
                                # print(current_line())
                                file_att = os.stat(dstname)[0]
                                # print(current_line())
                                if not (file_att & stat.S_IWRITE):
                                    # print(current_line())
                                    # File is read-only, so make it writeable
                                    os.chmod(dstname, stat.S_IWRITE)
                                # print(current_line())
                                # os.remove(dstname)
                        # print(current_line())
                        shutil.copy2(srcname, dstname)
                        # print(current_line())
                        result.copied_files.add(srcname)
                        # print(current_line())
                        # if spinner is not None:
                        #     # print(current_line())
                        #     spinner.next()
                        #     # print(current_line())
                # XXX What about devices, sockets etc.?
            except OSError as why:
                print('ERROR {}, when "{}" -> "{}": "{}"'.format('OSError', srcname.encode(), dstname, why))
                result.errors.append((srcname, dstname, str(why)))
                raise
            # catch the Error from the recursive copytree so that we can
            # continue with other files
            except shutil.Error as err:
                print('ERROR {}, when "{}" -> "{}": "{}"'.format('Error', srcname.encode(), dstname, err))
                result.errors.extend(err.args[0])
                raise
        except:
            exception = sys.exc_info()
            # formatted_traceback = traceback.format_exception(exception[0], exception[1], exception[2])
            # exception = exception[:2] + (formatted_traceback,)
            exception = exception[:2]
            print()
            print('EXCEPTION, when "{}" -> "{}":'.format(srcname.encode(), dstname))
            print(exception)
            print()
            result.exceptions.append((srcname, exception))
    try:
        try:
            # print('COPYSTAT "{}" TO "{}'.format(src, dst))
            shutil.copystat(src, dst)
            pass
        except OSError as why:
            # can't copy file access times on Windows
            if why.winerror is None:
                print('ERROR COPYSTAT {}, when "{}" -> "{}": "{}"'.format('OSError', src.encode(), dst, why))
                result.errors.extend((src, dst, str(why)))
                raise
            else:
                print('ERROR COPYSTAT WINERROR {}, when "{}" -> "{}": "{}"'.format('OSError', src.encode(), dst, why))
    except:
        exception = sys.exc_info()
        # formatted_traceback = traceback.format_exception(exception[0], exception[1], exception[2])
        # exception = exception[:2] + (formatted_traceback,)
        exception = exception[:2]
        print()
        print('EXCEPTION COPYSTAT, when "{}" -> "{}":'.format(src.encode(), dst))
        print(exception)
        print()
        result.exceptions.append((src, exception))

    return result


@contextmanager
def change_console_output_cp(new_output_cp=None, new_input_cp=None, encoding_error=None):
    '''
    :param new_output_cp: ResultExistence(True, (65001, 'utf-8))
    :param new_input_cp: ResultExistence(True, (65001, 'utf-8))
    :return:
    '''
    encoding_error = encoding_error or 'replace'
    cur_output_cp = None
    cur_input_cp = None
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    original_stdin = sys.stdin
    if 'nt' == os.name:
        if not IS_RUNNING_IN_PYCHARM:
            if (new_output_cp is not None) and new_output_cp.existence:
                sys.stdout = codecs.getwriter(new_output_cp.result[1])(sys.stdout.buffer, encoding_error)
                sys.stderr = codecs.getwriter(new_output_cp.result[1])(sys.stderr.buffer, encoding_error)
                cur_output_cp = win32console.GetConsoleOutputCP()
                win32console.SetConsoleOutputCP(new_output_cp.result[0])
            if (new_input_cp is not None) and new_input_cp.existence:
                sys.stdin = codecs.getwriter(new_input_cp.result[1])(sys.stdin.buffer, encoding_error)
                cur_input_cp = win32console.GetConsoleOutputCP()
                win32console.SetConsoleCP(new_input_cp.result[0])
    try:
        yield
    except:
        raise
    finally:
        if 'nt' == os.name:
            if not IS_RUNNING_IN_PYCHARM:
                if (new_output_cp is not None) and new_output_cp.existence:
                    win32console.SetConsoleOutputCP(cur_output_cp)
                    sys.stderr = original_stderr
                    sys.stdout = original_stdout
                if (new_input_cp is not None) and new_input_cp.existence:
                    sys.stdin = original_stdin
                    win32console.SetConsoleCP(cur_input_cp)


def main():
    if 'nt' == os.name:
        win_fs_global_install()

    try:
        global_config = GlobalConfig()
        raw_source_dirs_list = global_config.get_property('copy dir', 'dir\'s list') or ''
        raw_destination_dir = global_config.get_property('copy dir', 'destination dir') or ''
        raw_errors_dict = global_config.get_property('copy dir', 'errors dict') or ''
        raw_exceptions_dict = global_config.get_property('copy dir', 'exceptions dict') or ''
        raw_copied_files = global_config.get_property('copy dir', 'copied files') or ''

        errors_dict = dict()
        raw_errors_dict = raw_errors_dict.strip()
        if len(raw_errors_dict) > 0:
            errors_dict = hex_string__to__bytes(raw_errors_dict)
            errors_dict = pickle.loads(errors_dict)

        exceptions_dict = dict()
        raw_exceptions_dict = raw_exceptions_dict.strip()
        if len(raw_exceptions_dict) > 0:
            exceptions_dict = hex_string__to__bytes(raw_exceptions_dict)
            exceptions_dict = pickle.loads(exceptions_dict)

        copied_files = set()
        raw_copied_files = raw_copied_files.strip()
        if len(raw_copied_files) > 0:
            copied_files = hex_string__to__bytes(raw_copied_files)
            copied_files = pickle.loads(copied_files)

        may_use_already_copied_files_cache = True

        # DIRS FOR COPYING
        input_raw_source_dirs_list = input('Choose a SOURCE dir list (S:\\ome\\Dir\\Name), (["S:\\ome\\Dir"], '
                                           '["D:\\ir"], ["K:"]) or leave empty to use last used dir '
                                           '({}): '.format(raw_source_dirs_list))
        input_raw_source_dirs_list = input_raw_source_dirs_list.strip()
        if len(input_raw_source_dirs_list) == 0:
            input_raw_source_dirs_list = raw_source_dirs_list
        else:
            may_use_already_copied_files_cache = False
        global_config.set_property('copy dir', 'dir\'s list', input_raw_source_dirs_list)
        source_dir_list = parse_cmd_input_dir_list(input_raw_source_dirs_list)

        # DESTINATION DIR
        input_raw_destination_dir = input('Choose a DESTINATION dir (S:\\ome\\Dir\\Name) or '
                                    'leave empty to use last used dir ({}): '.format(raw_destination_dir))
        input_raw_destination_dir = input_raw_destination_dir.strip()
        if len(input_raw_destination_dir) == 0:
            input_raw_destination_dir = raw_destination_dir
        else:
            may_use_already_copied_files_cache = False
        global_config.set_property('copy dir', 'destination dir', input_raw_destination_dir)
        destination_dir = input_raw_destination_dir

        # if not may_use_already_copied_files_cache:
        #     copied_files = set()

        # PROCESS COPY PROCESS
        # spinner = Spinner('Loading ')
        spinner = None
        with change_console_output_cp(ResultExistence(True, (65001, 'utf-8'))):
            copy_result = CopyTreeResult()
            for source_dir in source_dir_list:
                copy_sub_result = copytree(source_dir, destination_dir, copied_files, spinner=spinner)
                copy_result.extend(copy_sub_result)
        print()
        print()

        print('============')
        print(' >> CURRENT SET COPIED FILES: {}'.format(len(copy_result.copied_files)))

        copied_files.update(copy_result.copied_files)
        print(' >> ALL SET COPIED FILES: {}'.format(len(copied_files)))
        raw_copied_files = pickle.dumps(copied_files)
        raw_copied_files = bytes__to__hex_string(raw_copied_files)
        global_config.set_property('copy dir', 'copied files', raw_copied_files)

        print(' >> ERRORS QNT: {}'.format(len(copy_result.errors)))
        raw_errors_dict = pickle.dumps(copy_result.errors)
        raw_errors_dict = bytes__to__hex_string(raw_errors_dict)
        global_config.set_property('copy dir', 'errors dict', raw_errors_dict)

        print(' >> EXCEPTIONS QNT: {}'.format(len(copy_result.exceptions)))
        raw_exceptions_dict = pickle.dumps(copy_result.exceptions)
        raw_exceptions_dict = bytes__to__hex_string(raw_exceptions_dict)
        global_config.set_property('copy dir', 'exceptions dict', raw_exceptions_dict)

        if not IS_RUNNING_IN_PYCHARM:
            print()
            input('Click Enter to exit')
    except:
        raise
    finally:
        if 'nt' == os.name:
                win_fs_global_uninstall()

if __name__ == "__main__":
    main()
