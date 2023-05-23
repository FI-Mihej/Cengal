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
__version__ = "3.2.2"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


__all__ = ['Sleep']

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.time_management.load_best_timer import perf_counter
from cengal.time_management.timer import Timer
from functools import partial
from typing import Optional, Tuple, Union


class Sleep(TypedService[float]):
    def __init__(self, loop: CoroScheduler):
        super(Sleep, self).__init__(loop)
        self.timer = Timer()
        self.pending_tasks_number = 0

    def single_task_registration_or_immediate_processing(
            self, delay: float) -> Tuple[bool, None, None]:
        def timer_handler_func(coro_id: CoroID, start_time: float):
            current_time = perf_counter()
            if start_time > current_time:
                start_time = current_time
            real_delay = current_time - start_time
            self.task_triggered()
            self.register_response(coro_id, real_delay, None)

        handler = partial(timer_handler_func, self.current_caller_coro_info.coro_id, perf_counter())
        self.task_added()
        self.timer.register(handler, delay)
        self.make_live()
        return False, None, None

    def full_processing_iteration(self):
        self.timer()
        if 0 == self.pending_tasks_number:
            self.make_dead()

    def task_added(self):
        self.pending_tasks_number += 1

    def task_triggered(self):
        self.pending_tasks_number -= 1

    def in_work(self) -> bool:
        result: bool = self.pending_tasks_number != 0
        return self.thrifty_in_work(result)
    
    def time_left_before_next_event(self) -> Tuple[bool, Optional[Union[int, float]]]:
        return True, self.timer.nearest_event()
