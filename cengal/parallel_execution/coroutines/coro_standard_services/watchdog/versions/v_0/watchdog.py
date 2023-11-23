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
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


__all__ = ['WatchdogTimeoutError', 'Watchdog']


from cengal.parallel_execution.coroutines.coro_scheduler import *
import signal
from typing import Tuple, Optional
from threading import current_thread, main_thread, Thread
from cengal.time_management.sleep_tools import sleep
from cengal.math.numbers import RationalNumber
from signal import SIG_IGN, SIGUSR1, raise_signal, signal
from cengal.system import OS_API_TYPE


class WatchdogTimeoutError(Exception):
    pass


class HungedCoroInfo:
    def __init__(self, interface: Interface, coro_start_time: RationalNumber):
        self.interface: Interface = interface
        self.coro_start_time: RationalNumber = coro_start_time


class Watchdog(TypedService[None]):
    def __init__(self, loop: CoroScheduler):
        super().__init__(loop)
        self.handler_set: bool = False
        self.previous_handler = None
        self.keyboard_interrupt_emited: bool = False
        self.period: RationalNumber = 5
        if 'nt' == OS_API_TYPE:
            self.raised_signal = SIG_IGN
        else:
            self.raised_signal = SIGUSR1
        
        self.hunged_coro: Optional[HungedCoroInfo] = None
        self.watchdog_thread: Optional[Thread] = None
        self.watchdog_thread_name: str = '_CengalCoroutinesWatchdogDeamon_'
        self.watchdog_thread_allowed: bool = True
        self.watchdog_thread_in_work: bool = False

    def watchdog_thread_func(self):
        while self.watchdog_thread_allowed and (not self._loop._destroyed):
            sleep(self.period)
            self.watchdog_thread_in_work = True
            try:
                self.check_idle_coro()
            finally:
                self.watchdog_thread_in_work = False
    
    def check_idle_coro(self):
        loop: CoroScheduler = self._loop
        if get_current_coro_scheduler() is not loop:
            return
        
        curr_interface: Optional[Interface] = current_interface()
        if curr_interface is None:
            return

        if curr_interface.ignored_by_watchdog:
            return

        if loop.current_coro_start_time is None:
            return

        if self.hunged_coro is not None:
            return

        coro_execution_piece_delta_time = loop.get_coro_start_time() - loop.current_coro_start_time
        if coro_execution_piece_delta_time > self.period:
            raise_signal(self.raised_signal)
    
    def is_in_main_thread(self):
        return current_thread() is main_thread()

    def single_task_registration_or_immediate_processing(
            self, period: RationalNumber) -> Tuple[bool, None, None]:
        result = False
        if self.is_in_main_thread():
            self._loop.set_coro_time_measurement(True)
            if not self.handler_set:
                self.previous_handler = signal.signal(self.raised_signal, self.interrupt_handler)
                self.handler_set = True
            
            if self.watchdog_thread is None:
                self.watchdog_thread = Thread(target=self.watchdog_thread_func, name=self.watchdog_thread_name, daemon=True)
                self.watchdog_thread.start()

            self.period = period
            result = True
        
        return result, None, None

    def full_processing_iteration(self):
        self.make_dead()

    def in_work(self) -> bool:
        result: bool = self.keyboard_interrupt_emited
        return self.thrifty_in_work(result)
    
    def interrupt_handler(self, sig, frame):
        if self.hunged_coro is None:
            return
        
        loop: CoroScheduler = self._loop
        if get_current_coro_scheduler() is not loop:
            return
        
        if current_interface() is not self.hunged_coro.interface:
            return

        if loop.current_coro_start_time != self.hunged_coro.coro_start_time:
            return

        try:
            raise WatchdogTimeoutError
        finally:
            self.hunged_coro = None
    
    def destroy(self):
        if self.watchdog_thread is not None:
            self.watchdog_thread_allowed = False
            while self.watchdog_thread_in_work:
                sleep(0.0001, high_cpu_utilisation_mode=True)
            
            # self.watchdog_thread.join()  # we don ot need this since it is a daemon thread
            self.watchdog_thread = None

        if self.handler_set:
            signal.signal(self.raised_signal, self.previous_handler)
            self.handler_set = False
