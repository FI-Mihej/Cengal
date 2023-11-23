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
    'EventBus', 'EventBusRequest', 'EventID', 'Handler'
]


from enum import Enum
from typing import Dict, Set, List, Tuple, Union, Type, Optional, Any
from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import *
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import *
from cengal.time_management.repeat_for_a_time import Tracer
from cengal.code_flow_control.smart_values.versions.v_1 import ValueExistence


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


EventID = str
Handler = Callable[[EventID, Any], None]


class EventBusRequest(ServiceRequest):
    def register_handler(self, event: EventID, handler: Handler) -> None:
        return self._save(0, event, handler)

    def remove_handler(self, event: EventID, handler: Handler) -> None:
        return self._save(1, event, handler)

    def send_event(self, event: EventID, data: Any) -> None:
        return self._save(2, event, data)

    def set_priority(self, priority: CoroPriority) -> None:
        return self._save(3, priority)


class EventBus(Service, EntityStatsMixin):
    def __init__(self, loop: CoroScheduler):
        super(EventBus, self).__init__(loop)

        self._request_workers = {
            0: self._on_register_handler,
            1: self._on_remove_handler,
            2: self._on_send_event,
            3: self._on_set_priority,
        }

        self.handlers: Dict[EventID, Set[Handler]] = dict()
        self.events: Dict[EventID, List[Any]] = dict()
        self.priority: CoroPriority = CoroPriority.low
        self._in_processing: bool = False

    def get_entity_stats(self, stats_level: 'EntityStatsMixin.StatsLevel' = EntityStatsMixin.StatsLevel.debug) -> Tuple[str, Dict[str, Any]]:
        if EntityStatsMixin.StatsLevel.info == stats_level:
            func_info = full_func_info_to_printable_dict
        else:
            func_info = full_func_info_to_dict

        handlers_set: Set = set()
        for handlers in self.handlers.values():
            handlers_set += handlers
            
        return type(self).__name__, {
            'priority': str(self.priority),
            'events': {
                'num': len(self.events),
                'list': set(self.events)
            },
            'handlers': {
                'num': len(handlers_set),
                'list': [func_info(handler) for handler in handlers_set]
            }
        }

    def single_task_registration_or_immediate_processing(self, request: Optional[EventBusRequest]=None
                                                         ) -> Tuple[bool, Any, None]:
        if request is not None:
            return self.resolve_request(request)
        return True, None, None

    def full_processing_iteration(self):
        if self._in_processing:
            return

        handlers_buff = self.handlers
        self.handlers = type(handlers_buff)()

        events_buff = self.events
        self.events = type(events_buff)()

        interested_events: Set[EventID] = handlers_buff.keys() & events_buff.keys()
        if interested_events:
            async def event_processing_coro(interface: Interface,
                                    interested_events: Set[EventID],
                                    events: Dict[EventID, List[Any]],
                                    handlers: Dict[EventID, Set[Handler]],
                                    priority: CoroPriority
                                    ):
                loop: CoroScheduler = interface._loop
                current_coro_interface_buff: Interface = loop.current_coro_interface
                ly = await agly(priority)
                for event in interested_events:
                    event_data_list = events[event]
                    for data in event_data_list:
                        event_handlers = handlers[event]
                        for handler in event_handlers:
                            try:
                                loop.current_coro_interface = None
                                handler(event, data)
                            except:
                                loop.logger.exception('EventBus. Event handler error')
                            finally:
                                loop.current_coro_interface = current_coro_interface_buff
                            
                            await ly()

            coro: CoroWrapperBase = self._loop.put_coro(event_processing_coro,
                                       interested_events, events_buff, handlers_buff,
                                       self.priority)
            # coro.is_background_coro = True  # must not be background coro: it is not an endless coro
            coro.add_on_coro_del_handler(self._on_coro_del_handler)
            self._in_processing = True
        
        self.make_dead()

    def _on_register_handler(self, event: EventID, handler: Handler):
        if event not in self.handlers:
            self.handlers[event] = set()

        self.handlers[event].add(handler)
        self.make_live()
        return True, None, None

    def _on_remove_handler(self, event: EventID, handler: Handler):
        if event in self.handlers:
            self.handlers[event].remove(handler)

        return True, None, None

    def _on_send_event(self, event: EventID, data: Any):
        if event not in self.events:
            self.events[event] = list()

            self.events[event].append(data)
        
        self.make_live()
        return True, None, None

    def _on_set_priority(self, priority: CoroPriority):
        self.priority = priority

        return True, None, None

    def in_work(self):
        result = (not self._in_processing) & bool(self.handlers) & bool(self.events)
        return self.thrifty_in_work(result)

    def _on_coro_del_handler(self, coro: CoroWrapperBase) -> bool:
        self._in_processing = False
        if bool(self.handlers) & bool(self.events):
            self.make_live()
        
        return False


EventBusRequest.default_service_type = EventBus


def try_send_event(
        backup_scheduler: Optional[CoroScheduler],
        event: EventID, data: Any):
    def event_sender(
            interface: Interface,
            event: EventID, data: Any):
        interface(EventBus, EventBusRequest().send_event(event, data))

    try_put_coro_to(get_interface_and_loop_with_explicit_loop(backup_scheduler), CoroType.auto, event_sender, event, data)
