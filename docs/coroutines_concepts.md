# Coroutines Concepts

Asyncio-compatible loops and Trio/Curio have quite monolithic architecture an as result it is quite hard to extend them. For example Uvloop has no shared code with asyncio. Also functionality is quite limited: launch timer (usually with an accuracy no better than once per 0.0167 sec on Windows) or coroutine and do some IO. Other extensions must handle all work with user code by them selves (handle singletons, ensure that all instances of some class are in sync between each other and the core of the extension, etc.). It is not such easy task to implement and usually leads to more errors than it can be in better case.

Cengal coroutines on the other hand, are like microkernel: they have small core and extendable bunch of smart services. For example, coro calls PutCoro service to create a task (in asyncio terms). Of cource putting coroutine is a basic functionality which is provided by loop itself, however an appropriate call allowed to be done only from outside of coroutine. As result we have universal entry point (PutCoro service) which can provide us with a complex and smart functionality like coroutines tree monitoring and manipulation. Developer can make their own implementation of other service and user can choose what version to use by importing (and calling) one or another version. Or developer can mark their version as a drop-in replacement or **alias**. And all third-party code will use it as well, without code modification, if user will use it.

An each coroutine has a set of on_delete handlers. It can be empty. Many of services use this functionality. Both developer and user can use this functionality as well.

# Types of coroutines

Cengal has two types of coroutines: async-await based and greenlets based. Both of them are executed concurrently within the same loop.

## Advantages of async-await coroutines

You can use any Asyncio code (and potentially Trio/Curio code) from inside of this coroutines. It is not an attempt of emulating subset of Asyncio API like in Trio. All alien requests are redirected to Asyncio loop (either external or internal). As result, Cengal do not need to constantly monitor changes in Asyncio/Uvloop to be in sync. Any Asyncio-compatible loop (Uvloop for example) is already supported and will be supported.

Supported on all Python compatible platforms. Including Emscripten an as a result - PyScript.

## Advantages of greenlet coroutines

Such a coroutine can be executed from any general synchronous Python code with ability to yield to the main loop. Cengal is using them to convert third-party synchronous libraries (Tkinter, Qt, wxWidget, Kivy, etc.) to asynchronous without changing their code.

Do not require "async" and "await" words spamming across the code.

You do not need to write two version of same function (one for sync and other for async code) unlike any async-await code. Just check is you are in the loop or not. Also you can use default loop (if registered in the current thread) or some variable with an explicit link to the loop instance.

## Disadvantages of greenlet coroutines

Number of supported platforms is currently limited to Windows, Mac OS X / iOS, Linux / Android. Emscripten (and PyScript) is not currently supported.

Support of Emscripten is planned (by using different C code in addition to greenlets).

# Imports

## Main

User-useful imports:

```python
from cengal.parallel_execution.coroutines.coro_scheduler import (
    CoroID, Interface, CoroScheduler,
    Coro, CoroType, 
    cs_coro, cs_acoro, 
    ExplicitWorker, AnyWorker, 
    execute_coro, exec_coro, ecoro, aexecute_coro, aexec_coro, aecoro, 
    OnCoroDelHandler, 
    OutsideCoroSchedulerContext, PrimaryCoroSchedulerWasNotSet, CoroSchedulerContextIsNotAvailable, WrongTypeOfShedulerError, InterfaceIsNotAvailableError, CurrentCoroIsNotAliveError, 
    current_coro_scheduler, get_current_coro_scheduler, set_primary_coro_scheduler, available_coro_scheduler, get_available_coro_scheduler, loop_with_backup_loop, get_loop_with_backup_loop, loop_with_explicit_loop, get_loop_with_explicit_loop, interface_and_loop_with_backup_loopk, get_interface_and_loop_with_backup_loop, interface_and_loop_with_explicit_loop, get_interface_and_loop_with_explicit_loop, interface_for_an_explicit_loop, get_interface_for_an_explicit_loop, service_with_backup_loop, get_service_with_backup_loop, service_with_explicit_loop, get_service_with_explicit_loop, service_fast_with_backup_loop, get_service_fast_with_backup_loop, service_fast_with_explicit_loop, get_service_fast_with_explicit_loop, 
)
```

