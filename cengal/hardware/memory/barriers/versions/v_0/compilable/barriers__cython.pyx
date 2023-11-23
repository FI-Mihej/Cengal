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
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


IF UNAME_SYSNAME == "Windows":
    cdef extern from "Windows.h":
        void MemoryBarrier()

    
    cpdef void memory_barrier():
        MemoryBarrier()
    
    
    full_memory_barrier = memory_barrier

ELSE:
    cdef extern from "stdatomic.h":
        void atomic_thread_fence(int)


    cdef int _MEMORY_ORDER_RELAXED = 0
    cdef int _MEMORY_ORDER_CONSUME = 1
    cdef int _MEMORY_ORDER_ACQUIRE = 2
    cdef int _MEMORY_ORDER_RELEASE = 3
    cdef int _MEMORY_ORDER_ACQ_REL = 4
    cdef int _MEMORY_ORDER_SEQ_CST = 5


    MEMORY_ORDER_RELAXED = _MEMORY_ORDER_RELAXED
    MEMORY_ORDER_CONSUME = _MEMORY_ORDER_CONSUME
    MEMORY_ORDER_ACQUIRE = _MEMORY_ORDER_ACQUIRE
    MEMORY_ORDER_RELEASE = _MEMORY_ORDER_RELEASE
    MEMORY_ORDER_ACQ_REL = _MEMORY_ORDER_ACQ_REL
    MEMORY_ORDER_SEQ_CST = _MEMORY_ORDER_SEQ_CST


    cpdef void py_atomic_thread_fence(int order):
        cdef int c_order = <int>order
        atomic_thread_fence(c_order)


    cpdef void py_atomic_thread_fence__memory_order_relaxed():
        atomic_thread_fence(_MEMORY_ORDER_RELAXED)


    cpdef void py_atomic_thread_fence__memory_order_consume():
        atomic_thread_fence(_MEMORY_ORDER_CONSUME)


    cpdef void py_atomic_thread_fence__memory_order_acquire():
        atomic_thread_fence(_MEMORY_ORDER_ACQUIRE)


    cpdef void py_atomic_thread_fence__memory_order_release():
        atomic_thread_fence(_MEMORY_ORDER_RELEASE)


    cpdef void py_atomic_thread_fence__memory_order_acq_rel():
        atomic_thread_fence(_MEMORY_ORDER_ACQ_REL)


    cpdef void py_atomic_thread_fence__memory_order_seq_cst():
        atomic_thread_fence(_MEMORY_ORDER_SEQ_CST)


    full_memory_barrier = py_atomic_thread_fence__memory_order_seq_cst


IF (UNAME_SYSNAME == "Windows") and (UNAME_MACHINE in ("x86_64", "x86", "i386", "i686", "AMD64")):
    cdef extern from "<emmintrin.h>" nogil:
        void _mm_mfence()


    cdef extern from "<emmintrin.h>" nogil:
        void _mm_sfence()


    cdef extern from "<emmintrin.h>" nogil:
        void _mm_lfence()


    cdef extern from "<immintrin.h>" nogil:
        void _mm_pause()


    cdef extern from "emmintrin.h":
        void _mm_clflush(void* p)


    cpdef void mm_mfence():
        _mm_mfence()


    cpdef void mm_sfence():
        _mm_sfence()


    cpdef void mm_lfence():
        _mm_lfence()


    cpdef void mm_pause():
        _mm_pause()


    cpdef void mm_clflush(int p):
        _mm_clflush(<void*> p)

    
    cpdef void sync_synchronize():
        MemoryBarrier()


    full_memory_barrier = memory_barrier

