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


__all__ = [
    'ensure_popen_params',
    'run_self',
    'popen_self',
    'ensure_environment_implicit',
    'ensure_environment_explicit',
    'ensure_environment',
]


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.text_processing.brackets_processing import BracketPair, find_text_in_brackets, replace_text_in_brackets
from cengal.introspection.inspect import exception_to_printable_text
from cengal.os.process.prepare_cmd_line import prepare_py_params

import os
import sys
import threading
import subprocess

from typing import Optional, List, Dict, Set, Tuple, Callable


def ensure_popen_params(
        *popen_args, 
        set_env_var: Optional[Dict[str, str]] = None,
        del_env_var: Optional[Set[str]] = None,
        preface_with_cmd_line_args: Optional[List[str]] = None,
        end_with_cmd_line_args: Optional[List[str]] = None,
        remove_cmd_line_args: Optional[List[str]] = None,
        change_cmd_line_args: Optional[List[Tuple[BracketPair, str, int]]] = None,
        **kwargs
        ) -> Tuple:
    changed: bool = False

    set_env_var = dict() if set_env_var is None else set_env_var
    del_env_var = list() if del_env_var is None else del_env_var
    
    provided_env: Dict = kwargs.get('env', None)
    new_env: Dict = os.environ.copy() if provided_env is None else provided_env
    for env_var_name, env_var_value in set_env_var.items():
        if env_var_name in new_env:
            if env_var_value == new_env[env_var_name]:
                continue
            else:
                changed = True
        else:
            changed = True
        
        new_env[env_var_name] = env_var_value
        
    new_env.update(set_env_var)
    for env_var_name in del_env_var:
        if env_var_name in new_env:
            del new_env[env_var_name]
            changed = True
    
    kwargs['env'] = new_env

    if popen_args:
        if 1 == len(popen_args):
            args = popen_args[0]
        else:
            for arg in popen_args:
                if not isinstance(arg, str):
                    raise ValueError('`*popen_args` arguments can be either single `str`/`List[str]` argument or several `str` arguments')
            
            args = list(popen_args)
    else:
        args = sys.argv.copy()

    preface_with_cmd_line_args = preface_with_cmd_line_args or list()
    end_with_cmd_line_args = end_with_cmd_line_args or list()
    remove_cmd_line_args = remove_cmd_line_args or list()
    change_cmd_line_args = change_cmd_line_args or list()

    args_set: Set[str] = set(args)
    additional_args: Set[str] = set(preface_with_cmd_line_args + end_with_cmd_line_args)
    if bool(additional_args - args_set):
        changed = True

    args = preface_with_cmd_line_args + args + end_with_cmd_line_args

    args_set: Set[str] = set(args)
    removable_args: Set[str] = set(remove_cmd_line_args)
    if bool(removable_args & args_set):
        changed = True

    new_args = list()
    for arg in args:
        if arg not in removable_args:
            new_args.append(arg)
    
    args = new_args

    for bracket_pair, value, count in change_cmd_line_args:
        for arg_index in range(len(args)):
            arg = args[arg_index]
            if find_text_in_brackets(arg, bracket_pair) is not None:
                data, result = replace_text_in_brackets(arg, bracket_pair, value, count)
                for old_text_slice, new_text_slice in result:
                    old_text_value = arg[old_text_slice]
                    if old_text_value != value:
                        changed = True
                
                args[arg_index] = data
    
    args = prepare_py_params(args, sys.executable)
    return (args,), kwargs, changed


def run_self(
        *run_args, 
        set_env_var: Optional[Dict[str, str]] = None,
        del_env_var: Optional[Set[str]] = None,
        preface_with_cmd_line_args: Optional[List[str]] = None,
        end_with_cmd_line_args: Optional[List[str]] = None,
        remove_cmd_line_args: Optional[List[str]] = None,
        change_cmd_line_args: Optional[List[Tuple[BracketPair, str, int]]] = None,
        **kwargs
        ) -> subprocess.CompletedProcess:
    args, kwargs, changed = ensure_popen_params(
        *run_args, 
        set_env_var=set_env_var, 
        del_env_var=del_env_var, 
        preface_with_cmd_line_args=preface_with_cmd_line_args, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        remove_cmd_line_args=remove_cmd_line_args, 
        change_cmd_line_args=change_cmd_line_args, 
        **kwargs
        )
    return subprocess.run(*args, **kwargs), changed


