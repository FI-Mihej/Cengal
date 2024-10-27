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


__all__ = []


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


from cengal.performance_test_lib import LineType, MeasureTime, measure_time_tl
from cengal.introspection.inspect import pcen, cen, pifr, pifrl, intro_func_repr_limited
from cengal.hardware.memory.barriers import full_memory_barrier
from cengal.code_inspection.auto_line_tracer import tl, tr, t, alt, LineType, OutputFields, AutoLineTracer
from cengal.user_interface.console.terminal import sprint, st, fill_current_line, cursor_forward, cursor_up, terminal_width, terminal, \
    set_background_color, BackgroundColor, set_foreground_color, ForegroundColor, erase_screen, erase_line, set_cursor_pos
from cengal.hardware.memory.shared_memory import *
from cengal.parallel_execution.asyncio.ashared_memory_manager import *

from multiprocessing import Process, Manager
from os.path import basename
from dataclasses import dataclass
from enum import IntEnum

from uuid import uuid4
import numpy as np
from typing import Union, List, Callable


async def consumer(shared_memory_name: str):
    pifrl()

    sm = SharedMemorySMP(shared_memory_name)
    async with ASharedMemoryManager(sm) as asmm:
        ashared_memory_context_manager: ASharedMemoryContextManager = asmm()

        max_consumers_num: int = sm.max_consumers_num
        my_id: int = sm.consumer_id
        async with ashared_memory_context_manager.if_has_messages():
            mapped_data: Data = sm.read_message()
            lock: RWLock = mapped_data.lock
            print_lock: RWLock = mapped_data.print_lock
            a = mapped_data.a
            b = mapped_data.b
            c = mapped_data.c
       
        async with lock.write():
            mapped_data.got_data_num += 1

        async with print_lock.write(periodic_sleep_time=1/60):
            # with measure_time_tl():
            sprint(st('Consumer ', st(my_id).f_green, ' started...').f_yellow)
        
        with sm.get_in_line_on_write(periodic_sleep_time=None):
            processing_start_requested: bool = False
            while not processing_start_requested:
                async with lock.read():
                    processing_start_requested = mapped_data.processing_start_requested
                    full_memory_barrier()

            if mapped_data.array_type in {ArrayType.ndarray, ArrayType.matrix, ArrayType.py_list}:
                c_rows, c_cols = c.shape
                a_rows, a_cols = a.shape
                b_rows, b_cols = b.shape

            for m in range(my_id, c_rows, max_consumers_num):
                for k in range(a_cols):
                    for n in range(c_cols):
                        c[m, n] += a[m, k] * b[k, n]
            
            async with lock.write():
                mapped_data.processed_data_num += 1
        
        async with print_lock.write(periodic_sleep_time=1/60):
            sprint(st('Consumer ', st(my_id).f_green, ' done.').f_white)


def consumer_main(*args, **kwargs):
    return asyncio.run(consumer(*args, **kwargs))


async def creator(shared_memory_name: str, shared_memory_size: Optional[int], max_consumers_num: int):
    print(f'{cen()}()')

    sm = SharedMemorySMP(shared_memory_name, True, shared_memory_size, max_consumers_num=max_consumers_num)
    async with ASharedMemoryManager(sm) as asmm:
        ashared_memory_context_manager: ASharedMemoryContextManager = asmm()

        async with ashared_memory_context_manager:
            mapped_data: Data = None
            message_offset: Offset = None
            mapped_data, message_offset = sm.put_message_2(data)
            lock: RWLock = mapped_data.lock
            print_lock: RWLock = mapped_data.print_lock

        async with print_lock.write(periodic_sleep_time=1/60):
            sprint(st('Creator started...').f_green)

        # async with print_lock.write(periodic_sleep_time=1/60):
        #     sprint(st(intro_func_repr_limited()).f_cyan)  # Will print the current function name and the arguments with values
        
        mflops = None
        with sm.get_in_line_on_write():
            result = True
            while result:
                async with lock.read():
                    result = sm.max_consumers_num > mapped_data.got_data_num

            with MeasureTime('Multiprocessing - creator', do_print=False) as mt:
                async with lock.write(periodic_sleep_time=None):
                    mapped_data.processing_start_requested = True

                result = True
                while result:
                    async with lock.read():
                        sleep(0.01)
                        result = sm.max_consumers_num > mapped_data.processed_data_num

            secs = mt.time_spent
            mflops = ((2*m*n*k)/secs) / 1e6

            async with print_lock.write(periodic_sleep_time=1/60):
                fill_current_line(st(' ').b_cyan.bs_dim)
                print()
                fill_current_line(st(' ').b_cyan.bs_dim)
                cursor_forward(3)
                sprint(st(
                    st(' time spent').f_green.sdim, ': ', st(secs).f_yellow.sdim, ' '
                ).b_blue.f_white)
                fill_current_line(st(' ').b_cyan.bs_dim)
                cursor_forward(3)
                sprint(st(
                    ' ', st(mflops).f_yellow.sdim, st(' MFLOP/s ').f_green.sdim
                ).b_blue.f_white)
                fill_current_line(st(' ').b_cyan.bs_dim)
                print()
        
                fill_current_line(st(' ').b_blue)
                sprint(st(' Creator done. ').b_blue.f_green)
                fill_current_line(st('=').b_blue.f_white)
                print()
                fill_current_line(st(' ').b_cyan.bs_dim)
                print()

                return mflops


