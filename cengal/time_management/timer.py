from time import perf_counter
from typing import Callable, Set, Any


TimerHandler = Callable
TimeInSeconds = float


class TimerRequest:
    def __init__(self, timer_handler: TimerHandler, desired_time: TimeInSeconds):
        self.timer_handler = timer_handler
        self.requested_time = desired_time
        self.start_time = perf_counter()
        self.real_end_time = None
        self.processed = False

    def __call__(self)->bool:
        if not self.processed:
            current_time = perf_counter()
            if self.start_time > current_time:
                self.start_time = current_time
            time_delta = current_time - self.start_time
            if time_delta >= self.requested_time:
                self.timer_handler()
                self.processed = True
        return self.processed


class Timer:
    def __init__(self):
        self.requests = set()  # type: Set[TimerRequest]

    def register(self, timer_handler: TimerHandler, desired_time: TimeInSeconds):
        self.requests.add(TimerRequest(timer_handler, desired_time))

    def __call__(self):
        pending_requests = set()
        current_requests = self.requests
        self.requests = set()
        for request in current_requests:
            if not request():
                pending_requests.add(request)
        self.requests |= pending_requests
