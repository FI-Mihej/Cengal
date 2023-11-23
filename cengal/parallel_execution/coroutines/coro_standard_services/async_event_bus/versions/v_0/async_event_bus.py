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
    'AsyncEventBus', 'AsyncEventBusRequest', 'EventID', 'Handler', 'try_send_async_event'
]


import sys
from enum import Enum
from typing import Dict, Set, List, Tuple, Union, Type, Optional, Any, Deque
from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import *
from cengal.parallel_execution.coroutines.coro_standard_services.event_bus import EventID, Handler
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import *
from cengal.code_flow_control.smart_values.versions.v_1 import ValueExistence
from cengal.introspection.inspect import get_exception
from cengal.time_management.repeat_for_a_time import Tracer
from collections import deque


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


class AsyncEventBusRequest(ServiceRequest):
    def register_handler(self, event: EventID, handler: Handler) -> None:
        return self._save(0, event, handler)

    def remove_handler(self, event: EventID, handler: Handler) -> None:
        return self._save(1, event, handler)

    def send_event(self, event: EventID, data: Any,
                   priority: Optional[CoroPriority]=CoroPriority.low) -> None:
        return self._save(2, event, data, priority)

    def wait(self, event: EventID) -> Any:
        """
        Will block coroutine untill result is ready
        :param event:
        :return: event data
        """
        return self._save(3, event)


