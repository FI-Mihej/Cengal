# Cengal

## About

**Cengal** is a Python library that consists of various Python helping modules for everyday use. 

Asynchronous loop with almost preemptive multitasking within the single thread. Async Tkinter. Python bytecode manipulation. Introspection. Code parsing. Etc.

It is made for [CPython 2/3 and PyPy 2/3; Linux, Win32 and OS X]

## Installation

`pip install git+https://github.com/FI-Mihej/Cengal.git`

or

`pip install cengal`

## Lets combine in single (!) thread: 2 CPU-bound functions, Tkinter app, Customtkinter app and asyncio-based file reading task

### Source code
* [rich_example.py](https://github.com/FI-Mihej/Cengal/blob/master/examples/rich_example.py)
* [third_party_cpu_bound.py](https://github.com/FI-Mihej/Cengal/blob/master/examples/third_party_cpu_bound.py)

### Video showcase

<a href="https://www.youtube.com/watch?feature=player_embedded&v=rc7PBF0cDjw" target="_blank">
 <img src="https://img.youtube.com/vi/rc7PBF0cDjw/mqdefault.jpg" alt="Watch the video" width="640" height="360" border="5" />
</a>

## Simpler example step by step

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

### Source code

* [simple_example.py](https://github.com/FI-Mihej/Cengal/blob/master/examples/simple_example.py)

## Most unique modules

* **"parallel_execution"**
    * **"coroutines"** - asynchronous loop with almost preemptive multitasking within the single thread. Brings an async approach to an unmodified Tkinter, Qt, Kivy, etc. Unlike asyncio/trio/curio, it uses microkernel (services-based) approach which makes it highly- and easily-expandable. Can be executed both independently (asyncio/uvloop loop will be injected within the Cengal-coroutine when needed) and within already executed asyncio/uvloop loop. Can be used from the PyScript for the Web app creation.
        * **"coro_standard_services"** - set of standard services. You can replace standard service by yours for your app or for third-party module without code changes: by registering your own alias.
            * **"loop_yield"** - automatically kinda yield from your loops from time to time (priority based). Can be used to make a proper coroutine (which will not hangs on its endless loops) even from the long-running CPU-hungry third-party function (by function's bytecode modification made in runtime).
            * **"tkinter"** - make your Tkninter app async easily. Run any number of asynchronous Tkinter apps in single thread.
            * **"db"** - async wrapper around LMDB which provides an appropriate async API
            * **"asyncio_loop"** - use asyncio-based code directly from your async Cengal-coroutine neither [Trio](https://github.com/python-trio/trio) nor [Curio](https://github.com/dabeaz/curio) able to to do this
            * **"wait_coro"** - 'put_atomic' request is an analogue of [Trio's Nurseries](https://trio.readthedocs.io/en/stable/tutorial.html) for list of one or more coroutines; 'put_fastest' - returns when at least N of coroutines from the list were done successfully; etc.
            * **"read_write_locker"** - sync primitive usefull for DB creation (was made for a TagDB)
            * **"remote_nodes"** - in progress - connect to any opened listener/port of the node (TCP/UDP/Unix_Socket - doesn't matter), and identify your receiver by name (defined once - during the connection creation process). Uses improved version of the asyncio.streams as a backend in order to have a back pressure and an improved performance (see "efficient_streams" module description below).
        * **"coro_tools"** - tools
            * **"await_coro"** - await Cengal-coroutine or await for a call to the Cengal-service from your asyncio code
            * **"low_latency"** - use standard json module from your coroutines without hangs on huge Json-data (which usually hung even fast json implementation like orjson)
        * **"integrations"** - 
            * **"customtkinter"** - wrapper around an unmodified [customtkinter](https://github.com/TomSchimansky/CustomTkinter). Implements an additional call, Customtkinter async apps needs to be executed for a proper work
            * **"nicegui"** - wrapper around an unmodified [NiceGUI](https://github.com/zauberzeug/nicegui). Execute nicegui instance from within your code (administrative page for example). Build your pages in an asynchronous way in order to improve your server latency (NiceGUI makes it in a sync way).
            * **"uvicorn"** - wrapper around an unmodified [uvicorn](https://github.com/encode/uvicorn). Run uvicorn as a usual asyncio coroutine.
            * **"uvloop"** - an easy-install for a [uvloop](https://github.com/MagicStack/uvloop) (if awailable).
    * **"asyncio"** - tools for an asyncio
        * **"efficient_streams"** - more efficient remake of an [asyncion.streams](https://docs.python.org/3/library/asyncio-stream.html). Better awailable traffic limits utilisation. Less kerner-calls number. Back pressure. Unlike asyncio, UDP version is planned but is not ready yet.
* **"code_flow_control"** - 
    * **"python_bytecode_manipulator"** - modify your or third-party Python function's code in runtime easily
    * **"chained_flow"** - easy to use monad. Execute your your code if all/none/some of steps were completed withot an exceptions. Use all/none/some resutls of your steps at the final part of monad execution.
    * **"multiinterface_essence"** - Make your model and add different interfaces to it easily. Can be used for example in games: create "chair", "ball", "person" models and add to them your library of general interfaces like "touch", "push", "sit", "shot", "burn", "wet", etc.

# Some of most interesting modules
* **"parallel_execution"**
    * **"coroutines"** - 
        * **"coro_tools"** - tools
            * **"wait_coro"** - decorate your coroutine in order to be able to execute it from the plain sunc code as a sync function
            * **"run_in_loop"** - serves the same purpose as an asyncio.run() call
            * **"prepare_loop"** - creates and returns loop. You may use it later
    * **"asyncio"** - tools for an asyncio
        * **"run_loop"** - similar to asyncio.run() but ends only when all background tasks will be finished (main coro can be finished long before this moment).
        * **"timed_yield"** - simple (dum-dum but faster) version of the "loop_yield" (see above) but made directly for an asyncio.
* **"bulk_pip_actions"** - install lists of required modules. Lists can be different for a different operating systems
* **"code_inspection"** - 
    * **"auto_line_tracer"** - smart and easy to use line logger (current func name, file, lines numbers, surrounding code)
    * **"line_tracer"** -  - easy to use line logger (current func name, file, line number)
    * **"line_profiling"** - confinient work with a [line_profiler](https://github.com/pyutils/line_profiler) if awailable
* **"data_containers"** - usefull data containers like stack, fast fifo, etc. Some of them are highly optimized for speed
* **"data_manipulation"** - 
    * **"conversion"** - 
        * **"bit_cast_like"** - similar to std::bit_cast from C++
        * **"reinterpret_cast"** - similar to reinterpret_cast from C++. You have a third-party object and you want to change it's type (and behavior) in runtime.
    * **"serialization"** - automatically choose a fastest appropriate serializer for your type and structure of data (json, simplejson, ujson, ojson, msgpack, cbor, cbor2, marshal, pickle, cloudpickle, ...)
    * **"tree_traversal"** - both recrsive and nonrecursive tree traversal algorithms
* **"ctypes_tools"** - ctypes code and structures used by Cengal.
    * **"tools"** - ctypes tools usefull for your code
* **"file_system"** - normalized relative path, etc.
    * **"app_fs_structure"** - unified list of the default app directories (data, cache, temp, etc.) recommended by OS (Linux, Windows, Mac OS X) in a runtime for a given application name or a service name. Results are cached. Cache size can be modified in runtime.
* **"hardware_info"** - 
    * **"cpu"** - normalized results from cpuinfo extended with an info from psutil.
* **"introspection"** - 
    * **"inspect"** - find out function parameters, entity owners list (method -> subclass -> class -> module), entitie's own properties (excluding parent's properties), etc.
    * **"third_party"** - 
        * **"ctypes"** - provice an instance of ctypes Structure and take a dict with all internals of this structure. Good for inspecting/logging/printing values of a given structure with all values of all its substructures.
* **"io"** - 
    * **"used_ports"** - database of known TCP/UDP ports. Updates from an appropriate Wikipedia page once per Cengal release but you can update if for your self anytime if you want to.
    * **"serve_free_ports"** - provide ports range with an interested port types set and receive number of the first open appropriate port on your machine within given port range.
    * **"named_connections_manager"** - base for the "remote_nodes" (see above) and similar entities
    * **"net_io"** - an experimental networking library with an expandable architecture. Has implemented modules for epoll and select.
* **"math"** - 
    * **"algebra"** - 
        * **"fast_algorithms"** - Fast inverse square root (the one from Quake III) implemented efficiently
    * **"geometry"** - 
        * **"ellipse"** - ellipse related. Also several algorithms for precisely or efficiently compute an ellipse perimeter
        * **"point"** - numpy (if awailable) or python implementation of points (1D, 2D, 3D, nD)
        * **"vector"** - numpy (if awailable) or python algotithms on vectors (1D, 2D, 3D, nD). Implements CoordinateVectorNd, VectorNd, DirectedGraphNd
* **"modules_management"** - reload module, import drop-in-replacement module if an original is not awailable
* **"statistics"** - 
    * **"normal_distribution"** - compute the normal distribution of your data. Booth count or use a formula. 99, 95, 68; standard_deviation: diff_mean, sqrt(variance), max_deviation, min_deviation.
* **"text_processing"** - text parsing, patching, detect BOM and encoding
* **"time_management"** - 
    * **"timer"** - timer for any synchronous code
    * **"sleep_tools"** - sleep for a production code. Using usual sleep you may get not wat you want if you are not really into your target OS internals (Windows/Linux)
    * **"repeat_for_a_time"** - measures code/function executions per second. But it _smart and eficiently_ repeats target code/function not N times but up to a T seconds. Results to a high precision measurements for even smallest and fastest pieces of code.
    * **"relative_time"** - time related module for a business purposes (calendars, payments, etc.)
* **"unittest"** - 
    * **"patcher"** - set of context manager for monkey patching builtins or other entities
* **"user_interface"** - 
    * **"gui"** - 
        * **"nt"** - 
            * **"blur_behind"** - Turn on Aero Glass backgrownd in Winndows 7, 10, 11 using documented or undocumented API (which one is awailable)
            * **"dpi_awareness"** - Turn on DPI awareness
* **"web_tools"** - 
    * **"detect_browsers_host_device_type"** - 
        * **"by_http_user_agent"** - detects is it mobile or tablet device by analizing its http user_agent string

## Size of the Cengal library

How much of your time you can save if you'll use Cengal?

That much (at the moment of 27 Oct 2022):

161 modules

```

-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                         397          10291          12906          35398
Cython                           5            423            284           1411
-------------------------------------------------------------------------------
SUM:                           402          10714          13190          36809
-------------------------------------------------------------------------------

```

Counted with [cloc](https://github.com/AlDanial/cloc) util.

It's at very least is 260 man-days of work or at very least is a 1 man-year of of work (8 hours per day, 5 days per week, without vacations/holidays/seakleaves). I've used widly known industry standard for this measurement: +142 lines of code to the codebase per day by the year of measurements.

## Examples

* Can be found in [examples](https://github.com/FI-Mihej/Cengal/blob/master/examples/) dir
* Each module has a `development` folder. Examples are usually placed there
* Some of old examples can be fined inside the [tests](https://github.com/FI-Mihej/Cengal/blob/master/tests/) dir.

### Cengal.coroutines examples

* [General idea, greenlet main Cengal.coro](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_tools/run_in_loop/versions/v_0/development/main.py)
* [General idea, async main Cengal.coro](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_tools/run_in_loop/versions/v_0/development/amain.py)
* [Transparent interconnection between Cengal.coroutines and asyncio](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_tools/run_in_loop/versions/v_0/development/asyncio_interconnection.py)

### Text processing example

[Ensures and updates copyright (with dates) in each Cengal's source file](https://github.com/FI-Mihej/Cengal/blob/master/scripts/ensure_copyright/ensure_copyright.py)

## Projects using Cengal

* [flet_async](https://github.com/FI-Mihej/flet_async) - wrapper which makes [Flet](https://github.com/flet-dev/flet) async and brings booth Cengal.coroutines and asyncio to Flet (Flutter based UI)
* [justpy_containers](https://github.com/FI-Mihej/justpy_containers) - wrapper around [JustPy](https://github.com/justpy-org/justpy) in order to bring more security and more production-needed features to JustPy (VueJS based UI)
* [Bensbach](https://github.com/FI-Mihej/Bensbach) - decompiler from Unreal Engine 3 bytecode to a Lisp-like script and compiler back to Unreal Engine 3 bytecode. Made for a game modding purposes
* [Realistic-Damage-Model-mod-for-Long-War](https://github.com/FI-Mihej/Realistic-Damage-Model-mod-for-Long-War) - Mod for both the original XCOM:EW and the mod Long War. Was made with a Bensbach, which was made with Cengal
* [SmartCATaloguer.com](http://www.smartcataloguer.com/index.html) - TagDB based catalog of images (tags), music albums (genre tags) and apps (categories)

## License

Copyright © 2012-2023 ButenkoMS. All rights reserved.

Licensed under the Apache License, Version 2.0.
