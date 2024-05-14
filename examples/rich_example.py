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


from uuid import uuid4
import asyncio
from datetime import datetime
from typing import Dict, Hashable

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
from cengal.parallel_execution.coroutines.coro_tools.wait_coro import sync_coro
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro
from cengal.parallel_execution.coroutines.coro_standard_services.kill_coro import KillCoro
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.timer_coro_runner import TimerCoroRunner
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import AsyncioLoopRequest
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly_patched, gly_patch
from cengal.parallel_execution.coroutines.coro_standard_services.tkinter import TkinterContextManager
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_on_keyboard_interrupt import ShutdownOnKeyboardInterrupt
from cengal.parallel_execution.coroutines.coro_standard_services.instance import InstanceRequest
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_loop import ShutdownLoop
from cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus import AsyncEventBusRequest
from cengal.parallel_execution.coroutines.integrations.customtkinter import prepare_mainloop
from cengal.parallel_execution.coroutines.coro_tools.await_coro import await_task_prim
from cengal.code_flow_control.smart_values import ValueExistence
from cengal.text_processing.encoding_detection import detect_and_decode
from cengal.time_management.repeat_for_a_time import Tracer, TracerIterator
from cengal.math.numbers import RationalNumber

from third_party_cpu_bound import third_party_cpu_bound_computations, DataHolder
gly_patch(third_party_cpu_bound_computations)  # patching third party code

import aiofiles

import tkinter
import customtkinter


DoneEventID: Hashable = f'DoneEventID {uuid4()}'
State: Hashable = uuid4()
CPUBoundCounters: Hashable = uuid4()


@cs_coro
@gly_patched
def cpu_bound_computations(num: int, counter_holder: DataHolder) -> int:
    for i in range(num):
        counter_holder.counter += 1
        for j in range(num):
            counter_holder.counter += 1
            for k in range(num):
                counter_holder.counter += 1
    
    return counter_holder.counter


async def asyncio_io_bound_coroutine(file_name: str, reading_time: RationalNumber):
    for i in TracerIterator(Tracer(reading_time)):  # will iterate for N seconds
        async with aiofiles.open(file_name, mode='rb') as f:
            text, encoding, bom_bytes = detect_and_decode(await f.read())
    
    return text, encoding, bom_bytes


def tkinter_counter_view_app(i: Interface):
    with(TkinterContextManager(i, tkinter.Tk())) as wr:
        app: tkinter.Tk = wr.tk
        app.geometry('400x150+0+100')
        button_holder: ValueExistence[tkinter.Button] = ValueExistence()
        state_label_holder: ValueExistence[tkinter.Label] = ValueExistence()
        counter_label_holder: ValueExistence[tkinter.Label] = ValueExistence()
        third_party_counter_label_holder: ValueExistence[tkinter.Label] = ValueExistence()

        @sync_coro
        async def kill_counter(i: Interface):
            counters = await i(InstanceRequest().wait(CPUBoundCounters))
            counter_coro_id, _ = counters['own_counter']
            third_party_counter_coro_id, _ = counters['third_party_counter']
            await i(KillCoro, counter_coro_id)
            await i(KillCoro, third_party_counter_coro_id)
            button_holder.value.configure(state='disabled')

        button_holder.value = tkinter.Button(app, text="Kill Counter Coroutine", command=kill_counter, state='disabled')
        button_holder.value.pack()
        state_label_holder.value = tkinter.Label(app)
        state_label_holder.value.pack()
        counter_label_holder.value = tkinter.Label(app)
        counter_label_holder.value.pack()
        third_party_counter_label_holder.value = tkinter.Label(app)
        third_party_counter_label_holder.value.pack()
        
        async def state_monitor(i: Interface):
            await i(InstanceRequest().wait(State))
            while await i(Sleep, 1/60):
                state_label_holder.value.configure(text=await i(InstanceRequest().get(State)))
                try:
                    counters = await i(InstanceRequest().get(CPUBoundCounters))
                    _, counter_holder = counters['own_counter']
                    _, third_party_counter_holder = counters['third_party_counter']
                    counter_label_holder.value.configure(text=str(counter_holder.counter))
                    third_party_counter_label_holder.value.configure(text=str(third_party_counter_holder.counter))
                except KeyError:
                    pass
        
        wr.put_coro(state_monitor)  # state_monitor will be killed automatically on a window close

        async def enable_kill_button(i: Interface):
            await i(InstanceRequest().wait(CPUBoundCounters))
            button_holder.value.configure(state='normal')
        
        wr.put_coro(enable_kill_button)  # state_monitor will be killed automatically on a window close


class TextFileViewer(customtkinter.CTkFrame):
    def __init__(self, parent, content: str):
        customtkinter.CTkFrame.__init__(self, parent)
        self.parent = parent
        self.content = content
        self.text = customtkinter.CTkTextbox(self, wrap="none")
        self.text.pack(side="left", fill="both", expand=True)
        self.text.insert("1.0", content)


