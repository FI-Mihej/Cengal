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


# __all__ = ['SharedMemory', 'QueueType', 'Offset', 'Size', 'SharedMemoryError',
#            'WrongObjectTypeError', 'NoMessagesInQueueError',
#            'nearest_size', 'nsize', 'TBase', 'IList', 'codec_by_type', 'get_in_line', 'wait_my_turn']


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


from cengal.introspection.inspect import is_callable, is_descriptor, is_async
from cengal.math.numbers import RationalNumber
from cengal.hardware.memory.barriers import full_memory_barrier, mm_pause
from cengal.time_management.cpu_clock import cpu_clock
from cengal.time_management.high_precision_sync_sleep import hps_sleep
from cengal.time_management.sleep_tools import sleep
from cengal.introspection.inspect import pdi, pifrl, intro_func_repr_limited
from cengal.system import OS_TYPE
from cengal.file_system.file_manager import file_exists
from cengal.data_manipulation.conversion.binary import bint_to_bytes, bytes_to_bint
from cengal.introspection.inspect import is_setable_data_descriptor
# from .compilable import write_uint64 as write_uint64_c, read_uint64 as read_uint64_c, write_int64, read_int64, write_double, read_double, zero_memory
from .compilable import write_uint64, read_uint64, read_uint8, write_int64, read_int64, write_double, read_double, \
    zero_memory, list__get_item, list__get_item_as_offset, list__set_item, list__set_item_as_offset, mask_least_significant_bits

import os
import asyncio
import pickle
import ctypes
import numpy as np
from enum import IntEnum
from multiprocessing.shared_memory import SharedMemory as MultiprocessingSharedMemory
from array import array
from inspect import isclass, ismodule, getattr_static
from contextlib import contextmanager
from pathlib import PurePath
from math import log2, ceil
from pickle import dumps as pickle_dumps, loads as pickle_loads
from inspect import isfunction, ismethod, isclass, ismethoddescriptor
from collections.abc import Sequence as AbsSequence, MutableSequence as AbsMutableSequence, Set as AbsSet, \
    MutableSet as AbsMutableSet, Mapping as AbsMapping, MutableMapping as AbsMutableMapping
try:
    from torch import Tensor, from_numpy
except ImportError:
    class Tensor:
        def numpy(self) -> np.ndarray:
            raise NotImplementedError
    
    def from_numpy(numpy_ndarray: np.ndarray) -> Tensor:
        raise NotImplementedError

from types import FrameType, CodeType
from typing import Any, Tuple, Optional, List, Dict, Set, FrozenSet, AbstractSet, Type, Union, Sequence, cast, Hashable, Coroutine


DEBUG = False


current_shared_memory_instance: 'SharedMemory' = None


# def write_uint64(base_address: int, offset: int, value: int):
#     if current_shared_memory_instance is not None:
#         if 460 <= offset <= 564:
#             print('write_uint64: offset_to_be_monitored: offset: {}, value: {}'.format(offset, value))
        
#     write_uint64_cython(base_address, offset, value)


# def write_uint64(base_address: int, offset: int, value: int):
#     if current_shared_memory_instance is None:
#         return write_uint64_c(base_address, offset, value)
#     else:
#         return current_shared_memory_instance.write_uint64(offset, value)

# def read_uint64(base_address: int, offset: int) -> int:
#     if current_shared_memory_instance is None:
#         return read_uint64_c(base_address, offset)
#     else:
#         return current_shared_memory_instance.read_uint64(offset)


class QueueType(IntEnum):
    fifo = 0
    lifo = 1


class ObjectType(IntEnum):
    tfree_memory = 0
    tmessage = 1
    tnone = 2
    tbool = 3
    tint = 4
    tfloat = 5
    tcomplex = 6
    tstr = 7
    tbytes = 8
    tbytearray = 9
    ttuple = 10
    tlist = 11
    tmutableset = 12
    tset = 13
    tmutablemapping = 14
    tmapping = 15
    tfastdict = 16
    tclass = 17
    tpickable = 18
    tinternal_list = 19
    tsmallint = 20
    tbigint = 21
    tgeneralobject = 22
    tnumpyndarray = 23
    ttorchtensor = 24
    tstaticobject = 25
    tfastset = 26
    tslice = 27


class SysValuesOffsets(IntEnum):
    total_mem_size = 0
    data_start_offset = 1
    data_size = 2
    data_end_offset = 3
    free_memory_search_start = 4
    first_message_offset = 5
    last_message_offset = 6
    creator_in_charge = 7
    consumer_in_charge = 8
    creator_wants_to_be_in_charge = 9
    consumer_wants_to_be_in_charge = 10
    creator_ready = 11
    consumer_ready = 12


Offset = int
Size = int
minimal_memory_block_size = 8
block_size = minimal_memory_block_size
bs = block_size


class SharedMemoryError(Exception):
    pass


class OperationTimedOutError(SharedMemoryError):
    pass


class FreeMemoryChunkNotFoundError(SharedMemoryError):
    """Indicates that an unpartitioned chunk of free memory of requested size not being found.

        Regarding this error, it’s important to adjust the size parameter in the SharedMemory configuration. Trying to estimate memory consumption down to the byte is not practical because it fails to account for the memory overhead required by each entity stored (such as entity type metadata, pointers to child entities, etc.).

        When setting the size parameter for SharedMemory, consider using broader units like tens (for embedded systems), hundreds, or thousands of megabytes, rather than precise byte counts. This approach is similar to how you would not precisely calculate the amount of memory needed for a web server hosted externally; you make an educated guess, like assuming that 256 MB might be insufficient but 768 MB could be adequate, and then adjust based on practical testing.

        Also, be aware of memory fragmentation, which affects all memory allocation systems, including the OS itself. For example, if you have a SharedMemory pool sized to store exactly ten 64-bit integers, accounting for additional bytes for system information, your total might be around 200 bytes. Initially, after storing the integers, your memory might appear as ["int", "int", ..., "int"]. If you delete every second integer, the largest contiguous free memory chunk could be just 10 bytes, despite having 50 bytes free in total. This fragmentation means you cannot store a larger data structure like a 20-byte string which needs contiguous space.

        To resolve this, simply increase the size parameter value of SharedMemory. This is akin to how you would manage memory allocation for server hosting or thread stack sizes in software development.

    Args:
        SharedMemoryError (_type_): _description_
    """
    pass


class ObjBufferIsSmallerThanRequestedNumpyArrayError(SharedMemoryError):
    pass


class WrongObjectTypeError(SharedMemoryError):
    pass


class NoMessagesInQueueError(SharedMemoryError):
    pass


def nearest_size(size: Size) -> Size:
    return ((size // 8) * 8 + 8) if size % 8 else size


nsize = nearest_size


class BaseIObject:
    pass


# TODO: add next fields: obj_id (simple int index; need to identify object in shared memory); ref_count (simple int counter; need to count references to object. Howerver this field can be moved to shared memory dict with all objects properties like ref_count, etc.)
class BaseObjOffsets(IntEnum):
    obj_type = 0
    obj_size = 1


BaseObjOffsetsLen: int = 2  # 2
bsBaseObjOffsetsLen: int = 16  # 8 * 2 = 16


class TBase:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: Any) -> Tuple[Any, Offset, Size]:
        raise NotImplementedError
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> Any:
        raise NotImplementedError
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        raise NotImplementedError
    
    def buffer(self, shared_memory: 'SharedMemory', offset: Offset) -> memoryview:
        raise NotImplementedError
    
    def buffer_2(self, shared_memory: 'SharedMemory', offset: Offset) -> Tuple[int, int]:
        raise NotImplementedError


# ======================================================================================================================
# === None =====================================================================================================


class TNone:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: None) -> Tuple[None, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.tnone, 0)
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.tnone != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        return None
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        if ObjectType.tnone != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        shared_memory.free(offset)


# ======================================================================================================================
# === Int =====================================================================================================


class IntOffsets(IntEnum):
    data = 0


class TInt:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: int) -> Tuple[int, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.tint, 8)
        write_int64(shared_memory.base_address, offset + 16 + 0, obj)
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> int:
        if ObjectType.tint != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        return read_int64(shared_memory.base_address, offset + 16 + 0)
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        if ObjectType.tint != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        shared_memory.free(offset)


# ======================================================================================================================
# === SmallInt =====================================================================================================


class SmallInt(int):
    ...


smallint = SmallInt
sint = SmallInt


class SmallIntOffsets(IntEnum):
    data = 0


class TSmallInt:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: int) -> Tuple[int, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.tsmallint, 8)
        write_int64(shared_memory.base_address, offset + 16 + 0, obj)
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> int:
        if ObjectType.tsmallint != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        return read_int64(shared_memory.base_address, offset + 16 + 0)
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        if ObjectType.tsmallint != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        shared_memory.free(offset)


# ======================================================================================================================
# === LargeInt =====================================================================================================


class BigInt(int):
    ...


bigint = BigInt
bint = BigInt


class BigIntOffsets(IntEnum):
    data_size = 0
    data = 1


class TBigInt:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: int) -> Tuple[int, Offset, Size]:
        data = bint_to_bytes(obj)
        data_size = len(data)
        # offset, real_size = shared_memory.malloc(ObjectType.tbigint, 16 + 8 * data_size)
        offset, real_size = shared_memory.malloc(ObjectType.tbigint, 16 + data_size)
        write_uint64(shared_memory.base_address, offset + 16 + 0, data_size)
        data_offset = offset + 16 + 8
        shared_memory._shared_memory.buf[data_offset:data_offset + data_size] = data
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> int:
        if ObjectType.tbigint != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        data_size = read_uint64(shared_memory.base_address, offset + 16 + 0)
        if data_size:
            data_offset = offset + 16 + 8
            data = bytes(shared_memory._shared_memory.buf[data_offset:data_offset + data_size])
            return bytes_to_bint(data)
        else:
            return 0
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        if ObjectType.tbigint != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        shared_memory.free(offset)
    
    def buffer(self, shared_memory: 'SharedMemory', offset: Offset) -> memoryview:
        if ObjectType.tbigint != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        data_size = read_uint64(shared_memory.base_address, offset + 16 + 0)
        data_offset = offset + 16 + 8
        return shared_memory._shared_memory.buf[data_offset:data_offset + data_size]
    
    def buffer_2(self, shared_memory: 'SharedMemory', offset: Offset) -> Tuple[int, int]:
        if ObjectType.tbigint != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        data_size = read_uint64(shared_memory.base_address, offset + 16 + 0)
        data_offset = offset + 16 + 8
        return data_offset, data_size


# ======================================================================================================================
# === Bool =====================================================================================================


class BoolOffsets(IntEnum):
    data = 0


class TBool:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: bool) -> Tuple[bool, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.tbool, 8)
        write_uint64(shared_memory.base_address, offset + 16 + 0, int(obj))
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> bool:
        if ObjectType.tbool != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        return bool(read_uint64(shared_memory.base_address, offset + 16 + 0))
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        if ObjectType.tbool != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        shared_memory.free(offset)


# ======================================================================================================================
# === Float =====================================================================================================


class FloatOffsets(IntEnum):
    data = 0


class TFloat:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: float) -> Tuple[float, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.tfloat, 8)
        write_double(shared_memory.base_address, offset + 16 + 0, obj)
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> float:
        if ObjectType.tfloat != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        return read_double(shared_memory.base_address, offset + 16 + 0)
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        if ObjectType.tfloat != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        shared_memory.free(offset)


# ======================================================================================================================
# === Bytes =====================================================================================================


class BytesOffsets(IntEnum):
    data_size = 0
    data = 1


class TBytes:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: bytes) -> Tuple[bytes, Offset, Size]:
        data_size = len(obj)
        # offset, real_size = shared_memory.malloc(ObjectType.tbytes, 16 + 8 * data_size)
        offset, real_size = shared_memory.malloc(ObjectType.tbytes, 16 + data_size)
        write_uint64(shared_memory.base_address, offset + 16 + 0, data_size)
        data_offset = offset + 16 + 8
        shared_memory._shared_memory.buf[data_offset:data_offset + data_size] = obj
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> bytes:
        if ObjectType.tbytes != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        data_size = read_uint64(shared_memory.base_address, offset + 16 + 0)
        if data_size:
            data_offset = offset + 16 + 8
            obj = bytes(shared_memory._shared_memory.buf[data_offset:data_offset + data_size])
            return obj
        else:
            return bytes()
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        if ObjectType.tbytes != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        shared_memory.free(offset)
    
    def buffer(self, shared_memory: 'SharedMemory', offset: Offset) -> memoryview:
        if ObjectType.tbytes != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        data_size = read_uint64(shared_memory.base_address, offset + 16 + 0)
        data_offset = offset + 16 + 8
        return shared_memory._shared_memory.buf[data_offset:data_offset + data_size]
    
    def buffer_2(self, shared_memory: 'SharedMemory', offset: Offset) -> Tuple[int, int]:
        if ObjectType.tbytes != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        data_size = read_uint64(shared_memory.base_address, offset + 16 + 0)
        data_offset = offset + 16 + 8
        return data_offset, data_size


# class TBytes:
#     def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: bytes) -> Tuple[bytes, Offset, Size]:
#         data_size = len(obj)
#         if 0 == data_size:
#             allocated_data_size = 1
#         else:
#             allocated_data_size = data_size
        
#         # offset, real_size = shared_memory.malloc(ObjectType.tbytes, 8 * (2 - 1) + 8 * allocated_data_size)
#         offset, real_size = shared_memory.malloc(ObjectType.tbytes, 8 * (2 - 1) + allocated_data_size)
#         shared_memory.print_mem(offset, 100, f'TBytes.map_to_shared_memory 0: offset: {offset}, real_size: {real_size}')
#         write_uint64(shared_memory.base_address, offset + 16 + 0, data_size)
#         shared_memory.print_mem(offset, 100, f'TBytes.map_to_shared_memory 1: offset: {offset}, real_size: {real_size}')
#         data_offset = offset + 16 + 8
#         if data_size:
#             try:
#                 shared_memory._shared_memory.buf[data_offset:data_offset + data_size] = obj
#             except ValueError:
#                 print(len(shared_memory._shared_memory.buf[data_offset:data_offset + data_size]), shared_memory._shared_memory.buf[data_offset:data_offset + data_size])
#                 print(len(obj), obj)
#                 raise
            
#             shared_memory.print_mem(offset, 100, f'TBytes.map_to_shared_memory 2: offset: {offset}, real_size: {real_size}, data_size: {data_size}, data_offset: {data_offset}')
        
#         return obj, offset, real_size
    
#     def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> bytes:
#         if ObjectType.tbytes != read_uint64(shared_memory.base_address, offset + 0):
#             raise WrongObjectTypeError

#         data_size = read_uint64(shared_memory.base_address, offset + 16 + 0)
#         data_offset = offset + 16 + 8
#         shared_memory.print_mem(offset, 100, f'TBytes.init_from_shared_memory 0: offset: {offset}, data_size: {data_size}, data_offset: {data_offset}')
#         if data_size:
#             obj = bytes(shared_memory._shared_memory.buf[data_offset:data_offset + data_size])
#         else:
#             obj = b''
        
#         return obj
    
#     def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
#         shared_memory.free(offset)


# ======================================================================================================================
# === Bytearray =====================================================================================================


class BytearrayOffsets(IntEnum):
    data_size = 0
    data = 1


class TBytearray:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: bytearray) -> Tuple[bytearray, Offset, Size]:
        data = bytes(obj)
        data_size = len(data)
        # offset, real_size = shared_memory.malloc(ObjectType.tbytearray, 16 + 8 * data_size)
        offset, real_size = shared_memory.malloc(ObjectType.tbytearray, 16 + data_size)
        write_uint64(shared_memory.base_address, offset + 16 + 0, data_size)
        data_offset = offset + 16 + 8
        shared_memory._shared_memory.buf[data_offset:data_offset + data_size] = data
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> bytearray:
        if ObjectType.tbytearray != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        data_size = read_uint64(shared_memory.base_address, offset + 16 + 0)
        if data_size:
            data_offset = offset + 16 + 8
            data = bytes(shared_memory._shared_memory.buf[data_offset:data_offset + data_size])
            return bytearray(data)
        else:
            return bytearray(bytes())
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        if ObjectType.tbytearray != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        shared_memory.free(offset)
    
    def buffer(self, shared_memory: 'SharedMemory', offset: Offset) -> memoryview:
        if ObjectType.tbytearray != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        data_size = read_uint64(shared_memory.base_address, offset + 16 + 0)
        data_offset = offset + 16 + 8
        return shared_memory._shared_memory.buf[data_offset:data_offset + data_size]
    
    def buffer_2(self, shared_memory: 'SharedMemory', offset: Offset) -> Tuple[int, int]:
        if ObjectType.tbytearray != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        data_size = read_uint64(shared_memory.base_address, offset + 16 + 0)
        data_offset = offset + 16 + 8
        return data_offset, data_size


# ======================================================================================================================
# === Str =====================================================================================================


class StrOffsets(IntEnum):
    data_size = 0
    data = 1


class TStr:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: str) -> Tuple[str, Offset, Size]:
        data = str.encode(obj)
        data_size = len(data)
        # offset, real_size = shared_memory.malloc(ObjectType.tstr, 16 + 8 * data_size)
        offset, real_size = shared_memory.malloc(ObjectType.tstr, 16 + data_size)
        write_uint64(shared_memory.base_address, offset + 16 + 0, data_size)
        data_offset = offset + 16 + 8
        shared_memory._shared_memory.buf[data_offset:data_offset + data_size] = data
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> str:
        if ObjectType.tstr != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        data_size = read_uint64(shared_memory.base_address, offset + 16 + 0)
        if data_size:
            data_offset = offset + 16 + 8
            data = bytes(shared_memory._shared_memory.buf[data_offset:data_offset + data_size])
            return data.decode()
        else:
            return str()
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        if ObjectType.tstr != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        shared_memory.free(offset)
    
    def buffer(self, shared_memory: 'SharedMemory', offset: Offset) -> memoryview:
        if ObjectType.tstr != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        data_size = read_uint64(shared_memory.base_address, offset + 16 + 0)
        data_offset = offset + 16 + 8
        return shared_memory._shared_memory.buf[data_offset:data_offset + data_size]
    
    def buffer_2(self, shared_memory: 'SharedMemory', offset: Offset) -> Tuple[int, int]:
        if ObjectType.tstr != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        data_size = read_uint64(shared_memory.base_address, offset + 16 + 0)
        data_offset = offset + 16 + 8
        return data_offset, data_size


# ======================================================================================================================
# === ListTrue =========================================================================================================
# An old preoptimized version with a bunch of issues and bugs due to the wrong offsets. Deprecated. Use IList instead


class InternalListTrueOffsets(IntEnum):
    capacity = 0
    size = 1


def malloc_tinternal_list_true(shared_memory: 'SharedMemory', size: Size, capacity: Size = None) -> Tuple[Offset, Size]:
    capacity = (size << 1 if size else 16) if capacity is None else capacity
    datas_sys_part_size = 8 * len(InternalListTrueOffsets)
    offset, real_size = shared_memory.malloc(ObjectType.tinternal_list, datas_sys_part_size + 8 * capacity)
    data_offset = offset + datas_sys_part_size
    write_uint64(shared_memory.base_address, data_offset + 8 * InternalListTrueOffsets.capacity, capacity)
    write_uint64(shared_memory.base_address, data_offset + 8 * InternalListTrueOffsets.size, size)
    return offset, real_size


def realloc_tinternal_list_true(shared_memory: 'SharedMemory', offset: Offset, desired_size: int = None, new_capacity: int = None, loop_allowed: bool = True, zero_mem: bool = True) -> Tuple[Offset, Size]:
    datas_sys_part_size = 8 * len(InternalListTrueOffsets)
    data_offset = offset + datas_sys_part_size
    capacity = read_uint64(shared_memory.base_address, data_offset + 8 * InternalListTrueOffsets.capacity)
    size = read_uint64(shared_memory.base_address, data_offset + 8 * InternalListTrueOffsets.size)
    new_list_capacity = capacity << 1 if new_capacity is None else new_capacity
    if new_capacity is None:
        if desired_size is None:
            new_list_capacity = capacity << 1 if capacity else 16
        else:
            new_list_capacity = desired_size << 1 if desired_size else 16
    else:
        new_list_capacity = new_capacity
    
    if new_list_capacity < size:
        new_list_capacity = size
    
    new_offset, new_real_size = shared_memory.realloc(offset, datas_sys_part_size + 8 * new_list_capacity, loop_allowed, zero_mem)
    data_offset = new_offset + datas_sys_part_size
    write_uint64(shared_memory.base_address, data_offset + 8 * InternalListTrueOffsets.capacity, new_list_capacity)
    return new_offset, new_real_size


