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

import sys
import os
from contextlib import contextmanager, redirect_stdout, redirect_stderr
from cengal.system import IS_RUNNING_IN_PYCHARM
if 'nt' == os.name:
    import win32console
    import codecs


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


# if 'nt' == os.name:
#     @contextmanager
#     def change_console_output_cp(new_output_cp=None, new_input_cp=None, encoding_error=None):
#         """
#         :param new_output_cp: ResultExistence(True, (65001, 'utf-8))
#         :param new_input_cp: ResultExistence(True, (65001, 'utf-8))
#         :return:
#         """
#         encoding_error = encoding_error or 'replace'
#         cur_output_cp = None
#         cur_input_cp = None
#         cur_output_cp_name = str()
#         cur_input_cp_name = str()
#         original_stdout = sys.stdout
#         original_stderr = sys.stderr
#         original_stdin = sys.stdin
#         original_stdout_fileno = sys.stdout.fileno()
#         original_stderr_fileno = sys.stderr.fileno()
#         original_stdin_fileno = sys.stdin.fileno()
#         if 'nt' == os.name:
#             if not IS_RUNNING_IN_PYCHARM:
#                 cur_output_cp = win32console.GetConsoleOutputCP()
#                 cur_output_cp_name = sys.stdout.encoding
#                 if (new_output_cp is not None) and new_output_cp.existence:
#                     # sys.stdout = codecs.getwriter(new_output_cp.result[1])(sys.stdout.buffer, encoding_error)
#                     # sys.stderr = codecs.getwriter(new_output_cp.result[1])(sys.stderr.buffer, encoding_error)
#                     # sys.stdout = codecs.getwriter(new_output_cp.result[1])(sys.stdout.detach(), encoding_error)
#                     # sys.stderr = codecs.getwriter(new_output_cp.result[1])(sys.stderr.detach(), encoding_error)
#                     sys.stdout = open(original_stdout_fileno, mode='w', encoding=new_output_cp.result[1], buffering=1)
#                     print('stdout:', sys.stdout.encoding)
#                     sys.stderr = open(original_stderr_fileno, mode='w', encoding=new_output_cp.result[1], buffering=1)
#                     print('stderr:', sys.stderr.encoding)
#                     win32console.SetConsoleOutputCP(new_output_cp.result[0])
#                     print('conout:', win32console.GetConsoleOutputCP())
#                 cur_input_cp = win32console.GetConsoleCP()
#                 cur_input_cp_name = sys.stdin.encoding
#                 if (new_input_cp is not None) and new_input_cp.existence:
#                     # sys.stdin = codecs.getwriter(new_input_cp.result[1])(sys.stdin.buffer, encoding_error)
#                     sys.stdin = open(original_stdin_fileno, mode='r', encoding=new_input_cp.result[1], buffering=1)
#                     print('stdin:', sys.stdin.encoding)
#                     win32console.SetConsoleCP(new_input_cp.result[0])
#                     print('conin:', win32console.GetConsoleOutputCP())
#         try:
#             yield ((cur_input_cp, cur_output_cp), (cur_input_cp_name, cur_output_cp_name))
#         except:
#             raise
#         finally:
#             if 'nt' == os.name:
#                 if not IS_RUNNING_IN_PYCHARM:
#                     if (new_output_cp is not None) and new_output_cp.existence:
#                         win32console.SetConsoleOutputCP(cur_output_cp)
#                         print('conout:', win32console.GetConsoleOutputCP())
#                         # sys.stdout.close()
#                         # sys.stdout = original_stdout
#                         # sys.stderr = original_stderr
#                         # sys.stdout = open(original_stdout_fileno, mode='w', encoding=cur_output_cp_name, buffering=1)
#                         print('stdout:', sys.stdout.encoding)
#                         # sys.stderr.close()
#                         # sys.stderr = open(original_stderr_fileno, mode='w', encoding=cur_output_cp_name, buffering=1)
#                         print('stderr:', sys.stderr.encoding)
#                     if (new_input_cp is not None) and new_input_cp.existence:
#                         win32console.SetConsoleCP(cur_input_cp)
#                         print('conin:', win32console.GetConsoleOutputCP())
#                         # sys.stdin.close()
#                         # sys.stdin = original_stdin
#                         # sys.stdin = open(original_stdin_fileno, mode='r', encoding=cur_input_cp_name, buffering=1)
#                         print('stdin:', sys.stdin.encoding)
# else:
#     @contextmanager
#     def change_console_output_cp(new_output_cp=None, new_input_cp=None, encoding_error=None):
#         yield None


def fileno(file_or_fd):
    fd = getattr(file_or_fd, 'fileno', lambda: file_or_fd)()
    if not isinstance(fd, int):
        raise ValueError("Expected a file (`.fileno()`) or a file descriptor")
    return fd