def customtkinter_file_view_app(i: Interface, text: str, encoding: str, bom_bytes: bytes):
    with(TkinterContextManager(i, customtkinter.CTk())) as wr:
        app = wr.tk
        app.geometry('400x250+400+100')
        button_holder: ValueExistence[customtkinter.CTkButton] = ValueExistence()
        counter_label_holder: ValueExistence[customtkinter.CTkLabel] = ValueExistence()

        @sync_coro
        def on_close(i: Interface):
            button_holder.value.configure(state='disabled')
            button_holder.value.configure(text='Closing for 2 seconds...')
            i(InstanceRequest().set(State, 'Closing customtkinter_file_view_app for 2 seconds...'))
            i(TimerCoroRunner, 2, lambda i: app.destroy())  # destroy this window after 2 seconds
        
        app.protocol("WM_DELETE_WINDOW", on_close)
        button_holder.value = customtkinter.CTkButton(master=app, text="Close and exit", command=on_close)
        button_holder.value.pack()
        counter_label_holder.value = customtkinter.CTkLabel(app, text=f'{encoding=}, {bom_bytes=}')
        counter_label_holder.value.pack()
        viewer = TextFileViewer(app, text)
        viewer.pack(side="top", fill="both", expand=True)
        i(InstanceRequest().set(State, 'customtkinter_file_view_app started.'))

        prepare_mainloop(app)  # required by customtkinter in order to prepare things
    
    i(AsyncEventBusRequest().send_event(DoneEventID, None))


async def status_printer():
    try:
        print(f'{datetime.now()}: Waiting for a State...')
        await await_task_prim(InstanceRequest().wait(State))
        state = None
        while True:
            await asyncio.sleep(1/60)
            new_state = await await_task_prim(InstanceRequest().get(State))
            if new_state != state:
                state = new_state
                print(f'{datetime.now()}: State: [{state}]')
    except:
        pass

async def main(i: Interface):
    await i(ShutdownOnKeyboardInterrupt)
    await i(AsyncioLoopRequest().ensure_loop(interrupt_when_no_requests=False))
    await i(AsyncioLoopRequest().turn_on_loops_intercommunication())

    asyncio.create_task(status_printer())  # starting an asyncio coroutine in background. It waits for a State
    await i(InstanceRequest().set(State, 'Starting up...'))

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    await i(InstanceRequest().set(State, 'Starting tkinter_counter_view_app for 2 seconds...'))
    await i(PutCoro, tkinter_counter_view_app)  # starting cs_coroutine in background
    await asyncio.sleep(2)  # waiting for an asyncio coroutine
    await i(InstanceRequest().set(State, 'Starting counting for 2 seconds...'))
    counter_holder: DataHolder = DataHolder(-500000)
    third_party_counter_holder: DataHolder = DataHolder(-999999)
    counter_coro_id: CoroID = await i(PutCoro, cpu_bound_computations, 999999999, counter_holder)  # starting CPU-heavy cs_coroutine with a patched bytecode in background
    third_party_counter_coro_id: CoroID = await i(PutCoro, cs_coro(third_party_cpu_bound_computations), 999999999, third_party_counter_holder)  # starting third-party CPU-heavy cs_coroutine with a patched bytecode in background
    await asyncio.sleep(2)  # waiting for an asyncio coroutine
    await i(InstanceRequest().set(State, 'Register counters and wait for 2 seconds...'))
    await i(InstanceRequest().set(CPUBoundCounters, {
        'own_counter': (counter_coro_id, counter_holder),
        'third_party_counter': (third_party_counter_coro_id, third_party_counter_holder),
    }))
    await asyncio.sleep(2)  # waiting for an asyncio coroutine
    await i(InstanceRequest().set(State, 'Repeatedly reading from file for 2 seconds...'))
    text, encoding, bom_bytes = await asyncio_io_bound_coroutine(__file__, 2.0)  # waiting for an asyncio coroutine which will repeatedly read from file for 2 seconds
    await i(InstanceRequest().set(State, 'Sleaping for 2 seconds...'))
    await asyncio.sleep(2)  # waiting for an asyncio coroutine
    await i(InstanceRequest().set(State, 'Starting customtkinter_file_view_app...'))
    await i(PutCoro, customtkinter_file_view_app, text, encoding, bom_bytes)  # starting cs_coroutine in background
    await i(AsyncEventBusRequest().wait(DoneEventID))  # waitin for a shutdown event from the CustomtkinterFileView's window
    await i(InstanceRequest().set(State, 'Shutting down for 2 seconds...'))
    await asyncio.sleep(2)  # waiting for an asyncio coroutine
    await i(ShutdownLoop)  # force loop shutdown in order to not wait for other running background coroutines to be completed


if '__main__' == __name__:
    run_in_loop(main)