def popen_self(
        *popen_args, 
        set_env_var: Optional[Dict[str, str]] = None,
        del_env_var: Optional[Set[str]] = None,
        preface_with_cmd_line_args: Optional[List[str]] = None,
        end_with_cmd_line_args: Optional[List[str]] = None,
        remove_cmd_line_args: Optional[List[str]] = None,
        change_cmd_line_args: Optional[List[Tuple[BracketPair, str, int]]] = None,
        **kwargs
        ) -> subprocess.Popen:
    args, kwargs, changed = ensure_popen_params(
        *popen_args, 
        set_env_var=set_env_var, 
        del_env_var=del_env_var, 
        preface_with_cmd_line_args=preface_with_cmd_line_args, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        remove_cmd_line_args=remove_cmd_line_args, 
        change_cmd_line_args=change_cmd_line_args, 
        **kwargs
        )
    return subprocess.Popen(*args, **kwargs), changed


def ensure_environment_implicit(
        *run_args, 
        execution_allowed: Optional[Callable] = None,
        set_env_var: Optional[Dict[str, str]] = None,
        del_env_var: Optional[Set[str]] = None,
        preface_with_cmd_line_args: Optional[List[str]] = None,
        end_with_cmd_line_args: Optional[List[str]] = None,
        remove_cmd_line_args: Optional[List[str]] = None,
        change_cmd_line_args: Optional[List[Tuple[BracketPair, str, int]]] = None,
        **kwargs
        ) -> None:
    args, kwargs, changed = ensure_popen_params(
        *run_args, 
        set_env_var=set_env_var, 
        del_env_var=del_env_var, 
        preface_with_cmd_line_args=preface_with_cmd_line_args, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        remove_cmd_line_args=remove_cmd_line_args, 
        change_cmd_line_args=change_cmd_line_args, 
        **kwargs
        )
    if not (((execution_allowed is None) or ((execution_allowed is not None) and execution_allowed())) and changed):
        return

    process: subprocess.CompletedProcess = subprocess.run(*args, **kwargs)
    sys.exit(process.returncode)


def ensure_environment_explicit(
        *popen_args, 
        execution_allowed: Optional[Callable] = None,
        set_env_var: Optional[Dict[str, str]] = None,
        del_env_var: Optional[Set[str]] = None,
        preface_with_cmd_line_args: Optional[List[str]] = None,
        end_with_cmd_line_args: Optional[List[str]] = None,
        remove_cmd_line_args: Optional[List[str]] = None,
        change_cmd_line_args: Optional[List[Tuple[BracketPair, str, int]]] = None,
        timeout: Optional[float] = 0.1,
        **kwargs
        ) -> None:
    args, kwargs, changed = ensure_popen_params(
        *popen_args, 
        set_env_var=set_env_var, 
        del_env_var=del_env_var, 
        preface_with_cmd_line_args=preface_with_cmd_line_args, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        remove_cmd_line_args=remove_cmd_line_args, 
        change_cmd_line_args=change_cmd_line_args, 
        **kwargs
        )
    if not (((execution_allowed is None) or ((execution_allowed is not None) and execution_allowed())) and changed):
        return

    kwargs['stdin'] = subprocess.PIPE
    kwargs['stdout'] = subprocess.PIPE
    kwargs['stderr'] = subprocess.PIPE
    process: subprocess.Popen = subprocess.Popen(*args, **kwargs)
    stop: bool = False

    def forward_input():
        try:
            while not stop:
                input_data = sys.stdin.read(1)
                if stop:
                    break

                if not input_data:
                    break

                process.stdin.write(input_data.encode())
                process.stdin.flush()
        except Exception as er:
            process.terminate()
            print(f"Input forwarding error:\n{exception_to_printable_text(er)}", file=sys.stderr)

    def forward_output(pipe, output_stream):
        try:
            while True:
                output_data = pipe.read(1)
                if not output_data:
                    break

                output_stream.write(output_data)
                output_stream.flush()
        except Exception as er:
            process.terminate()
            print(f"Output forwarding error:\n{exception_to_printable_text(er)}", file=sys.stderr)

    input_thread = threading.Thread(target=forward_input, daemon=True)
    stdout_thread = threading.Thread(target=forward_output, args=(process.stdout, sys.stdout.buffer), daemon=True)
    stderr_thread = threading.Thread(target=forward_output, args=(process.stderr, sys.stderr.buffer), daemon=True)

    input_thread.start()
    stdout_thread.start()
    stderr_thread.start()

    return_code: int = 1
    try:
        return_code = process.wait()
    except subprocess.SubprocessError as er:
        print(f"Subprocess error:\n{exception_to_printable_text(er)}", file=sys.stderr)
    except Exception as er:
        print(f"Unexpected error:\n{exception_to_printable_text(er)}", file=sys.stderr)
    finally:
        stop = True
        stdout_thread.join()
        stderr_thread.join()
        input_thread.join(timeout)
        sys.exit(return_code)


ensure_environment = ensure_environment_implicit
