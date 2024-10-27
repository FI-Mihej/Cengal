from cengal.performance_test_lib import LineType, MeasureTime, measure_time_tl
from cengal.introspection.inspect import pcen, cen, pifr, pifrl, intro_func_repr_limited
from cengal.hardware.memory.barriers import full_memory_barrier
from cengal.code_inspection.auto_line_tracer import tl, tr, t, alt, LineType, OutputFields, AutoLineTracer
from cengal.user_interface.console.terminal import sprint, st, fill_current_line, cursor_forward, cursor_up, terminal_width, terminal, \
    set_background_color, BackgroundColor, set_foreground_color, ForegroundColor, erase_screen, erase_line, set_cursor_pos
from cengal.hardware.memory.shared_memory import *
from cengal.parallel_execution.asyncio.ashared_memory_manager import *
from cengal.hardware.memory.shared_memory_external_types.numpy_types import types_collection as numpy_types_collection

from multiprocessing import Process, Manager
from os.path import basename
from dataclasses import dataclass
from enum import IntEnum

import numpy as np
from typing import Union, List, Callable


class ArrayType(IntEnum):
    ndarray = 0
    py_list = 1
    matrix = 2


@dataclass
class Data:
    lock: RWLock
    print_lock: RWLock
    got_data_num: int
    processing_start_requested: bool
    processed_data_num: int
    a: np.ndarray
    b: np.ndarray
    c: np.ndarray
    array_type: ArrayType


async def consumer(shared_memory_name: str):
    pifrl()

    sm = SharedMemorySMP(shared_memory_name, external_types_collections=numpy_types_collection())
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


async def creator(shared_memory_name: str, max_consumers_num: int, data: Data, m, n, k):
    print(f'{cen()}()')

    sm = SharedMemorySMP(shared_memory_name, True, 1000 * 1024**2, max_consumers_num=max_consumers_num, external_types_collections=numpy_types_collection())
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


def benchmark_matmul_multiprocess(shared_memory_name: str, prepare_data: Callable, m, n, k):
    recommended_max_consumers_num = SharedMemorySMP.recommended_max_consumers_num()
    # max_consumers_num = 10
    # max_consumers_num = 1
    max_consumers_num = recommended_max_consumers_num

    fill_current_line(st(' ').b_cyan.bs_dim)
    print()  # same as `sprint()` in this case: when we just need to print a newline

    fill_current_line(st(' ').b_blue)
    cursor_forward(3)
    sprint(st(
        ' ', st(shared_memory_name).f_yellow.sdim, st('(').f_green.sbright, m, st(',').f_green.sbright, n, st(',').f_green.sbright, k, st(')').f_green.sbright
    ).b_blue.f_white)

    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint()  # same as `print()` in this case: when we just need to print a newline

    fill_current_line(st(' ').b_cyan.bs_dim)
    cursor_forward(3)
    sprint(st(
        st(' recommended_max_consumers_num').f_green.sdim, ' = ', st(recommended_max_consumers_num).f_yellow.sdim, ' '
    ).b_blue.f_white)

    if max_consumers_num == recommended_max_consumers_num:
        fill_current_line(st(' ').b_cyan.bs_dim)
        cursor_forward(3)
        sprint(st(
            ' And we will spawn ', st(max_consumers_num).f_yellow.sdim, ' consumers '
        ).b_blue.f_white)
    else:
        fill_current_line(st(' ').b_cyan.bs_dim)
        cursor_forward(3)
        sprint(st(
            ' But we will spawn ', st(max_consumers_num).f_yellow.sdim, ' consumers instead '
        ).b_blue.f_white)
    
    fill_current_line(st(' ').b_cyan.bs_dim)
    print()  # same as `sprint()` in this case: when we just need to print a newline

    operators: List[Process] = list()
    operators.append(Process(target=creator_main, args=(shared_memory_name, max_consumers_num, prepare_data(m, n, k), m, n, k)))
    for _ in range(max_consumers_num):
        operators.append(Process(target=consumer_main, args=(shared_memory_name, )))
    
    for another_operators in operators:
        another_operators.start()

    for another_operators in operators:
        another_operators.join()


@alt.start_end()  # Will trace the start and the end of the function as well as input values and the result
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


@terminal()  # This is needed to make sure that terminal colors will be reset after the script is done
def main():
    erase_screen()
    set_cursor_pos(0, 0)

    # alt.rich_allowed = False  # Will disable Rich output even if it is installed. Will print only plain (uncolored) text
    alt.output_fields.add(OutputFields.process_pid)  # This is needed to make sure that the process id will be printed by the tracer
        # You can use alt tracer either directly or by using `tr()` and `tl()` functions
        # tr() will return the result of the expression and will print info about the current code line and about the result
        # tl() will print info about the next code line

    fill_current_line(st(' ').b_cyan.bs_dim)
    print()  # same as `sprint()` in this case: when we just need to print a newline
    fill_current_line(st('=').b_blue.f_white)
    print()
    fill_current_line(st('=').b_blue.f_white)
    cursor_forward(3)
    sprint(st(
        ' ', st(basename(__file__)).f_green.sdim, ' '
    ).b_blue.f_white)
    fill_current_line(st('=').b_blue.f_white)
    print()
    fill_current_line(st(' ').b_cyan.bs_dim)
    print()  # same as `sprint()` in this case: when we just need to print a newline

    dimension: int = tr(256)  # Trace Result. Will return 256 and print info about current code line and about the result
    tl()  # Trace Line. Will print info about next code line
    python_mflops = benchmark_matmul_multiprocess(
        'benchmark_matmul_numpy_multiprocess', 
        prepare_numpy_data, 
        dimension, dimension, dimension)


if '__main__' == __name__:
    ensure_adjusted_pythonhashseed()  # Ensure that the hash seed is adjusted for this process group
    # ensure_adjusted_scientific()  # Ensure (for this process group) that: 1) the hash seed is adjusted; 2) interpreter optimizations ('-OO') are turned on; 3) the integer string conversion length limitation is turned off
    main()
