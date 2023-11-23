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
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from enum import IntEnum
from multiprocessing.shared_memory import SharedMemory as MultiprocessingSharedMemory
from array import array
from inspect import isclass, ismodule
import pickle
import ctypes
from contextlib import contextmanager

import numpy as np

from cengal.introspection.inspect import is_callable, is_descriptor, is_async
from cengal.math.numbers import RationalNumber
from cengal.hardware.memory.barriers import full_memory_barrier, mm_pause
from cengal.time_management.cpu_clock import cpu_clock
from cengal.time_management.high_precision_sync_sleep import hps_sleep
from cengal.introspection.inspect import pdi

# from .compilable import write_uint64 as write_uint64_c, read_uint64 as read_uint64_c, write_int64, read_int64, write_double, read_double, zero_memory
from .compilable import write_uint64, read_uint64, read_uint8, write_int64, read_int64, write_double, read_double, zero_memory, list__get_item, list__set_item

from typing import Any, Tuple, Optional, List, Dict, Type, Union, Sequence


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
    tdict = 12
    tset = 13
    tclass = 14
    tpickable = 15
    tinternal_list = 16


class SysValuesOffsets(IntEnum):
    data_start_offset = 0
    data_size = 1
    data_end_offset = 2
    free_memory_search_start = 3
    first_message_offset = 4
    last_message_offset = 5
    creator_in_charge = 6
    consumer_in_charge = 7
    creator_wants_to_be_in_charge = 8
    consumer_wants_to_be_in_charge = 9
    creator_ready = 10
    consumer_ready = 11


Offset = int
Size = int
minimal_memory_block_size = 8
block_size = minimal_memory_block_size
bs = block_size


class SharedMemoryError(Exception):
    pass

class WrongObjectTypeError(SharedMemoryError):
    pass


class NoMessagesInQueueError(SharedMemoryError):
    pass


def nearest_size(size: Size) -> Size:
    return ((size // bs) * bs + bs) if size % bs else size


nsize = nearest_size


class BaseIObject:
    pass


# TODO: add next fields: obj_id (simple int index; need to identify object in shared memory); ref_count (simple int counter; need to count references to object. Howerver this field can be moved to shared memory dict with all objects properties like ref_count, etc.)
class BaseObjOffsets(IntEnum):
    obj_type = 0
    obj_size = 1


class TBase:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: Any) -> Tuple[Any, Offset, Size]:
        raise NotImplementedError
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> Any:
        raise NotImplementedError
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
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
        shared_memory.free(offset)


# ======================================================================================================================
# === Int =====================================================================================================


class IntOffsets(IntEnum):
    data = 0


class TInt:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: int) -> Tuple[int, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.tint, bs * len(IntOffsets))
        write_int64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * IntOffsets.data, obj)
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> int:
        if ObjectType.tint != read_uint64(shared_memory.base_address, offset + bs * BaseObjOffsets.obj_type):
            raise WrongObjectTypeError

        return read_int64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * IntOffsets.data)
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        shared_memory.free(offset)


# ======================================================================================================================
# === Bool =====================================================================================================


class BoolOffsets(IntEnum):
    data = 0


class TBool:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: bool) -> Tuple[bool, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.tbool, bs * len(BoolOffsets))
        write_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * BoolOffsets.data, int(obj))
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> bool:
        if ObjectType.tbool != read_uint64(shared_memory.base_address, offset + bs * BaseObjOffsets.obj_type):
            raise WrongObjectTypeError

        return bool(read_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * BoolOffsets.data))
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        shared_memory.free(offset)


# ======================================================================================================================
# === Float =====================================================================================================


class FloatOffsets(IntEnum):
    data = 0


class TFloat:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: float) -> Tuple[float, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.tfloat, bs * len(FloatOffsets))
        write_double(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * FloatOffsets.data, obj)
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> float:
        if ObjectType.tfloat != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        return read_double(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * FloatOffsets.data)
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        shared_memory.free(offset)


# ======================================================================================================================
# === Bytes =====================================================================================================


class BytesOffsets(IntEnum):
    data_size = 0
    data = 1


class TBytes:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: bytes) -> Tuple[bytes, Offset, Size]:
        data_size = len(obj)
        offset, real_size = shared_memory.malloc(ObjectType.tbytes, bs * len(BytesOffsets) + bs * data_size)
        write_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * BytesOffsets.data_size, data_size)
        data_offset = offset + bs * len(BaseObjOffsets) + bs * BytesOffsets.data
        shared_memory._shared_memory.buf[data_offset:data_offset + data_size] = obj
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> bytes:
        if ObjectType.tbytes != read_uint64(shared_memory.base_address, offset + bs * BaseObjOffsets.obj_type):
            raise WrongObjectTypeError

        data_size = read_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * BytesOffsets.data_size)
        data_offset = offset + bs * len(BaseObjOffsets) + bs * BytesOffsets.data
        obj = bytes(shared_memory._shared_memory.buf[data_offset:data_offset + data_size])
        return obj
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        shared_memory.free(offset)


# ======================================================================================================================
# === Bytearray =====================================================================================================


class BytearrayOffsets(IntEnum):
    data_size = 0
    data = 1


class TBytearray:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: bytearray) -> Tuple[bytearray, Offset, Size]:
        data = bytes(obj)
        data_size = len(data)
        offset, real_size = shared_memory.malloc(ObjectType.tbytearray, bs * len(BytearrayOffsets) + bs * data_size)
        write_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * BytearrayOffsets.data_size, data_size)
        data_offset = offset + bs * len(BaseObjOffsets) + bs * BytearrayOffsets.data
        shared_memory._shared_memory.buf[data_offset:data_offset + data_size] = data
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> bytearray:
        if ObjectType.tbytearray != read_uint64(shared_memory.base_address, offset + bs * BaseObjOffsets.obj_type):
            raise WrongObjectTypeError

        data_size = read_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * BytearrayOffsets.data_size)
        data_offset = offset + bs * len(BaseObjOffsets) + bs * BytearrayOffsets.data
        data = bytes(shared_memory._shared_memory.buf[data_offset:data_offset + data_size])
        return bytearray(data)
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        shared_memory.free(offset)