class IListTrue(BaseIObject, list):
    def __init__(self, shared_memory: 'SharedMemory', offset: Offset = None, obj: List = None) -> None:
        self._shared_memory = shared_memory
        self._base_address = shared_memory.base_address
        if offset is None:
            offset, real_size = shared_memory.malloc(ObjectType.tlist, 8)
            self._offset = offset
            self._offset__data = offset + 8 * 2
            self._offset__pointer_to_internal_list = self._offset__data
            
            if obj is None:
                obj = list()
            
            data_len = len(obj)
            capacity_len = data_len << 1 if data_len else 16
            internal_list_offset, data_tuple_real_size = malloc_tinternal_list(shared_memory, data_len, capacity_len)
            self._pointer_to_internal_list = internal_list_offset
            for i, item in enumerate(obj):
                item_mapped_obj, item_offset, item_size = shared_memory.put_obj(item)
                write_uint64(self._base_address, self._item_offset(i), item_offset)
        else:
            self._offset = offset
            self._offset__data = offset + 8 * 2
            self._offset__pointer_to_internal_list = self._offset__data
    
    def raw_to_bytes(self, bytes_num: int) -> bytes:
        start_index = self._pointer_to_internal_list
        return self._shared_memory.read_mem(start_index, bytes_num)
        # return bytes(self._shared_memory._shared_memory.buf[start_index : start_index + bytes_num])
    
    @property
    def _obj_size(self):
        return read_uint64(self._base_address, self._offset + 8 * BaseObjOffsets.obj_size)
    
    @property
    def _pointer_to_internal_list(self):
        return read_uint64(self._base_address, self._offset__pointer_to_internal_list)

    @_pointer_to_internal_list.setter
    def _pointer_to_internal_list(self, value: Offset):
        write_uint64(self._base_address, self._offset__pointer_to_internal_list, value)

    @property
    def _list_len(self):
        return read_uint64(self._base_address, self._pointer_to_internal_list + 8 * 2 + 8 * InternalListTrueOffsets.size)
    
    @_list_len.setter
    def _list_len(self, value: int):
        write_uint64(self._base_address, self._pointer_to_internal_list + 8 * 2 + 8 * InternalListTrueOffsets.size, value)

    @property
    def _list_capacity(self):
        return read_uint64(self._base_address, self._pointer_to_internal_list + 8 * 2 + 8 * InternalListTrueOffsets.capacity)
    
    def _item_offset(self, key: int) -> Offset:
        return self._pointer_to_internal_list + 8 * 2 + 8 * len(InternalListTrueOffsets) + key * 8
    
    def __len__(self) -> int:
        return self._list_len
    
    def get_children_offsets(self) -> List[Offset]:
        return [read_uint64(self._base_address, self._item_offset(i)) for i in range(self._list_len)]
    
    def __getitem__(self, key: Union[int, slice]) -> Union[Any, List]:
        if isinstance(key, int):
            if key < 0:
                key += len(self)
            if key < 0 or key >= len(self):
                raise IndexError

            item_offset = read_uint64(self._base_address, self._item_offset(key))
            return self._shared_memory.get_obj(item_offset)
        elif isinstance(key, slice):
            if key.step is not None:
                raise NotImplementedError
            
            if key.start is None:
                start = 0
            elif key.start < 0:
                start = key.start + len(self)
            else:
                start = key.start
            
            if key.stop is None:
                stop = len(self)
            elif key.stop < 0:
                stop = key.stop + len(self)
            else:
                stop = key.stop
            
            if start < 0 or start >= len(self) or stop < 0 or stop > len(self) or start >= stop:
                raise IndexError
            
            result_list = list()
            for i in range(start, stop):
                item_offset = read_uint64(self._base_address, self._item_offset(i))
                result_list.append(self._shared_memory.get_obj(item_offset))
            return result_list
        else:
            raise TypeError
    
    def __setitem__(self, key: Union[int, slice], value: Union[Any, Sequence]) -> Any:
        if isinstance(key, int):
            if key < 0:
                key += len(self)
            if key < 0 or key >= len(self):
                raise IndexError

            item_mapped_obj, item_offset, item_size = self._shared_memory.put_obj(value)
            write_uint64(self._base_address, self._item_offset(key), item_offset)
        elif isinstance(key, slice):
            if key.step is not None:
                raise NotImplementedError
            
            if key.start is None:
                start = 0
            elif key.start < 0:
                start = key.start + len(self)
            else:
                start = key.start
            
            if key.stop is None:
                stop = len(self)
            elif key.stop < 0:
                stop = key.stop + len(self)
            else:
                stop = key.stop
            
            if start < 0 or start >= len(self) or stop < 0 or stop > len(self) or start >= stop:
                raise IndexError
            
            for i in range(start, stop):
                item_mapped_obj, item_offset, item_size = self._shared_memory.put_obj(value[i - start])
                write_uint64(self._base_address, self._item_offset(i), item_offset)
        else:
            raise TypeError

    def __delitem__(self, key: Union[int, slice]) -> None:
        if isinstance(key, int):
            if key < 0:
                key += len(self)
            if key < 0 or key >= len(self):
                raise IndexError

            for i in range(key + 1, len(self)):
                item_offset = read_uint64(self._base_address, self._item_offset(i))
                self._shared_memory.free(item_offset)
                write_uint64(self._base_address, self._item_offset(i - 1), item_offset)
            
            self._list_len -= 1
        elif isinstance(key, slice):
            if key.step is not None:
                raise NotImplementedError
            
            if key.start is None:
                start = 0
            elif key.start < 0:
                start = key.start + len(self)
            else:
                start = key.start
            
            if key.stop is None:
                stop = len(self)
            elif key.stop < 0:
                stop = key.stop + len(self)
            else:
                stop = key.stop
            
            if start < 0 or start >= len(self) or stop < 0 or stop > len(self) or start >= stop:
                raise IndexError
            
            for i in range(start, stop):
                item_offset = read_uint64(self._base_address, self._item_offset(i))
                self._shared_memory.free(item_offset)
            
            del_items_num = stop - start
            
            for i in range(stop, len(self)):
                item_offset = read_uint64(self._base_address, self._item_offset(i))
                write_uint64(self._base_address, self._item_offset(i - del_items_num), item_offset)
            
            self._list_len -= del_items_num
        else:
            raise TypeError
    
    def append(self, item: Any) -> None:
        if self._list_len > self._list_capacity:
            self._pointer_to_internal_list, result_size = realloc_tinternal_list(self._shared_memory, self._pointer_to_internal_list)

        item_mapped_obj, item_offset, item_size = self._shared_memory.put_obj(item)
        write_uint64(self._base_address, self._item_offset(self._list_len), item_offset)
        self._list_len += 1

    def extend(self, items: Sequence) -> None:
        items_num = len(items)
        if self._list_len + items_num > self._list_capacity:
            self._pointer_to_internal_list, result_size = realloc_tinternal_list(self._shared_memory, self._pointer_to_internal_list, self._list_len + items_num)

        for i, item in enumerate(items):
            item_mapped_obj, item_offset, item_size = self._shared_memory.put_obj(item)
            write_uint64(self._base_address, self._item_offset(self._list_len + i), item_offset)
        
        self._list_len += items_num
    
    def insert(self, index: int, item: Any) -> None:
        if index < 0:
            index += len(self)
        if index < 0 or index > len(self):
            raise IndexError

        if self._list_len > self._list_capacity:
            self._pointer_to_internal_list, result_size = realloc_tinternal_list(self._shared_memory, self._pointer_to_internal_list)

        for i in range(self._list_len, index, -1):
            item_offset = read_uint64(self._base_address, self._item_offset(i - 1))
            write_uint64(self._base_address, self._item_offset(i), item_offset)
        
        item_mapped_obj, item_offset, item_size = self._shared_memory.put_obj(item)
        write_uint64(self._base_address, self._item_offset(index), item_offset)
        self._list_len += 1
    
    def pop(self, index: int = -1) -> Any:
        if index < 0:
            index += len(self)
        if index < 0 or index >= len(self):
            raise IndexError

        item_offset = read_uint64(self._base_address, self._item_offset(index))
        result = self._shared_memory.get_obj(item_offset)
        
        for i in range(index + 1, len(self)):
            item_offset = read_uint64(self._base_address, self._item_offset(i))
            write_uint64(self._base_address, self._item_offset(i - 1), item_offset)
        
        self._list_len -= 1
        return result
    
    def remove(self, item: Any) -> None:
        for i in range(len(self)):
            item_offset = read_uint64(self._base_address, self._item_offset(i))
            if item_offset == item._offset:
                for j in range(i + 1, len(self)):
                    item_offset = read_uint64(self._base_address, self._item_offset(j))
                    write_uint64(self._base_address, self._item_offset(j - 1), item_offset)
                
                self._list_len -= 1
                return
        
        raise ValueError
    
    def clear(self) -> None:
        for i in range(len(self)):
            item_offset = read_uint64(self._base_address, self._item_offset(i))
            self._shared_memory.free(item_offset)
        
        self._list_len = 0
    
    def __iter__(self):
        return IListIterator(self)
    
    def __reversed__(self):
        return IListReversedIterator(self)
    
    def __contains__(self, item: Any) -> bool:
        for i in range(len(self)):
            item_offset = read_uint64(self._base_address, self._item_offset(i))
            if item_offset == item._offset:
                return True
        
        return False
    
    def index(self, item: Any, start: int = 0, stop: int = None) -> int:
        if stop is None:
            stop = len(self)
        
        for i in range(start, stop):
            item_offset = read_uint64(self._base_address, self._item_offset(i))
            if item_offset == item._offset:
                return i
        
        raise ValueError
    
    def count(self, item: Any) -> int:
        result = 0
        for i in range(len(self)):
            item_offset = read_uint64(self._base_address, self._item_offset(i))
            if item_offset == item._offset:
                result += 1
        
        return result
    
    def reverse(self) -> None:
        for i in range(len(self) // 2):
            item_offset = read_uint64(self._base_address, self._item_offset(i))
            write_uint64(self._base_address, self._item_offset(i), read_uint64(self._base_address, self._item_offset(len(self) - i - 1)))
            write_uint64(self._base_address, self._item_offset(len(self) - i - 1), item_offset)
    
    def sort(self, key: Any = None, reverse: bool = False) -> None:
        raise NotImplementedError
    
    def copy(self) -> 'IList':
        result = IList(self._shared_memory)
        result.extend(self)
        return result
    
    def __add__(self, other: Sequence) -> 'IList':
        result = IList(self._shared_memory)
        result.extend(self)
        result.extend(other)
        return result
    
    def __iadd__(self, other: Sequence) -> 'IList':
        self.extend(other)
        return self
    
    def __mul__(self, other: int) -> 'IList':
        result = IList(self._shared_memory)
        for i in range(other):
            result.extend(self)
        
        return result
    
    def __imul__(self, other: int) -> 'IList':
        my_copy: IList = self.copy()
        for i in range(other):
            self.extend(my_copy)
        
        return self
    
    def __rmul__(self, other: int) -> 'IList':
        return self.__mul__(other)
    
    def __eq__(self, other: Sequence) -> bool:
        if len(self) != len(other):
            return False
        
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        
        return True
    
    def __ne__(self, other: Sequence) -> bool:
        return not self.__eq__(other)
    
    def __lt__(self, other: Sequence) -> bool:
        for i in range(len(self)):
            if self[i] >= other[i]:
                return False
        
        return True
    
    def __le__(self, other: Sequence) -> bool:
        for i in range(len(self)):
            if self[i] > other[i]:
                return False
        
        return True
    
    def __gt__(self, other: Sequence) -> bool:
        for i in range(len(self)):
            if self[i] <= other[i]:
                return False
        
        return True
    
    def __ge__(self, other: Sequence) -> bool:
        for i in range(len(self)):
            if self[i] < other[i]:
                return False
        
        return True
    
    def __repr__(self) -> str:
        return f'IList({list(self)})'
    
    def __str__(self) -> str:
        return f'IList({list(self)})'
    
    def __hash__(self) -> int:
        return hash(tuple(self))
    
    def __sizeof__(self) -> int:
        return read_uint64(self._base_address, self._offset + 8 * BaseObjOffsets.obj_size) + read_uint64(self._base_address, self._pointer_to_internal_list, 8 * BaseObjOffsets.obj_size)
    
    def export(self) -> list:
        return list(self)

    # def __del__(self) -> None:
    #     self._shared_memory.free(self._pointer_to_internal_list)
    #     self._shared_memory.free(self._offset)


# ======================================================================================================================
# === InternalList =====================================================================================================


class InternalListOffsets(IntEnum):
    capacity = 0
    size = 1


class InternalListFieldOffsets(IntEnum):
    field_type = 0
    offset_or_data = 1


class InternalListFieldTypes(IntEnum):
    tnone = 0
    tobj = 1
    tint = 2
    tfloat = 3
    tbool = 4


def malloc_tinternal_list(shared_memory: 'SharedMemory', size: Size, capacity: Size = None) -> Tuple[Offset, Size]:
    if (capacity is not None) and (size > capacity):
        raise ValueError
    
    capacity = (size << 1 if size else 16) if capacity is None else capacity
    offset, real_size = shared_memory.malloc(ObjectType.tinternal_list, 16 + 16 + capacity * 16, zero_mem=True)
    sys_data_offset = offset + 16
    write_uint64(shared_memory.base_address, sys_data_offset + 0, capacity)
    write_uint64(shared_memory.base_address, sys_data_offset + 8, size)
    return offset, real_size


def realloc_tinternal_list(shared_memory: 'SharedMemory', offset: Offset, desired_size: int = None, new_capacity: int = None, loop_allowed: bool = True, zero_mem: bool = True) -> Tuple[Offset, Size]:
    if (desired_size is not None) and (new_capacity is not None) and (desired_size > new_capacity):
        raise ValueError
    
    sys_data_offset = offset + 16
    capacity = read_uint64(shared_memory.base_address, sys_data_offset + 0)
    size = read_uint64(shared_memory.base_address, sys_data_offset + 8)
    new_list_capacity = capacity << 1 if new_capacity is None else new_capacity
    if new_capacity is None:
        if desired_size is None:
            new_list_capacity = capacity << 1 if capacity else 16
        else:
            new_list_capacity = desired_size << 1 if desired_size else 16
    else:
        new_list_capacity = new_capacity
    
    if new_list_capacity < size:
        new_list_capacity = size
    
    if new_list_capacity == capacity:
        real_size = read_uint64(shared_memory.base_address, offset + 8)
        return offset, real_size

    new_offset, new_real_size = shared_memory.realloc(
            offset,
            16 + new_list_capacity * 16,
            loop_allowed,
            zero_mem
        )
    new_sys_data_offset = new_offset + 16
    write_uint64(shared_memory.base_address, new_sys_data_offset + 0, new_list_capacity)
    return new_offset, new_real_size


def destroy_tinternal_list(shared_memory: 'SharedMemory', offset: Offset) -> None:
    shared_memory.free(offset)


def uint64_to_bytes(int_data: int) -> bytes:
    """
    For a 64 bit unsigned int in little endian
    :param int_data:
    :return: bytes(); len == 8
    """
    from struct import pack
    result = pack('<B', int_data)
    return result


def uint8_to_bytes(int_data: int) -> bytes:
    """
    For a 64 bit unsigned int in little endian
    :param int_data:
    :return: bytes(); len == 8
    """
    from struct import pack
    result = pack('<Q', int_data)
    return result


# ======================================================================================================================
# === List =====================================================================================================


class ListOffsets(IntEnum):
    internal_list_offset = 0


class IList(BaseIObject, list):
    def __init__(self, shared_memory: 'SharedMemory', offset: Offset = None, obj: List = None) -> None:
        self._shared_memory = shared_memory
        self._base_address = shared_memory.base_address
        if offset is None:
            offset, real_size = shared_memory.malloc(ObjectType.tlist, 8)
            try:
                self._offset = offset
                self._offset__data = offset + 16
                self._offset__pointer_to_internal_list = self._offset__data + 0
                
                if obj is None:
                    obj = list()
                
                data_len = len(obj)
                internal_list_offset, data_tuple_real_size = malloc_tinternal_list(shared_memory, data_len)
                self._pointer_to_internal_list = internal_list_offset
                for i, item in enumerate(obj):
                    # print(self.get_children_offsets())
                    # # print(self.raw_to_list(slice(0, None)))
                    # print(self.raw_to_bytes(200))
                    self._write_item(i, item)
                    # print(self.get_children_offsets())
                    # # print(self.raw_to_list(slice(0, None)))
                    # print(self.raw_to_bytes(200))
                
                # print(self.get_children_offsets())
                # # print(self.raw_to_list(slice(0, None)))
                # print(self.raw_to_bytes(200))
                # print('=======================')
            except:
                self._free_mem()
                raise
        else:
            self._offset = offset
            self._offset__data = offset + 16
            self._offset__pointer_to_internal_list = self._offset__data + 0
    
    def raw_to_list(self, key) -> List[bytes]:
        if isinstance(key, int):
            if key < 0:
                key += len(self)
            if key < 0 or key >= len(self):
                raise IndexError

            item_offset = self._read_item_offset_or_data(key)
            return [uint64_to_bytes(item_offset)]
        elif isinstance(key, slice):
            if key.step is not None:
                raise NotImplementedError
            
            if key.start is None:
                start = 0
            elif key.start < 0:
                start = key.start + len(self)
            else:
                start = key.start
            
            if key.stop is None:
                stop = len(self)
            elif key.stop < 0:
                stop = key.stop + len(self)
            else:
                stop = key.stop
            
            if start < 0 or start >= len(self) or stop < 0 or stop > len(self) or start >= stop:
                raise IndexError
            
            result_list = list()
            for i in range(start, stop):
                item_offset = self._read_item_offset_or_data(i)
                result_list.append(uint64_to_bytes(item_offset))
            
            return result_list
    
    def raw_to_bytes(self, bytes_num: int) -> bytes:
        start_index = self._pointer_to_internal_list
        return self._shared_memory.read_mem(start_index, bytes_num)
        # return bytes(self._shared_memory._shared_memory.buf[start_index : start_index + bytes_num])

    @property
    def _obj_size(self):
        return read_uint64(self._base_address, self._offset + 8)
    
    @property
    def _pointer_to_internal_list(self):
        return read_uint64(self._base_address, self._offset__pointer_to_internal_list)

    @_pointer_to_internal_list.setter
    def _pointer_to_internal_list(self, value: Offset):
        write_uint64(self._base_address, self._offset__pointer_to_internal_list, value)

    @property
    def _list_len(self):
        return read_uint64(self._base_address, self._pointer_to_internal_list + 16 + 8)
    
    @_list_len.setter
    def _list_len(self, value: int):
        write_uint64(self._base_address, self._pointer_to_internal_list + 16 + 8, value)

    @property
    def _list_capacity(self):
        return read_uint64(self._base_address, self._pointer_to_internal_list + 16 + 0)
    
    def _item_offset(self, key: int) -> Offset:
        return self._pointer_to_internal_list + 16 + 16 + key * 16
    
    def _item_type_offset(self, key: int) -> Offset:
        # from os import getpid
        result = self._pointer_to_internal_list + 16 + 16 + key * 16 + 0
        # add_0 = 16
        # add_1 = 16
        # add_2 = key * 16
        # add_3 = 0
        # print(f'PID: {getpid()}. [{add_0},{add_1},{add_2},{add_3}],{add_0 + add_1 + add_2 + add_3},{self._pointer_to_internal_list}: item_type_offset: {key}:{result}')
        return result

    def _item_value_offset(self, key: int) -> Offset:
        # from os import getpid
        result = self._pointer_to_internal_list + 16 + 16 + key * 16 + 8
        # print(f'PID: {getpid()}. {16 + 16 + key * 16 + 8},{self._pointer_to_internal_list}: item_value_offset: {key}:{result}')
        return result

    def _read_item_type(self, key: int) -> int:
        return read_uint64(self._base_address, self._item_type_offset(key))
    
    def _write_item_type(self, key: int, item_type: int) -> None:
        write_uint64(self._base_address, self._item_type_offset(key), item_type)
    
    def _read_item_offset_or_data(self, key: int) -> Union[Offset, int]:
        return read_uint64(self._base_address, self._item_value_offset(key))

    def _write_item_offset_or_data(self, key: int, offset_or_data: Union[Offset, int]) -> None:
        write_uint64(self._base_address, self._item_value_offset(key), offset_or_data)
    
    # def _determine_obj_type(self, obj: Any) -> int:
    #     if isinstance(obj, int):
    #         return 1
    #     elif isinstance(obj, float):
    #         return 2
    #     elif isinstance(obj, bool):
    #         return 3
    #     else:
    #         return 0
    
    def _determine_obj_type(self, obj: Any) -> int:
        if type(obj) is int:
            return 2
        elif type(obj) is float:
            return 3
        elif type(obj) is bool:
            return 4
        elif obj is None:
            return 0
        else:
            return 1
    
    def _determine_obj_offset(self, obj: Any) -> Optional[Offset]:
        if isinstance(obj, BaseIObject):
            return obj._offset
        else:
            return None
    
    def _compare_item_to_obj_fast(self, key: int, obj: Any, obj_type: int, obj_offset) -> bool:
        result: bool = False
        item_type = self._read_item_type(key)
        if item_type == obj_type:
            if item_type == 1:
                if obj_offset is None:
                    if self._read_item_value(key, item_type) == obj:
                        result = True
                else:
                    if self._read_item_offset_or_data(key) == obj_offset:
                        result = True
            elif item_type == 2:
                if self._read_item_offset_or_data(key) == obj:
                    result = True
            elif item_type == 3:
                if self._read_item_offset_or_data(key) == obj:
                    result = True
            elif item_type == 4:
                if self._read_item_offset_or_data(key) == obj:
                    result = True
            elif item_type == 0:
                result = obj is None
            else:
                raise ValueError

        return result
    
    def _compare_item_to_obj(self, key: int, obj: Any) -> bool:
        obj_type = self._determine_obj_type(obj)
        obj_offset = self._determine_obj_offset(obj)
        return self._compare_item_to_obj_fast(key, obj, obj_type, obj_offset)

    def _read_item_value(self, key: int, item_type: int) -> Any:
        if item_type == 1:
            item_offset = read_uint64(self._base_address, self._item_value_offset(key))
            return self._shared_memory.get_obj(item_offset)
        elif item_type == 2:
            return read_int64(self._base_address, self._item_value_offset(key))
        elif item_type == 3:
            return read_double(self._base_address, self._item_value_offset(key))
        elif item_type == 4:
            return bool(read_uint64(self._base_address, self._item_value_offset(key)))
        elif item_type == 0:
            return None
        else:
            raise ValueError
    
    def _write_item_value(self, key: int, item_type: int, value: Any) -> None:
        if item_type == 1:
            item_mapped_obj, item_offset, item_size = self._shared_memory.put_obj(value)
            write_uint64(self._base_address, self._item_value_offset(key), item_offset)
        elif item_type == 2:
            write_int64(self._base_address, self._item_value_offset(key), value)
        elif item_type == 3:
            write_double(self._base_address, self._item_value_offset(key), value)
        elif item_type == 4:
            write_uint64(self._base_address, self._item_value_offset(key), int(value))
        elif item_type == 0:
            pass
        else:
            raise ValueError
    
    def _free_item_value(self, key: int, item_type: int) -> None:
        if item_type == 1:
            item_offset = read_uint64(self._base_address, self._item_value_offset(key))
            # self._shared_memory.free(item_offset)
            self._shared_memory.destroy_obj(item_offset)
        elif item_type == 2:
            pass
        elif item_type == 3:
            pass
        elif item_type == 4:
            pass
        elif item_type == 0:
            pass
        else:
            raise ValueError

        self._write_item_type(key, 0)
    
    def _read_item_type_and_value(self, key: int) -> Tuple[int, Any]:
        item_type = self._read_item_type(key)
        return item_type, self._read_item_value(key, item_type)
    
    def _write_item_value_and_get_type(self, key: int, value: Any) -> int:
        if isinstance(value, int):
            write_uint64(self._base_address, self._item_value_offset(key), value)
            return 2
        elif isinstance(value, float):
            write_double(self._base_address, self._item_value_offset(key), value)
            return 3
        elif isinstance(value, bool):
            write_uint64(self._base_address, self._item_value_offset(key), int(value))
            return 4
        elif value is None:
            return 0
        else:
            item_mapped_obj, item_offset, item_size = self._shared_memory.put_obj(value)
            write_uint64(self._base_address, self._item_value_offset(key), item_offset)
            return 1
    
    def _free_item_value_and_get_type(self, key: int) -> int:
        item_type = self._read_item_type(key)
        self._free_item_value(key, item_type)
        return item_type
    
    def _read_item(self, key: int) -> Any:
        item_type = self._read_item_type(key)
        return self._read_item_value(key, item_type)
    
    def _write_item(self, key: int, value: Any) -> None:
        item_type = self._write_item_value_and_get_type(key, value)
        self._write_item_type(key, item_type)
    
    def _free_item(self, key: int) -> None:
        item_type = self._read_item_type(key)
        self._free_item_value(key, item_type)
    
    def _copy_item(self, src_key: int, dst_key: int) -> None:
        self._write_item_type(dst_key, self._read_item_type(src_key))
        self._write_item_offset_or_data(dst_key, self._read_item_offset_or_data(src_key))
    
    def copy_item(self, src_key: int, dst_key: int) -> None:
        return self._copy_item(src_key, dst_key)
    
    def _move_item(self, src_key: int, dst_key: int) -> None:
        self._write_item_type(dst_key, self._read_item_type(src_key))
        self._write_item_type(src_key, 0)
        self._write_item_offset_or_data(dst_key, self._read_item_offset_or_data(src_key))
    
    def move_item(self, src_key: int, dst_key: int) -> None:
        return self._move_item(src_key, dst_key)
    
    def copy_item_to_list(self, src_key: int, other: 'IList', dst_key: int) -> None:
        other._write_item_type(dst_key, self._read_item_type(src_key))
        other._write_item_offset_or_data(dst_key, self._read_item_offset_or_data(src_key))
    
    def move_item_to_list(self, src_key: int, other: 'IList', dst_key: int) -> None:
        other._write_item_type(dst_key, self._read_item_type(src_key))
        self._write_item_type(src_key, 0)
        other._write_item_offset_or_data(dst_key, self._read_item_offset_or_data(src_key))
    
    def _swap_items(self, key1: int, key2: int) -> None:
        item_type1 = self._read_item_type(key1)
        item_offset_or_data1 = self._read_item_offset_or_data(key1)
        self._write_item_type(key1, self._read_item_type(key2))
        self._write_item_type(key2, item_type1)
        self._write_item_offset_or_data(key1, self._read_item_offset_or_data(key2))
        self._write_item_offset_or_data(key2, item_offset_or_data1)
    
    def swap_items(self, key1: int, key2: int) -> None:
        return self._swap_items(key1, key2)

    def __len__(self) -> int:
        return self._list_len
    
    def get_children_data_or_offsets(self) -> List[Offset]:
        return [self._read_item_offset_or_data(i) for i in range(self._list_len)]
    
    def get_children_offsets(self):
        return self.get_children_data_or_offsets()

    def _getitem_as_offset(self, key: int) -> Tuple[int, Offset]:
            return list__get_item_as_offset(key, self._base_address, self._offset__pointer_to_internal_list)

    def __getitem__(self, key: Union[int, slice]) -> Union[Any, List]:
        if isinstance(key, int):
            base_address = self._base_address
            offset__pointer_to_internal_list = self._offset__pointer_to_internal_list
            pointer_to_internal_list = read_uint64(base_address, offset__pointer_to_internal_list)
            self_len = read_uint64(base_address, pointer_to_internal_list + 24)
            if key < 0 or key >= self_len:
                raise IndexError

            return list__get_item(key, self._base_address, self._offset__pointer_to_internal_list, self._shared_memory.get_obj)

            # base_address = self._base_address
            # offset__pointer_to_internal_list = self._offset__pointer_to_internal_list
            # pointer_to_internal_list = read_uint64(base_address, offset__pointer_to_internal_list)
            # self_len = read_uint64(base_address, pointer_to_internal_list + 24)

            # if key < 0:
            #     key += self_len
            
            # if key < 0 or key >= self_len:
            #     raise IndexError

            # item_type_offset = pointer_to_internal_list + 32 + key * 16
            # item_value_offset = pointer_to_internal_list + 40 + key * 16
            # item_type = read_uint64(base_address, item_type_offset)
            # if item_type == 1:
            #     return read_int64(base_address, item_value_offset)
            # elif item_type == 2:
            #     return read_double(base_address, item_value_offset)
            # elif item_type == 3:
            #     return bool(read_uint64(base_address, item_value_offset))
            # elif item_type == 0:
            #     item_offset = read_uint64(base_address, item_value_offset)
            #     return self._shared_memory.get_obj(item_offset)
            # else:
            #     raise ValueError

            # # return self._read_item(key)
        elif isinstance(key, slice):
            if key.step is not None:
                raise NotImplementedError
            
            if key.start is None:
                start = 0
            elif key.start < 0:
                start = key.start + len(self)
            else:
                start = key.start
            
            if key.stop is None:
                stop = len(self)
            elif key.stop < 0:
                stop = key.stop + len(self)
            else:
                stop = key.stop
            
            if start < 0 or start >= len(self) or stop < 0 or stop > len(self) or start >= stop:
                raise IndexError
            
            result_list = list()
            # performance improvement instead of using self._read_item(i)
            base_address = self._base_address
            offset__pointer_to_internal_list = self._offset__pointer_to_internal_list
            pointer_to_internal_list = read_uint64(base_address, offset__pointer_to_internal_list)

            # item_type_offset = pointer_to_internal_list + 32 + i * 16
            item_type_offset = pointer_to_internal_list + 16 + 16 + i * 16 + 0

            # item_value_offset = pointer_to_internal_list + 40 + i * 16
            item_value_offset = pointer_to_internal_list + 16 + 16 + i * 16 + 8

            for i in range(start, stop):
                # result_list.append(self._read_item(i))

                # performance improvement instead of using self._read_item(i)
                item_type = read_uint64(base_address, item_type_offset)
                if item_type == 2:
                    result_list.append(read_int64(base_address, item_value_offset))
                elif item_type == 3:
                    result_list.append(read_double(base_address, item_value_offset))
                elif item_type == 4:
                    result_list.append(bool(read_uint64(base_address, item_value_offset)))
                elif item_type == 0:
                    result_list.append(None)
                elif item_type == 1:
                    item_offset = read_uint64(base_address, item_value_offset)
                    result_list.append(self._shared_memory.get_obj(item_offset))
                else:
                    raise ValueError
            
            return result_list
        else:
            raise TypeError

    def _setitem_as_offset(self, key: int, value_type_and_offset: Tuple[int, Offset], need_to_free_item: bool = True) -> Any:
        value_item_type, value_item_offset = value_type_and_offset
        list__set_item_as_offset(key, value_item_type, value_item_offset, self._base_address, self._offset__pointer_to_internal_list, need_to_free_item, self._shared_memory.destroy_obj)
    
    def __setitem__(self, key: Union[int, slice], value: Union[Any, Sequence], need_to_free_item: bool = True) -> Any:
        if isinstance(key, int):
            # print(f'{key=}, {value=}, {need_to_free_item=}')
            # internal_list_data_offset = self._pointer_to_internal_list + 16 + 16 + key * 16 + 0
            # internal_list_data_size = self._list_len * 16
            # self._shared_memory.print_mem(internal_list_data_offset, internal_list_data_size, 'internal_list before list__set_item')
            
            base_address = self._base_address
            offset__pointer_to_internal_list = self._offset__pointer_to_internal_list
            pointer_to_internal_list = read_uint64(base_address, offset__pointer_to_internal_list)
            self_len = read_uint64(base_address, pointer_to_internal_list + 24)
            if key < 0 or key >= self_len:
                raise IndexError

            list__set_item(key, value, self._base_address, self._offset__pointer_to_internal_list, need_to_free_item, self._shared_memory.destroy_obj, self._shared_memory.put_obj)

            # base_address = self._base_address
            # offset__pointer_to_internal_list = self._offset__pointer_to_internal_list
            # pointer_to_internal_list = read_uint64(base_address, offset__pointer_to_internal_list)
            # self_len = read_uint64(base_address, pointer_to_internal_list + 24)

            # if key < 0:
            #     key += self_len
            
            # if key < 0 or key >= self_len:
            #     raise IndexError
            
            # item_type_offset = pointer_to_internal_list + 32 + key * 16
            # item_value_offset = pointer_to_internal_list + 40 + key * 16
            # if isinstance(value, int):
            #     write_int64(base_address, item_value_offset, value)
            #     item_type = 1
            # elif isinstance(value, float):
            #     write_double(base_address, item_value_offset, value)
            #     item_type = 2
            # elif isinstance(value, bool):
            #     write_uint64(base_address, item_value_offset, int(value))
            #     item_type = 3
            # else:
            #     item_mapped_obj, item_offset, item_size = self._shared_memory.put_obj(value)
            #     write_uint64(base_address, item_value_offset, item_offset)
            #     item_type = 0
            
            # write_uint64(base_address, item_type_offset, item_type)

            # # self._write_item(key, value)
        elif isinstance(key, slice):
            if key.step is not None:
                raise NotImplementedError
            
            if key.start is None:
                start = 0
            elif key.start < 0:
                start = key.start + len(self)
            else:
                start = key.start
            
            if key.stop is None:
                stop = len(self)
            elif key.stop < 0:
                stop = key.stop + len(self)
            else:
                stop = key.stop
            
            if start < 0 or start >= len(self) or stop < 0 or stop > len(self) or start >= stop:
                raise IndexError
            
            if need_to_free_item:
                for i in range(start, stop):
                    self._free_item(i)
            
            # performance improvement instead of using self._write_item(i, item)
            base_address = self._base_address
            offset__pointer_to_internal_list = self._offset__pointer_to_internal_list
            pointer_to_internal_list = read_uint64(base_address, offset__pointer_to_internal_list)

            # item_type_offset = pointer_to_internal_list + 32 + i * 16
            item_type_offset = pointer_to_internal_list + 16 + 16 + i * 16 + 0

            # item_value_offset = pointer_to_internal_list + 40 + i * 16
            item_value_offset = pointer_to_internal_list + 16 + 16 + i * 16 + 8

            for i in range(start, stop):
                item = value[i - start]
                # self._write_item(i, item)

                # performance improvement instead of using self._write_item(i, item)
                if isinstance(item, int):
                    write_int64(base_address, item_value_offset, item)
                    item_type = 2
                elif isinstance(item, float):
                    write_double(base_address, item_value_offset, item)
                    item_type = 3
                elif isinstance(item, bool):
                    write_uint64(base_address, item_value_offset, int(item))
                    item_type = 4
                elif item is None:
                    item_type = 0
                else:
                    item_mapped_obj, item_offset, item_size = self._shared_memory.put_obj(item)
                    write_uint64(base_address, item_value_offset, item_offset)
                    item_type = 1
                
                write_uint64(base_address, item_type_offset, item_type)
        else:
            raise TypeError

    def __delitem__(self, key: Union[int, slice], need_to_free_item: bool = True) -> None:
        if isinstance(key, int):
            if key < 0:
                key += len(self)
            if key < 0 or key >= len(self):
                raise IndexError

            if need_to_free_item:
                self._free_item(key)

            for i in range(key + 1, len(self)):
                self._move_item(i, i - 1)
            
            self._list_len -= 1
        elif isinstance(key, slice):
            if key.step is not None:
                raise NotImplementedError
            
            if key.start is None:
                start = 0
            elif key.start < 0:
                start = key.start + len(self)
            else:
                start = key.start
            
            if key.stop is None:
                stop = len(self)
            elif key.stop < 0:
                stop = key.stop + len(self)
            else:
                stop = key.stop
            
            if start < 0 or start >= len(self) or stop < 0 or stop > len(self) or start >= stop:
                raise IndexError
            
            if need_to_free_item:
                for i in range(start, stop):
                    self._free_item(i)
            
            del_items_num = stop - start
            
            for i in range(stop, len(self)):
                self._move_item(i, i - del_items_num)
            
            self._list_len -= del_items_num
        else:
            raise TypeError
    
    def append(self, item: Any) -> None:
        if self._list_len > self._list_capacity:
            self._pointer_to_internal_list, result_size = realloc_tinternal_list(self._shared_memory, self._pointer_to_internal_list)

        self._list_len += 1
        self.__setitem__(self._list_len - 1, item, need_to_free_item=False)
    
    def append_as_offset(self, value_type_and_offset: Tuple[int, Offset]) -> None:
        if self._list_len > self._list_capacity:
            self._pointer_to_internal_list, result_size = realloc_tinternal_list(self._shared_memory, self._pointer_to_internal_list)

        self._list_len += 1
        self._setitem_as_offset(self._list_len - 1, value_type_and_offset, need_to_free_item=False)
    
    def getitem_as_offset(self, key: int) -> Tuple[int, Offset]:
        return self._getitem_as_offset(key)
    
    def setitem_as_offset(self, key: int, value_type_and_offset: Tuple[int, Offset], need_to_free_item=True) -> None:
        self._setitem_as_offset(key, value_type_and_offset, need_to_free_item)

    def extend(self, items: Sequence) -> None:
        items_num = len(items)
        if (self._list_len + items_num) > self._list_capacity:
            self._pointer_to_internal_list, result_size = realloc_tinternal_list(self._shared_memory, self._pointer_to_internal_list, self._list_len + items_num)

        original_list_len = self._list_len
        self._list_len += items_num
        for i, item in enumerate(items):
            self.__setitem__(original_list_len + i, item, need_to_free_item=False)
    
    def extend_with(self, items_num: int, value = None) -> None:
        if (self._list_len + items_num) > self._list_capacity:
            self._pointer_to_internal_list, result_size = realloc_tinternal_list(self._shared_memory, self._pointer_to_internal_list, self._list_len + items_num)

        original_list_len = self._list_len
        self._list_len += items_num
        for i in range(items_num):
            self.__setitem__(original_list_len + i, value, need_to_free_item=False)

    def set_capacity(self, capacity: int) -> int:
        if capacity <= self._list_capacity:
            return
        
        self._pointer_to_internal_list, result_size = realloc_tinternal_list(self._shared_memory, self._pointer_to_internal_list, capacity)
        return result_size
    
    def insert(self, index: int, item: Any) -> None:
        if index < 0:
            index += len(self)
        if index < 0 or index > len(self):
            raise IndexError

        if self._list_len > self._list_capacity:
            # self._shared_memory.print_mem(self._pointer_to_internal_list, 200, 'before realloc. {}')
            # self.print_internal_list('before realloc. {}')
            self._pointer_to_internal_list, result_size = realloc_tinternal_list(self._shared_memory, self._pointer_to_internal_list)
            # self._shared_memory.print_mem(self._pointer_to_internal_list, 200, 'after realloc. {}')
            # self.print_internal_list('after realloc. {}')

        # self.print_internal_list('before inserting {}')
        self._list_len += 1
        # self.print_internal_list('before inserting but after +1 {}')
        for i in range(self._list_len - 1, index, -1):
            self._move_item(i - 1, i)
            # self._shared_memory.print_mem(self._pointer_to_internal_list, 200, f'after self._move_item({i - 1, i}). {{}}')
            # self.print_internal_list(f'after self._move_item({i - 1, i}). {{}}')
        
        self.__setitem__(index, item, need_to_free_item=False)
        # self._shared_memory.print_mem(self._pointer_to_internal_list, 200, 'after inserting. {}')
        # self.print_internal_list('after inserting. {}')
    
    def print_internal_list(self, text: str = None, additional_cells: int = 0):
        internal_list = self._shared_memory.read_mem(self._pointer_to_internal_list, 16 + 16 + self._list_len * 16 + additional_cells * 16)
        print('--- internal list -------------')
        if text:
            print(text.format(self._pointer_to_internal_list))
            print('------')

        index = 0
        print(f'{index},{self._pointer_to_internal_list + index}:', internal_list[index:index + 8])
        index += 8
        print(f'{index},{self._pointer_to_internal_list + index}:', internal_list[index:index + 8])
        index += 8
        print('---')
        print(f'{index},{self._pointer_to_internal_list + index}:', internal_list[index:index + 8])
        index += 8
        print(f'{index},{self._pointer_to_internal_list + index}:', internal_list[index:index + 8])
        index += 8
        print('---')
        for i in range(self._list_len):
            print(f'{index},{self._pointer_to_internal_list + index}:', internal_list[index:index + 8 * 2])
            index += 8 * 2
        
        if additional_cells:
            print('------')
            for i in range(additional_cells):
                print(f'{index},{self._pointer_to_internal_list + index}:', internal_list[index:index + 8])
                index += 8 * 2
        print('-------------------------------')
        print()

    def pop(self, index: int = -1) -> Any:
        if index < 0:
            index += len(self)
        if index < 0 or index >= len(self):
            raise IndexError

        result = self.__getitem__(index)
        
        for i in range(index + 1, len(self)):
            self._move_item(i, i - 1)
        
        self._list_len -= 1
        return result
    
    def remove(self, obj: Any) -> None:
        obj_type = self._determine_obj_type(obj)
        obj_offset = self._determine_obj_offset(obj)
        found_in_index = None
        for i in range(len(self)):
            if self._compare_item_to_obj_fast(i, obj, obj_type, obj_offset):
                found_in_index = i
                break
        
        if found_in_index is None:
            raise ValueError
        else:
            self.__delitem__(found_in_index)
    
    def clear(self, need_to_free_item: bool = True) -> None:
        if need_to_free_item:
            for i in range(len(self)):
                self._free_item(i)
        
        self._list_len = 0
    
    def __iter__(self):
        return IListIterator(self)
    
    def __reversed__(self):
        return IListReversedIterator(self)
    
    def __contains__(self, obj: Any) -> bool:
        obj_type = self._determine_obj_type(obj)
        obj_offset = self._determine_obj_offset(obj)
        found_in_index = None
        for i in range(len(self)):
            if self._compare_item_to_obj_fast(i, obj, obj_type, obj_offset):
                found_in_index = i
                break
        
        if found_in_index is None:
            return False
        else:
            return True
    
    def index(self, obj: Any, start: int = 0, stop: int = None) -> int:
        if stop is None:
            stop = len(self)

        obj_type = self._determine_obj_type(obj)
        obj_offset = self._determine_obj_offset(obj)
        found_in_index = None
        for i in range(start, stop):
            if self._compare_item_to_obj_fast(i, obj, obj_type, obj_offset):
                found_in_index = i
                break

        if found_in_index is None:
            raise ValueError
        else:
            return found_in_index
    
    def count(self, obj: Any) -> int:
        obj_type = self._determine_obj_type(obj)
        obj_offset = self._determine_obj_offset(obj)
        result = 0
        for i in range(len(self)):
            if self._compare_item_to_obj_fast(i, obj, obj_type, obj_offset):
                result += 1

        return result
    
    def reverse(self) -> None:
        my_len = len(self)
        for i in range(my_len // 2):
            self._swap_items(i, my_len - i - 1)
    
    def sort(self, key: Any = None, reverse: bool = False) -> None:
        raise NotImplementedError
    
    def copy(self) -> 'IList':
        result = IList(self._shared_memory)
        result.extend(self)
        return result
    
    def __add__(self, other: Sequence) -> 'IList':
        result = IList(self._shared_memory)
        result.extend(self)
        result.extend(other)
        return result
    
    def __iadd__(self, other: Sequence) -> 'IList':
        self.extend(other)
        return self
    
    def __mul__(self, other: int) -> 'IList':
        result = IList(self._shared_memory)
        for i in range(other):
            result.extend(self)
        
        return result
    
    def __imul__(self, other: int) -> 'IList':
        my_copy: IList = self.copy()
        for i in range(other):
            self.extend(my_copy)
        
        return self
    
    def __rmul__(self, other: int) -> 'IList':
        return self.__mul__(other)
    
    def __eq__(self, other: Sequence) -> bool:
        if len(self) != len(other):
            return False
        
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        
        return True
    
    def __ne__(self, other: Sequence) -> bool:
        return not self.__eq__(other)
    
    def __lt__(self, other: Sequence) -> bool:
        for i in range(len(self)):
            if self[i] >= other[i]:
                return False
        
        return True
    
    def __le__(self, other: Sequence) -> bool:
        for i in range(len(self)):
            if self[i] > other[i]:
                return False
        
        return True
    
    def __gt__(self, other: Sequence) -> bool:
        for i in range(len(self)):
            if self[i] <= other[i]:
                return False
        
        return True
    
    def __ge__(self, other: Sequence) -> bool:
        for i in range(len(self)):
            if self[i] < other[i]:
                return False
        
        return True
    
    def __repr__(self) -> str:
        return f'IList({list(self)})'
    
    def __str__(self) -> str:
        return f'IList({list(self)})'
    
    def __hash__(self) -> int:
        return hash(tuple(self))
    
    def __sizeof__(self) -> int:
        return 16 + read_uint64(self._base_address, self._offset + 8) + 16 + read_uint64(self._base_address, self._pointer_to_internal_list, 8)
    
    def export(self) -> list:
        return list(self)

    # def __del__(self) -> None:
    #     self._shared_memory.free(self._pointer_to_internal_list)
    #     self._shared_memory.free(self._offset)

    def _free_mem(self):
        if self._offset is not None:
            if self._pointer_to_internal_list is not None:
                self.clear()
                destroy_tinternal_list(self._shared_memory, self._pointer_to_internal_list)
                self._pointer_to_internal_list = 0
            
            self._shared_memory.free(self._offset)
            self._offset = None


# IList = IListTrue


class IListIterator:
    def __init__(self, ilist: IList) -> None:
        self._ilist = ilist
        self._index = 0
    
    def __next__(self):
        if self._index < len(self._ilist):
            # self._ilist.print_internal_list(f'ListIterator[{self._index}]. {{}}')
            result = self._ilist[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration
    
    def __iter__(self):
        return self


class IListReversedIterator:
    def __init__(self, ilist: IList) -> None:
        self._ilist = ilist
        self._index = len(ilist) - 1
    
    def __next__(self):
        if self._index >= 0:
            result = self._ilist[self._index]
            self._index -= 1
            return result
        else:
            raise StopIteration
    
    def __iter__(self):
        return self


class TList:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: list) -> Tuple[list, Offset, Size]:
        obj = IList(shared_memory, obj=obj)
        return obj, obj._offset, obj._obj_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.tlist != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError
        
        return IList(shared_memory, offset)
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        if ObjectType.tlist != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError
        
        obj: IList = IList(shared_memory, offset)
        obj._free_mem()


# ======================================================================================================================
# === Tuple ============================================================================================================


class TupleOffsets(IntEnum):
    size = 0


class TupleFieldOffsets(IntEnum):
    item_offset = 0


class TTuple:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: tuple) -> Tuple[tuple, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.ttuple, 8 + len(obj) * 8)
        created_items_offsets: List[Offset] = list()
        try:
            if (1, [2, 3]) == obj:
                shared_memory.offset_to_be_monitored = offset
            
            write_uint64(shared_memory.base_address, offset + 16 + 0, len(obj))
            for i, item in enumerate(obj):
                item_mapped_obj, item_offset, item_size = shared_memory.put_obj(item)
                created_items_offsets.append(item_offset)
                write_uint64(shared_memory.base_address, offset + 16 + 8 + i * 8, item_offset)
        except:
            shared_memory.free(offset)
            for item_offset in created_items_offsets:
                shared_memory.destroy_obj(item_offset)
            
            raise
        
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.ttuple != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        result_list = list()
        size = read_uint64(shared_memory.base_address, offset + 16 + 0)
        for i in range(size):
            item_offset = read_uint64(shared_memory.base_address, offset + 16 + 8 + i * 8)
            result_list.append(shared_memory.get_obj(item_offset))
        
        return tuple(result_list)
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        if ObjectType.ttuple != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        size = read_uint64(shared_memory.base_address, offset + 16 + 0)
        for i in range(size):
            item_offset = read_uint64(shared_memory.base_address, offset + 16 + 8 + i * 8)
            shared_memory.destroy_obj(item_offset)
        
        shared_memory.free(offset)


# ======================================================================================================================
# === Slice =============================================================================================================


class SliceOffsets(IntEnum):
    data_tuple_offset = 0


class TSlice:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: slice) -> Tuple[slice, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.tslice, 8)
        created_items_offsets: List[Offset] = list()
        try:
            data_tuple_mapped_obj, data_tuple_offset, data_tuple_size = shared_memory.put_obj(tuple(obj.start, obj.stop, obj.step))
            created_items_offsets.append(data_tuple_offset)
            write_uint64(shared_memory.base_address, offset + 16 + 0, data_tuple_offset)
        except:
            shared_memory.free(offset)
            for item_offset in created_items_offsets:
                shared_memory.destroy_obj(item_offset)
            
            raise

        return slice(*data_tuple_mapped_obj), offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> slice:
        if ObjectType.tslice != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        data_tuple_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        result_tuple = shared_memory.get_obj(data_tuple_offset)
        return slice(*result_tuple)
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.tslice != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        data_tuple_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        shared_memory.destroy_obj(data_tuple_offset)
        shared_memory.free(offset)


