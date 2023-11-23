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


__all__ = ['LazyPrint', 'lazy_print', 'lprint', 'lp']


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""


from time import perf_counter
from typing import Dict, List, Tuple

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.timer_func_runner import TimerFuncRunner, add_timer_func_run_from_other_service, discard_timer_func_run_from_other_service

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


class LazyPrint(TypedService[None]):
    def __init__(self, loop):
        super().__init__(loop)
        self.requests = list()
        self.update_period = 1 / 60
        self.update_timer_request = None

    def single_task_registration_or_immediate_processing(self, *args, **kwargs) -> Tuple[(bool, None, None)]:
        self.requests.append((args, kwargs))
        self.try_add_timer()
        return (True, None, None)

    def full_processing_iteration(self):
        requests_buff = self.requests
        self.requests = type(self.requests)()
        for args, kwargs in requests_buff:
            kwargs['flush'] = False
            print(*args, **kwargs)

        print(end='', flush=True)
        self.add_timer()
        self.make_dead()

    def timer_handler(self):
        self.update_timer_request = None
        if self.in_work_impl():
            self.make_live()
    
    def add_timer(self):
        self.update_timer_request = add_timer_func_run_from_other_service(self, True, self.update_period, self.timer_handler)
    
    def try_add_timer(self):
        if self.update_timer_request is None: self.add_timer()

    def _put_direct_request(self, *args, **kwargs):
        self.requests.append((args, kwargs))
        self.try_add_timer()

    def in_work_impl(self) -> bool:
        return bool(self.requests)

    def in_work(self) -> bool:
        result: bool = self.in_work_impl()
        return self.thrifty_in_work(result)
    
    def destroy(self):
        try:
            discard_timer_func_run_from_other_service(self, self.update_timer_request)
        except CoroSchedulerIsCurrentlyDestroingError:
            pass


def lazy_print(*args, **kwargs):
    fallback = False
    try:
        cs = current_coro_scheduler()
        if cs._destroyed:
            fallback = True
    except OutsideCoroSchedulerContext:
        fallback = True

    if fallback:
        fallback = False
        try:
            cs: CoroScheduler = primary_coro_scheduler()
            if cs._destroyed:
                fallback = True
        except PrimaryCoroSchedulerWasNotSet:
            fallback = True

    if fallback:
        fallback = False
        print(*args, **kwargs)
    else:
        cs.get_service_instance(LazyPrint)._put_direct_request(*args, **kwargs)


lprint = lazy_print
lp = lazy_print