def creator_main(*args, **kwargs):
    return asyncio.run(creator(*args, **kwargs))


def start():
    recommended_max_consumers_num = SharedMemorySMP.recommended_max_consumers_num()
    # max_consumers_num = 10
    # max_consumers_num = 1
    max_consumers_num = recommended_max_consumers_num

    operators: List[Process] = list()
    operators.append(Process(target=creator_main, args=(shared_memory_name, max_consumers_num, prepare_data(m, n, k), m, n, k)))
    for _ in range(max_consumers_num):
        operators.append(Process(target=consumer_main, args=(shared_memory_name, )))
    
    for another_operators in operators:
        another_operators.start()

    for another_operators in operators:
        another_operators.join()


class AProcessPool:
    def __init__(self, process_num: Optional[int] = None, shared_memory_size: Optional[int] = None, default_worker: Optional[Callable] = None):
        self._max_consumers_num = SharedMemorySMP.recommended_max_consumers_num() if process_num is None else process_num
        self._default_worker: Optional[Callable] = default_worker
        self._known_workers: Dict[Callable, int] = dict()  # worker: worker_index
        self._shared_memory_name: str = str(uuid4())
        self._operators: List[Process] = list()
    
    async def __aenter__(self):
        for _ in range(self._max_consumers_num):
            self._operators.append(Process(target=consumer_main, args=(self._shared_memory_name, )))
        
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        ...

    def __enter__(self):
        self._operators.append(Process(target=creator_main, args=(self._shared_memory_name, self._max_consumers_num)))
        for _ in range(self._max_consumers_num):
            self._operators.append(Process(target=consumer_main, args=(self._shared_memory_name, )))
        
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        ...


from cengal.introspection.inspect import is_async
from cengal.hardware.memory.barriers import full_memory_barrier, mm_pause
from cengal.time_management.high_precision_sync_sleep import hps_sleep
from cengal.data_containers.intenum_struct import *

from pickle import dumps as pickle_dumps, loads as pickle_loads
from enum import IntEnum
from typing import Generator


class SmpMapChainRequestFields(IntEnum):
    in_sequence = 0
    out_sequence = 1
    saved_out_sequence_indexes = 2
    removed_sequence_indexes = 3
    func_list = 4
    curent_func_index = 5
    start = 6
    started_consumers_num = 7
    finished_consumers_num = 8
    cleanup_started_consumers_num = 9
    cleanuped_consumers_num = 10
    shut_down = 11
    rwlock = 12
    periodic_sleep_time = 13


smp_map_chain_request = IntEnumStruct(SmpMapChainRequestFields)


WorkerFunction = Callable[[Any,], Tuple[bool, Any]]


IndexChoosingFunction = Callable[[int, int, int], Generator]
IndexChoosingGeneratorResult = int
IndexChoosingGeneratorResultInOut = Tuple[int, int]
IndexChoosingGeneratorResultInOutLists = Tuple[List[int], List[int]]


NoneType = type(None)


class SaveAll:
    __slots__ = ('func', )

    def __init__(self, func: Callable) -> None:
        self.func: Callable = func
    
    def __call__(self, *args, **kwargs):
        return True, self.func(*args, **kwargs)


