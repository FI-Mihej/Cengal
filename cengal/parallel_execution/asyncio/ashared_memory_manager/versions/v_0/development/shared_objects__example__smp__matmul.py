from cengal.performance_test_lib import MeasureTime
from cengal.hardware.memory.barriers import full_memory_barrier
from cengal.hardware.memory.shared_memory import *

from multiprocessing import Process
from dataclasses import dataclass
from enum import IntEnum

import numpy as np
from typing import List, Callable


class ArrayType(IntEnum):
    ndarray = 0
    py_list = 1
    matrix = 2


@dataclass
class Data:
    lock: RWLock
    got_data_num: int
    processing_start_requested: bool
    processed_data_num: int
    a: np.ndarray
    b: np.ndarray
    c: np.ndarray
    array_type: ArrayType


def consumer(shared_memory_name: str):
    with SharedMemorySMP(shared_memory_name) as sm:
        sm.init_consumer()
        max_consumers_num: int = sm.max_consumers_num
        my_id: int = sm.consumer_id
        with wait_my_turn_when_has_messages(sm):
            mapped_data: Data = sm.read_message()
            lock: RWLock = mapped_data.lock
            a = mapped_data.a
            b = mapped_data.b
            c = mapped_data.c
        
            with lock.write():
                mapped_data.got_data_num += 1
            
        with sm.get_in_line_on_write(periodic_sleep_time=None):
            processing_start_requested: bool = False
            while not processing_start_requested:
                with lock.read():
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
            
            with lock.write():
                mapped_data.processed_data_num += 1


def creator(shared_memory_name: str, max_consumers_num: int, data: Data, m, n, k):
    with SharedMemorySMP(shared_memory_name, True, 1000 * 1024**2, max_consumers_num=max_consumers_num) as sm:
        sm.wait_consumer_ready()
        with wait_my_turn(sm):
            mapped_data: Data = None
            message_offset: Offset = None
            mapped_data, message_offset = sm.put_message_2(data)
            lock: RWLock = mapped_data.lock
        
        mflops = None
        with sm.get_in_line_on_write():
            result = True
            while result:
                with lock.read():
                    result = sm.max_consumers_num > mapped_data.got_data_num

            with MeasureTime('Multiprocessing - creator', do_print=False) as mt:
                with lock.write(periodic_sleep_time=None):
                    mapped_data.processing_start_requested = True

                result = True
                while result:
                    with lock.read():
                        sleep(0.01)
                        result = sm.max_consumers_num > mapped_data.processed_data_num

            secs = mt.time_spent
            mflops = ((2*m*n*k)/secs) / 1e6
            return mflops


def benchmark_matmul_multiprocess(shared_memory_name: str, prepare_data: Callable, m, n, k):
    recommended_max_consumers_num = SharedMemorySMP.recommended_max_consumers_num()
    # max_consumers_num = 10
    # max_consumers_num = 1
    max_consumers_num = recommended_max_consumers_num

    operators: List[Process] = list()
    operators.append(Process(target=creator, args=(shared_memory_name, max_consumers_num, prepare_data(m, n, k), m, n, k)))
    for _ in range(max_consumers_num):
        operators.append(Process(target=consumer, args=(shared_memory_name, )))
    
    for another_operators in operators:
        another_operators.start()

    for another_operators in operators:
        another_operators.join()


def prepare_numpy_data(m, n, k):
    return Data(
        RWLock(),
        RWLock(),
        0,
        False,
        0,
        np.random.rand(m, k),
        np.random.rand(k, n),
        np.zeros((m, n)),
        ArrayType.ndarray,
    )


def main():
    dimension: int = 256
    python_mflops = benchmark_matmul_multiprocess(
        'benchmark_matmul_numpy_multiprocess', 
        prepare_numpy_data, 
        dimension, dimension, dimension)


if '__main__' == __name__:
    ensure_adjusted_pythonhashseed()  # Ensure that the hash seed is adjusted for this process group
    # ensure_adjusted_scientific()  # Ensure (for this process group) that: 1) the hash seed is adjusted; 2) interpreter optimizations ('-OO') are turned on; 3) the integer string conversion length limitation is turned off
    ensure_adjusted_scientific()
    main()