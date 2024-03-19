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
__version__ = "4.2.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


# cython: language_level=3
# coding=utf-8





from cpython cimport bool
from libc.stdint cimport int64_t

cdef extern from "Python.h":
    object PyLong_FromLong(long v)


cdef class IDGeneratorInt:
    cdef public int64_t counter

    def __init__(self):
        self.counter = 0

    cpdef int64_t get_new_id(self):
        cdef int64_t current_counter = self.counter
        self.counter += 1
        return current_counter

    cpdef remove_id(self, int64_t id_to_be_removed):
        pass

    cpdef clear(self):
        self.counter = 0

    def __call__(self):
        return self.get_new_id()


cdef class IDGeneratorUUID:
    cdef public int64_t counter
    cdef public object uuid

    def __init__(self):
        self.counter = 0
        self.uuid = __import__('uuid')  # Importing uuid in a way compatible with Cython

    cpdef get_new_id(self):
        cdef int64_t seq = self.counter
        self.counter += 1
        # Directly use the Python object without C type declaration
        return self.uuid.uuid1(clock_seq=seq).hex

    cpdef remove_id(self, id_to_be_removed):
        pass

    cpdef clear(self):
        self.counter = 0

    def __call__(self):
        return self.get_new_id()


cdef class IDGeneratorFakeUUID:
    cdef public int64_t counter

    def __init__(self):
        self.counter = 0

    cpdef get_new_id(self):
        cdef int64_t current_counter = self.counter
        self.counter += 1
        return str(PyLong_FromLong(current_counter))

    cpdef remove_id(self, object id_to_be_removed):
        pass

    cpdef clear(self):
        self.counter = 0

    def __call__(self):
        return self.get_new_id()


# cdef class IDGenerator:
#     cdef public object gen
#     cdef public object generator_type

#     def __init__(self, object generator_type = None):
#         self.gen = None
#         if generator_type is None:
#             self.generator_type = 0
#         else:
#             self.generator_type = generator_type.value

#         # Incorporate the UUID presence check here
#         uuid_present = self._check_uuid_availability()

#         if 0 == self.generator_type:
#             self.gen = IDGeneratorInt()
#         elif 1 == self.generator_type:
#             if uuid_present:
#                 self.gen = IDGeneratorUUID()
#             else:
#                 self.gen = IDGeneratorFakeUUID()
#         elif 2 == self.generator_type:
#             raise NotImplementedError
#         else:
#             raise RuntimeError('Wrong `generator_type` value')

#     cdef bool _check_uuid_availability(self):
#         try:
#             __import__('uuid')
#             return True
#         except ImportError:
#             return False

#     cpdef get_new_id(self):
#         return self.gen.get_new_id()

#     cpdef remove_id(self, id_to_be_removed):
#         self.gen.remove_id(id_to_be_removed)

#     cpdef clear(self):
#         self.gen.clear()

#     def __call__(self):
#         return self.gen.get_new_id()


cdef bool _check_uuid_availability():
    try:
        __import__('uuid')
        return True
    except ImportError:
        return False


cpdef IDGenerator(object generator_type = None):
    gen = None
    if generator_type is None:
        generator_type = 0
    else:
        generator_type = generator_type.value

    # Incorporate the UUID presence check here
    uuid_present = _check_uuid_availability()

    if 0 == generator_type:
        return IDGeneratorInt()
    elif 1 == generator_type:
        if uuid_present:
            return IDGeneratorUUID()
        else:
            return IDGeneratorFakeUUID()
    elif 2 == generator_type:
        raise NotImplementedError
    else:
        raise RuntimeError('Wrong `generator_type` value')
