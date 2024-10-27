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


from cengal.hardware.memory.shared_memory import SharedMemory, wait_my_turn, numpy_array_memory_size, ensure_adjusted_pythonhashseed
from cengal.time_management.cpu_clock_cycles import perf_counter
from cengal.performance_test_lib import measure_time
from cengal.time_management.sleep_tools import sleep
import numpy as np
import time


shared_memory_name: str = 'shmem_message_transmit'

shape = (100, 100, 30)
dtype=np.uint8
consumer: SharedMemory = SharedMemory(shared_memory_name, False)
print(f'shared_memory_size={consumer.size}')


def main():
    consumer.init_consumer()
    print('Consumer is ready')
    need_to_stop = False
    while not need_to_stop:
        messages_num = 0
        start = stop = 0
        obj = None
        messages = list()
        with wait_my_turn(consumer):
            start = perf_counter()
            while consumer.has_messages():
                with measure_time('take_message_2'):
                    obj, obj_offset = consumer.take_message_2()
                
                messages.append(obj)
                if obj is None:
                    need_to_stop = True
                else:
                    _ = np.frombuffer(obj, dtype=dtype).reshape(shape)
                
                messages_num += 1
                if obj_offset:
                    consumer.destroy_object(obj_offset)
                
                if need_to_stop:
                    break

            stop = perf_counter()
        
        if messages_num:
            print()
            for obj in messages:
                if obj:
                    print(obj[:10], '...', obj[-10:])
                else:
                    print(obj)
            
            delta_time = stop - start
            print(f"Read Duration for reading {messages_num} messages:", delta_time * 1000, "ms")
            if delta_time:
                print(f"Read Speed for reading {messages_num} messages:", messages_num / delta_time, "msg/s")


if '__main__' == __name__:
    ensure_adjusted_pythonhashseed(pythonhashseed=0)  # Ensure that the hash seed is adjusted for this process group
    # ensure_adjusted_scientific()  # Ensure (for this process group) that: 1) the hash seed is adjusted; 2) interpreter optimizations ('-OO') are turned on; 3) the integer string conversion length limitation is turned off
    with consumer:
        main()