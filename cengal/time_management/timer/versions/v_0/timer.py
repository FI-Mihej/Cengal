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


from time import perf_counter
from cengal.math.numbers import RationalNumber
from typing import Any, Callable, Optional, Set

TimerHandler = Callable
TimeInSeconds = RationalNumber


class TimerRequest:
    def __init__(self, timer_handler: TimerHandler, desired_time: TimeInSeconds):
        self.timer_handler = timer_handler
        self.requested_time = desired_time
        self.start_time = perf_counter()
        self.real_end_time = None
        self.processed = False

    def __call__(self) -> bool:
        if not self.processed:
            current_time = perf_counter()
            if self.start_time > current_time:
                self.start_time = current_time
            time_delta = current_time - self.start_time
            if time_delta >= self.requested_time:
                self.timer_handler()
                self.processed = True
        return self.processed

    def time_left(self) -> Optional[TimeInSeconds]:
        if self.processed:
            return None

        current_time = perf_counter()
        if self.start_time > current_time:
            self.start_time = current_time
        time_delta = current_time - self.start_time
        if time_delta >= self.requested_time:
            return 0
        else:
            return self.requested_time - time_delta


class Timer:
    # TODO: improve algorithm using `cengal\time_management\repeat_for_a_time` module
    def __init__(self):
        self.requests: Set[TimerRequest] = set()  # type: Set[TimerRequest]

    def register(self, timer_handler: TimerHandler, desired_time: TimeInSeconds) -> TimerRequest:
        request = TimerRequest(timer_handler, desired_time)
        self.requests.add(request)
        return request

    def discard(self, timer_request: TimerRequest):
        try:
            self.requests.remove(timer_request)
            return True
        except KeyError:
            return False

    def __call__(self):
        # processed_requests = set()
        # current_requests = self.requests
        # for request in current_requests:
        #     if request():
        #         processed_requests.add(request)

        # if processed_requests:
        #     self.requests -= processed_requests

        # requests_buff = self.requests
        # self.requests = type(requests_buff)()
        # for request in requests_buff:
        #     if not request():
        #         self.requests.add(request)

        requests_buff = self.requests
        self.requests = set()
        processed_requests = set()
        try:
            for request in requests_buff:
                request_result: bool = True
                try:
                    request_result = request()
                finally:
                    if request_result:
                        processed_requests.add(request)
        finally:
            if processed_requests:
                requests_buff -= processed_requests

            if self.requests:
                requests_buff.update(self.requests)

            self.requests = requests_buff

    def nearest_event(self) -> Optional[TimeInSeconds]:
        nearest_event_time = None
        for request in self.requests:
            time_left = request.time_left()
            if time_left is None:
                continue

            if 0 == time_left:
                return 0

            if (nearest_event_time is None) or (nearest_event_time > time_left):
                nearest_event_time = time_left

        return nearest_event_time
