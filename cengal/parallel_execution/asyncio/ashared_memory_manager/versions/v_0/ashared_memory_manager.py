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


__all__ = [
    'ASharedMemoryContextManager',
    'ASMCM',
    'ASharedMemoryManager',
    'ASMM',
]


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.hardware.memory.shared_memory import *
from cengal.parallel_execution.asyncio.atasks import create_task_awaitable
from cengal.time_management.sleep_tools import get_usable_min_sleep_interval
from cengal.code_flow_control.smart_values import ValueHolder

import asyncio
from typing import Any, Coroutine


class ASharedMemoryContextManager:
    def __init__(self, ashared_memory_management: 'ASharedMemoryManager', if_has_messages: Optional[bool] = None):
        self.ashared_memory_management: 'ASharedMemoryManager' = ashared_memory_management
        self._if_has_messages_original_value: Optional[bool] = if_has_messages
        self._if_has_messages_value: Optional[bool] = None
        self.if_has_messages_value = if_has_messages
        self.shared_memory: SharedMemory = self.ashared_memory_management.shared_memory
        self.shared_memory_holder: ValueHolder[SharedMemory] = ValueHolder(True, self.shared_memory)
        self.client_iteration_done: asyncio.Future = None
        self._entered: bool = False

    async def __aenter__(self) -> ValueHolder[SharedMemory]:
        self._entered = True
        if self.if_has_messages_value:
            await self.ashared_memory_management.has_messages()
        
        line_ready: asyncio.Future = self.ashared_memory_management.get_in_line()
        self.client_iteration_done = await line_ready
        self.shared_memory_holder.existence = True
        return self.shared_memory_holder
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.client_iteration_done.set_result(bool(self.shared_memory_holder))
        self.client_iteration_done = None
        self.if_has_messages_value = self._if_has_messages_original_value
        self._entered = False

    @property
    def save_cpu_time(self):
        return self.ashared_memory_management.save_cpu_time
    
    @save_cpu_time.setter
    def save_cpu_time(self, value: bool):
        self.ashared_memory_management.save_cpu_time = value
    
    @property
    def if_has_messages_value(self) -> Optional[bool]:
        return self._if_has_messages_value
    
    @if_has_messages_value.setter
    def if_has_messages_value(self, value: Optional[bool]):
        self._if_has_messages_value = False if value is None else value
    
    @property
    def _loop(self):
        return self.ashared_memory_management._loop
    
    def close(self) -> Optional[asyncio.Future]:
        return self.ashared_memory_management.close()
    
    async def aclose(self):
        await self.ashared_memory_management.aclose()
    
    async def has_messages(self):
        if self._entered:
            raise RuntimeError('You cannot wait for `has_messages()` while inside the context manager. This could cause the program to hang, as it might prevent other processes from taking their turn and adding new messages.')
        
        return await self.ashared_memory_management.has_messages()
    
    def if_has_messages(self, value: bool = True):
        self.if_has_messages_value = value
        return self
    
    def anyway(self):
        self.if_has_messages_value = False
        return self


ASMCM = ASharedMemoryContextManager


class ASharedMemoryManager:
    def __init__(self, shared_memory: SharedMemory, save_cpu_time: bool = False, time_limit: Optional[RationalNumber] = None):
        self.shared_memory: SharedMemory = shared_memory
        self._save_cpu_time: bool = None
        self._asleep_func: Coroutine = None
        self.save_cpu_time = save_cpu_time
        self.time_limit: Optional[RationalNumber] = time_limit
        self._loop: asyncio.AbstractEventLoop = None
        self.requests_from_clients: List[asyncio.Future] = list()
        self.clients_readyness: List[asyncio.Future] = list()
        self.closed: bool = False
        self.close_requested: bool = False
        self.close_requests: List[asyncio.Future] = list()
        self.has_messages_requests: List[asyncio.Future] = list()
        self.worker_task: asyncio.Task = None
    
    async def __aenter__(self) -> 'ASharedMemoryManager':
        self.closed = False
        self.run()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.aclose()

    async def _sleep_till_next_loop_iteration(self):
        await asyncio.sleep(0)
        mm_pause()
    
    async def _sleep_for_minimal_time(self):
        await asyncio.sleep(get_usable_min_sleep_interval())
        mm_pause()
    
    @property
    def save_cpu_time(self) -> bool:
        return self._save_cpu_time
    
    @save_cpu_time.setter
    def save_cpu_time(self, value: bool):
        self._save_cpu_time = value
        if value:
            self.shared_memory._asleep_func = self._asleep_func = self._sleep_for_minimal_time
        else:
            self.shared_memory._asleep_func = self._asleep_func = self._sleep_till_next_loop_iteration

    async def aclose(self) -> None:
        if self.closed:
            return
        
        self.close_requested = True
        close_request = self._loop.create_future()
        self.close_requests.append(close_request)
        await close_request

    def close(self) -> Optional[asyncio.Future]:
        if self.closed:
            return None

        self.close_requested = True
        close_request = self._loop.create_future()
        self.close_requests.append(close_request)
        return close_request
    
    def run(self):
        if self.worker_task:
            return
        
        self._loop = asyncio.get_event_loop()
        self.worker_task = create_task_awaitable(self.worker())
    
    def get_in_line(self) -> asyncio.Future:
        get_in_line_future = self._loop.create_future()
        self.requests_from_clients.append(get_in_line_future)
        return get_in_line_future

    async def has_messages(self):
        has_messages_future = self._loop.create_future()
        self.has_messages_requests.append(has_messages_future)
        return await has_messages_future
    
    def __call__(self, if_has_messages: Optional[bool] = None) -> ASharedMemoryContextManager:
        return ASharedMemoryContextManager(self, if_has_messages)
    
    async def worker(self):
        try:
            async with self.shared_memory:
                if self.shared_memory.create:
                    await self.shared_memory.await_consumer_ready(self.time_limit)
                else:
                    await self.shared_memory.ainit_consumer(self.time_limit)
                
                while not self.close_requested:
                    if self.requests_from_clients or self.has_messages_requests:
                        if self.shared_memory.get_in_line():
                            try:
                                if self.shared_memory.has_messages():
                                    has_messages_requests_buff = self.has_messages_requests
                                    self.has_messages_requests = list()
                                    for has_messages_request in has_messages_requests_buff:
                                        has_messages_request.set_result(True)
                                
                                requests_from_clients_buff = self.requests_from_clients
                                self.requests_from_clients = list()
                                for request_from_client in requests_from_clients_buff:
                                    client_ready_future = self._loop.create_future()
                                    request_from_client.set_result(client_ready_future)
                                    self.clients_readyness.append(client_ready_future)
                                
                                client_results = await asyncio.gather(*self.clients_readyness, return_exceptions=True)
                                self.clients_readyness.clear()
                            finally:
                                self.shared_memory.release()
                            
                            if any(client_results):
                                await asyncio.sleep(0)
                            else:
                                await asyncio.sleep(get_usable_min_sleep_interval())
                    else:
                        await self._asleep_func()
        finally:
            self.closed = True
            for close_request in self.close_requests:
                close_request.set_result(None)
            
            self.close_requests.clear()
            self.close_requested = False
            self.worker_task = None


ASMM = ASharedMemoryManager
