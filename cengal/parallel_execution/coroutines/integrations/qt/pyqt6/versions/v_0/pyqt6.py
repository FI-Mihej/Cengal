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
    'WrongQtVersion', 
    'exec_app', 
    'execa', 
    'aemit_signal', 
    'aemit', 
    'by_coro', 
    'aby_coro', 
    'modal_blocking', 
    'amodal_blocking', 
    'block_main_loop', 
    'ablock_main_loop', 
    'modal', 
    'amodal', 
    'CoroSlot', 
    'CSlot', 
    'coro_slot_implicit', 
    'cslot_implicit', 
    'csloti', 
    'csi', 
    'coro_slot_gly_patched', 
    'cslot_gly_patched', 
    'cslotglyp', 
    'cslotgp', 
    'csgp', 
    'coro_slot_agly_patched', 
    'cslot_agly_patched', 
    'cslotaglyp', 
    'cslotagp', 
    'csagp', 
    'coro_slot_explicit', 
    'cslot_explicit', 
    'cslotex', 
    'csex', 
    'qt_exec_in_coro', 
    'aqt_exec_in_coro', 
    'CoroThreadWorker', 
    'CoroThreadWithWorker',
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


from cengal.parallel_execution.coroutines.coro_scheduler import CoroScheduler, Interface, Coro, AnyWorker, current_interface, current_coro_scheduler, cs_coro, cs_acoro
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly, CoroPriority, gly_patched, agly_patched
from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import AsyncioLoopRequest
from cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus import AsyncEventBusRequest, try_send_async_event
from cengal.parallel_execution.coroutines.coro_standard_services.simple_yield import Yield
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_loop import ShutdownLoop
from cengal.parallel_execution.coroutines.coro_standard_services.instance import InstanceRequest
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
from cengal.parallel_execution.coroutines.integrations.qt.common.exceptions import WrongQtVersion
from cengal.code_flow_control.smart_values import ValueHolder
from cengal.data_generation.id_generator import IDGenerator

from PyQt6.QtCore import pyqtSlot, QObject, Qt, QTimer, pyqtSignal, QThread
from PyQt6.QtWidgets import QApplication

from inspect import signature, Signature
from contextlib import contextmanager, asynccontextmanager
from functools import wraps, update_wrapper, partial
from typing import Optional, Any, Callable, Hashable


YIELD_ALLOWED_EVENT = 'QT_yield_allowed_event'
YIELD_IN_WORK_EVENT = 'QT_yield_in_work_event'
MODAL_RESULT_EVENT = 'QT_modal_result_event'
MODAL_COUNTER = IDGenerator()


def exec_app(app, default_priority: CoroPriority = CoroPriority.normal) -> int:
    if not isinstance(app, QApplication):
        raise WrongQtVersion('Qt version is not PyQt6')
    
    timer = QTimer()
    ly = gly(default_priority)
    yield_allowed: ValueHolder[bool] = ValueHolder(True, True)
    yield_in_work: ValueHolder[bool] = ValueHolder(True, True)
    def yield_func():
        if yield_allowed.value:
            yield_in_work.value = True
            ly()
        else:
            yield_in_work.value = False

    i: Interface = current_interface()
    i(InstanceRequest().set(YIELD_ALLOWED_EVENT, yield_allowed))
    i(InstanceRequest().set(YIELD_IN_WORK_EVENT, yield_in_work))
    timer.timeout.connect(yield_func, Qt.ConnectionType.QueuedConnection)
    timer.start(0)
    def cleanup_callback():
        timer.stop()

    app.aboutToQuit.connect(cleanup_callback)
    return app.exec()


execa = exec_app


async def aemit_signal(signal, *args, **kwargs):
    i: Interface = current_interface()
    def coro(i: Interface):
        signal.emit(*args, **kwargs)
    
    return await i(RunCoro, coro)


aemit = aemit_signal


def by_coro(callable: Callable, *args, **kwargs):
    def coro(i: Interface):
        callable(*args, **kwargs)
    
    return current_interface()(RunCoro, coro)


async def aby_coro(callable: Callable, *args, **kwargs):
    def coro(i: Interface):
        callable(*args, **kwargs)
    
    return await current_interface()(RunCoro, coro)


def stop_yield_to_main_loop():
    i: Interface = current_interface()
    yield_allowed: ValueHolder[bool] = i(InstanceRequest().wait(YIELD_ALLOWED_EVENT))
    yield_allowed.value = False
    yield_in_work: ValueHolder[bool] = i(InstanceRequest().wait(YIELD_IN_WORK_EVENT))
    while yield_in_work.value:
        i(Yield)


@contextmanager
def block_main_loop():
    i: Interface = current_interface()
    yield_allowed: ValueHolder[bool] = i(InstanceRequest().wait(YIELD_ALLOWED_EVENT))
    yield_allowed.value = False
    yield_in_work: ValueHolder[bool] = i(InstanceRequest().wait(YIELD_IN_WORK_EVENT))
    while yield_in_work.value:
        i(Yield)
    
    try:
        yield
    finally:
        yield_allowed.value = True


