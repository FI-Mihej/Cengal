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
__version__ = "4.3.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


#!/usr/bin/env python3
import asyncio
import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager, Queue
from typing import Tuple, Dict
from cengal.parallel_execution.coroutines.coro_scheduler import Interface, cs_acoro, cs_coro
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import (
    CoroPriority, agly, gly)
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.instance import InstanceRequest
from nicegui import app, ui, Client
from cengal.parallel_execution.coroutines.integrations.nicegui import run, apage, sl_page


pool = ProcessPoolExecutor()


def heavy_computation(q: Queue) -> str:
    '''Some heavy computation that updates the progress bar through the queue.'''
    n = 50
    for i in range(n):
        # Perform some heavy computation
        time.sleep(0.1)

        # Update the progress bar through the queue
        q.put_nowait(i / n)
    return 'Done!'


# @ui.page('/')
@sl_page(True, 200.0)
@cs_coro
def main_page_impl():
# def main_page_impl(i: Interface):
    ly = gly(CoroPriority.normal)

    async def start_computation():
        progressbar.visible = True
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(pool, heavy_computation, queue)
        ui.notify(result)
        progressbar.visible = False

    # Create a queue to communicate with the heavy computation process
    queue = Manager().Queue()
    # Update the progress bar on the main process
    ui.timer(0.1, callback=lambda: progressbar.set_value(queue.get() if not queue.empty() else progressbar.value))

    # Create the UI
    for j in range(100):
        ui.button(f'compute {j}', on_click=start_computation)
        ly()

    progressbar = ui.linear_progress(value=0).props('instant-feedback')
    progressbar.visible = False


# @ui.page('/')
# def main_page():
#     main_page_impl()
        

@ui.page('/', response_timeout=30)
@apage
@cs_acoro
async def main_page_impl_2(client: Client):
# async def main_page_impl_2(i: Interface, client: Client):
    ly = await agly(CoroPriority.normal)

    async def start_computation():
        progressbar.visible = True
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(pool, heavy_computation, queue)
        ui.notify(result)
        progressbar.visible = False

    # Create a queue to communicate with the heavy computation process
    queue = Manager().Queue()
    # Update the progress bar on the main process
    progressbar_update_timer = ui.timer(0.1, callback=lambda: progressbar.set_value(queue.get() if not queue.empty() else progressbar.value))
    progressbar_update_timer.active = False
    # def destroy_progressbar_update_timer():
    #     progressbar_update_timer.active = False
    #     print(f'progressbar_update_timer made Inactive')
    
    # client.handlers.add_on_disconnected_handler(destroy_progressbar_update_timer)

    ui.link('show server startup parameters', show_server_startup_parameters)
    ui.link('wait for connection', wait_for_connection)
    ui.button(f'compute', on_click=start_computation)
    ui_update_progressbar = ui.linear_progress(value=0).props('instant-feedback')
    ui_update_progressbar_update_timer = ui.timer(0.1, callback=lambda: ui_update_progressbar.set_value(shown / bnum))
    ui_update_progressbar_update_timer.active = False
    await client.connected()

    # Create the UI
    bnum = 1000
    shown = 0
    ui_update_progressbar_update_timer.active = True
    for j in range(bnum):
        ui.button(f'compute {j}', on_click=start_computation)
        await ly()
        shown += 1
        # await i(Sleep, 0.05)
        # await asyncio.sleep(0.01)

    ui_update_progressbar.set_value(1)
    ui_update_progressbar.visible = False

    progressbar = ui.linear_progress(value=0).props('instant-feedback')
    progressbar_update_timer.active = True
    progressbar.visible = False
    # client.page_items(progressbar)


# @ui.page('/')
# async def main_page_2():
#     await main_page_impl_2()


@ui.page('/wait_for_connection', response_timeout=30)
@apage
# @cs_acoro
async def wait_for_connection(i: Interface, client: Client):
    ui.label('This text is displayed immediately.')
    progressbar = ui.linear_progress(value=0).props('instant-feedback')
    progressbar_update_timer = ui.timer(0.1, callback=lambda: progressbar.set_value(shown / bnum))
    progressbar_update_timer.active = False

    await client.connected()
    # await asyncio.sleep(2)
    ui.label('This text is displayed 2 seconds after the page has been fully loaded.')
    ui.label(f'The IP address {client.ip} was obtained from the websocket.')
    bnum = 100
    shown = 0
    progressbar_update_timer.active = True
    for j in range(bnum):
        ui.button(f'compute {j}')
        shown += 1
        await i(Sleep, 0.05)
    
    # progressbar_update_timer.active = False
    # await i(Sleep, 0.2)
    progressbar.set_value(1)
    progressbar.visible = False
    # await asyncio.sleep(0.5)
    # del progressbar_update_timer


@ui.page('/show_server_startup_parameters', response_timeout=30)
@apage
# @cs_acoro
async def show_server_startup_parameters(i: Interface):
    app_args_kwargs: Tuple[Tuple, Dict] = await i(InstanceRequest().wait('nicegui_app_args_kwargs'))
    args, kwargs = app_args_kwargs
    if args:
        ui.label('ARGS:')
        for value in args:
            ui.label(f'{value}')

    ui.label('KWARGS:')
    for key, value in kwargs.items():
        ui.label(f'{key}: {value}')


# stop the pool when the app is closed; will not cancel any running tasks
app.on_shutdown(pool.shutdown)


if '__main__' == __name__:
    run(port_or_range=(18000, 18050), reload=False)
