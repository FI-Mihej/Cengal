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


__all__ = ['change_version']


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


from cengal.file_system.file_manager import path_relative_to_current_src
from cengal.text_processing.brackets_processing import BracketPair, Bracket
from cengal.build_tools.ensure_copyright import get_version, set_version
from cengal.os.execute import prepare_py_command
from os import system
from typing import List, Union


default_credits_bracket_pair: BracketPair = BracketPair([Bracket('credits_string =')], [Bracket('credits_string_bracket_pair: BracketPair =')])
default_version_bracket_pair: BracketPair = BracketPair([Bracket('__version__ = "')], [Bracket('"')])


def change_version(credits_string_bracket_pair: BracketPair, version_bracket_pair: BracketPair):
    credits_string_bracket_pair = default_credits_bracket_pair if credits_string_bracket_pair is None else credits_string_bracket_pair
    version_bracket_pair = default_version_bracket_pair if version_bracket_pair is None else version_bracket_pair

    script_file_full_path: str = path_relative_to_current_src('../ensure_copyright/ensure_copyright.py')
    version: str = get_version(script_file_full_path, credits_string_bracket_pair, version_bracket_pair)
    if not version:
        raise ValueError('Version not found')
    
    version_str_parts: List[str] = version.split('.')
    version_parts: List[Union[int, str]] = list()
    for version_part in version_str_parts:
        try:
            version_parts.append(int(version_part))
        except ValueError:
            version_parts.append(version_part)

    print(f'Current version: {version}')
    new_version = input('Enter new version or hit Enter to autoincrease: ').strip()
    if not new_version:
        for reverse_index, version_part in enumerate(reversed(version_parts)):
            if isinstance(version_part, int):
                version_parts[-reverse_index - 1] += 1
                break
        
        new_version = '.'.join(str(version_part) for version_part in version_parts)

    set_version(script_file_full_path, new_version, credits_string_bracket_pair, version_bracket_pair)
    print(f'Version changed to: {new_version}')
    print('Updating version in all files...')
    system(prepare_py_command((script_file_full_path,)))
    print('Done.')
