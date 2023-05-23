#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.2.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import time
from cengal.time_management.repeat_for_a_time import TracerIterator, Tracer
from cengal.statistics.normal_distribution import count_99_95_68
from cengal.parallel_execution.asyncio.init_loop import init_loop
from cengal.parallel_execution.asyncio.run_loop import run_forever
import asyncio


def print_stats(sleep_check_results):
    val_99, val_95, val_68, max_deviation, min_deviation = count_99_95_68(sleep_check_results, min)
    print('Min:', val_99, val_95, val_68, max_deviation, min_deviation)
    
    val_99, val_95, val_68, max_deviation, min_deviation = count_99_95_68(sleep_check_results, max)
    print('Max:', val_99, val_95, val_68, max_deviation, min_deviation)
    
    val_99, val_95, val_68, max_deviation, min_deviation = count_99_95_68(sleep_check_results)
    print('Average:', val_99, val_95, val_68, max_deviation, min_deviation)


def sleep_check(sleep_time):
    start = time.perf_counter()
    time.sleep(sleep_time)
    stop = time.perf_counter()
    return stop - start


def time_sleep_test():
    print()
    print('time_sleep_test...')
    
    sleep_check_results = list()
    for i in TracerIterator(Tracer(5.0)):
        sleep_check_results.append(sleep_check(0.0000001))
    
    print_stats(sleep_check_results)


async def asleep_check(loop, sleep_time):
    start = time.perf_counter()
    await asyncio.sleep(sleep_time, loop=loop)
    stop = time.perf_counter()
    return stop - start


async def atime_sleep_test():
    print()
    print('atime_sleep_test...')
    
    loop = asyncio.get_event_loop()
    
    sleep_check_results = list()
    for i in TracerIterator(Tracer(5.0)):
        sleep_check_results.append(await asleep_check(loop, 0.0000001))
    
    print_stats(sleep_check_results)
    loop.stop()


class ACallLaterTest:
    def __init__(self, test_time: float) -> None:
        self.loop = None
        self.sleep_check_results = list()
        self.handle = None
        self.test_time = test_time
        self.test_start = None
        self.start = None
        self.stop = None
    
    async def run(self):
        print()
        print('ACallLaterTest...')
        
        self.loop = asyncio.get_event_loop()
        self()
    
    def __call__(self):
        current_time = time.perf_counter()
        if self.test_start is None:
            self.test_start = current_time
        
        if self.start is None:
            self.start = current_time
            self.handle = self.loop.call_later(0.0000001, self)
            return
        else:
            self.sleep_check_results.append(current_time - self.start)
            self.start = None
            if (current_time - self.test_start) >= self.test_time:
                print_stats(self.sleep_check_results)
                self.loop.stop()
            else:
                self()


if __name__ == '__main__':
    time_sleep_test()
    init_loop()
    run_forever(atime_sleep_test())
    run_forever(ACallLaterTest(5.0).run())