# ======================================================================================================================
# === Str =====================================================================================================


class StrOffsets(IntEnum):
    data_size = 0
    data = 1


class TStr:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: str) -> Tuple[str, Offset, Size]:
        data = str.encode(obj)
        data_size = len(data)
        offset, real_size = shared_memory.malloc(ObjectType.tstr, bs * len(StrOffsets) + bs * data_size)
        write_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * StrOffsets.data_size, data_size)
        data_offset = offset + bs * len(BaseObjOffsets) + bs * StrOffsets.data
        shared_memory._shared_memory.buf[data_offset:data_offset + data_size] = data
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> str:
        if ObjectType.tstr != read_uint64(shared_memory.base_address, offset + bs * BaseObjOffsets.obj_type):
            raise WrongObjectTypeError

        data_size = read_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * StrOffsets.data_size)
        data_offset = offset + bs * len(BaseObjOffsets) + bs * StrOffsets.data
        data = bytes(shared_memory._shared_memory.buf[data_offset:data_offset + data_size])
        return data.decode()
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        shared_memory.free(offset)


# ======================================================================================================================
# === ListTrue =====================================================================================================


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
            self._offset__data = offset + 8 * len(BaseObjOffsets)
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
            self._offset__data = offset + 8 * len(BaseObjOffsets)
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
        return read_uint64(self._base_address, self._pointer_to_internal_list + 8 * len(BaseObjOffsets) + 8 * InternalListTrueOffsets.size)
    
    @_list_len.setter
    def _list_len(self, value: int):
        write_uint64(self._base_address, self._pointer_to_internal_list + 8 * len(BaseObjOffsets) + 8 * InternalListTrueOffsets.size, value)

    @property
    def _list_capacity(self):
        return read_uint64(self._base_address, self._pointer_to_internal_list + 8 * len(BaseObjOffsets) + 8 * InternalListTrueOffsets.capacity)
    
    def _item_offset(self, key: int) -> Offset:
        return self._pointer_to_internal_list + 8 * len(BaseObjOffsets) + 8 * len(InternalListTrueOffsets) + key * 8
    
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


def malloc_tinternal_list(shared_memory: 'SharedMemory', size: Size, capacity: Size = None) -> Tuple[Offset, Size]:
    capacity = (size << 1 if size else 16) if capacity is None else capacity
    offset, real_size = shared_memory.malloc(ObjectType.tinternal_list, bs * len(BaseObjOffsets) + bs * len(InternalListOffsets) + capacity * bs * len(InternalListFieldOffsets))
    sys_data_offset = offset + bs * len(BaseObjOffsets)
    write_uint64(shared_memory.base_address, sys_data_offset + bs * InternalListOffsets.capacity, capacity)
    write_uint64(shared_memory.base_address, sys_data_offset + bs * InternalListOffsets.size, size)
    return offset, real_size


