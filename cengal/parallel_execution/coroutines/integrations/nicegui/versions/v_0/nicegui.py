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


__all__ = ['ClientHandlers', 'PageItems', 'nicegui_page_sync_coro', 'sync_like_page', 
           'sl_page', 'nicegui_page_async_coro', 'async_page', 'apage',
           'nicegui_page_class_async_coro', 'async_page_class', 'apage_class', 
           'nicegui_event_handler_func_async_coro', 'async_event_handler_func', 
           'aevent_handler_func', 'nicegui_event_handler_method_async_coro', 
           'async_event_handler_method', 'aevent_handler_method', 'PageContextBase', 
           'run']


import asyncio


class CurrentTask:
    def __init__(self, original) -> None:
        self.original = original
        self.new = original

    def patch(self, new):
        self.new = new

    def restore(self):
        self.new = self.original

    def __call__(self, *args, **kwds):
        return self.new(*args, **kwds)


current_task = CurrentTask(asyncio.current_task)
asyncio.current_task = current_task


from cengal.parallel_execution.coroutines.integrations.uvloop import uvloop_install
uvloop_install()


from cengal.parallel_execution.asyncio.init_loop import init_loop
init_loop()


if True:
    # increasing max decode packets to be able to transfer images
    # see https://github.com/miguelgrinberg/python-engineio/issues/142
    from engineio.payload import Payload
    Payload.max_decode_packets = 500


import inspect
from time import perf_counter
from typing import Set, Tuple, Optional, Union, Dict, Callable, Any, Hashable, cast, List, Coroutine
import warnings
from cengal.parallel_execution.asyncio.atasks import create_task
from cengal.parallel_execution.coroutines.coro_scheduler import Interface, AnyWorker, cs_acoro
from cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus import (AsyncEventBus,
                                                                                         AsyncEventBusRequest)
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro, put_coro_to
from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro, arun_coro_fast, run_coro_fast
from cengal.parallel_execution.coroutines.coro_standard_services.db import Db, DbRequest, EnvId, EnvInfo
from cengal.parallel_execution.coroutines.coro_standard_services.simple_yield import Yield
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import AsyncioLoop, AsyncioLoopRequest
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_loop import ShutdownLoop
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_on_keyboard_interrupt import ShutdownOnKeyboardInterrupt
from cengal.parallel_execution.coroutines.coro_standard_services.simple_yield import Yield
from cengal.parallel_execution.coroutines.coro_standard_services.instance import Instance, InstanceRequest, afast_wait, fast_get_explicit, fast_set_explicit
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import agly_patched
from cengal.parallel_execution.coroutines.coro_standard_services.log import LogRequest
from cengal.parallel_execution.coroutines.coro_tools.await_coro import await_coro_prim
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import (arun_in_fast_loop, arun_in_loop, run_in_loop)
from cengal.parallel_execution.coroutines.coro_tools.lock import Lock
from cengal.code_flow_control.args_manager import args_kwargs, EntityArgsHolder, EntityArgsHolderExplicit
from cengal.io.serve_free_ports import simple_port_search
from uuid import uuid4
from inspect import signature, Signature, isclass
from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.data_manipulation.conversion.reinterpret_cast import \
    reinterpret_cast
from cengal.parallel_execution.coroutines.coro_scheduler import (
    CoroWrapperAsyncAwait, Interface)
from cengal.parallel_execution.coroutines.coro_tools.await_coro import \
    await_coro_prim
from cengal.parallel_execution.coroutines.coro_tools.wait_coro import sync_coro_param
from cengal.parallel_execution.asyncio.atasks import create_task


from nicegui import app, ui, Client
# from nicegui.binding import loop
# agly_patched(loop)
from cengal.parallel_execution.asyncio.timed_yield import TimedYield
import nicegui.binding
original__propagate = nicegui.binding.propagate
class PropagateMock:
    def __init__(self) -> None:
        self.ty: TimedYield = TimedYield(0.01)
    
    def __call__(self, source_obj: Any, source_name: str, visited: Optional[Set[Tuple[int, str]]] = None) -> None:
        return original__propagate(source_obj, source_name, visited)


nicegui.binding.propagate = PropagateMock()
from nicegui.events import handle_event, GenericEventArguments, UiEventArguments
from nicegui.dataclasses import KWONLY_SLOTS
from nicegui.slot import Slot
from nicegui.globals import slot_stacks
from fastapi import Request as FastAPIRequest
from .text_translation import setup_translation, create_translatable_text_element, TextTranslator, \
    TranslationLanguageMapper, TranslationLanguageChooser, TranslatableTextElement, TTE, NiceguiTranslatableTextElement, NTTE
from cengal.parallel_execution.coroutines.coro_tools.await_coro import asyncio_coro
from cengal.file_system.app_fs_structure.app_dir_path import AppDirPath, AppDirectoryType
from cengal.file_system.path_manager import RelativePath
from cengal.web_tools.detect_browsers_host_device_type.by_http_headers import ClientViewType, client_view_type
from cengal.web_tools.detect_browsers_language.by_http_headers import parse_accept_language, optimize_accept_language, match_langs, normalize_lang
from cengal.math.numbers import RationalNumber
from cengal.base.exceptions import CengalError
from cengal.introspection.inspect import entity_name, entity_repr
from functools import partial
from collections import OrderedDict
from datetime import datetime, timedelta
from starlette.datastructures import Address, URL
from starlette.responses import Response, RedirectResponse
from aioipinfo import IPInfoClient, IPInfoError, IPInfoResponse
from dataclasses import dataclass
from contextlib import nullcontext
import os
import hashlib
import logging


DESTROY_CS_EVENT = f'DESTROY_CS_EVENT__{uuid4()}'
CS_PREPARED_FLAG = f'CS_PREPARED_FLAG'
CS_DESTROY_TIMEOUT = 3.0


text_translator: TextTranslator = None
translation_language_mapper: TranslationLanguageMapper = None
session_clients: Dict[Hashable, Set[Hashable]] = dict()
translatable_text_element_per_session: Dict[Hashable, NiceguiTranslatableTextElement] = dict()
translatable_text_element_per_client: Dict[Hashable, NiceguiTranslatableTextElement] = dict()

known_translation_param_names: Set[str] = {'_t', '_T', '__'}
known_page_context_param_names: Set[str] = {'page_context', 'pc', 'self'}
db_env_id: EnvId = 'cengal_nicegui_db_env'
db_request__logged_in_clients: DbRequest = DbRequest(db_env_id, 'logged_in_clients')
db_request__user_clients: DbRequest = DbRequest(db_env_id, 'user_clients')
db_request__logged_in_sessions: DbRequest = DbRequest(db_env_id, 'logged_in_sessions')
db_request__user_sessions: DbRequest = DbRequest(db_env_id, 'user_sessions')
db_request__ip_geolocation: DbRequest = DbRequest(db_env_id, 'ip_geolocation')
db_request__user_sign_in_info: DbRequest = DbRequest(db_env_id, 'user_sign_in_info')
db_request__credentials_by_user_id: DbRequest = DbRequest(db_env_id, 'credentials_by_user_id')
db_request__user_sign_up_info: DbRequest = DbRequest(db_env_id, 'user_sign_up_info')
signed_in_session_timeout: timedelta = timedelta(days=90)
ipinfo_io_token: str = os.environ.get('CENGAL_NICEGUI__IPINFO_IO_TOKEN', None)


