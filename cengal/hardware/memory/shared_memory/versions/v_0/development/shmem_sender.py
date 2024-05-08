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


from cengal.hardware.memory.shared_memory import SharedMemory, wait_my_turn, FreeMemoryChunkNotFoundError, numpy_array_memory_size
from cengal.time_management.cpu_clock_cycles import perf_counter
from cengal.time_management.sleep_tools import sleep
import numpy as np
import time

shared_memory_name: str = 'shmem_message_transmit'

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


shape = (100, 100, 3)
shared_memory_size = numpy_array_memory_size(shape, np.uint8) * 2
if 1024 * 10 > shared_memory_size:
    shared_memory_size = 1024 * 10

print(f'{shared_memory_size=}')
creator: SharedMemory = SharedMemory(shared_memory_name, True, shared_memory_size)

img = np.random.randint(0, 255, size=shape, dtype=np.uint8)
print(img)

def main():
    print('Sender is waiting for consumers')
    creator.wait_consumer_ready()
    print('Sender is ready')
    try:
        index = 0
        while True:
            start = stop = 0
            x = b''
            try:
                with wait_my_turn(creator):
                    start = perf_counter()
                    x = img.tobytes()
                    creator.put_message(x)
                    stop = perf_counter()
                
                print()
                print(type(x), len(x))
                if x:
                    print(x[:10], '...', x[-10:])
                
                print('Message sent')
                delta_time = stop - start
                print("Writing Duration:", delta_time * 1000, "ms")
                if delta_time:
                    print("Speed:", 1 / delta_time, "puts/s")
            except FreeMemoryChunkNotFoundError as ex:
                pass
            
    except KeyboardInterrupt:
        pass
    finally:
        with wait_my_turn(creator):
            creator.put_message(None)

if '__main__' == __name__:
    try:
        main()
    finally:
        creator._shared_memory.close()
        creator._shared_memory.unlink()