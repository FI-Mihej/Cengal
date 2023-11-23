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
    'ServiceWithADirectRequestMixin', 
    'put_request_to_service_with_context', 
    'try_put_request_to_service_with_context', 
    'make_request_to_service_with_context', 
    'try_make_request_to_service_with_context', 
    'amake_request_to_service_with_context', 
    'atry_make_request_to_service_with_context', 
    'make_request_to_service', 
    'try_make_request_to_service', 
    'amake_request_to_service', 
    'atry_make_request_to_service'
]


from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.introspection.inspect import get_exception
from cengal.code_flow_control.smart_values import ValueExistence
from typing import Tuple, List, Optional, Any, Union, cast, Type

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


class ServiceWithADirectRequestMixin:
    def _add_direct_request(self, *args, **kwargs) -> ValueExistence:
        raise NotImplementedError


def put_request_to_service_with_context(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], service_type: Type[ServiceWithADirectRequestMixin], *args, **kwargs) -> ValueExistence:
    loop, interface, coro_alive = context
    if loop is None:
        raise CoroSchedulerContextIsNotAvailable

    # Outside the loop or in the service
    service: ServiceWithADirectRequestMixin = loop.get_service_instance(service_type)
    return service._add_direct_request(*args, **kwargs)


def try_put_request_to_service_with_context(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], service_type: Type[ServiceWithADirectRequestMixin], *args, **kwargs) -> ValueExistence:
    loop, interface, coro_alive = context
    if loop is None:
        return None

    # Outside the loop or in the service
    service: ServiceWithADirectRequestMixin = loop.get_service_instance(service_type)
    return service._add_direct_request(*args, **kwargs)


def make_request_to_service_with_context(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], service_type: Type[ServiceWithADirectRequestMixin], *args, **kwargs) -> ValueExistence:
    loop, interface, coro_alive = context
    if loop is None:
        raise CoroSchedulerContextIsNotAvailable

    if coro_alive and isinstance(interface, InterfaceGreenlet):
        # In greenlet coroutine
        return ValueExistence(True, interface(service_type, *args, **kwargs))
    else:
        # Outside the loop or in the service
        service: ServiceWithADirectRequestMixin = loop.get_service_instance(service_type)
        return service._add_direct_request(*args, **kwargs)


def try_make_request_to_service_with_context(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], service_type: Type[ServiceWithADirectRequestMixin], *args, **kwargs) -> ValueExistence:
    loop, interface, coro_alive = context
    if loop is None:
        return None

    if coro_alive and isinstance(interface, InterfaceGreenlet):
        # In greenlet coroutine
        return ValueExistence(True, interface(service_type, *args, **kwargs))
    else:
        # Outside the loop or in the service
        service: ServiceWithADirectRequestMixin = loop.get_service_instance(service_type)
        return service._add_direct_request(*args, **kwargs)


async def amake_request_to_service_with_context(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], service_type: Type[ServiceWithADirectRequestMixin], *args, **kwargs) -> ValueExistence:
    loop, interface, coro_alive = context
    if loop is None:
        raise CoroSchedulerContextIsNotAvailable

    if coro_alive and isinstance(interface, InterfaceAsyncAwait):
        # In awaitable coroutine
        return ValueExistence(True, await interface(service_type, *args, **kwargs))
    else:
        # Outside the loop or in the service
        service: ServiceWithADirectRequestMixin = loop.get_service_instance(service_type)
        return service._add_direct_request(*args, **kwargs)


async def atry_make_request_to_service_with_context(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], service_type: Type[ServiceWithADirectRequestMixin], *args, **kwargs) -> ValueExistence:
    loop, interface, coro_alive = context
    if loop is None:
        return None

    if coro_alive and isinstance(interface, InterfaceAsyncAwait):
        # In awaitable coroutine
        return ValueExistence(True, await interface(service_type, *args, **kwargs))
    else:
        # Outside the loop or in the service
        service: ServiceWithADirectRequestMixin = loop.get_service_instance(service_type)
        return service._add_direct_request(*args, **kwargs)


def make_request_to_service(service_type: Type[ServiceWithADirectRequestMixin], *args, **kwargs) -> ValueExistence:
    return make_request_to_service_with_context(get_interface_and_loop_with_backup_loop(), service_type, *args, **kwargs)


def try_make_request_to_service(service_type: Type[ServiceWithADirectRequestMixin], *args, **kwargs) -> ValueExistence:
    return try_make_request_to_service_with_context(get_interface_and_loop_with_backup_loop(), service_type, *args, **kwargs)


async def amake_request_to_service(service_type: Type[ServiceWithADirectRequestMixin], *args, **kwargs) -> ValueExistence:
    return await amake_request_to_service_with_context(get_interface_and_loop_with_backup_loop(), service_type, *args, **kwargs)


async def atry_make_request_to_service(service_type: Type[ServiceWithADirectRequestMixin], *args, **kwargs) -> ValueExistence:
    return await atry_make_request_to_service_with_context(get_interface_and_loop_with_backup_loop(), service_type, *args, **kwargs)
