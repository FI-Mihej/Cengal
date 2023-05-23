#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.2.2"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from multiprocessing import Process

from cengal.hardware.memory.shared_memory import *
from cengal.time_management.cpu_clock import cpu_clock


shared_memory_name: str = 'test_shmem'
shared_memory_size: int = 200 * 1024 * 1024  # 200 MB

# `multiprocessing.SharedMemory` requires this cleanup in order to handle the case 
# when the previous run of the program was terminated unexpectedly:
try:
    import _posixshmem
    from multiprocessing.resource_tracker import unregister
    shm_name = f'/{shared_memory_name}'
    _posixshmem.shm_unlink(shm_name)
    unregister(shm_name, "shared_memory")
except FileNotFoundError:
    pass

creator: SharedMemory = SharedMemory(shared_memory_name, True, 200 * 1024 * 1024)

messages_num = 1000
communication_list_add_num = 200
clan_multiplier = 10000

messages_to_put = [
    1,
    2,
    (1, 2),
    [1, 2],
    (1, [2, 3]),
    {1: 1, 2: 2},
    {1: 1, 2: [2, (3,)]},
] * 10
messages_num = len(messages_to_put)
multiplier = 100


def creator_process():
    creator.wait_consumer_ready()
    print('Consumer is ready')
    start_time = cpu_clock()
    wait_time = 0.0
    for msg_index, msg in enumerate(messages_to_put):
        wait_time_start = cpu_clock()
        with wait_my_turn(creator, periodic_sleep_time=None):
            wait_time += cpu_clock() - wait_time_start
            for i in range(multiplier):
                creator.put_message(msg)
    
    wait_time_start = cpu_clock()
    with wait_my_turn(creator, periodic_sleep_time=None):
        wait_time += cpu_clock() - wait_time_start
        creator.put_message(None)

    dtime = cpu_clock() - start_time - wait_time
    print('<< Creator >>: {} messages put in {} seconds. MPS: {}. Wait time: {}'.format(messages_num * multiplier + 1, dtime, (messages_num * multiplier + 1) / dtime, wait_time))
    '''
    Wait time - is a another process working time + switching time + get into line time.
    '''

    # puting an IList
    print('<< Creator >>: puting an IList')
    with wait_my_turn(creator, periodic_sleep_time=None):
        initial_data = [
            9,
            (8,),
            {
                7: 6,
                5: 4
            }
        ]
        initial_data_size = len(initial_data)
        communication_list: IList = creator.put_message(initial_data)
    
    print('<< Creator >>: waiting for the list to be changed by the consumer')
    communication_list_size = len(communication_list)
    while communication_list_size <= initial_data_size:
        with wait_my_turn(creator, periodic_sleep_time=None):
            communication_list_size = len(communication_list)
    
    # changing list
    print('<< Creator >>: changing list')
    with wait_my_turn(creator, periodic_sleep_time=None):
        communication_list.insert(-1, 128)
        communication_list_size = len(communication_list)
        del communication_list[0: communication_list_size - 2]
    
    # saving working list into a variable
    print('<< Creator >>: saving working list into a variable')
    with wait_my_turn(creator, periodic_sleep_time=None):
        working_list = communication_list[1]
    
    # concurently adding elements to the list
    print('<< Creator >>: concurently adding elements to the list')
    print(f'<< Creator >>: {cpu_clock()}. Starting adding elements to the list')
    malloc_time: float = creator._malloc_time
    realloc_time: float = creator._realloc_time
    start_time = None
    edit_time = 0.0
    wait_time = 0.0
    communication_list_add_num_index = 0
    while communication_list_add_num_index < communication_list_add_num:
        wait_time_start = cpu_clock()
        with wait_my_turn(creator, periodic_sleep_time=None):
            wait_time += cpu_clock() - wait_time_start
            if start_time is None:
                wait_time = 0.0
                start_time = cpu_clock()

            edit_time_start = cpu_clock()
            for _ in range(clan_multiplier):
                working_list[1] += 1
            
            edit_time += cpu_clock() - edit_time_start
        
        communication_list_add_num_index += 1
    
    dtime = cpu_clock() - start_time - wait_time
    operations_made = communication_list_add_num * clan_multiplier
    alloc_dtime = creator._malloc_time - malloc_time + (creator._realloc_time - realloc_time)
    print(f'<< Creator >>: {alloc_dtime=}')
    print(f'<< Creator >>: {cpu_clock()}. Finished adding elements to the list')
    print('<< Creator >>: {} additions made in {} seconds. Operations/second: {}. Wait time: {}'.format(operations_made, dtime, operations_made / dtime, wait_time))
    print(f'<< Creator >>. Operations dedicated performance: {operations_made} additions made in {edit_time} seconds. Operations/second: {operations_made / edit_time}')
    '''
    Wait time - is a another process working time + switching time + get into line time.
    '''