if 'nt' == os.name:
    @contextmanager
    def change_console_output_cp(new_output_cp=None, new_input_cp=None, encoding_error=None):
        """
        :param new_output_cp: ResultExistence(True, (65001, 'utf-8))
        :param new_input_cp: ResultExistence(True, (65001, 'utf-8))
        :return:
        """
        encoding_error = encoding_error or 'replace'
        cur_output_cp = None
        cur_input_cp = None
        cur_output_cp_name = str()
        cur_input_cp_name = str()
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        original_stdin = sys.stdin
        original_stdout_fileno = sys.stdout.fileno()
        original_stderr_fileno = sys.stderr.fileno()
        original_stdin_fileno = sys.stdin.fileno()
        new_stdout = None
        new_stderr = None
        new_stdin = None
        if 'nt' == os.name:
            if IS_RUNNING_IN_PYCHARM:
                yield None
            else:
                with os.fdopen(os.dup(original_stdout_fileno), 'wb') as copied_stdout, \
                        os.fdopen(os.dup(original_stderr_fileno), 'wb') as copied_stderr, \
                        os.fdopen(os.dup(original_stdin_fileno), 'rb') as copied_stdin, \
                        os.fdopen(os.dup(original_stdout_fileno), 'wb') as copied_stdout_buff, \
                        os.fdopen(os.dup(original_stderr_fileno), 'wb') as copied_stderr_buff, \
                        os.fdopen(os.dup(original_stdin_fileno), 'rb') as copied_stdin_buff:
                    # copied_stdout = os.fdopen(os.dup(original_stdout_fileno), 'wb')
                    # copied_stderr = os.fdopen(os.dup(original_stderr_fileno), 'wb')
                    # copied_stdin = os.fdopen(os.dup(original_stdin_fileno), 'wb')
                    # copied_stdout_buff = os.fdopen(os.dup(original_stdout_fileno), 'wb')
                    # copied_stderr_buff = os.fdopen(os.dup(original_stderr_fileno), 'wb')
                    # copied_stdin_buff = os.fdopen(os.dup(original_stdin_fileno), 'wb')
                    original_stdout.flush()
                    original_stderr.flush()
                    original_stdin.flush()

                    cur_output_cp = win32console.GetConsoleOutputCP()
                    cur_output_cp_name = sys.stdout.encoding
                    if (new_output_cp is not None) and new_output_cp.existence:
                        new_stdout = open(copied_stdout.fileno(), mode='w', encoding=new_output_cp.result[1],
                                          buffering=1)
                        sys.stdout = new_stdout
                        # print('stdout:', sys.stdout.encoding)
                        new_stderr = open(copied_stderr.fileno(), mode='w', encoding=new_output_cp.result[1],
                                          buffering=1)
                        sys.stderr = new_stderr
                        # print('stderr:', sys.stderr.encoding)
                        win32console.SetConsoleOutputCP(new_output_cp.result[0])
                        # print('conout:', win32console.GetConsoleOutputCP())
                    cur_input_cp = win32console.GetConsoleCP()
                    cur_input_cp_name = sys.stdin.encoding
                    if (new_input_cp is not None) and new_input_cp.existence:
                        new_stdin = open(copied_stdin.fileno(), mode='r', encoding=new_input_cp.result[1],
                                         buffering=1)
                        sys.stdin = new_stdin
                        # print('stdin:', sys.stdin.encoding)
                        win32console.SetConsoleCP(new_input_cp.result[0])
                        # print('conin:', win32console.GetConsoleOutputCP())
                    try:
                        yield ((cur_input_cp, cur_output_cp), (cur_input_cp_name, cur_output_cp_name))
                    except:
                        raise
                    finally:
                        sys.stdout.flush()
                        sys.stderr.flush()
                        sys.stdin.flush()

                        if (new_output_cp is not None) and new_output_cp.existence:
                            win32console.SetConsoleOutputCP(cur_output_cp)
                            # print('conout:', win32console.GetConsoleOutputCP())
                            os.dup2(copied_stdout_buff.fileno(), original_stdout_fileno)
                            sys.stdout = original_stdout
                            # print('stdout:', sys.stdout.encoding)
                            os.dup2(copied_stderr_buff.fileno(), original_stderr_fileno)
                            sys.stderr = original_stderr
                            # print('stderr:', sys.stderr.encoding)
                        if (new_input_cp is not None) and new_input_cp.existence:
                            win32console.SetConsoleCP(cur_input_cp)
                            # print('conin:', win32console.GetConsoleOutputCP())
                            os.dup2(copied_stdin_buff.fileno(), original_stdin_fileno)
                            sys.stdin = original_stdin
                            # print('stdin:', sys.stdin.encoding)
        else:
            yield None
else:
    @contextmanager
    def change_console_output_cp(new_output_cp=None, new_input_cp=None, encoding_error=None):
        yield None
