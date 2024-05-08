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
__version__ = "4.4.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


cdef extern from "memory_access.h":
    void c_write_uint64(unsigned long long base_address, unsigned long long offset, unsigned long long value) nogil
    unsigned long long c_read_uint64(unsigned long long base_address, unsigned long long offset) nogil
    void c_write_int64(unsigned long long base_address, unsigned long long offset, long long value) nogil
    long long c_read_int64(unsigned long long base_address, unsigned long long offset) nogil
    void c_write_uint32(unsigned long long base_address, unsigned long long offset, unsigned int value) nogil
    unsigned int c_read_uint32(unsigned long long base_address, unsigned long long offset) nogil
    void c_write_int32(unsigned long long base_address, unsigned long long offset, int value) nogil
    int c_read_int32(unsigned long long base_address, unsigned long long offset) nogil
    void c_write_uint16(unsigned long long base_address, unsigned long long offset, unsigned short value) nogil
    unsigned short c_read_uint16(unsigned long long base_address, unsigned long long offset) nogil
    void c_write_int16(unsigned long long base_address, unsigned long long offset, short value) nogil
    short c_read_int16(unsigned long long base_address, unsigned long long offset) nogil
    void c_write_uint8(unsigned long long base_address, unsigned long long offset, unsigned char value) nogil
    unsigned char c_read_uint8(unsigned long long base_address, unsigned long long offset) nogil
    void c_write_int8(unsigned long long base_address, unsigned long long offset, char value) nogil
    char c_read_int8(unsigned long long base_address, unsigned long long offset) nogil
    void c_write_float(unsigned long long base_address, unsigned long long offset, float value) nogil
    float c_read_float(unsigned long long base_address, unsigned long long offset) nogil
    void c_write_double(unsigned long long base_address, unsigned long long offset, double value) nogil
    double c_read_double(unsigned long long base_address, unsigned long long offset) nogil
    void c_copy_memory(unsigned long long base_address, unsigned long long offset, unsigned long long size, unsigned long long source_offset) nogil
    void c_copy_memory_from(unsigned long long base_address, unsigned long long offset, unsigned long long size, unsigned long long source_offset) nogil
    void c_set_memory(unsigned long long base_address, unsigned long long offset, unsigned long long size, unsigned char value) nogil
    void c_zero_memory(unsigned long long base_address, unsigned long long offset, unsigned long long size) nogil
    unsigned long long c_mask_least_significant_bits(long long value, int n) nogil

cpdef void write_uint64(unsigned long long base_address, unsigned long long offset, unsigned long long value) noexcept:
    c_write_uint64(base_address, offset, value)

cpdef unsigned long long read_uint64(unsigned long long base_address, unsigned long long offset) noexcept:
    return c_read_uint64(base_address, offset)

cpdef void write_int64(unsigned long long base_address, unsigned long long offset, long long value) noexcept:
    c_write_int64(base_address, offset, value)

cpdef long long read_int64(unsigned long long base_address, unsigned long long offset) noexcept:
    return c_read_int64(base_address, offset)

cpdef void write_uint32(unsigned long long base_address, unsigned long long offset, unsigned int value) noexcept:
    c_write_uint32(base_address, offset, value)

cpdef unsigned int read_uint32(unsigned long long base_address, unsigned long long offset) noexcept:
    return c_read_uint32(base_address, offset)

cpdef void write_int32(unsigned long long base_address, unsigned long long offset, int value) noexcept:
    c_write_int32(base_address, offset, value)

cpdef int read_int32(unsigned long long base_address, unsigned long long offset) noexcept:
    return c_read_int32(base_address, offset)

cpdef void write_uint16(unsigned long long base_address, unsigned long long offset, unsigned short value) noexcept:
    c_write_uint16(base_address, offset, value)

cpdef unsigned short read_uint16(unsigned long long base_address, unsigned long long offset) noexcept:
    return c_read_uint16(base_address, offset)

cpdef void write_int16(unsigned long long base_address, unsigned long long offset, short value) noexcept:
    c_write_int16(base_address, offset, value)

cpdef short read_int16(unsigned long long base_address, unsigned long long offset) noexcept:
    return c_read_int16(base_address, offset)

cpdef void write_uint8(unsigned long long base_address, unsigned long long offset, unsigned char value) noexcept:
    c_write_uint8(base_address, offset, value)

cpdef unsigned char read_uint8(unsigned long long base_address, unsigned long long offset) noexcept:
    return c_read_uint8(base_address, offset)

cpdef void write_int8(unsigned long long base_address, unsigned long long offset, char value) noexcept:
    c_write_int8(base_address, offset, value)

cpdef char read_int8(unsigned long long base_address, unsigned long long offset) noexcept:
    return c_read_int8(base_address, offset)