ELIF (UNAME_SYSNAME in ("Linux", "Darwin")) and (UNAME_MACHINE in ("x86_64", "x86", "i386", "i686", "AMD64")):
    cdef extern from "<emmintrin.h>" nogil:
        void _mm_mfence()


    cdef extern from "<emmintrin.h>" nogil:
        void _mm_sfence()


    cdef extern from "<emmintrin.h>" nogil:
        void _mm_lfence()


    cdef extern from "<immintrin.h>" nogil:
        void _mm_pause()


    cdef extern from "<emmintrin.h>" nogil:
        void _mm_clflush(void* p)


    cdef extern from * nogil:
        void __sync_synchronize()


    cdef extern from "stdlib.h" nogil:
        void __clear_cache(char* beg, char* end)


    cpdef void mm_mfence():
        _mm_mfence()


    cpdef void mm_sfence():
        _mm_sfence()


    cpdef void mm_lfence():
        _mm_lfence()


    cpdef void mm_pause():
        _mm_pause()

    
    cpdef void memory_barrier():
        _mm_mfence()


    cpdef void mm_clflush(int p):
        _mm_clflush(<void*> p)

    
    cpdef void sync_synchronize():
        __sync_synchronize()


    # An alternative to mm_clflush() in GCC and Clang compilers
    cpdef void clear_cache(int beg, int end) nogil:
        __clear_cache(<char*>beg, <char*>end)


    full_memory_barrier = mm_mfence

ELIF (UNAME_SYSNAME == 'Windows') and UNAME_MACHINE.startswith("arm"):
    cdef extern from "arm64_neon.h" nogil:
        void __iso_volatile_store16(void* p, unsigned long long val)


    # An alternative to mm_clflush() for ARM in Visual Studio compiler
    cpdef void iso_volatile_store16(int p, unsigned long long val) nogil:
        __iso_volatile_store16(<void*> p, val)


    full_memory_barrier = memory_barrier


    cpdef void mm_mfence():
        MemoryBarrier()


    cpdef void mm_sfence():
        MemoryBarrier()


    cpdef void mm_lfence():
        MemoryBarrier()


    cpdef void mm_pause():
        pass

    
    cpdef void sync_synchronize():
        MemoryBarrier()


    full_memory_barrier = memory_barrier

ELIF UNAME_SYSNAME in ("Linux", "Darwin") and UNAME_MACHINE.startswith("arm"):
    cdef extern from * nogil:
        void __sync_synchronize()

    
    cpdef void sync_synchronize():
        __sync_synchronize()


    cdef extern from "stdlib.h" nogil:
        void __clear_cache(char* beg, char* end)


    # An alternative to mm_clflush() for ARM in GCC and Clang compilers
    cpdef void clear_cache(int beg, int end) nogil:
        __clear_cache(<char*>beg, <char*>end)


    full_memory_barrier = sync_synchronize


    cpdef void mm_mfence():
        __sync_synchronize()


    cpdef void mm_sfence():
        __sync_synchronize()


    cpdef void mm_lfence():
        __sync_synchronize()


    cpdef void mm_pause():
        pass

    
    cpdef void memory_barrier():
        __sync_synchronize()

ELIF UNAME_SYSNAME == "Emscripten":
    cdef extern from * nogil:
        void __sync_synchronize()

    
    cpdef void sync_synchronize():
        __sync_synchronize()


    cdef extern from "emscripten/atomics.h" nogil:
        void emscripten_atomic_fence()


    # Probably can be used as an alternative to mm_clflush() for Emscripten
    cpdef void py_emscripten_atomic_fence() nogil:
        emscripten_atomic_fence()

    
    full_memory_barrier = emscripten_atomic_fence


    cpdef void mm_mfence():
        __sync_synchronize()


    cpdef void mm_sfence():
        __sync_synchronize()


    cpdef void mm_lfence():
        __sync_synchronize()


    cpdef void mm_pause():
        pass

    
    cpdef void memory_barrier():
        __sync_synchronize()

ELSE:
    full_memory_barrier = py_atomic_thread_fence__memory_order_seq_cst


    cpdef void mm_mfence():
        atomic_thread_fence(_MEMORY_ORDER_SEQ_CST)


    cpdef void mm_sfence():
        atomic_thread_fence(_MEMORY_ORDER_SEQ_CST)


    cpdef void mm_lfence():
        atomic_thread_fence(_MEMORY_ORDER_SEQ_CST)


    cpdef void mm_pause():
        pass

    
    cpdef void sync_synchronize():
        atomic_thread_fence(_MEMORY_ORDER_SEQ_CST)

    
    cpdef void memory_barrier():
        atomic_thread_fence(_MEMORY_ORDER_SEQ_CST)


IF UNAME_SYSNAME == "Windows":
    full_memory_barrier = memory_barrier