class CengalNiceguiException(CengalError):
    pass


class UserNotFoundError(CengalNiceguiException):
    pass


class PasswordIsNotCorrectError(CengalNiceguiException):
    pass


class CoroWrapperNiceGuiPageAsyncAwait(CoroWrapperAsyncAwait):
    def reinit_for_nicegui(self):
        self.subtype = self._setup_subtype()
        self._current_call_method = self._call_method  # type: Callable
        self.original__current_task = None

    def mock__current_task(self, loop=None):
        return self.current_asyncio_task

    def patch_asyncio_current_task(self):
        current_task.patch(self.mock__current_task)

    def unpatch_asyncio_current_task(self):
        current_task.restore()

    def _init_coroutine(self, *init_args, **init_kwargs):
        try:
            self.patch_asyncio_current_task()
            return super()._init_coroutine(*init_args, **init_kwargs)
        finally:
            self.unpatch_asyncio_current_task()

    def _call_coroutine(self, *args, **kwargs):
        try:
            self.patch_asyncio_current_task()
            return super()._call_coroutine(*args, **kwargs)
        finally:
            self.unpatch_asyncio_current_task()

    def _throw_coroutine(self, ex_type, ex_value=None, ex_traceback=None):
        try:
            self.patch_asyncio_current_task()
            return super()._throw_coroutine(ex_type, ex_value, ex_traceback)
        finally:
            self.unpatch_asyncio_current_task()

    def _close_coroutine(self, *args, **kwargs):
        try:
            self.patch_asyncio_current_task()
            return super()._close_coroutine(*args, **kwargs)
        finally:
            self.unpatch_asyncio_current_task()


class CoroWrapperNiceGuiPageGreenlet(CoroWrapperGreenlet):
    def reinit_for_nicegui(self):
        self.subtype = self._setup_subtype()
        self._current_call_method = self._call_method  # type: Callable
        self.original__current_task = None

    def mock__current_task(self, loop=None):
        return self.current_asyncio_task

    def patch_asyncio_current_task(self):
        current_task.patch(self.mock__current_task)

    def unpatch_asyncio_current_task(self):
        current_task.restore()

    def _init_coroutine(self, *init_args, **init_kwargs):
        try:
            self.patch_asyncio_current_task()
            return super()._init_coroutine(*init_args, **init_kwargs)
        finally:
            self.unpatch_asyncio_current_task()

    def _call_coroutine(self, *args, **kwargs):
        try:
            self.patch_asyncio_current_task()
            return super()._call_coroutine(*args, **kwargs)
        finally:
            self.unpatch_asyncio_current_task()

    def _throw_coroutine(self, ex_type, ex_value=None, ex_traceback=None):
        try:
            self.patch_asyncio_current_task()
            return super()._throw_coroutine(ex_type, ex_value, ex_traceback)
        finally:
            self.unpatch_asyncio_current_task()

    def _close_coroutine(self, *args, **kwargs):
        try:
            self.patch_asyncio_current_task()
            return super()._close_coroutine(*args, **kwargs)
        finally:
            self.unpatch_asyncio_current_task()


class ClientHandlers:
    def __init__(self, client: Optional[Client]) -> None:
        self.client: Optional[Client] = client
        self.on_connected_handlers: Set[Callable] = set()
        self.on_disconnected_handlers: Set[Callable] = set()
        self.is_connected: bool = False
        self.is_disconnected: bool = False
    
    @classmethod
    def check_args_factory(cls, signature: Signature, args, kwargs) -> Optional['ClientHandlers']:
        client: Optional[Client] = kwargs.get('client', None)
        if (client is None) or (not isinstance(client, Client)):
            return None
        else:
            return cls.install(client)
    
    @classmethod
    def install(cls, client: Client) -> 'ClientHandlers':
        client_handlers: ClientHandlers = cls(client)
        client.handlers = client_handlers
        client.on_connect(client_handlers._on_connected())
        client.on_disconnect(client_handlers._on_disconnected())
        return client_handlers
    
    def add_on_connected_handler(self, handler: Callable):
        if self.is_connected:
            handler()
        else:
            self.on_connected_handlers.add(handler)
    
    def remove_on_connected_handler(self, handler: Callable):
        self.on_connected_handlers.discard(handler)
    
    async def _on_connected(self):
        on_connected_handlers_buff = tuple(self.on_connected_handlers)
        self.on_connected_handlers = set()
        for index, handler in enumerate(on_connected_handlers_buff):
            try:
                handler()
            except:
                self.on_connected_handlers.update(on_connected_handlers_buff[index + 1:])
                create_task(self._on_connected)
                raise
    
    def add_on_disconnected_handler(self, handler: Callable):
        if self.is_disconnected:
            handler()
        else:
            self.on_disconnected_handlers.add(handler)
    
    def remove_on_disconnected_handler(self, handler: Callable):
        self.on_disconnected_handlers.discard(handler)
    
    async def _on_disconnected(self):
        on_disconnected_handlers_buff = tuple(self.on_disconnected_handlers)
        self.on_disconnected_handlers = set()
        for index, handler in enumerate(on_disconnected_handlers_buff):
            try:
                handler()
            except:
                self.on_disconnected_handlers.update(on_disconnected_handlers_buff[index + 1:])
                create_task(self._on_disconnected)
                raise


class PageItems:
    def __init__(self, client: Optional[Client]) -> None:
        self.client: Optional[Client] = client
        self.items: Set[Any] = set()
    
    @classmethod
    def check_args_factory(cls, signature: Signature, args, kwargs) -> Optional['PageItems']:
        client: Optional[Client] = kwargs.get('client', None)
        if (client is None) or (not isinstance(client, Client)):
            return None
        else:
            return cls.install(client)
    
    @classmethod
    def install(cls, client: Client) -> 'PageItems':
        page_items: PageItems = cls(client)
        client.page_items = page_items
        return page_items
    
    def add(self, item: Any):
        self.items.add(item)
    
    def remove(self, item: Any):
        self.items.discard(item)
    
    def __call__(self, item: Any) -> Any:
        return self.add(item)


async def get_ip_geolocation(ipinfo_io_token, host):
    async with IPInfoClient(ipinfo_io_token) as client:
        try:
            ip_geolocation = await client.ipinfo_dict(host)
            if ip_geolocation is not None:
                await i(db_request__ip_geolocation.put(host))
        except IPInfoError:
            ip_geolocation = None
        
        return ip_geolocation