cpdef void write_float(unsigned long long base_address, unsigned long long offset, float value) noexcept:
    c_write_float(base_address, offset, value)

cpdef float read_float(unsigned long long base_address, unsigned long long offset) noexcept:
    return c_read_float(base_address, offset)

cpdef void write_double(unsigned long long base_address, unsigned long long offset, double value) noexcept:
    c_write_double(base_address, offset, value)

cpdef double read_double(unsigned long long base_address, unsigned long long offset) noexcept:
    return c_read_double(base_address, offset)

cpdef void copy_memory(unsigned long long base_address, unsigned long long offset, unsigned long long size, unsigned long long source_offset) noexcept:
    c_copy_memory(base_address, offset, size, source_offset)

cpdef void copy_memory_from(unsigned long long base_address, unsigned long long offset, unsigned long long size, unsigned long long source_offset) noexcept:
    c_copy_memory_from(base_address, offset, size, source_offset)

cpdef void set_memory(unsigned long long base_address, unsigned long long offset, unsigned long long size, unsigned char value) noexcept:
    c_set_memory(base_address, offset, size, value)

cpdef void zero_memory(unsigned long long base_address, unsigned long long offset, unsigned long long size) noexcept:
    c_zero_memory(base_address, offset, size)

cpdef unsigned long long mask_least_significant_bits(long long value, int n) noexcept:
    return c_mask_least_significant_bits(value, n)

# cpdef unsigned long long list__get_item__impl(unsigned long long key, unsigned long long base_address, unsigned long long offset__pointer_to_internal_list, object get_obj_callback, unsigned long long & item_type, unsigned long long & need_to_raise_exception):
#     cdef unsigned long long pointer_to_internal_list
#     cdef unsigned long long item_type_offset
#     cdef unsigned long long item_value_offset
#     pointer_to_internal_list = c_read_uint64(base_address, offset__pointer_to_internal_list)
#     item_type_offset = pointer_to_internal_list + 32 + key * 16
#     item_value_offset = pointer_to_internal_list + 40 + key * 16
#     item_type = c_read_uint64(base_address, item_type_offset)
#     if item_type == 1:
#         return c_read_int64(base_address, item_value_offset)
#     elif item_type == 2:
#         return read_double(base_address, item_value_offset)
#     elif item_type == 3:
#         return c_read_uint64(base_address, item_value_offset)
#     elif item_type == 0:
#         item_offset = c_read_uint64(base_address, item_value_offset)
#         return get_obj_callback(item_offset)
#     else:
#         need_to_raise_exception = 1
#         return 0


cpdef object list__get_item(long long key, unsigned long long base_address, unsigned long long offset__pointer_to_internal_list, object get_obj_callback):
    cdef unsigned long long pointer_to_internal_list
    cdef unsigned long long item_type_offset
    cdef unsigned long long item_value_offset
    cdef unsigned long long item_type
    cdef unsigned long long unsigned_key
    cdef unsigned long long self_len
    cdef unsigned long long item_offset

    pointer_to_internal_list = c_read_uint64(base_address, offset__pointer_to_internal_list)
    self_len = read_uint64(base_address, pointer_to_internal_list + 24)
    if key < 0:
        key += self_len
    
    if key < 0 or key >= self_len:
        raise IndexError
    
    unsigned_key = key
    item_type_offset = pointer_to_internal_list + 32 + unsigned_key * 16
    item_value_offset = pointer_to_internal_list + 40 + unsigned_key * 16
    item_type = c_read_uint64(base_address, item_type_offset)
    
    if item_type == 2:
        return c_read_int64(base_address, item_value_offset)
    elif item_type == 3:
        return c_read_double(base_address, item_value_offset)
    elif item_type == 4:
        return bool(c_read_uint64(base_address, item_value_offset))
    elif item_type == 0:
        return None
    elif item_type == 1:
        item_offset = c_read_uint64(base_address, item_value_offset)
        return get_obj_callback(item_offset)
    else:
        raise ValueError


cpdef object list__get_item_as_offset(long long key, unsigned long long base_address, unsigned long long offset__pointer_to_internal_list):
    cdef unsigned long long pointer_to_internal_list
    cdef unsigned long long item_type_offset
    cdef unsigned long long item_value_offset
    cdef unsigned long long item_type
    cdef unsigned long long unsigned_key
    cdef unsigned long long self_len

    pointer_to_internal_list = c_read_uint64(base_address, offset__pointer_to_internal_list)
    self_len = read_uint64(base_address, pointer_to_internal_list + 24)
    if key < 0:
        key += self_len
    
    if key < 0 or key >= self_len:
        raise IndexError
    
    unsigned_key = key
    item_type_offset = pointer_to_internal_list + 32 + unsigned_key * 16
    item_value_offset = pointer_to_internal_list + 40 + unsigned_key * 16
    item_type = c_read_uint64(base_address, item_type_offset)
    
    if item_type == 2:
        return (item_type, c_read_uint64(base_address, item_value_offset))
    elif item_type == 3:
        return (item_type, c_read_uint64(base_address, item_value_offset))
    elif item_type == 4:
        return (item_type, c_read_uint64(base_address, item_value_offset))
    elif item_type == 0:
        return (item_type, 0)
    elif item_type == 1:
        return (item_type, c_read_uint64(base_address, item_value_offset))
    else:
        raise ValueError