def realloc_tinternal_list(shared_memory: 'SharedMemory', offset: Offset, desired_size: int = None, new_capacity: int = None, loop_allowed: bool = True, zero_mem: bool = True) -> Tuple[Offset, Size]:
    sys_data_offset = offset + bs * len(BaseObjOffsets)
    capacity = read_uint64(shared_memory.base_address, sys_data_offset + bs * InternalListOffsets.capacity)
    size = read_uint64(shared_memory.base_address, sys_data_offset + bs * InternalListOffsets.size)
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
    
    new_offset, new_real_size = shared_memory.realloc(
            offset,
            bs * len(BaseObjOffsets) + bs * len(InternalListOffsets) + capacity * bs * len(InternalListFieldOffsets),
            loop_allowed,
            zero_mem
        )
    new_sys_data_offset = new_offset + bs * len(BaseObjOffsets)
    write_uint64(shared_memory.base_address, new_sys_data_offset + bs * InternalListOffsets.capacity, new_list_capacity)
    return new_offset, new_real_size


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
            offset, real_size = shared_memory.malloc(ObjectType.tlist, bs * len(ListOffsets))
            self._offset = offset
            self._offset__data = offset + bs * len(BaseObjOffsets)
            self._offset__pointer_to_internal_list = self._offset__data + bs * ListOffsets.internal_list_offset
            
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
        else:
            self._offset = offset
            self._offset__data = offset + bs * len(BaseObjOffsets)
            self._offset__pointer_to_internal_list = self._offset__data
    
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
        return read_uint64(self._base_address, self._offset + bs * BaseObjOffsets.obj_size)
    
    @property
    def _pointer_to_internal_list(self):
        return read_uint64(self._base_address, self._offset__pointer_to_internal_list)

    @_pointer_to_internal_list.setter
    def _pointer_to_internal_list(self, value: Offset):
        write_uint64(self._base_address, self._offset__pointer_to_internal_list, value)

    @property
    def _list_len(self):
        return read_uint64(self._base_address, self._pointer_to_internal_list + bs * len(BaseObjOffsets) + bs * InternalListOffsets.size)
    
    @_list_len.setter
    def _list_len(self, value: int):
        write_uint64(self._base_address, self._pointer_to_internal_list + bs * len(BaseObjOffsets) + bs * InternalListOffsets.size, value)

    @property
    def _list_capacity(self):
        return read_uint64(self._base_address, self._pointer_to_internal_list + bs * len(BaseObjOffsets) + bs * InternalListOffsets.capacity)
    
    def _item_offset(self, key: int) -> Offset:
        return self._pointer_to_internal_list + bs * len(BaseObjOffsets) + bs * len(InternalListOffsets) + key * bs * len(InternalListFieldOffsets)
    
    def _item_type_offset(self, key: int) -> Offset:
        # from os import getpid
        result = self._pointer_to_internal_list + bs * len(BaseObjOffsets) + bs * len(InternalListOffsets) + key * bs * len(InternalListFieldOffsets) + bs * InternalListFieldOffsets.field_type
        # add_0 = bs * len(BaseObjOffsets)
        # add_1 = bs * len(InternalListOffsets)
        # add_2 = key * bs * len(InternalListFieldOffsets)
        # add_3 = bs * InternalListFieldOffsets.field_type
        # print(f'PID: {getpid()}. [{add_0},{add_1},{add_2},{add_3}],{add_0 + add_1 + add_2 + add_3},{self._pointer_to_internal_list}: item_type_offset: {key}:{result}')
        return result

    def _item_value_offset(self, key: int) -> Offset:
        # from os import getpid
        result = self._pointer_to_internal_list + bs * len(BaseObjOffsets) + bs * len(InternalListOffsets) + key * bs * len(InternalListFieldOffsets) + bs * InternalListFieldOffsets.offset_or_data
        # print(f'PID: {getpid()}. {bs * len(BaseObjOffsets) + bs * len(InternalListOffsets) + key * bs * len(InternalListFieldOffsets) + bs * InternalListFieldOffsets.offset_or_data},{self._pointer_to_internal_list}: item_value_offset: {key}:{result}')
        return result

    def _read_item_type(self, key: int) -> int:
        return read_uint64(self._base_address, self._item_type_offset(key))
    
    def _write_item_type(self, key: int, item_type: int) -> None:
        write_uint64(self._base_address, self._item_type_offset(key), item_type)
    
    def _read_item_offset_or_data(self, key: int) -> Union[Offset, int]:
        return read_uint64(self._base_address, self._item_value_offset(key))

    def _write_item_offset_or_data(self, key: int, offset_or_data: Union[Offset, int]) -> None:
        write_uint64(self._base_address, self._item_value_offset(key), offset_or_data)
    
    def _determine_obj_type(self, obj: Any) -> int:
        if isinstance(obj, int):
            return 1
        elif isinstance(obj, float):
            return 2
        elif isinstance(obj, bool):
            return 3
        else:
            return 0
    
    def _determine_obj_offset(self, obj: Any) -> Optional[Offset]:
        if isinstance(obj, BaseIObject):
            return obj._offset
        else:
            return None
    
    def _compare_item_to_obj_fast(self, key: int, obj: Any, obj_type: int, obj_offset) -> bool:
        result: bool = False
        item_type = self._read_item_type(key)
        if item_type == obj_type:
            if item_type == 0:
                if obj_offset is None:
                    if self._read_item_value(key, item_type) == obj:
                        result = True
                else:
                    if self._read_item_offset_or_data(key) == obj_offset:
                        result = True
            elif item_type == 1:
                if self._read_item_offset_or_data(key) == obj:
                    result = True
            elif item_type == 2:
                if self._read_item_offset_or_data(key) == obj:
                    result = True
            elif item_type == 3:
                if self._read_item_offset_or_data(key) == obj:
                    result = True
            else:
                raise ValueError

        return result
    
    def _compare_item_to_obj(self, key: int, obj: Any) -> bool:
        obj_type = self._determine_obj_type(obj)
        obj_offset = self._determine_obj_offset(obj)
        return self._compare_item_to_obj_fast(key, obj, obj_type, obj_offset)

    def _read_item_value(self, key: int, item_type: int) -> Any:
        if item_type == 0:
            item_offset = read_uint64(self._base_address, self._item_value_offset(key))
            return self._shared_memory.get_obj(item_offset)
        elif item_type == 1:
            return read_int64(self._base_address, self._item_value_offset(key))
        elif item_type == 2:
            return read_double(self._base_address, self._item_value_offset(key))
        elif item_type == 3:
            return bool(read_uint64(self._base_address, self._item_value_offset(key)))
        else:
            raise ValueError
    
    def _write_item_value(self, key: int, item_type: int, value: Any) -> None:
        if item_type == 0:
            item_mapped_obj, item_offset, item_size = self._shared_memory.put_obj(value)
            write_uint64(self._base_address, self._item_value_offset(key), item_offset)
        elif item_type == 1:
            write_int64(self._base_address, self._item_value_offset(key), value)
        elif item_type == 2:
            write_double(self._base_address, self._item_value_offset(key), value)
        elif item_type == 3:
            write_uint64(self._base_address, self._item_value_offset(key), int(value))
        else:
            raise ValueError
    
    def _free_item_value(self, key: int, item_type: int) -> None:
        if item_type == 0:
            item_offset = read_uint64(self._base_address, self._item_value_offset(key))
            self._shared_memory.free(item_offset)
        elif item_type == 1:
            pass
        elif item_type == 2:
            pass
        elif item_type == 3:
            pass
        else:
            raise ValueError
    
    def _read_item_type_and_value(self, key: int) -> Tuple[int, Any]:
        item_type = self._read_item_type(key)
        return item_type, self._read_item_value(key, item_type)
    
    def _write_item_value_and_get_type(self, key: int, value: Any) -> int:
        if isinstance(value, int):
            write_uint64(self._base_address, self._item_value_offset(key), value)
            return 1
        elif isinstance(value, float):
            write_double(self._base_address, self._item_value_offset(key), value)
            return 2
        elif isinstance(value, bool):
            write_uint64(self._base_address, self._item_value_offset(key), int(value))
            return 3
        else:
            item_mapped_obj, item_offset, item_size = self._shared_memory.put_obj(value)
            write_uint64(self._base_address, self._item_value_offset(key), item_offset)
            return 0
    
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
    
    def _move_item(self, src_key: int, dst_key: int) -> None:
        self._write_item_type(dst_key, self._read_item_type(src_key))
        self._write_item_offset_or_data(dst_key, self._read_item_offset_or_data(src_key))
    
    def _swap_items(self, key1: int, key2: int) -> None:
        item_type1 = self._read_item_type(key1)
        item_offset_or_data1 = self._read_item_offset_or_data(key1)
        self._write_item_type(key1, self._read_item_type(key2))
        self._write_item_type(key2, item_type1)
        self._write_item_offset_or_data(key1, self._read_item_offset_or_data(key2))
        self._write_item_offset_or_data(key2, item_offset_or_data1)

    def __len__(self) -> int:
        return self._list_len
    
    def get_children_data_or_offsets(self) -> List[Offset]:
        return [self._read_item_offset_or_data(i) for i in range(self._list_len)]
    
    def get_children_offsets(self):
        return self.get_children_data_or_offsets()

    def __getitem__(self, key: Union[int, slice]) -> Union[Any, List]:
        if isinstance(key, int):
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
            item_type_offset = pointer_to_internal_list + 32 + i * 16
            item_value_offset = pointer_to_internal_list + 40 + i * 16
            for i in range(start, stop):
                # result_list.append(self._read_item(i))

                # performance improvement instead of using self._read_item(i)
                item_type = read_uint64(base_address, item_type_offset)
                if item_type == 1:
                    result_list.append(read_int64(base_address, item_value_offset))
                elif item_type == 2:
                    result_list.append(read_double(base_address, item_value_offset))
                elif item_type == 3:
                    result_list.append(bool(read_uint64(base_address, item_value_offset)))
                elif item_type == 0:
                    item_offset = read_uint64(base_address, item_value_offset)
                    result_list.append(self._shared_memory.get_obj(item_offset))
                else:
                    raise ValueError
            
            return result_list
        else:
            raise TypeError
    
    def __setitem__(self, key: Union[int, slice], value: Union[Any, Sequence]) -> Any:
        if isinstance(key, int):
            list__set_item(key, value, self._base_address, self._offset__pointer_to_internal_list, self._shared_memory.put_obj)

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
            
            # performance improvement instead of using self._write_item(i, item)
            base_address = self._base_address
            offset__pointer_to_internal_list = self._offset__pointer_to_internal_list
            pointer_to_internal_list = read_uint64(base_address, offset__pointer_to_internal_list)
            item_type_offset = pointer_to_internal_list + 32 + i * 16
            item_value_offset = pointer_to_internal_list + 40 + i * 16
            for i in range(start, stop):
                item = value[i - start]
                # self._write_item(i, item)

                # performance improvement instead of using self._write_item(i, item)
                if isinstance(item, int):
                    write_int64(base_address, item_value_offset, item)
                    item_type = 1
                elif isinstance(item, float):
                    write_double(base_address, item_value_offset, item)
                    item_type = 2
                elif isinstance(item, bool):
                    write_uint64(base_address, item_value_offset, int(item))
                    item_type = 3
                else:
                    item_mapped_obj, item_offset, item_size = self._shared_memory.put_obj(item)
                    write_uint64(base_address, item_value_offset, item_offset)
                    item_type = 0
                
                write_uint64(base_address, item_type_offset, item_type)
        else:
            raise TypeError

    def __delitem__(self, key: Union[int, slice]) -> None:
        if isinstance(key, int):
            if key < 0:
                key += len(self)
            if key < 0 or key >= len(self):
                raise IndexError

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
        self.__setitem__(self._list_len - 1, item)

    def extend(self, items: Sequence) -> None:
        items_num = len(items)
        if self._list_len + items_num > self._list_capacity:
            self._pointer_to_internal_list, result_size = realloc_tinternal_list(self._shared_memory, self._pointer_to_internal_list, self._list_len + items_num)

        original_list_len = self._list_len
        self._list_len += items_num
        for i, item in enumerate(items):
            self.__setitem__(original_list_len + i, item)
        
    
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
        
        self.__setitem__(index, item)
        # self._shared_memory.print_mem(self._pointer_to_internal_list, 200, 'after inserting. {}')
        # self.print_internal_list('after inserting. {}')
    
    def print_internal_list(self, text: str = None, additional_cells: int = 0):
        internal_list = self._shared_memory.read_mem(self._pointer_to_internal_list, bs * len(BaseObjOffsets) + bs * len(InternalListOffsets) + self._list_len * bs * len(InternalListFieldOffsets) + additional_cells * bs * len(InternalListFieldOffsets))
        print('--- internal list -------------')
        if text:
            print(text.format(self._pointer_to_internal_list))
            print('------')

        index = 0
        print(f'{index},{self._pointer_to_internal_list + index}:', internal_list[index:index + bs])
        index += bs
        print(f'{index},{self._pointer_to_internal_list + index}:', internal_list[index:index + bs])
        index += bs
        print('---')
        print(f'{index},{self._pointer_to_internal_list + index}:', internal_list[index:index + bs])
        index += bs
        print(f'{index},{self._pointer_to_internal_list + index}:', internal_list[index:index + bs])
        index += bs
        print('---')
        for i in range(self._list_len):
            print(f'{index},{self._pointer_to_internal_list + index}:', internal_list[index:index + bs * 2])
            index += bs * 2
        
        if additional_cells:
            print('------')
            for i in range(additional_cells):
                print(f'{index},{self._pointer_to_internal_list + index}:', internal_list[index:index + bs])
                index += bs * 2
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
    
    def clear(self) -> None:
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
        found_in_index = None
        for i in range(len(self)):
            if self._compare_item_to_obj_fast(i, obj, obj_type, obj_offset):
                found_in_index = i
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
        return bs * len(BaseObjOffsets) + read_uint64(self._base_address, self._offset + bs * BaseObjOffsets.obj_size) + bs * len(BaseObjOffsets) + read_uint64(self._base_address, self._pointer_to_internal_list, bs * BaseObjOffsets.obj_size)
    
    def export(self) -> list:
        return list(self)

    # def __del__(self) -> None:
    #     self._shared_memory.free(self._pointer_to_internal_list)
    #     self._shared_memory.free(self._offset)


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
        shared_memory.free(offset)


