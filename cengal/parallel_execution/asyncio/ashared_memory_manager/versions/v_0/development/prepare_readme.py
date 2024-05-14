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


__all__ = []


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


from cengal.text_processing.open_text_file import OpenTextFile, TextFileInfo
from cengal.text_processing.text_processing import normalize_line_separators_and_tabs, replace_text, replace_slice
from cengal.text_processing.help_tools import find_substring_full_word
from cengal.text_processing.brackets_processing import *
from cengal.file_system.path_manager import path_relative_to_src


def main():
    source_file_path: str = path_relative_to_src('README.md')
    result_file_path: str = path_relative_to_src('../docs/README.md')
    with OpenTextFile(source_file_path, 'rb') as source_text_file_info:
        source_text_file_info.text.existence = False
        content: str = source_text_file_info.text.value

        summary_brackets: BracketPair = BracketPair([Bracket('<summary title')], [Bracket('</summary>')])
        content, _ = replace_text_with_brackets(content, summary_brackets, '')

        html_comment_brackets: BracketPair = BracketPair([Bracket('<!-- !')], [Bracket(' -->')])
        content, _ = replace_text_with_brackets(content, html_comment_brackets, '')

        content = replace_text(content, '<details>', '')
        content = replace_text(content, '</details>', '')

        with OpenTextFile(result_file_path, 'wb', encoding=source_text_file_info.encoding) as result_text_file_info:
            result_text_file_info.text.value = content


if '__main__' == __name__:
    main()