cpdef void list__free_item(unsigned long long key, unsigned long long base_address, unsigned long long pointer_to_internal_list, object destroy_obj_method):
    cdef unsigned long long item_type_offset
    cdef unsigned long long item_type
    cdef unsigned long long unsigned_key
    cdef unsigned long long item_offset

    unsigned_key = key
    item_type = c_read_uint64(base_address, pointer_to_internal_list + 32 + unsigned_key * 16 + 0)
    if item_type == 1:
        item_offset = c_read_uint64(base_address, pointer_to_internal_list + 32 + unsigned_key * 16 + 8)
        destroy_obj_method(item_offset)
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

    item_type_offset = pointer_to_internal_list + 32 + unsigned_key * 16 + 0
    c_write_uint64(base_address, item_type_offset, 0)


cpdef void list__set_item(unsigned long long key, object value, unsigned long long base_address, unsigned long long offset__pointer_to_internal_list, unsigned int need_to_free_item, object destroy_obj_method, object put_obj_callback):
    cdef unsigned long long pointer_to_internal_list
    cdef unsigned long long item_type_offset
    cdef unsigned long long item_value_offset
    cdef unsigned long long item_type
    cdef unsigned long long unsigned_key
    cdef unsigned long long self_len
    cdef unsigned long long item_offset

    pointer_to_internal_list = read_uint64(base_address, offset__pointer_to_internal_list)
    self_len = read_uint64(base_address, pointer_to_internal_list + 24)
    if key < 0:
        key += self_len
    
    if key < 0 or key >= self_len:
        raise IndexError
    
    if need_to_free_item:
        list__free_item(key, base_address, pointer_to_internal_list, destroy_obj_method)
    
    unsigned_key = key
    item_type_offset = pointer_to_internal_list + 32 + unsigned_key * 16 + 0
    item_value_offset = pointer_to_internal_list + 32 + unsigned_key * 16 + 8
    if isinstance(value, int):
        c_write_int64(base_address, item_value_offset, value)
        item_type = 2
    elif isinstance(value, float):
        c_write_double(base_address, item_value_offset, value)
        item_type = 3
    elif isinstance(value, bool):
        c_write_uint64(base_address, item_value_offset, int(value))
        item_type = 4
    elif value is None:
        item_type = 0
    else:
        item_mapped_obj, item_offset, item_size = put_obj_callback(value)
        c_write_uint64(base_address, item_value_offset, item_offset)
        item_type = 1

    c_write_uint64(base_address, item_type_offset, item_type)


cpdef void list__set_item_as_offset(unsigned long long key, unsigned long long value_item_type, unsigned long long value_item_offset, unsigned long long base_address, unsigned long long offset__pointer_to_internal_list, unsigned int need_to_free_item, object destroy_obj_method):
    cdef unsigned long long pointer_to_internal_list
    cdef unsigned long long item_type_offset
    cdef unsigned long long item_value_offset
    cdef unsigned long long unsigned_key
    cdef unsigned long long self_len

    pointer_to_internal_list = read_uint64(base_address, offset__pointer_to_internal_list)
    self_len = read_uint64(base_address, pointer_to_internal_list + 24)
    if key < 0:
        key += self_len
    
    if key < 0 or key >= self_len:
        raise IndexError
    
    if need_to_free_item:
        list__free_item(key, base_address, pointer_to_internal_list, destroy_obj_method)
    
    unsigned_key = key
    item_type_offset = pointer_to_internal_list + 32 + unsigned_key * 16 + 0
    item_value_offset = pointer_to_internal_list + 32 + unsigned_key * 16 + 8
    if value_item_type == 2:
        c_write_int64(base_address, item_value_offset, value_item_offset)
    elif value_item_type == 3:
        c_write_double(base_address, item_value_offset, value_item_offset)
    elif value_item_type == 4:
        c_write_uint64(base_address, item_value_offset, value_item_offset)
    elif value_item_type == 0:
        pass
    else:
        c_write_uint64(base_address, item_value_offset, value_item_offset)
    
    c_write_uint64(base_address, item_type_offset, value_item_type)
