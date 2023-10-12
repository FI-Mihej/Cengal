#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.3.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


__all__ = ['ClientHandlers', 'PageItems', 'nicegui_page_sync_coro', 'sync_like_page', 
           'sl_page', 'nicegui_page_async_coro', 'async_page', 'apage',
           'nicegui_page_class_async_coro', 'async_page_class', 'apage_class', 
           'PageContextBase', 'run']


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
from typing import Set, Tuple, Optional, Union, Dict, Callable, Any, Hashable, cast
import warnings
from cengal.parallel_execution.asyncio.atasks import create_task
from cengal.parallel_execution.coroutines.coro_scheduler import Interface, AnyWorker, cs_acoro
from cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus import (AsyncEventBus,
                                                                                         AsyncEventBusRequest)
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro, put_coro_to
from cengal.parallel_execution.coroutines.coro_standard_services.simple_yield import Yield
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import AsyncioLoop, AsyncioLoopRequest
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_loop import ShutdownLoop
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_on_keyboard_interrupt import ShutdownOnKeyboardInterrupt
from cengal.parallel_execution.coroutines.coro_standard_services.simple_yield import \
    Yield
from cengal.parallel_execution.coroutines.coro_standard_services.instance import Instance, InstanceRequest, afast_wait
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import agly_patched
from cengal.parallel_execution.coroutines.coro_tools.await_coro import await_coro_prim
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import (arun_in_fast_loop, arun_in_loop, run_in_loop)
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
from nicegui.binding import loop
# agly_patched(loop)
from cengal.parallel_execution.asyncio.timed_yield import TimedYield
import nicegui.binding
original__propagate = nicegui.binding.propagate
class PropageteMock:
    def __init__(self) -> None:
        self.ty: TimedYield = TimedYield(0.01)
    
    def __call__(self, source_obj: Any, source_name: str, visited: Optional[Set[Tuple[int, str]]] = None) -> None:
        return original__propagate(source_obj, source_name, visited)


nicegui.binding.propagate = PropageteMock()
from fastapi import Request as FastAPIRequest
from .text_translation import setup_translation, create_translatable_text_element, TextTranslator, \
    TranslationLanguageMapper, TranslationLanguageChooser, TranslatableTextElement, TTE, NiceguiTranslatableTextElement, NTTE
from cengal.parallel_execution.coroutines.coro_tools.await_coro import asyncio_coro
from cengal.file_system.app_fs_structure.app_dir_path import AppDirPath, AppDirectoryType
from cengal.file_system.path_manager import RelativePath
from cengal.web_tools.detect_browsers_host_device_type.by_http_headers import ClientViewType, client_view_type
from cengal.web_tools.detect_browsers_language.by_http_headers import parse_accept_language, optimize_accept_language, match_langs, normalize_lang
from cengal.math.numbers import RationalNumber
from functools import partial
from collections import OrderedDict


DESTROY_CS_EVENT = f'DESTROY_CENGAL_EVENT__{uuid4()}'
CS_DESTROY_TIMEOUT = 3.0


text_translator: TextTranslator = None
translation_language_mapper: TranslationLanguageMapper = None
session_clients: Dict[Hashable, Set[Hashable]] = dict()
translatable_text_element_per_session: Dict[Hashable, NiceguiTranslatableTextElement] = dict()
translatable_text_element_per_client: Dict[Hashable, NiceguiTranslatableTextElement] = dict()


class CoroWrapperNiceGuiPage(CoroWrapperAsyncAwait):
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