or in general

```python
from cengal.parallel_execution.coroutines.coro_scheduler import *
```

## Standard Services

Standard services:
```python
from cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus import *
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import *
from cengal.parallel_execution.coroutines.coro_standard_services.communication import *
from cengal.parallel_execution.coroutines.coro_standard_services.cpu_tick_count_per_second import *
from cengal.parallel_execution.coroutines.coro_standard_services.db import *
from cengal.parallel_execution.coroutines.coro_standard_services.event_bus import *
from cengal.parallel_execution.coroutines.coro_standard_services.fast_aggregator import *
from cengal.parallel_execution.coroutines.coro_standard_services.instance import *
from cengal.parallel_execution.coroutines.coro_standard_services.kill_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.kill_coro_list import *
from cengal.parallel_execution.coroutines.coro_standard_services.lazy_print import *
from cengal.parallel_execution.coroutines.coro_standard_services.lmdb import *
from cengal.parallel_execution.coroutines.coro_standard_services.log import *
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import *
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro_list import *
from cengal.parallel_execution.coroutines.coro_standard_services.read_write_locker import *
from cengal.parallel_execution.coroutines.coro_standard_services.remote_nodes import *
from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_loop import *
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_on_keyboard_interrupt import *
from cengal.parallel_execution.coroutines.coro_standard_services.simple_yield import *
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import *
from cengal.parallel_execution.coroutines.coro_standard_services.some_printer import *
from cengal.parallel_execution.coroutines.coro_standard_services.throw_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.throw_coro_list import *
from cengal.parallel_execution.coroutines.coro_standard_services.timer_coro_runner import *
from cengal.parallel_execution.coroutines.coro_standard_services.timer_func_runner import *
from cengal.parallel_execution.coroutines.coro_standard_services.tkinter import *
from cengal.parallel_execution.coroutines.coro_standard_services.wait_coro import *
```

## Tools

```python
from cengal.parallel_execution.coroutines.coro_tools.await_coro import *
from cengal.parallel_execution.coroutines.coro_tools.coro_flow_control import *
from cengal.parallel_execution.coroutines.coro_tools.loop_administration import *
from cengal.parallel_execution.coroutines.coro_tools.low_latency import *
from cengal.parallel_execution.coroutines.coro_tools.prepare_loop import *
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import *
from cengal.parallel_execution.coroutines.coro_tools.wait_coro import *
```

## Integrations

In some cases it is enough to create a set of functions or coroutines to integrate with some third-party package instead of new stand-alone service creation. For example: `customtkinter` requires one single small function to be used in addition to Tkinter Service; and it is can be handfull to register `uvloop` as a default asyncio-compatible loop automatically, if it is awailable. 

```python
from cengal.parallel_execution.coroutines.integrations.customtkinter import *
from cengal.parallel_execution.coroutines.integrations.nicegui import *
from cengal.parallel_execution.coroutines.integrations.pytermgui import *
from cengal.parallel_execution.coroutines.integrations.qt import *
from cengal.parallel_execution.coroutines.integrations.uvicorn import *
from cengal.parallel_execution.coroutines.integrations.uvloop import *
```

# Explicit Syntax

## Async-Await

```python
async def sub_coro(i: Interface, ...):
    ...

@cs_acoro
async def sub_coro_2(...):
    i: Interface = current_interface()
    ...

async def coro(i: Interface, ...):
    await sub_coro(i)
    await sub_coro_2(i)
    ...
```

```python
class Class:
    async def sub_coro(self, i: Interface, ...):
        ...
    
    @cs_acoro
    async def sub_coro_2(self, ...):
        i: Interface = current_interface()
        ...
    
    async def coro(self, i: Interface, ...):
        await self.sub_coro(i)
        await self.sub_coro_2(i)
        ...
```

