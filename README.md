# Cengal compatibility and requirements

* Target platforms: Win32, Linux, OS X, Android, iOS, Emscripten
* Target architectures: x64, x86, ARM
* Target interpreters: CPython, PyPy
* Recommended Python versions: 3.8+

# Installation

`pip install cengal` will install prebuilt wheels for both Windows and Linux

# Documentation

[Cengal Wiki](https://github.com/FI-Mihej/Cengal/wiki)

For example [Cengal Coroutines Concepts & Usage](https://github.com/FI-Mihej/Cengal/wiki/Cengal-Coroutines)

# Exclusive Features: No Alternatives Online

## Run concurently following components in a Single (!) Thread

* own **blocking** CPU-bound function
* third-party **blocking** CPU-bound function
* Tkinter application
* CustomTkinter application
* asyncio-based file reading task.

### Examples

#### YouTube Showcase

<a href="https://www.youtube.com/watch?feature=player_embedded&v=rc7PBF0cDjw" target="_blank">
 <img src="https://github.com/FI-Mihej/Cengal/raw/master/docs/assets/2023-04-24 01-37-34-360p-YouTube.png" alt="Watch the video" width="640" height="360" border="5" />
</a>

#### Source code

* [rich_example.py](https://github.com/FI-Mihej/Cengal/blob/master/examples/rich_example.py)
* [third_party_cpu_bound.py](https://github.com/FI-Mihej/Cengal/blob/master/examples/third_party_cpu_bound.py)

#### Tutorial

* [Decorator which converts blocking code to concurrent code](https://github.com/FI-Mihej/Cengal/wiki/Decorator-which-converts-blocking-code-to-concurrent-code)


## True Interprocess Shared Memory (Proof of Concept Stage)

Share your data between your Python processes (2 processes currently) and work with them as usual. Work across different processes is made turn by turn (fast operation: using full memory barrier instead of system calls)

Supported types (currently):

* `list` - Unlike `multiprocessing.shared_memory.ShareableList`: **mutable** and **resizable** between different processes, supports other containers (lists, tuples, dicts) as an items and implements all `list` methods. Faster than `multiprocessing.shared_memory.ShareableList`.
* `dict` - *currently immutable*
* `tuple`
* `str`
* `bytes`
* `bytearray`
* `bool`
* `float` - Unlike values in `multiprocessing.shared_memory.ShareableList`, supports Addition Assignment (`shared_list[20] += 999.3`) and all other native methods and operators
* `int` - int64, currently. Unlike values in `multiprocessing.shared_memory.ShareableList`, supports Addition Assignment (`shared_list[15] += 999`) and all other native methods and operators
* `None`

### Examples

[shared_memory_example.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/hardware/memory/shared_memory/versions/v_0/development/shared_memory_example.py)

and smaller:

```python
from multiprocessing import Process
from cengal.hardware.memory.shared_memory import *


shared_memory_name = 'test_shared_mem'
shared_memory_size = 200 * 1024 * 1024
switches = 1000
changes_per_switch = 2000


def work(manager, shared_data)
    index = 0
    while index < switches:
        with wait_my_turn(manager):
            # emulatin our working process
            for i in range(changes_per_switch):
                shared_data[1] += 1

def second_process():
    consumer: SharedMemory = SharedMemory('test_shmem', False)
    consumer.wait_for_messages()
    with wait_my_turn(consumer):
        shared_data = consumer.take_message()
    
    work(consumer, shared_data)


creator: SharedMemory = SharedMemory(shared_memory_name, True, shared_memory_size)
p = Process(target=second_process)
p.start()
creator.wait_consumer_ready()
with wait_my_turn(creator):
    data = [
        'hello',
        0,
        (8, 2.0, False),
        {
            b'world': -6,
            5: 4
        }
    ]
    shared_data = creator.put_message(data)

work(creator, shared_data)
p.join()
```

### Performance Benchmark results

Shared `list` container (which is not yet fully optimizes currently) is already faster than `multiprocessing.shared_memory.ShareableList`.
And unlike `multiprocessing.shared_memory.ShareableList` supports Addition Assignment (`shared_list[15] += 999`) and all other native methods and operators of items.
It provides an ability to make more than 30000000 reads/writes per second of an int64 value (`shared_list[2] = 1234` / `val = shared_list[7]`) or more than 1450000 addition assignments per second (`shared_list[15] += 999`).

[Benchmark Results](https://github.com/FI-Mihej/Cengal/blob/master/cengal/hardware/memory/shared_memory/versions/v_0/development/benchmark_results.md)


### Roadmap

* Continuosly moving more logic to Cython
* Implement mutable `dict` and `set` using an appropricate C hashmap library or C++ code (depending what will be faster in our case)
* Increase number of interacting processes from 2 to variable value
* Implement garbage collector for shared data in addition to manual `free()` call
* Implement an appropriate Service for `cengal.parallel_execution.coroutines` - for comfortable shared memory usage inside an async code (including `asyncio`) 
* Improve memory allocation algorithm in an attempt of making it faster

## Async LMDB database API

An example of usage (unit test of the module):
* [test__db.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_standard_services/db/versions/v_1/tests/test__db.py)

## Async logging into LMDB database

Developer can observe their logs in runtime using `cengal.parallel_execution.coroutines.coro_tools.loop_administration.admin_tk` module (made with Async Tkinter GUI):
* [admin_tk.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_tools/loop_administration/admin_tk/versions/v_0/admin_tk.py)

An example of usage of the admin_tk:
* [admin_test.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_tools/loop_administration/admin_tk/versions/v_0/development/admin_test.py)

Alternatively, developer can load logs in off-line mode using Log Viewer application (made with async Tkinter GUI):
* [log_viewer.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_tools/log_viewer/versions/v_0/log_viewer.py)

## Async Tkinter and Customtkinter

* [tkinter_0.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_standard_services/tkinter/versions/v_0/development/tkinter_0.py)
* [customtkinter_0.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_standard_services/tkinter/versions/v_0/development/customtkinter_0.py)

## Async wxPython

* [async_wxpython_example.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/integrations/wxpython/versions/v_0/development/async_wxpython_example.py)

## Async QT (PySide, PySide2, PySide6, PyQt4, PyQt5, PyQt6)

* [pyside6__coro_slot_example_0.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/integrations/qt/pyside6/versions/v_0/development/pyside6__coro_slot_example_0.py)

## Async PyTermGUI

* [hello_world_app_autoexit.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/integrations/pytermgui/versions/v_0/development/hello_world_app_autoexit.py)
* [hello_world.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/integrations/pytermgui/versions/v_0/development/hello_world.py)

## Transparent background for your desktop applications (TBA)

* Target OS: Windows 11, Windows 10, Windows 8, Windows 7, Windows Vista.
* Target frameworks: PySide, PyQt, Kivy, PyWebView 

![title](https://github.com/FI-Mihej/Cengal/raw/master/docs/assets/Cengal_PyWebView_Transparent_UI_Windows_10.png)
,
![title](https://github.com/FI-Mihej/Cengal/raw/master/docs/assets/Cengal_Kivy_Transparent_UI_Windows_10.png)

## Tkinter True Borderless apps for Windows platform (TBA)

* Target OS: Windows 11, Windows 10, Windows 8, Windows 7, Windows Vista.
* Target frameworks: CustomTkinter, Tkinter, ttkbootstrap, ...

![title](https://github.com/FI-Mihej/Cengal/raw/master/docs/assets/Cengal_Tkinter_True_Borderless_Draggable_Applications_Windows_10.png)

## Cengal Coroutines and Asyncio Administration and Monitoring Page

Observe loop performance, services state and coroutines list with details. Use an async interactive console in order to interact with your application from inside.

### YouTube Showcase

<a href="https://www.youtube.com/watch?feature=player_embedded&v=qiuOH9B6uCY" target="_blank">
 <img src="https://github.com/FI-Mihej/Cengal/raw/master/docs/assets/CoroSchedulerAdminYoutube.png" alt="Watch the video" width="640" height="360" border="5" />
</a>

### Examples

[admin_test.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_tools/loop_administration/admin_tk/versions/v_0/development/admin_test.py)


# Modules with unique functionality

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
            * **"Qt"** - wrapper around an unmodified Qt (supports: PySide, PySide2, PySide6, PyQt4, PyQt5, PyQt6). Adds asynchronous behavior to Slots. Doesn't require total reimplementation of your Qt app unlike other suggestions and competitors.
            * **"customtkinter"** - wrapper around an unmodified [customtkinter](https://github.com/TomSchimansky/CustomTkinter). Implements an additional call, Customtkinter async apps needs to be executed for a proper work
            * **"nicegui"** - wrapper around an unmodified [NiceGUI](https://github.com/zauberzeug/nicegui). Execute nicegui instance from within your code (administrative page for example). Build your pages in an asynchronous way in order to improve your server latency (NiceGUI makes it in a sync way).
            * **"uvicorn"** - wrapper around an unmodified [uvicorn](https://github.com/encode/uvicorn). Run uvicorn as a usual asyncio coroutine.
            * **"uvloop"** - an easy-install for a [uvloop](https://github.com/MagicStack/uvloop) (if awailable).
            * **"PyTermGUI"** - wrapper around an unmodified PyTermGUI. Adds asynchronous behavior. No competitors currently.
    * **"asyncio"** - tools for an asyncio
        * **"efficient_streams"** - more efficient remake of an [asyncion.streams](https://docs.python.org/3/library/asyncio-stream.html). Better awailable traffic limits utilisation. Less kerner-calls number. Back pressure. Unlike asyncio, UDP version is planned but is not ready yet.
* **"code_flow_control"** - 
    * **"python_bytecode_manipulator"** - modify your or third-party Python function's code in runtime easily
    * **"chained_flow"** - easy to use monad. Execute your your code if all/none/some of steps were completed withot an exceptions. Use all/none/some resutls of your steps at the final part of monad execution.
    * **"multiinterface_essence"** - Make your model and add different interfaces to it easily. Can be used for example in games: create "chair", "ball", "person" models and add to them your library of general interfaces like "touch", "push", "sit", "shot", "burn", "wet", etc.
* **"hardware"** - hardware related
    * **"memory"** - RAM related
        * **"barriers"** - fast full memory barriers for both x86/x64 and ARM (Windows, Linux, OS X, iOS, Android).
* **"time_management"** - 
    * **"high_precision_sync_sleep"** - provides an ability to put your thread into legetimate sleep for at least 10x smaller time period than `time.sleep()` from the Python's Standard Library able to do on same Operating System: uses `nanosleep()` on Linux and periodic `SwitchToThread()` on Windows.
    * **"cpu_clock_cycles"** - Returnes value of `RDTSCP` on x86/x86_64 or `CNTVCT_EL0` on ARM. Fast implementation: 6-12 times faster than all other competitors on Github. Note: CPU Time Stamp Counter (TSC) is not depends on actual current CPU frequency in modern CPUs (starting from around year 2007) so can be safely used as a high precision clock (see `time_management.cpu_clock` module). Windows, Linux and other Operating Systems are using it internaly.
    * **"cpu_clock"** - like `perf_counter()` but 25% faster. Supports both x86/x86_64 and ARM. `cpu_clock` is slightly faster than `cpu_clock_cycles` because `double` (`float` in Python terms) transfered from C-code to Python code more efficiently than `64-bit int` (which needs an addition internal logic inside the Python itself for conversion). Highest-precision possible since it is CPU Time Stamp Counter based which is not depends on actual current CPU frequency in modern CPUs (starting from around year 2007) so can be safely used as a high precision clock (and Windows, Linux and other Operating Systems are using it internaly in this way). **Benchmark**: [cpu_clock_test.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/time_management/cpu_clock/versions/v_0/development/cpu_clock_test.py)

# Some Other modules
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
        * **"reinterpret_cast"** - similar to reinterpret_cast from C++. You have a third-party object and you want to change its type (and behavior) in runtime.
    * **"serialization"** - automatically choose a fastest appropriate serializer for your type and structure of data (json, simplejson, ujson, ojson, msgpack, cbor, cbor2, marshal, pickle, cloudpickle, ...)
    * **"tree_traversal"** - both recrsive and nonrecursive tree traversal algorithms
* **"ctypes_tools"** - ctypes code and structures used by Cengal.
    * **"tools"** - ctypes tools usefull for your code
* **"file_system"** - normalized relative path, etc.
    * **"app_fs_structure"** - unified list of the default app directories (data, cache, temp, etc.) recommended by OS (Linux, Windows, Mac OS X) in a runtime for a given application name or a service name. Results are cached. Cache size can be modified in runtime.
* **"hardware"** - hardware related
    * **"info"** - hardware info
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

At the moment of 11 Oct 2023:

More than 190 modules

```
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                         636          18572          21458          59787
Cython                           9            686            415           1817
C                                2             39             26            163
C/C++ Header                     2             14             26             37
-------------------------------------------------------------------------------
SUM:                           649          19311          21925          61804
-------------------------------------------------------------------------------
```

Counted with [cloc](https://github.com/AlDanial/cloc) util.

## Examples

* Can be found in [examples](https://github.com/FI-Mihej/Cengal/blob/master/examples/) dir
* Each module has a `development` folder. Examples are usually placed there
* Some of old examples can be fined inside the [tests](https://github.com/FI-Mihej/Cengal/blob/master/tests/) dir.

### Cengal.coroutines examples

* [General idea, greenlet main Cengal.coro](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_tools/run_in_loop/versions/v_0/development/main.py)
* [General idea, async main Cengal.coro](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_tools/run_in_loop/versions/v_0/development/amain.py)
* [Transparent interconnection between Cengal.coroutines and asyncio](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_tools/run_in_loop/versions/v_0/development/asyncio_interconnection.py)

### Text processing example

[Ensures and updates copyright (with dates) in each Cengal's source file](https://github.com/FI-Mihej/Cengal/blob/master/cengal_setup_scripts/ensure_copyright/ensure_copyright.py)

# Build

`pip install cengal` on Mac OS X

or

`pip install git+https://github.com/FI-Mihej/Cengal.git` on any system

Installation process requires compilation (prebuild Wheels are not prepared yet). So ensure that:
* GCC/Clang is installed in your Linux/WSL (`sudo apt-get --yes install build-essential` for Ubuntu. And `./before_install_on_wsl.sh` for Ubuntu under WSL for UI like Tkinter or Qt if you are using some kind of XServer on your host Windows)
* At least `Visual Studio Community - Build Tools` are installed on your Windows and you are installing Cengal from within its `Developer Command Prompt` for an appropriate target CPU architecture (`x64 Native Tools Command Prompt for VS 2022` for example). Make sure that you have compatible version of Visual Studio for your target CPython interpreter (see `python -VV` command output. For example `Python 3.9.11 (tags/v3.9.11:2de452f, Mar 16 2022, 14:33:45) [MSC v.1929 64 bit (AMD64)]`: this python interpreter requires Visual Studio 2019 version 16.11.2+ according to `1929` word search in [Wikipedia page](https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B))

# Projects using Cengal

* [flet_async](https://github.com/FI-Mihej/flet_async) - wrapper which makes [Flet](https://github.com/flet-dev/flet) async and brings booth Cengal.coroutines and asyncio to Flet (Flutter based UI)
* [justpy_containers](https://github.com/FI-Mihej/justpy_containers) - wrapper around [JustPy](https://github.com/justpy-org/justpy) in order to bring more security and more production-needed features to JustPy (VueJS based UI)
* [Bensbach](https://github.com/FI-Mihej/Bensbach) - decompiler from Unreal Engine 3 bytecode to a Lisp-like script and compiler back to Unreal Engine 3 bytecode. Made for a game modding purposes
* [Realistic-Damage-Model-mod-for-Long-War](https://github.com/FI-Mihej/Realistic-Damage-Model-mod-for-Long-War) - Mod for both the original XCOM:EW and the mod Long War. Was made with a Bensbach, which was made with Cengal
* [SmartCATaloguer.com](http://www.smartcataloguer.com/index.html) - TagDB based catalog of images (tags), music albums (genre tags) and apps (categories)

# License

Copyright © 2012-2024 ButenkoMS. All rights reserved.

Licensed under the Apache License, Version 2.0.
