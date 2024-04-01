# cengal_memory_barriers

Fast crossplatform memory barriers for Python.

Memory barriers are utilized by the operating system to implement synchronization primitives, such as Mutexes.

# Advantages

Supported OS: at least ["Linux", "Darwin", "Windows"]. Supported targets: at least ["Emscripten", "ARM", "x86_64", "x86", "i386", "i686", "AMD64"]. "Other" system or target should have "stdatomic.h" header to be supported.

# Installation

```bash
pip install cengal_memory_barriers
```

# Documentation

## Import

```python
from cengal_memory_barriers import full_memory_barrier, mm_pause
```

## Supported systems

| OS \ CPU:                               | x86 ("x86_64", "x86", "i386", "i686", "AMD64") | ARM | Emscripten | Other targets |
|-----------------------------------------|------------------------------------------------|-----|------------|---------------|
| Linux                                   | +                                              | +   | +          | +             |
| Darwin                                  | +                                              | +   | +          | +             |
| Windows                                 | +                                              | +   | +          |               |
| Other systems with "stdatomic.h" header | +                                              | +   | +          | +             |

## Available functions per system

| Func name: \ System:         | Linux/Darwin (x86) | Linux/Darwin (ARM) | Windows (x86) | Windows (ARM) | Emscripten | Other systems with "stdatomic.h" header |
|------------------------------|--------------------|--------------------|---------------|---------------|------------|-----------------------------------------|
| full_memory_barrier()        | +                  | +                  | +             | +             | +          | +                                       |
| memory_barrier()             | +                  | +                  | +             | +             | +          | +                                       |
| sync_synchronize()           | +                  | +                  | +             | +             | +          | +                                       |
|                              |                    |                    |               |               |            |                                         |
| mm_pause()                   | +                  | +                  | +             | +             | +          | +                                       |
| mm_mfence()                  | +                  | +                  | +             | +             | +          | +                                       |
| mm_sfence()                  | +                  | +                  | +             | +             | +          | +                                       |
| mm_lfence()                  | +                  | +                  | +             | +             | +          | +                                       |
|                              |                    |                    |               |               |            |                                         |
| mm_clflush(...)              | +                  |                    | +             |               |            |                                         |
| iso_volatile_store16(...)    |                    |                    |               | +             |            |                                         |
| py_emscripten_atomic_fence() |                    |                    |               |               | +          |                                         |
| clear_cache(...)             | +/- (Linux only)   | +/- (Linux only)   |               |               |            |                                         |
| py_atomic_thread_fence(...)  | +                  | +                  |               |               | +          | +                                       |
| py_atomic_thread_fence__*()  | +                  | +                  |               |               | +          | +                                       |

## Backend calls - Main functions

| System: \ Func name:                    | `full_memory_barrier()`                   | `memory_barrier()`                        | `sync_synchronize()`                      |
|-----------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| Linux/Darwin (x86)                      | _mm_mfence()                              | _mm_mfence()                              | __sync_synchronize()                      |
| Linux/Darwin (ARM)                      | __sync_synchronize()                      | __sync_synchronize()                      | __sync_synchronize()                      |
| Windows (x86)                           | MemoryBarrier()                           | MemoryBarrier()                           | MemoryBarrier()                           |
| Windows (ARM)                           | MemoryBarrier()                           | MemoryBarrier()                           | MemoryBarrier()                           |
| Emscripten                              | emscripten_atomic_fence()                 | __sync_synchronize()                      | __sync_synchronize()                      |
| Other systems with "stdatomic.h" header | atomic_thread_fence(MEMORY_ORDER_SEQ_CST) | atomic_thread_fence(MEMORY_ORDER_SEQ_CST) | atomic_thread_fence(MEMORY_ORDER_SEQ_CST) |

## Backend calls - Secondary functions

