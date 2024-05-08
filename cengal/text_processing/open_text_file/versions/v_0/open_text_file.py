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
    'OpenTextFile',
    'TextFileInfo',
]


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


from cengal.text_processing.encoding_detection import detect_and_decode
from cengal.code_flow_control.smart_values import ValueHolder

from pathlib import PurePath
from os import PathLike
from io import IOBase
from typing import Union, Tuple, Optional, NamedTuple


class TextFileInfo(NamedTuple):
    text: ValueHolder[str]
    encoding: str
    bom_bytes: bytes
    bin_data: bytes
    file: IOBase


class OpenTextFile:
    def __init__(self, 
                file: Union[str, bytes, PathLike],
                mode: str = 'r+b',
                buffering: int = -1,
                encoding = None,
                errors = None,
                newline = None,
                closefd = True,
                opener = None,
                detect_as_utf8_when_possible: bool = True,
                check_text_for_utf8_compliance: bool = True,
                ):
        self.file: Union[str, bytes, PathLike] = file
        self.mode: str = mode
        self.buffering = buffering
        self.encoding = encoding
        self.proposed_encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener
        self.detect_as_utf8_when_possible: bool = detect_as_utf8_when_possible
        self.check_text_for_utf8_compliance: bool = check_text_for_utf8_compliance
        self.readable: bool = ('r' in mode) or ('+' in mode)
        self.writtable: bool = ('w' in mode) or ('a' in mode) or ('+' in mode)
        self.binary_mode: bool = 'b' in mode
        if self.binary_mode:
            self.encoding = None
        
        self.text_value_holder: Optional[ValueHolder[str]] = None
        self.detected_encoding: str = None
        self.bom_bytes: bytes = None
    
    def __enter__(self) -> TextFileInfo:
        if (not self.readable) and (not self.proposed_encoding):
            raise ValueError('Encoding must be specified for files without reading mode')

        self.file = open(self.file, self.mode, self.buffering, self.encoding, self.errors, self.newline, self.closefd, self.opener)
        if self.binary_mode:
            if self.readable:
                bin_data: bytes = self.file.read()
                text, encoding, bom_bytes = detect_and_decode(bin_data, self.detect_as_utf8_when_possible, self.check_text_for_utf8_compliance)
            else:
                bin_data = bytes()
                text = str()
                encoding = self.proposed_encoding
                bom_bytes = bytes()
            
            self.detected_encoding = encoding
            self.bom_bytes = bom_bytes
            self.text_value_holder = ValueHolder(self.writtable, text)
            return TextFileInfo(self.text_value_holder, encoding, bom_bytes, bin_data, self.file)
        else:
            encoding = self.proposed_encoding
            if self.readable:
                text: str = self.file.read()
                bin_text: bytes = text.encode(encoding)
            else:
                bin_text = bytes()
                text = str()
            
            self.detected_encoding = encoding
            bom_bytes = bytes()
            self.bom_bytes = bom_bytes
            self.text_value_holder = ValueHolder(self.writtable, text)
            return TextFileInfo(self.text_value_holder, encoding, bom_bytes, bin_text, self.file)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.writtable and self.text_value_holder:
            self.file.write(self.bom_bytes + self.text_value_holder.value.encode(self.detected_encoding))
        
        self.file.close()
        return False
    
    async def __aenter__(self) -> TextFileInfo:
        # TODO: implement async version using next backends in exact priority sequence: 
        # ['https://github.com/mosquito/aiofile', 'https://github.com/Tinche/aiofiles', 'own asyncio thread based read-write implementation']. 
        # Dependencies must be optional so own implementation is a last viable option.
        return self.__enter__()
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return self.__exit__(exc_type, exc_val, exc_tb)
