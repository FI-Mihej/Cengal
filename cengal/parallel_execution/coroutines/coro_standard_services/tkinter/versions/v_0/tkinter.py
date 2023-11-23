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


from time import perf_counter
from cengal.introspection.inspect.versions.v_0.inspect import get_exception
from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield.versions.v_0.loop_yield import CoroPriority
from cengal.parallel_execution.coroutines.coro_standard_services.simple_yield import Yield
from cengal.parallel_execution.coroutines.coro_tools.await_coro import *
from enum import Enum
from typing import Callable, Dict, Hashable, Tuple, Union, Type, Optional, Any, List, Set
from cengal.time_management.repeat_for_a_time import Tracer
from cengal.code_flow_control.smart_values.versions.v_1 import ValueExistence
from async_generator import asynccontextmanager, async_generator, yield_
import asyncio
from tkinter import Tk, TclError
import inspect
from functools import partial
from inspect import isfunction, ismethod
from copy import copy
from cengal.time_management.sleep_tools import get_usable_min_sleep_interval


TkObjId = int


class TkinterServiceRequest(ServiceRequest):
    def create(self, tk_class: Type[Tk], *args, **kwargs) -> TkObjId:
        return self._save(0, tk_class, *args, **kwargs)

    def put(self, tk_obj: Tk) -> TkObjId:
        return self._save(1, tk_obj)

    def get(self, tk_obj_id: TkObjId) -> Tk:
        return self._save(2, tk_obj_id)

    def destroy(self, tk_obj_id: TkObjId, just_mark_as_destroyed: bool = False) -> None:
        return self._save(3, tk_obj_id, just_mark_as_destroyed)
    
    def destroy_and_wait_for_destroyed(self, tk_obj_id: TkObjId, just_mark_as_destroyed: bool = False) -> None:
        return self._save(4, tk_obj_id, just_mark_as_destroyed)
    
    def wait_for_destroyed(self, tk_obj_id: TkObjId) -> None:
        return self._save(5, tk_obj_id)
    
    def put_coro(self, tk_obj_id: TkObjId, coro_worker: AnyWorker, *args, **kwargs) -> CoroID:
        return self._save(6, tk_obj_id, coro_worker, *args, **kwargs)
    
    def register_coro(self, tk_obj_id: TkObjId, coro_id: CoroID) -> None:
        return self._save(7, tk_obj_id, coro_id)
    
    def set_update_period(self, tk_obj_id: TkObjId, period: float) -> None:
        return self._save(8, tk_obj_id, period)


class TkObjDestroyedError(Exception):
    pass


