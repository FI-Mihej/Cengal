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
    'TTorchTensorOffsets', 
    'TTorchTensor', 
    'types_collection', 
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
from cengal.hardware.memory.shared_memory_external_types.numpy_types import types_collection as numpy_types_collection

from numpy import ndarray
from torch import Tensor, from_numpy

from enum import IntEnum


# ======================================================================================================================
# === torch Tensor =============================================================================================================


class TTorchTensorOffsets(IntEnum):
    numpy_ndarray_offset = 0


class TTorchTensor:
    def map_to_shared_memory(self, shared_memory: 'SharedMemory', tensor: Tensor) -> Tuple[Tensor, Offset, Size]:
        offset, real_size = shared_memory.malloc(ObjectType.ttorchtensor, bs * len(TTorchTensorOffsets))
        created_items_offsets: List[Offset] = list()
        try:
            numpy_ndarray_mapped_obj, numpy_ndarray_offset, numpy_ndarray_size = shared_memory.put_obj(tensor.numpy())
            created_items_offsets.append(numpy_ndarray_offset)
            write_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * TTorchTensorOffsets.numpy_ndarray_offset, numpy_ndarray_offset)
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

        numpy_ndarray_offset = read_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * TTorchTensorOffsets.numpy_ndarray_offset)
        numpy_ndarray_mapped_obj: ndarray = shared_memory.get_obj(numpy_ndarray_offset)
        mapped_torch_tensor: Tensor = from_numpy(numpy_ndarray_mapped_obj)
        return mapped_torch_tensor
    
    def destroy(self, shared_memory: 'SharedMemory', offset: Offset) -> None:
        if ObjectType.ttorchtensor != read_uint64(shared_memory.base_address, offset):
            raise WrongObjectTypeError

        numpy_ndarray_offset = read_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * TTorchTensorOffsets.numpy_ndarray_offset)
        shared_memory.destroy_obj(numpy_ndarray_offset)
        shared_memory.free(offset)
    
    def buffer(self, shared_memory: 'SharedMemory', offset: Offset) -> memoryview:
        if ObjectType.ttorchtensor != read_uint64(shared_memory.base_address, offset + bs * BaseObjOffsets.obj_type):
            raise WrongObjectTypeError

        numpy_ndarray_offset = read_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * TTorchTensorOffsets.numpy_ndarray_offset)
        return shared_memory.get_obj_buffer(numpy_ndarray_offset)
    
    def buffer_2(self, shared_memory: 'SharedMemory', offset: Offset) -> Tuple[int, int]:
        if ObjectType.ttorchtensor != read_uint64(shared_memory.base_address, offset + bs * BaseObjOffsets.obj_type):
            raise WrongObjectTypeError


        numpy_ndarray_offset = read_uint64(shared_memory.base_address, offset + bs * len(BaseObjOffsets) + bs * TTorchTensorOffsets.numpy_ndarray_offset)
        return shared_memory.get_obj_buffer_2(numpy_ndarray_offset)


# Add your own codecs to `codec_by_type`
codec_by_type: Dict[ObjectType, TBase] = {
    ObjectType.ttorchtensor: TTorchTensor(),
}

# Add your own types to `obj_type_map`
obj_type_map: Dict[Type, ObjectType] = {
    Tensor: ObjectType.ttorchtensor,
}

# Add your own base types to `obj_base_type_map`
obj_base_type_map: Dict[Type, ObjectType] = {
    Tensor: ObjectType.ttorchtensor,
}

numpy_types_collection_obj: ExternalTypesCollection = numpy_types_collection()
numpy_codec_by_type = numpy_types_collection_obj.codec_by_type
numpy_obj_type_map = numpy_types_collection_obj.obj_type_map
numpy_obj_base_type_map = numpy_types_collection_obj.obj_base_type_map
codec_by_type.update(numpy_codec_by_type)
obj_type_map.update(numpy_obj_type_map)
obj_base_type_map.update(numpy_obj_base_type_map)


def types_collection() -> ExternalTypesCollection:
    return ExternalTypesCollection(codec_by_type, obj_type_map, obj_base_type_map)
