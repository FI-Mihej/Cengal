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


from cengal.performance_test_lib import PrecisePerformanceTestTracer
from cengal.introspection.inspect import func_name
from threading import Lock, RLock
from pprint import pprint
from random import random
from typing import Callable


def func_perf_test(func: Callable, *args, **kwargs):
    tr = PrecisePerformanceTestTracer(1.0)
    while tr.iter():
        func(*args, **kwargs)

    with tr as fast_iter:
        for i in fast_iter:
            func(*args, **kwargs)

    print('{}(): {} iter/s; {} seconds; {} iterations'.format(func_name(func), tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))


from cengal.hardware.memory.shared_memory import *
from cengal.time_management.cpu_clock import cpu_clock
from cengal.time_management.high_precision_sync_sleep import hps_sleep
from multiprocessing import Process

creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

with_consumer = False
with_consumer = True

messages_num = 1000
communication_list_add_num = 20
clan_multiplier = 100000

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
verbose = False
# verbose = True


def creator_1():
    start_time = cpu_clock()
    for i in range(messages_num):
        with wait_my_turn(creator, periodic_sleep_time=None):
            creator.put_message(None)
    
    dtime = cpu_clock() - start_time
    print('<< Creator >>: {} messages put in {} seconds. MPS: {}'.format(messages_num, dtime, messages_num / dtime))