class TkObjWrapper:
    def __init__(self, interface: Interface, tk_obj_id, tk_obj, destroy_on_finish: bool = False) -> None:
        self._interface = interface
        self._tk_obj_id = tk_obj_id
        self._tk_obj = tk_obj
        self._destroyed: bool = False
        self._just_mark_as_destroyed: bool = not destroy_on_finish
        self._service: TkinterService = self._interface._loop.get_service_instance(TkinterService)
    
    @property
    def tk(self):
        if self._destroyed:
            raise TkObjDestroyedError
        else:
            return self._tk_obj
    
    @property
    def tk_id(self):
        if self._destroyed:
            raise TkObjDestroyedError
        else:
            return self._tk_obj_id
    
    def destroy(self, just_mark_as_destroyed: bool = False):
        if not self._destroyed:
            self._destroyed = True
            self._interface(TkinterService, TkinterServiceRequest().destroy(self._tk_obj_id, just_mark_as_destroyed))
    
    async def adestroy(self, just_mark_as_destroyed: bool = False):
        if not self._destroyed:
            self._destroyed = True
            await self._interface(TkinterService, TkinterServiceRequest().destroy(self._tk_obj_id, just_mark_as_destroyed))
    
    def put_coro(self, coro_worker: AnyWorker, *args, **kwargs):
        return self._interface(TkinterService, TkinterServiceRequest().put_coro(self.tk_id, coro_worker, *args, **kwargs))
    
    async def aput_coro(self, coro_worker: AnyWorker, *args, **kwargs):
        return await self._interface(TkinterService, TkinterServiceRequest().put_coro(self.tk_id, coro_worker, *args, **kwargs))
    
    def register_coro(self, coro_id: CoroID):
        return self._interface(TkinterService, TkinterServiceRequest().register_coro(self.tk_id, coro_id))
    
    async def aregister_coro(self, coro_id: CoroID):
        return await self._interface(TkinterService, TkinterServiceRequest().register_coro(self.tk_id, coro_id))
    
    @property
    def destroyed(self):
        return self._destroyed or (not self._service._get_inline(self._tk_obj_id))
    
    def __call__(self) -> Any:
        return self.tk
    
    def __enter__(self):
        return self._tk_obj
    
    def __exit__(self, type, value, traceback):
        self.destroy()

    async def __aenter__(self):
        return self._tk_obj

    async def __aexit__(self, type, value, traceback):
        await self.adestroy()
    
    def set_update_period(self, period: float):
        return self._interface(TkinterService, TkinterServiceRequest().set_update_period(self.tk_id, period))
    
    async def aset_update_period(self, period: float):
        return await self._interface(TkinterService, TkinterServiceRequest().set_update_period(self.tk_id, period))


class TkinterContextManager:
    def __init__(self, interface: Optional[Interface] = None, tk_obj_or_id: Optional[Union[Tk, TkObjId, Type[Tk]]] = None, *args, **kwargs):
        self._interface: Interface = interface or current_interface()
        self._tk_obj_or_id: Optional[Union[Tk, TkObjId]] = tk_obj_or_id
        self._args = args
        self._kwargs = kwargs
        self._tk_obj: Tk = None
        self._tk_obj_id: Optional[TkObjId] = None
        self._tk_wrapper: TkObjWrapper = None
        self._destroy_on_finish: bool = False
    
    def __enter__(self):
        if self._tk_obj_or_id is None:
            self._destroy_on_finish = True
            self._tk_obj_or_id = self._interface(TkinterService, TkinterServiceRequest().create(Tk, *self._args, **self._kwargs))
        
        if isinstance(self._tk_obj_or_id, Tk):
            self._tk_obj = self._tk_obj_or_id
            self._tk_obj_id = self._interface(TkinterService, TkinterServiceRequest().put(self._tk_obj))
        elif inspect.isclass(self._tk_obj_or_id):
            self._destroy_on_finish = True
            if not issubclass(self._tk_obj_or_id, Tk):
                self._interface._loop.logger.warning('Given class is not a subclass of Tk')
            
            self._tk_obj_id = self._interface(TkinterService, TkinterServiceRequest().create(self._tk_obj_or_id, *self._args, **self._kwargs))
            self._tk_obj = self._interface(TkinterService, TkinterServiceRequest().get(self._tk_obj_id))
        else:
            self._tk_obj_id = self._tk_obj_or_id
            self._tk_obj = self._interface(TkinterService, TkinterServiceRequest().get(self._tk_obj_id))
        
        self._tk_wrapper = TkObjWrapper(self._interface, self._tk_obj_id, self._tk_obj, self._destroy_on_finish)
        return self._tk_wrapper
    
    def __exit__(self, type, value: Exception, traceback):
        if not self._tk_wrapper.destroyed:
            self._interface(TkinterService, TkinterServiceRequest().wait_for_destroyed(self._tk_wrapper._tk_obj_id))

    async def __aenter__(self):
        if self._tk_obj_or_id is None:
            self._destroy_on_finish = True
            self._tk_obj_or_id = await self._interface(TkinterService, TkinterServiceRequest().create(Tk, *self._args, **self._kwargs))
        
        if isinstance(self._tk_obj_or_id, Tk):
            self._tk_obj = self._tk_obj_or_id
            self._tk_obj_id = await self._interface(TkinterService, TkinterServiceRequest().put(self._tk_obj))
        elif inspect.isclass(self._tk_obj_or_id):
            self._destroy_on_finish = True
            if not issubclass(self._tk_obj_or_id, Tk):
                self._interface._loop.logger.warning('Given class is not a subclass of Tk')
            
            self._tk_obj_id = await self._interface(TkinterService, TkinterServiceRequest().create(self._tk_obj_or_id, *self._args, **self._kwargs))
            self._tk_obj = await self._interface(TkinterService, TkinterServiceRequest().get(self._tk_obj_id))
        else:
            self._tk_obj_id = self._tk_obj_or_id
            self._tk_obj = await self._interface(TkinterService, TkinterServiceRequest().get(self._tk_obj_id))
        
        self._tk_wrapper = TkObjWrapper(self._interface, self._tk_obj_id, self._tk_obj, self._destroy_on_finish)
        return self._tk_wrapper

    async def __aexit__(self, type, value, traceback):
        if not self._tk_wrapper.destroyed:
            await self._interface(TkinterService, TkinterServiceRequest().wait_for_destroyed(self._tk_wrapper._tk_obj_id))


