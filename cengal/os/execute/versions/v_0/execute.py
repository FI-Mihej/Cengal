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
__version__ = "4.2.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.system import OS_TYPE

import os
import sys
from typing import Sequence, Union, List


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


def prepare_py_params(params: Sequence[str]) -> List[str]:
    result: List[str] = [handle_spaces(sys.executable)]
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


def prepare_py_command(params: Union[str, Sequence[str]] = None) -> str:
    return prepare_command(sys.executable, params)
