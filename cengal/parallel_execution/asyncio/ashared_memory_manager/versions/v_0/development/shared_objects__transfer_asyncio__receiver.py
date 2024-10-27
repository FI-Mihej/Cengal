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


__all__ = [
]


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


from cengal.hardware.memory.shared_memory import *
from cengal.parallel_execution.asyncio.ashared_memory_manager import *
from cengal.time_management.cpu_clock import perf_counter

import asyncio


ashared_memory_manager: ASharedMemoryManager = ASharedMemoryManager(SharedMemory('shared_objects'))


async def receiver():
    async with ashared_memory_manager as asmm:
        print('Receiver is ready.')

        # An each coroutine should get its own context manager (ASharedMemoryContextManager). Either `asmm` or `ashared_memory_manager` can be used
        ashared_memory_context_manager: ASharedMemoryContextManager = asmm()

        done = False
        msgs_received = 0
        async with ashared_memory_context_manager.if_has_messages() as shared_memory:
            mapped_flag_holder: List[bool] = shared_memory.value.take_message()
            mapped_flag_holder[0] = True
            done = mapped_flag_holder[1]
        
        start_time = perf_counter()

        while not done:
            async with ashared_memory_context_manager.if_has_messages() as shared_memory:
                while shared_memory.value.has_messages():
                    some_binary, obj_offset = shared_memory.value.take_message_2()
                    shared_memory.value.destroy_obj(obj_offset)
                    msgs_received += 1
                    mapped_flag_holder[0] = True
                    done = mapped_flag_holder[1]
                
        transfer_time = perf_counter() - start_time
        print(f'Transfer throughput ({len(some_binary)} * {msgs_received} = {(len(some_binary) * msgs_received)} bytes per {transfer_time} seconds): {(len(some_binary) * msgs_received) / transfer_time:.2f} bytes per second')
        print()

        print('Receiver is done.')


if __name__ == '__main__':
    ensure_adjusted_pythonhashseed(pythonhashseed=0)  # Ensure that the hash seed is adjusted for this process group
    # ensure_adjusted_scientific()  # Ensure (for this process group) that: 1) the hash seed is adjusted; 2) interpreter optimizations ('-OO') are turned on; 3) the integer string conversion length limitation is turned off
    print('Receiver is starting its work.')
    asyncio.run(receiver())
    print('Receiver has finished its work.')
