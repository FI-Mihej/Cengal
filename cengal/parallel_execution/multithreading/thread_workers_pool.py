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


from cengal.introspection.inspect import get_exception
from typing import Callable, Any, Optional, Tuple, List, Dict, Type
from enum import Enum
import queue
import threading
import sys


ExceptionInfo = Tuple


class RequestToThread:
    class Command(Enum):
        request = 0
        shut_down = 1

    def __init__(self, command_type: 'Command', request: Any):
        self.command_type = command_type
        self.request = request


class ResponseFromThread:
    def __init__(self, has_response: bool, response: Any, exception: Optional[ExceptionInfo] = None):
        self.has_response = has_response  # type: bool
        self.response = response          # type: Any
        self.exception = exception        # type: Optional[ExceptionInfo]


ThreadWorker = Callable[[RequestToThread], ResponseFromThread]
TypeOfThreadWorker = Type[ThreadWorker]


class ServiceThread(threading.Thread):
    def __init__(self, worker_type: TypeOfThreadWorker):
        super(ServiceThread, self).__init__(daemon=True)
        self.requests = queue.Queue()  # type: queue.Queue
        self.results = queue.Queue()   # type: queue.Queue
        self.worker = worker_type()    # type: ThreadWorker

    def run(self):
        shut_down = False
        while not shut_down:
            request: RequestToThread = self.requests.get()

            if RequestToThread.Command.shut_down == request.command_type:
                shut_down = True

            try:
                response = self.worker(request)
            except:
                response = ResponseFromThread(False, None, get_exception())

            self.results.put(response)
            self.requests.task_done()

    def put(self, request: RequestToThread):
        self.requests.put(request)

    def put_nowait(self, request: RequestToThread):
        self.requests.put_nowait(request)

    def get(self) -> Any:
        response: ResponseFromThread = self.results.get()
        self.results.task_done()
        if response.has_response:
            return response.response
        elif response.exception is not None:
            raise response.exception[1]
        else:
            raise RuntimeError

    def get_nowait(self) -> Any:
        response: ResponseFromThread = self.results.get_nowait()
        self.results.task_done()
        if response.has_response:
            return response.response
        elif response.exception is not None:
            raise response.exception[1]
        else:
            raise RuntimeError


class ServiceThreadPool:
    def __init__(self, worker_type: TypeOfThreadWorker, number_of_threads: int = 1):
        self.worker_type = worker_type
        self.number_of_threads = number_of_threads
        if self.number_of_threads < 1:
            self.number_of_threads = 1
        self.threads = list()                 # type: List[ServiceThread]
        self.thread_pending_results = dict()  # type: Dict[ServiceThread, int]
        self.pending_requests_queue = list()  # type: List[RequestToThread]
        self._init()

    def put_synchronous(self, request: RequestToThread):
        thread: ServiceThread = self._get_best_thread()
        thread.put(request)
        self.thread_pending_results[thread] += 1

    def put_into_pending_queue(self, request: RequestToThread):
        self.pending_requests_queue.append(request)

    def put_pending_queue_into_work(self):
        buff_pending_requests_queue = self.pending_requests_queue
        self.pending_requests_queue = type(self.pending_requests_queue)()
        for pending_request in buff_pending_requests_queue:
            if not self._put_impl(pending_request):
                self.pending_requests_queue.append(pending_request)

    def get_results(self) -> List[Any]:
        responses: List[Any] = list()
        for thread, pending_responses in self.thread_pending_results.items():
            if pending_responses:
                try:
                    while True:
                        responses.append(thread.get_nowait())
                        self.thread_pending_results[thread] -= 1
                except queue.Empty:
                    pass
        return responses

    def stop(self) -> List[Any]:
        for thread in self.threads:
            thread.put(RequestToThread(RequestToThread.Command.shut_down, None))
        for thread in self.threads:
            thread.join()
        return self.get_results()

    def _init(self):
        for index in range(self.number_of_threads):
            self.threads.append(ServiceThread(self.worker_type))
        for thread in self.threads:
            self.thread_pending_results[thread] = 0
            thread.start()

    def _get_best_thread(self) -> ServiceThread:
        thread_load: Dict = dict()
        thread_index = -1
        for thread in self.threads:
            thread: ServiceThread = thread
            thread_index += 1
            thread_load[thread_index] = thread.requests.unfinished_tasks
        sorted_by_value = sorted(thread_load.items(), key=lambda kv: kv[1])
        return self.threads[sorted_by_value[0][0]]

    def _get_threads_list(self) -> List[Tuple[int, ServiceThread]]:
        thread_load: Dict = dict()
        thread_index = -1
        for thread in self.threads:
            thread: ServiceThread = thread
            thread_index += 1
            thread_load[thread_index] = thread.requests.unfinished_tasks
        sorted_by_value = sorted(thread_load.items(), key=lambda kv: kv[1])
        return sorted_by_value

    def _put_impl(self, request: RequestToThread) -> bool:
        is_ok = False
        for thread_index, thread_qsize in self._get_threads_list():
            try:
                thread = self.threads[thread_index]
                thread.put_nowait(request)
                self.thread_pending_results[thread] += 1
                is_ok = True
                break
            except queue.Full:
                pass
        return is_ok
