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


IF (UNAME_SYSNAME == "Windows") and (UNAME_MACHINE in ("x86_64", "x86", "i386", "i686", "AMD64")):
    cdef extern from "<immintrin.h>" nogil:
        void _mm_pause()


    cpdef void mm_pause():
        _mm_pause()


ELIF (UNAME_SYSNAME in ("Linux", "Darwin")) and (UNAME_MACHINE in ("x86_64", "x86", "i386", "i686", "AMD64")):
    cdef extern from "<immintrin.h>" nogil:
        void _mm_pause()


    cpdef void mm_pause():
        _mm_pause()


ELSE:
    cpdef void mm_pause():
        pass


IF UNAME_SYSNAME == "Windows":
    from libc.time cimport clock, CLOCKS_PER_SEC, clock_t

    cdef extern from "Windows.h":
        int SwitchToThread() nogil


    cpdef void cython_spinwait(double sleep_time):
        cdef clock_t start, end

        start = clock()
        end = start + <clock_t>(sleep_time * CLOCKS_PER_SEC)

        while clock() < end:
            mm_pause()
            SwitchToThread()
            mm_pause()
    

    hps_sleep = high_precision_sync_sleep = cython_spinwait

ELIF UNAME_SYSNAME in ("Linux", "Darwin"):
    cdef extern from "time.h":
        struct timespec:
            long tv_sec
            long tv_nsec


    cdef extern from "unistd.h":
        int nanosleep(const timespec *req, timespec *rem) nogil


    cpdef void cython_nanosleep(double sleep_time):
        cdef timespec sleep_req
        cdef timespec sleep_rem

        sleep_req.tv_sec = <long>(sleep_time)
        sleep_req.tv_nsec = <long>((sleep_time - sleep_req.tv_sec) * 1e9)

        while nanosleep(&sleep_req, &sleep_rem) == -1:
            mm_pause()
            sleep_req = sleep_rem
            mm_pause()
    
    hps_sleep = high_precision_sync_sleep = cython_nanosleep

ELIF UNAME_SYSNAME == "Emscripten":
    from libc.stdint cimport uint32_t

    cdef extern from "emscripten.h":
        void emscripten_sleep(uint32_t ms) nogil

    cpdef void cython_emscripten_sleep(double sleep_time):
        cdef uint32_t sleep_ms

        sleep_ms = <uint32_t>(sleep_time * 1e3)

        emscripten_sleep(sleep_ms)
    
    
    hps_sleep = high_precision_sync_sleep = cython_emscripten_sleep