@asynccontextmanager
async def ablock_main_loop():
    i: Interface = current_interface()
    yield_allowed: ValueHolder[bool] = await i(InstanceRequest().wait(YIELD_ALLOWED_EVENT))
    yield_allowed.value = False
    yield_in_work: ValueHolder[bool] = await i(InstanceRequest().wait(YIELD_IN_WORK_EVENT))
    while yield_in_work.value:
        await i(Yield)
    
    try:
        yield
    finally:
        yield_allowed.value = True


def modal_blocking(modal_obj, *args, **kwargs):
    with block_main_loop():
        return modal_obj(*args, **kwargs)


async def amodal_blocking(modal_obj, *args, **kwargs):
    async with ablock_main_loop():
        return modal_obj(*args, **kwargs)


def modal(callable_with_modal, *args, **kwargs):
    class ShowModal(QObject):
        signal = pyqtSignal()

        def __init__(self, cs: CoroScheduler, result_event: Hashable):
            super().__init__()
            self.cs: CoroScheduler = cs
            self.result_event: Hashable = result_event
            self.signal.connect(self.show_modal, Qt.ConnectionType.QueuedConnection)

        @pyqtSlot()
        def show_modal(self):
            result = callable_with_modal(*args, **kwargs)
            try_send_async_event(self.cs, self.result_event, result)

    event = (MODAL_RESULT_EVENT, MODAL_COUNTER())
    sm: ShowModal = ShowModal(current_coro_scheduler(), event)
    sm.signal.emit()
    i: Interface = current_interface()
    return i(AsyncEventBusRequest().wait(event))


async def amodal(callable_with_modal, *args, **kwargs):
    class ShowModal(QObject):
        signal = pyqtSignal()

        def __init__(self, cs: CoroScheduler, result_event: Hashable):
            super().__init__()
            self.cs: CoroScheduler = cs
            self.result_event: Hashable = result_event
            self.signal.connect(self.show_modal, Qt.ConnectionType.QueuedConnection)

        @pyqtSlot()
        def show_modal(self):
            result = callable_with_modal(*args, **kwargs)
            try_send_async_event(self.cs, self.result_event, result)

    event = (MODAL_RESULT_EVENT, MODAL_COUNTER())
    sm: ShowModal = ShowModal(current_coro_scheduler(), event)
    sm.signal.emit()
    i: Interface = current_interface()
    return await i(AsyncEventBusRequest().wait(event))


# class CoroSlot(QObject):
class CoroSlot:
    def __init__(self, *types: type, name: Optional[str] = None, result: Optional[str] = None) -> None:
        self._types = types
        self._name = name
        self._result = result
        self._coro = None

    def __call__(self, coro: Coro, method = None) -> Any:
        method = method or self.implicit_coro_impl
        return method(coro)

    def implicit_coro_impl(self, coro: Coro) -> Any:
        self._coro = coro

        def func_wrapper(*args, **kwargs):
            cs: CoroScheduler = current_coro_scheduler()
            service: PutCoro = cs.get_service_instance(PutCoro)
            return service._add_direct_request(cs_coro(coro), *args, **kwargs)
        
        coro_worker_sign: Signature = signature(coro)
        update_wrapper(func_wrapper, coro)
        func_wrapper.__signature__ = coro_worker_sign.replace(parameters=tuple(coro_worker_sign.parameters.values()), return_annotation=coro_worker_sign.return_annotation)
        return pyqtSlot(*self._types, self._name, self._result)(func_wrapper)
    
    def implicit_coro(self):
        return partial(self, method=self.implicit_coro_impl)
    
    ic = implicit_coro

    def gly_patched_function_impl(self, func: Callable) -> Any:
        return self.__call__(gly_patched(func))

    def gly_patched_function(self) -> Any:
        return partial(self, method=self.gly_patched_function_impl)
    
    glypf = gly_patched_function
    gpf = gly_patched_function
    gp = gly_patched_function

    def agly_patched_function_impl(self, afunc: Callable) -> Any:
        return self.__call__(agly_patched(afunc))

    def agly_patched_function(self) -> Any:
        return partial(self, method=self.agly_patched_function_impl)
    
    aglypf = agly_patched_function
    agpf = agly_patched_function
    agp = agly_patched_function

    def explicit_coro_impl(self, coro: Coro) -> Any:
        self._coro = coro

        def func_wrapper(*args, **kwargs):
            cs: CoroScheduler = current_coro_scheduler()
            service: PutCoro = cs.get_service_instance(PutCoro)
            return service._add_direct_request(coro, *args, **kwargs)
        
        coro_worker_sign: Signature = signature(coro)
        update_wrapper(func_wrapper, coro)
        func_wrapper.__signature__ = coro_worker_sign.replace(parameters=tuple(coro_worker_sign.parameters.values())[1:], return_annotation=coro_worker_sign.return_annotation)
        return pyqtSlot(*self._types, self._name, self._result)(func_wrapper)

    def explicit_coro(self) -> Any:
        return partial(self, method=self.explicit_coro_impl)
    
    ec = explicit_coro
    interface = explicit_coro
    i = interface