class ASaveAll:
    __slots__ = ('func', )

    def __init__(self, async_func: Callable) -> None:
        self.func: Callable = async_func
    
    async def __call__(self, *args, **kwargs):
        return True, await self.func(*args, **kwargs)


def alternate_selection(items_num: int, consumer_id: int, max_consumers_num: int) -> Generator:
    """Returns generator for selecting items for processing in an alternate way.
    For example, if there are 10 items and 3 consumers, then the first consumer will process items with indexes 0, 3, 6, 9, 
    the second consumer will process items with indexes 1, 4, 7, the third consumer will process items with indexes 2, 5, 8.
    This is a default way of selecting items for processing.

    Args:
        items_num (int): _description_
        consumer_id (int): _description_
        max_consumers_num (int): _description_

    Returns:
        _type_: _description_
    """    
    return range(consumer_id, items_num, max_consumers_num)


def selection_in_blocks(items_num: int, consumer_id: int, max_consumers_num: int) -> Generator:
    """Returns generator for selecting items for processing in blocks.
    For example, if there are 10 items and 3 consumers, then the first consumer will process items with indexes 0, 1, 2,
    the second consumer will process items with indexes 3, 4, 5, the third consumer will process items with indexes 6, 7, 8, 9.
    (The last consumer will process the rest of the items as well, if the number of items is not divisible by the number of consumers)

    Args:
        items_num (int): _description_
        consumer_id (int): _description_
        max_consumers_num (int): _description_

    Returns:
        _type_: _description_
    """    
    block_size = int(round(items_num / max_consumers_num))
    if consumer_id == max_consumers_num - 1:
        return range(consumer_id * block_size, items_num)
    else:
        return range(consumer_id * block_size, (consumer_id + 1) * block_size)


class SmpWorker:
    multi_item_processing: bool = False
    multi_item_inplace_processing: bool = False
    multi_item_processing_protection_required: bool = True

    def __init__(self) -> None:
        self.items_num: int = None
        self.consumer_id: int = None
        self.max_consumers_num: int = None
    
    def init(self, items_num: int, consumer_id: int, max_consumers_num: int) -> None:
        self.items_num: int = items_num
        self.consumer_id: int = consumer_id
        self.max_consumers_num: int = max_consumers_num
    
    def __call__(self, *args, **kwargs) -> Any:
        pass

    def index_choosing_function(self):
        return alternate_selection(self.items_num, self.consumer_id, self.max_consumers_num)


class ASmpWorker(SmpWorker):
    def __init__(self) -> None:
        super().__init__()
    
    async def __call__(self, *args, **kwargs) -> Any:
        pass


class SmpRawWorker:
    def __init__(self) -> None:
        self.sm: SharedMemorySMP = None
        self.asmm: ASharedMemoryManager = None
        self.asmcm: ASharedMemoryContextManager = None
        self.request: List = None
    
    def init(self, sm: SharedMemorySMP, asmm: ASharedMemoryManager, asmcm: ASharedMemoryContextManager, request: List) -> None:
        self.sm = sm
        self.asmm = asmm
        self.asmcm = asmcm
        self.request = request
    
    def __call__(self, *args, **kwargs) -> Any:
        pass


class ASmpRawWorker(SmpRawWorker):
    def __init__(self) -> None:
        super().__init__()
    
    async def __call__(self, *args, **kwargs) -> Any:
        pass


