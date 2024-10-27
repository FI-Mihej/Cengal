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


from cengal.performance_test_lib import mperformance_tl, mtime_tl
from cengal.code_flow_control.context_management import conditional
from cengal.code_inspection.auto_line_tracer import tr, alt
from cengal.introspection.inspect import cen
from cengal.parallel_execution.asyncio.run_in_process_pool.versions.v_0.run_in_process_pool import *

import asyncio
import pickle
from math import ceil
from concurrent.futures import ProcessPoolExecutor


async def aworker(int_data: int) -> int:
    return int_data + 1


def worker(int_data: int) -> int:
    return int_data + 1


def pickle_perf_sync():
    print(f'{cen()} Data size: {len(pickle.dumps((worker, 0)))}')
    with mperformance_tl(1.0, cen(), turn_off_gc=True) as pt:
        while pt():
            data = pickle.dumps((worker, 0))
            w, i = pickle.loads(data)


def pickle_perf_async():
    print(f'{cen()} Data size: {len(pickle.dumps((worker, 0)))}')
    with mperformance_tl(1.0, cen(), turn_off_gc=True) as pt:
        while pt():
            data = pickle.dumps((aworker, 0))
            w, i = pickle.loads(data)


def multiprocess_sync():
    bench_name = cen()
    async def coro():
        pp: ProcessPool = ProcessPool(ExecutorTypeSetup(ProcessPoolExecutor))
        pp.set_is_multiprocessing(True)
        with mperformance_tl(1.0, bench_name, turn_off_gc=True) as pt:
            while pt():
                result = await pp(worker, 0)
    
    asyncio.run(coro())


def multiprocess_sync_single():
    bench_name = cen()
    async def coro():
        pp: ProcessPool = ProcessPool(ExecutorTypeSetup(ProcessPoolExecutor))
        pp.set_is_multiprocessing(True)
        with conditional(mtime_tl(bench_name, depth=2), True):
            result = await pp(worker, 0)
    
    asyncio.run(coro())


def multiprocess_sync_massive():
    bench_name = cen()
    async def coro():
        pp: ProcessPool = ProcessPool(ExecutorTypeSetup(ProcessPoolExecutor))
        pp.set_is_multiprocessing(True)
        with mperformance_tl(0.1, 'WARMUP: ' + bench_name, do_print=False, turn_off_gc=True) as pt:
            while pt():
                result = await pp(worker, 0)

        concurent_coros: int = 1000
        with mperformance_tl(3.0, bench_name, turn_off_gc=True) as pt:
            while pt():
                results = await asyncio.gather(*[pp(worker, 0) for i in range(concurent_coros)])
        
        print(f'{alt.additional_lines_prefix}Resulting iterations: {pt.iterations_made * concurent_coros}')
        print(f'{alt.additional_lines_prefix}Resulting performance: {(pt.iterations_made * concurent_coros) / pt.time_spent} requests/second')
    
    asyncio.run(coro())


def multiprocess_async():
    bench_name = cen()
    async def coro():
        pp: ProcessPool = ProcessPool(ExecutorTypeSetup(ProcessPoolExecutor))
        pp.set_is_multiprocessing(True)
        with mperformance_tl(1.0, bench_name, turn_off_gc=True) as pt:
            while pt():
                result = await pp(aworker, 0)
    
    asyncio.run(coro())


def multiprocess_async_single():
    bench_name = cen()
    async def coro():
        pp: ProcessPool = ProcessPool(ExecutorTypeSetup(ProcessPoolExecutor))
        pp.set_is_multiprocessing(True)
        with conditional(mtime_tl(bench_name, depth=2), True):
            result = await pp(aworker, 0)
    
    asyncio.run(coro())


def multiprocess_async_massive():
    bench_name = cen()
    async def coro():
        pp: ProcessPool = ProcessPool(ExecutorTypeSetup(ProcessPoolExecutor))
        pp.set_is_multiprocessing(True)
        with mperformance_tl(0.1, 'WARMUP: ' + bench_name, do_print=False, turn_off_gc=True) as pt:
            while pt():
                result = await pp(aworker, 0)

        concurent_coros: int = 1000
        with mperformance_tl(3.0, bench_name, turn_off_gc=True) as pt:
            while pt():
                results = await asyncio.gather(*[pp(aworker, 0) for i in range(concurent_coros)])
        
        print(f'{alt.additional_lines_prefix}Resulting iterations: {pt.iterations_made * concurent_coros}')
        print(f'{alt.additional_lines_prefix}Resulting performance: {(pt.iterations_made * concurent_coros) / pt.time_spent} requests/second')
    
    asyncio.run(coro())


def singleprocess_sync():
    bench_name = cen()
    async def coro():
        pp: ProcessPool = ProcessPool(ExecutorTypeSetup(ProcessPoolExecutor))
        pp.set_is_multiprocessing(False)
        with mperformance_tl(1.0, bench_name, turn_off_gc=True) as pt:
            while pt():
                result = await pp(worker, 0)
    
    asyncio.run(coro())


def singleprocess_async():
    bench_name = cen()
    async def coro():
        pp: ProcessPool = ProcessPool(ExecutorTypeSetup(ProcessPoolExecutor))
        pp.set_is_multiprocessing(False)
        with mperformance_tl(1.0, bench_name, turn_off_gc=True) as pt:
            while pt():
                result = await pp(aworker, 0)
    
    asyncio.run(coro())


def main():
    pickle_perf_sync()
    pickle_perf_async()
    multiprocess_sync_single()
    multiprocess_async_single()
    multiprocess_sync()
    multiprocess_async()
    multiprocess_sync_massive()
    multiprocess_async_massive()
    singleprocess_sync()
    singleprocess_async()


if '__main__' == __name__:
    main()