class PageContextBase:
    def __init__(self, client: Client, request: FastAPIRequest, _t: NTTE) -> None:
        self.client: Client = client
        self.request: FastAPIRequest = request
        self.client_id: Hashable = client.id
        self.session_id: Hashable = client.session_id
        self.user_id: Hashable = None
        self._t: NTTE = _t
        self.client_view_type: ClientViewType = self._determine_client_view_type()
        self.better_lang: str = None
        self.featured_langs: OrderedDict[str, RationalNumber] = None
        self.langs: OrderedDict[str, RationalNumber] = None
        self.better_lang, self.featured_langs, self.langs = self._determine_client_languages()
        self._t.text_translation_language_chooser.lang = self.better_lang
    
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
            async def awaitable_coro_wrapper(i: Interface, current_asyncio_task, wrapper_signature, coro_worker_with_args: EntityArgsHolderExplicit):
                coro_worker, args, kwargs = coro_worker_with_args.entity_args_kwargs()
                reinterpret_cast(CoroWrapperNiceGuiPage, i._coro)
                i._coro.current_asyncio_task = current_asyncio_task
                i._coro.reinit_for_nicegui()
                await i(Yield)
                ClientHandlers.check_args_factory(wrapper_signature, args, kwargs)
                PageItems.check_args_factory(wrapper_signature, args, kwargs)
                return await coro_worker(i, *args, **kwargs)
            
            coro_wrapper = awaitable_coro_wrapper
        elif CoroType.greenlet == coro_worker_type:
            def greenlet_coro_wrapper(i: Interface, current_asyncio_task, wrapper_signature, coro_worker_with_args: EntityArgsHolderExplicit):
                coro_worker, args, kwargs = coro_worker_with_args.entity_args_kwargs()
                reinterpret_cast(CoroWrapperNiceGuiPage, i._coro)
                i._coro.current_asyncio_task = current_asyncio_task
                i._coro.reinit_for_nicegui()
                i(Yield)
                ClientHandlers.check_args_factory(wrapper_signature, args, kwargs)
                PageItems.check_args_factory(wrapper_signature, args, kwargs)
                return coro_worker(i, *args, **kwargs)
            
            coro_wrapper = greenlet_coro_wrapper
        else:
            raise TypeError(f'{coro_worker} is neither an awaitable nor a greenlet')

        current_asyncio_task = asyncio.current_task()
        args_kwargs: Optional[Tuple[Tuple, Dict]] = dict().get('args_kwargs', None)
        if args_kwargs is None:
            args_kwargs = (tuple(), dict())
        
        args = tuple()
        kwargs = dict()
        coro_worker_param_names_set: Set[str] = set(inspect.signature(coro_worker).parameters.keys())
        if 'client' in coro_worker_param_names_set:
            kwargs['client'] = client

        if 'request' in coro_worker_param_names_set:
            kwargs['request'] = request
        
        translation_params: Set[str] = {'_t', '_T', '__'} & coro_worker_param_names_set
        if translation_params:
            for translation_param in translation_params:
                kwargs[translation_param] = translatable_text_element
        
        page_context_params: Set[str] = {'page_context', 'pc', 'self'} & coro_worker_param_names_set
        if page_context_params:
            page_class = page_class_0
            if isclass(page_class):
                if issubclass(page_class, PageContextBase):
                    page_context: PageContextBase = page_class(client, request, translatable_text_element)
                else:
                    raise TypeError(f'{page_class} is not a subclass of PageContextBase')
            elif isinstance(page_class, EntityArgsHolder):
                page_class = cast(EntityArgsHolder, page_class)
                page_class, page_class_own_args, page_class_own_kwargs = page_class.entity_args_kwargs()
                page_class_own_kwargs.update({
                    'client': client,
                    'request': request,
                    '_t': translatable_text_element,
                })
                page_context = page_class(*page_class_own_args, **page_class_own_kwargs)
            else:
                raise TypeError(f'{page_class} is not a subclass of PageContextBase nor an EntityArgsHolder')

            for page_context_param in page_context_params:
                kwargs[page_context_param] = page_context

        return await await_coro_prim(coro_wrapper, current_asyncio_task, wrapper_signature, EntityArgsHolderExplicit(coro_worker, args, kwargs))
        
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
        await i(AsyncioLoop, AsyncioLoopRequest().inherit_surrounding_loop())
        await i(AsyncioLoop, AsyncioLoopRequest().turn_on_loops_intercommunication(True))
        await i(ShutdownOnKeyboardInterrupt)
        await i(Instance, InstanceRequest().set('nicegui__app_args_kwargs', app_args_kwargs))

        app_name: str = app_args_kwargs[1]['app_name']
        app_name_for_fs: str = app_args_kwargs[1]['app_name_for_fs']
        app_version: str = app_args_kwargs[1]['app_version']
        app_version_str: str = app_args_kwargs[1]['app_version_str']
        await i(Instance, InstanceRequest().set('app_name', app_name))
        await i(Instance, InstanceRequest().set('app_name_for_fs', app_name_for_fs))
        await i(Instance, InstanceRequest().set('app_version', app_version))
        await i(Instance, InstanceRequest().set('app_version_str', app_version_str))

        # await init_translation(i, app_args_kwargs)
        if main_coro is not None:
            await i(PutCoro, main_coro, app_args_kwargs)

        await i(AsyncEventBus, AsyncEventBusRequest().wait(DESTROY_CS_EVENT))
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
    await i(Instance, InstanceRequest().set('nicegui__text_translator', text_translator))
    await i(Instance, InstanceRequest().set('nicegui__translation_language_mapper', translation_language_mapper))


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
    """Prepares and starts NiceGUI. Saves initial args and kwargs parameters (as well as determined free port) into a tuple (Tuple[Tuple, Dict]) within an Instance service awailable by a 'nicegui__app_args_kwargs' string key 

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
