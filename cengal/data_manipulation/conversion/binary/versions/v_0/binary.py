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
    'bigint_to_bytes',
    'bint_to_bytes',
    'bytes_to_bigint',
    'bytes_to_bint',
    'ubigint_to_bytes',
    'ubint_to_bytes',
    'bytes_to_ubigint',
    'bytes_to_ubint',
    'int64_to_bytes',
    'longlongint_to_bytes',
    'llint_to_bytes',
    'bytes_to_int64',
    'bytes_to_longlongint',
    'bytes_to_llint',
    'int32_to_bytes',
    'int_to_bytes',
    'bytes_to_int32',
    'bytes_to_int',
    'int16_to_bytes',
    'short_to_bytes',
    'bytes_to_int16',
    'bytes_to_short',
    'int8_to_bytes',
    'byte_to_bytes',
    'bytes_to_int8',
    'bytes_to_byte',
    'uint64_to_bytes',
    'ulonglongint_to_bytes',
    'ullint_to_bytes',
    'bytes_to_uint64',
    'bytes_to_ulonglongint',
    'bytes_to_ullint',
    'uint32_to_bytes',
    'uint_to_bytes',
    'bytes_to_uint32',
    'bytes_to_uint',
    'uint16_to_bytes',
    'ushort_to_bytes',
    'bytes_to_uint16',
    'bytes_to_ushort',
    'uint8_to_bytes',
    'ubyte_to_bytes',
    'bytes_to_uint8',
    'bytes_to_ubyte',
    'float64_to_bytes',
    'double_to_bytes',
    'bytes_to_float64',
    'bytes_to_double',
    'float32_to_bytes',
    'float_to_bytes',
    'bytes_to_float32',
    'bytes_to_float',
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


import struct


# Arbitrary length integers 


