![PyPI - Downloads](https://img.shields.io/pypi/dm/cengal-light?color=darkgreen)

![GitHub tag (with filter)](https://img.shields.io/github/v/tag/FI-Mihej/Cengal) ![Static Badge](https://img.shields.io/badge/OS-Linux_%7C_Windows_%7C_macOS-blue) ![Static Badge](https://img.shields.io/badge/coverage-41%25-blue) ![Static Badge](https://img.shields.io/badge/covered_lines_of_code-15855-blue)

![PyPI - Version](https://img.shields.io/pypi/v/cengal-light) ![PyPI - Format](https://img.shields.io/pypi/format/cengal-light?color=darkgreen) ![Static Badge](https://img.shields.io/badge/wheels-Linux_%7C_Windows_%7C_macOS-blue) ![Static Badge](https://img.shields.io/badge/Architecture-x86__64_%7C_ARM__64-blue) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cengal-light) ![Static Badge](https://img.shields.io/badge/PyPy-3.8_%7C_3.9_%7C_3.10-blue) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/cengal-light) 

![GitHub License](https://img.shields.io/github/license/FI-Mihej/Cengal?color=darkgreen) ![PyPI - Status](https://img.shields.io/pypi/status/cengal) 

# Cengal

![CengalLogo](https://github.com/FI-Mihej/Cengal/raw/master/docs/assets/CengalLogoRound128.png)
<!-- ![CengalLogo](./docs/assets/CengalLogoRound128.png)  -->

Cengal is a versatile Python library designed for a wide range of applications. To enhance performance, certain modules within Cengal have been implemented using Cython, C/C++, Nim or Go.

Cengal features an extensive codebase with over 200 projects and more than 80,000 lines of code. I am continually focused on developing new features and making improvements. Contributions are very welcome, especially Pull Requests that include unit tests and documentation enhancements.

If you have any questions or would like to participate in discussions, feel free to join the [Cengal Discord](https://discord.gg/TAy7xNgR). Your support and involvement are greatly appreciated as Cengal evolves.

## Architecture & API Design Rationale

<details>
<summary title="Rationale"><kbd> Rationale </kbd></summary>

The Cengal library adheres to an API design approach used in frameworks such as Qt. For those familiar with the C++ language, I will draw comparisons between the approaches of Qt and the C++ Standard Template Library (STL). The API provided by the STL was designed to significantly reduce the burden on programmers who develop the STL. This decision was logical from the standpoint of marketing the STL among compiler creators. However, this led to the usability of the STL for the user not being great. This is evident in the fact that the STL provides the most minimal possible API, and any conveniences must be programmed anew by each programmer every time - constantly reinventing the wheel. In contrast, Qt uses the opposite approach to API construction: classes have many methods whose purposes are similar, but are aimed at different usage models. This simplifies the use of Qt for users, speeds up the writing of the final code, and avoids many errors that we usually make when we write our own 'bicycles' for the same actions each time (not because the we are not smart, but because we are humans and therefore prone to make mistakes from time to time).

</details>

# Cengal compatibility and requirements

<details>
<summary title="Compatibility and requirements"><kbd> Compatibility and requirements </kbd></summary>

* Target platforms: Win32, Linux, macOS, Android, iOS, Emscripten
* Target architectures: x64, x86, ARM
* Target interpreters: CPython, PyPy
* Recommended Python versions: 3.8+

</details>

# Installation

<details>
<summary title="General wheel"><kbd> General wheel </kbd></summary>

To get started with Cengal, you can easily install it along with all the mandatory dependencies by running `pip install cengal`. This command not only installs Cengal and its required dependencies but also takes care of fetching and installing prebuilt wheels tailored for the Cengal library. These wheels are compatible with both Windows and Linux systems and work seamlessly with both CPython and PyPy interpreters.

</details>

<details>
<summary title="Wheel without dependencies"><kbd> Wheel without dependencies </kbd></summary>

If you prefer to install Cengal without its dependencies, you can opt for the 'cengal-light' package, which serves as the backend for the 'cengal' package. Simply run `pip install cengal-light` to get the lightweight version of Cengal.

</details>

# Documentation

[Cengal Discord](https://discord.gg/TAy7xNgR)

[Cengal Documentation](https://FI-Mihej.github.io/Cengal)

For example [Cengal Coroutines Concepts & Usage](https://FI-Mihej.github.io/Cengal/coroutines_concepts/)

<!-- or partially:

[Cengal Wiki](https://github.com/FI-Mihej/Cengal/wiki)

For example [Wiki: Cengal Coroutines Concepts & Usage](https://github.com/FI-Mihej/Cengal/wiki/Cengal-Coroutines) -->

# Stand-Alone Packages for Specific Cengal Modules

<details>
<summary title="Rationale"><kbd> Rationale </kbd></summary>

To cater to varying needs and streamline the installation process, I've introduced stand-alone packages for select Cengal modules. These packages are designed to offer users the ability to install specific Cengal functionality without the burden of the library's full set of dependencies.

The core of this approach lies in our 'cengal-light' package, which houses both Python and compiled Cengal modules. The 'cengal' package itself serves as a lightweight shell, devoid of its own modules, but dependent on 'cengal-light[full]' for a complete Cengal library installation with all required dependencies.

For users seeking individual Cengal features or looking to minimize dependencies, our stand-alone packages provide a convenient solution. Each stand-alone package is dedicated to a specific Cengal module and relies on 'cengal-light' as its sole dependency.

</details>

Below, you'll find a list of these stand-alone packages, each corresponding to a distinct Cengal module:

* [CengalPolyBuild](https://github.com/FI-Mihej/CengalPolyBuild): A Comprehensive and Hackable Build System for Multilingual Python Packages: Cython (including automatic conversion from Python to Cython), C/C++, Objective-C, Go, and Nim, with ongoing expansions to include additional languages. (Planned to be released soon) 
* [InterProcessPyObjects](https://github.com/FI-Mihej/InterProcessPyObjects) (package for `cengal.parallel_execution.asyncio.ashared_memory_manager` module): High-performance package delivers blazing-fast inter-process communication through shared memory, enabling Python objects to be shared across processes with exceptional efficiency. 
* [cengal_memory_barriers](https://github.com/FI-Mihej/cengal_memory_barriers) (package for `cengal.hardware.memory.barriers` module): Fast crossplatform memory barriers for Python.
* [cengal_cpu_info](https://github.com/FI-Mihej/cengal_cpu_info) (package for `cengal.hardware.cpu.info` module): Extended, cached CPU info with consistent output format.
* [cengal_app_dir_path_finder](https://github.com/FI-Mihej/cengal_app_dir_path_finder) (package for `cengal.file_system.app_fs_structure.app_dir_path` module): Offering a unified API for easy retrieval of OS-specific application directories, enhancing data management across Windows, Linux, and macOS.

Stay tuned for future additions to our collection of stand-alone packages!

# Exclusive Features: No Alternatives Online


<details>
<summary title="Build system (work in progress)"><kbd> Build system (work in progress) </kbd></summary>

## Build system (work in progress)

Automatic hackable build system for your package which supports Python modules made with different languages: Cython (including Python to Cython automatic compilation), C/C++, ObjectiveC, Go, Nim. Other languages support is in progress.

Compiles your code, gather binary artifacts and puts them into your wheel.

### Examples

* [Compilable Golang module](https://github.com/FI-Mihej/Cengal/blob/master/cengal/_examples/ex_golang)
* [Compilable Nim module](https://github.com/FI-Mihej/Cengal/blob/master/cengal/_examples/ex_nim)
* [Pure Python module auto-compiled with Cython](https://github.com/FI-Mihej/Cengal/blob/master/examples/compiled_python)

</details>

<details>
<summary title="Fast inter-process communication through shared memory"><kbd> Fast inter-process communication through shared memory </kbd></summary>

## Fast inter-process communication through shared memory

blazing-fast inter-process communication through shared memory, enabling Python objects to be shared across processes with exceptional efficiency. By minimizing the need for frequent serialization-deserialization, it enhances overall speed and responsiveness. The package offers a comprehensive suite of functionalities designed to support a diverse array of Python types and facilitate asynchronous IPC, optimizing performance for demanding applications.

![Throughput GiB/s](https://github.com/FI-Mihej/Cengal/raw/master/docs/assets/InterProcessPyObjects/ChartThroughputGiBs.png)

![Dict increments per second](https://github.com/FI-Mihej/Cengal/raw/master/docs/assets/InterProcessPyObjects/ChartDictPerformanceComparison.png)

```python
from cengal.hardware.memory.shared_memory import *
from cengal.parallel_execution.asyncio.ashared_memory_manager import *
```

### Key Features

* Shared Memory Communication:
    * Enables sharing of Python objects directly between processes using shared memory.
    * Utilizes a linked list of global messages to inform connected processes about new shared objects.

* Lock-Free Synchronization:
    * Uses memory barriers for efficient communication, avoiding slow syscalls.
    * Ensures each process can access and modify shared memory without contention.

* Supported Python Types:
    * Handles various Python data structures including:
        * Basic types: `None`, `bool`, 64-bit `int`, large `int` (arbitrary precision integers), `float`, `complex`, `bytes`, `bytearray`, `str`.
        * Standard types: `Decimal`, `slice`, `datetime`, `timedelta`, `timezone`, `date`, `time`
        * Containers: `tuple`, `list`, classes inherited from: `AbstractSet` (`frozenset`), `MutableSet` (`set`), `Mapping` and `MutableMapping` (`dict`).
        * Pickable classes instancess: custom classes including `dataclass`
    * Allows mutable containers (lists, sets, mappings) to save basic types (`None`, `bool`, 64 bit `int`, `float`) internally, optimizing memory use and speed.

* NumPy and Torch Support:
    * Supports numpy arrays by creating shared bytes objects coupled with independent arrays.
    * Supports torch tensors by coupling them with shared numpy arrays.

* Custom Class Support:
    * Projects pickable custom classes instancess (including `dataclasses`) onto shared dictionaries in shared memory.
    * Modifies the class instance to override attribute access methods, managing data fields within the shared dictionary.
    * supports classes with or without `__dict__` attr
    * supports classes with or without `__slots__` attr

* Asyncio Compatibility:
    * Provides a wrapper module for async-await functionality, integrating seamlessly with asyncio.
    * Ensures asynchronous operations work smoothly with the package's lock-free approach.

### Docs

[Readme.md](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/asyncio/ashared_memory_manager/versions/v_0/development/README.md)

### Examples

* An async examples (with asyncio):
    * [shared_objects__example__sender.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/asyncio/ashared_memory_manager/versions/v_0/development/shared_objects__example__sender.py)
    * [shared_objects__example__receiver.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/asyncio/ashared_memory_manager/versions/v_0/development/shared_objects__example__receiver.py)
    * [shared_objects__types.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/asyncio/ashared_memory_manager/versions/v_0/development/shared_objects__types.py)

### Performance Benchmark results

#### Throughput

| Approach                        | sync/async | Throughput GiB/s |
|---------------------------------|------------|------------------|
| InterProcessPyObjects (sync)    | sync       | 3.770            |
| InterProcessPyObjects + uvloop  | async      | 3.222            |
| InterProcessPyObjects + asyncio | async      | 3.079            |
| multiprocessing.shared_memory   | sync       | 2.685            |
| uvloop.UnixDomainSockets        | async      | 0.966            |
| asyncio + cengal.Streams        | async      | 0.942            |
| uvloop.Streams                  | async      | 0.922            |
| asyncio.Streams                 | async      | 0.784            |
| asyncio.UnixDomainSockets       | async      | 0.708            |
| multiprocessing.Queue           | sync       | 0.669            |
| multiprocessing.Pipe            | sync       | 0.469            |

#### Shared Dict Performance

| Approach                                  | increments/s |
|-------------------------------------------|--------------|
| InterProcessPyObjects - IntEnumListStruct | 1189730      |
| InterProcessPyObjects - Dataclass         | 143091       |
| UltraDict                                 | 76214        |
| InterProcessPyObjects - Dict              | 44285        |
| shared_memory_dict                        | 42862        |
| multiprocessing.Manager - dict            | 2751         |

### Todo

- [ ] Connect more than two processes
- [ ] Use third-party fast hashing implementations instead of or in addition to built in `hash()` call
- [ ] Continuous performance improvements

</details>

<details>
<summary title="Concurrent Execution of blocking CPU-Bound and GUI Tasks on a Single Thread"><kbd> Concurrent Execution of blocking CPU-Bound and GUI Tasks on a Single Thread </kbd></summary>

## Concurrent Execution of blocking CPU-Bound and GUI Tasks on a Single Thread

Cengal offers a unique and powerful feature that allows you to execute a diverse set of tasks concurrently on a single thread, effectively managing CPU-bound and GUI-related operations without introducing the complexity of multithreading or multiprocessing. Notably, Cengal can convert `blocking CPU-bound` functions into proper asynchronous coroutines, preventing them from blocking the thread for extended periods.

### Examples

In this example, an application concurrently (at the same time) executes all of the following components within a single thread:
* own **blocking** CPU-bound function
* third-party **blocking** CPU-bound function
* Tkinter application
* CustomTkinter application
* asyncio-based file reading task.

#### YouTube Showcase

<a href="https://www.youtube.com/watch?feature=player_embedded&v=rc7PBF0cDjw" target="_blank">
 <img src="https://github.com/FI-Mihej/Cengal/raw/master/docs/assets/2023-04-24 01-37-34-360p-YouTube.png" alt="Watch the video" width="640" height="360" border="5" />
</a>

#### Source code

* [rich_example.py](https://github.com/FI-Mihej/Cengal/blob/master/examples/rich_example.py)
* [third_party_cpu_bound.py](https://github.com/FI-Mihej/Cengal/blob/master/examples/third_party_cpu_bound.py)

#### Tutorial

* [Decorator which converts blocking code to concurrent code](https://github.com/FI-Mihej/Cengal/wiki/Decorator-which-converts-blocking-code-to-concurrent-code)

</details>

<details>
<summary title="Async LMDB database API"><kbd> Async LMDB database API </kbd></summary>

## Async LMDB database API

An example of usage (unit test of the module):
* [test__db.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_standard_services/db/versions/v_1/tests/test__db.py)

</details>

<details>
<summary title="Async logging into LMDB database"><kbd> Async logging into LMDB database </kbd></summary>

## Async logging into LMDB database

Developer can observe their logs in runtime using `cengal.parallel_execution.coroutines.coro_tools.loop_administration.admin_tk` module (made with Async Tkinter GUI):
* [admin_tk.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_tools/loop_administration/admin_tk/versions/v_0/admin_tk.py)

An example of usage of the admin_tk:
* [admin_test.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_tools/loop_administration/admin_tk/versions/v_0/development/admin_test.py)

Alternatively, developer can load logs in off-line mode using Log Viewer application (made with async Tkinter GUI):
* [log_viewer.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_tools/log_viewer/versions/v_0/log_viewer.py)

</details>

<details>
<summary title="Async Tkinter and Customtkinter"><kbd> Async Tkinter and Customtkinter </kbd></summary>

## Async Tkinter and Customtkinter

* [tkinter_0.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_standard_services/tkinter/versions/v_0/development/tkinter_0.py)
* [customtkinter_0.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_standard_services/tkinter/versions/v_0/development/customtkinter_0.py)

</details>

<details>
<summary title="Async wxPython"><kbd> Async wxPython </kbd></summary>

## Async wxPython

* [async_wxpython_example.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/integrations/wxpython/versions/v_0/development/async_wxpython_example.py)

</details>

<details>
<summary title="Async QT (PySide, PySide2, PySide6, PyQt4, PyQt5, PyQt6)"><kbd> Async QT (PySide, PySide2, PySide6, PyQt4, PyQt5, PyQt6) </kbd></summary>

## Async QT (PySide, PySide2, PySide6, PyQt4, PyQt5, PyQt6)

* [pyside6__coro_slot_example_0.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/integrations/qt/pyside6/versions/v_0/development/pyside6__coro_slot_example_0.py)

</details>

<details>
<summary title="Async PyTermGUI"><kbd> Async PyTermGUI </kbd></summary>

## Async [PyTermGUI](https://github.com/bczsalba/pytermgui)

* [hello_world_app_autoexit.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/integrations/pytermgui/versions/v_0/development/hello_world_app_autoexit.py)
* [hello_world.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/integrations/pytermgui/versions/v_0/development/hello_world.py)

</details>

<details>
<summary title="Wrapper for Netti (reliable UDP connection library for games in Nim)"><kbd> Wrapper for Netti (reliable UDP connection library for games in Nim) </kbd></summary>

## Wrapper for [Netti (reliable UDP connection library for games in Nim)](https://github.com/treeform/netty)

* [netty_benchmarks.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/integrations/nim__netty/core/versions/v_0/development/netty_benchmarks.py)

</details>

<details>
<summary title="Transparent background for your desktop applications (TBA)"><kbd> Transparent background for your desktop applications (TBA) </kbd></summary>

## Transparent background for your desktop applications (TBA)

* Target OS: Windows 11, Windows 10, Windows 8, Windows 7, Windows Vista.
* Target frameworks: PySide, PyQt, Kivy, PyWebView 

![title](https://github.com/FI-Mihej/Cengal/raw/master/docs/assets/Cengal_PyWebView_Transparent_UI_Windows_10.png)
,
![title](https://github.com/FI-Mihej/Cengal/raw/master/docs/assets/Cengal_Kivy_Transparent_UI_Windows_10.png)

</details>

<details>
<summary title="Tkinter True Borderless apps for Windows platform (TBA)"><kbd> Tkinter True Borderless apps for Windows platform (TBA) </kbd></summary>

## Tkinter True Borderless apps for Windows platform (TBA)

* Target OS: Windows 11, Windows 10, Windows 8, Windows 7, Windows Vista.
* Target frameworks: CustomTkinter, Tkinter, ttkbootstrap, ...

![title](https://github.com/FI-Mihej/Cengal/raw/master/docs/assets/Cengal_Tkinter_True_Borderless_Draggable_Applications_Windows_10.png)

</details>

<details>
<summary title="Cengal Coroutines and Asyncio Administration and Monitoring Page"><kbd> Cengal Coroutines and Asyncio Administration and Monitoring Page </kbd></summary>

## Cengal Coroutines and Asyncio Administration and Monitoring Page

Observe loop performance, services state and coroutines list with details. Use an async interactive console in order to interact with your application from inside.

### YouTube Showcase

<a href="https://www.youtube.com/watch?feature=player_embedded&v=qiuOH9B6uCY" target="_blank">
 <img src="https://github.com/FI-Mihej/Cengal/raw/master/docs/assets/CoroSchedulerAdminYoutube.png" alt="Watch the video" width="640" height="360" border="5" />
</a>

### Examples

[admin_test.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_tools/loop_administration/admin_tk/versions/v_0/development/admin_test.py)

</details>


# Modules with unique functionality

<details>
<summary title="Unique modules List (was not updated for some time)"><kbd> Unique modules List (was not updated for some time) </kbd></summary>

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

</details>

# Some Other modules

<details>
<summary title="Other modules List (was not updated for some time)"><kbd> Other modules List (was not updated for some time) </kbd></summary>

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

</details>

## Size of the Cengal library

At the moment of 19 Mar 2024:

Around 200 modules

```
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                         751          23696          30083          77396
Cython                          10            727            472           1892
C                                2             39             26            163
C/C++ Header                     2             14             26             37
Go                               3             19             37             88
Nim                              2             14              6             36
-------------------------------------------------------------------------------
SUM:                           770          24509          30650          79612
-------------------------------------------------------------------------------
```

Counted with [cloc](https://github.com/AlDanial/cloc) util.

## Unittest coverage

At the moment of 2 Apr 2024:

Linux:

```
Stmts   Miss  Cover
41576  25826    38%
```

## Examples

<details>
<summary title="Examples locations"><kbd> Examples locations </kbd></summary>

* Can be found in [examples](https://github.com/FI-Mihej/Cengal/blob/master/examples/) dir
* Each module has a `development` folder. Examples are usually placed there
* Some of old examples can be fined inside the [tests](https://github.com/FI-Mihej/Cengal/blob/master/tests/) dir.

### Cengal.coroutines examples

* [General idea, greenlet main Cengal.coro](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_tools/run_in_loop/versions/v_0/development/main.py)
* [General idea, async main Cengal.coro](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_tools/run_in_loop/versions/v_0/development/amain.py)
* [Transparent interconnection between Cengal.coroutines and asyncio](https://github.com/FI-Mihej/Cengal/blob/master/cengal/parallel_execution/coroutines/coro_tools/run_in_loop/versions/v_0/development/asyncio_interconnection.py)

### Text processing example

[Ensures and updates copyright (with dates) in each Cengal's source file](https://github.com/FI-Mihej/Cengal/blob/master/cengal_setup_scripts/ensure_copyright/ensure_copyright.py)

</details>

# Build from sources

<details>
<summary title="Build instructions"><kbd> Build instructions </kbd></summary>

Linux, macOS:

```bash
git clone https://github.com/FI-Mihej/Cengal.git
cd ./Cengal
./prepare__setup.sh
./install_in_dev_mode.sh
```

Windows:

```bat
git clone https://github.com/FI-Mihej/Cengal.git
cd .\Cengal
.\prepare__setup.cmd
.\install_in_dev_mode.cmd
```

Installation process requires compilation. So ensure that:
* GCC/Clang is installed in your Linux/WSL (`sudo apt-get --yes install build-essential` for Ubuntu. And `./before_install_on_wsl.sh` for Ubuntu under WSL for UI like Tkinter or Qt if you are using some kind of XServer on your host Windows)
* At least `Visual Studio Community - Build Tools` are installed on your Windows and you are installing Cengal from within its `Developer Command Prompt` for an appropriate target CPU architecture (`x64 Native Tools Command Prompt for VS 2022` for example). Make sure that you have compatible version of Visual Studio for your target CPython interpreter (see `python -VV` command output. For example `Python 3.9.11 (tags/v3.9.11:2de452f, Mar 16 2022, 14:33:45) [MSC v.1929 64 bit (AMD64)]`: this python interpreter requires Visual Studio 2019 version 16.11.2+ according to `1929` word search in [Wikipedia page](https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B))
* Nim installed (Optional)
* Go installed (Optional)

</details>

# Projects using Cengal

* [CengalPolyBuild](https://github.com/FI-Mihej/CengalPolyBuild) - A Comprehensive and Hackable Build System for Multilingual Python Packages: Cython (including automatic conversion from Python to Cython), C/C++, Objective-C, Go, and Nim, with ongoing expansions to include additional languages. (Planned to be released soon) 
* [InterProcessPyObjects](https://github.com/FI-Mihej/InterProcessPyObjects) - High-performance package delivers blazing-fast inter-process communication through shared memory, enabling Python objects to be shared across processes with exceptional efficiency. 
* [cengal_app_dir_path_finder](https://github.com/FI-Mihej/cengal_app_dir_path_finder) - A Python module offering a unified API for easy retrieval of OS-specific application directories, enhancing data management across Windows, Linux, and macOS 
* [cengal_cpu_info](https://github.com/FI-Mihej/cengal_cpu_info) - Extended, cached CPU info with consistent output format.
* [cengal_memory_barriers](https://github.com/FI-Mihej/cengal_memory_barriers) - Fast crossplatform memory barriers for Python.
* [flet_async](https://github.com/FI-Mihej/flet_async) - wrapper which makes [Flet](https://github.com/flet-dev/flet) async and brings booth Cengal.coroutines and asyncio to Flet (Flutter based UI)
* [justpy_containers](https://github.com/FI-Mihej/justpy_containers) - wrapper around [JustPy](https://github.com/justpy-org/justpy) in order to bring more security and more production-needed features to JustPy (VueJS based UI)
* [Bensbach](https://github.com/FI-Mihej/Bensbach) - decompiler from Unreal Engine 3 bytecode to a Lisp-like script and compiler back to Unreal Engine 3 bytecode. Made for a game modding purposes
* [Realistic-Damage-Model-mod-for-Long-War](https://github.com/FI-Mihej/Realistic-Damage-Model-mod-for-Long-War) - Mod for both the original XCOM:EW and the mod Long War. Was made with a Bensbach, which was made with Cengal
* [SmartCATaloguer.com](http://www.smartcataloguer.com/index.html) - TagDB based catalog of images (tags), music albums (genre tags) and apps (categories)

# License

Copyright © 2012-2024 ButenkoMS. All rights reserved.

Licensed under the Apache License, Version 2.0.
