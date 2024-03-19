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
__version__ = "4.2.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


#!/usr/bin/env python3

import uvloop
uvloop.install()

if True:
    # increasing max decode packets to be able to transfer images
    # see https://github.com/miguelgrinberg/python-engineio/issues/142
    from engineio.payload import Payload
    Payload.max_decode_packets = 500

import asyncio
import uvicorn
import os
from collections import deque
from datetime import datetime
from pathlib import Path
from time import perf_counter, sleep
from typing import Set, Tuple

from cengal.code_flow_control.smart_values import ValueExistence
from cengal.math.numbers import RationalNumber
from cengal.parallel_execution.asyncio.atasks import create_task
from cengal.parallel_execution.coroutines.coro_scheduler import CoroID, Interface, CoroSchedulerDestroyRequestedException
from cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus import (AsyncEventBus,
                                                                                         AsyncEventBusRequest)
from cengal.parallel_execution.coroutines.coro_standard_services.cpu_tick_count_per_second import (
    CpuTickCountPerSecond, cpu_clock_cycles)
from cengal.parallel_execution.coroutines.coro_standard_services.instance import Instance, InstanceRequest
from cengal.parallel_execution.coroutines.coro_standard_services.lazy_print import lprint
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import (PutCoro, PutCoroRequest, aput_coro,
                                                                                  get_set_of_all_coro_children)
from cengal.parallel_execution.coroutines.coro_standard_services.simple_yield import Yield
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import AsyncioLoop, AsyncioLoopRequest
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly, CoroPriority, LoopYieldPriorityScheduler, LoopYieldPrioritySchedulerRequest
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_loop import ShutdownLoop
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_on_keyboard_interrupt import ShutdownOnKeyboardInterrupt
from cengal.parallel_execution.coroutines.coro_tools.await_coro import await_coro_prim, RunSchedulerInAsyncioLoop
from cengal.parallel_execution.coroutines.coro_tools.coro_flow_control import agraceful_coro_destroyer
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import (arun_in_fast_loop, arun_in_loop,
                                                                         run_in_fast_loop, run_in_loop)
from cengal.parallel_execution.coroutines.integrations.uvicorn import get_uvicorn_awaitable
from cengal.statistics.normal_distribution import count_99_95_68
from cengal.time_management.sleep_tools import ensure_waitable_time_or_bigger, get_usable_min_sleep_interval, try_sleep
from cengal.io.serve_free_ports import find_free_port
from cengal.io.used_ports import UsedPorts, PortsIterator, Protocol, PortStatus, unify_ports
from cengal.parallel_execution.asyncio.init_loop import init_loop
from cengal.parallel_execution.asyncio.run_loop import run_forever
from fastapi.responses import FileResponse
from pygments.formatters import HtmlFormatter


init_loop()


DESTROY_CENGAL_EVENT = 'DESTROY_CENGAL_EVENT'


async def retarding_coro(i: Interface, delta_time: RationalNumber, multiplier: RationalNumber):
    destroy_cengal_event: ValueExistence = await i(Instance, InstanceRequest().wait(DESTROY_CENGAL_EVENT))
    waiting_time = ensure_waitable_time_or_bigger(delta_time * multiplier)
    release_time = ensure_waitable_time_or_bigger(delta_time)
    while not destroy_cengal_event:
        try_sleep(waiting_time, None, sleep)
        await i(Sleep, release_time)


def natural_ratio(rational_ratio: RationalNumber) -> Tuple[int, int]:
    rational_ratio = abs(rational_ratio)
    if rational_ratio >= 1:
        return (1, int(round(rational_ratio)))
    else:
        rational_ratio = 1 / rational_ratio
        return (int(round(rational_ratio)), 1)


async def hard_retarding_coro(i: Interface, delta_time: RationalNumber, multiplier: RationalNumber):
    destroy_cengal_event: ValueExistence = await i(Instance, InstanceRequest().wait(DESTROY_CENGAL_EVENT))
    waiting_times, release_times = natural_ratio(multiplier)
    sleep_time = ensure_waitable_time_or_bigger(delta_time)
    while not destroy_cengal_event:
        for k in range(release_times):
            await i(Yield)

        for k in range(waiting_times):
            try_sleep(sleep_time, None, sleep)