| System: \ Func name:                    | `mm_mfence()`                             | `mm_sfence()`                             | `mm_lfence()`                             | `mm_pause()` |
|-----------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|--------------|
| Linux/Darwin (x86)                      | _mm_mfence()                              | _mm_sfence()                              | _mm_lfence()                              | _mm_pause()  |
| Linux/Darwin (ARM)                      | __sync_synchronize()                      | __sync_synchronize()                      | __sync_synchronize()                      | pass         |
| Windows (x86)                           | _mm_mfence()                              | _mm_sfence()                              | _mm_lfence()                              | _mm_pause()  |
| Windows (ARM)                           | MemoryBarrier()                           | MemoryBarrier()                           | MemoryBarrier()                           | pass         |
| Emscripten                              | __sync_synchronize()                      | __sync_synchronize()                      | __sync_synchronize()                      | pass         |
| Other systems with "stdatomic.h" header | atomic_thread_fence(MEMORY_ORDER_SEQ_CST) | atomic_thread_fence(MEMORY_ORDER_SEQ_CST) | atomic_thread_fence(MEMORY_ORDER_SEQ_CST) | pass         |

## Backend calls - Unique calls

| Func name:                                     | Backend call:                             |
|------------------------------------------------|-------------------------------------------|
| mm_clflush(p: int) -> None                     | _mm_clflush(...)                          |
| iso_volatile_store16(p: int, val: int) -> None | __iso_volatile_store16(...)               |
| py_emscripten_atomic_fence() -> None           | emscripten_atomic_fence()                 |
| clear_cache(beg: int, end: int) -> None        | __clear_cache(...)                        |
| py_atomic_thread_fence(order: int) -> None     | atomic_thread_fence(...)                  |
| py_atomic_thread_fence__memory_order_relaxed() | atomic_thread_fence(MEMORY_ORDER_RELAXED) |
| py_atomic_thread_fence__memory_order_consume() | atomic_thread_fence(MEMORY_ORDER_CONSUME) |
| py_atomic_thread_fence__memory_order_acquire() | atomic_thread_fence(MEMORY_ORDER_ACQUIRE) |
| py_atomic_thread_fence__memory_order_release() | atomic_thread_fence(MEMORY_ORDER_RELEASE) |
| py_atomic_thread_fence__memory_order_acq_rel() | atomic_thread_fence(MEMORY_ORDER_ACQ_REL) |
| py_atomic_thread_fence__memory_order_seq_cst() | atomic_thread_fence(MEMORY_ORDER_SEQ_CST) |

Alternatives description:
* `clear_cache(beg: int, end: int) -> None` - "Linux", "Darwin" - An alternative to `mm_clflush()` in GCC and Clang compilers
* `iso_volatile_store16(p: int, val: int) -> None` - "Windows" - "ARM" - An alternative to `mm_clflush()` for ARM in Visual Studio compiler
* `py_emscripten_atomic_fence() -> None` - "Emscripten" - Probably can be used as an alternative to `mm_clflush()` for Emscripten

# Based on Cengal

Represents part of Cengal library:
* https://pypi.org/project/cengal/
* https://github.com/FI-Mihej/Cengal

An equivalent import:
```python
from cengal.hardware.memory.barriers import full_memory_barrier, mm_pause
```

Cengal library can be installed by:

```bash
pip install cengal
```


# Projects using Cengal

* [flet_async](https://github.com/FI-Mihej/flet_async) - wrapper which makes [Flet](https://github.com/flet-dev/flet) async and brings booth Cengal.coroutines and asyncio to Flet (Flutter based UI)
* [justpy_containers](https://github.com/FI-Mihej/justpy_containers) - wrapper around [JustPy](https://github.com/justpy-org/justpy) in order to bring more security and more production-needed features to JustPy (VueJS based UI)
* [Bensbach](https://github.com/FI-Mihej/Bensbach) - decompiler from Unreal Engine 3 bytecode to a Lisp-like script and compiler back to Unreal Engine 3 bytecode. Made for a game modding purposes
* [Realistic-Damage-Model-mod-for-Long-War](https://github.com/FI-Mihej/Realistic-Damage-Model-mod-for-Long-War) - Mod for both the original XCOM:EW and the mod Long War. Was made with a Bensbach, which was made with Cengal
* [SmartCATaloguer.com](http://www.smartcataloguer.com/index.html) - TagDB based catalog of images (tags), music albums (genre tags) and apps (categories)

# License

Copyright © 2012-2024 ButenkoMS. All rights reserved.

Licensed under the Apache License, Version 2.0.