def nicegui_event_handler_func_async_coro(coro_worker: Worker):
    """Decorator. Without arguments. Makes a proper, fully functional async Page from any decorated Cengal coroutine

    Args:
        coro_worker (Worker): _description_

    Raises:
        TypeError: _description_

    Returns:
        _type_: _description_
    """    
    coro_worker_0 = coro_worker
    # async def wrapper(*args, **kwargs):
    async def wrapper(*args, **kwargs):
        await await_cs_initiated()
        coro_worker = coro_worker_0
        app.cs.logger.debug(f'nicegui_event_handler_async_coro.wrapper - start: {entity_name(coro_worker)}')
        coro_worker_type: CoroType = find_coro_type(coro_worker)
        if CoroType.awaitable == coro_worker_type:
            async def awaitable_coro_wrapper(i: Interface, current_asyncio_task, 
                                             coro_worker_with_args: EntityArgsHolderExplicit):
                coro_worker, args, kwargs = coro_worker_with_args.entity_args_kwargs()
                i.log.debug(f'nicegui_event_handler_async_coro.wrapper.awaitable_coro_wrapper - start: {entity_name(coro_worker)}')
                await apretent_to_be_asyncio_coro(i, current_asyncio_task)
                # await i(Instance, InstanceRequest().wait(CS_PREPARED_FLAG))
                i.log.debug(f'nicegui_event_handler_async_coro.wrapper.awaitable_coro_wrapper - ready: {entity_name(coro_worker)}')
                return await coro_worker(i, *args, **kwargs)
            
            coro_wrapper = awaitable_coro_wrapper
        elif CoroType.greenlet == coro_worker_type:
            def greenlet_coro_wrapper(i: Interface, current_asyncio_task, 
                                      coro_worker_with_args: EntityArgsHolderExplicit):
                coro_worker, args, kwargs = coro_worker_with_args.entity_args_kwargs()
                i.log.debug(f'nicegui_event_handler_async_coro.wrapper.greenlet_coro_wrapper - start: {entity_name(coro_worker)}')
                pretent_to_be_asyncio_coro(i, current_asyncio_task)
                # i(Instance, InstanceRequest().wait(CS_PREPARED_FLAG))
                i.log.debug(f'nicegui_event_handler_async_coro.wrapper.greenlet_coro_wrapper - ready: {entity_name(coro_worker)}')
                return coro_worker(i, *args, **kwargs)
            
            coro_wrapper = greenlet_coro_wrapper
        else:
            raise TypeError(f'{coro_worker} is neither an awaitable nor a greenlet')

        current_asyncio_task = asyncio.current_task()
        return await await_coro_prim(coro_wrapper, current_asyncio_task, 
                                     EntityArgsHolderExplicit(coro_worker, args, kwargs))
        
    coro_worker_sign: Signature = signature(coro_worker)
    wrapper_signature = coro_worker_sign.replace(parameters=tuple(coro_worker_sign.parameters.values())[1:], return_annotation=coro_worker_sign.return_annotation)
    wrapper.__signature__ = wrapper_signature
    
    return wrapper


async_event_handler_func = nicegui_event_handler_func_async_coro
aevent_handler_func = nicegui_event_handler_func_async_coro


def nicegui_event_handler_method_async_coro(coro_worker: Worker):
    """Decorator. Without arguments. Makes a proper, fully functional async Page from any decorated Cengal coroutine

    Args:
        coro_worker (Worker): _description_

    Raises:
        TypeError: _description_

    Returns:
        _type_: _description_
    """    
    coro_worker_0 = coro_worker
    # async def wrapper(*args, **kwargs):
    async def wrapper(self, *args, **kwargs):
        await await_cs_initiated()
        coro_worker = coro_worker_0
        coro_worker_name: str = coro_worker.__name__
        unwrapped_coro_worker_name: str = f'_unwrapped_method__{coro_worker_name}'
        if not hasattr(self, unwrapped_coro_worker_name):
            bound_coro_worker = coro_worker.__get__(self, self.__class__)
            setattr(self, unwrapped_coro_worker_name, bound_coro_worker)

        coro_worker = getattr(self, unwrapped_coro_worker_name)
        app.cs.logger.debug(f'nicegui_event_handler_async_coro.wrapper - start: {entity_name(coro_worker)}')
        coro_worker_type: CoroType = find_coro_type(coro_worker)
        if CoroType.awaitable == coro_worker_type:
            async def awaitable_coro_wrapper(i: Interface, current_asyncio_task, 
                                             coro_worker_with_args: EntityArgsHolderExplicit):
                coro_worker, args, kwargs = coro_worker_with_args.entity_args_kwargs()
                i.log.debug(f'nicegui_event_handler_async_coro.wrapper.awaitable_coro_wrapper - start: {entity_name(coro_worker)}')
                await apretent_to_be_asyncio_coro(i, current_asyncio_task)
                # await i(Instance, InstanceRequest().wait(CS_PREPARED_FLAG))
                i.log.debug(f'nicegui_event_handler_async_coro.wrapper.awaitable_coro_wrapper - ready: {entity_name(coro_worker)}')
                i.log.debug(f'{entity_repr(coro_worker)}')
                return await coro_worker(i, *args, **kwargs)
            
            coro_wrapper = awaitable_coro_wrapper
        elif CoroType.greenlet == coro_worker_type:
            def greenlet_coro_wrapper(i: Interface, current_asyncio_task, 
                                      coro_worker_with_args: EntityArgsHolderExplicit):
                coro_worker, args, kwargs = coro_worker_with_args.entity_args_kwargs()
                i.log.debug(f'nicegui_event_handler_async_coro.wrapper.greenlet_coro_wrapper - start: {entity_name(coro_worker)}')
                pretent_to_be_asyncio_coro(i, current_asyncio_task)
                # i(Instance, InstanceRequest().wait(CS_PREPARED_FLAG))
                i.log.debug(f'nicegui_event_handler_async_coro.wrapper.greenlet_coro_wrapper - ready: {entity_name(coro_worker)}')
                return coro_worker(i, *args, **kwargs)
            
            coro_wrapper = greenlet_coro_wrapper
        else:
            raise TypeError(f'{coro_worker} is neither an awaitable nor a greenlet')

        current_asyncio_task = asyncio.current_task()
        return await await_coro_prim(coro_wrapper, current_asyncio_task, 
                                     EntityArgsHolderExplicit(coro_worker, args, kwargs))
        
    coro_worker_sign: Signature = signature(coro_worker)
    new_parameters = list(coro_worker_sign.parameters.values())
    del new_parameters[1]
    wrapper_signature = coro_worker_sign.replace(parameters=tuple(new_parameters), return_annotation=coro_worker_sign.return_annotation)
    wrapper.__signature__ = wrapper_signature
    
    return wrapper


async_event_handler_method = nicegui_event_handler_method_async_coro
aevent_handler_method = nicegui_event_handler_method_async_coro


def get_task_slot_stack(task_id) -> List[Slot]:
    if task_id not in slot_stacks:
        slot_stacks[task_id] = []
    return slot_stacks[task_id]


class FakeElementForEvents:
    def __init__(self, task_id) -> None:
        self.is_ignoring_events: bool = False
        self.parent_slot: Union[Slot, nullcontext] = nullcontext()
        slot_stack = get_task_slot_stack(task_id)
        if slot_stack:
            self.parent_slot = slot_stack[-1]


@dataclass(**KWONLY_SLOTS)
class OnSignInEventArguments(UiEventArguments):
    user_id: Hashable
    user_sign_in_info: Union[Dict, Tuple, List]


@dataclass(**KWONLY_SLOTS)
class OnSignOutEventArguments(UiEventArguments):
    user_id: Hashable


