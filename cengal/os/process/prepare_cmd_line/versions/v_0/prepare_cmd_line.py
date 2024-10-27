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
    'ScriptIsFrozenError',
    'escape_text', 
    'handle_spaces', 
    'escape_param', 
    'prepare_params', 
    'prepare_py_params', 
    'prepare_command', 
    'prepare_py_command', 
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


from cengal.code_flow_control.args_manager import ArgsKwargs
from cengal.system import OS_TYPE, IS_FROZEN

import os
import sys
from typing import Sequence, Union, List, Dict, Set, Optional


class ScriptIsFrozenError(Exception):
    """Current script is frozen. There is no way to find its interpreter path.

    Args:
        Exception (_type_): _description_
    """
    pass


def escape_text(text: str) -> str:
    """Resulting text can be used safely inside a brackets:

    param = f'--define:MyVar="{escape_text(param)}"'

    Args:
        text (str): _description_

    Returns:
        str: _description_
    """
    if 'Windows' == OS_TYPE:
        text = text.replace('"', '""')
    else:
        text = text.translate(str.maketrans({'\\': '\\\\', '"': '\\"', '$': '\\$', '`': '\\`'}))

    return text


def handle_spaces(text: str) -> str:
    if ' ' in text:
        if 'Windows' == OS_TYPE:
            # text = '"{}"'.format(text)
            need_to_wrap: bool = False
            start = 0
            while True:
                space_pos = text.find(' ', start)
                if -1 >= space_pos:
                    break

                lbracket_pos = text.find('"', start)
                rbracket_pos = text.find('"', space_pos + 1)
                if (-1 < lbracket_pos) and (-1 < rbracket_pos) and (lbracket_pos < space_pos < rbracket_pos):
                    start = rbracket_pos + 1
                    continue
                else:
                    need_to_wrap = True
                    break
            
            if need_to_wrap:
                text = text.replace('"', '""')
                text = '"{}"'.format(text)
        else:
            # text = text.replace(' ', '\\ ')
            unescaped_spaces: List[int] = list()
            probably_unescaped_spaces: List[int] = list()
            escaped: bool = False
            lbracket_found: bool = False
            for index, char in enumerate(text):
                if escaped:
                    escaped = False
                    continue

                if '\\' == char:
                    escaped = True
                elif ' ' == char:
                    if lbracket_found:
                        probably_unescaped_spaces.append(index)
                    else:
                        unescaped_spaces.append(index)
                elif '"' == char:
                    if lbracket_found:
                        probably_unescaped_spaces.clear()
                        lbracket_found = False
                    else:
                        lbracket_found = True

            unescaped_spaces.extend(probably_unescaped_spaces)
            if unescaped_spaces:
                characters: List[str] = list(text)
                for space_pos in reversed(unescaped_spaces):
                    characters.insert(space_pos, '\\')
                
                text = ''.join(characters)

    return text


def escape_param(text: str) -> str:
    return handle_spaces(escape_text(text))


def prepare_params(params: Sequence[str]) -> List[str]:
    result: List[str] = list()
    for param in params:
        result.append(handle_spaces(param))
    
    return result


def prepare_py_params(params: Sequence[str], interpreter_path: Optional[str] = None) -> List[str]:
    if interpreter_path is None:
        if IS_FROZEN:
            raise ScriptIsFrozenError('Current script is frozen. There is no way to find its interpreter path.')
        else:
            interpreter_path = sys.executable
    
    result: List[str] = [handle_spaces(interpreter_path)]
    for param in params:
        result.append(handle_spaces(param))
    
    return result


def prepare_command(command: str, params: Union[str, Sequence[str]] = None) -> str:
    command = handle_spaces(command)
    params_has_spaces_under_windows: bool = False
    if (params is not None) and (not isinstance(params, str)):
        new_params: List[str] = list()
        for param in params:
            if ('Windows' == OS_TYPE) and ' ' in param:
                params_has_spaces_under_windows = True
                
            new_params.append(handle_spaces(param))

        params = ' '.join(new_params)
    
    if params:
        command = '{} {}'.format(command, params)
        if params_has_spaces_under_windows:
            command = '"{}"'.format(command)
    
    return command


def prepare_py_command(params: Union[str, Sequence[str]] = None, interpreter_path: Optional[str] = None) -> str:
    if interpreter_path is None:
        if IS_FROZEN:
            raise ScriptIsFrozenError('Current script is frozen. There is no way to find its interpreter path.')
        else:
            interpreter_path = sys.executable
    
    return prepare_command(interpreter_path, params)


def adjust_popen_environment(
        popen_args_kwargs: Optional[ArgsKwargs] = None, 
        executable_path: Optional[str] = None, 
        set_env_var: Optional[Dict[str, str]] = None,
        del_env_var: Optional[Set[str]] = None,
        preface_with_cmd_line_args: Optional[List[str]] = None,
        end_with_cmd_line_args  : Optional[List[str]] = None,
        ) -> ArgsKwargs:
    pythonhashseed: int = randint(pythonhashseed_min_value, pythonhashseed_max_value) if pythonhashseed is None else pythonhashseed
    
    new_env: Dict = os.environ.copy()
    new_env[pythonhashseed_env_var_name] = str(pythonhashseed)
    new_env.update(kwargs.get('env', dict()))
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
        args = None

    if add_command_line_parameter:
        if args is None:
            args = sys.argv.copy()
            args.append(same_pythonhashseed_param)
        elif isinstance(args, str):
            args += f' {same_pythonhashseed_param}'
        elif isinstance(args, AbsSequence):
            args = list(args) + [same_pythonhashseed_param]
        else:
            raise ValueError(f'Unsupported {type(args)} type of an `args` argument: {args=}')
    
    args = prepare_py_command(args, sys.executable)
    return ArgsKwargs(args, **kwargs)
