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
    'bytes__to__hex_string',
    'hex_string__to__bytes',
    'bytes__to__solid_hex_string',
    'solid_hex_string__to__bytes',
    'hex_dword_to_int',
    'int_to_hex_dword',
]


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


from cengal.system import PLATFORM_NAME
from cengal.code_flow_control.none_or import none_or

import binascii


# HEX STRING - BYTES:


def bytes__to__hex_string(input_data: bytes, delimiter: str=None)->str:
    delimiter = none_or(delimiter, ' ')
    # 48508.80358249831 inputs per second
    fake_start = '00'
    fake_start_len = len(fake_start)
    hex_string = fake_start + binascii.hexlify(input_data).decode()
    result = delimiter.join(map(''.join, zip(*[iter(hex_string)]*2)))[fake_start_len:]
    result = result.strip()
    return result

# Very high memory consumption! Use .replace(' ', '') and then solid_hex_string__to__bytes() instead.
if 'PyPy' == PLATFORM_NAME:
    def hex_string__to__bytes(input_data: str, delimiter: str=None)->bytes:
        delimiter = none_or(delimiter, ' ')
        result = b''.join(binascii.unhexlify(b.encode()) for b in input_data.split(delimiter))
        return result
else:
    def hex_string__to__bytes(input_data: str, delimiter: str=None)->bytes:
        delimiter = none_or(delimiter, ' ')
        result = b''.join(binascii.unhexlify(b) for b in input_data.split(delimiter))
        return result


def bytes__to__solid_hex_string(input_data: bytes)->str:
    return binascii.hexlify(input_data).decode()

if 'PyPy' == PLATFORM_NAME:
    def solid_hex_string__to__bytes(input_data: str)->bytes:
        return binascii.unhexlify(input_data.encode())
else:
    def solid_hex_string__to__bytes(input_data: str)->bytes:
        return binascii.unhexlify(input_data)


# HEX DWORD:


def hex_dword_to_int(dword: str, byteorder: str = None, signed: bool = False) -> int:
    """
    "0x008A151D" is big endian; so dword = '008A151D', byteorder = 'big'
    :param dword: str(); '008A151D'
    :param byteorder: str(); 'big' / 'little'
    :param signed: bool();
    :return: 9049373
    """
    byteorder: str = byteorder or 'big'
    bin_dword: bytes = binascii.unhexlify(dword)
    result = int.from_bytes(bin_dword, byteorder=byteorder, signed=signed)
    return result


def int_to_hex_dword(int_value: int, byteorder: str = None, signed: bool = False):
    byteorder: str = byteorder or 'big'
    result = (binascii.hexlify(int_value.to_bytes(4, byteorder=byteorder, signed=signed))).decode()
    return result