# ======================================================================================================================
# === Complex =============================================================================================================


class ComplexOffsets(IntEnum):
    data_tuple_offset = 0


class TComplex:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: complex) -> Tuple[complex, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.tfastset, 8)
        created_items_offsets: List[Offset] = list()
        try:
            data_tuple_mapped_obj, data_tuple_offset, data_tuple_size = shared_memory.put_obj(tuple(obj.real, obj.imag))
            created_items_offsets.append(data_tuple_offset)
            write_uint64(shared_memory.base_address, offset + 16 + 0, data_tuple_offset)
        except:
            shared_memory.free(offset)
            for item_offset in created_items_offsets:
                shared_memory.destroy_obj(item_offset)
            
            raise

        return complex(real=data_tuple_mapped_obj[0], imag=data_tuple_mapped_obj[1]), offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> complex:
        if ObjectType.tfastset != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        data_tuple_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        result_tuple = shared_memory.get_obj(data_tuple_offset)
        return complex(real=result_tuple[0], imag=result_tuple[1])
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.tfastset != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        data_tuple_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        shared_memory.destroy_obj(data_tuple_offset)
        shared_memory.free(offset)


# ======================================================================================================================
# === FastSet =============================================================================================================


class FastLimitedSet(set):
    ...


class FastSetOffsets(IntEnum):
    data_tuple_offset = 0


class TFastSet:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: set) -> Tuple[set, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.tfastset, 8)
        created_items_offsets: List[Offset] = list()
        try:
            data_tuple_mapped_obj, data_tuple_offset, data_tuple_size = shared_memory.put_obj(tuple(obj))
            created_items_offsets.append(data_tuple_offset)
            write_uint64(shared_memory.base_address, offset + 16 + 0, data_tuple_offset)
        except:
            shared_memory.free(offset)
            for item_offset in created_items_offsets:
                shared_memory.destroy_obj(item_offset)
            
            raise

        return set(data_tuple_mapped_obj), offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> set:
        if ObjectType.tfastset != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        data_tuple_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        result_tuple = shared_memory.get_obj(data_tuple_offset)
        return set(result_tuple)
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.tfastset != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        data_tuple_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        shared_memory.destroy_obj(data_tuple_offset)
        shared_memory.free(offset)


# ======================================================================================================================
# === FastDict =============================================================================================================


class FastLimitedDict(dict):
    ...


class FastDictOffsets(IntEnum):
    data_tuple_offset = 0


class TFastDict:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: dict) -> Tuple[dict, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.tfastdict, 8)
        created_items_offsets: List[Offset] = list()
        try:
            data_tuple_mapped_obj, data_tuple_offset, data_tuple_size = shared_memory.put_obj(tuple(obj.items()))
            created_items_offsets.append(data_tuple_offset)
            write_uint64(shared_memory.base_address, offset + 16 + 0, data_tuple_offset)
        except:
            shared_memory.free(offset)
            for item_offset in created_items_offsets:
                shared_memory.destroy_obj(item_offset)
            
            raise

        return dict(data_tuple_mapped_obj), offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> dict:
        if ObjectType.tfastdict != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        data_tuple_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        result_tuple = shared_memory.get_obj(data_tuple_offset)
        return dict(result_tuple)
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.tfastdict != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        data_tuple_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        shared_memory.destroy_obj(data_tuple_offset)
        shared_memory.free(offset)


# ======================================================================================================================
# === Set =============================================================================================================


class SetOffsets(IntEnum):
    size = 0
    capacity = 1
    hashmap_offset = 2


class SetHashmapFieldTypes(IntEnum):
    tnone = 0
    tobj = 1
    tbucket = 2


class SetHashmapItemOffsets(IntEnum):
    field_type = 0
    field_hash = 1
    obj_or_bucket = 2


class SetBucketOffsets(IntEnum):
    field_hash = 0
    obj = 1


class ISet(BaseIObject, AbsSet):
    def __init__(self, shared_memory: 'SharedMemory', offset: Offset = None, obj: AbsSet = None) -> None:
        self._shared_memory = shared_memory
        self._base_address = shared_memory.base_address
        self._obj_size = None
        self._offset: Offset = None
        self._offset__data: Offset = None
        self._offset__size_offset: Offset = None
        self._offset__capacity_offset: Offset = None
        self._offset__hashmap_offset: Offset = None
        self._load_factor = 0.75
        self._hash_bits: int = None
        self._capacity: int = None
        self._size: int = None
        self.hashmap: IList = None
        self.hashmap_offset: Offset = None
        self.buckets: Dict[int, IList] = dict()

        if offset is None:
            if obj is None:
                # obj = frozenset(set())
                data_len = 16
            else:
                data_len = len(obj)

            self._size: int = data_len
            self.hash_bits = 1
            self.capacity = int(ceil(data_len / self._load_factor))

            offset, self._obj_size = shared_memory.malloc(ObjectType.tset, 24)
            try:
                self._offset = offset
                offset__data = offset + 16
                self._offset__data = offset__data
                self._offset__size_offset: Offset = offset__data + 0
                self._offset__capacity_offset: Offset = offset__data + 8
                self._offset__hashmap_offset = offset__data + 16

                write_uint64(shared_memory.base_address, self._offset__size_offset, self._size)
                write_uint64(shared_memory.base_address, self._offset__capacity_offset, self.capacity)

                self.hashmap, hashmap_offset, _ = shared_memory.put_obj(list())
                self.hashmap = cast(IList, self.hashmap)
                self.hashmap_offset = hashmap_offset
                write_uint64(shared_memory.base_address, self._offset__hashmap_offset, hashmap_offset)
                hashmap_capacity = self.capacity * 3
                self.hashmap.set_capacity(hashmap_capacity)
                self.hashmap.extend_with(hashmap_capacity, 0)
                hash_bits: int = self.hash_bits
                if obj is not None:
                    for item in obj:
                        item_hash = hash(item)
                        item_info_index: int = mask_least_significant_bits(item_hash, hash_bits) * 3
                        field_type_index = item_info_index + 0
                        item_hash_index = item_info_index + 1
                        item_bucket_index = item_info_index + 2
                        field_type = self.hashmap[field_type_index]
                        if 0 == field_type:
                            self.hashmap[field_type_index] = 1
                            self.hashmap[item_hash_index] = item_hash
                            self.hashmap[item_bucket_index] = item
                        elif 1 == field_type:
                            bucket, bucket_offset, _ = shared_memory.put_obj(list())
                            bucket = cast(IList, bucket)
                            bucket.set_capacity(2)
                            bucket.extend_with(2, 0)
                            self.buckets[item_info_index] = bucket
                            self.hashmap.move_item_to_list(item_hash_index, bucket, 0)
                            self.hashmap.move_item_to_list(item_bucket_index, bucket, 1)
                            self.hashmap[field_type_index] = 2
                            self.hashmap[item_bucket_index] = bucket_offset
                            bucket.append(item_hash)
                            bucket.append(item)
                        elif 2 == field_type:
                            bucket = self.buckets[item_info_index]
                            bucket.append(item_hash)
                            bucket.append(item)
                        else:
                            raise ValueError(f'Unknown SetHashmapFieldTypes field type at {item_info_index=}: {field_type}')
            except:
                self._free_mem()
                raise
        else:
            self._offset = offset
            offset__data = offset + 16
            self._offset__data = offset__data
            self._offset__size_offset: Offset = offset__data + 0
            self._offset__capacity_offset: Offset = offset__data + 8
            self._offset__hashmap_offset = offset__data + 16

            self._size = read_uint64(shared_memory.base_address, self._offset__size_offset)
            self.hash_bits = 1
            self.capacity = read_uint64(shared_memory.base_address, self._offset__capacity_offset)
            hashmap_offset = read_uint64(shared_memory.base_address, self._offset__hashmap_offset)
            
            self.hashmap_offset = hashmap_offset
            self.hashmap = IList(shared_memory, hashmap_offset)
            item_info_index: int = 0
            # for item_info_index in range(self.capacity):
            #     field_type_index = item_info_index * 3 + 0
            #     item_hash_index = item_info_index * 3 + 1
            #     item_bucket_index = item_info_index * 3 + 2
            #     field_type = self.hashmap[field_type_index]
            #     if 0 == field_type:
            #         continue
            #     elif 1 == field_type:
            #         continue
            #     elif 2 == field_type:
            #         bucket_offset = self.hashmap[item_bucket_index]
            #         self.buckets[item_info_index] = IList(shared_memory, bucket_offset)
            #     else:
            #         raise ValueError(f'Unknown SetHashmapFieldTypes field type at {item_info_index=}: {field_type}')

            for item_info_index in range(0, self.capacity * 3, 3):
                field_type_index = item_info_index + 0
                item_hash_index = item_info_index + 1
                item_bucket_index = item_info_index + 2
                field_type = self.hashmap[field_type_index]
                if 0 == field_type:
                    continue
                elif 1 == field_type:
                    continue
                elif 2 == field_type:
                    bucket_offset = self.hashmap[item_bucket_index]
                    self.buckets[item_info_index] = IList(shared_memory, bucket_offset)
                else:
                    raise ValueError(f'Unknown SetHashmapFieldTypes field type at {item_info_index=}: {field_type}')

    def __len__(self):
        return self._size
    
    def __iter__(self):
        return ISetIterator(self)
    
    def __contains__(self, obj: Any) -> bool:
        item_hash = hash(obj)
        item_info_index: int = mask_least_significant_bits(item_hash, self.hash_bits) * 3
        field_type_index = item_info_index + 0
        item_hash_index = item_info_index + 1
        item_bucket_index = item_info_index + 2
        field_type = self.hashmap[field_type_index]
        if 0 == field_type:
            return False
        elif 1 == field_type:
            return (item_hash == self.hashmap[item_hash_index]) and (obj == self.hashmap[item_bucket_index])
        elif 2 == field_type:
            bucket = self.buckets[item_info_index]
            # for sub_item_info_index in range(len(bucket)):
            for sub_item_info_index in range(0, len(bucket) * 2, 2):
                sub_item_hash_index = sub_item_info_index + 0
                sub_item_obj_index = sub_item_info_index + 1
                if (item_hash == bucket[sub_item_hash_index]) and (obj == bucket[sub_item_obj_index]):
                    return True
            
            return False
        else:
            raise ValueError(f'Unknown SetHashmapFieldTypes field type at {item_info_index=}: {field_type}')

    def __hash__(self):
        return self._hash()

    @property
    def hash_bits(self) -> int:
        return self._hash_bits

    @hash_bits.setter
    def hash_bits(self, value: int) -> None:
        self._hash_bits = value
        self._capacity = 2 ** value
    
    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        if value <= self._capacity:
            return
        
        if value <= 2:
            self.hash_bits = 1
        else:
            self.hash_bits = int(ceil(log2(value)))
    
    def __str__(self) -> str:
        return set(self).__str__()

    def __repr__(self) -> str:
        return set(self).__repr__()

    def _free_mem(self):
        if self._offset is not None:
            for _, bucket in self.buckets.items():
                self._shared_memory.destroy_obj(bucket._offset)
            
            self.buckets.clear()
            if self.hashmap_offset is not None:
                self._shared_memory.destroy_obj(self.hashmap_offset)
                self.hashmap_offset = None

            self._shared_memory.free(self._offset)
            self._offset = None


class ISetIterator:
    def __init__(self, iset: ISet) -> None:
        self._iset = iset
        self._index = 0
        self._sub_index = 0
    
    def __next__(self):
        while self._index < self._iset.capacity:
            item_info_index: int = self._index * 3
            field_type_index = item_info_index + 0
            item_hash_index = item_info_index + 1
            item_bucket_index = item_info_index + 2
            field_type = self._iset.hashmap[field_type_index]
            if 0 == field_type:
                self._index += 1
                continue
            elif 1 == field_type:
                result = self._iset.hashmap[item_bucket_index]
                self._index += 1
                break
            elif 2 == field_type:
                bucket = self._iset.buckets[item_info_index]
                sub_item_info_index = self._sub_index
                sub_item_hash_index = sub_item_info_index * 2 + 0
                sub_item_obj_index = sub_item_info_index * 2 + 1
                if (sub_item_info_index * 2) >= len(bucket):
                    self._sub_index = 0
                    self._index += 1
                    continue

                result = bucket[sub_item_obj_index]
                self._sub_index += 1
                break
            else:
                raise ValueError(f'Unknown SetHashmapFieldTypes field type at {item_info_index=}: {field_type}')
        else:
            raise StopIteration

        return result
    
    def __iter__(self):
        return self


class TSet:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: set) -> Tuple[AbsSet, Offset, Size]:
        obj: ISet = ISet(shared_memory, obj=obj)
        return obj, obj._offset, obj._obj_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> ISet:
        if ObjectType.tset != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError
        
        return ISet(shared_memory, offset)
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.tset != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError
        
        obj: ISet = ISet(shared_memory, offset)
        obj._free_mem()


# ======================================================================================================================
# === MutableSet =============================================================================================================


class MutableSetOffsets(IntEnum):
    size = 0
    capacity = 1
    hashmap_offset = 2
    refresh_counter = 3


class MutableSetHashmapFieldTypes(IntEnum):
    tnone = 0
    tobj = 1
    tbucket = 2


class MutableSetHashmapItemOffsets(IntEnum):
    field_type = 0
    field_hash = 1
    obj_or_bucket = 2


class MutableSetBucketFieldTypes(IntEnum):
    tnone = 0
    tobj = 1


class MutableSetBucketOffsets(IntEnum):
    field_type = 0
    field_hash = 1
    obj = 2


