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
    'CoroApp', 
    'bind_coro_explicit', 
    'bind_coro_implicit', 
    'bind_coro', 
    'abind_coro_explicit', 
    'abind_coro_implicit', 
    'abind_coro', 
    'asyncio_bind_coro_explicit', 
    'asyncio_bind_coro_implicit', 
    'asyncio_bind_coro', 
    'bind_asyncio_coro', 
    'bind_running_coro', 
    'bind_running_asyncio_coro', 
    'wx_exec_in_coro', 
    'bind_to', 
    'bind', 
    'event_handler_implicit', 
    'event_handler', 
    'event_handler_explicit', 
    'asyncio_event_handler', 
    'aevent_handler', 
    'blocking_event_handler_implicit', 
    'blocking_event_handler_explicit', 
]


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


from cengal.parallel_execution.coroutines.coro_scheduler import CoroScheduler, Interface, CoroID, Coro, AnyWorker, current_interface, current_coro_scheduler, cs_coro, cs_acoro
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly, CoroPriority, gly_patched, agly_patched
from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import AsyncioLoopRequest
from cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus import AsyncEventBusRequest, try_send_async_event
from cengal.parallel_execution.coroutines.coro_standard_services.simple_yield import Yield
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_loop import ShutdownLoop
from cengal.parallel_execution.coroutines.coro_standard_services.instance import InstanceRequest
from cengal.parallel_execution.coroutines.coro_tools.await_coro import await_task_prim
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
from cengal.parallel_execution.coroutines.coro_tools.coro_flow_control import graceful_coro_destroyer
from cengal.code_flow_control.smart_values import ValueHolder
from cengal.data_generation.id_generator import IDGenerator
from cengal.time_management.sleep_tools import try_sleep, get_usable_min_sleep_interval
from cengal.math.numbers import RationalNumber

from math import ceil
from inspect import signature, Signature, ismethod
from contextlib import contextmanager, asynccontextmanager
from functools import wraps, update_wrapper, partial
from asyncio import Future, Task, create_task
from typing import Optional, Any, Callable, Hashable, Set, Union, Awaitable, Coroutine


from wx import App, Window, Frame, Dialog, Timer, GetTopLevelParent, EVT_TIMER, EVT_CLOSE, ID_ANY


class BindedEntityIsAboutToBeDestroyed(Exception):
    pass


def sec_to_ms(sec: RationalNumber) -> int:
    return int(ceil(sec * 1000))


class CoroApp(App):
    def __init__(self, default_priority: CoroPriority = CoroPriority.normal):
        self._cs: CoroScheduler = current_coro_scheduler()
        self._cs.on_idle_handlers.add(self._on_system_loop_idle)
        self._cs.idle_managers_num += 1
        self._default_priority: CoroPriority = default_priority
        self._ly = gly(self._default_priority)
        self._binded_coros: Set = set()
        self._idle_for: Optional[int] = None  # in milliseconds
        super(CoroApp, self).__init__()

    def OnInit(self):
        super().OnInit()
        self._system_loop_timer = Timer(self)
        self.Bind(EVT_TIMER, self._on_system_loop_timer, self._system_loop_timer)
        self._system_loop_timer.StartOnce(1) # run every 1 millisecond
        return True

    def OnExit(self):
        super().OnExit()
        i: Interface = current_interface()
        i.log.info('Application is exiting.')
        i.log.info('Destroying all binded coros...')
        for furure_or_coro_id in self._binded_coros:
            if isinstance(furure_or_coro_id, Future):
                furure_or_coro_id.cancel()
            else:
                graceful_coro_destroyer(i, 0.1, furure_or_coro_id, BindedEntityIsAboutToBeDestroyed)
        
        i.log.info('All binded coroutines destroyed.')
        self._cs.idle_managers_num -= 1
        self._cs.on_idle_handlers.discard(self._on_system_loop_idle)
        i.log.info('Application is exiting... Done.')
        return super().OnExit()

    def _on_system_loop_timer(self, event):
        # from datetime import datetime
        # print(f'Cengal Timer >> {datetime.now()}>>')
        self._ly()
        if self._idle_for is None:
            self._system_loop_timer.StartOnce(1) # run every 1 millisecond
        else:
            # print(f'Idle for {self._idle_for} milliseconds.')
            idle_for = self._idle_for
            self._idle_for = None
            self._system_loop_timer.StartOnce(idle_for)

    def _on_system_loop_idle(self, next_event_after: Optional[RationalNumber]):
        if next_event_after is None:
            self._idle_for = max(1, sec_to_ms(get_usable_min_sleep_interval()))
        else:
            self._idle_for = max(1, sec_to_ms(next_event_after))


