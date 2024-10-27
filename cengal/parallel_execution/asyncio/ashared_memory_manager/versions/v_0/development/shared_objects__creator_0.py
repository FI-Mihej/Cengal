from cengal.hardware.memory.shared_memory import *
from cengal.parallel_execution.asyncio.ashared_memory_manager import *

import asyncio


async def sender():
    # Create named shared memory instance as a creator
    async with ASharedMemoryManager(SharedMemory('shared_objects', create=True, size=200 * 1024**2)) as asmm:
        print('Creator is ready.')

        ashared_memory_context_manager: ASharedMemoryContextManager = asmm()

        # Send 12 messages
        async with ashared_memory_context_manager as shared_memory:
            for i in range(12):
                mapped_flag_holder = shared_memory.value.put_message([False])


if __name__ == '__main__':
    ensure_adjusted_pythonhashseed(pythonhashseed=0)  # Ensure that the hash seed is adjusted for this process group
    # ensure_adjusted_scientific()  # Ensure (for this process group) that: 1) the hash seed is adjusted; 2) interpreter optimizations ('-OO') are turned on; 3) the integer string conversion length limitation is turned off
    print('Sender is starting its work.')
    asyncio.run(sender())
    print('Sender has finished its work.')
