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


__all__ = ['Lock']


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


from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro
from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
from cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus import AsyncEventBus, AsyncEventBusRequest, EventID
from cengal.parallel_execution.coroutines.coro_standard_services.wait_coro import WaitCoro, WaitCoroRequest, PutSingleCoroParams, CoroutineNotFoundError, TimeoutError
from cengal.time_management.load_best_timer import perf_counter
from cengal.math.numbers import RationalNumber
from typing import Optional, Union


async def wait_for_event(i: Interface, event: EventID):
    await i(AsyncEventBus, AsyncEventBusRequest().wait(event))
    return True


class Lock:
    def __init__(self, event: EventID, timeout: Optional[RationalNumber] = None, parent: Optional['Lock'] = None) -> None:
        self._locked: bool = False
        self._event: EventID = event
        self.timeout: Optional[RationalNumber] = timeout
        self.parent: Optional['Lock'] = parent
        self.last_lock_attempt_successful: Union[None, bool] = None
    
    @property
    def locked(self):
        if self.parent is None:
            return self._locked
        else:
            return self.parent.locked
    
    @locked.setter
    def locked(self, value: bool):
        if self.parent is None:
            self._locked = value
        else:
            self.parent.locked = value
    
    @property
    def event(self):
        if self.parent is None:
            return self._event
        else:
            return self.parent.event
    
    @event.setter
    def event(self, value: EventID):
        if self.parent is None:
            self._event = value
        else:
            self.parent.event = value
    
    def lock(self, timeout: RationalNumber):
        return Lock(self.event, timeout, self)
    
    def try_lock(self):
        return Lock(self.event, 0, self)
    
    def __enter__(self):
        if self.locked:
            if 0 == self.timeout:
                self.last_lock_attempt_successful = False
                return False
            elif self.timeout is None:
                i: Interface = current_interface()
                i(RunCoro, wait_for_event, self.event)
                self.locked = True
                self.last_lock_attempt_successful = True
                return True
            else:
                i = current_interface()
                try:
                    need_to_repeat = True
                    time_spend = 0
                    while need_to_repeat and ((self.timeout is None) or (time_spend < self.timeout)):
                        start_time: float = perf_counter()
                        wait_for_event_coro_id: CoroID = i(PutCoro, wait_for_event, self.event)
                        try:
                            i(WaitCoro, WaitCoroRequest(self.timeout - time_spend, kill_on_timeout=True, result_required=True).single(wait_for_event_coro_id))
                        except CoroutineNotFoundError:
                            pass

                        time_spend += perf_counter() - start_time
                        if not self.locked:
                            self.locked = True
                            self.last_lock_attempt_successful = True
                            need_to_repeat = False
                            return True
                except TimeoutError:
                    pass
                
                return False
        else:
            self.locked = True
            self.last_lock_attempt_successful = True
            return True
    
    def __exit__(self, type, value: Exception, traceback):
        self.locked = False
        i: Interface = current_interface()
        i(AsyncEventBus, AsyncEventBusRequest().send_event(self.event, None))

    async def __aenter__(self):
        if self.locked:
            if 0 == self.timeout:
                self.last_lock_attempt_successful = False
                return False
            elif self.timeout is None:
                i: Interface = current_interface()
                await i(RunCoro, wait_for_event, self.event)
                self.locked = True
                self.last_lock_attempt_successful = True
                return True
            else:
                i = current_interface()
                try:
                    need_to_repeat = True
                    time_spend = 0
                    while need_to_repeat and ((self.timeout is None) or (time_spend < self.timeout)):
                        start_time: float = perf_counter()
                        wait_for_event_coro_id: CoroID = await i(PutCoro, wait_for_event, self.event)
                        try:
                            await i(WaitCoro, WaitCoroRequest(self.timeout - time_spend, kill_on_timeout=True, result_required=True).single(wait_for_event_coro_id))
                        except CoroutineNotFoundError:
                            pass

                        time_spend += perf_counter() - start_time
                        if not self.locked:
                            self.locked = True
                            self.last_lock_attempt_successful = True
                            need_to_repeat = False
                            return True
                except TimeoutError:
                    pass
                
                return False
        else:
            self.locked = True
            self.last_lock_attempt_successful = True
            return True

    async def __aexit__(self, type, value, traceback):
        self.locked = False
        i: Interface = current_interface()
        await i(AsyncEventBus, AsyncEventBusRequest().send_event(self.event, None))
