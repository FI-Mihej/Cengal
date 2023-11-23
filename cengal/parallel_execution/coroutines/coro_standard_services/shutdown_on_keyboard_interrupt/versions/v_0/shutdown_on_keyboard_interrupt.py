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


__all__ = ['ShutdownOnKeyboardInterrupt']


from cengal.parallel_execution.coroutines.coro_scheduler import *
import signal
from typing import Tuple


class ShutdownOnKeyboardInterrupt(TypedService[None]):
    def __init__(self, loop: CoroScheduler):
        super().__init__(loop)
        self.handler_set: bool = False
        self.previous_handler = None
        self.keyboard_interrupt_emited: bool = False

    def single_task_registration_or_immediate_processing(
            self, *args, **kwargs) -> Tuple[bool, None, None]:
        if not self.handler_set:
            self.previous_handler = signal.signal(signal.SIGINT, self.keyboard_interrupt_handler)
            self.handler_set = True
        
        return True, None, None

    def full_processing_iteration(self):
        if self.keyboard_interrupt_emited:
            signal.signal(signal.SIGINT, self.previous_handler)
            self.handler_set = False
            if callable(self.previous_handler):
                def on_cs_destroy_handler():
                    self.previous_handler(signal.SIGINT, None)
                
                self._loop.on_destroyed_handlers.add(on_cs_destroy_handler)

            raise CoroSchedulerDestroyRequestedException
        
        self.make_dead()

    def in_work(self) -> bool:
        result: bool = self.keyboard_interrupt_emited
        return self.thrifty_in_work(result)
    
    def keyboard_interrupt_handler(self, sig, frame):
        self.keyboard_interrupt_emited = True
        self.make_live()
    
    def destroy(self):
        if self.handler_set:
            signal.signal(signal.SIGINT, self.previous_handler)
            self.handler_set = False