async def print_tickcount(i: Interface, time_period: RationalNumber):
    destroy_cengal_event: ValueExistence = await i(Instance, InstanceRequest().wait(DESTROY_CENGAL_EVENT))
    while not destroy_cengal_event:
        cpu_clock_cycles, last_ticks_per_second, val_99, val_95, val_68, max_deviation, min_deviation = await i(CpuTickCountPerSecond)
        lprint(f'{datetime.now()} >> {cpu_clock_cycles=}, {last_ticks_per_second=}, {val_99=}, {val_95=}, {val_68=}, {max_deviation=}, {min_deviation=}')
        await i(Sleep, time_period)


async def print_iterations_per_second(i: Interface, time_period: RationalNumber):
    destroy_cengal_event: ValueExistence = await i(Instance, InstanceRequest().wait(DESTROY_CENGAL_EVENT))
    last_measurement_time: float = perf_counter()
    last_iteration_index: int = i._loop.iteration_index
    while not destroy_cengal_event:
        await i(Sleep, time_period)
        current_time: float = perf_counter()
        delta_time: float = current_time - last_measurement_time
        current_iteration_index: int = i._loop.iteration_index
        delta_iteration_index: int = current_iteration_index - last_iteration_index
        iterations_per_second: float = delta_iteration_index / delta_time
        last_measurement_time = current_time
        last_iteration_index = current_iteration_index
        lprint(f'{datetime.now()} >> {iterations_per_second=}')

    lprint(f'{datetime.now()} >> print_iterations_per_second() - Destroyed.')


async def print_iterations_per_second_2(i: Interface, time_period: RationalNumber):
    last_measurement_time: float = perf_counter()
    last_iteration_index: int = i._loop.iteration_index
    while True:
        await i(Sleep, time_period)
        current_time: float = perf_counter()
        delta_time: float = current_time - last_measurement_time
        current_iteration_index: int = i._loop.iteration_index
        delta_iteration_index: int = current_iteration_index - last_iteration_index
        iterations_per_second: float = delta_iteration_index / delta_time
        last_measurement_time = current_time
        last_iteration_index = current_iteration_index
        lprint(f'{datetime.now()} >> {iterations_per_second=}')


async def sleep_preventor(i: Interface):
    destroy_cengal_event: ValueExistence = await i(Instance, InstanceRequest().wait(DESTROY_CENGAL_EVENT))
    while not destroy_cengal_event:
        await i(Yield)

    lprint(f'{datetime.now()} >> sleep_preventor() - Destroyed.')


async def sleep_preventor_2(i: Interface):
    while True:
        await i(Yield)


async def sleep_preventor_with_iter_time_print(i: Interface, print_time_period: RationalNumber):
    destroy_cengal_event: ValueExistence = await i(Instance, InstanceRequest().wait(DESTROY_CENGAL_EVENT))
    _, _, val_99, _, _, _, _ = await i(CpuTickCountPerSecond, False)
    sliding_window = deque(maxlen=1000)
    last_cpu_clock_cycles: int = cpu_clock_cycles()
    last_stat_print_time = None
    while not destroy_cengal_event:
        _, _, val_99, _, _, _, _ = await i(CpuTickCountPerSecond, False)
        current_cpu_clock_cycles: int = cpu_clock_cycles()
        delta_cpu_clock_cycles: int = current_cpu_clock_cycles - last_cpu_clock_cycles
        seconds = delta_cpu_clock_cycles / val_99
        sliding_window.append(seconds)
        if (last_stat_print_time is None) or (print_time_period <= (current_cpu_clock_cycles - last_stat_print_time) / val_99):
            val_99, val_95, val_68, max_deviation, min_deviation = count_99_95_68(sliding_window)
            lprint(f'{datetime.now()} >> loop iteration time: {val_99=}, {val_95=}, {val_68=}, {max_deviation=}, {min_deviation=}')
            last_stat_print_time = cpu_clock_cycles()

        last_cpu_clock_cycles = current_cpu_clock_cycles


async def loop_time_print(i: Interface, print_time_period: RationalNumber):
    destroy_cengal_event: ValueExistence = await i(Instance, InstanceRequest().wait(DESTROY_CENGAL_EVENT))
    while not destroy_cengal_event:
        val_99, val_95, val_68, max_deviation, min_deviation = count_99_95_68(i._loop.sliding_window)
        lprint(f'{datetime.now()} >> Loop Iteration Time: {val_99=}, {val_95=}, {val_68=}, {max_deviation=}, {min_deviation=}')
        await i(Sleep, print_time_period)

    lprint(f'{datetime.now()} >> loop_time_print() - Destroyed.')


