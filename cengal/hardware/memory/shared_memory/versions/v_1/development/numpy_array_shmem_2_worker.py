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
__version__ = "4.4.1"
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


shape = (10, 10, 3)
dtype = np.float64

consumer: SharedMemory = SharedMemory(shared_memory_name)
print(f'shared_memory_size={consumer.size}')


def main():
    print('Consumer is waiting for sender')
    consumer.init_consumer()
    print(f'shared_memory_size={consumer.size}')
    print('Sender is ready')

    consumer.wait_for_messages()
    with test_run_time('Taking control', 1, ignore_index=True):
        with wait_my_turn(consumer):
            flow_control: Tuple[FlowControl, float] = consumer.take_message()

    consumer.wait_for_messages()
    with test_run_time('Taking numpy array', 1, ignore_index=True):
        with wait_my_turn(consumer):
            _, holder_offset = consumer.take_message_2()
            np_arr: np.ndarray = make_numpy_array_from_obj_offset(consumer, holder_offset, shape, dtype)
    
    with test_run_time('Whole processing', 1, ignore_index=True):
        while True:
            with wait_my_turn(consumer):
                request_type = flow_control[0]
                if FlowControl.no_requests.value == request_type:
                    continue
                if FlowControl.result_ready.value == request_type:
                    continue
                elif FlowControl.multiply.value == request_type:
                    np_arr *= flow_control[1]
                    flow_control[0] = FlowControl.result_ready.value
                elif FlowControl.add.value == request_type:
                    np_arr += flow_control[1]
                    flow_control[0] = FlowControl.result_ready.value
                elif FlowControl.subtract.value == request_type:
                    np_arr -= flow_control[1]
                    flow_control[0] = FlowControl.result_ready.value
                elif FlowControl.divide.value == request_type:
                    np_arr /= flow_control[1]
                    flow_control[0] = FlowControl.result_ready.value
                elif FlowControl.divide.value == request_type:
                    np_arr /= flow_control[1]
                    flow_control[0] = FlowControl.result_ready.value
                elif FlowControl.finish_your_work.value == request_type:
                    flow_control[0] = FlowControl.result_ready.value
                    break
                else:
                    raise RuntimeError(f'Unknown request type: {request_type}')
    
    print('Done.')


if '__main__' == __name__:
    with consumer:
        main()
