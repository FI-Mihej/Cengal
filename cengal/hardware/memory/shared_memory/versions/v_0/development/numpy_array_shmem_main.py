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


from cengal.hardware.memory.shared_memory import SharedMemory, wait_my_turn, FreeMemoryChunkNotFoundError, \
    numpy_array_made_from_pointer_memory_size, make_numpy_array_from_obj_offset, ObjBufferIsSmallerThanRequestedNumpyArrayError
from cengal.performance_test_lib import test_run_time
from enum import IntEnum
import numpy as np
import ctypes
from typing import Tuple


class FlowControl(IntEnum):
    no_requests = 0
    multiply = 1
    add = 2
    subtract = 3
    divide = 4
    finish_your_work = 5
    result_ready = 6


shared_memory_name: str = 'shmem_numpy_array'

# `multiprocessing.SharedMemory` requires this cleanup in order to handle the case 
# when the previous run of the program was terminated unexpectedly:
try:
    import _posixshmem
    from multiprocessing import resource_tracker
    shm_name = f'/{shared_memory_name}'
    _posixshmem.shm_unlink(shm_name)
    resource_tracker.unregister(shm_name, "shared_memory")
except FileNotFoundError:
    pass


shape = (10, 10, 3)
shared_memory_size = numpy_array_made_from_pointer_memory_size(shape, ctypes.c_double) * 2
if 1024 * 10 > shared_memory_size:
    shared_memory_size = 1024 * 10

print(f'{shared_memory_size=}')
creator: SharedMemory = SharedMemory(shared_memory_name, True, shared_memory_size)

def main():
    print('Sender is waiting for consumers')
    creator.wait_consumer_ready()
    print('Sender is ready')

    np_arr = None
    with wait_my_turn(creator):
        with test_run_time('Initialization Duration', 1, ignore_index=True):
            flow_control: Tuple[FlowControl, float] = creator.put_message([FlowControl.no_requests.value, None])

            holder: bytes = bytes(numpy_array_made_from_pointer_memory_size(shape, ctypes.c_double))
            _, holder_offset = creator.put_message_2(holder)
            np_arr: np.ndarray = make_numpy_array_from_obj_offset(creator, holder_offset, shape, ctypes.c_double)
            np_arr.fill(0.0)

    with wait_my_turn(creator):
        with test_run_time('Request Add', 1, ignore_index=True):
            flow_control[0] = FlowControl.add.value
            flow_control[1] = 2.5
    
    with test_run_time('Wait for Add result', 1, ignore_index=True):
        while True:
            with wait_my_turn(creator):
                if FlowControl.result_ready != flow_control[0]:
                    continue

                flow_control[0] = FlowControl.no_requests.value
                break
    
    with wait_my_turn(creator):
        print(np_arr)
        print()
    
    with wait_my_turn(creator):
        with test_run_time('Adjusting values and request Multiply', 1, ignore_index=True):
            np_arr[0, 0, 0] = 100.0
            np_arr[1, 1, 1] = 200.0
            np_arr[2, 2, 2] = 300.0
            np_arr[3, 3, 0] = 400.0
            np_arr[4, 4, 1] = 500.0
            np_arr[5, 5, 2] = 600.0
            np_arr[6, 6, 0] = 700.0
            np_arr[7, 7, 1] = 800.0
            np_arr[8, 8, 2] = 900.0
            np_arr[9, 9, 0] = 1000.0

            flow_control[0] = FlowControl.multiply.value
            flow_control[1] = 15.0
        
        print(np_arr)
        print()
    
    with test_run_time('Wait for Multiply results', 1, ignore_index=True):
        while True:
            with wait_my_turn(creator):
                if FlowControl.result_ready != flow_control[0]:
                    continue

                flow_control[0] = FlowControl.no_requests.value
                break
    
    with wait_my_turn(creator):
        print(np_arr)
        print()

    with test_run_time('Shutting down receiver', 1, ignore_index=True):
        with wait_my_turn(creator):
            flow_control[0] = FlowControl.finish_your_work.value
    
        while True:
            with wait_my_turn(creator):
                if FlowControl.result_ready != flow_control[0]:
                    continue

                break
    
    print('Done.')


if '__main__' == __name__:
    try:
        main()
    finally:
        creator._shared_memory.close()
        creator._shared_memory.unlink()