class IMutableSet(BaseIObject, AbsMutableSet):
    def __init__(self, shared_memory: 'SharedMemory', offset: Offset = None, obj: AbsMutableSet = None) -> None:
        self._shared_memory = shared_memory
        self._base_address = shared_memory.base_address
        self._obj_size = None
        self._offset: Offset = None
        self._offset__data: Offset = None
        self._offset__size_offset: Offset = None
        self._offset__capacity_offset: Offset = None
        self._offset__hashmap_offset: Offset = None
        self._offset__refresh_counter_offset: Offset = None
        self._load_factor = 0.75
        self._load_factor_2 = 0.5625
        self._hash_bits: int = None
        self._capacity: int = None
        self._min_capacity: int = None
        self._size: int = None
        self.hashmap: IList = None
        self._refresh_counter: int = 0
        self.hashmap_offset: Offset = None
        self.buckets: Dict[int, IList] = dict()

        self.ignore_rehash: bool = True

        if offset is None:
            if obj is None:
                # obj = frozenset(set())
                data_len = 16
            else:
                data_len = len(obj)

            self._size = 0
            self.hash_bits = 1
            self.capacity = int(ceil(data_len / self._load_factor))
            self._min_capacity = int(ceil(self._capacity * self._load_factor_2))

            offset, self._obj_size = shared_memory.malloc(ObjectType.tmutableset, 32)
            try:
                self._offset = offset
                offset__data = offset + 16
                self._offset__data = offset__data
                self._offset__size_offset: Offset = offset__data + 0
                self._offset__capacity_offset: Offset = offset__data + 8
                self._offset__hashmap_offset = offset__data + 16
                self._offset__refresh_counter_offset = offset__data + 24

                write_uint64(shared_memory.base_address, self._offset__size_offset, self._size)
                write_uint64(shared_memory.base_address, self._offset__capacity_offset, self.capacity)
                write_uint64(shared_memory.base_address, self._offset__refresh_counter_offset, self._refresh_counter)

                self.hashmap, hashmap_offset, _ = shared_memory.put_obj(list())
                self.hashmap = cast(IList, self.hashmap)
                self.hashmap_offset = hashmap_offset
                write_uint64(shared_memory.base_address, self._offset__hashmap_offset, hashmap_offset)
                hashmap_capacity = self.capacity * 3
                self.hashmap.set_capacity(hashmap_capacity)
                self.hashmap.extend_with(hashmap_capacity, 0)
                hash_bits: int = self.hash_bits
                if obj is None:
                    pass
                elif isinstance(obj, IMutableSet):
                    self._move_from(obj)
                else:
                    for item in obj:
                        self.add(item)
                
                self._refresh_counter = read_uint64(shared_memory.base_address, self._offset__refresh_counter_offset)
                
                self.ignore_rehash = False
            except:
                self._free_mem()
                raise
        else:
            self._refresh_hashmap(offset)
            self.ignore_rehash = False

            # self._offset = offset
            # offset__data = offset + 16
            # self._offset__data = offset__data
            # self._offset__size_offset: Offset = offset__data + 0
            # self._offset__capacity_offset: Offset = offset__data + 8
            # self._offset__hashmap_offset = offset__data + 16

            # self._size = read_uint64(shared_memory.base_address, self._offset__size_offset)
            # self.hash_bits = 1
            # self.capacity = read_uint64(shared_memory.base_address, self._offset__capacity_offset)
            # hashmap_offset = read_uint64(shared_memory.base_address, self._offset__hashmap_offset)
            # self._min_capacity = int(ceil(self._capacity * self._load_factor_2))
            
            # self.hashmap_offset = hashmap_offset
            # self.hashmap = IList(shared_memory, hashmap_offset)
            # item_info_index: int = 0
            # # for item_info_index in range(self.capacity):
            # #     field_type_index = item_info_index * 3 + 0
            # #     item_hash_index = item_info_index * 3 + 1
            # #     item_bucket_index = item_info_index * 3 + 2
            # #     field_type = self.hashmap[field_type_index]
            # #     if 0 == field_type:
            # #         continue
            # #     elif 1 == field_type:
            # #         continue
            # #     elif 2 == field_type:
            # #         bucket_offset = self.hashmap[item_bucket_index]
            # #         self.buckets[item_info_index] = IList(shared_memory, bucket_offset)
            # #     else:
            # #         raise ValueError(f'Unknown MutableSetHashmapFieldTypes field type at {item_info_index=}: {field_type}')

            # for item_info_index in range(0, self.capacity * 3, 3):
            #     field_type_index = item_info_index + 0
            #     item_hash_index = item_info_index + 1
            #     item_bucket_index = item_info_index + 2
            #     field_type = self.hashmap[field_type_index]
            #     if 0 == field_type:
            #         continue
            #     elif 1 == field_type:
            #         continue
            #     elif 2 == field_type:
            #         bucket_offset = self.hashmap[item_bucket_index]
            #         self.buckets[item_info_index] = IList(shared_memory, bucket_offset)
            #     else:
            #         raise ValueError(f'Unknown MutableSetHashmapFieldTypes field type at {item_info_index=}: {field_type}')

            # self.ignore_rehash = False

    def _refresh_hashmap(self, offset: Offset):
        # ignore_rehash = self.ignore_rehash
        # self.ignore_rehash = True

        self._hash_bits = None
        self._capacity = None
        self._min_capacity = None
        self._size = None
        self.hashmap = None
        self._refresh_counter = 0
        self.hashmap_offset = None
        self.buckets = dict()

        shared_memory = self._shared_memory
        self._offset = offset
        offset__data = offset + 16
        self._offset__data = offset__data
        self._offset__size_offset: Offset = offset__data + 0
        self._offset__capacity_offset: Offset = offset__data + 8
        self._offset__hashmap_offset = offset__data + 16
        self._offset__refresh_counter_offset = offset__data + 24

        self._refresh_counter = read_uint64(shared_memory.base_address, self._offset__refresh_counter_offset)
        self._size = read_uint64(shared_memory.base_address, self._offset__size_offset)
        self.hash_bits = 1
        self.capacity = read_uint64(shared_memory.base_address, self._offset__capacity_offset)
        hashmap_offset = read_uint64(shared_memory.base_address, self._offset__hashmap_offset)
        self._min_capacity = int(ceil(self._capacity * self._load_factor_2))
        
        self.hashmap_offset = hashmap_offset
        self.hashmap = IList(shared_memory, hashmap_offset)
        item_info_index: int = 0
        # for item_info_index in range(self.capacity):
        #     field_type_index = item_info_index * 3 + 0
        #     item_hash_index = item_info_index * 3 + 1
        #     item_bucket_index = item_info_index * 3 + 2
        #     field_type = self.hashmap[field_type_index]
        #     if 0 == field_type:
        #         continue
        #     elif 1 == field_type:
        #         continue
        #     elif 2 == field_type:
        #         bucket_offset = self.hashmap[item_bucket_index]
        #         self.buckets[item_info_index] = IList(shared_memory, bucket_offset)
        #     else:
        #         raise ValueError(f'Unknown MutableSetHashmapFieldTypes field type at {item_info_index=}: {field_type}')

        for item_info_index in range(0, self.capacity * 3, 3):
            field_type_index = item_info_index + 0
            item_hash_index = item_info_index + 1
            item_bucket_index = item_info_index + 2
            field_type = self.hashmap[field_type_index]
            if 0 == field_type:
                continue
            elif 1 == field_type:
                continue
            elif 2 == field_type:
                bucket_offset = self.hashmap[item_bucket_index]
                self.buckets[item_info_index] = IList(shared_memory, bucket_offset)
            else:
                raise ValueError(f'Unknown MutableSetHashmapFieldTypes field type at {item_info_index=}: {field_type}')

        # self.ignore_rehash = ignore_rehash
    
    @property
    def refresh_counter(self):
        return read_uint64(self._shared_memory.base_address, self._offset__refresh_counter_offset)
    
    def _increase_refresh_counter(self):
        if not self.ignore_rehash:
            self._refresh_counter += 1
            write_uint64(self._shared_memory.base_address, self._offset__refresh_counter_offset, self._refresh_counter)
    
    def _check_hashmap(self):
        if self.ignore_rehash:
            return False
        else:
            base_address = self._shared_memory.base_address
            refresh_counter = read_uint64(base_address, self._offset__refresh_counter_offset)
            # hashmap_offset = read_uint64(base_address, self._offset__hashmap_offset)
            # if (self._refresh_counter != refresh_counter) or (self.hashmap_offset != hashmap_offset) or (self._hashmap._offset != hashmap_offset):
            if self._refresh_counter != refresh_counter:
                self._refresh_hashmap(self._offset)
                return True
            
            return False

    # @property
    # def hashmap(self) -> IList:
    #     if self.ignore_rehash:
    #         return self._hashmap
    #     else:
    #         hashmap_offset = read_uint64(self._shared_memory.base_address, self._offset__hashmap_offset)
    #         if (self.hashmap_offset != hashmap_offset) or (self._hashmap._offset != hashmap_offset):
    #             self._refresh_hashmap(self._offset)
            
    #         return self._hashmap
    
    # @hashmap.setter
    # def hashmap(self, value: IList):
    #     self._hashmap = value

    def _increase_size(self):
        self._size += 1
        write_uint64(self._base_address, self._offset__size_offset, self._size)
        if (self._size > self._capacity) or (self._size < self._min_capacity):
            self._rehash()
    
    def _decrease_size(self):
        self._size -= 1
        if self._size < 0:
            raise RuntimeError('Size of the set is negative')

        write_uint64(self._base_address, self._offset__size_offset, self._size)
        if (self._size > self._capacity) or (self._size < self._min_capacity):
            self._rehash()
    
    def _move_from(self, other: 'IMutableSet'):
        for value_hash, value_type, value_offset in other.iter_offset_pop():
            self.add_as_offset(value_hash, value_type, value_offset)
    
    def _rehash(self):
        if self.ignore_rehash:
            return
        
        self._increase_refresh_counter()

        ignore_rehash = self.ignore_rehash
        self.ignore_rehash = True

        new_other, new_other_offset, new_other_size = self._shared_memory.put_obj(self)
        new_other = cast(IMutableSet, new_other)

        other_capacity = new_other._capacity
        other_hash_bits = new_other._hash_bits
        other_min_capacity = new_other._min_capacity
        other_size = new_other._size
        # other_refresh_counter = new_other._refresh_counter
        other_hashmap = new_other.hashmap
        other_hashmap_offset = new_other.hashmap_offset
        other_buckets = new_other.buckets
        other_hashmap_offset_bin = read_uint64(new_other._shared_memory.base_address, new_other._offset__hashmap_offset)
        other_size_bin = read_uint64(new_other._shared_memory.base_address, new_other._offset__size_offset)
        other_capacity_bin = read_uint64(new_other._shared_memory.base_address, new_other._offset__capacity_offset)
        # other_refresh_counter_bin = read_uint64(new_other._shared_memory.base_address, new_other._offset__refresh_counter_offset)
        
        new_other._capacity = self._capacity
        new_other._hash_bits = self._hash_bits
        new_other._min_capacity = self._min_capacity
        new_other._size = self._size
        # new_other._refresh_counter = self._refresh_counter
        new_other.hashmap = self.hashmap
        new_other.hashmap_offset = self.hashmap_offset
        new_other.buckets = self.buckets
        write_uint64(new_other._shared_memory.base_address, new_other._offset__hashmap_offset, read_uint64(self._shared_memory.base_address, self._offset__hashmap_offset))
        write_uint64(new_other._shared_memory.base_address, new_other._offset__size_offset, read_uint64(self._shared_memory.base_address, self._offset__size_offset))
        write_uint64(new_other._shared_memory.base_address, new_other._offset__capacity_offset, read_uint64(self._shared_memory.base_address, self._offset__capacity_offset))
        # write_uint64(new_other._shared_memory.base_address, new_other._offset__refresh_counter_offset, read_uint64(self._shared_memory.base_address, self._offset__refresh_counter_offset))

        self._capacity = other_capacity
        self._hash_bits = other_hash_bits
        self._min_capacity = other_min_capacity
        self._size = other_size
        # self._refresh_counter = other_refresh_counter
        self.hashmap = other_hashmap
        self.hashmap_offset = other_hashmap_offset
        self.buckets = other_buckets
        write_uint64(self._shared_memory.base_address, self._offset__hashmap_offset, other_hashmap_offset_bin)
        write_uint64(self._shared_memory.base_address, self._offset__size_offset, other_size_bin)
        write_uint64(self._shared_memory.base_address, self._offset__capacity_offset, other_capacity_bin)
        # write_uint64(self._shared_memory.base_address, self._offset__refresh_counter_offset, other_refresh_counter_bin)

        self._shared_memory.destroy_obj(new_other_offset)

        self.ignore_rehash = ignore_rehash

    def __len__(self):
        return self._size
    
    def __iter__(self):
        return IMutableSetIterator(self)
    
    def iter_offset(self):
        return IMutableSetIteratorAsOffset(self)
    
    def iter_offset_pop(self):
        return IMutableSetIteratorAsOffset(self, True)
    
    def __contains__(self, obj: Any) -> bool:
        self._check_hashmap()
        item_hash = hash(obj)
        item_info_index: int = mask_least_significant_bits(item_hash, self.hash_bits) * 3
        field_type_index = item_info_index + 0
        item_hash_index = item_info_index + 1
        item_bucket_index = item_info_index + 2
        field_type = self.hashmap[field_type_index]
        if 0 == field_type:
            return False
        elif 1 == field_type:
            return (item_hash == self.hashmap[item_hash_index]) and (obj == self.hashmap[item_bucket_index])
        elif 2 == field_type:
            bucket_offset = self.hashmap[item_bucket_index]
            try:
                bucket = self.buckets[item_info_index]
                if bucket._offset != bucket_offset:
                    raise KeyError
            except KeyError:
                raise
                self.buckets[item_info_index] = bucket = IList(self._shared_memory, bucket_offset)

            for bucket_item_index in range(0, len(bucket), 3):
                bucket_field_type = bucket[bucket_item_index + 0]
                if 0 == bucket_field_type:
                    continue

                bucket_field_hash = bucket[bucket_item_index + 1]
                bucket_obj = bucket[bucket_item_index + 2]
                if (item_hash == bucket[bucket_field_hash]) and (obj == bucket[bucket_obj]):
                    return True
            
            return False
        else:
            raise ValueError(f'Unknown MutableSetHashmapFieldTypes field type at {item_info_index=}: {field_type}')

    def add(self, value):
        """Add an element."""
        self._check_hashmap()
        item = value
        item_hash = hash(item)
        item_info_index: int = mask_least_significant_bits(item_hash, self.hash_bits) * 3
        field_type_index = item_info_index + 0
        item_hash_index = item_info_index + 1
        item_bucket_index = item_info_index + 2
        field_type = self.hashmap[field_type_index]
        if 0 == field_type:
            self.hashmap[field_type_index] = 1
            self.hashmap[item_hash_index] = item_hash
            self.hashmap[item_bucket_index] = item
            self._increase_size()
            return
        elif 1 == field_type:
            if (item_hash == self.hashmap[item_hash_index]) and (item == self.hashmap[item_bucket_index]):
                return
            
            self._increase_refresh_counter()
            bucket, bucket_offset, _ = self._shared_memory.put_obj(list())
            bucket = cast(IList, bucket)
            bucket.set_capacity(3)
            bucket.extend_with(3, 0)
            self.buckets[item_info_index] = bucket
            bucket[0] = 1
            self.hashmap.move_item_to_list(item_hash_index, bucket, 1)
            self.hashmap.move_item_to_list(item_bucket_index, bucket, 2)
            self.hashmap[field_type_index] = 2
            self.hashmap[item_bucket_index] = bucket_offset
            bucket.append(1)
            bucket.append(item_hash)
            bucket.append(item)
            self._increase_size()
            return
        elif 2 == field_type:
            bucket_offset = self.hashmap[item_bucket_index]
            try:
                bucket = self.buckets[item_info_index]
                if bucket._offset != bucket_offset:
                    raise KeyError
            except KeyError:
                raise
                self.buckets[item_info_index] = bucket = IList(self._shared_memory, bucket_offset)

            bucket_len: int = len(bucket)
            for bucket_item_index in range(0, bucket_len, 3):
                bucket_field_type = bucket[bucket_item_index + 0]
                if 1 == bucket_field_type:
                    if (item_hash == bucket[bucket_item_index + 1]) and (item == bucket[bucket_item_index + 2]):
                        return
            
            for bucket_item_index in range(0, bucket_len, 3):
                bucket_field_type = bucket[bucket_item_index + 0]
                if 0 == bucket_field_type:
                    bucket[bucket_item_index + 0] = 1
                    bucket[bucket_item_index + 1] = item_hash
                    bucket[bucket_item_index + 2] = item
                    self._increase_size()
                    return
            else:
                bucket.append(1)
                bucket.append(item_hash)
                bucket.append(item)
                self._increase_size()
                return
        else:
            raise ValueError(f'Unknown MutableSetHashmapFieldTypes field type at {item_info_index=}: {field_type}')

    def add_as_offset(self, value_hash, value_type, value_offset):
        """Add an element."""
        self._check_hashmap()
        item = (value_type, value_offset)
        item_hash = value_hash
        item_info_index: int = mask_least_significant_bits(item_hash, self.hash_bits) * 3
        field_type_index = item_info_index + 0
        item_hash_index = item_info_index + 1
        item_bucket_index = item_info_index + 2
        field_type = self.hashmap[field_type_index]
        if 0 == field_type:
            self.hashmap[field_type_index] = 1
            self.hashmap[item_hash_index] = item_hash
            self.hashmap.setitem_as_offset(item_bucket_index, item)
            self._increase_size()
            return
        elif 1 == field_type:
            if (item_hash == self.hashmap[item_hash_index]) and (item == self.hashmap.getitem_as_offset(item_bucket_index)):
                return
            
            self._increase_refresh_counter()
            bucket, bucket_offset, _ = self._shared_memory.put_obj(list())
            bucket = cast(IList, bucket)
            bucket.set_capacity(3)
            bucket.extend_with(3, 0)
            self.buckets[item_info_index] = bucket
            bucket[0] = 1
            self.hashmap.move_item_to_list(item_hash_index, bucket, 1)
            self.hashmap.move_item_to_list(item_bucket_index, bucket, 2)
            self.hashmap[field_type_index] = 2
            self.hashmap[item_bucket_index] = bucket_offset
            bucket.append(1)
            bucket.append(item_hash)
            bucket.append_as_offset(item)
            self._increase_size()
            return
        elif 2 == field_type:
            bucket_offset = self.hashmap[item_bucket_index]
            try:
                bucket = self.buckets[item_info_index]
                if bucket._offset != bucket_offset:
                    raise KeyError
            except KeyError:
                raise
                self.buckets[item_info_index] = bucket = IList(self._shared_memory, bucket_offset)

            bucket_len: int = len(bucket)
            for bucket_item_index in range(0, bucket_len, 3):
                bucket_field_type = bucket[bucket_item_index + 0]
                if 1 == bucket_field_type:
                    if (item_hash == bucket[bucket_item_index + 1]) and (item == bucket.getitem_as_offset(bucket_item_index + 2)):
                        return
            
            for bucket_item_index in range(0, bucket_len, 3):
                bucket_field_type = bucket[bucket_item_index + 0]
                if 0 == bucket_field_type:
                    bucket[bucket_item_index + 0] = 1
                    bucket[bucket_item_index + 1] = item_hash
                    bucket.setitem_as_offset(bucket_item_index + 2, item)
                    self._increase_size()
                    return
            else:
                bucket.append(1)
                bucket.append(item_hash)
                bucket.append_as_offset(item)
                self._increase_size()
                return
        else:
            raise ValueError(f'Unknown MutableSetHashmapFieldTypes field type at {item_info_index=}: {field_type}')

    def discard(self, value):
        """Remove an element.  Do not raise an exception if absent."""
        self._check_hashmap()
        obj = value
        item_hash = hash(obj)
        item_info_index: int = mask_least_significant_bits(item_hash, self.hash_bits) * 3
        field_type_index = item_info_index + 0
        item_hash_index = item_info_index + 1
        item_bucket_index = item_info_index + 2
        field_type = self.hashmap[field_type_index]
        if 0 == field_type:
            return
        elif 1 == field_type:
            if (item_hash == self.hashmap[item_hash_index]) and (obj == self.hashmap[item_bucket_index]):
                self.hashmap[field_type_index] = 0
                self.hashmap[item_hash_index] = None
                self.hashmap[item_bucket_index] = None
                self._decrease_size()
                return
            else:
                return
        elif 2 == field_type:
            bucket_offset = self.hashmap[item_bucket_index]
            try:
                bucket = self.buckets[item_info_index]
                if bucket._offset != bucket_offset:
                    raise KeyError
            except KeyError:
                raise
                self.buckets[item_info_index] = bucket = IList(self._shared_memory, bucket_offset)

            for bucket_item_index in range(0, len(bucket), 3):
                bucket_field_type = bucket[bucket_item_index + 0]
                if 0 == bucket_field_type:
                    continue
                
                bucket_field_hash = bucket[bucket_item_index + 1]
                bucket_obj = bucket[bucket_item_index + 2]
                if (item_hash == bucket[bucket_field_hash]) and (obj == bucket[bucket_obj]):
                    bucket[bucket_item_index + 0] = 0
                    bucket[bucket_item_index + 1] = None
                    bucket[bucket_item_index + 2] = None
                    self._decrease_size()
                    return
            return
        else:
            raise ValueError(f'Unknown MutableSetHashmapFieldTypes field type at {item_info_index=}: {field_type}')

    @property
    def hash_bits(self) -> int:
        return self._hash_bits

    @hash_bits.setter
    def hash_bits(self, value: int) -> None:
        self._hash_bits = value
        self._capacity = 2 ** value
    
    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        if value <= self._capacity:
            return
        
        if value <= 2:
            self.hash_bits = 1
        else:
            self.hash_bits = int(ceil(log2(value)))
    
    def __str__(self) -> str:
        return set(self).__str__()

    def __repr__(self) -> str:
        return set(self).__repr__()

    def _free_mem(self):
        if self._offset is not None:
            for _, bucket in self.buckets.items():
                self._shared_memory.destroy_obj(bucket._offset)
            
            self.buckets.clear()
            if self.hashmap_offset is not None:
                self._shared_memory.destroy_obj(self.hashmap_offset)
                self.hashmap_offset = None
            
            self._shared_memory.free(self._offset)
            self._offset = None


class IMutableSetIterator:
    def __init__(self, iset: IMutableSet) -> None:
        self._iset = iset
        self._index = 0
        self._sub_index = 0
    
    def __next__(self):
        if self._iset._check_hashmap():
            raise RuntimeError("Sets's hashmap changed during iteration")

        while self._index < self._iset.capacity:
            item_info_index: int = self._index * 3
            field_type_index = item_info_index + 0
            item_hash_index = item_info_index + 1
            item_bucket_index = item_info_index + 2
            field_type = self._iset.hashmap[field_type_index]
            if 0 == field_type:
                self._index += 1
                continue
            elif 1 == field_type:
                result = self._iset.hashmap[item_bucket_index]
                self._index += 1
                return result
            elif 2 == field_type:
                bucket_offset = self._iset.hashmap[item_bucket_index]
                try:
                    bucket = self._iset.buckets[item_info_index]
                    if bucket._offset != bucket_offset:
                        raise KeyError
                except KeyError:
                    raise
                    self._iset.buckets[item_info_index] = bucket = IList(self._iset._shared_memory, bucket_offset)

                bucket_len = len(bucket)
                sub_item_info_index = self._sub_index
                while (sub_item_info_index * 3) < bucket_len:
                    sub_item_field_type_index = sub_item_info_index * 3 + 0
                    if bucket[sub_item_field_type_index] == 0:
                        sub_item_info_index += 1
                        continue

                    sub_item_hash_index = sub_item_info_index * 3 + 1
                    sub_item_obj_index = sub_item_info_index * 3 + 2
                    result = bucket[sub_item_obj_index]
                    self._sub_index += 1
                    return result
                else:
                    self._sub_index = 0
                    self._index += 1
                    continue
            else:
                raise ValueError(f'Unknown MutableSetHashmapFieldTypes field type at {item_info_index=}: {field_type}')
        else:
            raise StopIteration
    
    def __iter__(self):
        return self


class IMutableSetIteratorAsOffset:
    def __init__(self, iset: IMutableSet, pop: bool = False) -> None:
        self._iset = iset
        self._pop: bool = pop
        self._index = 0
        self._sub_index = 0
    
    def __next__(self):
        if self._iset._check_hashmap():
            raise RuntimeError("Set's hashmap changed during iteration")

        if self._index < self._iset.capacity:
            while self._index < self._iset.capacity:
                item_info_index: int = self._index * 3
                field_type_index = item_info_index + 0
                item_hash_index = item_info_index + 1
                item_bucket_index = item_info_index + 2
                field_type = self._iset.hashmap[field_type_index]
                if 0 == field_type:
                    self._index += 1
                    continue
                elif 1 == field_type:
                    item_hash = self._iset.hashmap[item_hash_index]
                    value_type, value_offset = self._iset.hashmap.getitem_as_offset(item_bucket_index)
                    if self._pop:
                        self._iset.hashmap[field_type_index] = 0
                        self._iset.hashmap[item_hash_index] = None
                        self._iset.hashmap.setitem_as_offset(item_bucket_index, (0, 0), False)
                    
                    self._index += 1
                    return (item_hash, value_type, value_offset)
                elif 2 == field_type:
                    bucket_offset = self._iset.hashmap[item_bucket_index]
                    try:
                        bucket = self._iset.buckets[item_info_index]
                        if bucket._offset != bucket_offset:
                            raise KeyError
                    except KeyError:
                        raise
                        self._iset.buckets[item_info_index] = bucket = IList(self._iset._shared_memory, bucket_offset)

                    bucket_len = len(bucket)
                    sub_item_info_index = self._sub_index
                    while (sub_item_info_index * 3) < bucket_len:
                        sub_item_field_type_index = sub_item_info_index * 3 + 0
                        if bucket[sub_item_field_type_index] == 0:
                            sub_item_info_index += 1
                            continue

                        sub_item_hash_index = sub_item_info_index * 3 + 1
                        sub_item_obj_index = sub_item_info_index * 3 + 2
                        sub_item_hash = bucket[sub_item_hash_index]
                        sub_item_value_type, sub_item_value_offset = bucket.getitem_as_offset(sub_item_obj_index)
                        if self._pop:
                            bucket[sub_item_field_type_index] = 0
                            bucket[sub_item_hash_index] = None
                            bucket.setitem_as_offset(sub_item_obj_index, (0, 0), False)
                        
                        self._sub_index += 1
                        return (sub_item_hash, sub_item_value_type, sub_item_value_offset)
                    else:
                        self._sub_index = 0
                        self._index += 1
                        continue
                else:
                    raise ValueError(f'Unknown MutableSetHashmapFieldTypes field type at {item_info_index=}: {field_type}')
            else:
                raise StopIteration
        else:
            raise StopIteration
    
    def __iter__(self):
        return self


class TMutableSet:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: set) -> Tuple[IMutableSet, Offset, Size]:
        obj: IMutableSet = IMutableSet(shared_memory, obj=obj)
        return obj, obj._offset, obj._obj_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> IMutableSet:
        if ObjectType.tmutableset != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError
        
        return IMutableSet(shared_memory, offset)
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.tmutableset != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError
        
        obj: IMutableSet = IMutableSet(shared_memory, offset)
        obj._free_mem()


# ======================================================================================================================
# === Mapping =============================================================================================================


class ForceMapping(dict):
    ...


FMapping = ForceMapping
forcemapping = ForceMapping
fmapping = ForceMapping


class MappingOffsets(IntEnum):
    size = 0
    capacity = 1
    hashmap_offset = 2


class MappingHashmapFieldTypes(IntEnum):
    tnone = 0
    tobj = 1
    tbucket = 2


class MappingHashmapItemOffsets(IntEnum):
    field_type = 0
    field_hash = 1
    key_or_bucket = 2
    value_or_none = 3


class MappingBucketOffsets(IntEnum):
    field_hash = 0
    key_obj = 1
    value_obj = 2


class IMapping(BaseIObject, AbsMapping):
    def __init__(self, shared_memory: 'SharedMemory', offset: Offset = None, obj: AbsMapping = None) -> None:
        self._shared_memory = shared_memory
        self._base_address = shared_memory.base_address
        self._obj_size = None
        self._offset: Offset = None
        self._offset__data: Offset = None
        self._offset__size_offset: Offset = None
        self._offset__capacity_offset: Offset = None
        self._offset__hashmap_offset: Offset = None
        self._load_factor = 0.75
        self._hash_bits: int = None
        self._capacity: int = None
        self._size: int = None
        self.hashmap: IList = None
        self.hashmap_offset: Offset = None
        self.buckets: Dict[int, IList] = dict()

        if offset is None:
            if obj is None:
                # obj = frozenset(set())
                data_len = 16
            else:
                data_len = len(obj)

            self._size: int = data_len
            self.hash_bits = 1
            self.capacity = int(ceil(data_len / self._load_factor))

            offset, self._obj_size = shared_memory.malloc(ObjectType.tmapping, 24)
            try:
                self._offset = offset
                offset__data = offset + 16
                self._offset__data = offset__data
                self._offset__size_offset: Offset = offset__data + 0
                self._offset__capacity_offset: Offset = offset__data + 8
                self._offset__hashmap_offset = offset__data + 16

                write_uint64(shared_memory.base_address, self._offset__size_offset, self._size)
                write_uint64(shared_memory.base_address, self._offset__capacity_offset, self.capacity)

                self.hashmap, hashmap_offset, _ = shared_memory.put_obj(list())
                self.hashmap = cast(IList, self.hashmap)
                self.hashmap_offset = hashmap_offset
                write_uint64(shared_memory.base_address, self._offset__hashmap_offset, hashmap_offset)
                hashmap_capacity = self.capacity * 4
                self.hashmap.set_capacity(hashmap_capacity)
                self.hashmap.extend_with(hashmap_capacity, 0)
                hash_bits: int = self.hash_bits
                if obj is not None:
                    for key, value in obj.items():
                        key_hash = hash(key)
                        item_info_index: int = mask_least_significant_bits(key_hash, hash_bits) * 4
                        field_type_index = item_info_index + 0
                        item_hash_index = item_info_index + 1
                        item_bucket_index = item_info_index + 2
                        item_value_index = item_info_index + 3
                        field_type = self.hashmap[field_type_index]
                        if 0 == field_type:
                            self.hashmap[field_type_index] = 1
                            self.hashmap[item_hash_index] = key_hash
                            self.hashmap[item_bucket_index] = key
                            self.hashmap[item_value_index] = value
                        elif 1 == field_type:
                            bucket, bucket_offset, _ = shared_memory.put_obj(list())
                            bucket = cast(IList, bucket)
                            bucket.set_capacity(3)
                            bucket.extend_with(3, 0)
                            self.buckets[item_info_index] = bucket
                            self.hashmap.move_item_to_list(item_hash_index, bucket, 0)
                            self.hashmap.move_item_to_list(item_bucket_index, bucket, 1)
                            self.hashmap.move_item_to_list(item_value_index, bucket, 2)
                            self.hashmap[field_type_index] = 2
                            self.hashmap[item_bucket_index] = bucket_offset
                            bucket.append(key_hash)
                            bucket.append(key)
                            bucket.append(value)
                        elif 2 == field_type:
                            bucket = self.buckets[item_info_index]
                            bucket.append(key_hash)
                            bucket.append(key)
                            bucket.append(value)
                        else:
                            raise ValueError(f'Unknown MappingHashmapFieldTypes field type at {item_info_index=}: {field_type}')

                # print(f'Constructed {self.hashmap=}')
                # print(f'\tConstructed buckets:')
                # pdi(self.buckets)
                # for bucket_index, bucket in self.buckets.items():
                #     pdi(bucket)
                #     print(f'\t\t{bucket_index}:', bucket)
            except:
                self._free_mem()
                raise
        else:
            self._offset = offset
            offset__data = offset + 16
            self._offset__data = offset__data
            self._offset__size_offset: Offset = offset__data + 0
            self._offset__capacity_offset: Offset = offset__data + 8
            self._offset__hashmap_offset = offset__data + 16

            self._size = read_uint64(shared_memory.base_address, self._offset__size_offset)
            self.hash_bits = 1
            self.capacity = read_uint64(shared_memory.base_address, self._offset__capacity_offset)
            hashmap_offset = read_uint64(shared_memory.base_address, self._offset__hashmap_offset)
            
            self.hashmap_offset = hashmap_offset
            self.hashmap = IList(shared_memory, hashmap_offset)
            # print(f'Adopted by {type(self)}: {self.hashmap=}')
            item_info_index: int = 0
            # for item_info_index in range(self.capacity):
            #     field_type_index = item_info_index * 4 + 0
            #     item_hash_index = item_info_index * 4 + 1
            #     item_bucket_index = item_info_index * 4 + 2
            #     item_value_index = item_info_index * 4 + 3
            #     field_type = self.hashmap[field_type_index]
            #     if 0 == field_type:
            #         continue
            #     elif 1 == field_type:
            #         continue
            #     elif 2 == field_type:
            #         bucket_offset = self.hashmap[item_bucket_index]
            #         self.buckets[item_info_index] = IList(shared_memory, bucket_offset)
            #     else:
            #         raise ValueError(f'Unknown MappingHashmapFieldTypes field type at {item_info_index=}: {field_type}')

            for item_info_index in range(0, self.capacity * 4, 4):
                field_type_index = item_info_index + 0
                item_hash_index = item_info_index + 1
                item_bucket_index = item_info_index + 2
                item_value_index = item_info_index + 3
                field_type = self.hashmap[field_type_index]
                if 0 == field_type:
                    continue
                elif 1 == field_type:
                    continue
                elif 2 == field_type:
                    bucket_offset = self.hashmap[item_bucket_index]
                    self.buckets[item_info_index] = IList(shared_memory, bucket_offset)
                else:
                    raise ValueError(f'Unknown MappingHashmapFieldTypes field type at {item_info_index=}: {field_type}')

            # print(f'\tAdopted buckets:')
            # pdi(self.buckets)
            # for bucket_index, bucket in self.buckets.items():
            #     pdi(bucket)
            #     print(f'\t\t{bucket_index}:', bucket)

    def __len__(self):
        return self._size
    
    def __iter__(self):
        return IMappingIterator(self)
    
    # def __contains__(self, obj: Hashable) -> bool:
    #     item_hash = hash(obj)
    #     item_info_index: int = mask_least_significant_bits(item_hash, self.hash_bits)
    #     field_type_index = item_info_index * 4 + 0
    #     item_hash_index = item_info_index * 4 + 1
    #     item_bucket_index = item_info_index * 4 + 2
    #     item_value_index = item_info_index * 4 + 3
    #     field_type = self.hashmap[field_type_index]
    #     if 0 == field_type:
    #         return False
    #     elif 1 == field_type:
    #         return (item_hash == self.hashmap[item_hash_index]) and (obj == self.hashmap[item_bucket_index])
    #     elif 2 == field_type:
    #         bucket = self.buckets[item_info_index]
    #         # for sub_item_info_index in range(len(bucket)):
    #         for sub_item_info_index in range(0, len(bucket) * 3, 3):
    #             sub_item_hash_index = sub_item_info_index + 0
    #             sub_item_key_obj_index = sub_item_info_index + 1
    #             sub_item_value_obj_index = sub_item_info_index + 2
    #             if (item_hash == bucket[sub_item_hash_index]) and (obj == bucket[sub_item_key_obj_index]):
    #                 return True
            
    #         return False
    #     else:
    #         raise ValueError(f'Unknown MappingHashmapFieldTypes field type at {item_info_index=}: {field_type}')

    def __getitem__(self, key: Hashable):
        item_hash = hash(key)
        item_info_index: int = mask_least_significant_bits(item_hash, self.hash_bits) * 4
        field_type_index = item_info_index + 0
        item_hash_index = item_info_index + 1
        item_bucket_index = item_info_index + 2
        item_value_index = item_info_index + 3
        field_type = self.hashmap[field_type_index]
        if 0 == field_type:
            raise KeyError
        elif 1 == field_type:
            if (item_hash == self.hashmap[item_hash_index]) and (key == self.hashmap[item_bucket_index]):
                return self.hashmap[item_value_index]
            else:
                raise KeyError
        elif 2 == field_type:
            bucket = self.buckets[item_info_index]
            # for sub_item_info_index in range(len(bucket)):
            for sub_item_info_index in range(0, len(bucket) * 3, 3):
                sub_item_hash_index = sub_item_info_index + 0
                sub_item_key_obj_index = sub_item_info_index + 1
                sub_item_value_obj_index = sub_item_info_index + 2
                if (item_hash == bucket[sub_item_hash_index]) and (key == bucket[sub_item_key_obj_index]):
                    return bucket[sub_item_value_obj_index]
            
            raise KeyError
        else:
            raise ValueError(f'Unknown MappingHashmapFieldTypes field type at {item_info_index=}: {field_type}')

    @property
    def hash_bits(self) -> int:
        return self._hash_bits

    @hash_bits.setter
    def hash_bits(self, value: int) -> None:
        self._hash_bits = value
        self._capacity = 2 ** value
    
    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        if value <= self._capacity:
            return
        
        if value <= 2:
            self.hash_bits = 1
        else:
            self.hash_bits = int(ceil(log2(value)))
    
    def __str__(self) -> str:
        return dict(self).__str__()

    def __repr__(self) -> str:
        return dict(self).__repr__()

    def _free_mem(self):
        if self._offset is not None:
            for _, bucket in self.buckets.items():
                self._shared_memory.destroy_obj(bucket._offset)
            
            self.buckets.clear()
            if self.hashmap_offset is not None:
                self._shared_memory.destroy_obj(self.hashmap_offset)
                self.hashmap_offset = None
            
            self._shared_memory.free(self._offset)
            self._offset = None