class PageContextBase:
    def __init__(self, client: Client, request: FastAPIRequest, _t: NTTE, current_asyncio_task) -> None:
        self.client: Client = client
        self.request: FastAPIRequest = request
        self.client_host_port: Address = self.request.client
        self.client_id: Hashable = client.id
        self.session_id: Hashable = client.session_id
        self.user_id: Hashable = None
        self._t: NTTE = _t
        self.current_asyncio_task = current_asyncio_task
        self.current_asyncio_task_id = id(current_asyncio_task)
        self.client_view_type: ClientViewType = self._determine_client_view_type()
        self.better_lang: str = None
        self.featured_langs: OrderedDict[str, RationalNumber] = None
        self.langs: OrderedDict[str, RationalNumber] = None
        self.better_lang, self.featured_langs, self.langs = self._determine_client_languages()
        self._t.text_translation_language_chooser.lang = self.better_lang
    
    def _init(self, i: Interface):
        self.register_session_page(i)
        i(PutCoro, self._arequest_ip_geolocation, self.client_host_port[0])
        if self._find_user(i):
            i.log.debug(f'{self.session_id}, {self.client_id}: logged in')
        else:
            i.log.debug(f'{self.session_id}, {self.client_id}: logged out')
    
    async def _ainit(self, i: Interface):
        self.register_session_page(i)
        await i(PutCoro, self._arequest_ip_geolocation, self.client_host_port[0])
        if await self._afind_user(i):
            i.log.debug(f'{self.session_id}, {self.client_id}: logged in')
        else:
            i.log.debug(f'{self.session_id}, {self.client_id}: logged out')
    
    async def _arequest_ip_geolocation(self, i: Interface, host: str):
        ip_geolocation: Optional[Dict] = None
        need_to_request: bool = True
        try:
            ip_geolocation = await i(db_request__ip_geolocation.get(host))
            need_to_request = False
        except KeyError:
            pass

        if need_to_request:
            ip_geolocation = await i(AsyncioLoop, AsyncioLoopRequest().wait(get_ip_geolocation(ipinfo_io_token, host)))
        
        await self.on_ip_geolocation_ready(i, ip_geolocation)
    
    def register_session_page(self, i: Interface):
        session_pages: Dict[Hashable, Set[PageContextBase]] = fast_get_explicit(i, 'cengal_nicegui__session_pages')
        if self.session_id not in session_pages:
            session_pages[self.session_id] = set()
        
        session_pages[self.session_id].add(self)
    
    def _determine_client_view_type(self) -> ClientViewType:
        return client_view_type(self.request.headers)
    
    def _determine_client_languages(self):
        parsed_accept_language: Optional[OrderedDict[str, RationalNumber]] = optimize_accept_language(parse_accept_language(self.request.headers))
        translation_data: Dict = self._t.text_translator.decoded_data
        return match_langs(
                translation_data['default_language'], 
                set(translation_data['featured_languages']),
                set(translation_data['supported_languages']),
                translation_data['translation_language_map'],
                parsed_accept_language,
            )
    
    def _find_user(self, i: Interface) -> bool:
        if self.session_id is None:
            return False
        
        try:
            user_id, sign_in_date_time = i(db_request__logged_in_sessions.get(self.session_id))
            sign_in_date_time = datetime.fromisoformat(sign_in_date_time)
            if (datetime.now() - sign_in_date_time) > signed_in_session_timeout:
                i(db_request__logged_in_sessions.delete(self.session_id))
                return False
            
            self.user_id = user_id
            return True
        except KeyError:
            return False
    
    async def _afind_user(self, i: Interface) -> bool:
        if self.session_id is None:
            return False
        
        try:
            user_id, sign_in_date_time = await i(db_request__logged_in_sessions.get(self.session_id))
            sign_in_date_time = datetime.fromisoformat(sign_in_date_time)
            if (datetime.now() - sign_in_date_time) > signed_in_session_timeout:
                await i(db_request__logged_in_sessions.delete(self.session_id))
                return False
            
            self.user_id = user_id
            return True
        except KeyError:
            return False
    
    # def find_user(self, i: Interface, client_connection_check_interval: RationalNumber = 0.01) -> bool:
    #     if not self.client.has_socket_connection:
    #         if not self.client.is_waiting_for_connection:
    #             i(AsyncioLoop, AsyncioLoopRequest().wait(self.client.connected()))
        
    #     while self.client.is_waiting_for_connection:
    #         i(Sleep, client_connection_check_interval)
        
    #     return self._find_user(i)
    
    # async def afind_user(self, i: Interface, client_connection_check_interval: RationalNumber = 0.01) -> bool:
    #     if not self.client.has_socket_connection:
    #         if not self.client.is_waiting_for_connection:
    #             await i(AsyncioLoop, AsyncioLoopRequest().wait(self.client.connected()))
        
    #     while self.client.is_waiting_for_connection:
    #         await i(Sleep, client_connection_check_interval)
        
    #     return await self._afind_user(i)
    
    def try_sign_in(self, i: Interface, credentials: Union[Dict, Tuple, List, str, bytes, int, float]) -> Optional[Union[Dict, Tuple, List]]:
        user_data: Union[Dict, Tuple, List] = None

        try:
            user_data = i(db_request__user_sign_in_info.get(credentials))
        except KeyError:
            pass
        
        if user_data is None:
            return None
        
        user_id = user_data[0]
        if self.session_id is None:
            i(db_request__logged_in_clients.put(self.client_id, (user_id, datetime.now())))
            user_clients_lock: Lock = fast_get_explicit(i, 'cengal_nicegui__user_clients_lock')
            with user_clients_lock:
                try:
                    user_clients: Set[Hashable] = set(i(db_request__user_clients.get(user_id)))
                except KeyError:
                    user_clients = set()
                
                user_clients.add(self.client_id)
                i(db_request__user_sessions.put(user_id, user_clients))
            
            i(PutCoro, self._on_signed_in, user_id)
        else:
            i(db_request__logged_in_sessions.put(self.session_id, (user_id, datetime.now())))
            user_sessions_lock: Lock = fast_get_explicit(i, 'cengal_nicegui__user_sessions_lock')
            with user_sessions_lock:
                try:
                    user_sessions: Set[Hashable] = set(i(db_request__user_sessions.get(user_id)))
                except KeyError:
                    user_sessions = set()
                
                user_sessions.add(self.session_id)
                i(db_request__user_sessions.put(user_id, user_sessions))
            
            session_pages: Dict[Hashable, Set[PageContextBase]] = fast_get_explicit(i, 'cengal_nicegui__session_pages')
            current_session_pages: Set[PageContextBase] = session_pages.get(self.session_id, set())
            for session_page in current_session_pages:
                i(PutCoro, session_page._on_signed_in, user_id, user_data)
        
        return user_data
    
    async def atry_sign_in(self, i: Interface, credentials: Union[Dict, Tuple, List, str, bytes, int, float]) -> Optional[Union[Dict, Tuple, List]]:
        user_data: Union[Dict, Tuple, List] = None

        try:
            user_data = await i(db_request__user_sign_in_info.get(credentials))
        except KeyError:
            pass
        
        if user_data is None:
            return None
        
        user_id = user_data[0]
        if self.session_id is None:
            await i(db_request__logged_in_clients.put(self.client_id, (user_id, datetime.now())))
            user_clients_lock: Lock = fast_get_explicit(i, 'cengal_nicegui__user_clients_lock')
            async with user_clients_lock:
                try:
                    user_clients: Set[Hashable] = set(await i(db_request__user_clients.get(user_id)))
                except KeyError:
                    user_clients = set()
                
                user_clients.add(self.client_id)
                await i(db_request__user_sessions.put(user_id, user_clients))
            
            await i(PutCoro, self._on_signed_in, user_id)
        else:
            await i(db_request__logged_in_sessions.put(self.session_id, (user_id, datetime.now())))
            user_sessions_lock: Lock = fast_get_explicit(i, 'cengal_nicegui__user_sessions_lock')
            async with user_sessions_lock:
                try:
                    user_sessions: Set[Hashable] = set(await i(db_request__user_sessions.get(user_id)))
                except KeyError:
                    user_sessions = set()
                
                user_sessions.add(self.session_id)
                await i(db_request__user_sessions.put(user_id, user_sessions))
            
            session_pages: Dict[Hashable, Set[PageContextBase]] = fast_get_explicit(i, 'cengal_nicegui__session_pages')
            current_session_pages: Set[PageContextBase] = set(session_pages.get(self.session_id, set()))  # TODO: robust fix needed for `RuntimeError: Set changed size during iteration`
            for session_page in current_session_pages:
                await i(PutCoro, session_page._on_signed_in, user_id, user_data)
        
        return user_data
    
    def user_signed_up(self, i: Interface, credentials: Union[Dict, Tuple, List, str, bytes, int, float],
                              user_sign_in_info: Union[Dict, Tuple, List]):
        i(db_request__user_sign_in_info.put(credentials, user_sign_in_info))
    
    async def auser_signed_up(self, i: Interface, credentials: Union[Dict, Tuple, List, str, bytes, int, float],
                              user_sign_in_info: Union[Dict, Tuple, List]):
        await i(db_request__user_sign_in_info.put(credentials, user_sign_in_info))

    def sign_out(self, i: Interface) -> bool:
        user_id = self.user_id
        if user_id is None:
            return False
        
        if self.session_id is None:
            try:
                i(db_request__logged_in_clients.delete(self.client_id))
            except KeyError:
                pass

            i(PutCoro, self._on_signed_out)
            return True
        else:
            try:
                i(db_request__logged_in_sessions.delete(self.session_id))
            except KeyError:
                pass

            session_pages: Dict[Hashable, Set[PageContextBase]] = fast_get_explicit(i, 'cengal_nicegui__session_pages')
            current_session_pages: Set[PageContextBase] = session_pages.get(self.session_id, set())
            for session_page in current_session_pages:
                i(PutCoro, session_page._on_signed_out)

            return True

    async def asign_out(self, i: Interface) -> bool:
        user_id = self.user_id
        if user_id is None:
            return False
        
        if self.session_id is None:
            try:
                await i(db_request__logged_in_clients.delete(self.client_id))
            except KeyError:
                pass

            user_clients_lock: Lock = fast_get_explicit(i, 'cengal_nicegui__user_clients_lock')
            async with user_clients_lock:
                try:
                    user_clients: Set[Hashable] = set(await i(db_request__user_clients.get(user_id)))
                except KeyError:
                    user_clients = set()
                
                user_clients.discard(self.client_id)
                await i(db_request__user_sessions.put(user_id, user_clients))

            await i(PutCoro, self._on_signed_out)
            return True
        else:
            try:
                await i(db_request__logged_in_sessions.delete(self.session_id))
            except KeyError:
                pass

            user_sessions_lock: Lock = fast_get_explicit(i, 'cengal_nicegui__user_sessions_lock')
            async with user_sessions_lock:
                try:
                    user_sessions: Set[Hashable] = set(await i(db_request__user_sessions.get(user_id)))
                except KeyError:
                    user_sessions = set()
                
                user_sessions.discard(self.session_id)
                await i(db_request__user_sessions.put(user_id, user_sessions))

            session_pages: Dict[Hashable, Set[PageContextBase]] = fast_get_explicit(i, 'cengal_nicegui__session_pages')
            current_session_pages: Set[PageContextBase] = session_pages.get(self.session_id, set())
            for session_page in current_session_pages:
                await i(PutCoro, session_page._on_signed_out)

            return True

    def try_sign_up__login_password(self, i: Interface, login: str, password: str, 
                                    user_sign_in_info_maker: Callable[[Interface, str, Hashable, datetime], Union[Dict, Tuple, List]]) -> bool:
        login_exists: bool = False
        try:
            i(db_request__user_sign_up_info.get(login))
            login_exists = True
        except KeyError:
            pass

        if login_exists:
            return False
        
        password_bytes = password.encode('utf-8')
        salt = os.urandom(16)
        key_length = 64
        N = 16384  # CPU/memory cost factor
        r = 8     # Block size
        p = 1     # Parallelization factor
        dk = hashlib.scrypt(password_bytes, salt=salt, n=N, r=r, p=p, dklen=key_length)
        i(db_request__user_sign_up_info.put(login, (dk, salt, N, r, p, key_length)))
        user_id: Hashable = uuid4()
        credentials: Tuple = (login, dk)
        i(db_request__credentials_by_user_id.put(user_id, credentials))
        user_sign_in_info: Union[Dict, Tuple, List] = run_coro_fast(i, user_sign_in_info_maker, login, user_id, datetime.now())
        self.user_signed_up(i, credentials, user_sign_in_info)
        return True

    async def atry_sign_up__login_password(self, i: Interface, login: str, password: str, 
                                           user_sign_in_info_maker: Callable[[Interface, str, Hashable, datetime], Union[Dict, Tuple, List]]) -> bool:
        login_exists: bool = False
        try:
            await i(db_request__user_sign_up_info.get(login))
            login_exists = True
        except KeyError:
            pass

        if login_exists:
            return False
        
        password_bytes = password.encode('utf-8')
        salt = os.urandom(16)
        key_length = 64
        N = 16384  # CPU/memory cost factor
        r = 8     # Block size
        p = 1     # Parallelization factor
        dk = hashlib.scrypt(password_bytes, salt=salt, n=N, r=r, p=p, dklen=key_length)
        await i(db_request__user_sign_up_info.put(login, (dk, salt, N, r, p, key_length)))
        user_id: Hashable = uuid4().bytes
        credentials: Tuple = (login, dk)
        await i(db_request__credentials_by_user_id.put(user_id, credentials))
        user_sign_in_info: Union[Dict, Tuple, List] = await arun_coro_fast(i, user_sign_in_info_maker, login, user_id, datetime.now())
        await self.auser_signed_up(i, credentials, user_sign_in_info)
        return True

    def try_sign_in__login_password(self, i: Interface, login: str, password: str) -> Union[Dict, Tuple, List]:
        user_found: bool = False
        try:
            dk, salt, N, r, p, key_length = i(db_request__user_sign_up_info.get(login))
            user_found = True
        except KeyError:
            pass

        if not user_found:
            raise UserNotFoundError

        password_bytes = password.encode('utf-8')
        dk_0 = hashlib.scrypt(password_bytes, salt=salt, n=N, r=r, p=p, dklen=key_length)
        if dk != dk_0:
            raise PasswordIsNotCorrectError
        
        credentials: Tuple = (login, dk)
        return self.try_sign_in(i, credentials)

    async def atry_sign_in__login_password(self, i: Interface, login: str, password: str) -> Union[Dict, Tuple, List]:
        user_found: bool = False
        try:
            dk, salt, N, r, p, key_length = await i(db_request__user_sign_up_info.get(login))
            user_found = True
        except KeyError:
            pass

        if not user_found:
            raise UserNotFoundError

        password_bytes = password.encode('utf-8')
        dk_0 = hashlib.scrypt(password_bytes, salt=salt, n=N, r=r, p=p, dklen=key_length)
        if dk != dk_0:
            raise PasswordIsNotCorrectError
        
        credentials: Tuple = (login, dk)
        return await self.atry_sign_in(i, credentials)

    def try_sign_up__email_password(self, i: Interface, email: str, password: str) -> bool:
        raise NotImplementedError

    async def atry_sign_up__email_password(self, i: Interface, email: str, password: str) -> bool:
        raise NotImplementedError

    async def _on_signed_in(self, i: Interface, user_id: Hashable, user_sign_in_info: Union[Dict, Tuple, List]) -> None:
        self.user_id = user_id
        handle_event(self._on_signed_in_impl, OnSignInEventArguments(sender=FakeElementForEvents(self.current_asyncio_task_id), client=self.client, user_id=user_id, user_sign_in_info=user_sign_in_info))

    @aevent_handler_method
    async def _on_signed_in_impl(self, i: Interface, arguments: OnSignInEventArguments) -> None:
        return await self.on_signed_in(i, arguments.user_id, arguments.user_sign_in_info)

    async def on_signed_in(self, i: Interface, user_id: Hashable, user_sign_in_info: Union[Dict, Tuple, List]) -> None:
        pass

    async def _on_signed_out(self, i: Interface) -> None:
        user_id = self.user_id
        self.user_id = None
        handle_event(self._on_signed_out_impl, OnSignOutEventArguments(sender=FakeElementForEvents(self.current_asyncio_task_id), client=self.client, user_id=user_id))

    @aevent_handler_method
    async def _on_signed_out_impl(self, i: Interface, arguments: OnSignOutEventArguments) -> None:
        return await self.on_signed_out(i, arguments.user_id)

    async def on_signed_out(self, i: Interface, user_id: Hashable) -> None:
        pass

    async def on_ip_geolocation_ready(self, i: Interface, ip_geolocation: Optional[Dict]) -> None:
        pass

    def refferer(self) -> Optional[str]:
        return self.request.headers.get('referer', None)

    def url(self) -> URL:
        return self.request.url

    def open_page(self, target: Optional[Union[Callable[..., Any], str]] = None, new_tab: bool = False) -> Optional[RedirectResponse]:
        if target is None:
            return
        
        client = self.client
        if client.has_socket_connection:
            client.open(target, new_tab)
        else:
            return RedirectResponse(target)

    def open_previous_page(self, default_target: Optional[Union[Callable[..., Any], str]] = None, new_tab: bool = False, can_be_current_page: bool = False) -> Optional[RedirectResponse]:
        target: str = self.refferer()
        current_url: str = str(self.url())
        if (target is None) or (False if can_be_current_page else (target == current_url)):
            if not isinstance(default_target, str):
                default_target = globals.page_routes[target]
            
            target = default_target if default_target is not None else '/'
        
        client = self.client
        if client.has_socket_connection:
            client.open(target, new_tab)
        else:
            return self.open_previous_page_http_response(default_target, can_be_current_page)

    def open_previous_page_http_response(self, default_target: Optional[Union[Callable[..., Any], str]] = None, can_be_current_page: bool = False) -> RedirectResponse:
        refferer: str = self.refferer()
        current_url: str = str(self.url())
        if (refferer is None) or (False if can_be_current_page else (refferer == current_url)):
            refferer = default_target if default_target is not None else '/'
        
        return RedirectResponse(refferer)