def consumer_process():
    consumer: SharedMemory = SharedMemory(shared_memory_name, False, 100 * 1024 * 1024)
    taken_messages = 0
    messages: list = list()
    need_to_stop = False
    start_time = None
    wait_time = 0.0
    while not need_to_stop:
        wait_time_start = cpu_clock()
        with wait_my_turn(consumer, periodic_sleep_time=None):
            wait_time += cpu_clock() - wait_time_start
            while consumer.has_messages():
                if start_time is None:
                    wait_time = 0.0
                    start_time = cpu_clock()
                
                new_message = consumer.take_message()
                if new_message is None:
                    need_to_stop = True
                    break
                
                messages.append(new_message)
                taken_messages += 1
    
    dtime = cpu_clock() - start_time - wait_time
    print('<< Consumer >>: {} messages taken in {} seconds. MPS: {}. Wait time: {}'.format(taken_messages, dtime, taken_messages / dtime, wait_time))
    '''
    Wait time - is a another process working time + switching time + get into line time.
    '''

    # waiting for an IList
    print('<< Consumer >>: waiting for an IList')
    communication_list: IList = None
    list_found = False
    while not list_found:
        consumer.wait_for_messages()
        with wait_my_turn(consumer, periodic_sleep_time=None):
            while consumer.has_messages():
                new_message = consumer.take_message()
                if isinstance(new_message, IList):
                    communication_list = new_message
                    list_found = True
    
    # adding elements to the list
    print('<< Consumer >>: adding elements to the list')
    with wait_my_turn(consumer, periodic_sleep_time=None):
        communication_list.extend([1, 2, (3, 4), [5, 0]])
    
    # waiting for the list to be changed by the creator
    print('<< Consumer >>: waiting for the list to be changed by the creator')
    communication_list_size = len(communication_list)
    while communication_list_size > 2:
        with wait_my_turn(consumer, periodic_sleep_time=None):
            communication_list_size = len(communication_list)
    
    # saving working list into a variable
    print('<< Consumer >>: saving working list into a variable')
    with wait_my_turn(consumer, periodic_sleep_time=None):
        working_list = communication_list[1]
    
    # concurently adding elements to the list
    print('<< Consumer >>: concurently adding elements to the list')
    print(f'<< Consumer >>: {cpu_clock()}. Starting adding elements to the list')
    malloc_time: float = consumer._malloc_time
    realloc_time: float = consumer._realloc_time
    start_time = None
    edit_time = 0.0
    wait_time = 0.0
    communication_list_add_num_index = 0
    while communication_list_add_num_index < communication_list_add_num:
        wait_time_start = cpu_clock()
        with wait_my_turn(consumer, periodic_sleep_time=None):
            wait_time += cpu_clock() - wait_time_start
            if start_time is None:
                wait_time = 0.0
                start_time = cpu_clock()

            edit_time_start = cpu_clock()
            for _ in range(clan_multiplier):
                working_list[1] += 1
            
            edit_time += cpu_clock() - edit_time_start
        
        communication_list_add_num_index += 1
    
    dtime = cpu_clock() - start_time - wait_time
    operations_made = communication_list_add_num * clan_multiplier
    alloc_dtime = consumer._malloc_time - malloc_time + (consumer._realloc_time - realloc_time)
    print(f'<< Consumer >>: {alloc_dtime=}')
    print(f'<< Consumer >>: {cpu_clock()}. Finished adding elements to the list')
    print('<< Consumer >>: {} additions made in {} seconds. Operations/second: {}. Wait time: {}'.format(operations_made, dtime, operations_made / dtime, wait_time))
    print(f'<< Consumer >>. Operations dedicated performance: {operations_made} additions made in {edit_time} seconds. Operations/second: {operations_made / edit_time}')
    '''
    Wait time - is a another process working time + switching time + get into line time.
    '''

    consumer._shared_memory.close()


if '__main__' == __name__:
    try:
        p = Process(target=consumer_process)
        p.start()
        creator_process()
        p.join()
    finally:
        p.kill()
        creator._shared_memory.close()
        creator._shared_memory.unlink()