class IMappingIterator:
    def __init__(self, imapping: IMapping) -> None:
        self._imapping = imapping
        self._index = 0
        self._sub_index = 0
    
    def __next__(self):
        while self._index < self._imapping.capacity:
            item_info_index: int = self._index * 4
            field_type_index = item_info_index + 0
            item_hash_index = item_info_index + 1
            item_bucket_index = item_info_index + 2
            item_value_index = item_info_index + 3
            field_type = self._imapping.hashmap[field_type_index]
            if 0 == field_type:
                self._index += 1
                continue
            elif 1 == field_type:
                result = self._imapping.hashmap[item_bucket_index]
                self._index += 1
                break
            elif 2 == field_type:
                bucket = self._imapping.buckets[item_info_index]
                sub_item_info_index = self._sub_index
                sub_item_hash_index = sub_item_info_index * 3 + 0
                sub_item_key_obj_index = sub_item_info_index * 3 + 1
                sub_item_value_obj_index = sub_item_info_index * 3 + 2
                if (sub_item_info_index * 3) >= len(bucket):
                    self._sub_index = 0
                    self._index += 1
                    continue

                result = bucket[sub_item_key_obj_index]
                self._sub_index += 1
                break
            else:
                raise ValueError(f'Unknown MappingHashmapFieldTypes field type at {item_info_index=}: {field_type}')
        else:
            raise StopIteration

        return result
    
    def __iter__(self):
        return self


class TMapping:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: AbsMapping) -> Tuple[IMapping, Offset, Size]:
        obj: IMapping = IMapping(shared_memory, obj=obj)
        return obj, obj._offset, obj._obj_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> IMapping:
        if ObjectType.tmapping != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError
        
        return IMapping(shared_memory, offset)
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.tmapping != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError
        
        obj: IMapping = IMapping(shared_memory, offset)
        obj._free_mem()


# ======================================================================================================================
# === MutableMapping =============================================================================================================


class MutableMappingOffsets(IntEnum):
    size = 0
    capacity = 1
    hashmap_offset = 2
    refresh_counter = 3


class MutableMappingHashmapFieldTypes(IntEnum):
    tnone = 0
    tobj = 1
    tbucket = 2


class MutableMappingHashmapItemOffsets(IntEnum):
    field_type = 0
    field_hash = 1
    key_or_bucket = 2
    value_or_none = 3


class MutableMappingBucketFieldTypes(IntEnum):
    tnone = 0
    tobj = 1


class MutableMappingBucketOffsets(IntEnum):
    field_type = 0
    field_hash = 1
    key_obj = 2
    value_obj = 3


class IMutableMapping(BaseIObject, AbsMutableMapping):
    @property
    def __mro__(self) -> Tuple:
        return BaseIObject, AbsMutableMapping, dict

    def __init__(self, shared_memory: 'SharedMemory', offset: Offset = None, obj: AbsMutableMapping = None) -> None:
        self._shared_memory = shared_memory
        self._base_address = shared_memory.base_address
        self._obj_size = None
        self._offset: Offset = None
        self._offset__data: Offset = None
        self._offset__size_offset: Offset = None
        self._offset__capacity_offset: Offset = None
        self._offset__hashmap_offset: Offset = None
        self._offset__refresh_counter_offset: Offset = None
        self._load_factor = 0.75
        self._load_factor_2 = 0.5625
        self._hash_bits: int = None
        self._capacity: int = None
        self._min_capacity: int = None
        self._size: int = None
        self.hashmap: IList = None
        self._refresh_counter: int = 0
        self.hashmap_offset: Offset = None
        self.buckets: Dict[int, IList] = dict()

        self.ignore_rehash: bool = True

        if offset is None:
            if obj is None:
                # obj = frozenset(set())
                data_len = 16
            else:
                data_len = len(obj)

            self._size: int = 0
            self.hash_bits = 1
            self.capacity = int(ceil(data_len / self._load_factor))
            self._min_capacity = int(ceil(self._capacity * self._load_factor_2))

            offset, self._obj_size = shared_memory.malloc(ObjectType.tmutablemapping, 32)
            created_items_offsets: List[Offset] = list()
            try:
                self._offset = offset
                offset__data = offset + 16
                self._offset__data = offset__data
                self._offset__size_offset = offset__data + 0
                self._offset__capacity_offset = offset__data + 8
                self._offset__hashmap_offset = offset__data + 16
                self._offset__refresh_counter_offset = offset__data + 24

                write_uint64(shared_memory.base_address, self._offset__size_offset, self._size)
                write_uint64(shared_memory.base_address, self._offset__capacity_offset, self.capacity)
                write_uint64(shared_memory.base_address, self._offset__refresh_counter_offset, self._refresh_counter)

                self.hashmap, hashmap_offset, _ = shared_memory.put_obj(list())
                self.hashmap = cast(IList, self.hashmap)
                self.hashmap_offset = hashmap_offset
                write_uint64(shared_memory.base_address, self._offset__hashmap_offset, hashmap_offset)
                hashmap_capacity = self.capacity * 4
                self.hashmap.set_capacity(hashmap_capacity)
                self.hashmap.extend_with(hashmap_capacity, 0)
                hash_bits: int = self.hash_bits
                if obj is None:
                    pass
                elif isinstance(obj, IMutableMapping):
                    self._move_from(obj)
                else:
                    for key, value in obj.items():
                        self.__setitem__(key, value)
                
                self._refresh_counter = read_uint64(shared_memory.base_address, self._offset__refresh_counter_offset)

                self.ignore_rehash = False

                # print(f'Constructed {self.hashmap=}')
                # print(f'\tConstructed buckets:')
                # pdi(self.buckets)
                # for bucket_index, bucket in self.buckets.items():
                #     pdi(bucket)
                #     print(f'\t\t{bucket_index}:', bucket)
            except:
                self._free_mem()
                raise
        else:
            self._refresh_hashmap(offset)
            self.ignore_rehash = False

            # self._offset = offset
            # offset__data = offset + 16
            # self._offset__data = offset__data
            # self._offset__size_offset: Offset = offset__data + 0
            # self._offset__capacity_offset: Offset = offset__data + 8
            # self._offset__hashmap_offset = offset__data + 16

            # self._size = read_uint64(shared_memory.base_address, self._offset__size_offset)
            # self.hash_bits = 1
            # self.capacity = read_uint64(shared_memory.base_address, self._offset__capacity_offset)
            # hashmap_offset = read_uint64(shared_memory.base_address, self._offset__hashmap_offset)
            # self._min_capacity = int(ceil(self._capacity * self._load_factor_2))
            
            # self.hashmap_offset = hashmap_offset
            # self.hashmap = IList(shared_memory, hashmap_offset)
            # # print(f'Adopted by {type(self)}: {self.hashmap=}')
            # item_info_index: int = 0
            # # for item_info_index in range(self.capacity):
            # #     field_type_index = item_info_index * 4 + 0
            # #     item_hash_index = item_info_index * 4 + 1
            # #     item_bucket_index = item_info_index * 4 + 2
            # #     item_value_index = item_info_index * 4 + 3
            # #     field_type = self.hashmap[field_type_index]
            # #     if 0 == field_type:
            # #         continue
            # #     elif 1 == field_type:
            # #         continue
            # #     elif 2 == field_type:
            # #         bucket_offset = self.hashmap[item_bucket_index]
            # #         self.buckets[item_info_index] = IList(shared_memory, bucket_offset)
            # #     else:
            # #         raise ValueError(f'Unknown MutableMappingHashmapFieldTypes field type at {item_info_index=}: {field_type}')
            
            # for item_info_index in range(0, self.capacity * 4, 4):
            #     field_type_index = item_info_index + 0
            #     item_hash_index = item_info_index + 1
            #     item_bucket_index = item_info_index + 2
            #     item_value_index = item_info_index + 3
            #     field_type = self.hashmap[field_type_index]
            #     if 0 == field_type:
            #         continue
            #     elif 1 == field_type:
            #         continue
            #     elif 2 == field_type:
            #         bucket_offset = self.hashmap[item_bucket_index]
            #         self.buckets[item_info_index] = IList(shared_memory, bucket_offset)
            #     else:
            #         raise ValueError(f'Unknown MutableMappingHashmapFieldTypes field type at {item_info_index=}: {field_type}')

            # self.ignore_rehash = False
            
            # # print(f'\tAdopted by {type(self)} buckets:')
            # # pdi(self.buckets)
            # # for bucket_index, bucket in self.buckets.items():
            # #     pdi(bucket)
            # #     print(f'\t\t{bucket_index}:', bucket)

    def _refresh_hashmap(self, offset: Offset):
        # print(f'~ refresh_hashmap {offset}: {intro_func_repr_limited()}')

        # ignore_rehash = self.ignore_rehash
        # self.ignore_rehash = True

        self._hash_bits = None
        self._capacity = None
        self._min_capacity = None
        self._size = None
        self.hashmap = None
        self._refresh_counter = 0
        self.hashmap_offset = None
        self.buckets = dict()

        shared_memory = self._shared_memory
        self._offset = offset
        offset__data = offset + 16
        self._offset__data = offset__data
        self._offset__size_offset: Offset = offset__data + 0
        self._offset__capacity_offset: Offset = offset__data + 8
        self._offset__hashmap_offset = offset__data + 16
        self._offset__refresh_counter_offset = offset__data + 24

        self._refresh_counter = read_uint64(shared_memory.base_address, self._offset__refresh_counter_offset)
        self._size = read_uint64(shared_memory.base_address, self._offset__size_offset)
        self.hash_bits = 1
        self.capacity = read_uint64(shared_memory.base_address, self._offset__capacity_offset)
        hashmap_offset = read_uint64(shared_memory.base_address, self._offset__hashmap_offset)
        self._min_capacity = int(ceil(self._capacity * self._load_factor_2))
        
        self.hashmap_offset = hashmap_offset
        self.hashmap = IList(shared_memory, hashmap_offset)
        # print(f'Adopted by {type(self)}: {self.hashmap=}')
        # item_info_index: int = 0
        # for item_info_index in range(self.capacity):
        #     field_type_index = item_info_index * 4 + 0
        #     item_hash_index = item_info_index * 4 + 1
        #     item_bucket_index = item_info_index * 4 + 2
        #     item_value_index = item_info_index * 4 + 3
        #     field_type = self.hashmap[field_type_index]
        #     if 0 == field_type:
        #         continue
        #     elif 1 == field_type:
        #         continue
        #     elif 2 == field_type:
        #         bucket_offset = self.hashmap[item_bucket_index]
        #         self.buckets[item_info_index] = IList(shared_memory, bucket_offset)
        #     else:
        #         raise ValueError(f'Unknown MutableMappingHashmapFieldTypes field type at {item_info_index=}: {field_type}')
        
        for item_info_index in range(0, self.capacity * 4, 4):
            field_type_index = item_info_index + 0
            item_hash_index = item_info_index + 1
            item_bucket_index = item_info_index + 2
            item_value_index = item_info_index + 3
            field_type = self.hashmap[field_type_index]
            if 0 == field_type:
                continue
            elif 1 == field_type:
                continue
            elif 2 == field_type:
                bucket_offset = self.hashmap[item_bucket_index]
                self.buckets[item_info_index] = IList(shared_memory, bucket_offset)
            else:
                raise ValueError(f'Unknown MutableMappingHashmapFieldTypes field type at {item_info_index=}: {field_type}')

        # self.ignore_rehash = ignore_rehash
    
    @property
    def refresh_counter(self):
        return read_uint64(self._shared_memory.base_address, self._offset__refresh_counter_offset)
    
    def _increase_refresh_counter(self):
        if self.ignore_rehash:
            # print(f'~ ignore increase_refresh_counter {self._offset}: {intro_func_repr_limited()}')
            pass
        else:
            # print(f'~ increase_refresh_counter {self._offset}: {intro_func_repr_limited()}')
            # refresh_counter = read_uint64(self._shared_memory.base_address, self._offset__refresh_counter_offset)
            # if self._refresh_counter != refresh_counter:
            #     print('~!!! increase_refresh_counter')
            
            self._refresh_counter += 1
            write_uint64(self._shared_memory.base_address, self._offset__refresh_counter_offset, self._refresh_counter)
    
    def _check_hashmap(self):
        if self.ignore_rehash:
            # print(f'~ ignore check_hashmap {self._offset}: {intro_func_repr_limited()}')
            return False
        else:
            base_address = self._shared_memory.base_address
            refresh_counter = read_uint64(base_address, self._offset__refresh_counter_offset)
            # hashmap_offset = read_uint64(base_address, self._offset__hashmap_offset)
            # if (self._refresh_counter != refresh_counter) or (self.hashmap_offset != hashmap_offset) or (self._hashmap._offset != hashmap_offset):
            if self._refresh_counter != refresh_counter:
                # print(f'~ check_hashmap {self._offset}: {intro_func_repr_limited()}')
                self._refresh_hashmap(self._offset)
                return True
            
            return False

    # @property
    # def hashmap(self) -> IList:
    #     if self.ignore_rehash:
    #         return self._hashmap
    #     else:
    #         self._check_hashmap()
    #         return self._hashmap
    
    # @hashmap.setter
    # def hashmap(self, value: IList):
    #     self._hashmap = value

    def _increase_size(self):
        self._size += 1
        write_uint64(self._base_address, self._offset__size_offset, self._size)
        if (self._size > self._capacity) or (self._size < self._min_capacity):
            self._rehash()
    
    def _decrease_size(self):
        self._size -= 1
        if self._size < 0:
            raise RuntimeError('Size of the set is negative')

        write_uint64(self._base_address, self._offset__size_offset, self._size)
        if (self._size > self._capacity) or (self._size < self._min_capacity):
            self._rehash()
    
    def _move_from(self, other: 'IMutableMapping'):
        for key_hash, key_type, key_offset, value_type, value_offset in other.iter_offset_pop():
            self.setitem_as_offset(key_hash, key_type, key_offset, value_type, value_offset)
    
    def _rehash(self):
        if self.ignore_rehash:
            # print(f'~ ignore rehash {self._offset}: {intro_func_repr_limited()}')
            return 
        
        # print(f'~ rehash {self._offset}: {intro_func_repr_limited()}')
        self._increase_refresh_counter()

        ignore_rehash = self.ignore_rehash
        self.ignore_rehash = True

        new_other, new_other_offset, new_other_size = self._shared_memory.put_obj(self)
        new_other = cast(IMutableMapping, new_other)

        other_capacity = new_other._capacity
        other_hash_bits = new_other._hash_bits
        other_min_capacity = new_other._min_capacity
        other_size = new_other._size
        # refresh_counter = new_other._refresh_counter
        other_hashmap = new_other.hashmap
        other_hashmap_offset = new_other.hashmap_offset
        other_buckets = new_other.buckets
        other_hashmap_offset_bin = read_uint64(new_other._shared_memory.base_address, new_other._offset__hashmap_offset)
        other_size_bin = read_uint64(new_other._shared_memory.base_address, new_other._offset__size_offset)
        other_capacity_bin = read_uint64(new_other._shared_memory.base_address, new_other._offset__capacity_offset)
        # refresh_counter_bin = read_uint64(new_other._shared_memory.base_address, new_other._offset__refresh_counter_offset)
        
        new_other._capacity = self._capacity
        new_other._hash_bits = self._hash_bits
        new_other._min_capacity = self._min_capacity
        new_other._size = self._size
        # new_other._refresh_counter = self._refresh_counter
        new_other.hashmap = self.hashmap
        new_other.hashmap_offset = self.hashmap_offset
        new_other.buckets = self.buckets
        write_uint64(new_other._shared_memory.base_address, new_other._offset__hashmap_offset, read_uint64(self._shared_memory.base_address, self._offset__hashmap_offset))
        write_uint64(new_other._shared_memory.base_address, new_other._offset__size_offset, read_uint64(self._shared_memory.base_address, self._offset__size_offset))
        write_uint64(new_other._shared_memory.base_address, new_other._offset__capacity_offset, read_uint64(self._shared_memory.base_address, self._offset__capacity_offset))
        # write_uint64(new_other._shared_memory.base_address, new_other._offset__refresh_counter_offset, read_uint64(self._shared_memory.base_address, self._offset__refresh_counter_offset))

        self._capacity = other_capacity
        self._hash_bits = other_hash_bits
        self._min_capacity = other_min_capacity
        self._size = other_size
        # self._refresh_counter = refresh_counter
        self.hashmap = other_hashmap
        self.hashmap_offset = other_hashmap_offset
        self.buckets = other_buckets
        write_uint64(self._shared_memory.base_address, self._offset__hashmap_offset, other_hashmap_offset_bin)
        write_uint64(self._shared_memory.base_address, self._offset__size_offset, other_size_bin)
        write_uint64(self._shared_memory.base_address, self._offset__capacity_offset, other_capacity_bin)
        # write_uint64(self._shared_memory.base_address, self._offset__refresh_counter_offset, refresh_counter_bin)

        self._shared_memory.destroy_obj(new_other_offset)

        self.ignore_rehash = ignore_rehash

    def __len__(self):
        self._check_hashmap()
        return self._size
    
    def __iter__(self):
        self._check_hashmap()
        return IMutableMappingIterator(self)
    
    def iter_offset(self):
        self._check_hashmap()
        return IMutableMappingIteratorAsOffset(self)
    
    def iter_offset_pop(self):
        self._check_hashmap()
        return IMutableMappingIteratorAsOffset(self, True)
    
    # def __contains__(self, key: Hashable) -> bool:
    #     item_hash = hash(key)
    #     item_info_index: int = mask_least_significant_bits(item_hash, self.hash_bits)
    #     field_type_index = item_info_index * 4 + 0
    #     item_hash_index = item_info_index * 4 + 1
    #     item_bucket_index = item_info_index * 4 + 2
    #     item_value_index = item_info_index * 4 + 3
    #     field_type = self.hashmap[field_type_index]
    #     if 0 == field_type:
    #         return False
    #     elif 1 == field_type:
    #         return (item_hash == self.hashmap[item_hash_index]) and (key == self.hashmap[item_bucket_index])
    #     elif 2 == field_type:
    #         bucket = self.buckets[item_info_index]
    #         for sub_item_info_index in range(0, len(bucket), 4):
    #             bucket_field_type = bucket[sub_item_info_index + 0]
    #             if 0 == bucket_field_type:
    #                 continue

    #             sub_item_hash_index = sub_item_info_index + 1
    #             sub_item_key_obj_index = sub_item_info_index + 2
    #             sub_item_value_obj_index = sub_item_info_index + 3
    #             if (item_hash == bucket[sub_item_hash_index]) and (key == bucket[sub_item_key_obj_index]):
    #                 return True
            
    #         return False
    #     else:
    #         raise ValueError(f'Unknown MutableMappingHashmapFieldTypes field type at {item_info_index=}: {field_type}')

    def __getitem__(self, key: Hashable):
        self._check_hashmap()
        item_hash = hash(key)
        item_info_index: int = mask_least_significant_bits(item_hash, self.hash_bits) * 4
        field_type_index = item_info_index + 0
        item_hash_index = item_info_index + 1
        item_bucket_index = item_info_index + 2
        item_value_index = item_info_index + 3
        field_type = self.hashmap[field_type_index]
        if 0 == field_type:
            raise KeyError
        elif 1 == field_type:
            if (item_hash == self.hashmap[item_hash_index]) and (key == self.hashmap[item_bucket_index]):
                return self.hashmap[item_value_index]
            else:
                raise KeyError
        elif 2 == field_type:
            bucket_offset = self.hashmap[item_bucket_index]
            try:
                bucket = self.buckets[item_info_index]
                if bucket._offset != bucket_offset:
                    raise KeyError
            except KeyError:
                raise
                self.buckets[item_info_index] = bucket = IList(self._shared_memory, bucket_offset)

            for sub_item_info_index in range(0, len(bucket), 4):
                bucket_field_type = bucket[sub_item_info_index + 0]
                if 0 == bucket_field_type:
                    continue

                sub_item_hash_index = sub_item_info_index + 1
                sub_item_key_obj_index = sub_item_info_index + 2
                sub_item_value_obj_index = sub_item_info_index + 3
                if (item_hash == bucket[sub_item_hash_index]) and (key == bucket[sub_item_key_obj_index]):
                    return bucket[sub_item_value_obj_index]
            
            raise KeyError
        else:
            raise ValueError(f'Unknown MutableMappingHashmapFieldTypes field type at {item_info_index=}: {field_type}')

    def __setitem__(self, key, value):
        self._check_hashmap()
        key_hash = hash(key)
        item_info_index: int = mask_least_significant_bits(key_hash, self.hash_bits) * 4
        field_type_index = item_info_index + 0
        item_hash_index = item_info_index + 1
        item_bucket_index = item_info_index + 2
        item_value_index = item_info_index + 3
        field_type = self.hashmap[field_type_index]
        if 0 == field_type:
            self.hashmap[field_type_index] = 1
            self.hashmap[item_hash_index] = key_hash
            self.hashmap[item_bucket_index] = key
            self.hashmap[item_value_index] = value
            self._increase_size()
            return
        elif 1 == field_type:
            if (key_hash == self.hashmap[item_hash_index]) and (key == self.hashmap[item_bucket_index]):
                self.hashmap[item_value_index] = value
                return
            
            self._increase_refresh_counter()
            bucket, bucket_offset, _ = self._shared_memory.put_obj(list())
            bucket = cast(IList, bucket)
            bucket.set_capacity(4)
            bucket.extend_with(4, 0)
            self.buckets[item_info_index] = bucket
            bucket[0] = 1
            self.hashmap.move_item_to_list(item_hash_index, bucket, 1)
            self.hashmap.move_item_to_list(item_bucket_index, bucket, 2)
            self.hashmap.move_item_to_list(item_value_index, bucket, 3)
            self.hashmap[field_type_index] = 2
            self.hashmap[item_bucket_index] = bucket_offset
            bucket.append(1)
            bucket.append(key_hash)
            bucket.append(key)
            bucket.append(value)
            self._increase_size()
            return
        elif 2 == field_type:
            bucket_offset = self.hashmap[item_bucket_index]
            try:
                bucket = self.buckets[item_info_index]
                if bucket._offset != bucket_offset:
                    raise KeyError
            except KeyError:
                raise
                self.buckets[item_info_index] = bucket = IList(self._shared_memory, bucket_offset)

            bucket_len: int = len(bucket)
            for bucket_item_index in range(0, bucket_len, 4):
                bucket_field_type = bucket[bucket_item_index + 0]
                if 1 == bucket_field_type:
                    if (key_hash == bucket[bucket_item_index + 1]) and (key == bucket[bucket_item_index + 2]):
                        bucket[bucket_item_index + 3] = value
                        return
            
            for bucket_item_index in range(0, bucket_len, 4):
                bucket_field_type = bucket[bucket_item_index + 0]
                if 0 == bucket_field_type:
                    bucket[bucket_item_index + 0] = 1
                    bucket[bucket_item_index + 1] = key_hash
                    bucket[bucket_item_index + 2] = key
                    bucket[bucket_item_index + 3] = value
                    self._increase_size()
                    return
            else:
                bucket.append(1)
                bucket.append(key_hash)
                bucket.append(key)
                bucket.append(value)
                self._increase_size()
                return
        else:
            raise ValueError(f'Unknown MutableMappingHashmapFieldTypes field type at {item_info_index=}: {field_type}')

    def setitem_as_offset(self, key_hash, key_type, key_offset, value_type, value_offset):
        self._check_hashmap()
        key = (key_type, key_offset)
        value = (value_type, value_offset)
        item_info_index: int = mask_least_significant_bits(key_hash, self.hash_bits) * 4
        field_type_index = item_info_index + 0
        item_hash_index = item_info_index + 1
        item_bucket_index = item_info_index + 2
        item_value_index = item_info_index + 3
        field_type = self.hashmap[field_type_index]
        if 0 == field_type:
            self.hashmap[field_type_index] = 1
            self.hashmap[item_hash_index] = key_hash
            self.hashmap.setitem_as_offset(item_bucket_index, key)
            self.hashmap.setitem_as_offset(item_value_index, value)
            self._increase_size()
            return
        elif 1 == field_type:
            if (key_hash == self.hashmap[item_hash_index]) and (key == self.hashmap.getitem_as_offset(item_bucket_index)):
                self.hashmap.setitem_as_offset(item_value_index, value)
                return
            
            self._increase_refresh_counter()
            bucket, bucket_offset, _ = self._shared_memory.put_obj(list())
            bucket = cast(IList, bucket)
            bucket.set_capacity(4)
            bucket.extend_with(4, 0)
            self.buckets[item_info_index] = bucket
            bucket[0] = 1
            self.hashmap.move_item_to_list(item_hash_index, bucket, 1)
            self.hashmap.move_item_to_list(item_bucket_index, bucket, 2)
            self.hashmap.move_item_to_list(item_value_index, bucket, 3)
            self.hashmap[field_type_index] = 2
            self.hashmap[item_bucket_index] = bucket_offset
            bucket.append(1)
            bucket.append(key_hash)
            bucket.append_as_offset(key)
            bucket.append_as_offset(value)
            self._increase_size()
            return
        elif 2 == field_type:
            bucket_offset = self.hashmap[item_bucket_index]
            try:
                bucket = self.buckets[item_info_index]
                if bucket._offset != bucket_offset:
                    raise KeyError
            except KeyError:
                raise
                self.buckets[item_info_index] = bucket = IList(self._shared_memory, bucket_offset)

            bucket_len: int = len(bucket)
            for bucket_item_index in range(0, bucket_len, 4):
                bucket_field_type = bucket[bucket_item_index + 0]
                if 1 == bucket_field_type:
                    if (key_hash == bucket[bucket_item_index + 1]) and (key == bucket.getitem_as_offset(bucket_item_index + 2)):
                        bucket.setitem_as_offset(bucket_item_index + 3, value)
                        return
            
            for bucket_item_index in range(0, bucket_len, 4):
                bucket_field_type = bucket[bucket_item_index + 0]
                if 0 == bucket_field_type:
                    bucket[bucket_item_index + 0] = 1
                    bucket[bucket_item_index + 1] = key_hash
                    bucket.setitem_as_offset(bucket_item_index + 2, key)
                    bucket.setitem_as_offset(bucket_item_index + 3, value)
                    self._increase_size()
                    return
            else:
                bucket.append(1)
                bucket.append(key_hash)
                bucket.append_as_offset(key)
                bucket.append_as_offset(value)
                self._increase_size()
                return
        else:
            raise ValueError(f'Unknown MutableMappingHashmapFieldTypes field type at {item_info_index=}: {field_type}')

    def __delitem__(self, key):
        self._check_hashmap()
        item_hash = hash(key)
        item_info_index: int = mask_least_significant_bits(item_hash, self.hash_bits) * 4
        field_type_index = item_info_index + 0
        item_hash_index = item_info_index + 1
        item_bucket_index = item_info_index + 2
        item_value_index = item_info_index + 3
        field_type = self.hashmap[field_type_index]
        if 0 == field_type:
            raise KeyError
        elif 1 == field_type:
            if (item_hash == self.hashmap[item_hash_index]) and (key == self.hashmap[item_bucket_index]):
                self.hashmap[field_type_index] = 0
                self.hashmap[item_hash_index] = None
                self.hashmap[item_bucket_index] = None
                self.hashmap[item_value_index] = None
                self._decrease_size()
                return
            else:
                raise KeyError
        elif 2 == field_type:
            bucket_offset = self.hashmap[item_bucket_index]
            try:
                bucket = self.buckets[item_info_index]
                if bucket._offset != bucket_offset:
                    raise KeyError
            except KeyError:
                raise
                self.buckets[item_info_index] = bucket = IList(self._shared_memory, bucket_offset)

            for sub_item_info_index in range(0, len(bucket), 4):
                bucket_field_type = bucket[sub_item_info_index + 0]
                if 0 == bucket_field_type:
                    continue

                sub_item_hash_index = sub_item_info_index + 1
                sub_item_key_obj_index = sub_item_info_index + 2
                sub_item_value_obj_index = sub_item_info_index + 3
                if (item_hash == bucket[sub_item_hash_index]) and (key == bucket[sub_item_key_obj_index]):
                    bucket[sub_item_info_index + 0] = 0
                    bucket[sub_item_hash_index] = None
                    bucket[sub_item_key_obj_index] = None
                    bucket[sub_item_value_obj_index] = None
                    self._decrease_size()
                    return

            raise KeyError
        else:
            raise ValueError(f'Unknown MutableMappingHashmapFieldTypes field type at {item_info_index=}: {field_type}')

    @property
    def hash_bits(self) -> int:
        return self._hash_bits

    @hash_bits.setter
    def hash_bits(self, value: int) -> None:
        self._hash_bits = value
        self._capacity = 2 ** value
    
    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        if value <= self._capacity:
            return
        
        if value <= 2:
            self.hash_bits = 1
        else:
            self.hash_bits = int(ceil(log2(value)))
    
    def __str__(self) -> str:
        return dict(self).__str__()

    def __repr__(self) -> str:
        return dict(self).__repr__()

    def _free_mem(self):
        if self._offset is not None:
            if self.hashmap_offset is not None:
                self._check_hashmap()
            
            for _, bucket in self.buckets.items():
                self._shared_memory.destroy_obj(bucket._offset)
            self.buckets.clear()
            if self.hashmap_offset is not None:
                self._shared_memory.destroy_obj(self.hashmap_offset)
                self.hashmap_offset = None
            
            self._shared_memory.free(self._offset)
            self._offset = None


