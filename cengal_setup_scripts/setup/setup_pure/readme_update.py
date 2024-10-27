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


from cengal.text_processing.open_text_file import OpenTextFile
from cengal.text_processing.text_processing import replace_slice, iterlines
from cengal.file_system.path_manager import path_relative_to_src

from typing import Set


old_text = '# Cengal'

new_text_lines = '''# cengal_pure

This is the pure-Python Cengal package, designed for compatibility across a wide range of Python versions. It does not include compiled extensions, and mandatory requirements are not automatically installed.

As a result, 'cengal-pure' can be installed on older Python versions like 2.7 or 3.1. Please note that while it provides compatibility, not all modules may function optimally on such legacy interpreters.

In order to install Cengal with compiled extensions and with all requirements, execute either:
* `pip install cengal_light[full]` - will install Cengal as well as most of requirements
* `pip install cengal` - Recommended - will install `cengal_light[full]` as well as some missed requirements

# Cengal'''.splitlines()


new_headers: Set[str] = {
    '# cengal_light', 
    '# cengal_pure', 
}


def main():
    with OpenTextFile(path_relative_to_src('README.md')) as readme_file_info:
        content: str = readme_file_info.text.value
        new_text_start = None
        for _, line_content_place, _ in iterlines(content):
            line_content = content[line_content_place]
            if (new_text_start is None) and (line_content in new_headers):
                new_text_start = line_content_place.start
            elif line_content == old_text:
                if new_text_start is None:
                    new_text_start = None
                else:
                    content, _ = replace_slice(content, slice(new_text_start, line_content_place.stop), old_text)
                    
                break
        
        for _, line_content_place, endline_place in iterlines(content):
            if content[line_content_place] == old_text:
                endline = content[endline_place] or '\n'
                new_text: str = endline.join(new_text_lines)
                content, _ = replace_slice(content, line_content_place, new_text)
                break
        
        readme_file_info.text.value = content
        readme_file_info.text.existence = True


if '__main__' == __name__:
    main()
