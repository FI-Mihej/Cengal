from cengal.performance_test_lib import MeasureTimeTraceLine, LineType, MeasureTime
from cengal.introspection.inspect import pcen, cen, pifr, pifrl
from cengal.text_processing.text_processing import to_identifier
from cengal.hardware.memory.barriers import full_memory_barrier
from cengal.time_management.high_precision_sync_sleep import hps_sleep
from cengal.code_inspection.line_tracer import LineTracer
from cengal.code_inspection.auto_line_tracer import tl, tr, t, alt, LineType, OutputFields, AutoLineTracer
from cengal.hardware.memory.shared_memory import *

from multiprocessing import Process, Manager
from os.path import basename
from dataclasses import dataclass
from enum import IntEnum

import numpy as np
from typing import Union, List, Callable


class Matrix:
    def __init__(self, value, rows, cols):
        self.value = value
        self.rows = rows
        self.cols = cols
        self.shape = (rows, cols)

    def __getitem__(self, idxs):
        return self.value[idxs[0]][idxs[1]]

    def __setitem__(self, idxs, value):
        self.value[idxs[0]][idxs[1]] = value
    
    @staticmethod
    def get_item(data, idxs):
        return data[idxs[0]][idxs[1]]
    
    @staticmethod
    def set_item(data, idxs, value):
        data[idxs[0]][idxs[1]] = value


def matmul_python(C, A, B):
    for m in range(C.rows):
        for k in range(A.cols):
            for n in range(C.cols):
                C[m, n] += A[m, k] * B[k, n]


def benchmark_matmul_matrix(M, N, K):
    print('===========================')
    print(f'{cen()}: {M}, {N}, {K}')
    A = Matrix(list(np.random.rand(M, K)), M, K)
    B = Matrix(list(np.random.rand(K, N)), K, N)
    C = Matrix(list(np.zeros((M, N))), M, N)
    with MeasureTimeTraceLine() as mt:
        matmul_python(C, A, B)

    # secs = timeit(lambda: matmul_python(C, A, B), number=2)/2
    secs = mt.time_spent
    print(f'time spent: {secs}')
    mflops = ((2*M*N*K)/secs) / 1e6
    print(mflops, "MFLOP/s")
    print()
    return mflops


def benchmark_matmul_python(M, N, K):
    print('===========================')
    print(f'{cen()}: {M}, {N}, {K}')
    A = Matrix(list(np.random.rand(M, K).tolist()), M, K)
    B = Matrix(list(np.random.rand(K, N).tolist()), K, N)
    C = Matrix(list(np.zeros((M, N)).tolist()), M, N)

    c_rows, c_cols = C.shape
    a_rows, a_cols = A.shape
    b_rows, b_cols = B.shape
    a = list(A.value)
    b = list(B.value)
    c = list(C.value)
    # pdi(a[0])

    # tr((c_rows, a_cols, c_cols))
    with MeasureTimeTraceLine() as mt:
        for m in range(c_rows):
            for k in range(a_cols):
                for n in range(c_cols):
                    c[m][n] += a[m][k] * b[k][n]
    
    # secs = timeit(lambda: matmul_python(C, A, B), number=2)/2
    secs = mt.time_spent
    print(f'time spent: {secs}')
    mflops = ((2*M*N*K)/secs) / 1e6
    print(mflops, "MFLOP/s")
    print()
    return mflops


def matmul_numpy(C: np.ndarray, A: np.ndarray, B: np.ndarray):
    c_rows, c_cols = C.shape
    a_rows, a_cols = A.shape
    b_rows, b_cols = B.shape
    for m in range(c_rows):
        for k in range(a_cols):
            for n in range(c_cols):
                C[m, n] += A[m, k] * B[k, n]