# ======================================================================================================================
# === Tuple ============================================================================================================


class TupleOffsets(IntEnum):
    size = 0


class TupleFieldOffsets(IntEnum):
    item_offset = 0


class TTuple:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: tuple) -> Tuple[tuple, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.ttuple, bs * len(TupleOffsets) + len(obj) * bs * len(TupleFieldOffsets))
        if (1, [2, 3]) == obj:
            shared_memory.offset_to_be_monitored = offset
        
        write_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * TupleOffsets.size, len(obj))
        for i, item in enumerate(obj):
            item_mapped_obj, item_offset, item_size = shared_memory.put_obj(item)
            write_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * len(TupleOffsets) + i * bs * len(TupleFieldOffsets), item_offset)
        
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.ttuple != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        result_list = list()
        size = read_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * TupleOffsets.size)
        for i in range(size):
            item_offset = read_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * len(TupleOffsets) + i * bs * len(TupleFieldOffsets))
            result_list.append(shared_memory.get_obj(item_offset))
        
        return tuple(result_list)
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        shared_memory.free(offset)


# ======================================================================================================================
# === Dict =============================================================================================================


class DictOffsets(IntEnum):
    data_tuple_offset = 0


class TDict:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', obj: dict) -> Tuple[dict, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.tdict, bs * len(DictOffsets))
        item_mapped_obj, item_offset, item_size = shared_memory.put_obj(tuple(obj.items()))
        write_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * DictOffsets.data_tuple_offset, item_offset)
        return obj, offset, real_size
    
    def init_from_shared_memory(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.tdict != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        item_offset = read_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * DictOffsets.data_tuple_offset)
        result_tuple = shared_memory.get_obj(item_offset)
        return dict(result_tuple)
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset):
        shared_memory.free(offset)


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
    ObjectType.tdict: TDict(),
}
obj_type_map: Dict[Type, ObjectType] = {
}