class IMutableMappingIterator:
    def __init__(self, imapping: IMutableMapping) -> None:
        self._imapping = imapping
        self._index = 0
        self._sub_index = 0
    
    def __next__(self):
        if self._imapping._check_hashmap():
            raise RuntimeError("Dictionary's hashmap changed during iteration")

        while self._index < self._imapping.capacity:
            item_info_index: int = self._index * 4
            field_type_index = item_info_index + 0
            item_hash_index = item_info_index + 1
            item_bucket_index = item_info_index + 2
            item_value_index = item_info_index + 3
            field_type = self._imapping.hashmap[field_type_index]
            if 0 == field_type:
                self._index += 1
                continue
            elif 1 == field_type:
                result = self._imapping.hashmap[item_bucket_index]
                self._index += 1
                return result
            elif 2 == field_type:
                bucket_offset = self._imapping.hashmap[item_bucket_index]
                try:
                    bucket = self._imapping.buckets[item_info_index]
                    if bucket._offset != bucket_offset:
                        raise KeyError
                except KeyError:
                    raise
                    self._imapping.buckets[item_info_index] = bucket = IList(self._imapping._shared_memory, bucket_offset)

                bucket_len = len(bucket)
                sub_item_info_index = self._sub_index
                while (sub_item_info_index * 4) < bucket_len:
                    sub_item_field_type_index = sub_item_info_index * 4 + 0
                    if bucket[sub_item_field_type_index] == 0:
                        sub_item_info_index += 1
                        continue

                    sub_item_hash_index = sub_item_info_index * 4 + 1
                    sub_item_key_obj_index = sub_item_info_index * 4 + 2
                    sub_item_value_obj_index = sub_item_info_index * 4 + 3
                    result = bucket[sub_item_key_obj_index]
                    self._sub_index += 1
                    return result
                else:
                    self._sub_index = 0
                    self._index += 1
                    continue
            else:
                raise ValueError(f'Unknown MutableMappingHashmapFieldTypes field type at {item_info_index=}: {field_type}')
        else:
            raise StopIteration
    
    def __iter__(self):
        return self


class IMutableMappingIteratorAsOffset:
    def __init__(self, imapping: IMutableMapping, pop: bool = False) -> None:
        self._imapping = imapping
        self._pop: bool = pop
        self._index = 0
        self._sub_index = 0
    
    def __next__(self):
        if self._imapping._check_hashmap():
            raise RuntimeError("Dictionary's hashmap changed during iteration")

        while self._index < self._imapping.capacity:
            item_info_index: int = self._index * 4
            field_type_index = item_info_index + 0
            item_hash_index = item_info_index + 1
            item_bucket_index = item_info_index + 2
            item_value_index = item_info_index + 3
            field_type = self._imapping.hashmap[field_type_index]
            if 0 == field_type:
                self._index += 1
                continue
            elif 1 == field_type:
                key_hash = self._imapping.hashmap[item_hash_index]
                key_type, key_offset = self._imapping.hashmap.getitem_as_offset(item_bucket_index)
                value_type, value_offset = self._imapping.hashmap.getitem_as_offset(item_value_index)
                if self._pop:
                    self._imapping.hashmap[field_type_index] = 0
                    self._imapping.hashmap[item_hash_index] = None
                    self._imapping.hashmap.setitem_as_offset(item_bucket_index, (0, 0), False)
                    self._imapping.hashmap.setitem_as_offset(item_value_index, (0, 0), False)

                self._index += 1
                return key_hash, key_type, key_offset, value_type, value_offset
            elif 2 == field_type:
                bucket_offset = self._imapping.hashmap[item_bucket_index]
                try:
                    bucket = self._imapping.buckets[item_info_index]
                    if bucket._offset != bucket_offset:
                        raise KeyError
                except KeyError:
                    raise
                    self._imapping.buckets[item_info_index] = bucket = IList(self._imapping._shared_memory, bucket_offset)

                bucket_len = len(bucket)
                sub_item_info_index = self._sub_index
                while (sub_item_info_index * 4) < bucket_len:
                    sub_item_field_type_index = sub_item_info_index * 4 + 0
                    if bucket[sub_item_field_type_index] == 0:
                        sub_item_info_index += 1
                        continue

                    sub_item_hash_index = sub_item_info_index * 4 + 1
                    sub_item_key_obj_index = sub_item_info_index * 4 + 2
                    sub_item_value_obj_index = sub_item_info_index * 4 + 3

                    key_hash = bucket[sub_item_hash_index]
                    key_type, key_offset = bucket.getitem_as_offset(sub_item_key_obj_index)
                    value_type, value_offset = bucket.getitem_as_offset(sub_item_value_obj_index)
                    if self._pop:
                        bucket[sub_item_field_type_index] = 0
                        bucket[sub_item_hash_index] = None
                        bucket.setitem_as_offset(sub_item_key_obj_index, (0, 0), False)
                        bucket.setitem_as_offset(sub_item_value_obj_index, (0, 0), False)

                    self._sub_index += 1
                    return key_hash, key_type, key_offset, value_type, value_offset
                else:
                    self._sub_index = 0
                    self._index += 1
                    continue
            else:
                raise ValueError(f'Unknown MutableMappingHashmapFieldTypes field type at {item_info_index=}: {field_type}')
        else:
            raise StopIteration
    
    def __iter__(self):
        return self


class TMutableMapping:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: AbsMutableMapping) -> Tuple[IMutableMapping, Offset, Size]:
        obj: IMutableMapping = IMutableMapping(shared_memory, obj=obj)
        return obj, obj._offset, obj._obj_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> IMutableMapping:
        if ObjectType.tmutablemapping != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError
        
        return IMutableMapping(shared_memory, offset)
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.tmutablemapping != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError
        
        obj: IMutableMapping = IMutableMapping(shared_memory, offset)
        obj._free_mem()


# ======================================================================================================================
# === General Object =============================================================================================================


class ForceGeneralObjectCopy:
    def __init__(self, obj: Any) -> None:
        self.obj = obj


FGeneralObjectCopy = ForceGeneralObjectCopy
forcegeneralobjectcopy = ForceGeneralObjectCopy
fgeneralobjectcopy = ForceGeneralObjectCopy


class ForceGeneralObjectInplace:
    def __init__(self, obj: Any) -> None:
        self.obj = obj


FGeneralObjectInplace = ForceGeneralObjectInplace
forcegeneralobjectinplace = ForceGeneralObjectInplace
fgeneralobjectinplace = ForceGeneralObjectInplace


class GeneralObjectOffsets(IntEnum):
    pickled_obj = 0
    obj_dict = 1
    setable_data_descriptor_field_names = 2


def tgeneralobject_custom_getattribute(self, name):
    if name in {'_tgeneralobject_imutablemapping_attributes', '_tgeneralobject_setable_data_descriptor_field_names'} or name.startswith('__'):
        return object.__getattribute__(self, name)
    
    try:
        return self._tgeneralobject_imutablemapping_attributes[name]
    except KeyError:
        pass
    
    return object.__getattribute__(self, name)


def tgeneralobject_custom_setattr(self, name, value):
    if name in {'_tgeneralobject_imutablemapping_attributes', '_tgeneralobject_setable_data_descriptor_field_names'} or name.startswith('__'):
        object.__setattr__(self, name, value)
    else:
        if isfunction(value) or ismethod(value) or isinstance(value, FrameType) or isinstance(value, CodeType) or ismethoddescriptor(value):
            object.__setattr__(self, name, value)
            return

        # try:
        #     if name in self._tgeneralobject_setable_data_descriptor_field_names:
        #         object.__setattr__(self, name, value)
        # except AttributeError:
        #     pass
        
        self._tgeneralobject_imutablemapping_attributes[name] = value


def tgeneralobject_custom_delattr(self, name):
    if name in {'_tgeneralobject_imutablemapping_attributes', '_tgeneralobject_setable_data_descriptor_field_names'} or name.startswith('__'):
        object.__delattr__(self, name)
    else:
        has_value_static: bool = False
        value_static = None
        try:
            value_static = getattr_static(self, name)
            has_value_static = True
        except AttributeError:
            pass

        deleted: bool = False
        try:
            if has_value_static and isfunction(value_static) or ismethod(value_static) or isinstance(value_static, FrameType) or isinstance(value_static, CodeType) or ismethoddescriptor(value_static):
                object.__delattr__(self, name)
                return
        except AttributeError:
            pass

        try:
            if has_value_static and (not isclass(value_static)) and hasattr(value_static, "__delete__"):
                object.__delattr__(self, name)
                deleted = True
        except AttributeError:
            pass
        
        try:
            del self._tgeneralobject_imutablemapping_attributes[name]
            return
        except KeyError:
            pass
        
        if not deleted:
            object.__delattr__(self, name)


def tgeneralobject_wrap_obj(obj, mapped_obj_dict: IMutableMapping, setable_data_descriptor_field_names: Set[str], init_mapped_obj_dict: bool):
    base = obj.__class__
    setattr(obj, '_tgeneralobject_imutablemapping_attributes', mapped_obj_dict)
    setattr(obj, '_tgeneralobject_setable_data_descriptor_field_names', setable_data_descriptor_field_names)
    if init_mapped_obj_dict:
        object_fields = set(dir(object))
        obj_fields = set(dir(obj)) - object_fields
        for key in obj_fields:
            value = getattr_static(obj, key)
            if key in {'_tgeneralobject_imutablemapping_attributes', '_tgeneralobject_setable_data_descriptor_field_names'} or key.startswith('__'):
                continue

            if isfunction(value) or ismethod(value) or isinstance(value, FrameType) or isinstance(value, CodeType) or ismethoddescriptor(value):
                continue

            if (not isclass(value)) and (hasattr(value, "__get__") and (not (hasattr(value, "__set__") or hasattr(value, "__delete__")))):
                continue

            if is_setable_data_descriptor(value):
                setable_data_descriptor_field_names.add(key)
            
            mapped_obj_dict[key] = getattr(obj, key)
    
    NewClass = type(
        base.__name__ + 'WrappedByTGeneralObject',
        (base,),
        {
            '__getattribute__': tgeneralobject_custom_getattribute,
            '__setattr__': tgeneralobject_custom_setattr,
            '__delattr__': tgeneralobject_custom_delattr,
        }
    )
    obj.__class__ = NewClass


class TGeneralObject:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: Any) -> Tuple[Any, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.tgeneralobject, 24)
        created_items_offsets: List[Offset] = list()
        try:
            make_changes_inplace: bool = True
            if isinstance(obj, ForceGeneralObjectCopy):
                obj = obj.obj
                make_changes_inplace = False
            elif isinstance(obj, ForceGeneralObjectInplace):
                obj = obj.obj
                make_changes_inplace = True

            dumped_obj: bytes = pickle_dumps(obj)
            dumped_mapped_obj_type, dumped_obj_offset, dumped_obj_type_size = shared_memory.put_obj(dumped_obj)
            created_items_offsets.append(dumped_obj_offset)
            mapped_obj_dict, obj_dict_offset, obj_dict_size = shared_memory.put_obj(dict())
            created_items_offsets.append(obj_dict_offset)
            
            write_uint64(shared_memory.base_address, offset + 16 + 0, dumped_obj_offset)
            write_uint64(shared_memory.base_address, offset + 16 + 8, obj_dict_offset)
            
            setable_data_descriptor_field_names: Set[str] = set()

            mapped_obj = None
            if make_changes_inplace:
                tgeneralobject_wrap_obj(obj, mapped_obj_dict, setable_data_descriptor_field_names, True)
                mapped_obj = obj
            else:
                # mapped_obj = self.init_from_shared_memory(shared_memory, offset)
                mapped_obj = pickle_loads(dumped_obj)
                tgeneralobject_wrap_obj(mapped_obj, mapped_obj_dict, setable_data_descriptor_field_names, True)

            dumped_setable_data_descriptor_field_names: bytes = pickle_dumps(setable_data_descriptor_field_names)
            mapped_dumped_setable_data_descriptor_field_names, dumped_setable_data_descriptor_field_names_offset, dumped_setable_data_descriptor_field_names_size = shared_memory.put_obj(dumped_setable_data_descriptor_field_names)
            write_uint64(shared_memory.base_address, offset + 16 + 16, dumped_setable_data_descriptor_field_names_offset)
        except:
            shared_memory.free(offset)
            for item_offset in created_items_offsets:
                shared_memory.destroy_obj(item_offset)
            
            raise

        return mapped_obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> Any:
        if ObjectType.tgeneralobject != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        dumped_obj_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        dumped_obj: bytes = shared_memory.get_obj(dumped_obj_offset)
        
        obj_dict_offset = read_uint64(shared_memory.base_address, offset + 16 + 8)
        mapped_obj_dict = shared_memory.get_obj(obj_dict_offset)
        obj = pickle_loads(dumped_obj)
        
        dumped_setable_data_descriptor_field_names_offset = read_uint64(shared_memory.base_address, offset + 16 + 16)
        dumped_setable_data_descriptor_field_names = shared_memory.get_obj(dumped_setable_data_descriptor_field_names_offset)
        setable_data_descriptor_field_names = pickle_loads(dumped_setable_data_descriptor_field_names)
        
        tgeneralobject_wrap_obj(obj, mapped_obj_dict, setable_data_descriptor_field_names, False)
        return obj
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.tgeneralobject != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        dumped_obj_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        shared_memory.destroy_obj(dumped_obj_offset)
        obj_dict_offset = read_uint64(shared_memory.base_address, offset + 16 + 8)
        if obj_dict_offset:
            shared_memory.destroy_obj(obj_dict_offset)
        
        dumped_setable_data_descriptor_field_names_offset = read_uint64(shared_memory.base_address, offset + 16 + 16)
        shared_memory.destroy_obj(dumped_setable_data_descriptor_field_names_offset)
        shared_memory.free(offset)
    
    # def buffer(self, shared_memory: 'SharedMemory', offset: Offset) -> memoryview:
    #     if ObjectType.tgeneralobject != read_uint64(shared_memory.base_address, offset + 0):
    #         raise WrongObjectTypeError

    #     dumped_obj_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
    #     return shared_memory.get_obj_buffer(dumped_obj_offset)
    
    # def buffer_2(self, shared_memory: 'SharedMemory', offset: Offset) -> Tuple[int, int]:
    #     if ObjectType.tgeneralobject != read_uint64(shared_memory.base_address, offset + 0):
    #         raise WrongObjectTypeError


    #     dumped_obj_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
    #     return shared_memory.get_obj_buffer_2(dumped_obj_offset)


# ======================================================================================================================
# === Static Object =============================================================================================================


class ForceStaticObjectCopy:
    def __init__(self, obj: Any) -> None:
        self.obj = obj


FStaticObjectCopy = ForceStaticObjectCopy
forcestaticobjectcopy = ForceStaticObjectCopy
fstaticobjectcopy = ForceStaticObjectCopy


class ForceStaticObjectInplace:
    def __init__(self, obj: Any) -> None:
        self.obj = obj


FStaticObjectInplace = ForceStaticObjectInplace
forcestaticobjectinplace = ForceStaticObjectInplace
fstaticobjectinplace = ForceStaticObjectInplace


class StaticObjectOffsets(IntEnum):
    pickled_obj = 0
    pickled_attributes_dict = 1
    attributes_slots = 2
    setable_data_descriptor_field_names = 3


def tstaticobject_custom_getattribute(self, name):
    if name in {'_tstaticobject_attributes_dict', '_tstaticobject_attributes_slots', '_tstaticobject_setable_data_descriptor_field_names'} or name.startswith('__'):
        return object.__getattribute__(self, name)
    
    try:
        return self._tstaticobject_attributes_slots[self._tstaticobject_attributes_dict[name]]
    except KeyError:
        pass
    
    return object.__getattribute__(self, name)


def tstaticobject_custom_setattr(self, name, value):
    if name in {'_tstaticobject_attributes_dict', '_tstaticobject_attributes_slots', '_tstaticobject_setable_data_descriptor_field_names'} or name.startswith('__'):
        object.__setattr__(self, name, value)
    else:
        if isfunction(value) or ismethod(value) or isinstance(value, FrameType) or isinstance(value, CodeType) or ismethoddescriptor(value):
            object.__setattr__(self, name, value)
            return
        
        # try:
        #     if name in self._tstaticobject_setable_data_descriptor_field_names:
        #         object.__setattr__(self, name, value)
        # except AttributeError:
        #     pass
        
        try:
            self._tstaticobject_attributes_slots[self._tstaticobject_attributes_dict[name]] = value
            return
        except KeyError:
            pass
            
        object.__setattr__(self, name, value)


def tstaticobject_custom_delattr(self, name):
    if name in {'_tstaticobject_attributes_dict', '_tstaticobject_attributes_slots', '_tstaticobject_setable_data_descriptor_field_names'} or name.startswith('__'):
        object.__delattr__(self, name)
    else:
        if name in self._tstaticobject_attributes_dict:
            raise AttributeError(f"'{type(self).__name__}' object attribute '{name}' is read-only")
        else:
            object.__delattr__(self, name)


def tstaticobject_wrap_obj(obj, attributes_dict: Dict, attributes_slots: IList, setable_data_descriptor_field_names: Set[str], init_mapped_attributes: bool):
    base = obj.__class__
    setattr(obj, '_tstaticobject_attributes_dict', attributes_dict)
    setattr(obj, '_tstaticobject_attributes_slots', attributes_slots)
    setattr(obj, '_tstaticobject_setable_data_descriptor_field_names', setable_data_descriptor_field_names)
    if init_mapped_attributes:
        object_fields = set(dir(object))
        obj_fields = set(dir(obj)) - object_fields
        good_fields: List[Hashable] = list()
        for key in obj_fields:
            value = getattr_static(obj, key)
            if key in {'_tstaticobject_attributes_dict', '_tstaticobject_attributes_slots', '_tstaticobject_setable_data_descriptor_field_names'} or key.startswith('__'):
                continue

            if isfunction(value) or ismethod(value) or isinstance(value, FrameType) or isinstance(value, CodeType) or ismethoddescriptor(value):
                continue

            if (not isclass(value)) and (hasattr(value, "__get__") and (not (hasattr(value, "__set__") or hasattr(value, "__delete__")))):
                continue
            
            if is_setable_data_descriptor(value):
                setable_data_descriptor_field_names.add(key)
            
            good_fields.append(key)
        
        good_fields_len = len(good_fields)
        attributes_slots.set_capacity(good_fields_len)
        attributes_slots.extend_with(good_fields_len, 0)
        for index, key in enumerate(good_fields):
            attributes_dict[key] = index
            value = getattr(obj, key)
            attributes_slots[index] = value
    
    NewClass = type(
        base.__name__ + 'WrappedByTStaticObject',
        (base,),
        {
            '__getattribute__': tstaticobject_custom_getattribute,
            '__setattr__': tstaticobject_custom_setattr,
            '__delattr__': tstaticobject_custom_delattr,
        }
    )
    obj.__class__ = NewClass


class TStaticObject:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: Any) -> Tuple[Any, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.tstaticobject, 32)
        created_items_offsets: List[Offset] = list()
        try:
            make_changes_inplace: bool = True
            if isinstance(obj, ForceStaticObjectCopy):
                obj = obj.obj
                make_changes_inplace = False
            elif isinstance(obj, ForceStaticObjectInplace):
                obj = obj.obj
                make_changes_inplace = True

            dumped_obj: bytes = pickle_dumps(obj)
            dumped_mapped_obj, dumped_obj_offset, dumped_obj_size = shared_memory.put_obj(dumped_obj)
            created_items_offsets.append(dumped_obj_offset)
            write_uint64(shared_memory.base_address, offset + 16 + 0, dumped_obj_offset)

            attributes_dict: Dict = dict()

            attributes_slots, attributes_slots_offset, attributes_slots_size = shared_memory.put_obj(list())
            created_items_offsets.append(attributes_slots_offset)
            write_uint64(shared_memory.base_address, offset + 16 + 16, attributes_slots_offset)
            
            setable_data_descriptor_field_names: Set[str] = set()

            mapped_obj = None
            if make_changes_inplace:
                tstaticobject_wrap_obj(obj, attributes_dict, attributes_slots, setable_data_descriptor_field_names, True)
                mapped_obj = obj
            else:
                # mapped_obj = self.init_from_shared_memory(shared_memory, offset)
                mapped_obj = pickle_loads(dumped_obj)
                tstaticobject_wrap_obj(mapped_obj, attributes_dict, attributes_slots, setable_data_descriptor_field_names, True)
            
            dumped_attributes_dict: bytes = pickle_dumps(attributes_dict)
            dumped_mapped_attributes_dict, dumped_attributes_dict_offset, dumped_attributes_dict_size = shared_memory.put_obj(dumped_attributes_dict)
            write_uint64(shared_memory.base_address, offset + 16 + 8, dumped_attributes_dict_offset)
            
            dumped_setable_data_descriptor_field_names: bytes = pickle_dumps(setable_data_descriptor_field_names)
            mapped_dumped_setable_data_descriptor_field_names, dumped_setable_data_descriptor_field_names_offset, dumped_setable_data_descriptor_field_names_size = shared_memory.put_obj(dumped_setable_data_descriptor_field_names)
            write_uint64(shared_memory.base_address, offset + 16 + 24, dumped_setable_data_descriptor_field_names_offset)
        except:
            shared_memory.free(offset)
            for item_offset in created_items_offsets:
                shared_memory.destroy_obj(item_offset)
            
            raise
        
        return mapped_obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> Any:
        if ObjectType.tstaticobject != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        dumped_obj_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        dumped_obj: bytes = shared_memory.get_obj(dumped_obj_offset)
        obj = pickle_loads(dumped_obj)

        attributes_slots_offset = read_uint64(shared_memory.base_address, offset + 16 + 16)
        attributes_slots: IList = shared_memory.get_obj(attributes_slots_offset)

        dumped_attributes_dict_offset = read_uint64(shared_memory.base_address, offset + 16 + 8)
        dumped_attributes_dict = shared_memory.get_obj(dumped_attributes_dict_offset)
        attributes_dict = pickle_loads(dumped_attributes_dict)

        dumped_setable_data_descriptor_field_names_offset = read_uint64(shared_memory.base_address, offset + 16 + 24)
        dumped_setable_data_descriptor_field_names = shared_memory.get_obj(dumped_setable_data_descriptor_field_names_offset)
        setable_data_descriptor_field_names = pickle_loads(dumped_setable_data_descriptor_field_names)

        tstaticobject_wrap_obj(obj, attributes_dict, attributes_slots, setable_data_descriptor_field_names, False)
        return obj
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.tstaticobject != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        dumped_obj_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        shared_memory.destroy_obj(dumped_obj_offset)
        attributes_slots_offset = read_uint64(shared_memory.base_address, offset + 16 + 16)
        shared_memory.destroy_obj(attributes_slots_offset)
        dumped_attributes_dict_offset = read_uint64(shared_memory.base_address, offset + 16 + 8)
        shared_memory.destroy_obj(dumped_attributes_dict_offset)
        dumped_setable_data_descriptor_field_names_offset = read_uint64(shared_memory.base_address, offset + 16 + 24)
        shared_memory.destroy_obj(dumped_setable_data_descriptor_field_names_offset)
        shared_memory.free(offset)
    
    # def buffer(self, shared_memory: 'SharedMemory', offset: Offset) -> memoryview:
    #     if ObjectType.tstaticobject != read_uint64(shared_memory.base_address, offset + 0):
    #         raise WrongObjectTypeError

    #     dumped_obj_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
    #     return shared_memory.get_obj_buffer(dumped_obj_offset)
    
    # def buffer_2(self, shared_memory: 'SharedMemory', offset: Offset) -> Tuple[int, int]:
    #     if ObjectType.tstaticobject != read_uint64(shared_memory.base_address, offset + 0):
    #         raise WrongObjectTypeError


    #     dumped_obj_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
    #     return shared_memory.get_obj_buffer_2(dumped_obj_offset)


# ======================================================================================================================
# === Numpy ndarray =============================================================================================================


class TNumpyNdarrayOffsets(IntEnum):
    data_buffer_offset = 0
    shape_tuple_offset = 1
    pickled_datatype_offset = 2