async def loop_time_print_2(i: Interface, print_time_period: RationalNumber):
    while True:
        val_99, val_95, val_68, max_deviation, min_deviation = count_99_95_68(i._loop.sliding_window)
        lprint(f'{datetime.now()} >> Loop Iteration Time: {val_99=}, {val_95=}, {val_68=}, {max_deviation=}, {min_deviation=}')
        await i(Sleep, print_time_period)


async def main_coro(i: Interface):
    lprint(f'{datetime.now()} >> Cengal Main Coro Init...')
    destroy_cengal_event = ValueExistence()
    await i(Instance, InstanceRequest().set(DESTROY_CENGAL_EVENT, destroy_cengal_event))

    delta_time: RationalNumber = 0.5
    multiplier: RationalNumber = 3
    # await i(PutCoro, retarding_coro, delta_time, multiplier)
    # await i(PutCoro, hard_retarding_coro, delta_time, multiplier)

    # await i(PutCoro, print_tickcount, 1.0)
    await i(PutCoro, print_iterations_per_second, 1.0)
    await i(PutCoro, loop_time_print, 1.0)
    await i(Sleep, 15)
    # await i(PutCoro, sleep_preventor_with_iter_time_print, 1.0)
    await i(PutCoro, sleep_preventor)

    lprint(f'{datetime.now()} >> Cengal Ready.')
    await i(AsyncEventBus, AsyncEventBusRequest().wait(DESTROY_CENGAL_EVENT))
    lprint(f'{datetime.now()} >> Destroying Cengal...')
    destroy_cengal_event.value = True
    children: Set[CoroID] = get_set_of_all_coro_children(i.coro_id)
    children.remove(i.coro_id)
    for child_coro_id in children:
        await agraceful_coro_destroyer(i, 2 * (delta_time + delta_time * multiplier), child_coro_id)

    await(Sleep, 2)
    pass


async def main_coro_2(i: Interface):
    lprint(f'{datetime.now()} >> Cengal Main Coro Init...')
    await i(PutCoro, print_iterations_per_second_2, 1.0)
    await i(PutCoro, loop_time_print_2, 1.0)
    await i(Sleep, 10)
    await i(PutCoro, sleep_preventor_2)
    lprint(f'{datetime.now()} >> Cengal Ready.')


async def asyncio_print_iterations_per_second(print_time_period: RationalNumber):
    index = 0
    last_time = perf_counter()
    while True:
        await asyncio.sleep(0)
        index += 1
        current_time = perf_counter()
        delta_time = current_time - last_time
        if print_time_period <= delta_time:
            iter_per_sec = index / delta_time
            print(f'{datetime.now()} >> asyncio >> {iter_per_sec=}')
            last_time = current_time
            index = 0


async def coro_print_iterations_per_second(i: Interface, print_time_period: RationalNumber):
    try:
        rs: RunSchedulerInAsyncioLoop = await i(Instance, InstanceRequest().get(RunSchedulerInAsyncioLoop))
        rs.execute_every_X_iterations = 1
    except KeyError:
        pass

    index = 0
    last_time = perf_counter()
    while True:
        await i(Yield)
        index += 1
        current_time = perf_counter()
        delta_time = current_time - last_time
        if print_time_period <= delta_time:
            iter_per_sec = index / delta_time
            print(f'{datetime.now()} >> coro >> {iter_per_sec=}')
            last_time = current_time
            index = 0
            # await i(ShutdownLoop)


def coro_print_iterations_per_second_1(i: Interface, print_time_period: RationalNumber):
    try:
        rs: RunSchedulerInAsyncioLoop = i(Instance, InstanceRequest().get(RunSchedulerInAsyncioLoop))
        rs.execute_every_X_iterations = 1
    except KeyError:
        pass

    index = 0
    last_time = perf_counter()
    while True:
        i(Yield)
        index += 1
        current_time = perf_counter()
        delta_time = current_time - last_time
        if print_time_period <= delta_time:
            iter_per_sec = index / delta_time
            print(f'{datetime.now()} >> coro >> {iter_per_sec=}')
            last_time = current_time
            index = 0


