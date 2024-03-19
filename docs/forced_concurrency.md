
## Tutorial step by step

We will merge following components into a **single** thread:
* own **blocking** CPU-bound function
* Tkinter application
* CustomTkinter application
* asyncio-based file reading task.

Steps with imports:

1. CPU-bound function and counter. Bytecode of this function is adjusted by `gly_patched` decorator. Now it is an unblocking coroutine.

```python
from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly_patched


class DataHolder:
    def __init__(self, counter: int):
        self.counter: int = counter


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
```

2. Asyncio-based file reading function

```python
import aiofiles

from cengal.text_processing.encoding_detection import detect_and_decode
from cengal.time_management.repeat_for_a_time import Tracer, TracerIterator
from cengal.math.numbers import RationalNumber


async def asyncio_io_bound_coroutine(file_name: str, reading_time: RationalNumber):
    for i in TracerIterator(Tracer(reading_time)):  # will repeat reading for N seconds
        async with aiofiles.open(file_name, mode='rb') as f:
            text, encoding, bom_bytes = detect_and_decode(await f.read())
    
    return text, encoding, bom_bytes
```

3. Tkinter app for displaying counter

```python
import tkinter

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.tkinter import TkinterContextManager
from cengal.code_flow_control.smart_values import ValueExistence


def tkinter_counter_view(i: Interface, counter_holder: DataHolder):
    with(TkinterContextManager(i, tkinter.Tk())) as wr:
        app: tkinter.Tk = wr.tk
        app.geometry('300x100+100+100')
        label_holder: ValueExistence[tkinter.Label] = ValueExistence()
        label_holder.value = tkinter.Label(app)
        label_holder.value.pack()
        
        async def state_monitor(i: Interface, counter_holder: DataHolder):
            while await i(Sleep, 1/60):
                if counter_holder:
                    label_holder.value.configure(text=str(counter_holder.counter))
        
        wr.put_coro(state_monitor, counter_holder)  # state_monitor will be killed automatically on a window close
```

4. Customtkinter app for displaying text

```python
import customtkinter

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.tkinter import TkinterContextManager
from cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus import AsyncEventBusRequest
from cengal.parallel_execution.coroutines.integrations.customtkinter import prepare_mainloop
from cengal.code_flow_control.smart_values import ValueExistence


class TextFileViewer(customtkinter.CTkFrame):
    def __init__(self, parent, content: str):
        customtkinter.CTkFrame.__init__(self, parent)
        self.parent = parent
        self.content = content
        self.text = customtkinter.CTkTextbox(self, wrap="none")
        self.text.pack(side="left", fill="both", expand=True)
        self.text.insert("1.0", content)


def customtkinter_file_view(i: Interface, text: str, encoding: str, bom_bytes: bytes):
    with(TkinterContextManager(i, customtkinter.CTk())) as wr:
        app = wr.tk
        app.geometry('400x250+400+100')
        label_holder: ValueExistence[customtkinter.CTkLabel] = ValueExistence()
        label_holder.value = customtkinter.CTkLabel(app, text=f'{encoding=}, {bom_bytes=}')
        label_holder.value.pack()
        viewer = TextFileViewer(app, text)
        viewer.pack(side="top", fill="both", expand=True)

        prepare_mainloop(app)  # required by customtkinter in order to prepare things
    
    i(AsyncEventBusRequest().send_event('DoneEvent', None))
```

5. Main function which will combine all above parts

```python
import asyncio
import customtkinter

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import AsyncioLoopRequest
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_on_keyboard_interrupt import ShutdownOnKeyboardInterrupt
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_loop import ShutdownLoop
from cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus import AsyncEventBusRequest


async def main(i: Interface):
    await i(ShutdownOnKeyboardInterrupt)  # force loop shutdown on keyboard interrupt
    await i(AsyncioLoopRequest().ensure_loop(interrupt_when_no_requests=True))  # ensure that asyncio loop is running
    await i(AsyncioLoopRequest().turn_on_loops_intercommunication())  # turn on loops intercommunication
    customtkinter.set_appearance_mode("dark")  # set appearance mode for all Customtkinter apps
    customtkinter.set_default_color_theme("blue")  # set default color theme for all Customtkinter apps

    counter_holder: DataHolder = DataHolder(-500000)  # counter. Counting will starts from -500000
    await i(PutCoro, cpu_bound_computations, 999999999, counter_holder)  # starting CPU-heavy cs_coroutine with a patched bytecode in background
    await i(PutCoro, tkinter_counter_view, counter_holder)  # starting cs_coroutine in background
    text, encoding, bom_bytes = await asyncio_io_bound_coroutine(__file__, 2.0)  # waiting for an asyncio coroutine which will repeatedly read from file for 2 seconds
    await asyncio.sleep(2)  # waiting for an asyncio coroutine
    await i(PutCoro, customtkinter_file_view, text, encoding, bom_bytes)  # starting cs_coroutine in background
    await i(AsyncEventBusRequest().wait('DoneEvent'))  # waitin for a shutdown event from the CustomtkinterFileView's window
    await i(ShutdownLoop)  # force loop shutdown in order to not wait for other running background coroutines to be completed


if '__main__' == __name__:
    run_in_loop(main)
```

## Source code

* [simple_example.py](https://github.com/FI-Mihej/Cengal/blob/master/examples/simple_example.py)