def nicegui_page_sync_coro(*dargs, **dkwargs):
    """Decorator. With an arguments. Gives ability to execute any decorated Cengal coroutine based page as a sync function.
    Can postpone execution to the actual loop when possible if None as an immediate result (no result) is acceptible.
    Can start own loop if needed. See sync_coro_param() decorator from cengal/parallel_execution/coroutines/coro_tools/wait_coro for more details

    Returns:
        _type_: _description_
    """    
    dargs_0 = dargs
    dkwargs_0 = dkwargs
    def nicegui_page_sync_coro_impl(coro_worker: Worker):
        coro_worker_0 = coro_worker
        dargs_1 = dargs_0
        dkwargs_1 = dkwargs_0
        def wrapper(*args, **kwargs):
            coro_worker = coro_worker_0
            dargs = dargs_1
            dkwargs = dkwargs_1
            sync_coro_decorator = sync_coro_param(*dargs, **dkwargs)
            sync_coro_decorator_wrapper = sync_coro_decorator(coro_worker)
            ClientHandlers.check_args_factory(wrapper_signature, args, kwargs)
            PageItems.check_args_factory(wrapper_signature, args, kwargs)
            return sync_coro_decorator_wrapper(*args, **kwargs)
            
        coro_worker_sign: Signature = signature(coro_worker)
        wrapper_signature = coro_worker_sign.replace(parameters=tuple(coro_worker_sign.parameters.values())[1:], return_annotation=coro_worker_sign.return_annotation)
        wrapper.__signature__ = wrapper_signature
        
        return wrapper
    return nicegui_page_sync_coro_impl