## Greenlets

```python
def sub_coro(i: Interface, ...):
    ...

@cs_coro
def sub_coro_2(...):
    i: Interface = current_interface()
    ...

def coro(i: Interface, ...):
    sub_coro(i)
    sub_coro_2(i)
    ...
```

```python
class Class:
    def sub_coro(self, i: Interface, ...):
        ...

    @cs_coro
    def sub_coro_2(self, ...):
        i: Interface = current_interface()
        ...

    def coro(self, i: Interface, ...):
        self.sub_coro(i)
        self.sub_coro_2(i)
        ...
```

# Implicit Syntax

## Async-Await

```python
async def implicit_coro(...):
    i: Interface = current_interface()
    ...

async def coro(i: Interface, ...):
    await implicit_coro()
    ...
```

```python
class Class:
    async def implicit_coro(self, ...):
        i: Interface = current_interface()
        ...

    async def coro(self, i: Interface, ...):
        await self.implicit_coro()
        ...
```

## Greenlets

```python
def implicit_coro(...):
    i: Interface = current_interface()
    ...

def coro(i: Interface, ...):
    implicit_coro()
    ...
```

```python
class Class:
    def implicit_coro(...):
        i: Interface = current_interface()
        ...

    def coro(self, i: Interface, ...):
        implicit_coro()
        ...
```

# Working with services

Calls to services are made through the Interface instances which are provided by loop to an each coroutine. Each such a call to the service returns execution back to the loop until coroutine receives a response from the service.

If service has only one type of a request, its API is a simplest:

```python
def coro(i: Interface) -> str:
    i(Sleep, 0.0004)
    return 'Hello World'
```
or

```python
async def coro(i: Interface) -> str:
    await i(Sleep, 0.0004)

    return 'Hello World'
```

Otherwise, service can have one or several ServerRequest-derived classes


```python
def coro(i: Interface) -> str:
    i(FastAggregator, FastAggregatorRequest().wait(DataStreamID))
    i(FastAggregatorRequest().wait(DataStreamID))
    i(FastAggregatorWaitFor(DataStreamID))

    result: str = i(RunCoro, my_concat_str_coro, 'hello', 'coro')  ## will create a new coro and waits until it will be finished

    coro_id: CoroID = i(PutCoro, my_concat_str_coro, 'hello', 'coro')  ## Creates coroutine and returns its ID
    i(WaitCoro, WaitCoroRequest(result_required=False).single(coro_id))  ## Will wait until coro with coro_id will be finished. (Coro can be already finished before this call - it's totaly OK)
    result: str = i(WaitCoro, WaitCoroRequest().single(coro_id))  ## Will wait until coro with coro_id will be finished. (Will raise `SubCoroutineNotFoundError` if coro was already finished before this call)
    assert 'hello coro' == result

    i(WaitCoroRequest(timeout=0.01, kill_on_timeout=True, tree=True).list([
        CoroID_0,
        CoroID_1,
        CoroID_2,
    ]))  # Will wait until at least one of coroutines completes. Will kill all coroutines with all their children coroutines if timeout is reached before at leas one of coroutines completes.

    i(WaitCoroRequest(timeout=0.01, kill_on_timeout=True, tree=True).put_fastest([
        PutSingleCoroParams(my_coro_0, 'hello', 'world'),
        PSCP(my_coro_1, 'hello', 'world'),
        PSCP(my_coro_2, 'hello', 'world'),
    ]))  # Will start three new corotines. Will wait until at least one of coroutines completes. Will kill all coroutines with all their children coroutines if timeout is reached before at leas one of coroutines completes.

    return 'Hello World'
```
or

