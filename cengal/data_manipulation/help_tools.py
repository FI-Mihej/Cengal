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

from cengal.system import PLATFORM_NAME
from cengal.code_flow_control.none_or import none_or
import binascii
import struct
import base64


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


# SIGNED - BYTES:
# def bytes_to_int(data):
#     # Python 3.2+ only
#     int_data = int.from_bytes(data, byteorder='little', signed=False)
#     return int_data


def int_to_bytes(int_data):
    """
    For a 32 bit signed int in little endian
    :param int_data:
    :return: bytes(); len == 4
    """
    result = struct.pack('<i', int_data)
    return result


def bytes_to_int(bytes_data):
    """
    For a 32 bit signed int in little endian
    :param bytes_data:
    :return:
    """
    result = struct.unpack('<i', bytes_data)[0]
    return result


def short_to_bytes(short_data):
    """
    For a 16 bit signed short in little endian
    :param short_data:
    :return: bytes(); len == 2
    """
    result = struct.pack('<h', short_data)
    return result


def bytes_to_short(bytes_data):
    """
    For a 16 bit signed short in little endian
    :param bytes_data:
    :return:
    """
    result = struct.unpack('<h', bytes_data)[0]
    return result


def byte_to_bytes(byte_data):
    """
    For a 8 bit signed byte
    :param byte_data:
    :return: bytes(); len == 1
    """
    result = struct.pack('<b', byte_data)
    return result


def bytes_to_byte(bytes_data):
    """
    For a 8 bit signed byte
    :param bytes_data:
    :return:
    """
    result = struct.unpack('<b', bytes_data)[0]
    return result


def float_to_bytes(float_data):
    """
    For a 32 bit signed ieee 754 floating points
    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python
    :param float_data:
    :return: bytes() with len == 4
    """
    result = struct.pack('f', float_data)
    return result


def bytes_to_float(bytes_data):
    """
    For a 32 bit signed ieee 754 floating points
    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python
    :param bytes_data: bytes() with len == 4
    :return:
    """
    result = struct.unpack('f', bytes_data)[0]
    return result


# UNSIGNED - BYTES:
def uint_to_bytes(int_data: int)->bytes:
    """
    For a 32 bit unsigned int in little endian
    :param int_data:
    :return: bytes(); len == 4
    """
    result = struct.pack('<I', int_data)
    return result


def bytes_to_uint(bytes_data: bytes)->int:
    """
    For a 32 bit unsigned int in little endian
    :param bytes_data:
    :return:
    """
    result = struct.unpack('<I', bytes_data)[0]
    return result


def ushort_to_bytes(short_data: int)->bytes:
    """
    For a 16 bit unsigned short in little endian
    :param short_data:
    :return: bytes(); len == 2
    """
    result = struct.pack('<H', short_data)
    return result


def bytes_to_ushort(bytes_data: bytes)->int:
    """
    For a 16 bit unsigned short in little endian
    :param bytes_data:
    :return:
    """
    result = struct.unpack('<H', bytes_data)[0]
    return result


def ubyte_to_bytes(byte_data: int)->bytes:
    """
    For a 8 bit unsigned byte
    :param byte_data:
    :return: bytes(); len == 1
    """
    result = struct.pack('<B', byte_data)
    return result


def bytes_to_ubyte(bytes_data: bytes)->int:
    """
    For a 8 bit unsigned byte
    :param bytes_data:
    :return:
    """
    result = struct.unpack('<B', bytes_data)[0]
    return result


# HEX DWORD:
def hex_dword_to_int(dword: str, byteorder=None, signed=False)->bytes:
    """
    "0x008A151D" is big endian; so dword = '008A151D', byteorder = 'big'
    :param dword: str(); '008A151D'
    :param byteorder: str(); 'big' / 'little'
    :param signed: bool();
    :return: 9049373
    """
    byteorder = byteorder or 'big'
    bin_dword = binascii.unhexlify(dword)
    result = int.from_bytes(bin_dword, byteorder=byteorder, signed=signed)
    return result


def int_to_hex_dword(int_value, byteorder=None, signed=False):
    byteorder = byteorder or 'big'
    result = (binascii.hexlify(int_value.to_bytes(4, byteorder=byteorder, signed=signed))).decode()
    return result


# BASE64
def str_to_base64str(string_data):
    result = base64.b64encode(str(string_data).encode()).decode()
    return result


def base64str_to_str(base64string_data):
    result = base64.b64decode(str(base64string_data).encode()).decode()
    return result


# OTHER:
def split_solid_hex_string(hex_string, delimiter=None):
    delimiter = none_or(delimiter, ' ')
    fake_start = '00'
    fake_start_len = len(fake_start)
    hex_string = fake_start + hex_string
    result = delimiter.join(map(''.join, zip(*[iter(hex_string)]*2)))[fake_start_len:]
    result = result.strip()
    return result


def get_slice_from_array(data, offset, size):
    result = data[offset: offset + size]
    return result


def inverse_mapping(f):
    return f.__class__(map(reversed, f.items()))