def benchmark_matmul_numpy(M, N, K):
    print('===========================')
    print(f'{cen()}: {M}, {N}, {K}')
    A = np.random.rand(M, K)
    B = np.random.rand(K, N)
    C = np.zeros((M, N))
    with MeasureTimeTraceLine() as mt:
        matmul_numpy(C, A, B)
    
    # secs = timeit(lambda: matmul_numpy(C, A, B), number=2)/2
    secs = mt.time_spent
    print(f'time spent: {secs}')
    mflops = ((2*M*N*K)/secs) / 1e6
    print(mflops, "MFLOP/s")
    print()
    return mflops


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


def consumer(shared_memory_name: str, consumer_id: Optional[int]):
    pifrl()
    with SharedMemory(shared_memory_name, consumer_id=consumer_id) as sm:
        sm.init_consumer()
        max_consumers_num: int = sm.max_consumers_num
        my_id: int = sm.consumer_id
        print(f'Consumer {my_id} started...')

        # tl()
        with wait_my_turn_when_has_messages(sm):
            mapped_data: Data = sm.read_message()
            lock: RWLock = mapped_data.lock
            a = mapped_data.a
            b = mapped_data.b
            c = mapped_data.c
        
            # tl()
            with lock.write():
                # tl()
                mapped_data.got_data_num += 1
            
        # tl()
        with sm.get_in_line_on_write(periodic_sleep_time=None):
            # tl()
            processing_start_requested: bool = False
            # tl()
            while not processing_start_requested:
                with lock.read():
                    processing_start_requested = mapped_data.processing_start_requested
                    full_memory_barrier()

            # tl()
            if mapped_data.array_type in {ArrayType.ndarray, ArrayType.matrix, ArrayType.py_list}:
                c_rows, c_cols = c.shape
                a_rows, a_cols = a.shape
                b_rows, b_cols = b.shape

            if ArrayType.ndarray == mapped_data.array_type:
                for m in range(my_id, c_rows, max_consumers_num):
                    for k in range(a_cols):
                        for n in range(c_cols):
                            c[m, n] += a[m, k] * b[k, n]
            elif ArrayType.matrix == mapped_data.array_type:
                a = a.value
                b = b.value
                c = c.value

                for m in range(my_id, c_rows, max_consumers_num):
                    for k in range(a_cols):
                        for n in range(c_cols):
                            Matrix.set_item(c, (m, n), Matrix.get_item(c, (m, n)) + (Matrix.get_item(a, (m, k)) * Matrix.get_item(b, (k, n))))
            elif ArrayType.py_list == mapped_data.array_type:
                a = list(a.value)
                b = list(b.value)
                c = list(c.value)
                # pdi(a[0])

                # tr((c_rows, a_cols, c_cols))
                for m in range(my_id, c_rows, max_consumers_num):
                    for k in range(a_cols):
                        for n in range(c_cols):
                            c[m][n] += a[m][k] * b[k][n]
                
                # t('processing finished')
            
            # tl()
            with lock.write():
                mapped_data.processed_data_num += 1
        
    print(f'Consumer {my_id} done.')


def creator(shared_memory_name: str, max_consumers_num: int, data: Data, m, n, k):
    pifrl()
    with SharedMemory(shared_memory_name, True, 1000 * 1024**2, max_consumers_num=max_consumers_num) as sm:
        sm.wait_consumer_ready()
        # tl()
        with wait_my_turn(sm):
            mapped_data: Data = None
            message_offset: Offset = None
            mapped_data, message_offset = sm.put_message_2(data)
            lock: RWLock = mapped_data.lock
            
        # tl()
        with sm.get_in_line_on_write():
            result = True
            while result:
                # tl()
                with lock.read():
                    # tl()
                    result = sm.max_consumers_num > mapped_data.got_data_num

            # tl()
            with MeasureTime('Multiprocessing - creator', do_print=False) as mt:
                # tl()
                with lock.write(periodic_sleep_time=None):
                    # tl()
                    mapped_data.processing_start_requested = True

                result = True
                # tl()
                while result:
                    with lock.read():
                        sleep(0.01)
                        result = sm.max_consumers_num > mapped_data.processed_data_num

            # tl()
            secs = mt.time_spent
            mflops = ((2*m*n*k)/secs) / 1e6
            print(f'time spent: {secs}')
            print(mflops, "MFLOP/s")
            print()
            return mflops