def creator_2():
    if with_consumer: creator.wait_consumer_ready()
    print('Consumer is ready')
    start_time = cpu_clock()
    wait_time = 0.0
    for msg_index, msg in enumerate(messages_to_put):
        wait_time_start = cpu_clock()
        with wait_my_turn(creator, periodic_sleep_time=None):
            wait_time += cpu_clock() - wait_time_start
            for i in range(multiplier):
                if verbose: print(f'<< Creator >>. Put message {msg_index}: {msg}')
                creator.put_message(msg)
    
    wait_time_start = cpu_clock()
    with wait_my_turn(creator, periodic_sleep_time=None):
        wait_time += cpu_clock() - wait_time_start
        creator.put_message(None)

    dtime = cpu_clock() - start_time - wait_time
    print('<< Creator >>: {} messages put in {} seconds. MPS: {}. Wait time: {}'.format(messages_num * multiplier + 1, dtime, (messages_num * multiplier + 1) / dtime, wait_time))

    '''
    Wait time - is a time your application would spend to other operations in an async environment.
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
        if verbose: print(f'<< Creator >>. Children offsets - 0 - 0: {communication_list.get_children_offsets()}')
        if verbose: print(f'<< Creator >>. Children offsets - 0 - 0: {communication_list.raw_to_bytes(200)}')
        if verbose: print(f'<< Creator >>. Children offsets - 0 - 1: {communication_list}')
    
    # waiting for the list to be changed by the consumer
    print('<< Creator >>: waiting for the list to be changed by the consumer')
    communication_list_size = len(communication_list)
    while communication_list_size <= initial_data_size:
        with wait_my_turn(creator, periodic_sleep_time=None):
            communication_list_size = len(communication_list)
    
    # changing list
    print('<< Creator >>: changing list')
    with wait_my_turn(creator, periodic_sleep_time=None):
        if verbose: print(f'<< Creator >>. Children offsets - 1: {communication_list.get_children_offsets()}. {communication_list}')
        # print(f'>\t> Free memory search start - before insert 0: {creator.get_free_memory_search_start()}:{creator.read_free_memory_search_start()}')
        # creator.print_mem(communication_list._pointer_to_internal_list, 100, f'>\t> before insert: {0}; {{}}')
        # creator.print_mem(communication_list._pointer_to_internal_list, 1000, f'>\t> before insert: {0}; {{}}')
        # communication_list.print_internal_list('after insert {}', 100)
        communication_list.insert(-1, 128)
        # communication_list.print_internal_list('after insert {}', 100)
        # print(f'>\t> Free memory search start - after insert 0: {creator.get_free_memory_search_start()}:{creator.read_free_memory_search_start()}')
        # creator.print_mem(communication_list._pointer_to_internal_list, 100, f'>\t> after insert: {0}; {{}}')
        # creator.print_mem(communication_list._pointer_to_internal_list, 1000, f'>\t> after insert: {0}; {{}}')
        if verbose: print(f'<< Creator >>. Children offsets - 2: {communication_list.get_children_offsets()}. {communication_list}')
        communication_list_size = len(communication_list)
        del communication_list[0: communication_list_size - 2]
        if verbose: print(f'<< Creator >>. Children offsets - 3: {communication_list.get_children_offsets()}. {communication_list}')
    
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

            if verbose: print(f'<< Creator >>. Children offsets - ADD START: {communication_list.get_children_offsets()}. {communication_list}')
            edit_time_start = cpu_clock()
            # working_list[1] += 1
            # working_list[1] += 1
            # working_list[1] += 1
            # working_list[1] += 1
            # working_list[1] += 1
            # working_list[1] += 1
            # working_list[1] += 1
            # working_list[1] += 1
            # working_list[1] += 1
            # working_list[1] += 1
            for _ in range(clan_multiplier):
                # working_list[1] += 1
                working_list[1] = 1
                # working_list[1]
            
            edit_time += cpu_clock() - edit_time_start
            if verbose: print(f'<< Creator >>. Children offsets - ADD FINISH: {communication_list.get_children_offsets()}. {communication_list}')
        
        communication_list_add_num_index += 1
    
    dtime = cpu_clock() - start_time - wait_time
    operations_made = communication_list_add_num * clan_multiplier
    alloc_dtime = creator._malloc_time - malloc_time + (creator._realloc_time - realloc_time)
    print(f'<< Creator >>: {alloc_dtime=}')
    print(f'<< Creator >>: {cpu_clock()}. Finished adding elements to the list')
    print('<< Creator >>: {} additions made in {} seconds. APS: {}. Wait time: {}'.format(operations_made, dtime, operations_made / dtime, wait_time))
    print(f'<< Creator >>: {operations_made} additions made in {edit_time} seconds. APS: {operations_made / edit_time}')

    '''
    Wait time - is a time your application would spend to other operations in an async environment.
    '''


def consumer_2():
    consumer: SharedMemory = SharedMemory('test_shmem', False, 100 * 1024 * 1024)
    with consumer:
        consumer.init_consumer()
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
                    # print('Got message: {}'.format(new_message))
                    if verbose: print(f'<< Consumer >>. Got message {taken_messages}: {new_message}')
                    if new_message is None:
                        need_to_stop = True
                        break
                    
                    messages.append(new_message)
                    taken_messages += 1
        
        dtime = cpu_clock() - start_time - wait_time
        print('<< Consumer >>: {} messages taken in {} seconds. MPS: {}. Wait time: {}'.format(taken_messages, dtime, taken_messages / dtime, wait_time))

        '''
        Wait time - is a time your application would spend to other operations in an async environment.
        '''

        # from pprint import pprint
        # pprint(messages)

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
            if verbose: print(f'<< Consumer >>. Children offsets - 0: {communication_list.get_children_offsets()}. {communication_list}')
            # print(f'>\t> Free memory search start: {consumer.get_free_memory_search_start()}:{consumer.read_free_memory_search_start()}')
            # consumer.print_mem(communication_list._offset, 100, f'>\t> before extend by: {[1, 2, (3, 4), [5, 0]]}; {{}}')
            # consumer.print_mem(communication_list._offset, 500, f'>\t> before extend by: {[1, 2, (3, 4), [5, 0]]}; {{}}')
            communication_list.extend([1, 2, (3, 4), [5, 0]])
            if verbose: print(f'<< Consumer >>. Children offsets - 1: {communication_list.get_children_offsets()}. {communication_list}')
        
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

                if verbose: print(f'<< Consumer >>. Children offsets - ADD START: {communication_list.get_children_offsets()}. {communication_list}')
                edit_time_start = cpu_clock()
                # working_list[1] += 1
                # working_list[1] += 1
                # working_list[1] += 1
                # working_list[1] += 1
                # working_list[1] += 1
                # working_list[1] += 1
                # working_list[1] += 1
                # working_list[1] += 1
                # working_list[1] += 1
                # working_list[1] += 1
                for _ in range(clan_multiplier):
                    # working_list[1] += 1
                    # working_list[1] = 1
                    working_list[1]
                
                edit_time += cpu_clock() - edit_time_start
                if verbose: print(f'<< Consumer >>. Children offsets - ADD FINISH: {communication_list.get_children_offsets()}. {communication_list}')
            
            communication_list_add_num_index += 1
        
        dtime = cpu_clock() - start_time - wait_time
        operations_made = communication_list_add_num * clan_multiplier
        alloc_dtime = consumer._malloc_time - malloc_time + (consumer._realloc_time - realloc_time)
        print(f'<< Consumer >>: {alloc_dtime=}')
        print(f'<< Consumer >>: {cpu_clock()}. Finished adding elements to the list')
        print('<< Consumer >>: {} additions made in {} seconds. APS: {}. Wait time: {}'.format(operations_made, dtime, operations_made / dtime, wait_time))
        print(f'<< Consumer >>: {operations_made} additions made in {edit_time} seconds. APS: {operations_made / edit_time}')

        '''
        Wait time - is a time your application would spend to other operations in an async environment.
        '''


if '__main__' == __name__:
    ensure_adjusted_pythonhashseed()  # Ensure that the hash seed is adjusted for this process group
    # ensure_adjusted_scientific()  # Ensure (for this process group) that: 1) the hash seed is adjusted; 2) interpreter optimizations ('-OO') are turned on; 3) the integer string conversion length limitation is turned off
    try:
        # def write_message():
        #     creator.wait_my_turn()
        #     creator.put_message(None)
        #     creator.release()


        # def read_message():
        #     consumer.wait_my_turn()
        #     consumer.read_message_info()
        #     consumer.release()


        # def full_cycle():
        #     write_message()
        #     read_message()


        # func_perf_test(full_cycle)

        p = Process(target=consumer_2)
        
        if with_consumer: p.start()
        creator_2()
        if with_consumer: p.join()
    finally:
        if with_consumer: p.kill()
        creator.close()