tcm = TkinterContextManager


class TkObjNotFoundError(Exception):
    pass


class TkinterService(Service, EntityStatsMixin):
    def __init__(self, loop: CoroScheduler):
        super(TkinterService, self).__init__(loop)

        self._request_workers = {
            0: self._on_create,
            1: self._on_put,
            2: self._on_get,
            3: self._on_destroy,
            4: self._on_destroy_and_wait_for_destroyed,
            5: self._on_wait_for_destroyed,
            6: self._on_put_coro,
            7: self._on_register_coro,
            8: self._on_set_update_period,
        }
        
        self.standard_ui_update_interval: float = 1 / 60
        self.default_update_period: float = max(get_usable_min_sleep_interval(), self.standard_ui_update_interval)
        self.update_period: float = self.default_update_period
        self.update_periods: Dict[TkObjId, float] = dict()
        self.tk_counter = Counter()
        self.tk_by_id: Dict[TkObjId, Tk] = dict()
        self.coroutines: Dict[CoroID, Set[TkObjId]] = dict()
        self.waiting_for_destroyed: Dict[TkObjId, Set[CoroID]] = dict()
        self.new_destroyed: Dict[TkObjId, bool] = dict()
        self.new_closed: Dict[TkObjId, bool] = dict()
        self.destroyed: Set[TkObjId] = set()
        self.coro_by_tk: Dict[TkObjId, CoroID] = dict()
        self.tk_users: Dict[TkObjId, Set[CoroID]] = dict()
        self.tk_after_ids: Dict[TkObjId, Set[str]] = dict()
        
        self.updater_running: bool = False
    
    def start_tk_updater(self):
        if not self.updater_running:
            self.updater_running = True
            tk_updater_coro = self._loop.put_coro(tk_updater, self)
            tk_updater_coro.is_background_coro = True

    def get_entity_stats(self, stats_level: 'EntityStatsMixin.StatsLevel' = EntityStatsMixin.StatsLevel.debug) -> Tuple[str, Dict[str, Any]]:
        return type(self).__name__, {
            'tk_counter': self.tk_counter._index + 1,
        }

    def single_task_registration_or_immediate_processing(self, request: Optional[TkinterServiceRequest]=None
                                                         ) -> ServiceProcessingResponse:
        if request is not None:
            return self.resolve_request(request)
        return True, None, None

    def full_processing_iteration(self):
        # closed
        new_closed_bak = self.new_closed
        self.new_closed = type(new_closed_bak)()
        for tk_obj_id, just_mark_as_destroyed in new_closed_bak.items():
            self.new_destroyed[tk_obj_id] = just_mark_as_destroyed
        
        # waiting_for_destroyed
        new_destroyed_bak = self.new_destroyed
        self.new_destroyed = type(self.new_destroyed)()
        for tk_obj_id, just_mark_as_destroyed in new_destroyed_bak.items():
            if tk_obj_id in self.destroyed:
                continue
                
            self.destroyed.add(tk_obj_id)
            
            tk_obj = self.tk_by_id[tk_obj_id]
            
            # if tk_obj_id in self.tk_after_ids:
            #     after_ids = self.tk_after_ids[tk_obj_id]
            #     for after_id in after_ids:
            #         tk_obj.after_cancel(after_id)
                
            #     del self.tk_after_ids[tk_obj_id]

            # cancel_all_after(tk_obj)
            
            if not just_mark_as_destroyed:
                tk_obj.destroy()
            
            if tk_obj_id in self.tk_by_id:
                del self.tk_by_id[tk_obj_id]

            if tk_obj_id in self.waiting_for_destroyed:
                for waiter_coro_id in self.waiting_for_destroyed[tk_obj_id]:
                    self.register_response(waiter_coro_id, None, None)
                
                del self.waiting_for_destroyed[tk_obj_id]
            
            if tk_obj_id in self.coro_by_tk:
                coros_tks = self.coroutines[self.coro_by_tk[tk_obj_id]]
                del self.coro_by_tk[tk_obj_id]
                if tk_obj_id in coros_tks:
                    coros_tks.remove(tk_obj_id)

            if tk_obj_id in self.tk_users:
                tk_users = self.tk_users[tk_obj_id]
                for tk_user_coro_id in tk_users:
                    # TODO: switch to an appropriate service
                    self._loop.kill_coro_by_id(tk_user_coro_id)
            
            if tk_obj_id in self.update_periods:
                del self.update_periods[tk_obj_id]
        
        # compute min update period
        if self.update_periods:
            self.update_period = min(self.update_periods.values())
        else:
            self.update_period = self.default_update_period
        
        # general
        if (not self.new_closed) and (not self.new_destroyed):
            self.make_dead()

    def in_work(self) -> bool:
        result: bool = bool(self.new_closed) or bool(self.new_destroyed) or bool(self.update_periods)
        return self.thrifty_in_work(result)
    
    def _on_create(self, tk_class: Type[Tk], *args, **kwargs) -> ServiceProcessingResponse:
        tk = tk_class(*args, **kwargs)
        tk_id: TkObjId = self.tk_counter.get()
        on_destroy = partial(self._on_create_on_destroyed, tk_id, tk)
        tk.bind("<Destroy>", on_destroy, '+')
        old_on_close = tk.protocol("WM_DELETE_WINDOW", None)
        if (not isfunction(old_on_close)) and (not ismethod(old_on_close)):
            old_on_close = None
        
        on_create_on_closed = partial(self._on_create_on_closed, tk_id, tk, old_on_close)
        tk.protocol("WM_DELETE_WINDOW", on_create_on_closed)
        self.tk_by_id[tk_id] = tk
        coro = self.current_caller_coro_info.coro
        coro_id = self.current_caller_coro_info.coro_id
        if coro_id not in self.coroutines:
            self.coroutines[coro_id] = set()
            coro.add_on_coro_del_handler(self._on_created_coro_del_handler)
        
        self.coroutines[coro_id].add(tk_id)
        self.coro_by_tk[tk_id] = coro_id
        # after_setup(tk, 1)
        after_idle_setup(tk)
        self.start_tk_updater()
        return True, tk_id, None
    
    def _on_put(self, tk_obj: Tk) -> ServiceProcessingResponse:
        tk: Tk = tk_obj
        tk_id: TkObjId = self.tk_counter.get()
        on_destroy = partial(self._on_put_on_destroyed, tk_id, tk)
        tk.bind("<Destroy>", on_destroy, '+')
        old_on_close = tk.protocol("WM_DELETE_WINDOW", None)
        if (not isfunction(old_on_close)) and (not ismethod(old_on_close)):
            old_on_close = None
        
        on_put_on_closed = partial(self._on_put_on_closed, tk_id, tk, old_on_close)
        tk.protocol("WM_DELETE_WINDOW", on_put_on_closed)
        self.tk_by_id[tk_id] = tk
        coro = self.current_caller_coro_info.coro
        coro_id = self.current_caller_coro_info.coro_id
        if coro_id not in self.coroutines:
            self.coroutines[coro_id] = set()
            coro.add_on_coro_del_handler(self._on_put_coro_del_handler)
        
        self.coroutines[coro_id].add(tk_id)
        self.coro_by_tk[tk_id] = coro_id
        # after_setup(tk, 1)
        after_idle_setup(tk)
        self.start_tk_updater()
        return True, tk_id, None
    
    def _on_get(self, tk_obj_id: TkObjId) -> ServiceProcessingResponse:
        if tk_obj_id in self.tk_by_id:
            return True, self.tk_by_id[tk_obj_id], None
        else:
            return True, None, TkObjNotFoundError()
    
    def _get_inline(self, tk_obj_id: TkObjId) -> Optional[Tk]:
        return self.tk_by_id.get(tk_obj_id, None)
    
    def _on_destroy(self, tk_obj_id: TkObjId, just_mark_as_destroyed: bool = False) -> ServiceProcessingResponse:
        self.new_destroyed[tk_obj_id] = just_mark_as_destroyed
        self.make_live()
        return True, None, None
    
    def _on_destroy_and_wait_for_destroyed(self, tk_obj_id: TkObjId, just_mark_as_destroyed: bool = False) -> ServiceProcessingResponse:
        self.new_destroyed[tk_obj_id] = just_mark_as_destroyed
        return self._on_wait_for_destroyed(tk_obj_id)
    
    def _on_wait_for_destroyed(self, tk_obj_id: TkObjId) -> ServiceProcessingResponse:
        if tk_obj_id in self.destroyed:
            return True, None, None
        
        if tk_obj_id not in self.waiting_for_destroyed:
            self.waiting_for_destroyed[tk_obj_id] = set()
        
        self.waiting_for_destroyed[tk_obj_id].add(self.current_caller_coro_info.coro_id)
        self.make_live()
        return False, None, None
    
    def _on_put_coro(self, tk_obj_id: TkObjId, coro_worker: AnyWorker, *args, **kwargs):
        exception = None
        coro_id: CoroID = None
        try:
            # TODO: switch to an appropriate service
            coro_id = self._loop.put_coro(coro_worker, *args, **kwargs).coro_id
        except:
            exception = get_exception()
        
        self._register_coro_impl(tk_obj_id, coro_id)
        return True, coro_id, exception
    
    def _on_register_coro(self, tk_obj_id: TkObjId, coro_id: CoroID):
        exception = None
        try:
            self._register_coro_impl(tk_obj_id, coro_id)
        except:
            exception = get_exception()
        
        return True, None, exception
    
    def _register_coro_impl(self, tk_obj_id: TkObjId, coro_id: CoroID):
        if tk_obj_id not in self.tk_users:
            self.tk_users[tk_obj_id] = set()
        
        self.tk_users[tk_obj_id].add(coro_id)

    def _on_set_update_period(self, tk_obj_id: TkObjId, period: float):
        self.update_periods[tk_obj_id] = period
        
        self.make_live()
        return True, None, None

    def _on_created_coro_del_handler(self, coro: CoroWrapperBase) -> bool:
        for tk_obj_id in self.coroutines[coro.coro_id]:
            self.new_destroyed[tk_obj_id] = False
        
        self.make_live()
        return True

    def _on_put_coro_del_handler(self, coro: CoroWrapperBase) -> bool:
        for tk_obj_id in self.coroutines[coro.coro_id]:
            self.new_destroyed[tk_obj_id] = True
        
        self.make_live()
        return True
    
    def _on_create_on_destroyed(self, tk_obj_id: TkObjId, tk_obj: Tk, event):
        if event.widget is tk_obj:
            if tk_obj_id not in self.destroyed:
                self.new_destroyed[tk_obj_id] = True
        
        self.make_live()
    
    def _on_put_on_destroyed(self, tk_obj_id: TkObjId, tk_obj: Tk, event):
        if event.widget is tk_obj:
            if tk_obj_id not in self.destroyed:
                self.new_destroyed[tk_obj_id] = True
        
        self.make_live()
    
    def _on_create_on_closed(self, tk_obj_id: TkObjId, tk: Tk, previous_on_close: Optional[Callable]):
        if previous_on_close is not None:
            previous_on_close()
        
        if tk_obj_id not in self.destroyed:
            self.new_closed[tk_obj_id] = False

        self.make_live()
    
    def _on_put_on_closed(self, tk_obj_id: TkObjId, tk: Tk, previous_on_close: Optional[Callable]):
        if previous_on_close is not None:
            previous_on_close()
        
        if tk_obj_id not in self.destroyed:
            self.new_closed[tk_obj_id] = False

        self.make_live()