async def coro_print_iterations_per_second_2(i: Interface, print_time_period: RationalNumber):
    # await i(PutCoro, coro_print_iterations_per_second, 1.0)
    await i(AsyncioLoop, AsyncioLoopRequest().inherit_surrounding_loop())
    await i(AsyncioLoop, AsyncioLoopRequest().turn_on_loops_intercommunication())
    try:
        rs: RunSchedulerInAsyncioLoop = await i(Instance, InstanceRequest().get(RunSchedulerInAsyncioLoop))
        rs.execute_every_X_iterations = 1
    except KeyError:
        pass

    index = 0
    last_time = perf_counter()
    while True:
        await asyncio.sleep(0)
        # await asyncio.sleep(0.0019)
        # await i(AsyncioLoop, AsyncioLoopRequest().wait(asyncio.sleep(0.0019)))
        # await i(AsyncioLoop, AsyncioLoopRequest().wait_idle(asyncio.sleep(0.0019)))
        index += 1
        current_time = perf_counter()
        delta_time = current_time - last_time
        if print_time_period <= delta_time:
            iter_per_sec = index / delta_time
            print(f'{datetime.now()} >> asyncio in coro >> {iter_per_sec=}')
            last_time = current_time
            index = 0


async def main_coro_3(i: Interface, *args, **kwargs):
    print(f'{datetime.now()} >> Cengal Main Coro Init...')
    await i(ShutdownOnKeyboardInterrupt)
    # await i(LoopYieldPriorityScheduler, LoopYieldPrioritySchedulerRequest().setup(0.0001))
    await i(PutCoro, coro_print_iterations_per_second, 1.0)
    print(f'{datetime.now()} >> Cengal Ready.')


async def init_cengal():
    print(f'{datetime.now()} >> Cengal Initialisation...')

    # create_task(asyncio_print_iterations_per_second, 1.0)
    # await arun_in_fast_loop(main_coro)
    # await arun_in_fast_loop(coro_print_iterations_per_second, 1.0)
    # await arun_in_fast_loop(coro_print_iterations_per_second_1, 1.0)
    await arun_in_fast_loop(coro_print_iterations_per_second_2, 1.0)


async def destroy_cengal():
    async def coro(i: Interface):
        lprint(f'{datetime.now()} >> On Cengal Destroy')
        await i(AsyncEventBus, AsyncEventBusRequest().send_event(DESTROY_CENGAL_EVENT, None))
        await i(Sleep, 2)
        lprint(f'{datetime.now()} >> On Cengal Destroy - Done.')

    await await_coro_prim(coro)


# run_in_fast_loop(main_coro_2)
run_in_fast_loop(main_coro_3)
# run_in_fast_loop(coro_print_iterations_per_second, 1)
# run_in_fast_loop(coro_print_iterations_per_second_1, 1)


from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    create_task(init_cengal)
    pass


@app.on_event("shutdown")
async def startup_event():
    await destroy_cengal()
    pass


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


async def wait_sec(seconds: float):
    await asyncio.sleep(seconds)


async def main_coro_uvicorn_injected(i: Interface, *args, **kwargs):
    print(f'{datetime.now()} >> Cengal Main Coro Init...')
    await i(LoopYieldPriorityScheduler, LoopYieldPrioritySchedulerRequest().setup(0.0001))
    await i(PutCoro, coro_print_iterations_per_second, 1.0)
    await i(AsyncioLoop, AsyncioLoopRequest().start_internal_loop(get_uvicorn_awaitable(*args, **kwargs), CoroPriority.low, True))
    await i(Sleep, 10.0)
    print(f'{datetime.now()} >> Starting measurer for a 10 sec.')
    await i(AsyncioLoop, AsyncioLoopRequest().create_task(asyncio_print_iterations_per_second(1.0)))
    await i(AsyncioLoop, AsyncioLoopRequest().wait(wait_sec(10.0)))
    print(f'{datetime.now()} >> Cengal Ready.')


if __name__ == "__main__":
    print('START')
    used_ports: UsedPorts = UsedPorts()
    ports_iterartor: PortsIterator = PortsIterator(used_ports, Protocol.tcp, slice(18000, 19000), {PortStatus.na, PortStatus.no}, 1)
    port = asyncio.run(find_free_port('127.0.0.1', ports_iterartor))
    print(f'Found free port: {port}')

    # uvicorn.run(app, host="0.0.0.0", port=port, loop='asyncio')
    run_in_fast_loop(main_coro_uvicorn_injected, app, host="0.0.0.0", port=port)
