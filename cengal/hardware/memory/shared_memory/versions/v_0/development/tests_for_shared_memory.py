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
__version__ = "4.3.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.performance_test_lib import PrecisePerformanceTestTracer
from cengal.introspection.inspect import func_name
from threading import Lock, RLock
from pprint import pprint
from typing import Callable


def func_perf_test(func: Callable, *args, **kwargs):
    tr = PrecisePerformanceTestTracer(1.0)
    while tr.iter():
        func(*args, **kwargs)

    with tr as fast_iter:
        for i in fast_iter:
            func(*args, **kwargs)

    print('{}(): {} iter/s; {} seconds; {} iterations'.format(func_name(func), tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))


from cengal.hardware.memory.shared_memory import *
from cengal.time_management.cpu_clock import cpu_clock
from cengal.time_management.high_precision_sync_sleep import hps_sleep
from multiprocessing import Process
from multiprocessing.resource_tracker import unregister
import _posixshmem

try:
    shm_name = '/test_shmem'
    _posixshmem.shm_unlink(shm_name)
    unregister(shm_name, "shared_memory")
except FileNotFoundError:
    pass

creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

try:
    print(f'Free memory search start: {creator.get_free_memory_search_start()}:{creator.read_free_memory_search_start()}')
    creator.print_mem(creator.get_data_start_offset(), 50, 'Initial state: {}')
    offset, size = creator.malloc(ObjectType.tbool, 1)
    print(f'Free memory search start: {creator.get_free_memory_search_start()}:{creator.read_free_memory_search_start()}')
    creator.print_mem(creator.get_data_start_offset(), 50, f'Malloc bool: {offset=}, {size=}; {{}}')
    offset, size = creator.realloc(offset, 11)
    print(f'Free memory search start: {creator.get_free_memory_search_start()}:{creator.read_free_memory_search_start()}')
    creator.print_mem(creator.get_data_start_offset(), 50, f'Realloc bool: {offset=}, {size=}; {{}}')
    result = creator.free(offset)
    print(f'Free memory search start: {creator.get_free_memory_search_start()}:{creator.read_free_memory_search_start()}')
    creator.print_mem(creator.get_data_start_offset(), 50, f'Free bool: {result=}; {{}}')
    creator.set_free_memory_search_start(0)
    print(f'Free memory search start: {creator.get_free_memory_search_start()}:{creator.read_free_memory_search_start()}')
    creator.commit_free_memory_search_start()
    print(f'Free memory search start: {creator.get_free_memory_search_start()}:{creator.read_free_memory_search_start()}')
    print()
    creator.print_mem(creator.get_data_start_offset(), 50, 'Initial state: {}')
    print(f'Free memory search start: {creator.get_free_memory_search_start()}:{creator.read_free_memory_search_start()}')
    offset, size = creator.malloc(ObjectType.tbool, 1)
    print(f'Free memory search start: {creator.get_free_memory_search_start()}:{creator.read_free_memory_search_start()}')
    creator.print_mem(creator.get_data_start_offset(), 50, f'Malloc bool: {offset=}, {size=}; {{}}')
    offset, size = creator.realloc(offset, 11)
    print(f'Free memory search start: {creator.get_free_memory_search_start()}:{creator.read_free_memory_search_start()}')
    creator.print_mem(creator.get_data_start_offset(), 50, f'Realloc bool: {offset=}, {size=}; {{}}')
    result = creator.free(offset)
    print(f'Free memory search start: {creator.get_free_memory_search_start()}:{creator.read_free_memory_search_start()}')
    creator.print_mem(creator.get_data_start_offset(), 50, f'Free bool: {result=}; {{}}')
    creator.set_free_memory_search_start(0)
    print(f'Free memory search start: {creator.get_free_memory_search_start()}:{creator.read_free_memory_search_start()}')
    creator.commit_free_memory_search_start()
    print(f'Free memory search start: {creator.get_free_memory_search_start()}:{creator.read_free_memory_search_start()}')
    print()


    print('=================================================================')
    print()
    values = [
        0,
        1,
        999999999999,
        -1,
        -999999999999,
        0.0,
        1.0,
        999999999999.0,
        -1.0,
        -999999999999.0,
        (1,),
        [1],
        (1, 2),
        [1, 2],
        (1, [2, 3]),
        {1: 1, 2: 2},
        {1: 1, 2: [2, (3,)]},
        'test',
        'test'.encode('utf-8'),
        bytearray('test'.encode('utf-8')),
        True,
        False,
        {
            'test': 1,
            'test2': 2.0,
            'test3': 'test',
            'test4': [
                1, 
                2.0, 
                True, 
                False, 
                'test', 
                'test'.encode('utf-8'), 
                bytearray('test'.encode('utf-8')), 
                ('hello', 1),
                ['world', 2.0],
                {
                    'hello': [1, (2, 3)],
                    'world': 'world',
                }
            ],
        }
    ]
    print(f'Free memory search start: {creator.get_free_memory_search_start()}:{creator.read_free_memory_search_start()}')
    creator.print_mem(creator.get_free_memory_search_start(), 100, 'Initial state: {}')
    creator.print_mem(creator.get_data_start_offset(), 500, 'Initial state: {}')
    for val in values:
        print(f'>> Put message: {val} ...')
        creator.put_message(val)
        print(f'>\t> Free memory search start: {creator.get_free_memory_search_start()}:{creator.read_free_memory_search_start()}')
        text_data = f'{val=}'.replace('{', '{{').replace('}', '}}')
        creator.print_mem(creator.get_free_memory_search_start(), 100, f'>\t> 0 - put_message: {text_data}; {{}}')
        creator.print_mem(creator.get_data_start_offset(), 500, f'>\t> 1 - put_message: {text_data}; {{}}')
        print('>> Taking message...')
        assert(val == creator.take_message())
        print(f'>\t> Free memory search start: {creator.get_free_memory_search_start()}:{creator.read_free_memory_search_start()}')
        creator.print_mem(creator.get_free_memory_search_start(), 100, f'>\t> 0 - take_message: {text_data}; {{}}')
        creator.print_mem(creator.get_data_start_offset(), 500, f'>\t> 1 - take_message: {text_data}; {{}}')
        print('>> OK')
        print()
finally:
    creator._shared_memory.close()
    creator._shared_memory.unlink()