sync_like_page = nicegui_page_sync_coro
sl_page = nicegui_page_sync_coro


async def await_cs_initiated():
    while (not hasattr(app, 'cs_initiated')) or (not app.cs_initiated):
        await asyncio.sleep(0.01)


async def apretent_to_be_asyncio_coro(i: Interface, asyncio_coro):
    reinterpret_cast(CoroWrapperNiceGuiPageAsyncAwait, i._coro)
    i._coro.current_asyncio_task = asyncio_coro
    i._coro.reinit_for_nicegui()
    await i(Yield)


def pretent_to_be_asyncio_coro(i: Interface, asyncio_coro):
    reinterpret_cast(CoroWrapperNiceGuiPageGreenlet, i._coro)
    i._coro.current_asyncio_task = asyncio_coro
    i._coro.reinit_for_nicegui()
    i(Yield)


def nicegui_page_async_coro_impl(page_class: Optional[Union[PageContextBase, EntityArgsHolder]], coro_worker: Worker):
    """Decorator. Without arguments. Makes a proper, fully functional async Page from any decorated Cengal coroutine

    Args:
        coro_worker (Worker): _description_

    Raises:
        TypeError: _description_

    Returns:
        _type_: _description_
    """    
    coro_worker_0 = coro_worker
    page_class_0 = page_class
    # async def wrapper(*args, **kwargs):
    async def wrapper(request: FastAPIRequest, client: Client):
        await await_cs_initiated()
        request.app.cs.logger.debug(f'nicegui_page_async_coro_impl.wrapper - start: {request.url}')
        client_id = client.id
        session_id = request.session.get('id', None)
        client.session_id = session_id
        if session_id not in session_clients:
            session_clients[session_id] = set()
        
        session_clients[session_id].add(client_id)

        if session_id is None:
            translatable_text_element: NiceguiTranslatableTextElement = create_translatable_text_element(text_translator, translation_language_mapper)
            # translatable_text_element: NiceguiTranslatableTextElement = create_translatable_text_element(
            #         await asyncio_coro(cs_acoro(afast_wait))('text_translator'), await asyncio_coro(cs_acoro(afast_wait))('translation_language_mapper')
            #     )
            translatable_text_element_per_client[client_id] = translatable_text_element
        else:
            if session_id in translatable_text_element_per_session:
                translatable_text_element = translatable_text_element_per_session[session_id]
            else:
                translatable_text_element: NiceguiTranslatableTextElement = create_translatable_text_element(text_translator, translation_language_mapper)
                # translatable_text_element: NiceguiTranslatableTextElement = create_translatable_text_element(
                #         await asyncio_coro(cs_acoro(afast_wait))('text_translator'), await asyncio_coro(cs_acoro(afast_wait))('translation_language_mapper')
                #     )
                translatable_text_element_per_session[session_id] = translatable_text_element
        
        client.translatable_text_element = translatable_text_element
        await asyncio_coro(cs_acoro(translatable_text_element.aregister_on_lang_changed_handler))()
        coro_worker = coro_worker_0
        coro_worker_type: CoroType = find_coro_type(coro_worker)
        if CoroType.awaitable == coro_worker_type:
            async def awaitable_coro_wrapper(i: Interface, current_asyncio_task, wrapper_signature, 
                                             coro_worker_with_args: EntityArgsHolderExplicit, page_context: PageContextBase):
                coro_worker, args, kwargs = coro_worker_with_args.entity_args_kwargs()
                i.log.debug(f'awaitable_coro_wrapper - start: {entity_name(coro_worker)}')
                await apretent_to_be_asyncio_coro(i, current_asyncio_task)
                ClientHandlers.check_args_factory(wrapper_signature, args, kwargs)
                PageItems.check_args_factory(wrapper_signature, args, kwargs)
                # await i(Instance, InstanceRequest().wait(CS_PREPARED_FLAG))
                await page_context._ainit(i)
                i.log.debug(f'awaitable_coro_wrapper - ready: {entity_name(coro_worker)}')
                return await coro_worker(i, *args, **kwargs)
            
            coro_wrapper = awaitable_coro_wrapper
        elif CoroType.greenlet == coro_worker_type:
            def greenlet_coro_wrapper(i: Interface, current_asyncio_task, wrapper_signature, 
                                      coro_worker_with_args: EntityArgsHolderExplicit, page_context: PageContextBase):
                coro_worker, args, kwargs = coro_worker_with_args.entity_args_kwargs()
                i.log.debug(f'greenlet_coro_wrapper - start: {entity_name(coro_worker)}')
                pretent_to_be_asyncio_coro(i, current_asyncio_task)
                ClientHandlers.check_args_factory(wrapper_signature, args, kwargs)
                PageItems.check_args_factory(wrapper_signature, args, kwargs)
                # i(Instance, InstanceRequest().wait(CS_PREPARED_FLAG))
                page_context._init(i)
                i.log.debug(f'greenlet_coro_wrapper - ready: {entity_name(coro_worker)}')
                return coro_worker(i, *args, **kwargs)
            
            coro_wrapper = greenlet_coro_wrapper
        else:
            raise TypeError(f'{coro_worker} is neither an awaitable nor a greenlet')

        current_asyncio_task = asyncio.current_task()
        # args_kwargs: Optional[Tuple[Tuple, Dict]] = dict().get('args_kwargs', None)
        # if args_kwargs is None:
        #     args_kwargs = (tuple(), dict())
        
        args = tuple()
        kwargs = dict()
        coro_worker_param_names_set: Set[str] = set(inspect.signature(coro_worker).parameters.keys())
        if 'client' in coro_worker_param_names_set:
            kwargs['client'] = client

        if 'request' in coro_worker_param_names_set:
            kwargs['request'] = request
        
        translation_params: Set[str] = known_translation_param_names & coro_worker_param_names_set
        if translation_params:
            for translation_param in translation_params:
                kwargs[translation_param] = translatable_text_element
        
        page_context_params: Set[str] = known_page_context_param_names & coro_worker_param_names_set
        if page_context_params:
            page_class = page_class_0
            if isclass(page_class):
                if issubclass(page_class, PageContextBase):
                    page_context: PageContextBase = page_class(client, request, translatable_text_element, current_asyncio_task)
                else:
                    raise TypeError(f'{page_class} is not a subclass of PageContextBase')
            elif isinstance(page_class, EntityArgsHolder):
                page_class = cast(EntityArgsHolder, page_class)
                page_class, page_class_own_args, page_class_own_kwargs = page_class.entity_args_kwargs()
                page_class_own_kwargs.update({
                    'client': client,
                    'request': request,
                    '_t': translatable_text_element,
                    'current_asyncio_task': current_asyncio_task,
                })
                page_context = page_class(*page_class_own_args, **page_class_own_kwargs)
            else:
                raise TypeError(f'{page_class} is not a subclass of PageContextBase nor an EntityArgsHolder')

            for page_context_param in page_context_params:
                kwargs[page_context_param] = page_context

        return await await_coro_prim(coro_wrapper, current_asyncio_task, wrapper_signature, 
                                     EntityArgsHolderExplicit(coro_worker, args, kwargs), page_context)
        
    wrapper_sign: Signature = signature(wrapper)
    coro_worker_sign: Signature = signature(coro_worker)
    # wrapper_signature = coro_worker_sign.replace(parameters=tuple(coro_worker_sign.parameters.values())[1:], return_annotation=coro_worker_sign.return_annotation)
    wrapper_signature = coro_worker_sign.replace(parameters=wrapper_sign.parameters.values(), return_annotation=coro_worker_sign.return_annotation)
    wrapper.__signature__ = wrapper_signature
    
    return wrapper


