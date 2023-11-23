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


__all__ = ['WrongTextType', 'KNOWN_BOMS', 'determine_text_bom', 'remove_bom', 'determine_bom_encoding', 'decode_text_and_remove_all_wrong_symbols']


#!/usr/bin/env python
# coding=utf-8




import platform, sys
import codecs
from typing import Optional, Union
from cengal.text_processing.text_processing import Text, DEFAULT_ENCODING, normalize_text, removeprefix







class WrongTextType(Exception):
    pass


KNOWN_BOMS = {
    codecs.BOM_UTF8: 'utf-8',
    codecs.BOM_UTF16_BE: 'utf-16be',
    codecs.BOM_UTF16_LE: 'utf-16le',
    codecs.BOM_UTF32_BE: 'utf-32be',
    codecs.BOM_UTF32_LE: 'utf-32le',
}
KNOWN_BOMS_ORDER = [
    codecs.BOM_UTF8,
    codecs.BOM_UTF32_BE,
    codecs.BOM_UTF32_LE,
    codecs.BOM_UTF16_BE,
    codecs.BOM_UTF16_LE,
]


def determine_text_bom(text: Union[bytes, bytearray]) -> Union[bytes, bytearray]:
    if (not isinstance(text, bytes)) and (not isinstance(text, bytearray)):
        raise WrongTextType
    
    bom_list = list()
    
    absent_bom = b''
    
    if isinstance(text, bytearray):
        for bom in KNOWN_BOMS_ORDER:
            bom_list.append(normalize_text(bom, bytearray))
        
        absent_bom = bytearray(absent_bom)
    else:
        bom_list = list(KNOWN_BOMS_ORDER)

    for bom in bom_list:
        if text.startswith(bom):
            return bom
    
    return absent_bom


def remove_bom(text: Union[bytes, bytearray], bom: Union[bytes, bytearray]) -> Union[bytes, bytearray]:
    return removeprefix(text, bom)


def determine_bom_encoding(bom: Union[bytes, bytearray]) -> Optional[str]:
    bom = normalize_text(bom, bytes)
    return KNOWN_BOMS.get(bom, None)


def decode_text_and_remove_all_wrong_symbols(text: Union[bytes, bytearray], encoding: str) -> str:
    return text.decode(encoding, 'replace')

