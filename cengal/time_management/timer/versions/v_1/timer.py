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


__all__ = ['TimerHandler', 'TimeInSeconds', 'TimerRequest', 'Timer']


from cengal.time_management.cpu_clock import cpu_clock
from cengal.math.numbers import RationalNumber
from cengal.data_generation.id_generator import IDGenerator, GeneratorType
from collections import deque
from bisect import bisect_left
from typing import Any, Callable, Optional, Set, Dict, Tuple, List, Deque

TimerHandler = Callable
TimeInSeconds = RationalNumber
RequestId = int


class TimerRequest:
    def __init__(self, id: RequestId, timer_handler: TimerHandler, desired_time: TimeInSeconds):
        self.request_id: RequestId = id
        self.timer_handler = timer_handler
        self.requested_time = desired_time
        self.start_time = cpu_clock()
        self.real_end_time = None
        self.processed = False

    def __call__(self, current_time = None) -> bool:
        if not self.processed:
            if current_time is None: current_time = cpu_clock()
            if self.start_time > current_time:
                self.start_time = current_time
            time_delta = current_time - self.start_time
            if time_delta >= self.requested_time:
                self.timer_handler()
                self.processed = True
        
        return self.processed

    def time_left(self, current_time = None) -> Optional[TimeInSeconds]:
        if self.processed:
            return None

        if current_time is None: current_time = cpu_clock()
        if self.start_time > current_time:
            self.start_time = current_time
        time_delta = current_time - self.start_time
        if time_delta >= self.requested_time:
            return 0
        else:
            return self.requested_time - time_delta


class Timer:
    # TODO: (old todo) improve algorithm using `cengal\time_management\repeat_for_a_time` module
    def __init__(self):
        self.request_id_generator: IDGenerator = IDGenerator(GeneratorType.integer)
        self.requests_dict: Dict[RequestId, TimerRequest] = dict()
        self.requests_order: Deque[Tuple[RequestId, TimeInSeconds]] = deque()
        self.times_left_order: Deque[TimeInSeconds] = deque()
        self.last_time: Optional[TimeInSeconds] = None

    def register(self, timer_handler: TimerHandler, desired_time: TimeInSeconds) -> TimerRequest:
        request_id = self.request_id_generator()
        request = TimerRequest(request_id, timer_handler, desired_time)
        self.requests_dict[request_id] = request
        if self.requests_order:
            self._fast_update_requests_order(request_id, desired_time)
        else:
            self._init_requests_order(request_id, desired_time)
        
        return request
    
    def _init_requests_order(self, request_id, desired_time):
        current_time = cpu_clock()
        self.last_time = current_time
        self.requests_order.append((request_id, desired_time))
        self.times_left_order.append(desired_time)
    
    def _fast_update_requests_order(self, request_id: RequestId, desired_time: TimeInSeconds):
        current_time: TimeInSeconds = cpu_clock()
        time_left: TimeInSeconds = desired_time + (current_time - self.last_time)
        if self.requests_order[0][1] >= time_left:
            self.requests_order.appendleft((request_id, time_left))
            self.times_left_order.appendleft(time_left)
        elif self.requests_order[-1][1] <= time_left:
            self.requests_order.append((request_id, time_left))
            self.times_left_order.append(time_left)
        else:
            insert_pos: int = bisect_left(self.times_left_order, time_left)
            self.requests_order.insert(insert_pos, (request_id, time_left))
            self.times_left_order.insert(insert_pos, time_left)
    
    # Not needed anymore since much slower
    def _update_requests_order(self):
        current_time = cpu_clock()
        self.last_time = current_time
        requests_times_left = ((request.request_id, request.time_left(current_time)) for request in self.requests_dict.values())
        self.requests_order = deque((request_and_time_left for request_and_time_left in sorted(requests_times_left, key=lambda request_and_time_left: request_and_time_left[1])))
        self.times_left_order = deque((time_left for _, time_left in self.requests_order))

    def discard(self, timer_request: TimerRequest):
        try:
            del self.requests_dict[timer_request.request_id]
            return True
        except KeyError:
            return False

    def __call__(self, current_time = None):
        if current_time is None: current_time = cpu_clock()
        time_spend = current_time - self.last_time
        need_to_process_num: int = 0
        for _, time_left in self.requests_order:
            if time_left > time_spend:
                break
            
            need_to_process_num += 1
        
        if need_to_process_num:
            need_to_process: List[TimerRequest] = list()
            for _ in range(need_to_process_num):
                need_to_process.append(self.requests_dict.pop(self.requests_order.popleft()[0]))
            
            for request in need_to_process:
                request()

    def nearest_event(self, current_time = None) -> Optional[TimeInSeconds]:
        if current_time is None: current_time = cpu_clock()
        if not self.requests_order:
            return None
        
        nearest_event_time = self.requests_order[0][1] - (current_time - self.last_time)
        if nearest_event_time >= 0:
            return nearest_event_time
        else:
            return 0