nicegui_page_async_coro = partial(nicegui_page_async_coro_impl, None)


async_page = nicegui_page_async_coro
apage = nicegui_page_async_coro


def nicegui_page_class_async_coro(page_class: Optional[Union[PageContextBase, EntityArgsHolder]] = PageContextBase):
    return partial(nicegui_page_async_coro_impl, page_class)


async_page_class = nicegui_page_class_async_coro
apage_class = nicegui_page_class_async_coro


async def init_cs(is_fast_loop: bool = True, main_coro: AnyWorker = None, app_args_kwargs = None):
    async def coro(i: Interface, main_coro: AnyWorker = None, app_args_kwargs = None):
        set_primary_coro_scheduler(i._loop)
        app.cs = i._loop
        app.cs_initiated = False
        app_name: str = app_args_kwargs[1]['app_name']
        app_name_for_fs: str = app_args_kwargs[1]['app_name_for_fs']
        app_version: str = app_args_kwargs[1]['app_version']
        app_version_str: str = app_args_kwargs[1]['app_version_str']

        await i(Instance, InstanceRequest().set('app_name', app_name))
        await i(Instance, InstanceRequest().set('app_name_for_fs', app_name_for_fs))
        await i(Instance, InstanceRequest().set('app_version', app_version))
        await i(Instance, InstanceRequest().set('app_version_str', app_version_str))

        i.log.setLevel(logging.INFO)
        await i(LogRequest().sync())
        i.log.debug('cengal.nicegui.init_cs - start')
        await i(AsyncioLoop, AsyncioLoopRequest().inherit_surrounding_loop())
        await i(AsyncioLoop, AsyncioLoopRequest().turn_on_loops_intercommunication(True))
        await i(ShutdownOnKeyboardInterrupt)
        await i(Instance, InstanceRequest().set('cengal_nicegui__app', app))
        await i(Instance, InstanceRequest().set('cengal_nicegui__app_args_kwargs', app_args_kwargs))

        db_env_info: EnvInfo = await i(DbRequest().open_db_environment(db_env_id, None, False, max_dbs=20))
        await i(DbRequest(env_id=db_env_id).open_databases({
            'logged_in_clients',
            'user_clients',
            'logged_in_sessions',
            'user_sessions',
            'ip_geolocation',
            'user_sign_in_info',
            'credentials_by_user_id',
            'user_sign_up_info',
        }))
        await i(Instance, InstanceRequest().set('cengal_nicegui__db_env_info', db_env_info))
        await i(Instance, InstanceRequest().set('cengal_nicegui__session_pages', dict()))
        await i(Instance, InstanceRequest().set('cengal_nicegui__user_clients_lock', Lock(f'cengal_nicegui__user_clients_lock__{uuid4()}')))
        await i(Instance, InstanceRequest().set('cengal_nicegui__user_sessions_lock', Lock(f'cengal_nicegui__user_sessions_lock__{uuid4()}')))

        # await init_translation(i, app_args_kwargs)
        if main_coro is not None:
            await i(PutCoro, main_coro, app_args_kwargs)
        
        app.cs_initiated = True
        i.log.debug('cengal.nicegui.init_cs - ready')
        await i(Instance, InstanceRequest().set(CS_PREPARED_FLAG, True))
        try:
            await i(AsyncEventBus, AsyncEventBusRequest().wait(DESTROY_CS_EVENT))
        finally:
            await i(DbRequest().close_db_environment(db_env_id))
            i.log.debug('cengal.nicegui.init_cs - shutting down loop')
            await i(ShutdownLoop)

    if is_fast_loop:
        await arun_in_fast_loop(coro, main_coro, app_args_kwargs)
    else:
        await arun_in_loop(coro, main_coro, app_args_kwargs)


