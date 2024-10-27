from cengal.hardware.memory.shared_memory import *
from cengal.parallel_execution.asyncio.ashared_memory_manager import *

import asyncio
from typing import List


async def my_coro(asmm: ASharedMemoryManager, coro_id):
    asmcm: ASharedMemoryContextManager = asmm()
    async with asmcm.if_has_messages() as shared_memory:
        mapped_flag_holder: List[bool] = shared_memory.value.take_message()


async def receiver():
    # Connect to created named shared memory instance as a consumer
    ashared_memory_manager: ASharedMemoryManager = ASharedMemoryManager(SharedMemory('shared_objects'))
    async with ashared_memory_manager as asmm:
        print('Consumer is ready.')

        # An each coroutine should get its own context manager (ASharedMemoryContextManager). Either `asmm` or `ashared_memory_manager` can be used
        asmcm: ASharedMemoryContextManager = asmm()
        
        # Example 0: use your shared memory in same coroutine
        async with asmcm.if_has_messages() as shared_memory:
            mapped_flag_holder: List[bool] = shared_memory.value.take_message()
        
        # Example 1: await for single my_coro()
        await my_coro(asmm, 'single')

        # Example 2: await for 10 my_coro() tasks
        #   Step 1: make 10 instances of my_coro() tasks
        my_tasks: List[asyncio.Task] = [asyncio.create_task(my_coro(asmm, coro_id)) for coro_id in range(10)]
        #   Step 2: await for your 10 concurrent instances of my_coro()
        await asyncio.gather(*my_tasks)


if __name__ == '__main__':
    ensure_adjusted_pythonhashseed(pythonhashseed=0)  # Ensure that the hash seed is adjusted for this process group
    # ensure_adjusted_scientific()  # Ensure (for this process group) that: 1) the hash seed is adjusted; 2) interpreter optimizations ('-OO') are turned on; 3) the integer string conversion length limitation is turned off
    print('Receiver is starting its work.')
    asyncio.run(receiver())
    print('Receiver has finished its work.')
