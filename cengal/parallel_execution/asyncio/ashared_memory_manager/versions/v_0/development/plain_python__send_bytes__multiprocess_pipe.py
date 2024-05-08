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


import asyncio
import multiprocessing
from os import getpid
from cengal.performance_test_lib import MeasureTimeTraceLine


async def send_data(conn):
    print(f"Sender PID: {getpid()}")
    data = bytes([255] * 300000)
    with MeasureTimeTraceLine('send_data', iterations=1000) as mt:
        for i in range(mt.iterations):
            conn.send(data)
            # print(f"Data sent iteration {i+1}")
            
    print(f'Throughput: {(300000 * mt.iterations) / mt.time_spent:.2f} bytes per second')
    print()
    
    conn.close()

async def receive_data(conn):
    loop = asyncio.get_running_loop()
    print(f"Receiver PID: {getpid()}")
    with MeasureTimeTraceLine('receive_data', iterations=1000) as mt:
        for i in range(mt.iterations):
            data = await loop.run_in_executor(None, conn.recv)
            # print("Received data")
            
    print(f'Throughput: {(300000 * mt.iterations) / mt.time_spent:.2f} bytes per second')
    print()

def main():
    parent_conn, child_conn = multiprocessing.Pipe()

    # Start sender process
    sender_process = multiprocessing.Process(target=asyncio.run, args=(send_data(child_conn),))
    sender_process.start()

    # Start receiver process
    receiver_process = multiprocessing.Process(target=asyncio.run, args=(receive_data(parent_conn),))
    receiver_process.start()

    # Wait for both processes to complete
    sender_process.join()
    receiver_process.join()

if __name__ == "__main__":
    main()