async def consumer(shared_memory_name: str, try_to_use_uvloop: bool):
    pifrl()

    sm = SharedMemorySMP(shared_memory_name)
    async with ASharedMemoryManager(sm) as asmm:
        ashared_memory_context_manager: ASharedMemoryContextManager = asmm()

        max_consumers_num: int = sm.max_consumers_num
        max_additional_consumers_num: int = max_consumers_num - 1
        my_id: int = sm.consumer_id
        async with ashared_memory_context_manager.if_has_messages():
            request: List = sm.read_message()
            in_sequence: IList = request[SmpMapChainRequestFields.in_sequence]
            out_sequence: IList = request[SmpMapChainRequestFields.out_sequence]
            saved_out_sequence_indexes: List = request[SmpMapChainRequestFields.saved_out_sequence_indexes]
            removed_sequence_indexes: List = request[SmpMapChainRequestFields.removed_sequence_indexes]
            func_list: List = request[SmpMapChainRequestFields.func_list]
            curent_func_index = request[SmpMapChainRequestFields.curent_func_index]
            start = request[SmpMapChainRequestFields.start]
            started_consumers_num = request[SmpMapChainRequestFields.started_consumers_num]
            finished_consumers_num = request[SmpMapChainRequestFields.finished_consumers_num]
            cleanup_started_consumers_num = request[SmpMapChainRequestFields.cleanup_started_consumers_num]
            cleanuped_consumers_num = request[SmpMapChainRequestFields.cleanuped_consumers_num]
            shut_down = request[SmpMapChainRequestFields.shut_down]
            rwlock: RWLock = request[SmpMapChainRequestFields.rwlock]
            periodic_sleep_time: Optional[RationalNumber] = request[SmpMapChainRequestFields.periodic_sleep_time]

        while True:
            while True:
                async with rwlock.read():
                    if request[SmpMapChainRequestFields.start]:
                        break
                    
                if periodic_sleep_time is None:
                    mm_pause()
                else:
                    hps_sleep(periodic_sleep_time)
            
            async with rwlock.write():
                request[SmpMapChainRequestFields.started_consumers_num] += 1
            
            while True:
                async with rwlock.read():
                    if not request[SmpMapChainRequestFields.start]:
                        break
                    
                if periodic_sleep_time is None:
                    mm_pause()
                else:
                    hps_sleep(periodic_sleep_time)
            
            async with rwlock.read():
                if request[SmpMapChainRequestFields.shut_down]:
                    break
                
            async with rwlock.read():
                is_raw_processing: bool = False
                in_sequence_len: int = len(in_sequence)
                multi_item_processing: bool = False
                multi_item_inplace_processing: bool = False
                multi_item_processing_protection_required: bool = True
                curent_func_index = request[SmpMapChainRequestFields.curent_func_index]
                func = pickle_loads(func_list[curent_func_index])
                if isinstance(func, (tuple, list)):
                    func, index_choosing_function = func
                    index_gen = index_choosing_function(in_sequence_len, my_id, max_consumers_num)
                elif isinstance(func, SmpWorker):
                    func.init(in_sequence_len, my_id, max_consumers_num)
                    index_gen = func.index_choosing_function()
                    multi_item_processing = func.multi_item_processing
                    multi_item_inplace_processing = func.multi_item_inplace_processing
                    multi_item_processing_protection_required = func.multi_item_processing_protection_required
                elif isinstance(func, SmpRawWorker):
                    is_raw_processing = True
                    func.init(sm, asmm, ashared_memory_context_manager, request)
                else:
                    index_gen = alternate_selection(in_sequence_len, my_id, max_consumers_num)
                
                is_async_func: bool = is_async(func)

            if is_raw_processing:
                if is_async_func:
                    await func()
                else:
                    func()
            else: 
                with sm.get_in_line_on_write():
                    if multi_item_processing:
                        if multi_item_inplace_processing:
                            if multi_item_processing_protection_required:
                                async with rwlock.read():
                                    for indexes in index_gen:
                                        items: Dict[int, Any] = dict()
                                        for index in indexes:
                                            item = in_sequence[index]
                                            items[index] = pickle_loads(item) if isinstance(item, bytes) else item
                                        
                                        results: Dict[int, Any] = await func(items) if is_async_func else func(items)
                                        async with rwlock.write():
                                            for item_index, item in results:
                                                item = pickle_dumps(item) if not isinstance(item, (NoneType, bool, int, float)) else item
                                                in_sequence_len = len(in_sequence)
                                                if item_index < in_sequence_len:
                                                    in_sequence[item_index] = item
                                                elif item_index == in_sequence_len:
                                                    in_sequence.append(item)
                                                else:
                                                    in_sequence.extend([None] * (item_index - in_sequence_len + 1))
                                                    in_sequence[item_index] = item
                            else:
                                for indexes in index_gen:
                                    items: Dict[int, Any] = dict()
                                    for index in indexes:
                                        item = in_sequence[index]
                                        items[index] = pickle_loads(item) if isinstance(item, bytes) else item
                                    
                                    results: Dict[int, Any] = await func(items) if is_async_func else func(items)
                                    for item_index, item in results:
                                        item = pickle_dumps(item) if not isinstance(item, (NoneType, bool, int, float)) else item
                                        in_sequence[item_index] = item
                        else:
                            for indexes in index_gen:
                                items: Dict[int, Any] = dict()
                                for index in indexes:
                                    item = in_sequence[index]
                                    items[index] = pickle_loads(item) if isinstance(item, bytes) else item
                                
                                results: Dict[int, Any] = await func(items) if is_async_func else func(items)
                                
                                for item_index, item in results:
                                    saved_out_sequence_indexes[item_index] = True
                                    item = pickle_dumps(item) if not isinstance(item, (NoneType, bool, int, float)) else item
                                    if multi_item_processing_protection_required:
                                        async with rwlock.read():
                                            if item_index >= len(out_sequence):
                                                async with rwlock.write():
                                                    out_sequence_len = len(out_sequence)
                                                    if item_index < out_sequence_len:
                                                        out_sequence[item_index] = item
                                                    elif item_index == out_sequence_len:
                                                        out_sequence.append(item)
                                                    else:
                                                        out_sequence.extend([None] * (item_index - out_sequence_len + 1))
                                                        out_sequence[item_index] = item
                                            else:
                                                out_sequence[item_index] = item
                                    else:
                                        out_sequence[item_index] = item
                    else:
                        for index in index_gen:
                            item = in_sequence[index]
                            item = pickle_loads(item) if isinstance(item, bytes) else item
                            saved, result = await func(item) if is_async_func else func(item)
                            if saved:
                                # saved_out_sequence_indexes.append(index)
                                saved_out_sequence_indexes[index] = True
                                result = pickle_dumps(result) if not isinstance(result, (NoneType, bool, int, float)) else result
                                out_sequence[index] = result
                            # else:
                            #     removed_sequence_indexes.append(index)



                # ========================================
                async with rwlock.write():
                    request[SmpMapChainRequestFields.finished_consumers_num] += 1
                    
                while True:
                    async with rwlock.read():
                        if request[SmpMapChainRequestFields.start]:
                            break
                        
                    if periodic_sleep_time is None:
                        mm_pause()
                    else:
                        hps_sleep(periodic_sleep_time)
                
                async with rwlock.write():
                    request[SmpMapChainRequestFields.cleanup_started_consumers_num] += 1
                
                while True:
                    async with rwlock.read():
                        if not request[SmpMapChainRequestFields.start]:
                            break
                        
                    if periodic_sleep_time is None:
                        mm_pause()
                    else:
                        hps_sleep(periodic_sleep_time)
                
                if not is_raw_processing:
                    saved_items_num: int = len(saved_out_sequence_indexes)
                    in_sequence: IList = request[SmpMapChainRequestFields.in_sequence]
                    for index in alternate_selection(saved_items_num, my_id, max_consumers_num):
                        if saved_out_sequence_indexes[index]:
                            out_sequence.move_item_to_list(index, in_sequence, index)

                    request[SmpMapChainRequestFields.out_sequence] = [None] * saved_items_num
                    request[SmpMapChainRequestFields.saved_out_sequence_indexes] = list()

                async with rwlock.write():
                    request[SmpMapChainRequestFields.cleanuped_consumers_num] += 1
            



            # =================================
                if my_id:
                    async with rwlock.write():
                        request[SmpMapChainRequestFields.finished_consumers_num] += 1
                
            if 0 == my_id:
                while True:
                    async with rwlock.read():
                        if max_additional_consumers_num == request[SmpMapChainRequestFields.finished_consumers_num]:
                            break
                        
                    if periodic_sleep_time is None:
                        mm_pause()
                    else:
                        hps_sleep(periodic_sleep_time)
                
                with wait_my_turn(sm):
                    saved_items_num: int = len(saved_out_sequence_indexes)
                    request[SmpMapChainRequestFields.in_sequence] = [None] * saved_items_num
                    in_sequence: IList = request[SmpMapChainRequestFields.in_sequence]
                    for index, saved_index in enumerate(saved_out_sequence_indexes):
                        out_sequence.move_item_to_list(saved_index, in_sequence, index)

                    request[SmpMapChainRequestFields.out_sequence] = [None] * saved_items_num
                    request[SmpMapChainRequestFields.saved_out_sequence_indexes] = list()

                async with rwlock.write():
                    request[SmpMapChainRequestFields.finished_consumers_num] += 1