def bigint_to_bytes(int_data: int, byteorder: str = 'little'):
    return int_data.to_bytes((int_data.bit_length() + 8) // 8, byteorder, signed=True)  # Add 7 to handle cases where bit_length is not a multiple of 8. Add 1 to ensure that the number is always has a sign bit


bint_to_bytes = bigint_to_bytes


def bytes_to_bigint(bytes_data: bytes, byteorder: str = 'little') -> int:
    return int.from_bytes(bytes_data, byteorder=byteorder, signed=True)


bytes_to_bint = bytes_to_bigint


def ubigint_to_bytes(int_data: int, byteorder: str = 'little') -> bytes:
    return int_data.to_bytes((int_data.bit_length() + 7) // 8, byteorder)  # Add 7 to handle cases where bit_length is not a multiple of 8


ubint_to_bytes = ubigint_to_bytes


def bytes_to_ubigint(bytes_data: bytes, byteorder: str = 'little') -> int:
    return int.from_bytes(bytes_data, byteorder)


bytes_to_ubint = bytes_to_ubigint


# Fixed length integers


def int64_to_bytes(int_data: int)->bytes:
    """
    For a 64 bit signed int in little endian
    :param int_data:
    :return: bytes(); len == 8
    """
    result = struct.pack('<q', int_data)
    return result


longlongint_to_bytes = int64_to_bytes
llint_to_bytes = int64_to_bytes


def bytes_to_int64(bytes_data: bytes)->int:
    """
    For a 64 bit signed int in little endian
    :param bytes_data:
    :return:
    """
    result = struct.unpack('<q', bytes_data)[0]
    return result


bytes_to_longlongint = bytes_to_int64
bytes_to_llint = bytes_to_int64


def int32_to_bytes(int_data: int)->bytes:
    """
    For a 32 bit signed int in little endian
    :param int_data:
    :return: bytes(); len == 4
    """
    result = struct.pack('<i', int_data)
    return result


int_to_bytes = int32_to_bytes


def bytes_to_int32(bytes_data: bytes)->int:
    """
    For a 32 bit signed int in little endian
    :param bytes_data:
    :return:
    """
    result = struct.unpack('<i', bytes_data)[0]
    return result


bytes_to_int = bytes_to_int32


def int16_to_bytes(short_data: int)->bytes:
    """
    For a 16 bit signed short in little endian
    :param short_data:
    :return: bytes(); len == 2
    """
    result = struct.pack('<h', short_data)
    return result


short_to_bytes = int16_to_bytes


def bytes_to_int16(bytes_data: bytes)->int:
    """
    For a 16 bit signed short in little endian
    :param bytes_data:
    :return:
    """
    result = struct.unpack('<h', bytes_data)[0]
    return result


bytes_to_short = bytes_to_int16


def int8_to_bytes(byte_data: int)->bytes:
    """
    For a 8 bit signed byte
    :param byte_data:
    :return: bytes(); len == 1
    """
    result = struct.pack('<b', byte_data)
    return result


byte_to_bytes = int8_to_bytes


def bytes_to_int8(bytes_data: bytes)->int:
    """
    For a 8 bit signed byte
    :param bytes_data:
    :return:
    """
    result = struct.unpack('<b', bytes_data)[0]
    return result


bytes_to_byte = bytes_to_int8


def uint64_to_bytes(int_data: int)->bytes:
    """
    For a 64 bit unsigned int in little endian
    :param int_data:
    :return: bytes(); len == 8
    """
    result = struct.pack('<Q', int_data)
    return result


ulonglongint_to_bytes = uint64_to_bytes
ullint_to_bytes = uint64_to_bytes


def bytes_to_uint64(bytes_data: bytes)->int:
    """
    For a 64 bit unsigned int in little endian
    :param bytes_data:
    :return:
    """
    result = struct.unpack('<Q', bytes_data)[0]
    return result


bytes_to_ulonglongint = bytes_to_uint64
bytes_to_ullint = bytes_to_uint64


def uint32_to_bytes(int_data: int)->bytes:
    """
    For a 32 bit unsigned int in little endian
    :param int_data:
    :return: bytes(); len == 4
    """
    result = struct.pack('<I', int_data)
    return result


uint_to_bytes = uint32_to_bytes


def bytes_to_uint32(bytes_data: bytes)->int:
    """
    For a 32 bit unsigned int in little endian
    :param bytes_data:
    :return:
    """
    result = struct.unpack('<I', bytes_data)[0]
    return result


bytes_to_uint = bytes_to_uint32


def uint16_to_bytes(short_data: int)->bytes:
    """
    For a 16 bit unsigned short in little endian
    :param short_data:
    :return: bytes(); len == 2
    """
    result = struct.pack('<H', short_data)
    return result


ushort_to_bytes = uint16_to_bytes


def bytes_to_uint16(bytes_data: bytes)->int:
    """
    For a 16 bit unsigned short in little endian
    :param bytes_data:
    :return:
    """
    result = struct.unpack('<H', bytes_data)[0]
    return result


bytes_to_ushort = bytes_to_uint16


def uint8_to_bytes(byte_data: int)->bytes:
    """
    For a 8 bit unsigned byte
    :param byte_data:
    :return: bytes(); len == 1
    """
    result = struct.pack('<B', byte_data)
    return result


ubyte_to_bytes = uint8_to_bytes


def bytes_to_uint8(bytes_data: bytes)->int:
    """
    For a 8 bit unsigned byte
    :param bytes_data:
    :return:
    """
    result = struct.unpack('<B', bytes_data)[0]
    return result


bytes_to_ubyte = bytes_to_uint8


# Fixed length floats


def float64_to_bytes(float_data):
    """
    For a 64 bit signed ieee 754 floating points
    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python
    :param float_data:
    :return: bytes() with len == 8
    """
    result = struct.pack('d', float_data)
    return result


double_to_bytes = float64_to_bytes


def bytes_to_float64(bytes_data):
    """
    For a 64 bit signed ieee 754 floating points
    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python
    :param bytes_data: bytes() with len == 8
    :return:
    """
    result = struct.unpack('d', bytes_data)[0]
    return result


bytes_to_double = bytes_to_float64


def float32_to_bytes(float_data):
    """
    For a 32 bit signed ieee 754 floating points
    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python
    :param float_data:
    :return: bytes() with len == 4
    """
    result = struct.pack('f', float_data)
    return result


float_to_bytes = float32_to_bytes


def bytes_to_float32(bytes_data):
    """
    For a 32 bit signed ieee 754 floating points
    http://stackoverflow.com/questions/6286033/reading-32-bit-signed-ieee-754-floating-points-from-a-binary-file-with-python
    :param bytes_data: bytes() with len == 4
    :return:
    """
    result = struct.unpack('f', bytes_data)[0]
    return result


bytes_to_float = bytes_to_float32