def bind_coro_explicit(wx_entity: Union[App, Frame, Dialog], coro: AnyWorker, *args, **kwargs):
    i: Interface = current_interface()
    coro_id: CoroID = i(PutCoro, coro, *args, **kwargs)
    bind_running_coro(wx_entity, coro_id)


def bind_coro_implicit(wx_entity: Union[App, Frame, Dialog], coro: AnyWorker, *args, **kwargs):
    i: Interface = current_interface()
    coro_id: CoroID = i(PutCoro, cs_coro(coro), *args, **kwargs)
    bind_running_coro(wx_entity, coro_id)


bind_coro = bind_coro_implicit


async def abind_coro_explicit(wx_entity: Union[App, Frame, Dialog], coro: AnyWorker, *args, **kwargs):
    i: Interface = current_interface()
    coro_id: CoroID = await i(PutCoro, coro, *args, **kwargs)
    bind_running_coro(wx_entity, coro_id)


async def abind_coro_implicit(wx_entity: Union[App, Frame, Dialog], coro: AnyWorker, *args, **kwargs):
    i: Interface = current_interface()
    coro_id: CoroID = await i(PutCoro, cs_coro(coro), *args, **kwargs)
    bind_running_coro(wx_entity, coro_id)


abind_coro = abind_coro_implicit


async def asyncio_bind_coro_explicit(wx_entity: Union[App, Frame, Dialog], coro: AnyWorker, *args, **kwargs):
    coro_id: CoroID = await await_task_prim(PutCoro, coro, *args, **kwargs)
    bind_running_coro(wx_entity, coro_id)


async def asyncio_bind_coro_implicit(wx_entity: Union[App, Frame, Dialog], coro: AnyWorker, *args, **kwargs):
    coro_id: CoroID = await await_task_prim(PutCoro, cs_coro(coro), *args, **kwargs)
    bind_running_coro(wx_entity, coro_id)


asyncio_bind_coro = asyncio_bind_coro_implicit


def bind_asyncio_coro(wx_entity: Union[App, Frame, Dialog], awaitable: Awaitable):
    coro_task: Task = create_task(awaitable)
    bind_running_asyncio_coro(wx_entity, coro_task)


def bind_running_coro(wx_entity: Union[App, Frame, Dialog], coro_id: CoroID):
    if isinstance(wx_entity, Window):
        wx_entity = GetTopLevelParent(wx_entity)
    
    if isinstance(wx_entity, App):
        wx_entity._binded_coros.add(coro_id)
    elif isinstance(wx_entity, (Frame, Dialog)):
        def close_binded_coro(event):
            i: Interface = current_interface()
            graceful_coro_destroyer(i, 0.1, coro_id, BindedEntityIsAboutToBeDestroyed)
            event.Skip()
        
        wx_entity.Bind(EVT_CLOSE, close_binded_coro)
    else:
        raise RuntimeError(f'wx_entity must be App, Frame, Dialog or a widget (Window) on a top level window, not {type(wx_entity)}')


def bind_running_asyncio_coro(wx_entity: Union[App, Frame, Dialog], coro_future: Future):
    if isinstance(wx_entity, App):
        wx_entity._binded_coros.add(coro_future)
    elif isinstance(wx_entity, (Frame, Dialog)):
        def close_binded_asyncio_coro(event):
            coro_future.cancel()
            event.Skip()
        
        wx_entity.Bind(EVT_CLOSE, close_binded_asyncio_coro)