class TNumpyNdarray:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', nparray: np.ndarray) -> Tuple[np.ndarray, Offset, Size]:
        shape = tuple(nparray.shape)
        data_type = nparray.dtype
        pickled_data_type = pickle_dumps(data_type)
        data_buffer: bytes = nparray.tobytes()
        offset, real_size = shared_memory.malloc(ObjectType.tnumpyndarray, 24)
        created_items_offsets: List[Offset] = list()
        try:
            data_buffer_mapped_obj, data_buffer_offset, data_buffer_size = shared_memory.put_obj(data_buffer)
            created_items_offsets.append(data_buffer_offset)
            shape_mapped_obj, shape_offset, shape_size = shared_memory.put_obj(shape)
            created_items_offsets.append(shape_offset)
            pickled_data_type_mapped_obj, pickled_data_type_offset, pickled_data_type_size = shared_memory.put_obj(pickled_data_type)
            write_uint64(shared_memory.base_address, offset + 16 + 0, data_buffer_offset)
            write_uint64(shared_memory.base_address, offset + 16 + 8, shape_offset)
            write_uint64(shared_memory.base_address, offset + 16 + 16, pickled_data_type_offset)
            mapped_nparray: np.ndarray = make_numpy_array_from_obj_offset(shared_memory, data_buffer_offset, shape, data_type)
        except:
            shared_memory.free(offset)
            for item_offset in created_items_offsets:
                shared_memory.destroy_obj(item_offset)
            
            raise

        return mapped_nparray, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> dict:
        if ObjectType.tnumpyndarray != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        data_buffer_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        shape_offset = read_uint64(shared_memory.base_address, offset + 16 + 8)
        pickled_data_type_offset = read_uint64(shared_memory.base_address, offset + 16 + 16)
        shape = shared_memory.get_obj(shape_offset)
        pickled_data_type = shared_memory.get_obj(pickled_data_type_offset)
        data_type = pickle_loads(pickled_data_type)
        mapped_nparray: np.ndarray = make_numpy_array_from_obj_offset(shared_memory, data_buffer_offset, shape, data_type)
        return mapped_nparray
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.tnumpyndarray != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        data_buffer_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        shape_offset = read_uint64(shared_memory.base_address, offset + 16 + 8)
        pickled_data_type_offset = read_uint64(shared_memory.base_address, offset + 16 + 16)
        shared_memory.destroy_obj(data_buffer_offset)
        shared_memory.destroy_obj(shape_offset)
        shared_memory.destroy_obj(pickled_data_type_offset)
        shared_memory.free(offset)
    
    def buffer(self, shared_memory: 'SharedMemory', offset: Offset) -> memoryview:
        if ObjectType.tnumpyndarray != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        data_buffer_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        return shared_memory.get_obj_buffer(data_buffer_offset)
    
    def buffer_2(self, shared_memory: 'SharedMemory', offset: Offset) -> Tuple[int, int]:
        if ObjectType.tnumpyndarray != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError


        data_buffer_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        return shared_memory.get_obj_buffer_2(data_buffer_offset)


# ======================================================================================================================
# === Numpy ndarray =============================================================================================================


class TTorchTensorOffsets(IntEnum):
    numpy_ndarray_offset = 0


class TTorchTensor:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', tensor: Tensor) -> Tuple[Tensor, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.ttorchtensor, 8)
        created_items_offsets: List[Offset] = list()
        try:
            numpy_ndarray_mapped_obj, numpy_ndarray_offset, numpy_ndarray_size = shared_memory.put_obj(tensor.numpy())
            created_items_offsets.append(numpy_ndarray_offset)
            write_uint64(shared_memory.base_address, offset + 16 + 0, numpy_ndarray_offset)
            mapped_torch_tensor: Tensor = from_numpy(numpy_ndarray_mapped_obj)
        except:
            self._offset = None
            shared_memory.free(offset)
            for item_offset in created_items_offsets:
                shared_memory.destroy_obj(item_offset)
            
            raise
        return mapped_torch_tensor, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> dict:
        if ObjectType.ttorchtensor != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        numpy_ndarray_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        numpy_ndarray_mapped_obj: np.ndarray = shared_memory.get_obj(numpy_ndarray_offset)
        mapped_torch_tensor: Tensor = from_numpy(numpy_ndarray_mapped_obj)
        return mapped_torch_tensor
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.ttorchtensor != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        numpy_ndarray_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        shared_memory.destroy_obj(numpy_ndarray_offset)
        shared_memory.free(offset)
    
    def buffer(self, shared_memory: 'SharedMemory', offset: Offset) -> memoryview:
        if ObjectType.ttorchtensor != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError

        numpy_ndarray_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        return shared_memory.get_obj_buffer(numpy_ndarray_offset)
    
    def buffer_2(self, shared_memory: 'SharedMemory', offset: Offset) -> Tuple[int, int]:
        if ObjectType.ttorchtensor != read_uint64(shared_memory.base_address, offset + 0):
            raise WrongObjectTypeError


        numpy_ndarray_offset = read_uint64(shared_memory.base_address, offset + 16 + 0)
        return shared_memory.get_obj_buffer_2(numpy_ndarray_offset)


# ======================================================================================================================
# === Types and Codecs ==========================================================================================================


# Add your own codecs to `codec_by_type`
codec_by_type: Dict[ObjectType, TBase] = {
    ObjectType.tnone: TNone(),
    ObjectType.tint: TInt(),
    ObjectType.tbool: TBool(),
    ObjectType.tfloat: TFloat(),
    ObjectType.tbytes: TBytes(),
    ObjectType.tbytearray: TBytearray(),
    ObjectType.tstr: TStr(),
    ObjectType.tlist: TList(),
    ObjectType.ttuple: TTuple(),
    ObjectType.tmutableset: TMutableSet(),
    ObjectType.tset: TSet(),
    ObjectType.tmutablemapping: TMutableMapping(),
    ObjectType.tmapping: TMapping(),
    ObjectType.tfastdict: TFastDict(),
    ObjectType.tsmallint: TSmallInt(),
    ObjectType.tbigint: TBigInt(),
    ObjectType.tgeneralobject: TGeneralObject(),
    ObjectType.tpickable: TGeneralObject(),
    ObjectType.tstaticobject: TStaticObject(),
    ObjectType.tnumpyndarray: TNumpyNdarray(),
    ObjectType.ttorchtensor: TTorchTensor(),
}

# Add your own types to `obj_type_map`
obj_type_map: Dict[Type, ObjectType] = {
}


# ======================================================================================================================
# === Message ==========================================================================================================


class MessageOffsets(IntEnum):
    previous_message_offset = 0
    next_message_offset = 1
    item_offset = 2


