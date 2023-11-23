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
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.text_processing.encoding_detection import detect_and_decode
from cengal.text_processing.text_processing import DEFAULT_ENCODING
from typing import List, Tuple, Optional, Callable, Any



def patch_text_file(file_path: str, patch: Any, patch_text: Callable, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None):
    with open(file_path, 'r+b') as file:
        text, text_encoding, bom_bytes = detect_and_decode(file.read())
        text = patch_text(text, patch, encoding, normalizer)
        file.seek(0, 0)
        file.truncate(0)
        data = bom_bytes + text.encode(text_encoding)
        file.write(data)


def patch_bin_file(file_path: str, patch: Any, patch_text: Callable, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None):
    with open(file_path, 'r+b') as file:
        data: bytes = file.read()
        data = patch_text(data, patch, encoding, normalizer)
        file.seek(0, 0)
        file.truncate(0)
        file.write(data)
