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

# Examples

[shared_memory_example.py](https://github.com/FI-Mihej/Cengal/blob/master/cengal/hardware/memory/shared_memory/versions/v_1/development/shared_memory_example.py)

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
    with consumer:
        consumer.init_consumer()
        consumer.wait_for_messages()
        with wait_my_turn(consumer):
            shared_data = consumer.take_message()
        
        work(consumer, shared_data)


creator: SharedMemory = SharedMemory(shared_memory_name, True, shared_memory_size)
with creator:
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

# Performance Benchmark results

Shared `list` container (which is not yet fully optimizes currently) is already faster than `multiprocessing.shared_memory.ShareableList`.
And unlike `multiprocessing.shared_memory.ShareableList` supports Addition Assignment (`shared_list[15] += 999`) and all other native methods and operators of items.
It provides an ability to make more than 30000000 reads/writes per second of an int64 value (`shared_list[2] = 1234` / `val = shared_list[7]`) or more than 1450000 addition assignments per second (`shared_list[15] += 999`).

[Benchmark Results](https://github.com/FI-Mihej/Cengal/blob/master/cengal/hardware/memory/shared_memory/versions/v_1/development/benchmark_results.md)


# Roadmap

* Continuosly moving more logic to Cython
* Implement mutable `dict` and `set` using an appropricate C hashmap library or C++ code (depending what will be faster in our case)
* Increase number of interacting processes from 2 to variable value
* Implement garbage collector for shared data in addition to manual `free()` call
* Implement an appropriate Service for `cengal.parallel_execution.coroutines` - for comfortable shared memory usage inside an async code (including `asyncio`) 
* Improve memory allocation algorithm in an attempt of making it faster