CSlot = CoroSlot


def coro_slot_implicit(*types: type, name: Optional[str] = None, result: Optional[str] = None):
    def decorator(coro: Coro) -> Any:
        return CoroSlot(*types, name=name, result=result).implicit_coro()(coro)
    
    return decorator

cslot_implicit = coro_slot_implicit
csloti = coro_slot_implicit
csi = coro_slot_implicit


def coro_slot_gly_patched(*types: type, name: Optional[str] = None, result: Optional[str] = None):
    def decorator(func: Callable) -> Any:
        return CoroSlot(*types, name=name, result=result).gly_patched_function()(func)
    
    return decorator

cslot_gly_patched = coro_slot_gly_patched
cslotglyp = coro_slot_gly_patched
cslotgp = coro_slot_gly_patched
csgp = coro_slot_gly_patched


def coro_slot_agly_patched(*types: type, name: Optional[str] = None, result: Optional[str] = None):
    def decorator(afunc: Callable) -> Any:
        return CoroSlot(*types, name=name, result=result).agly_patched_function()(afunc)
    
    return decorator

cslot_agly_patched = coro_slot_agly_patched
cslotaglyp = coro_slot_agly_patched
cslotagp = coro_slot_agly_patched
csagp = coro_slot_gly_patched


def coro_slot_explicit(*types: type, name: Optional[str] = None, result: Optional[str] = None):
    def decorator(coro: Coro) -> Any:
        return CoroSlot(*types, name=name, result=result).explicit_coro()(coro)
    
    return decorator

cslot_explicit = coro_slot_explicit
cslotex = coro_slot_explicit
csex = coro_slot_explicit


def qt_exec_in_coro(func: Callable, default_priority: CoroPriority = CoroPriority.normal) -> Callable:
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
        if isinstance(app_or_tuple, QApplication):
            app = app_or_tuple
        elif isinstance(app_or_tuple, tuple):
            app, on_exit = app_or_tuple
        else:
            raise RuntimeError("qt_exec_in_coro must return either QApplication or (QApplication, on_exit) tuple")
        
        # Run the event loop
        ret = i(RunCoro, cs_coro(execa), app, default_priority)
        ret = i(RunCoro, cs_coro(on_exit), ret)
        i(ShutdownLoop)
        return ret
    
    return cs_coro(wrapper)


async def aqt_exec_in_coro(func: Callable, default_priority: CoroPriority = CoroPriority.normal) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        i: Interface = current_interface()
        await i(AsyncioLoopRequest().ensure_loop(interrupt_when_no_requests=True))
        await i(AsyncioLoopRequest().turn_on_loops_intercommunication())

        app_or_tuple = func(*args, **kwargs)
        on_exit = lambda ret: ret
        if isinstance(app_or_tuple, QApplication):
            app = app_or_tuple
        else:
            app, on_exit = app_or_tuple
        
        ret = await i(RunCoro, cs_coro(execa), app, default_priority)
        ret = await i(RunCoro, cs_coro(on_exit), ret)
        await i(ShutdownLoop)
        return ret
    
    return cs_acoro(wrapper)


class CoroThreadWorker(QObject):
    def __init__(self, worker: AnyWorker) -> None:
        super().__init__()
        self._worker: AnyWorker = worker
        self._cs: CoroScheduler = None
        self.allowed_to_run = False

    def run(self):
        self.allowed_to_run = True
        async def my_worker_wrapper(i: Interface, worker):
            self._cs = current_coro_scheduler()
            await i(RunCoro, self.setup)
            await i(RunCoro, worker)
        
        run_in_loop(my_worker_wrapper, self._worker)
    
    async def setup(self, i: Interface):
        await i(AsyncioLoopRequest().ensure_loop(interrupt_when_no_requests=True))
        await i(AsyncioLoopRequest().turn_on_loops_intercommunication())

    def stop(self):
        if not self.allowed_to_run:
            return

        self.allowed_to_run = False
        async def coro(i: Interface):
            await i(ShutdownLoop)
        
        if self._cs is not None:
            service: PutCoro = self._cs.get_service_instance(PutCoro)
            return service._add_direct_request(coro)


class CoroThread(QThread):
    def __init__(self, parent, worker: CoroThreadWorker) -> None:
        super().__init__(parent)
        self._worker: CoroThreadWorker = worker
        self._worker.moveToThread(self)
        self.started.connect(self._worker.run)
    
    def stop(self):
        self.quit()
        self.wait()


class CoroThreadWithWorker(CoroThreadWorker):
    def __init__(self, parent, worker: AnyWorker) -> None:
        super().__init__(worker)
        self._thread: CoroThread = CoroThread(parent, self)
    
    def start(self):
        self._thread.start()
    
    def stop(self):
        super().stop()
        self._thread.stop()