# def tk_updater(i: Interface, tkinter_service: TkinterService):
#     from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
#     while tkinter_service.tk_by_id:
#         tk_by_id_bak = copy(tkinter_service.tk_by_id)
#         for tk_id, tk_obj in tk_by_id_bak.items():
#             if tk_id not in tkinter_service.destroyed:
#                 tk_obj.update()
        
#         i(Sleep, tkinter_service.update_period)
    
#     tkinter_service.updater_running = False
    

# def tk_updater(i: Interface, tkinter_service: TkinterService):
#     """
#     https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app
#     https://github.com/ipython/ipython/blob/master/IPython/terminal/pt_inputhooks/tk.py

#     Args:
#         i (Interface): [description]
#         tkinter_service (TkinterService): [description]
#     """
#     from _tkinter import ALL_EVENTS as _tkinter__ALL_EVENTS, DONT_WAIT as _tkinter__DONT_WAIT
#     from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
#     from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import get_loop_yield
#     ly = get_loop_yield(CoroPriority.low)
#     while tkinter_service.tk_by_id:
#         tk_by_id_bak = copy(tkinter_service.tk_by_id)
#         for tk_id, tk_obj in tk_by_id_bak.items():
#             ly()
#             if tk_id not in tkinter_service.destroyed:
#                 while tk_obj.dooneevent(_tkinter__ALL_EVENTS | _tkinter__DONT_WAIT):
#                     ly()
        