def consumer_main(shared_memory_name: str, try_to_use_uvloop: bool):
    if try_to_use_uvloop:
        from cengal.parallel_execution.coroutines.integrations.uvloop import uvloop_silent_install
        uvloop_silent_install()
    
    return asyncio.run(consumer(shared_memory_name, try_to_use_uvloop))


def smp_map_chain(func_or_chain: Union[Callable, Sequence[Callable]], 
              data: Sequence, process_num: Optional[int] = None, 
              shared_memory_size: Optional[int] = None, 
              default_worker: Optional[Callable] = None, 
              periodic_sleep_time: Optional[RationalNumber] = 0.000000001, 
              try_to_use_uvloop: bool = True, 
              ):
    if callable(func_or_chain) or isinstance(func_or_chain, tuple):
        func_or_chain = [func_or_chain, ]
    else:
        func_or_chain = list(func_or_chain)
    
    data = list(data)  # TODO: What if it is generator? Should I convert it to list? Or should I process it item by item by putting anothe item into queue?
    
    max_consumers_num = SharedMemorySMP.recommended_max_consumers_num() if process_num is None else process_num
    default_worker: Optional[Callable] = default_worker
    shared_memory_name: str = str(uuid4())
    operators: List[Process] = list()
    for _ in range(max_consumers_num):
        operators.append(Process(target=consumer_main, args=(shared_memory_name, try_to_use_uvloop)))
    
    with SharedMemorySMP(shared_memory_name, True, shared_memory_size, max_consumers_num=max_consumers_num) as sm:
        try:
            for another_operators in operators:
                another_operators.start()
            
            sm.wait_consumer_ready()

            with wait_my_turn(sm):
                request: List = sm.put_message(smp_map_chain_request(
                    in_sequence=data, 
                    out_sequence=[None] * len(data), 
                    saved_out_sequence_indexes=[None] * len(data), 
                    removed_sequence_indexes=list(), 
                    func_list=func_or_chain, 
                    curent_func_index=0, 
                    start=False, 
                    started_consumers_num=0, 
                    finished_consumers_num=0, 
                    cleanup_started_consumers_num=0, 
                    cleanuped_consumers_num=0, 
                    shut_down=False,
                    rwlock=RWLock(),
                    periodic_sleep_time=periodic_sleep_time,
                    ))
                request_lock: RWLock = request[SmpMapChainRequestFields.rwlock]
            
            last_iteration: bool = False
            while not last_iteration:
                with sm.get_in_line_on_write():
                    with request_lock.write():
                        request[SmpMapChainRequestFields.start] = True
                    
                    while True:
                        with request_lock.read():
                            if request[SmpMapChainRequestFields.started_consumers_num] == max_consumers_num:
                                break
                    
                        if periodic_sleep_time is None:
                            mm_pause()
                        else:
                            hps_sleep(periodic_sleep_time)
                    
                    with request_lock.write():
                        request[SmpMapChainRequestFields.start] = False
                    
                    while True:
                        with request_lock.read():
                            if request[SmpMapChainRequestFields.finished_consumers_num] == max_consumers_num:
                                break
                    
                        if periodic_sleep_time is None:
                            mm_pause()
                        else:
                            hps_sleep(periodic_sleep_time)
                    
                    request[SmpMapChainRequestFields.in_sequence] = [None] * len(request[SmpMapChainRequestFields.saved_out_sequence_indexes])

                    with request_lock.write():
                        request[SmpMapChainRequestFields.start] = True
                    
                    while True:
                        with request_lock.read():
                            if request[SmpMapChainRequestFields.cleanup_started_consumers_num] == max_consumers_num:
                                break
                    
                        if periodic_sleep_time is None:
                            mm_pause()
                        else:
                            hps_sleep(periodic_sleep_time)

                    with request_lock.write():
                        request[SmpMapChainRequestFields.start] = False
                    
                    while True:
                        with request_lock.read():
                            if request[SmpMapChainRequestFields.cleanuped_consumers_num] == max_consumers_num:
                                break
                    
                        if periodic_sleep_time is None:
                            mm_pause()
                        else:
                            hps_sleep(periodic_sleep_time)
                    
                    request[SmpMapChainRequestFields.out_sequence] = [None] * len(request[SmpMapChainRequestFields.in_sequence])

            with request_lock.write():
                request[SmpMapChainRequestFields.shut_down] = True

        finally:
            for another_operators in operators:
                another_operators.join()
            
            if sm is not None:
                sm.close()