```python
async def coro(i: Interface) -> str:
    await i(FastAggregator, FastAggregatorRequest().wait(DataStreamID))
    await i(FastAggregatorRequest().wait(DataStreamID))
    await i(FastAggregatorWaitFor(DataStreamID))

    result: str = await i(RunCoro, my_concat_str_coro, 'hello', 'coro')  ## will create a new coro and waits until it will be finished

    coro_id: CoroID = await i(PutCoro, my_concat_str_coro, 'hello', 'coro')  ## Creates coroutine and returns its ID
    await i(WaitCoro, WaitCoroRequest(result_required=False).single(coro_id))  ## Will wait until coro with coro_id will be finished. (Coro can be already finished before this call - it's totaly OK)
    result: str = await i(WaitCoro, WaitCoroRequest().single(coro_id))  ## Will wait until coro with coro_id will be finished. (Will raise `SubCoroutineNotFoundError` if coro was already finished before this call)
    assert 'hello coro' == result

    await i(WaitCoroRequest(timeout=0.01, kill_on_timeout=True, tree=True).list([
        coro_id_0,
        coro_id_1,
        coro_id_2,
    ]))  # Will wait until at least one of coroutines completes. Will kill all coroutines with all their children coroutines if timeout is reached before at leas one of coroutines completes.

    await i(WaitCoroRequest(timeout=0.01, kill_on_timeout=True, tree=True).put_fastest([
        PutSingleCoroParams(my_coro_0, 'hello', 'world'),
        PSCP(my_coro_1, 'hello', 'world'),
        PSCP(my_coro_2, 'hello', 'world'),
    ]))  # Will start three new corotine. Will wait until at least one of coroutines completes. Will kill all coroutines with all their children coroutines if timeout is reached before at leas one of coroutines completes.

    return 'Hello World'
```

# Work with different coroutines types

We can make general call (for a greenlet coro) or await (for an async coro) when we are working with the same coroutine type.

```python
@cs_coro
def coro_green(a: int, b: int) -> int:
    return a - b


@cs_acoro
async def coro_async(a: int, b: int) -> int:
    return a - b


def main_green(i: Interface):
    res = coro_green(i, 1, 2)
    res = execute_coro(coro_green, 1, 2)
    res = exec_coro(coro_green, 1, 2)
    res = ecoro(coro_green, 1, 2)


async def main_async(i: Interface):
    res = await coro_async(i, 1, 2)
    res = await aexecute_coro(coro_async, 1, 2)
    res = await aexec_coro(coro_async, 1, 2)
    res = await aecoro(coro_async, 1, 2)
```

On the other hand, a general way to work with a different or unknown type of coroutines is through an appropriate services (RunCoro, PutCoro, WaitCoro, ThrowCoro, KillCoro, etc.)

```python
@cs_coro
def coro_green(a: int, b: int) -> int:
    return a - b


@cs_acoro
async def coro_async(a: int, b: int) -> int:
    return a - b


def main_green(i: Interface):
    res_0 = i(RunCoro, coro_green, 1, 2)
    res_1 = i(RunCoro, coro_async, 1, 2)
    assert res_0 == res_1


async def main_async(i: Interface):
    res_0 = await i(RunCoro, coro_green, 1, 2)
    res_1 = await i(RunCoro, coro_async, 1, 2)
    assert res_0 == res_1
```

Be aware that same as with Asyncio Code, next Cengal Coroutines code will not return execution back to the loop (unlike work through an appropriate services):

```python
@cs_coro
def coro_green(a: int, b: int) -> int:
    return a - b


@cs_acoro
async def coro_async(a: int, b: int) -> int:
    return a - b


def main_green(i: Interface):
    for True:
        coro_green(i, 1, 2)


async def main_async(i: Interface):
    for True:
        await coro_async(i, 1, 2)
```

It is because an `await` keyword in Python does not return execution back to the loop. And there is a common misunderstood among interviewed by me Senior Python Developers when developer thinks that an each `await` or even `async` keyword returns execution back to the loop which is not true.