#         i(Sleep, tkinter_service.update_period)
    
#     tkinter_service.updater_running = False
    

# def tk_updater(i: Interface, tkinter_service: TkinterService):
#     """
#     https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app
#     https://github.com/ipython/ipython/blob/master/IPython/terminal/pt_inputhooks/tk.py

#     Args:
#         i (Interface): [description]
#         tkinter_service (TkinterService): [description]
#     """
#     from _tkinter import ALL_EVENTS as _tkinter__ALL_EVENTS, DONT_WAIT as _tkinter__DONT_WAIT
#     from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
#     from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import get_loop_yield
#     ly = get_loop_yield(CoroPriority.low)
#     while tkinter_service.tk_by_id:
#         ly()
#         tk_by_id_bak = copy(tkinter_service.tk_by_id)
#         tk_objects_with_events = set()
#         for tk_id, tk_obj in tk_by_id_bak.items():
#             if tk_id not in tkinter_service.destroyed:
#                 tk_objects_with_events.add(tk_obj)
        
#         while tk_objects_with_events:
#             new_tk_objects_with_events = set()
#             for tk_obj in tk_objects_with_events:
#                 ly()
#                 if tk_obj.dooneevent(_tkinter__ALL_EVENTS | _tkinter__DONT_WAIT):
#                     new_tk_objects_with_events.add(tk_obj)
            
