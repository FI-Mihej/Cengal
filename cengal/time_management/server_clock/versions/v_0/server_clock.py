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

import time
import threading
from contextlib import contextmanager


"""
This module is usefull for Linux kernels before 3.17 (Ubuntu before 15.04). It is not usefull for Windows.
Before version 3.17, fetching the current time in the Linux kernel involved a system call, which is relatively expensive in terms of performance.
It was Ubuntu 15.04 (Vivid Vervet) that included Linux kernel 3.19 by default, so it benefited from the improved time fetching mechanism introduced in 3.17
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


__server_clock_var = 0
__global_timer = None
__global_semaphore = threading.RLock()
__timer_interval = 0.2  # in seconds (float value)
__is_need_to_stop_clock = False


def get_server_clock():
    # return time.time()

    global __server_clock_var
    global __global_timer
    global __global_semaphore
    global __is_need_to_stop_clock

    if __global_timer is None:
        with __global_semaphore:
            __is_need_to_stop_clock = False
            __server_clock_var = time.time()
            __global_timer = threading.Timer(__timer_interval, __update_server_clock)
            __global_timer.start()
    result = __server_clock_var

    return result


def stop_server_clock():
    global __server_clock_var
    global __global_timer
    global __global_semaphore
    global __is_need_to_stop_clock

    with __global_semaphore:
        __is_need_to_stop_clock = True
        if __global_timer is not None:
            __global_timer.cancel()


def __update_server_clock():
    global __server_clock_var
    global __global_timer
    global __global_semaphore
    global __is_need_to_stop_clock

    with __global_semaphore:
        __server_clock_var = time.time()
        if not __is_need_to_stop_clock:
            __global_timer = threading.Timer(__timer_interval, __update_server_clock)
            __global_timer.start()


@contextmanager
def server_clock():
    try:
        yield get_server_clock
    except:
        raise
    finally:
        stop_server_clock()
