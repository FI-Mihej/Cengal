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

import colorama
from user_interface.console.chooser import Chooser
import various_tools.count_loc_py
import various_tools.find_all_file_extensions_in_folder
import various_tools.find_files
import various_tools.find_in_files
import various_tools.replace_in_files
import various_tools.copy_dir
import various_tools.list_simlinks
import various_tools.unit_converter
from file_settings_manager.config_manager import ConfigManager

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = 'ButenkoMS <gtalk@butenkoms.space>'


class GlobalConfig(ConfigManager):
    def __init__(self, immediate_save=True):
        default_content = {
            'all tools runner': {
                'last tool id': '',
            },
        }
        super(GlobalConfig, self).__init__(['.PythonLibs Settings', 'Various Tools'],
                                           default_content=default_content,
                                           immediate_save=immediate_save)


ALL_TOOLS_LIST = [
    ('Count Loc Py', various_tools.count_loc_py.main),
    ('Find All Extensions', various_tools.find_all_file_extensions_in_folder.main),
    ('Find Files', various_tools.find_files.main),
    ('Find In Files', various_tools.find_in_files.main),
    ('Replace In Files', various_tools.replace_in_files.main),
    ('Copy dir', various_tools.copy_dir.main),
    ('List simlinks', various_tools.list_simlinks.main),
    ('Unit converter', various_tools.unit_converter.main),
]
ALL_TOOLS_NAMES_LIST = list([x[0] for x in ALL_TOOLS_LIST])


def main():
    global_config = GlobalConfig()
    raw_last_tool_id = global_config.get_property('all tools runner', 'last tool id') or ''

    raw_last_tool_id = raw_last_tool_id.strip()
    last_tool_id_str = raw_last_tool_id

    chooser = Chooser(ALL_TOOLS_NAMES_LIST, 'tool')
    tool_is_chosen, tool_number, input_raw_last_tool_id = chooser.choose(last_tool_id_str)

    if tool_is_chosen:
        global_config.set_property('all tools runner', 'last tool id', input_raw_last_tool_id)

        tool_info = ALL_TOOLS_LIST[tool_number]
        tool_main = tool_info[1]
        tool_main()


if __name__ == "__main__":
    main()