class SharedMemory:
    def __init__(self, name: str, create: bool = False, size: Optional[int] = None, queue_type: QueueType = QueueType.fifo, zero_mem: bool = True, 
                 consumer_id: Optional[int] = None, creator_destroy_timeout: float = 5.0, unlink_old: bool = True):
        global current_shared_memory_instance
        current_shared_memory_instance = self
        self._initiated: bool = False
        self._consumer_id: Optional[int] = consumer_id
        self._creator_destroy_timeout: float = creator_destroy_timeout
        self.offset_to_be_monitored: Offset = None
        self._malloc_time: float = 0.0
        self._realloc_time: float = 0.0
        self._name: str = name
        self._create: bool = create
        self._queue_type: QueueType = queue_type
        self._zero_mem: bool = zero_mem
        self._last_message_offset: Offset = None
        self._asleep_func: Coroutine = self._default_asleep_func

        sys_arr_length = 13
        self.global_sys_array_len: int = sys_arr_length
        arr_byte_size = sys_arr_length * 8
        self.global_sys_area_size: int = arr_byte_size

        self._size: Optional[int] = size or None
        if (size is None) or (0 == size):
            size = self.global_sys_area_size
            if self._create:
                self._size = size
        
        if self._create:
            if unlink_old:
                SharedMemory.unlink_by_name(name)
            
            self._shared_memory: MultiprocessingSharedMemory = MultiprocessingSharedMemory(name=name, create=create, size=size)
            self._init_post_mem()
            
            write_uint64(self.base_address, self.sys_values_offset + 0, self._size)
            write_uint64(self.base_address, self.sys_values_offset + 8, sys_arr_length * 8)
            write_uint64(self.base_address, self.sys_values_offset + 16, self._size - arr_byte_size)
            write_uint64(self.base_address, self.sys_values_offset + 24, self._size)
            write_uint64(self.base_address, self.sys_values_offset + 32, sys_arr_length * 8)
            write_uint64(self.base_address, self.sys_values_offset + 40, 0)
            write_uint64(self.base_address, self.sys_values_offset + 48, 0)
            write_uint64(self.base_address, self.sys_values_offset + 56, 0)
            write_uint64(self.base_address, self.sys_values_offset + 64, 0)
            write_uint64(self.base_address, self.sys_values_offset + 72, 0)
            write_uint64(self.base_address, self.sys_values_offset + 80, 0)
            write_uint64(self.base_address, self.sys_values_offset + 88, 0)
            write_uint64(self.base_address, self.sys_values_offset + 96, 0)
            # print(bytes(self._shared_memory.buf[0:120]))

            self.free_memory_search_start = self.read_free_memory_search_start()
            data_size: int = self.get_data_size()
            if self._zero_mem:
                zero_memory(self.base_address, self.free_memory_search_start, data_size)
            
            write_uint64(self.base_address, self.free_memory_search_start + 0, 0)
            write_uint64(self.base_address, self.free_memory_search_start + 8, data_size - 16)

            self.set_creator_ready()

            # print(bytes(self._shared_memory.buf[0:120]))
            self.get_data_end_offset()
            if self._create:
                self._initiated = True
            
        full_memory_barrier()
    
    async def _default_asleep_func(self):
        await asyncio.sleep(0)
    
    @property
    def size(self) -> int:
        return self._size

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def create(self) -> bool:
        return self._create
    
    def _init_post_mem(self):
        self.base_address = ctypes.addressof(ctypes.c_char.from_buffer(self._shared_memory.buf))
        self.sys_values_offset = 0
        # if create:
        #     print(f'Creator: {self.base_address=}')
        # else:
        #     print(f'Consumer: {self.base_address=}')

        # self._shared_memory_bytearray = bytearray(self._shared_memory.buf)

        # self.sys_arr = np.ndarray((self.global_sys_array_len,), dtype=np.uint64, buffer=self._shared_memory.buf)
        # if DEBUG:
        #     self.log_arr = np.ndarray((500,), dtype=np.uint64, buffer=self._shared_memory.buf)
        # else:
        #     self.log_arr = self.sys_arr
    
    def init_consumer(self, time_limit: Optional[RationalNumber] = None) -> bool:
        if self._initiated:
            return

        if not self.wait_shared_memory_ready(time_limit):
            return False
        
        if (self._size is None) or (0 == self._size):
            size: int = self.global_sys_area_size
        else:
            size = self._size

        self._shared_memory: MultiprocessingSharedMemory = MultiprocessingSharedMemory(name=self._name, create=self._create, size=size)
        self._init_post_mem()
        self.wait_creator_ready()
        
        if self._size is None:
            self._size = read_uint64(self.base_address, self.sys_values_offset + 0)
            self._shared_memory.close()
            self._shared_memory: MultiprocessingSharedMemory = MultiprocessingSharedMemory(name=self._name, create=self._create, size=self._size)
        
        self._init_post_mem()
        self.free_memory_search_start = self.read_free_memory_search_start()
        
        self.set_consumer_ready()

        # print(bytes(self._shared_memory.buf[0:120]))
        self.get_data_end_offset()
        self._initiated = True
        full_memory_barrier()
    
    async def ainit_consumer(self, time_limit: Optional[RationalNumber] = None) -> bool:
        if self._initiated:
            return

        if not await self.await_shared_memory_ready(time_limit):
            return False
        
        if (self._size is None) or (0 == self._size):
            size: int = self.global_sys_area_size
        else:
            size = self._size

        self._shared_memory: MultiprocessingSharedMemory = MultiprocessingSharedMemory(name=self._name, create=self._create, size=size)
        self._init_post_mem()
        await self.await_creator_ready(time_limit)
        
        if self._size is None:
            self._size = read_uint64(self.base_address, self.sys_values_offset + 0)
            self._shared_memory.close()
            self._shared_memory: MultiprocessingSharedMemory = MultiprocessingSharedMemory(name=self._name, create=self._create, size=self._size)
        
        self._init_post_mem()
        self.free_memory_search_start = self.read_free_memory_search_start()
        
        self.set_consumer_ready()

        # print(bytes(self._shared_memory.buf[0:120]))
        self.get_data_end_offset()
        self._initiated = True
        full_memory_barrier()
    
    def close_consumer(self):
        self.set_consumer_closed()
        full_memory_barrier()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.proper_close()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.aproper_close()
    
    def close(self):
        self._shared_memory.close()
        if self._create:
            self._shared_memory.unlink()
            SharedMemory.unlink_by_name(self._name)
        else:
            if 'posix' == os.name:
                try:
                    from multiprocessing import resource_tracker
                    shm_name = f'/{self._name}'
                    resource_tracker.unregister(shm_name, "shared_memory")
                except FileNotFoundError:
                    pass

    def proper_close(self):
        if self._create:
            self.wait_consumer_closed(self._creator_destroy_timeout)
        else:
            self.close_consumer()
        
        self.close()

    async def aproper_close(self):
        if self._create:
            await self.await_consumer_closed(self._creator_destroy_timeout)
        else:
            self.close_consumer()
        
        self.close()

    @staticmethod
    def unlink_by_name(shared_memory_name: str):
        """`multiprocessing.SharedMemory` requires this cleanup in order to handle the case 
            when the previous run of the program was terminated unexpectedly

        Args:
            shared_memory_name (str): _description_
        """        
        if 'posix' == os.name:
            try:
                import _posixshmem
                from multiprocessing import resource_tracker
                shm_name = f'/{shared_memory_name}'
                _posixshmem.shm_unlink(shm_name)
                resource_tracker.unregister(shm_name, "shared_memory")
            except FileNotFoundError:
                pass
    
    @property
    def buf(self):
        """A memoryview of contents of the shared memory block.

        Returns:
            _type_: _description_
        """        
        return self._shared_memory.buf
    
    def mem_view(self, offset: Offset, size: Size) -> memoryview:
        return self._shared_memory.buf[offset:offset + size]
    
    def read_mem(self, offset: Offset, size: Size) -> List[int]:
        result = list()
        for i in range(size):
            result.append(read_uint8(self.base_address, offset + i))
        
        return result
    
    def print_mem(self, offset: Offset, size: Size, text: str = None):
        result = list()
        for i in range(size):
            result.append(read_uint8(self.base_address, offset + i))
        
        if text:
            print(f'{text.format(offset)}: {result}')
        else:
            print(f'{result}')
    
    def set_creator_ready(self):
        write_uint64(self.base_address, self.sys_values_offset + 88, 1)
    
    def set_consumer_ready(self):
        write_uint64(self.base_address, self.sys_values_offset + 96, 1)
    
    def set_consumer_closed(self):
        write_uint64(self.base_address, self.sys_values_offset + 96, 0)
    
    def get_creator_ready(self):
        return read_uint64(self.base_address, self.sys_values_offset + 88)
    
    def get_consumer_ready(self):
        return read_uint64(self.base_address, self.sys_values_offset + 96)

    def wait_shared_memory_ready(self, time_limit: Optional[RationalNumber] = None, periodic_sleep_time: Optional[RationalNumber] = 0.000000001) -> bool:
        start_time = cpu_clock()
        shared_memory: MultiprocessingSharedMemory = None
        while True:
            try:
                shared_memory: MultiprocessingSharedMemory = MultiprocessingSharedMemory(name=self._name, create=False)
            except FileNotFoundError as ex:
                if time_limit is not None:
                    if (cpu_clock() - start_time) > time_limit:
                        return False
                
                if periodic_sleep_time is None:
                    continue
                else:
                    sleep(periodic_sleep_time)
            finally:
                if shared_memory is not None:
                    shared_memory.close()
                    return True
        
        return False

    async def await_shared_memory_ready(self, time_limit: Optional[RationalNumber] = None) -> bool:
        start_time = cpu_clock()
        shared_memory: MultiprocessingSharedMemory = None
        while True:
            try:
                shared_memory: MultiprocessingSharedMemory = MultiprocessingSharedMemory(name=self._name, create=False)
            except FileNotFoundError as ex:
                if time_limit is not None:
                    if (cpu_clock() - start_time) > time_limit:
                        return False
                
                await self._asleep_func()
            finally:
                if shared_memory is not None:
                    shared_memory.close()
                    return True
        
        return False
    
    def wait_creator_ready(self, time_limit: Optional[RationalNumber] = None, periodic_sleep_time: Optional[RationalNumber] = 0.000000001) -> bool:
        if self._create:
            return
        
        start_time = cpu_clock()
        full_memory_barrier()
        while not read_uint64(self.base_address, self.sys_values_offset + 88):
            if time_limit is not None:
                if (cpu_clock() - start_time) > time_limit:
                    return False
            
            if periodic_sleep_time is None:
                mm_pause()
            else:
                hps_sleep(periodic_sleep_time)
            
            full_memory_barrier()
    
    async def await_creator_ready(self, time_limit: Optional[RationalNumber] = None) -> bool:
        if self._create:
            return
        
        start_time = cpu_clock()
        full_memory_barrier()
        while not read_uint64(self.base_address, self.sys_values_offset + 88):
            if time_limit is not None:
                if (cpu_clock() - start_time) > time_limit:
                    return False
            
            await self._asleep_func()
            
            full_memory_barrier()
    
    def wait_consumer_ready(self, time_limit: Optional[RationalNumber] = None, periodic_sleep_time: Optional[RationalNumber] = 0.000000001) -> bool:
        if not self._create:
            return
        
        start_time = cpu_clock()
        full_memory_barrier()
        while not read_uint64(self.base_address, self.sys_values_offset + 96):
            if time_limit is not None:
                if (cpu_clock() - start_time) > time_limit:
                    return False
            
            if periodic_sleep_time is None:
                mm_pause()
            else:
                hps_sleep(periodic_sleep_time)
            
            full_memory_barrier()
    
    async def await_consumer_ready(self, time_limit: Optional[RationalNumber] = None) -> bool:
        if not self._create:
            return
        
        start_time = cpu_clock()
        full_memory_barrier()
        while not read_uint64(self.base_address, self.sys_values_offset + 96):
            if time_limit is not None:
                if (cpu_clock() - start_time) > time_limit:
                    return False
            
            await self._asleep_func()
            
            full_memory_barrier()
    
    def wait_consumer_closed(self, time_limit: Optional[RationalNumber] = None, periodic_sleep_time: Optional[RationalNumber] = 0.000000001) -> bool:
        if not self._create:
            return
        
        start_time = cpu_clock()
        full_memory_barrier()
        while read_uint64(self.base_address, self.sys_values_offset + 96):
            if time_limit is not None:
                if (cpu_clock() - start_time) > time_limit:
                    return False
            
            if periodic_sleep_time is None:
                mm_pause()
            else:
                hps_sleep(periodic_sleep_time)
            
            full_memory_barrier()
    
    async def await_consumer_closed(self, time_limit: Optional[RationalNumber] = None) -> bool:
        if not self._create:
            return
        
        start_time = cpu_clock()
        full_memory_barrier()
        while read_uint64(self.base_address, self.sys_values_offset + 96):
            if time_limit is not None:
                if (cpu_clock() - start_time) > time_limit:
                    return False
            
            await self._asleep_func()
            
            full_memory_barrier()
    
    def creator_in_charge(self) -> bool:
        return read_uint64(self.base_address, self.sys_values_offset + 56)
    
    def consumer_in_charge(self) -> bool:
        return read_uint64(self.base_address, self.sys_values_offset + 64)
    
    def creator_wants_to_be_in_charge(self) -> bool:
        return read_uint64(self.base_address, self.sys_values_offset + 72)
    
    def consumer_wants_to_be_in_charge(self) -> bool:
        return read_uint64(self.base_address, self.sys_values_offset + 80)
    
    def read_free_memory_search_start(self) -> int:
        # return self.get_data_start_offset()
        return read_uint64(self.base_address, self.sys_values_offset + 32)
    
    def update_free_memory_search_start(self) -> int:
        self.free_memory_search_start = self.read_free_memory_search_start()
    
    def get_free_memory_search_start(self) -> int:
        # self.update_free_memory_search_start()
        return self.free_memory_search_start
    
    def write_free_memory_search_start(self, offset: Offset) -> int:
        # return
        if ((self.get_data_end_offset() - 16) < offset) or (offset < self.get_data_start_offset()):
            offset = self.get_data_start_offset()
        
        write_uint64(self.base_address, self.sys_values_offset + 32, offset)
    
    def commit_free_memory_search_start(self):
        self.write_free_memory_search_start(self.free_memory_search_start)
    
    def set_free_memory_search_start(self, offset: Offset) -> int:
        # return
        if ((self.get_data_end_offset() - 16) < offset) or (offset < self.get_data_start_offset()):
            offset = self.get_data_start_offset()
        
        self.free_memory_search_start = offset
        # self.commit_free_memory_search_start()
    
    def get_last_message_offset(self) -> Optional[Offset]:
        return read_uint64(self.base_address, self.sys_values_offset + 48)

    def set_last_message_offset(self, offset: Offset):
        write_uint64(self.base_address, self.sys_values_offset + 48, offset)
    
    def get_first_message_offset(self) -> Optional[Offset]:
        return read_uint64(self.base_address, self.sys_values_offset + 40)

    def set_first_message_offset(self, offset: Offset):
        write_uint64(self.base_address, self.sys_values_offset + 40, offset)
    
    def get_data_start_offset(self) -> Offset:
        return read_uint64(self.base_address, self.sys_values_offset + 8)

    def get_data_size(self) -> Size:
        return read_uint64(self.base_address, self.sys_values_offset + 16)
    
    def get_data_end_offset(self) -> Offset:
        result = read_uint64(self.base_address, self.sys_values_offset + 24)
        if result != len(self._shared_memory.buf):
            print(result, len(self._shared_memory.buf))
        
        return result

    # def read_uint64(self, offset: Offset) -> int:
    #     return read_uint64(self.base_address, offset)
    
    # def write_uint64(self, offset: Offset, value: int):
    #     write_uint64(self.base_address, offset, value)
    
    def read_uint64(self, offset: Offset) -> int:
        return int.from_bytes(self._shared_memory.buf[offset:offset + 8], byteorder='little', signed=False)
    
    def write_uint64(self, offset: Offset, value: int):
        self._shared_memory.buf[offset:offset + 8] = value.to_bytes(8, byteorder='little', signed=False)
    
    # def read_uint32(self, offset: Offset) -> int:
    #     return int.from_bytes(self._shared_memory.buf[offset:offset + 4], byteorder='little', signed=False)
    
    # def write_uint32(self, offset: Offset, value: int):
    #     self._shared_memory.buf[offset:offset + 4] = value.to_bytes(4, byteorder='little', signed=False)
    
    # def read_uint16(self, offset: Offset) -> int:
    #     return int.from_bytes(self._shared_memory.buf[offset:offset + 2], byteorder='little', signed=False)
    
    # def write_uint16(self, offset: Offset, value: int):
    #     self._shared_memory.buf[offset:offset + 2] = value.to_bytes(2, byteorder='little', signed=False)
    
    # def read_uint8(self, offset: Offset) -> int:
    #     return int.from_bytes(self._shared_memory.buf[offset:offset + 1], byteorder='little', signed=False)
    
    # def write_uint8(self, offset: Offset, value: int):
    #     self._shared_memory.buf[offset:offset + 1] = value.to_bytes(1, byteorder='little', signed=False)
    
    # def read_int64(self, offset: Offset) -> int:
    #     return int.from_bytes(self._shared_memory.buf[offset:offset + 8], byteorder='little', signed=True)
    
    # def write_int64(self, offset: Offset, value: int):
    #     self._shared_memory.buf[offset:offset + 8] = value.to_bytes(8, byteorder='little', signed=True)
    
    # def read_int32(self, offset: Offset) -> int:
    #     return int.from_bytes(self._shared_memory.buf[offset:offset + 4], byteorder='little', signed=True)
    
    # def write_int32(self, offset: Offset, value: int):
    #     self._shared_memory.buf[offset:offset + 4] = value.to_bytes(4, byteorder='little', signed=True)
    
    # def read_int16(self, offset: Offset) -> int:
    #     return int.from_bytes(self._shared_memory.buf[offset:offset + 2], byteorder='little', signed=True)
    
    # def write_int16(self, offset: Offset, value: int):
    #     self._shared_memory.buf[offset:offset + 2] = value.to_bytes(2, byteorder='little', signed=True)

    # def read_int8(self, offset: Offset) -> int:
    #     return int.from_bytes(self._shared_memory.buf[offset:offset + 1], byteorder='little', signed=True)
    
    # def write_int8(self, offset: Offset, value: int):
    #     self._shared_memory.buf[offset:offset + 1] = value.to_bytes(1, byteorder='little', signed=True)

    # def read_float(self, offset: Offset) -> float:
    #     return float.from_bytes(self._shared_memory.buf[offset:offset + 4], byteorder='little', signed=False)
    
    # def write_float(self, offset: Offset, value: float):
    #     self._shared_memory.buf[offset:offset + 4] = value.to_bytes(4, byteorder='little', signed=False)

    # def read_double(self, offset: Offset) -> float:
    #     return float.from_bytes(self._shared_memory.buf[offset:offset + 8], byteorder='little', signed=False)
    
    # def write_double(self, offset: Offset, value: float):
    #     self._shared_memory.buf[offset:offset + 8] = value.to_bytes(8, byteorder='little', signed=False)
    
    # def read_complex(self, offset: Offset) -> complex:
    #     return complex.from_bytes(self._shared_memory.buf[offset:offset + 16], byteorder='little', signed=False)
    
    # def write_complex(self, offset: Offset, value: complex):
    #     self._shared_memory.buf[offset:offset + 16] = value.to_bytes(16, byteorder='little', signed=False)
    
    # def read_bool(self, offset: Offset) -> bool:
    #     return bool.from_bytes(self._shared_memory.buf[offset:offset + 1], byteorder='little', signed=False)
    
    # def write_bool(self, offset: Offset, value: bool):
    #     self._shared_memory.buf[offset:offset + 1] = value.to_bytes(1, byteorder='little', signed=False)
    
    # def read_str(self, offset: Offset) -> str:
    #     size = read_uint64(self.base_address, offset)
    #     return self._shared_memory.buf[offset + 8:offset + 8 + size].decode()
    
    # def read_str_2(self, offset: Offset, size: Size) -> str:
    #     return self._shared_memory.buf[offset + 8:offset + 8 + size].decode()
    
    # def write_str(self, offset: Offset, value: str):
    #     size = len(value)
    #     write_uint64(self.base_address, offset, size)
    #     self._shared_memory.buf[offset + 8:offset + 8 + size] = value.encode()
    
    # def read_bytes(self, offset: Offset) -> bytes:
    #     size = read_uint64(self.base_address, offset)
    #     return self._shared_memory.buf[offset + 8:offset + 8 + size]

    # def read_bytes_2(self, offset: Offset, size: Size) -> bytes:
    #     return self._shared_memory.buf[offset + 8:offset + 8 + size]
    
    # def write_bytes(self, offset: Offset, value: bytes):
    #     size = len(value)
    #     write_uint64(self.base_address, offset, size)
    #     self._shared_memory.buf[offset + 8:offset + 8 + size] = value
    
    # def read_bytearray(self, offset: Offset) -> bytearray:
    #     size = read_uint64(self.base_address, offset)
    #     return bytearray(self._shared_memory.buf[offset + 8:offset + 8 + size])
    
    # def read_bytearray_2(self, offset: Offset, size: Size) -> bytearray:
    #     return bytearray(self._shared_memory.buf[offset + 8:offset + 8 + size])
    
    # def write_bytearray(self, offset: Offset, value: bytearray):
    #     size = len(value)
    #     write_uint64(self.base_address, offset, size)
    #     self._shared_memory.buf[offset + 8:offset + 8 + size] = value
    
    # def read_tuple(self, offset: Offset) -> tuple:
    #     size = read_uint64(self.base_address, offset)
    #     return tuple(self._shared_memory.buf[offset + 8:offset + 8 + size])
    
    # def write_tuple(self, offset: Offset, value: tuple):
    #     size = len(value)
    #     write_uint64(self.base_address, offset, size)
    #     self._shared_memory.buf[offset + 8:offset + 8 + size] = value
    
    # def read_list(self, offset: Offset) -> list:
    #     size = read_uint64(self.base_address, offset)
    #     return list(self._shared_memory.buf[offset + 8:offset + 8 + size])
    
    # def write_list(self, offset: Offset, value: list):
    #     size = len(value)
    #     write_uint64(self.base_address, offset, size)
    #     self._shared_memory.buf[offset + 8:offset + 8 + size] = value

    # def read_dict(self, offset: Offset) -> dict:
    #     size = read_uint64(self.base_address, offset)
    #     return dict(self._shared_memory.buf[offset + 8:offset + 8 + size])
    
    # def write_dict(self, offset: Offset, value: dict):
    #     size = len(value)
    #     write_uint64(self.base_address, offset, size)
    #     self._shared_memory.buf[offset + 8:offset + 8 + size] = value
    
    # def read_set(self, offset: Offset) -> set:
    #     size = read_uint64(self.base_address, offset)
    #     return set(self._shared_memory.buf[offset + 8:offset + 8 + size])
    
    # def write_set(self, offset: Offset, value: set):
    #     size = len(value)
    #     write_uint64(self.base_address, offset, size)
    #     self._shared_memory.buf[offset + 8:offset + 8 + size] = value
    
    # def read_pickable(self, offset: Offset) -> Any:
    #     size = read_uint64(self.base_address, offset)
    #     return pickle.loads(self._shared_memory.buf[offset + 8:offset + 8 + size])
    
    # def write_pickable(self, offset: Offset, value: Any):
    #     value_bytes = pickle.dumps(value)
    #     size = len(value_bytes)
    #     write_uint64(self.base_address, offset, size)
    #     self._shared_memory.buf[offset + 8:offset + 8 + size] = value_bytes

    # ----------------------------
    
    def read_obj_type_and_size(self, offset: Offset) -> Tuple[ObjectType, Size]:
        obj_type = ObjectType(read_uint64(self.base_address, offset + 0))
        size = read_uint64(self.base_address, offset + 8)
        return obj_type, size
    
    def write_obj_type_and_size(self, offset: Offset, obj_type: ObjectType, size: Size):
        write_uint64(self.base_address, offset + 0, obj_type.value)
        write_uint64(self.base_address, offset + 8, size)
        return offset + 16

    # ----------------------------
    
    def test_free_memory_blocks(self, offset: Offset, desired_size: Size, data_end_offset: Offset) -> Tuple[bool, Size, Offset]:
        adjusted_size = desired_size
        initial_offset = offset
        sum_size = 0
        max_viable_offset = data_end_offset - 16
        last_found_obj_offset = None
        last_found_obj_size = None
        while True:
            last_found_obj_offset = offset
            try:
                obj_type = ObjectType(read_uint64(self.base_address, offset))
            except ValueError:
                print(f'Error: {offset=}, {desired_size=}, {sum_size=}')
            
            size = read_uint64(self.base_address, offset + 8)
            if size % 8:
                print(f'WRONG SIZE {obj_type=} {size=} {offset=} {desired_size=} {data_end_offset=}')
                self.print_mem(offset - 8 * 10, 8 * 10, 'WRONG SIZE - before')
                self.print_mem(offset, 8 * 10, 'WRONG SIZE - after')
                raise RuntimeError(f'WRONG SIZE: {size=}, {offset=}, {obj_type=}')
            
            last_found_obj_size = 16 + size
            next_block_offset = last_found_obj_offset + last_found_obj_size
            if next_block_offset > data_end_offset:
                print(f'{next_block_offset=}, {data_end_offset=}, {len(self._shared_memory.buf)=}')
                return False, adjusted_size, None, None, next_block_offset

            if obj_type is not ObjectType.tfree_memory:
                return False, adjusted_size, None, None, next_block_offset

            sum_size = next_block_offset - initial_offset

            if sum_size == desired_size:
                return True, adjusted_size, None, None, next_block_offset

            if sum_size > desired_size:
                new_next_block_offset = initial_offset + desired_size
                new_next_block_size = last_found_obj_size - (new_next_block_offset - last_found_obj_offset)
                if new_next_block_size < 16:
                    adjusted_size = desired_size + new_next_block_size
                    return True, adjusted_size, None, None, next_block_offset
                else:
                    return True, adjusted_size, new_next_block_offset, new_next_block_size, new_next_block_offset

            offset = last_found_obj_offset + last_found_obj_size
            if offset > max_viable_offset:
                return False, adjusted_size, None, None, next_block_offset

    def combine_free_memory_blocks(self, free_mem_block_offset: Offset, size: Size, last_free_block_offset: Offset, last_free_block_new_size: Size, next_block_offset: Offset, mark_block: bool = False) -> Tuple[Size, Offset]:
        if mark_block:
            self.write_obj_type_and_size(free_mem_block_offset, ObjectType.tfree_memory, size - 16)
        
        if last_free_block_offset is not None:
            if last_free_block_new_size - 16 < 0:
                print(f'Error: {last_free_block_new_size=}')
            
            self.write_obj_type_and_size(last_free_block_offset, ObjectType.tfree_memory, last_free_block_new_size - 16)
        
        # self.set_free_memory_search_start(next_block_offset)

    # ----------------------------
    
    def malloc(self, obj_type: ObjectType, size: Size, loop_allowed: bool = True, zero_mem: bool = False) -> Tuple[Optional[Offset], Size]:
        start_time = cpu_clock()
        try:
            size += 16
            size = nearest_size(size)
            adjusted_size = size
            initial_start_offset = self.get_free_memory_search_start()
            data_end_offset: Offset = self.get_data_end_offset()
            search_end_offset = data_end_offset - 16
            start_offset = initial_start_offset
            free_mem_block_offset: Offset = None
            last_free_block_offset: Offset = None
            last_free_block_new_size: Size = None
            found: bool = False
            sum_size: Size = 0
            while (not found) and (start_offset <= search_end_offset):
                free_mem_block_offset = start_offset
                found, adjusted_size, last_free_block_offset, last_free_block_new_size, next_block_offset = self.test_free_memory_blocks(start_offset, size, data_end_offset)
                start_offset = next_block_offset
            
            if (not found) and loop_allowed:
                start_offset = self.get_data_start_offset()
                search_end_offset = initial_start_offset - 16
                while (not found) and (start_offset <= search_end_offset):
                    free_mem_block_offset = start_offset
                    found, adjusted_size, last_free_block_offset, last_free_block_new_size, next_block_offset = self.test_free_memory_blocks(start_offset, size, data_end_offset)
                    start_offset = next_block_offset

            if not found:
                raise FreeMemoryChunkNotFoundError(obj_type, size, loop_allowed, zero_mem)
            
            self.combine_free_memory_blocks(free_mem_block_offset, adjusted_size, last_free_block_offset, last_free_block_new_size, next_block_offset)
            obj_size = adjusted_size - 16
            self.write_obj_type_and_size(free_mem_block_offset, obj_type, obj_size)
            if zero_mem:
                # print(f'Zeroing memory 1: {free_mem_block_offset=}, {result_size=}')
                # hps_sleep(0.01)
                zero_memory(self.base_address, free_mem_block_offset + 16, obj_size)

            if free_mem_block_offset % 8:
                print(f'Error: {free_mem_block_offset=}, {obj_size=}')
                
        
            self.set_free_memory_search_start(free_mem_block_offset)
            return free_mem_block_offset, obj_size
        finally:
            self._malloc_time += cpu_clock() - start_time
    
    # def zero_memory(self, offset: Offset, size: Size):
    #     # print(f'Zeroing memory 1: [{self.base_address + offset}:{self.base_address + offset + size}], {size=}')
    #     self._shared_memory_bytearray[offset:offset + size] = bytearray(size)
    
    def calloc(self, obj_type: ObjectType, size: Size, num: int, loop_allowed: bool = True, zero_mem: bool = True) -> Tuple[Optional[Offset], Size]:
        return self.malloc(obj_type, size * num, loop_allowed, zero_mem)
    
    def realloc(self, obj_offset: Offset, new_size: int, loop_allowed: bool = True, zero_mem: bool = True) -> Tuple[Optional[Offset], Size]:
        start_time: float = cpu_clock()
        internal_malloc_time: float = 0.0
        try:
            new_size += 16
            new_size = nearest_size(new_size)
            data_end_offset: Offset = self.get_data_end_offset()
            result_offset: Offset = None
            result_obj_size: Size = 0
            original_obj_size = read_uint64(self.base_address, obj_offset + 8)
            size = original_obj_size + 16
            next_obj_offset = obj_offset + size
            free_mem_block_offset = next_obj_offset
            dsize = new_size - size
            found, additional_adjusted_size, last_free_block_offset, last_free_block_new_size, next_block_offset = self.test_free_memory_blocks(free_mem_block_offset, dsize, data_end_offset)
            if found:
                self.combine_free_memory_blocks(free_mem_block_offset, additional_adjusted_size, last_free_block_offset, last_free_block_new_size, next_block_offset)
                if zero_mem:
                    # print(f'Zeroing memory 3: {free_mem_block_offset=}, {result_size=}')
                    # hps_sleep(0.01)
                    zero_memory(self.base_address, free_mem_block_offset, dsize)
                
                result_obj_size = new_size - 16
                write_uint64(self.base_address, obj_offset + 8, result_obj_size)
                self.set_free_memory_search_start(obj_offset)
                result_offset = obj_offset
            else:
                internal_malloc_start_time: float = cpu_clock()
                new_offset, result_obj_size = self.malloc(ObjectType(read_uint64(self.base_address, obj_offset + 0)), new_size, loop_allowed)
                internal_malloc_time += cpu_clock() - internal_malloc_start_time
                if new_offset is None:
                    return None, 0

                self._shared_memory.buf[new_offset + 16:new_offset + 16 + size] = self._shared_memory.buf[obj_offset + 16:obj_offset + 16 + size]
                if zero_mem:
                    # print(f'Zeroing memory 4: {new_offset=}, {new_size=}')
                    # hps_sleep(0.01)
                    zero_memory(self.base_address, new_offset + 16 + original_obj_size, result_obj_size - original_obj_size)
                
                self.free(obj_offset)
                result_offset = new_offset
            
            return result_offset, result_obj_size
        finally:
            self._realloc_time += cpu_clock() - start_time - internal_malloc_time
    
    def free(self, offset: Offset) -> bool:
        write_uint64(self.base_address, offset, 0)
        return True

    # ----------------------------
    
    def put_obj(self, obj: Any):
        obj_type = self._get_obj_type(obj)
        codec = codec_by_type[obj_type]
        mapped_obj, offset, size = codec.map_to_shared_memory(self, obj)
        return mapped_obj, offset, size

    def get_obj(self, offset: int) -> Any:
        # print(f'get_obj: {offset=}')
        obj_type = ObjectType(read_uint64(self.base_address, offset))
        if obj_type is ObjectType.tfree_memory:
            # self.print_mem(offset - 32, 96, 'get_obj [offset - 32: offset + 64]. {}')
            raise RuntimeError
        
        codec = codec_by_type[obj_type]
        return codec.init_from_shared_memory(self, offset)

    def get_obj_buffer(self, offset: int) -> memoryview:
        # print(f'get_obj: {offset=}')
        obj_type = ObjectType(read_uint64(self.base_address, offset))
        if obj_type is ObjectType.tfree_memory:
            # self.print_mem(offset - 32, 96, 'get_obj [offset - 32: offset + 64]. {}')
            raise RuntimeError
        
        codec = codec_by_type[obj_type]
        return codec.buffer(self, offset)

    def get_obj_buffer_2(self, offset: int) -> Tuple[int, int]:
        # print(f'get_obj: {offset=}')
        obj_type = ObjectType(read_uint64(self.base_address, offset))
        if obj_type is ObjectType.tfree_memory:
            # self.print_mem(offset - 32, 96, 'get_obj [offset - 32: offset + 64]. {}')
            raise RuntimeError
        
        codec = codec_by_type[obj_type]
        return codec.buffer_2(self, offset)

    def get_obj_mem_view(self, offset: int) -> memoryview:
        return self.mem_view(*self.get_obj_buffer_2(offset))

    def destroy_obj(self, offset: int) -> Any:
        obj_type = ObjectType(read_uint64(self.base_address, offset))
        codec = codec_by_type[obj_type]
        return codec.destroy(self, offset)

    # ----------------------------

    def map_object(self, obj: Any) -> Any:
        # self.update_free_memory_search_start()
        mapped_obj, offset, size = self.put_obj(obj)
        # self.commit_free_memory_search_start()
        return mapped_obj

    def get_object(self, offset: Offset) -> Any:
        return self.get_obj(offset)

    def destroy_object(self, offset: Offset) -> Any:
        return self.destroy_obj(offset)

    # ----------------------------

    def write_message(self, obj: Any) -> Tuple[Any, Offset, Offset]:
        # self.update_free_memory_search_start()
        message_offset, message_real_size = self.malloc(ObjectType.tmessage, 24)
        try:
            mapped_obj, offset, size = self.put_obj(obj)
            # self.commit_free_memory_search_start()
            last_message_offset: Offset = self.get_last_message_offset()
            if last_message_offset:
                write_uint64(self.base_address, last_message_offset + 16 + 8, message_offset)
            else:
                self.set_first_message_offset(message_offset)
            
            write_uint64(self.base_address, message_offset + 16 + 0, last_message_offset)
            write_uint64(self.base_address, message_offset + 16 + 8, 0)
            write_uint64(self.base_address, message_offset + 16 + 16, offset)
            self.set_last_message_offset(message_offset)
        except:
            self.free(message_offset)
            raise

        return mapped_obj, offset, message_offset

    def put_message(self, obj: Any) -> Any:
        mapped_obj, offset, message_offset = self.write_message(obj)
        return mapped_obj
    
    def put_message_2(self, obj: Any) -> Tuple[Any, Offset]:
        mapped_obj, offset, message_offset = self.write_message(obj)
        return mapped_obj, offset

    def has_messages(self) -> bool:
        return self.get_last_message_offset() != 0

    def read_message_info(self, queue_type: QueueType = QueueType.fifo) -> Tuple[Any, Optional[Offset], Optional[Offset]]:
        # print(0)
        if QueueType.fifo == queue_type:
            message_offset = self.get_first_message_offset()
            # print(f'0.0| {message_offset=}')
            if not message_offset:
                return None, None, None
            
            next_message_offset = read_uint64(self.base_address, message_offset + 16 + 8)
            self.set_first_message_offset(next_message_offset)
            if next_message_offset:
                write_uint64(self.base_address, next_message_offset + 16 + 0, 0)
            else:
                self.set_last_message_offset(0)
        else:
            message_offset = self.get_last_message_offset()
            # print(f'0.1| {message_offset=}')
            if not message_offset:
                return None, None, None
            
            prev_message_offset = read_uint64(self.base_address, message_offset + 16 + 0)
            self.set_last_message_offset(prev_message_offset)
            if prev_message_offset:
                write_uint64(self.base_address, prev_message_offset + 16 + 8, 0)
            else:
                self.set_first_message_offset(0)
        
        # print(1)
        obj_offset = read_uint64(self.base_address, message_offset + 16 + 16)
        # print(2)
        if not obj_offset:
            return None, None, message_offset

        # print(3)
        obj = self.get_obj(obj_offset)
        # print(4)
        return obj, obj_offset, message_offset

    def destroy_message(self, message_offset: Offset):
        if not message_offset:
            return
        
        # obj_offset = read_uint64(self.base_address, message_offset + 16 + 16)
        # if obj_offset:
        #     self.destroy_obj(obj_offset)
        
        # self.destroy_obj(message_offset)

        self.free(message_offset)
    
    def read_message(self, queue_type: QueueType = QueueType.fifo) -> Any:
        obj, obj_offset, message_offset = self.read_message_info(queue_type)
        if message_offset:
            return obj
        else:
            raise NoMessagesInQueueError
    
    def read_message_2(self, queue_type: QueueType = QueueType.fifo) -> Tuple[Any, Offset]:
        obj, obj_offset, message_offset = self.read_message_info(queue_type)
        if message_offset:
            return obj, obj_offset
        else:
            raise NoMessagesInQueueError

    def take_message(self, queue_type: QueueType = QueueType.fifo) -> Any:
        obj, obj_offset, message_offset = self.read_message_info(queue_type)
        if message_offset:
            self.destroy_message(message_offset)
        else:
            raise NoMessagesInQueueError
        
        return obj

    def take_message_2(self, queue_type: QueueType = QueueType.fifo) -> Tuple[Any, Offset]:
        obj, obj_offset, message_offset = self.read_message_info(queue_type)
        if message_offset:
            self.destroy_message(message_offset)
        else:
            raise NoMessagesInQueueError
        
        return obj, obj_offset
    
    def get_message(self, default = None, queue_type: QueueType = QueueType.fifo) -> Any:
        obj, obj_offset, message_offset = self.read_message_info(queue_type)
        if message_offset:
            return obj
        else:
            return default
    
    def get_message_2(self, default = None, queue_type: QueueType = QueueType.fifo) -> Tuple[Any, Optional[Offset]]:
        obj, obj_offset, message_offset = self.read_message_info(queue_type)
        if message_offset:
            return obj, obj_offset
        else:
            return default, None

    def pop_message(self, default = None, queue_type: QueueType = QueueType.fifo) -> Any:
        obj, obj_offset, message_offset = self.read_message_info(queue_type)
        if message_offset:
            self.destroy_message(message_offset)
        else:
            obj = default
        
        return obj

    def pop_message_2(self, default = None, queue_type: QueueType = QueueType.fifo) -> Tuple[Any, Optional[Offset]]:
        obj, obj_offset, message_offset = self.read_message_info(queue_type)
        if message_offset:
            self.destroy_message(message_offset)
        else:
            obj = default
            obj_offset = None
        
        return obj, obj_offset

    # ----------------------------

    def get_in_line(self) -> bool:
        if self._create:
            write_uint64(self.base_address, self.sys_values_offset + 56, 0)
            write_uint64(self.base_address, self.sys_values_offset + 72, 1)
            full_memory_barrier()
            if self.consumer_in_charge():
                return False
            else:
                write_uint64(self.base_address, self.sys_values_offset + 56, 1)
                full_memory_barrier()
                write_uint64(self.base_address, self.sys_values_offset + 72, 0)
                full_memory_barrier()
                self.update_free_memory_search_start()
                if self.consumer_in_charge():
                    write_uint64(self.base_address, self.sys_values_offset + 56, 0)
                    full_memory_barrier()
                    write_uint64(self.base_address, self.sys_values_offset + 72, 1)
                    full_memory_barrier()
                    return False

                return True
        else:
            write_uint64(self.base_address, self.sys_values_offset + 64, 0)
            write_uint64(self.base_address, self.sys_values_offset + 80, 1)
            full_memory_barrier()
            if self.creator_in_charge():
                return False
            else:
                write_uint64(self.base_address, self.sys_values_offset + 64, 1)
                full_memory_barrier()
                write_uint64(self.base_address, self.sys_values_offset + 80, 0)
                full_memory_barrier()
                self.update_free_memory_search_start()
                if self.creator_in_charge():
                    write_uint64(self.base_address, self.sys_values_offset + 64, 0)
                    full_memory_barrier()
                    write_uint64(self.base_address, self.sys_values_offset + 80, 1)
                    full_memory_barrier()
                    return False
                
                return True
            
    def release(self):
        self.commit_free_memory_search_start()
        if self._create:
            write_uint64(self.base_address, self.sys_values_offset + 56, 0)
            write_uint64(self.base_address, self.sys_values_offset + 72, 0)
            full_memory_barrier()
        else:
            write_uint64(self.base_address, self.sys_values_offset + 64, 0)
            write_uint64(self.base_address, self.sys_values_offset + 80, 0)
            full_memory_barrier()

    def wait_my_turn(self, time_limit: Optional[RationalNumber] = None, periodic_sleep_time: Optional[RationalNumber] = 0.000000001) -> bool:
        start_time = cpu_clock()
        while not self.get_in_line():
            if time_limit is not None:
                if (cpu_clock() - start_time) > time_limit:
                    return False
            
            if periodic_sleep_time is None:
                mm_pause()
            else:
                hps_sleep(periodic_sleep_time)
        
        return True

    async def await_my_turn(self, time_limit: Optional[RationalNumber] = None) -> bool:
        start_time = cpu_clock()
        while not self.get_in_line():
            if time_limit is not None:
                if (cpu_clock() - start_time) > time_limit:
                    return False
            
            await self._asleep_func()
        
        return True

    # ----------------------------

    def wait_for_messages(self, time_limit: Optional[RationalNumber] = None, periodic_sleep_time: Optional[RationalNumber] = 0.000000001) -> bool:
        start_time = cpu_clock()
        has_messages = False
        while not has_messages:
            if time_limit is not None:
                if (cpu_clock() - start_time) > time_limit:
                    return False
            
            if periodic_sleep_time is None:
                mm_pause()
            else:
                hps_sleep(periodic_sleep_time)

            with wait_my_turn(self):
                has_messages = self.has_messages()
        
        return True

    async def await_for_messages(self, time_limit: Optional[RationalNumber] = None) -> bool:
        start_time = cpu_clock()
        has_messages = False
        while not has_messages:
            if time_limit is not None:
                if (cpu_clock() - start_time) > time_limit:
                    return False
            
            await self._asleep_func()

            with await_my_turn(self, time_limit):
                has_messages = self.has_messages()
        
        return True

    # ----------------------------

    @staticmethod
    def _get_obj_type(obj: Any) -> ObjectType:
        obj_type = type(obj)
        if obj is None:
            obj_type_atom: ObjectType = ObjectType.tnone
        elif obj_type is bool:
            obj_type_atom = ObjectType.tbool
        elif obj_type is int:
            obj_type_atom = ObjectType.tint
        elif obj_type is float:
            obj_type_atom = ObjectType.tfloat
        elif obj_type is complex:
            obj_type_atom = ObjectType.tcomplex
        elif obj_type is slice:
            obj_type_atom = ObjectType.tslice
        elif obj_type is str:
            obj_type_atom = ObjectType.tstr
        elif obj_type is bytes:
            obj_type_atom = ObjectType.tbytes
        elif obj_type is bytearray:
            obj_type_atom = ObjectType.tbytearray
        elif obj_type is tuple:
            obj_type_atom = ObjectType.ttuple
        elif obj_type is list:
            obj_type_atom = ObjectType.tlist
        elif issubclass(obj_type, FastLimitedSet):
            obj_type_atom = ObjectType.tfastset
        elif issubclass(obj_type, AbsMutableSet):
            obj_type_atom = ObjectType.tmutableset
        elif issubclass(obj_type, AbsSet):
            obj_type_atom = ObjectType.tset
        elif issubclass(obj_type, FastLimitedDict):
            obj_type_atom = ObjectType.tfastdict
        elif issubclass(obj_type, ForceMapping):
            obj_type_atom = ObjectType.tmapping
        elif issubclass(obj_type, AbsMutableMapping):
            obj_type_atom = ObjectType.tmutablemapping
        elif issubclass(obj_type, AbsMapping):
            obj_type_atom = ObjectType.tmapping
        elif obj_type is SmallInt:
            obj_type_atom = ObjectType.tsmallint
        elif obj_type is BigInt:
            obj_type_atom = ObjectType.tbigint
        elif issubclass(obj_type, Tensor):
            obj_type_atom = ObjectType.ttorchtensor
        elif issubclass(obj_type, np.ndarray):
            obj_type_atom = ObjectType.tnumpyndarray
        elif issubclass(obj_type, (ForceGeneralObjectCopy, ForceGeneralObjectInplace)):
            obj_type_atom = ObjectType.tgeneralobject
        elif issubclass(obj_type, (ForceStaticObjectCopy, ForceStaticObjectInplace)):
            obj_type_atom = ObjectType.tstaticobject
        elif obj_type in obj_type_map:
            obj_type_atom = obj_type_map[obj_type]
        # elif hasattr(obj, '__dict__'):
        #     obj_type_atom = ObjectType.tgeneralobject
        # else:
        #     obj_type_atom = ObjectType.tpickable
        else:
            # obj_type_atom = ObjectType.tgeneralobject
            obj_type_atom = ObjectType.tstaticobject
        
        return obj_type_atom


# @contextmanager
# def get_in_line(shared_memory: SharedMemory):
#     shared_memory.get_in_line()
#     try:
#         yield
#     finally:
#         shared_memory.release()


class GetInLine:
    def __init__(self, shared_memory: SharedMemory):
        self.shared_memory: SharedMemory = shared_memory
    
    def __enter__(self):
        self.shared_memory.get_in_line()
        return
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.shared_memory.release()


get_in_line = GetInLine


# @contextmanager
# def wait_my_turn(shared_memory: SharedMemory, time_limit: Optional[RationalNumber] = None, periodic_sleep_time: Optional[RationalNumber] = 0.000000001):
#     shared_memory.wait_my_turn(time_limit, periodic_sleep_time)
#     try:
#         yield
#     finally:
#         shared_memory.release()


class WaitMyTurn:
    def __init__(self, shared_memory: SharedMemory, time_limit: Optional[RationalNumber] = None, periodic_sleep_time: Optional[RationalNumber] = 0.000000001):
        self.shared_memory: SharedMemory = shared_memory
        self.time_limit: Optional[RationalNumber] = time_limit
        self.periodic_sleep_time: Optional[RationalNumber] = periodic_sleep_time
    
    def __enter__(self):
        self.shared_memory.wait_my_turn(self.time_limit, self.periodic_sleep_time)
        return
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.shared_memory.release()


wait_my_turn = WaitMyTurn


# @contextmanager
# def wait_my_turn_when_has_messages(shared_memory: SharedMemory, time_limit: Optional[RationalNumber] = None, periodic_sleep_time: Optional[RationalNumber] = 0.000000001):
#     while True:
#         if not shared_memory.wait_my_turn(time_limit, periodic_sleep_time):
#             raise OperationTimedOutError
        
#         try:
#             if not shared_memory.has_messages():
#                 continue

#             yield
#             break
#         finally:
#             shared_memory.release()


class WaitMyTurnWhenHasMessages:
    def __init__(self, shared_memory: SharedMemory, time_limit: Optional[RationalNumber] = None, periodic_sleep_time: Optional[RationalNumber] = 0.000000001):
        self.shared_memory: SharedMemory = shared_memory
        self.time_limit: Optional[RationalNumber] = time_limit
        self.periodic_sleep_time: Optional[RationalNumber] = periodic_sleep_time
    
    def __enter__(self):
        while True:
            if not self.shared_memory.wait_my_turn(self.time_limit, self.periodic_sleep_time):
                raise OperationTimedOutError
            
            if self.shared_memory.has_messages():
                return
            else:
                self.shared_memory.release()
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.shared_memory.release()


wait_my_turn_when_has_messages = WaitMyTurnWhenHasMessages


class await_my_turn:
    def __init__(self, shared_memory: SharedMemory, time_limit: Optional[RationalNumber] = None):
        self.shared_memory: SharedMemory = shared_memory
        self.time_limit: Optional[RationalNumber] = time_limit
    
    async def __aenter__(self):
        await self.shared_memory.await_my_turn(self.time_limit)
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.shared_memory.release()


def numpy_array_memory_size(np_shape, np_dtype):
    num_elements = np.prod(np_shape)
    element_size = np.dtype(np_dtype).itemsize
    memory_size_bytes = num_elements * element_size
    return memory_size_bytes


def numpy_array_made_from_pointer_memory_size(np_shape, ctypes_type) -> int:
    num_elements: int = np.prod(np_shape)
    element_size: int = ctypes.sizeof(ctypes_type)
    memory_size_bytes: int = num_elements * element_size
    return memory_size_bytes


from ctypes import _SimpleCData

def make_numpy_array_from_obj_offset(shared_memory: SharedMemory, offset: Offset, np_shape, np_dtype_or_ctypes_type = None) -> Any:
    if np_dtype_or_ctypes_type is None:
        np_dtype_or_ctypes_type = ctypes.c_uint8
    
    data_offset, data_size = shared_memory.get_obj_buffer_2(offset)
    if isinstance(np_dtype_or_ctypes_type, _SimpleCData):
        num_elements = np.prod(np_shape)
        np_array_size = num_elements * ctypes.sizeof(np_dtype_or_ctypes_type)
        if data_size < np_array_size:
            raise ObjBufferIsSmallerThanRequestedNumpyArrayError(data_size, np_array_size)
        
        data_address = shared_memory.base_address + data_offset
        void_ptr = ctypes.c_void_p(data_address)
        # actual_ptr = ctypes.cast(void_ptr, ctypes.POINTER(np_dtype_or_ctypes_type * num_elements))
        actual_ptr = ctypes.cast(void_ptr, ctypes.POINTER(np_dtype_or_ctypes_type))
        return np.ctypeslib.as_array(actual_ptr, shape=np_shape)
    else:
        return np.ndarray(np_shape, dtype=np_dtype_or_ctypes_type, buffer=shared_memory.mem_view(data_offset, data_size))


def zero_bytes_from_numpy_array(np: np.ndarray) -> bytes:
    return bytes(np.nbytes)


def bytes_from_numpy_array(np: np.ndarray) -> bytes:
    return np.tobytes()


def dict_to_list(mapping: AbsMapping) -> List:
    items_num = max(mapping.keys())
    result = [None] * items_num
    for key, value in mapping.items():
        result[key] = value
    
    return result


def list_to_dict(data_list: List) -> Dict:
    return {key: value for key, value in enumerate(data_list)}


def intenum_dict_to_list(mapping: AbsMapping, int_enum_class: Optional[Type] = None) -> List:
    if int_enum_class:
        items_num = len(int_enum_class)
    else:
        first_key_type_detected: bool = False
        for first_key in mapping.keys():
            first_key_type = type(first_key)
            if issubclass(first_key_type, IntEnum):
                items_num = len(first_key_type)
                first_key_type_detected = True
        
        if not first_key_type_detected:
            items_num = max(mapping.keys(), key=lambda value: int(value))
    
    result = [None] * items_num
    for key, value in mapping.items():
        result[int(key)] = value
    
    return result


def intenum_list_to_dict(data_list: List, int_enum_class: Optional[Type] = None) -> Dict:
    if int_enum_class:
        return {int_enum_class(key): value for key, value in enumerate(data_list)}
    else:
        return {key: value for key, value in enumerate(data_list)}