# # Async on_destroy handling is currently (08 Feb 2023) broken in NiceGUI: 
# #     they should await for handlers instead of current tasks creation approach
# async def destroy_cs():
#     async def coro(i: Interface):
#         await i(AsyncEventBus, AsyncEventBusRequest().send_event(DESTROY_CS_EVENT, None))
#         await i(Sleep, CS_DESTROY_TIMEOUT)

#     await await_coro_prim(coro)


# Async on_destroy handling is currently (08 Feb 2023) broken in NiceGUI: 
#     they should await for handlers instead of current tasks creation approach
def destroy_cs():
    cs: CoroScheduler = get_available_coro_scheduler()
    cs_destroy_timeouted: bool = False
    if cs and (not cs._destroyed):
        async def coro(i: Interface):
            await i(AsyncEventBus, AsyncEventBusRequest().send_event(DESTROY_CS_EVENT, None))

        put_coro_to(get_interface_and_loop_with_explicit_loop(cs), coro)
        start_time = perf_counter()
        while cs.iteration():
            if (perf_counter() - start_time) >= CS_DESTROY_TIMEOUT:
                cs_destroy_timeouted = True
                break

    if cs_destroy_timeouted:
        warnings.warn(f'destroy_cs - not finished within timeout of {CS_DESTROY_TIMEOUT} sec.')


@asyncio_coro
async def on_disconnect_handler(i: Interface, client: Client):
    client_id = client.id
    if hasattr(client, 'session_id'):
        session_id = client.session_id
    else:
        session_id = None
    
    if session_id is None:
        translatable_text_element: NiceguiTranslatableTextElement = translatable_text_element_per_client.pop(client_id, None)
    else:
        translatable_text_element = translatable_text_element_per_session.pop(session_id, None)
    
    if hasattr(client, 'translatable_text_element'):
        if translatable_text_element is None:
            translatable_text_element = client.translatable_text_element
        
        delattr(client, 'translatable_text_element')

    if translatable_text_element is not None:
        await translatable_text_element.aremove_on_lang_changed_handler()
    
    if session_id is not None:
        session_clients[session_id].discard(client_id)
        if not session_clients[session_id]:
            session_clients.pop(session_id, None)


async def init_translation(i: Interface, app_args_kwargs: Tuple[Tuple, Dict]):
    await i(ShutdownOnKeyboardInterrupt)
    app_dir_path: AppDirPath = await i(Instance, InstanceRequest().get(AppDirPath))
    app_data_dir_path_type: str = await i(Instance, InstanceRequest().get('app_data_dir_path_type'))
    app_name_for_fs: str = await i(Instance, InstanceRequest().get('app_name_for_fs'))
    app_name_for_fs = app_name_for_fs if app_name_for_fs else app_args_kwargs[1]['app_name_for_fs']
    app_data_dir_path_rel: RelativePath = RelativePath(app_dir_path(app_data_dir_path_type, app_name_for_fs))
    global text_translator
    global translation_language_mapper
    text_translator, translation_language_mapper = setup_translation(app_data_dir_path_rel('text_dictionary.json'))
    await i(Instance, InstanceRequest().set('cengal_nicegui__text_translator', text_translator))
    await i(Instance, InstanceRequest().set('cengal_nicegui__translation_language_mapper', translation_language_mapper))


def run(*,
        host: str = '0.0.0.0',
        port_or_range: Union[int, slice, Tuple[int, int]] = 8080,
        main_coro: AnyWorker = None,
        is_fast_loop: bool = True,
        app_name: str = str(),
        app_name_for_fs: str = str(),
        app_version: Tuple[int, int, int, Union[int, str]] = tuple(),
        app_version_str: str = str(),
        **kwargs
    ) -> None:
    """Prepares and starts NiceGUI. Saves initial args and kwargs parameters (as well as determined free port) into a tuple (Tuple[Tuple, Dict]) within an Instance service awailable by a 'cengal_nicegui__app_args_kwargs' string key 

    Args:
        host (str, optional): _description_. Defaults to '0.0.0.0'.
        port_or_range (Union[int, slice, Tuple[int, int]], optional): _description_. Defaults to 8080.
        title (str, optional): _description_. Defaults to 'NiceGUI'.
        viewport (str, optional): _description_. Defaults to 'width=device-width, initial-scale=1'.
        favicon (Optional[str], optional): _description_. Defaults to None.
        dark (Optional[bool], optional): _description_. Defaults to False.
        binding_refresh_interval (float, optional): _description_. Defaults to 0.1.
        show (bool, optional): _description_. Defaults to True.
        reload (bool, optional): _description_. Defaults to True.
        uvicorn_logging_level (str, optional): _description_. Defaults to 'warning'.
        uvicorn_reload_dirs (str, optional): _description_. Defaults to '.'.
        uvicorn_reload_includes (str, optional): _description_. Defaults to '*.py'.
        uvicorn_reload_excludes (str, optional): _description_. Defaults to '.*, .py[cod], .sw.*, ~*'.
        tailwind (bool, optional): _description_. Defaults to True.
        is_fast_loop (bool, optional): _description_. Defaults to True.
        main_coro (AnyWorker, optional): _description_. Defaults to None.
    """
    port = simple_port_search(host, port_or_range)
    app_args_kwargs: Tuple[Tuple, Dict] = args_kwargs(
        host=host, 
        port_or_range=port_or_range, 
        port=port, 
        main_coro=main_coro,
        is_fast_loop=is_fast_loop,
        app_name=app_name,
        app_name_for_fs=app_name_for_fs,
        app_version=app_version,
        app_version_str=app_version_str,
        **kwargs,
    )
    run_in_loop(init_translation, app_args_kwargs)
    app.on_startup(init_cs(is_fast_loop, main_coro, app_args_kwargs))
    app.on_shutdown(destroy_cs)
    # app.on_connect(on_connect_handler)
    app.on_disconnect(on_disconnect_handler)
    ui.run(
        host=host,
        port=port,
        **kwargs,
        )
