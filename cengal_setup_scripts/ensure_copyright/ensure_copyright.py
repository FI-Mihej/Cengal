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


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.4.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.file_system.file_manager import current_src_file_dir, path_relative_to_current_src
from cengal.file_system.directory_manager import filtered_file_list_traversal, FilteringType
from cengal.file_system.path_manager import path_relative_to_src, RelativePath
from cengal.text_processing.encoding_detection import detect_and_decode
from cengal.text_processing.text_processing import find_text, replace_slice
from cengal.text_processing.brackets_processing import BracketPair, Bracket, replace_text_with_brackets, find_text_with_brackets
from os.path import splitext, join
from cengal.build_tools.ensure_copyright import ensure_copyright as ensure_copyright_orig
import sys


head_string = \
'''#!/usr/bin/env python
# coding=utf-8'''


license_string = \
'''# Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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
# limitations under the License.'''
license_bracket_pair: BracketPair = BracketPair([Bracket('# Copyright ©')], [Bracket('# limitations under the License.')])


module_docstring_string = \
'''"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""'''


credits_string = \
'''__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.4.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"'''
credits_bracket_pair: BracketPair = BracketPair([Bracket('__author__ =')], [Bracket('__status__ = "Production"')])


def main():
    silent: bool = '--silent' in sys.argv
    cengal_root_dir: str = path_relative_to_current_src('../..')
    ensure_copyright_orig(
        cengal_root_dir,
        head_string,
        license_string,
        license_bracket_pair,
        module_docstring_string,
        credits_string,
        credits_bracket_pair,
        silent=silent,
    )


if '__main__' == __name__:
    main()
