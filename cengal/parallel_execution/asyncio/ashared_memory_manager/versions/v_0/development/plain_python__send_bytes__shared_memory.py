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


import multiprocessing
from multiprocessing import shared_memory, Semaphore, Process
from cengal.performance_test_lib import MeasureTimeTraceLine


def receiver(shm_name, semaphore_sender, semaphore_receiver):
    shm = shared_memory.SharedMemory(name=shm_name)
    current_process = multiprocessing.current_process()
    print(f'Receiver: {current_process.name=}')

    try:
        semaphore_sender.acquire()  # Wait for the sender to send data
        data = bytes(shm.buf[:300000])
        semaphore_receiver.release()  # Notify sender that data has been processed
        with MeasureTimeTraceLine('Receiver', iterations=1000) as mt:
            for _ in range(mt.iterations):
                semaphore_sender.acquire()  # Wait for the sender to send data
                data = bytes(shm.buf[:300000])
                semaphore_receiver.release()  # Notify sender that data has been processed
            
            print('Receiving - Done.')
            
        print(f'Throughput: {(300000 * mt.iterations) / mt.time_spent:.2f} bytes per second')
        print()

    finally:
        # Clean up
        shm.close()

def sender(shm_name, semaphore_sender, semaphore_receiver):
    shm = shared_memory.SharedMemory(name=shm_name)
    current_process = multiprocessing.current_process()
    print(f'Sender: {current_process.name=}')

    try:
        data = bytes([255] * 300000)  # Example data block of 300000 bytes
        shm.buf[:300000] = data
        semaphore_sender.release()  # Signal the receiver that the data is ready
        semaphore_receiver.acquire()  # Wait for receiver to process data
        with MeasureTimeTraceLine('Sender', iterations=1000) as mt:
            for _ in range(mt.iterations):
                shm.buf[:300000] = data
                semaphore_sender.release()  # Signal the receiver that the data is ready
                semaphore_receiver.acquire()  # Wait for receiver to process data
        
        print('Sending - Done.')
            
        print(f'Throughput: {(300000 * mt.iterations) / mt.time_spent:.2f} bytes per second')
        print()

    finally:
        # Clean up
        shm.close()

def main():
    # Create shared memory
    shm = shared_memory.SharedMemory(create=True, size=300000)
    semaphore_sender = Semaphore(0)
    semaphore_receiver = Semaphore(0)

    # Create and start processes
    process_receiver = Process(target=receiver, args=(shm.name, semaphore_sender, semaphore_receiver))
    process_sender = Process(target=sender, args=(shm.name, semaphore_sender, semaphore_receiver))

    process_receiver.start()
    process_sender.start()

    # Wait for processes to complete
    process_sender.join()
    process_receiver.join()

    # Cleanup shared memory
    shm.close()
    shm.unlink()

if __name__ == '__main__':
    main()