#             tk_objects_with_events = new_tk_objects_with_events
        
#         i(Sleep, tkinter_service.update_period)
    
#     tkinter_service.updater_running = False


TkinterServiceRequest.default_service_type = TkinterService


# TODO: currently it uses Yield if delay is bigger that a magic number `0.001` seconds. Maybe make it some how use TkinterService.update_periods or somethin like it instead?
def tk_updater(i: Interface, tkinter_service: TkinterService):
    """
    https://stackoverflow.com/questions/4083796/how-do-i-run-unittest-on-a-tkinter-app
    https://github.com/ipython/ipython/blob/master/IPython/terminal/pt_inputhooks/tk.py

    Args:
        i (Interface): [description]
        tkinter_service (TkinterService): [description]
    """
    from _tkinter import ALL_EVENTS as _tkinter__ALL_EVENTS, WINDOW_EVENTS as _tkinter__WINDOW_EVENTS, FILE_EVENTS as _tkinter__FILE_EVENTS, TIMER_EVENTS as _tkinter__TIMER_EVENTS, IDLE_EVENTS as _tkinter__IDLE_EVENTS, DONT_WAIT as _tkinter__DONT_WAIT
    from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
    from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import get_loop_yield
    ly = get_loop_yield(CoroPriority.low)
    while tkinter_service.tk_by_id:
        ly()
        tk_by_id_bak = copy(tkinter_service.tk_by_id)
        desired_length = len(tk_by_id_bak.keys())
        tk_ids_without_events = set()
        
        while len(tk_ids_without_events) < desired_length:
            for tk_id, tk_obj in tk_by_id_bak.items():
                if tk_id in tk_ids_without_events:
                    continue
                
                if tk_id in tkinter_service.destroyed:
                    tk_ids_without_events.add(tk_id)
                    continue
                
                start = perf_counter()
                has_window_events = tk_obj.dooneevent(_tkinter__WINDOW_EVENTS | _tkinter__DONT_WAIT)
                stop = perf_counter()
                if (stop - start) > 0.001:
                    i(Yield)
                # ly()
                
                start = perf_counter()
                has_file_events = tk_obj.dooneevent(_tkinter__FILE_EVENTS | _tkinter__DONT_WAIT)
                stop = perf_counter()
                if (stop - start) > 0.001:
                    i(Yield)
                # ly()
                
                start = perf_counter()
                has_timer_events = tk_obj.dooneevent(_tkinter__TIMER_EVENTS | _tkinter__DONT_WAIT)
                stop = perf_counter()
                if (stop - start) > 0.001:
                    i(Yield)
                # ly()
                
                has_events = has_window_events or has_file_events or has_timer_events
                
                if not has_events:
                    start = perf_counter()
                    tk_obj.dooneevent(_tkinter__IDLE_EVENTS | _tkinter__DONT_WAIT)
                    stop = perf_counter()
                    if (stop - start) > 0.001:
                        i(Yield)
                    # ly()
                    tk_ids_without_events.add(tk_id)

        i(Sleep, tkinter_service.update_period)
    
    tkinter_service.updater_running = False


def after_func(root):
    from cengal.parallel_execution.coroutines.coro_standard_services.simple_yield import Yield
    from cengal.parallel_execution.coroutines.coro_scheduler import current_interface, OutsideCoroSchedulerContext
    try:
        i = current_interface()
        if i is not None:
            i(Yield)
    except OutsideCoroSchedulerContext:
        pass
    
    # after_setup(root, 1)
    after_idle_setup(root)


def after_setup(root, update_period) -> bool:
    try:
        handler = root.after(update_period, after_func, root)
    except TclError:
        return False

    return True


def after_idle_setup(root) -> bool:
    try:
        handler = root.after_idle(after_setup, root, 0)
    except TclError:
        return False

    return True