def wx_exec_in_coro(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        cs: CoroScheduler = current_coro_scheduler()
        cs.high_cpu_utilisation_mode = False
        cs.use_internal_sleep = False
        i: Interface = current_interface()
        i(AsyncioLoopRequest().use_higher_level_sleep_manager())
        i(AsyncioLoopRequest().ensure_loop(interrupt_when_no_requests=True))
        i(AsyncioLoopRequest().turn_on_loops_intercommunication())

        app_or_tuple = func(*args, **kwargs)
        on_exit = lambda ret: ret
        if isinstance(app_or_tuple, App):
            app = app_or_tuple
        elif isinstance(app_or_tuple, tuple):
            app, on_exit = app_or_tuple
        else:
            raise RuntimeError("wx_exec_in_coro must return either wx.App or (wx.App, on_exit) tuple")
        
        # Run the event loop
        ret = app.MainLoop()
        ret = i(RunCoro, cs_coro(on_exit), ret)
        i(ShutdownLoop)
        return ret
    
    return cs_coro(wrapper)


def bind_to(wx_entity: Union[App, Frame, Dialog], wrapped_coro: Callable):
    if not (hasattr(wrapped_coro, '__wrapped__') and hasattr(wrapped_coro, '_decorator_func')):
        return wrapped_coro
    
    coro: Union[AnyWorker, Coroutine] = wrapped_coro.__wrapped__
    decorator_func = wrapped_coro._decorator_func
    new_wrapped_coro = decorator_func(coro)
    # if hasattr(wrapped_coro, '__self__'):
    #     new_wrapped_coro = new_wrapped_coro.__get__(wrapped_coro.__self__, wrapped_coro.__self__.__class__)
    
    new_wrapped_coro._binded_entity = wx_entity
    if hasattr(wrapped_coro, '__self__'):
        new_wrapped_coro.__self__ = wrapped_coro.__self__
    
    return new_wrapped_coro


def bind(wrapped_coro: Callable):
    if hasattr(wrapped_coro, '__self__'):
        return bind_to(wrapped_coro.__self__, wrapped_coro)
    else:
        return wrapped_coro 


def event_handler_implicit(coro: AnyWorker):
    def wrapper(*args, **kwargs):
        coro_sign: Signature = signature(coro)
        binded_entity = None
        if 2 == len(coro_sign.parameters):
            # The first parameter is self since event handler must have single parameter: event
            # binded_entity = wrapper.__self__
            binded_entity = args[0]

        i: Interface = current_interface()
        if hasattr(wrapper, '_binded_entity') and hasattr(wrapper, '__self__'):
            args = (wrapper.__self__,) + args
        
        coro_id: CoroID = i(PutCoro, cs_coro(coro), *args, **kwargs)
        if hasattr(wrapper, '_binded_entity'):
            binded_entity = getattr(wrapper, '_binded_entity')
        else:
            if binded_entity is None:
                binded_entity = App.Get()
        
        bind_running_coro(binded_entity, coro_id)
    
    wrapper.__wrapped__ = coro
    wrapper._decorator_func = event_handler_implicit
    return wrapper


event_handler = event_handler_implicit
aevent_handler = event_handler_implicit


def event_handler_explicit(coro: AnyWorker):
    @wraps(coro)
    def wrapper(*args, **kwargs):
        coro_sign: Signature = signature(coro)
        binded_entity = None
        if 3 == len(coro_sign.parameters):
            # The first parameter is self since event handler must have single parameter: event
            # binded_entity = wrapper.__self__
            binded_entity = args[1]

        i: Interface = current_interface()
        if hasattr(wrapper, '_binded_entity') and hasattr(wrapper, '__self__'):
            args = (wrapper.__self__,) + args
        
        coro_id: CoroID = i(PutCoro, coro, *args, **kwargs)
        if hasattr(wrapper, '_binded_entity'):
            binded_entity = getattr(wrapper, '_binded_entity')
        else:
            if binded_entity is None:
                binded_entity = App.Get()
        
        bind_running_coro(binded_entity, coro_id)
    
    wrapper.__wrapped__ = coro
    wrapper._decorator_func = event_handler_explicit
    return wrapper


def asyncio_event_handler(coro: Coroutine):
    @wraps(coro)
    def wrapper(*args, **kwargs):
        coro_sign: Signature = signature(coro)
        binded_entity = None
        if 2 == len(coro_sign.parameters):
            # The first parameter is self since event handler must have single parameter: event
            # binded_entity = wrapper.__self__
            binded_entity = args[0]

        if hasattr(wrapper, '_binded_entity') and hasattr(wrapper, '__self__'):
            args = (wrapper.__self__,) + args
        
        coro_task: Task = create_task(coro(*args, **kwargs))
        if hasattr(wrapper, '_binded_entity'):
            binded_entity = getattr(wrapper, '_binded_entity')
        else:
            if binded_entity is None:
                binded_entity = App.Get()
        
        bind_running_asyncio_coro(binded_entity, coro_task)
    
    wrapper.__wrapped__ = coro
    wrapper._decorator_func = asyncio_event_handler
    return wrapper


def blocking_event_handler_implicit(coro: AnyWorker):
    @wraps(coro)
    def wrapper(*args, **kwargs):
        i: Interface = current_interface()
        if hasattr(wrapper, '_binded_entity') and hasattr(wrapper, '__self__'):
            args = (wrapper.__self__,) + args
        
        i(RunCoro, cs_coro(coro), *args, **kwargs)
    
    wrapper.__wrapped__ = coro
    wrapper._decorator_func = blocking_event_handler_implicit
    return wrapper


def blocking_event_handler_explicit(coro: AnyWorker):
    @wraps(coro)
    def wrapper(*args, **kwargs):
        i: Interface = current_interface()
        if hasattr(wrapper, '_binded_entity') and hasattr(wrapper, '__self__'):
            args = (wrapper.__self__,) + args
        
        i(RunCoro, coro, *args, **kwargs)
    
    wrapper.__wrapped__ = coro
    wrapper._decorator_func = blocking_event_handler_explicit
    return wrapper