def benchmark_matmul_multiprocess(shared_memory_name: str, manual_consumer_ids: bool, prepare_data: Callable, m, n, k):
    print('===========================')
    print(f'{shared_memory_name}: {m}, {n}, {k}')

    # max_consumers_num = cpu_info().virtual_cores_num or 1
    max_consumers_num = SharedMemory.recommended_max_consumers_num()
    max_consumers_num = 10
    # max_consumers_num = 1
    print(f'{max_consumers_num=}')
    operators: List[Process] = list()
    operators.append(Process(target=creator, args=(shared_memory_name, max_consumers_num, prepare_data(m, n, k), m, n, k)))
    consumer_id = -1
    for _ in range(max_consumers_num):
        if manual_consumer_ids:
            operators.append(Process(target=consumer, args=(shared_memory_name, consumer_id)))
        else:
            operators.append(Process(target=consumer, args=(shared_memory_name, None)))
        
        consumer_id += 1
    
    for another_operators in operators:
        another_operators.start()

    for another_operators in operators:
        another_operators.join()


@alt.start_end()
def prepare_numpy_data(m, n, k):
    return Data(
        RWLock(),
        0,
        False,
        0,
        np.random.rand(m, k),
        np.random.rand(k, n),
        np.zeros((m, n)),
        ArrayType.ndarray,
    )


def prepare_matrix_data(m, n, k):
    return Data(
        RWLock(), 
        0, 
        False, 
        0, 
        Matrix(list(np.random.rand(m, k)), m, k), 
        Matrix(list(np.random.rand(k, n)), k, n), 
        Matrix(list(np.zeros((m, n))), m, n), 
        ArrayType.matrix,
    )


def prepare_python_data(m, n, k):
    with alt.start_end():
        return Data(
            RWLock(), 
            0, 
            False, 
            0, 
            Matrix(list(np.random.rand(m, k).tolist()), m, k), 
            Matrix(list(np.random.rand(k, n).tolist()), k, n), 
            Matrix(list(np.zeros((m, n)).tolist()), m, n), 
            ArrayType.py_list,
        )


def main(manual_consumer_ids: bool):
    # alt.rich_allowed = False
    alt.output_fields.add(OutputFields.process_pid)

    dimension: int = 128
    # python_mflops = benchmark_matmul_matrix(dimension, dimension, dimension)
    python_mflops = benchmark_matmul_python(dimension, dimension, dimension)
    python_mflops = benchmark_matmul_numpy(dimension, dimension, dimension)

    dimension: int = 256
    python_mflops = benchmark_matmul_multiprocess(
        'benchmark_matmul_numpy_multiprocess', 
        manual_consumer_ids, 
        prepare_numpy_data, 
        dimension, dimension, dimension)

    # dimension: int = 32
    # python_mflops = benchmark_matmul_multiprocess(
    #     'benchmark_matmul_matrix_multiprocess', 
    #     manual_consumer_ids, 
    #     prepare_matrix_data, 
    #     dimension, dimension, dimension)

    dimension: int = 128
    python_mflops = benchmark_matmul_multiprocess(
        'benchmark_matmul_python_multiprocess', 
        manual_consumer_ids, 
        prepare_python_data, 
        dimension, dimension, dimension)


if '__main__' == __name__:
    ensure_adjusted_pythonhashseed()  # Ensure that the hash seed is adjusted for this process group
    # ensure_adjusted_scientific()  # Ensure (for this process group) that: 1) the hash seed is adjusted; 2) interpreter optimizations are turned on; 3) the integer string conversion length limitation is turned off
    main(False)
    main(True)