# ======================================================================================================================
# === Message ==========================================================================================================


class MessageOffsets(IntEnum):
    previous_message_offset = 0
    next_message_offset = 1
    item_offset = 2


class SharedMemory:
    def __init__(self, name: str, create: bool = False, size: int = 0, queue_type: QueueType = QueueType.fifo, zero_mem: bool = True):
        global current_shared_memory_instance
        current_shared_memory_instance = self
        self.offset_to_be_monitored: Offset = None
        self._malloc_time: float = 0.0
        self._realloc_time: float = 0.0
        self._shared_memory: MultiprocessingSharedMemory = MultiprocessingSharedMemory(name=name, create=create, size=size)
        self.base_address = ctypes.addressof(ctypes.c_char.from_buffer(self._shared_memory.buf))
        self.sys_values_offset = 0
        # if create:
        #     print(f'Creator: {self.base_address=}')
        # else:
        #     print(f'Consumer: {self.base_address=}')
        
        self._name: str = name
        self._create: bool = create
        self._size: int = size
        self._queue_type: QueueType = queue_type
        self._zero_mem: bool = zero_mem
        self._last_message_offset: Offset = None

        self._shared_memory_bytearray = bytearray(self._shared_memory.buf)

        sys_arr_length = len(SysValuesOffsets)
        arr_byte_size = sys_arr_length * bs
        self.log_arr = np.ndarray((500,), dtype=np.uint64, buffer=self._shared_memory.buf)
        self.sys_arr = np.ndarray((sys_arr_length,), dtype=np.uint64, buffer=self._shared_memory.buf)
        write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.data_start_offset, sys_arr_length * bs)
        write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.data_size, self._size - arr_byte_size)
        write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.data_end_offset, self._size)
        write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.free_memory_search_start, sys_arr_length * bs)
        write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.first_message_offset, 0)
        write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.last_message_offset, 0)
        write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.creator_in_charge, 0)
        write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.consumer_in_charge, 0)
        write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.creator_wants_to_be_in_charge, 0)
        write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.consumer_wants_to_be_in_charge, 0)
        write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.creator_ready, 0)
        write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.consumer_ready, 0)
        # print(bytes(self._shared_memory.buf[0:120]))

        self.free_memory_search_start = self.read_free_memory_search_start()
        data_size: int = self.get_data_size()
        if self._create and self._zero_mem:
            zero_memory(self.base_address, self.free_memory_search_start, data_size)
        
        write_uint64(self.base_address, self.free_memory_search_start + bs * BaseObjOffsets.obj_type, ObjectType.tfree_memory.value)
        write_uint64(self.base_address, self.free_memory_search_start + bs * BaseObjOffsets.obj_size, data_size - bs * len(BaseObjOffsets))

        if self._create:
            write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.creator_ready, 1)
        else:
            write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.consumer_ready, 1)

        # print(bytes(self._shared_memory.buf[0:120]))
    
    def read_mem(self, offset: Offset, size: Size, text: str = None) -> List[int]:
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
        write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.creator_ready, 1)
    
    def set_consumer_ready(self):
        write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.consumer_ready, 1)
    
    def get_creator_ready(self):
        return read_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.creator_ready)
    
    def get_consumer_ready(self):
        return read_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.consumer_ready)
    
    def wait_creator_ready(self, time_limit: Optional[RationalNumber] = None, periodic_sleep_time: Optional[RationalNumber] = 0.000000001):
        start_time = cpu_clock()
        while not read_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.creator_ready):
            if time_limit is not None:
                if (cpu_clock() - start_time) > time_limit:
                    return False
            
            if periodic_sleep_time is None:
                mm_pause()
            else:
                hps_sleep(periodic_sleep_time)
    
    def wait_consumer_ready(self, time_limit: Optional[RationalNumber] = None, periodic_sleep_time: Optional[RationalNumber] = 0.000000001):
        start_time = cpu_clock()
        while not read_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.consumer_ready):
            if time_limit is not None:
                if (cpu_clock() - start_time) > time_limit:
                    return False
            
            if periodic_sleep_time is None:
                mm_pause()
            else:
                hps_sleep(periodic_sleep_time)
    
    def creator_in_charge(self) -> bool:
        return read_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.creator_in_charge)
    
    def consumer_in_charge(self) -> bool:
        return read_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.consumer_in_charge)
    
    def creator_wants_to_be_in_charge(self) -> bool:
        return read_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.creator_wants_to_be_in_charge)
    
    def consumer_wants_to_be_in_charge(self) -> bool:
        return read_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.consumer_wants_to_be_in_charge)
    
    def read_free_memory_search_start(self) -> int:
        # return self.get_data_start_offset()
        return read_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.free_memory_search_start)
    
    def update_free_memory_search_start(self) -> int:
        self.free_memory_search_start = self.read_free_memory_search_start()
    
    def get_free_memory_search_start(self) -> int:
        # self.update_free_memory_search_start()
        return self.free_memory_search_start
    
    def write_free_memory_search_start(self, offset: Offset) -> int:
        # return
        if ((self.get_data_end_offset() - bs * len(BaseObjOffsets)) < offset) or (offset < self.get_data_start_offset()):
            offset = self.get_data_start_offset()
        
        write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.free_memory_search_start, offset)
    
    def commit_free_memory_search_start(self):
        self.write_free_memory_search_start(self.free_memory_search_start)
    
    def set_free_memory_search_start(self, offset: Offset) -> int:
        # return
        if ((self.get_data_end_offset() - bs * len(BaseObjOffsets)) < offset) or (offset < self.get_data_start_offset()):
            offset = self.get_data_start_offset()
        
        self.free_memory_search_start = offset
        # self.commit_free_memory_search_start()
    
    def get_last_message_offset(self) -> Optional[Offset]:
        return read_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.last_message_offset)

    def set_last_message_offset(self, offset: Offset):
        write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.last_message_offset, offset)
    
    def get_first_message_offset(self) -> Optional[Offset]:
        return read_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.first_message_offset)

    def set_first_message_offset(self, offset: Offset):
        write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.first_message_offset, offset)
    
    def get_data_start_offset(self) -> Offset:
        return read_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.data_start_offset)

    def get_data_size(self) -> Size:
        return read_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.data_size)
    
    def get_data_end_offset(self) -> Offset:
        return read_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.data_end_offset)

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
        obj_type = ObjectType(read_uint64(self.base_address, offset + bs * BaseObjOffsets.obj_type))
        size = read_uint64(self.base_address, offset + bs * BaseObjOffsets.obj_size)
        return obj_type, size
    
    def write_obj_type_and_size(self, offset: Offset, obj_type: ObjectType, size: Size):
        write_uint64(self.base_address, offset + bs * BaseObjOffsets.obj_type, obj_type.value)
        write_uint64(self.base_address, offset + bs * BaseObjOffsets.obj_size, size)
        return offset + bs * len(BaseObjOffsets)

    # ----------------------------
    
    def test_free_memory_blocks(self, offset: Offset, desired_size: Size) -> Tuple[bool, Size, Offset]:
        adjusted_size = desired_size
        initial_offset = offset
        sum_size = 0
        max_viable_offset = self.get_data_end_offset() - bs * len(BaseObjOffsets)
        last_found_obj_offset = None
        last_found_obj_size = None
        while True:
            last_found_obj_offset = offset
            try:
                obj_type = ObjectType(read_uint64(self.base_address, offset))
            except ValueError:
                print(f'Error: {offset=}, {desired_size=}, {sum_size=}')
            
            size = read_uint64(self.base_address, offset + bs * BaseObjOffsets.obj_size)
            if size % bs:
                print('WRONG SIZE')
            
            last_found_obj_size = size + bs * len(BaseObjOffsets)
            next_block_offset = last_found_obj_offset + last_found_obj_size
            if obj_type is not ObjectType.tfree_memory:
                return False, adjusted_size, None, None, next_block_offset

            sum_size = next_block_offset - initial_offset

            if sum_size == desired_size:
                return True, adjusted_size, None, None, next_block_offset

            if sum_size > desired_size:
                new_next_block_offset = initial_offset + desired_size
                new_next_block_size = last_found_obj_size - (new_next_block_offset - last_found_obj_offset)
                if new_next_block_size < bs * len(BaseObjOffsets):
                    adjusted_size = desired_size + new_next_block_size
                    return True, adjusted_size, None, None, next_block_offset
                else:
                    return True, adjusted_size, new_next_block_offset, new_next_block_size, new_next_block_offset

            offset = last_found_obj_offset + last_found_obj_size
            if offset > max_viable_offset:
                return False, adjusted_size, None, None, next_block_offset

    def combine_free_memory_blocks(self, free_mem_block_offset: Offset, size: Size, last_free_block_offset: Offset, last_free_block_new_size: Size, next_block_offset: Offset, mark_block: bool = False) -> Tuple[Size, Offset]:
        if mark_block:
            self.write_obj_type_and_size(free_mem_block_offset, ObjectType.tfree_memory, size - bs * len(BaseObjOffsets))
        
        if last_free_block_offset is not None:
            if last_free_block_new_size - bs * len(BaseObjOffsets) < 0:
                print(f'Error: {last_free_block_new_size=}')
            
            self.write_obj_type_and_size(last_free_block_offset, ObjectType.tfree_memory, last_free_block_new_size - bs * len(BaseObjOffsets))
        
        # self.set_free_memory_search_start(next_block_offset)

    # ----------------------------
    
    def malloc(self, obj_type: ObjectType, size: Size, loop_allowed: bool = True, zero_mem: bool = False) -> Tuple[Optional[Offset], Size]:
        start_time = cpu_clock()
        try:
            size += bs * len(BaseObjOffsets)
            size = nearest_size(size)
            adjusted_size = size
            initial_start_offset = self.get_free_memory_search_start()
            search_end_offset = self.get_data_end_offset() - bs * len(BaseObjOffsets)
            start_offset = initial_start_offset
            free_mem_block_offset: Offset = None
            last_free_block_offset: Offset = None
            last_free_block_new_size: Size = None
            found: bool = False
            sum_size: Size = 0
            while (not found) and (start_offset <= search_end_offset):
                free_mem_block_offset = start_offset
                found, adjusted_size, last_free_block_offset, last_free_block_new_size, next_block_offset = self.test_free_memory_blocks(start_offset, size)
                start_offset = next_block_offset
            
            if (not found) and loop_allowed:
                start_offset = self.get_data_start_offset()
                search_end_offset = initial_start_offset - bs * len(BaseObjOffsets)
                while (not found) and (start_offset <= search_end_offset):
                    free_mem_block_offset = start_offset
                    found, adjusted_size, last_free_block_offset, last_free_block_new_size, next_block_offset = self.test_free_memory_blocks(start_offset, size)
                    start_offset = next_block_offset

            if not found:
                return None, None
            
            self.combine_free_memory_blocks(free_mem_block_offset, adjusted_size, last_free_block_offset, last_free_block_new_size, next_block_offset)
            obj_size = adjusted_size - bs * len(BaseObjOffsets)
            self.write_obj_type_and_size(free_mem_block_offset, obj_type, obj_size)
            if zero_mem:
                # print(f'Zeroing memory 1: {free_mem_block_offset=}, {result_size=}')
                # hps_sleep(0.01)
                zero_memory(self.base_address, free_mem_block_offset + bs * len(BaseObjOffsets), obj_size)

            if free_mem_block_offset % bs:
                print(f'Error: {free_mem_block_offset=}, {obj_size=}')
                
        
            self.set_free_memory_search_start(free_mem_block_offset)
            return free_mem_block_offset, obj_size
        finally:
            self._malloc_time += cpu_clock() - start_time
    
    def zero_memory(self, offset: Offset, size: Size):
        # print(f'Zeroing memory 1: [{self.base_address + offset}:{self.base_address + offset + size}], {size=}')
        self._shared_memory_bytearray[offset:offset + size] = bytearray(size)
    
    def calloc(self, obj_type: ObjectType, size: Size, num: int, loop_allowed: bool = True, zero_mem: bool = True) -> Tuple[Optional[Offset], Size]:
        return self.malloc(obj_type, size * num, loop_allowed, zero_mem)
    
    def realloc(self, obj_offset: Offset, new_size: int, loop_allowed: bool = True, zero_mem: bool = True) -> Tuple[Optional[Offset], Size]:
        start_time: float = cpu_clock()
        internal_malloc_time: float = 0.0
        try:
            new_size += bs * len(BaseObjOffsets)
            new_size = nearest_size(new_size)
            result_offset: Offset = None
            result_obj_size: Size = 0
            original_obj_size = read_uint64(self.base_address, obj_offset + bs * BaseObjOffsets.obj_size)
            size = original_obj_size + bs * len(BaseObjOffsets)
            next_obj_offset = obj_offset + size
            free_mem_block_offset = next_obj_offset
            dsize = new_size - size
            found, additional_adjusted_size, last_free_block_offset, last_free_block_new_size, next_block_offset = self.test_free_memory_blocks(free_mem_block_offset, dsize)
            if found:
                self.combine_free_memory_blocks(free_mem_block_offset, additional_adjusted_size, last_free_block_offset, last_free_block_new_size, next_block_offset)
                if zero_mem:
                    # print(f'Zeroing memory 3: {free_mem_block_offset=}, {result_size=}')
                    # hps_sleep(0.01)
                    zero_memory(self.base_address, free_mem_block_offset, dsize)
                
                result_obj_size = new_size - bs * len(BaseObjOffsets)
                write_uint64(self.base_address, obj_offset + bs * BaseObjOffsets.obj_size, result_obj_size)
                self.set_free_memory_search_start(obj_offset)
                result_offset = obj_offset
            else:
                internal_malloc_start_time: float = cpu_clock()
                new_offset, result_obj_size = self.malloc(ObjectType(read_uint64(self.base_address, obj_offset + bs * BaseObjOffsets.obj_type)), new_size, loop_allowed)
                internal_malloc_time += cpu_clock() - internal_malloc_start_time
                if new_offset is None:
                    return None, 0

                self._shared_memory.buf[new_offset + bs * len(BaseObjOffsets):new_offset + bs * len(BaseObjOffsets) + size] = self._shared_memory.buf[obj_offset + bs * len(BaseObjOffsets):obj_offset + bs * len(BaseObjOffsets) + size]
                if zero_mem:
                    # print(f'Zeroing memory 4: {new_offset=}, {new_size=}')
                    # hps_sleep(0.01)
                    zero_memory(self.base_address, new_offset + bs * len(BaseObjOffsets) + original_obj_size, result_obj_size - original_obj_size)
                
                self.free(obj_offset)
                result_offset = new_offset
            
            return result_offset, result_obj_size
        finally:
            self._realloc_time += cpu_clock() - start_time - internal_malloc_time
    
    def free(self, offset: Offset) -> bool:
        write_uint64(self.base_address, offset, ObjectType.tfree_memory.value)
        return True

    # ----------------------------
    
    def put_obj(self, obj: Any):
        obj_type = self._get_obj_type(obj)
        codec = codec_by_type[obj_type]
        mapped_obj, offset, size = codec.map_to_shared_memory(self, obj)
        return mapped_obj, offset, size

    def get_obj(self, offset: int) -> Any:
        obj_type = ObjectType(read_uint64(self.base_address, offset))
        if obj_type is ObjectType.tfree_memory:
            # self.print_mem(offset - 32, 96, 'get_obj [offset - 32: offset + 64]. {}')
            raise RuntimeError
        
        codec = codec_by_type[obj_type]
        return codec.init_from_shared_memory(self, offset)

    def destroy_obj(self, offset: int):
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

    def write_message(self, obj: Any):
        # self.update_free_memory_search_start()
        message_offset, message_real_size = self.malloc(ObjectType.tmessage, bs * len(MessageOffsets))
        mapped_obj, offset, size = self.put_obj(obj)
        # self.commit_free_memory_search_start()
        last_message_offset: Offset = self.get_last_message_offset()
        if last_message_offset:
            write_uint64(self.base_address, last_message_offset + bs * len(BaseObjOffsets) + bs * MessageOffsets.next_message_offset, message_offset)
            write_uint64(self.base_address, message_offset + bs * len(BaseObjOffsets) + bs * MessageOffsets.previous_message_offset, last_message_offset)
        else:
            self.set_first_message_offset(message_offset)
        
        write_uint64(self.base_address, message_offset + bs * len(BaseObjOffsets) + bs * MessageOffsets.item_offset, offset)
        self.set_last_message_offset(message_offset)
        return mapped_obj, offset, message_offset
    

    def put_message(self, obj: Any):
        mapped_obj, offset, message_offset = self.write_message(obj)
        return mapped_obj


    def has_messages(self) -> bool:
        return self.get_last_message_offset() != 0

    def read_message_info(self, queue_type: QueueType = QueueType.fifo) -> Tuple[Any, Optional[Offset], Optional[Offset]]:
        if QueueType.fifo == queue_type:
            message_offset = self.get_first_message_offset()
            if not message_offset:
                return None, None, None
            
            next_message_offset = read_uint64(self.base_address, message_offset + bs * len(BaseObjOffsets) + bs * MessageOffsets.next_message_offset)
            self.set_first_message_offset(next_message_offset)
            if next_message_offset:
                write_uint64(self.base_address, next_message_offset + bs * len(BaseObjOffsets) + bs * MessageOffsets.previous_message_offset, 0)
            else:
                self.set_last_message_offset(0)
        else:
            message_offset = self.get_last_message_offset()
            if not message_offset:
                return None, None, None
            
            prev_message_offset = read_uint64(self.base_address, message_offset + bs * len(BaseObjOffsets) + bs * MessageOffsets.previous_message_offset)
            self.set_last_message_offset(prev_message_offset)
            if prev_message_offset:
                write_uint64(self.base_address, prev_message_offset + bs * len(BaseObjOffsets) + bs * MessageOffsets.next_message_offset, 0)
            else:
                self.set_first_message_offset(0)
        
        obj_offset = read_uint64(self.base_address, message_offset + bs * len(BaseObjOffsets) + bs * MessageOffsets.item_offset)
        if not obj_offset:
            return None, None, message_offset

        obj = self.get_obj(obj_offset)
        return obj, obj_offset, message_offset

    def destroy_message(self, message_offset: Offset):
        if not message_offset:
            return
        
        # obj_offset = read_uint64(self.base_address, message_offset + bs * len(BaseObjOffsets) + bs * MessageOffsets.item_offset)
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

    def take_message(self, queue_type: QueueType = QueueType.fifo) -> Any:
        obj, obj_offset, message_offset = self.read_message_info(queue_type)
        if message_offset:
            self.destroy_message(message_offset)
        else:
            raise NoMessagesInQueueError
        
        return obj
    
    def get_message(self, default = None, queue_type: QueueType = QueueType.fifo) -> Any:
        obj, obj_offset, message_offset = self.read_message_info(queue_type)
        if message_offset:
            return obj
        else:
            return default

    def pop_message(self, default = None, queue_type: QueueType = QueueType.fifo) -> Any:
        obj, obj_offset, message_offset = self.read_message_info(queue_type)
        if message_offset:
            self.destroy_message(message_offset)
        else:
            obj = default
        
        return obj

    # ----------------------------

    def get_in_line(self) -> bool:
        if self._create:
            write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.creator_in_charge, 0)
            write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.creator_wants_to_be_in_charge, 1)
            full_memory_barrier()
            if self.consumer_in_charge():
                return False
            else:
                write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.creator_in_charge, 1)
                full_memory_barrier()
                write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.creator_wants_to_be_in_charge, 0)
                full_memory_barrier()
                self.update_free_memory_search_start()
                if self.consumer_in_charge():
                    write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.creator_in_charge, 0)
                    full_memory_barrier()
                    write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.creator_wants_to_be_in_charge, 1)
                    full_memory_barrier()
                    return False

                return True
        else:
            write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.consumer_in_charge, 0)
            write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.consumer_wants_to_be_in_charge, 1)
            full_memory_barrier()
            if self.creator_in_charge():
                return False
            else:
                write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.consumer_in_charge, 1)
                full_memory_barrier()
                write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.consumer_wants_to_be_in_charge, 0)
                full_memory_barrier()
                self.update_free_memory_search_start()
                if self.creator_in_charge():
                    write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.consumer_in_charge, 0)
                    full_memory_barrier()
                    write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.consumer_wants_to_be_in_charge, 1)
                    full_memory_barrier()
                    return False
                
                return True
            
    def release(self):
        self.commit_free_memory_search_start()
        if self._create:
            write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.creator_in_charge, 0)
            write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.creator_wants_to_be_in_charge, 0)
            full_memory_barrier()
        else:
            write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.consumer_in_charge, 0)
            write_uint64(self.base_address, self.sys_values_offset + bs * SysValuesOffsets.consumer_wants_to_be_in_charge, 0)
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
        elif obj_type is dict:
            obj_type_atom = ObjectType.tdict
        elif obj_type is set:
            obj_type_atom = ObjectType.tset
        elif obj_type in obj_type_map:
            obj_type_atom = obj_type_map[obj_type]
        else:
            obj_type_atom = ObjectType.tpickable
        
        return obj_type_atom


@contextmanager
def get_in_line(shared_memor: SharedMemory):
    shared_memor.get_in_line()
    try:
        yield
    finally:
        shared_memor.release()


@contextmanager
def wait_my_turn(shared_memor: SharedMemory, time_limit: Optional[RationalNumber] = None, periodic_sleep_time: Optional[RationalNumber] = 0.000000001):
    shared_memor.wait_my_turn(time_limit, periodic_sleep_time)
    try:
        yield
    finally:
        shared_memor.release()
