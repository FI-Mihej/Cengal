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
    'TNumpyNdarrayOffsets', 
    'TNumpyNdarray', 
    'types_collection', 
    'numpy_array_memory_size', 
    'numpy_array_made_from_pointer_memory_size', 
    'make_numpy_array_from_obj_offset', 
    'zero_bytes_from_numpy_array', 
    'bytes_from_numpy_array', 
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


from cengal.hardware.memory.shared_memory import *

import numpy as np
from numpy import ndarray

from enum import IntEnum


# ======================================================================================================================
# === Numpy ndarray =============================================================================================================


class TNumpyNdarrayOffsets(IntEnum):
    data_buffer_offset = 0
    shape_tuple_offset = 1
    pickled_datatype_offset = 2


class TNumpyNdarray:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', nparray: ndarray) -> Tuple[ndarray, Offset, Size]:
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
            mapped_nparray: ndarray = make_numpy_array_from_obj_offset(shared_memory, data_buffer_offset, shape, data_type)
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
        mapped_nparray: ndarray = make_numpy_array_from_obj_offset(shared_memory, data_buffer_offset, shape, data_type)
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


# Add your own codecs to `codec_by_type`
codec_by_type: Dict[ObjectType, TBase] = {
    ObjectType.tnumpyndarray: TNumpyNdarray(),
}

# Add your own types to `obj_type_map`
obj_type_map: Dict[Type, ObjectType] = {
    ndarray: ObjectType.tnumpyndarray,
}

# Add your own base types to `obj_base_type_map`
obj_base_type_map: Dict[Type, ObjectType] = {
    ndarray: ObjectType.tnumpyndarray,
}


def types_collection() -> ExternalTypesCollection:
    return ExternalTypesCollection(codec_by_type, obj_type_map, obj_base_type_map)


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