class AsyncEventBus(Service, EntityStatsMixin):
    def __init__(self, loop: CoroScheduler):
        super(AsyncEventBus, self).__init__(loop)

        self._request_workers = {
            0: self._on_register_handler,
            1: self._on_remove_handler,
            2: self._on_send_event,
            3: self._on_wait,
        }

        self.waiters: Dict[EventID, Set[CoroID]] = dict()
        self.events_by_waiter: Dict[CoroID, Set[Any]] = dict()
        self.handlers: Dict[EventID, Set[Handler]] = dict()
        self.events: Dict[CoroPriority, Dict[EventID, Deque[Any]]] = {
            CoroPriority.low: dict(),
            CoroPriority.normal: dict(),
            CoroPriority.high: dict()
        }
        self.priority_sequence = [
            CoroPriority.high,
            CoroPriority.normal,
            CoroPriority.low
        ]

    def get_entity_stats(self, stats_level: 'EntityStatsMixin.StatsLevel' = EntityStatsMixin.StatsLevel.debug) -> Tuple[str, Dict[str, Any]]:
        if EntityStatsMixin.StatsLevel.info == stats_level:
            func_info = full_func_info_to_printable_dict
        else:
            func_info = full_func_info_to_dict

        coroutines_set: Set = set()
        for coroutines in self.waiters.values():
            coroutines_set.update(coroutines)

        handlers_set: Set = set()
        for handlers in self.handlers.values():
            handlers_set.update(handlers)
            
        return type(self).__name__, {
            'events': {
                'low priority': {
                    'num': len(self.events[CoroPriority.low]),
                    'list': set(self.events[CoroPriority.low])
                },
                'normal priority': {
                    'num': len(self.events[CoroPriority.normal]),
                    'list': set(self.events[CoroPriority.normal])
                },
                'high priority': {
                    'num': len(self.events[CoroPriority.high]),
                    'list': set(self.events[CoroPriority.high])
                },
            },
            'waiting coroutines': {
                'num': len(coroutines_set),
                'list': coroutines_set,
            },
            'handlers': {
                'num': len(handlers_set),
                'list': [func_info(handler) for handler in handlers_set]
            }
        }

    def single_task_registration_or_immediate_processing(self, request: Optional[AsyncEventBusRequest]=None
                                                         ) -> Tuple[bool, Any, None]:
        if request is not None:
            return self.resolve_request(request)
        return True, None, None

    def full_processing_iteration(self):
        handlers = self.handlers
        waiters = self.waiters
        for priority in self.priority_sequence:
            priority_events = self.events[priority]
            if not priority_events:
                continue
            else:
                interested_events = waiters.keys() & priority_events.keys()
                for event in interested_events:
                    event_data_list: Deque = priority_events[event]
                    for i in range(len(event_data_list)):
                        event_waiters = waiters.pop(event, None)
                        if event_waiters is None:
                            break
                        else:
                            for waiter in event_waiters:
                                waiter_events = self.events_by_waiter.get(waiter, None)
                                if waiter_events:
                                    if event in waiter_events:
                                        waiter_events.remove(event)
                                        self.register_response(waiter, event_data_list.popleft())
                
                    if not event_data_list:
                        del priority_events[event]

                interested_events = handlers.keys() & priority_events.keys()
            
            if interested_events:
                processed_priority_events = set()
                handlers_info_list = list()
                for event in interested_events:
                    event_data_list = priority_events[event]
                    processed_priority_events.add(event)
                    for data in event_data_list:
                        event_handlers = handlers.get(event, None)
                        if event_handlers:
                            for handler in event_handlers:
                                handlers_info_list.append((handler, event, data))

                async def event_processing_coro(
                    interface: Interface,
                    handlers_info_list: List[Tuple[(Handler, EventID, Any)]],
                    priority: CoroPriority,
                ):
                    loop: CoroScheduler = interface._loop
                    current_coro_interface_buff: Interface = loop.current_coro_interface
                    ly = await agly(priority)
                    for handler, event, data in handlers_info_list:
                        try:
                            loop.current_coro_interface = None
                            handler(event, data)
                        except:
                            loop.logger.exception('AsyncEventBus. Event handler error')
                        finally:
                            loop.current_coro_interface = current_coro_interface_buff

                        await ly()

                try:
                    coro: CoroWrapperBase = self._loop.put_coro(
                        event_processing_coro,
                        handlers_info_list,
                        priority,
                    )
                    # coro.is_background_coro = True  # must not be background coro: it is not an endless coro
                except:
                    ex_type, exception, tracback = sys.exc_info()
                    raise
                finally:
                    for processed_event in processed_priority_events:
                        del priority_events[processed_event]

        self.make_dead()

    def _on_register_handler(self, event: EventID, handler: Handler):
        if event not in self.handlers:
            self.handlers[event] = set()

        self.handlers[event].add(handler)
        self.make_live()
        return True, None, None

    def _on_remove_handler(self, event: EventID, handler: Handler):
        if event in self.handlers:
            self.handlers[event].discard(handler)
            if not self.handlers[event]:
                del self.handlers[event]

        return True, None, None

    def _on_send_event(self, event: EventID, data: Any, priority: Optional[CoroPriority]=CoroPriority.low):
        events_of_priority = self.events[priority]
        if event not in events_of_priority:
            events_of_priority[event] = deque()

        events_of_priority[event].append(data)
        self.make_live()

        return True, None, None

    def _on_wait(self, event: EventID):
        requester_id = self.current_caller_coro_info.coro_id
        requester = self.current_caller_coro_info.coro
        requester.add_on_coro_del_handler(self._on_coro_del_handler)
        if event not in self.waiters:
            self.waiters[event] = set()

        if requester_id not in self.events_by_waiter:
            self.events_by_waiter[requester_id] = set()

        self.waiters[event].add(requester_id)
        self.events_by_waiter[requester_id].add(event)
        return (False, None, None)

    def _on_coro_del_handler(self, coro: CoroWrapperBase) -> bool:
        coro_id = coro.coro_id
        if coro_id in self.events_by_waiter:
            events = self.events_by_waiter[coro_id]
            for event in events:
                if event in self.waiters:
                    if coro_id in self.waiters[event]:
                        self.waiters[event].remove(coro_id)

            del self.events_by_waiter[coro_id]
        
        return False

    def in_work(self):
        result: bool = bool(self.waiters) | bool(self.handlers)
        for priority in self.priority_sequence:
            result |= bool(self.events[priority])
        
        return self.thrifty_in_work(result)


AsyncEventBusRequest.default_service_type = AsyncEventBus


def try_send_async_event(
        backup_scheduler: Optional[CoroScheduler],
        event: EventID, data: Any, priority: Optional[CoroPriority]=CoroPriority.low):
    def event_sender(
            interface: Interface,
            event: EventID, data: Any, priority: Optional[CoroPriority]=CoroPriority.low):
        interface(AsyncEventBus, AsyncEventBusRequest().send_event(event, data, priority))

    try_put_coro_to(get_interface_and_loop_with_explicit_loop(backup_scheduler), event_sender, event, data, priority)
