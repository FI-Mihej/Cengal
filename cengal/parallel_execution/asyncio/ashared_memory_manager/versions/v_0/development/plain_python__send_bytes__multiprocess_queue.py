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


import multiprocessing
from cengal.performance_test_lib import MeasureTimeTraceLine


def sender(queue):
    data = bytes([255] * 300000)  # Generate a data block of 300000 bytes
    with MeasureTimeTraceLine('sender', iterations=1000) as mt:
        for i in range(mt.iterations):
            queue.put(data, block=True)  # Send data to the queue
            # print(f"Data sent iteration {i + 1}")
        queue.put(None)  # Signal that no more data will be sent
            
    print(f'Throughput: {(300000 * mt.iterations) / mt.time_spent:.2f} bytes per second')
    print()

def receiver(queue):
    with MeasureTimeTraceLine('receiver', iterations=1000) as mt:
        while True:
            data = queue.get()  # Receive data from the queue
            if data is None:
                # print("No more data to receive. Exiting.")
                break

            # print("Received data")
            
    print(f'Throughput: {(300000 * mt.iterations) / mt.time_spent:.2f} bytes per second')
    print()

def main():
    queue = multiprocessing.Queue(maxsize=10)

    # Start sender process
    sender_process = multiprocessing.Process(target=sender, args=(queue,))
    sender_process.start()

    # Start receiver process
    receiver_process = multiprocessing.Process(target=receiver, args=(queue,))
    receiver_process.start()

    # Wait for both processes to complete
    sender_process.join()
    receiver_process.join()

if __name__ == "__main__":
    main()
