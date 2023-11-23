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


from typing import Tuple, Union
import cchardet as chardet
from cengal.modules_management.alternative_import import alt_import
with alt_import('cchardet') as chardet:
    if chardet is None:
        CHARDET_PRESENT: bool = False
    else:
        CHARDET_PRESENT = True

from charset_normalizer import detect as cn_detect
from cengal.text_processing.text_processing import Text, normalize_text
from cengal.text_processing.utf_bom_processing import *


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


def detect_and_decode(text: Union[bytes, bytearray]) -> Tuple[str, str, bytes]:
    if not text:
        return str(), 'utf-8', bytes()

    text = normalize_text(text, bytes)
    possible_utf_bom = determine_text_bom(text)
    text = remove_bom(text, possible_utf_bom)
    possible_encoding = determine_bom_encoding(possible_utf_bom)
    if possible_encoding is not None:
        return decode_text_and_remove_all_wrong_symbols(text, possible_encoding), possible_encoding, possible_utf_bom
    else:
        try_charset_normalizer = False
        try:
            if CHARDET_PRESENT:
                detection = chardet.detect(text)
            else:
                try_charset_normalizer = True
        except LookupError:
            try_charset_normalizer = True
        
        if try_charset_normalizer:
            detection = cn_detect(text)
            
        encoding = detection["encoding"]
        bom_bytes = bytes()
        return text.decode(encoding), encoding, bom_bytes


def decode(text: Union[bytes, bytearray]) -> str:
    text, encoding, bom_bytes = detect_and_decode(text)
    return text
