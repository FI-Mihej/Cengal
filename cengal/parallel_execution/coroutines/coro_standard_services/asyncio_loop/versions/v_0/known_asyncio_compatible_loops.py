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


__all__ = ['prepare_loop', 'restore_loop', 'DerivedFromProactorEventLoop', 'DerivedFromSelectorEventLoop', 'DerivedFromUVLoop']


from cengal.parallel_execution.coroutines.coro_scheduler import CoroScheduler, Interface, Coro, AnyWorker, current_interface, current_coro_scheduler, cs_coro, cs_acoro
from cengal.data_manipulation.conversion.reinterpret_cast import reinterpret_cast
from cengal.data_manipulation.conversion.reinterpret_cast_management.manager import BaseAutoDerivedObjWrapper
from asyncio import SelectorEventLoop, AbstractEventLoop
_proactor_present = False
try:
    from asyncio import ProactorEventLoop
    _proactor_present = True
except ImportError:
    pass

from uvloop import Loop as UVLoop
from typing import Type, Tuple, Dict, Callable, Any


def call_soon(self, callback, *args, **kwargs):
    from .asyncio_loop import AsyncioLoop
    cs: CoroScheduler = self._cs
    service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
    service.register_new_asyncio_request()
    return SelectorEventLoop.call_soon(self, callback, *args, **kwargs)

def call_later(self, delay, callback, *args, **kwargs):
    from .asyncio_loop import AsyncioLoop
    cs: CoroScheduler = self._cs
    service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
    service.register_new_asyncio_request()
    return SelectorEventLoop.call_later(self, delay, callback, *args, **kwargs)

def call_at(self, when, callback, *args, **kwargs):
    from .asyncio_loop import AsyncioLoop
    cs: CoroScheduler = self._cs
    service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
    service.register_new_asyncio_request()
    return SelectorEventLoop.call_at(self, when, callback, *args, **kwargs)

# Method scheduling a coroutine object: create a task.

def create_task(self, coro, **kwargs):
    from .asyncio_loop import AsyncioLoop
    cs: CoroScheduler = self._cs
    service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
    service.register_new_asyncio_request()
    return SelectorEventLoop.create_task(self, coro, **kwargs)

# Methods for interacting with threads.

def call_soon_threadsafe(self, callback, *args, **kwargs):
    from .asyncio_loop import AsyncioLoop
    cs: CoroScheduler = self._cs
    service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
    service.register_new_asyncio_request()
    return SelectorEventLoop.call_soon_threadsafe(self, callback, *args, **kwargs)

def run_in_executor(self, executor, func, *args):
    from .asyncio_loop import AsyncioLoop
    cs: CoroScheduler = self._cs
    service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
    service.register_new_asyncio_request()
    return SelectorEventLoop.run_in_executor(self, executor, func, *args)

def add_reader(self, fd, callback, *args):
    from .asyncio_loop import AsyncioLoop
    cs: CoroScheduler = self._cs
    service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
    service.register_new_asyncio_request()
    return SelectorEventLoop.add_reader(self, fd, callback, *args)

def add_writer(self, fd, callback, *args):
    from .asyncio_loop import AsyncioLoop
    cs: CoroScheduler = self._cs
    service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
    service.register_new_asyncio_request()
    return SelectorEventLoop.add_writer(self, fd, callback, *args)

# Signal handling.

def add_signal_handler(self, sig, callback, *args):
    from .asyncio_loop import AsyncioLoop
    cs: CoroScheduler = self._cs
    service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
    service.register_new_asyncio_request()
    return SelectorEventLoop.add_signal_handler(self, sig, callback, *args)


class LoopWrapper(BaseAutoDerivedObjWrapper):
    def wrapping_required(self, obj: Any, base_type: Type, fields: Tuple[str], planned_type_name: str) -> bool:
        return issubclass(base_type, AbstractEventLoop)
    
    def methods(self, obj: Any, base_type: Type, fields: Tuple[str]) -> Dict[str, Callable]:
        return {
            'call_soon': call_soon,
            'call_later': call_later,
            'call_at': call_at,
            'create_task': create_task,
            'call_soon_threadsafe': call_soon_threadsafe,
            'run_in_executor': run_in_executor,
            'add_reader': add_reader,
            'add_writer': add_writer,
            'add_signal_handler': add_signal_handler,
        }


_lw: LoopWrapper = LoopWrapper()


def prepare_loop(loop: AbstractEventLoop) -> Type:
    if _proactor_present and type(loop) is ProactorEventLoop:
        reinterpret_cast(DerivedFromProactorEventLoop, loop)
        loop._cs = current_coro_scheduler()
        return ProactorEventLoop
    elif type(loop) is SelectorEventLoop:
        reinterpret_cast(DerivedFromSelectorEventLoop, loop)
        loop._cs = current_coro_scheduler()
        return SelectorEventLoop
    elif type(loop) is UVLoop:
        reinterpret_cast(DerivedFromUVLoop, loop)
        loop._cs = current_coro_scheduler()
        return UVLoop
    elif isinstance(loop, AbstractEventLoop):
        original_type: Type = type(loop)
        _lw(loop)
        loop._cs = current_coro_scheduler()
        return original_type
    else:
        raise TypeError('Unknown loop type: {}'.format(type(loop)))


def restore_loop(loop: AbstractEventLoop, original_type: Type) -> None:
    reinterpret_cast(original_type, loop)


if _proactor_present:
    class DerivedFromProactorEventLoop(ProactorEventLoop):
        def call_soon(self, callback, *args, **kwargs):
            from .asyncio_loop import AsyncioLoop
            cs: CoroScheduler = self._cs
            service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
            service.register_new_asyncio_request()
            return ProactorEventLoop.call_soon(self, callback, *args, **kwargs)

        def call_later(self, delay, callback, *args, **kwargs):
            from .asyncio_loop import AsyncioLoop
            cs: CoroScheduler = self._cs
            service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
            service.register_new_asyncio_request()
            return ProactorEventLoop.call_later(self, delay, callback, *args, **kwargs)

        def call_at(self, when, callback, *args, **kwargs):
            from .asyncio_loop import AsyncioLoop
            cs: CoroScheduler = self._cs
            service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
            service.register_new_asyncio_request()
            return ProactorEventLoop.call_at(self, when, callback, *args, **kwargs)

        # Method scheduling a coroutine object: create a task.

        def create_task(self, coro, **kwargs):
            from .asyncio_loop import AsyncioLoop
            cs: CoroScheduler = self._cs
            service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
            service.register_new_asyncio_request()
            return ProactorEventLoop.create_task(self, coro, **kwargs)

        # Methods for interacting with threads.

        def call_soon_threadsafe(self, callback, *args, **kwargs):
            from .asyncio_loop import AsyncioLoop
            cs: CoroScheduler = self._cs
            service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
            service.register_new_asyncio_request()
            return ProactorEventLoop.call_soon_threadsafe(self, callback, *args, **kwargs)

        def run_in_executor(self, executor, func, *args):
            from .asyncio_loop import AsyncioLoop
            cs: CoroScheduler = self._cs
            service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
            service.register_new_asyncio_request()
            return ProactorEventLoop.run_in_executor(self, executor, func, *args)

        def add_reader(self, fd, callback, *args):
            from .asyncio_loop import AsyncioLoop
            cs: CoroScheduler = self._cs
            service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
            service.register_new_asyncio_request()
            return ProactorEventLoop.add_reader(self, fd, callback, *args)

        def add_writer(self, fd, callback, *args):
            from .asyncio_loop import AsyncioLoop
            cs: CoroScheduler = self._cs
            service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
            service.register_new_asyncio_request()
            return ProactorEventLoop.add_writer(self, fd, callback, *args)

        # Signal handling.

        def add_signal_handler(self, sig, callback, *args):
            from .asyncio_loop import AsyncioLoop
            cs: CoroScheduler = self._cs
            service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
            service.register_new_asyncio_request()
            return ProactorEventLoop.add_signal_handler(self, sig, callback, *args)


class DerivedFromSelectorEventLoop(SelectorEventLoop):
    def call_soon(self, callback, *args, **kwargs):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return SelectorEventLoop.call_soon(self, callback, *args, **kwargs)

    def call_later(self, delay, callback, *args, **kwargs):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return SelectorEventLoop.call_later(self, delay, callback, *args, **kwargs)

    def call_at(self, when, callback, *args, **kwargs):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return SelectorEventLoop.call_at(self, when, callback, *args, **kwargs)

    # Method scheduling a coroutine object: create a task.

    def create_task(self, coro, **kwargs):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return SelectorEventLoop.create_task(self, coro, **kwargs)

    # Methods for interacting with threads.

    def call_soon_threadsafe(self, callback, *args, **kwargs):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return SelectorEventLoop.call_soon_threadsafe(self, callback, *args, **kwargs)

    def run_in_executor(self, executor, func, *args):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return SelectorEventLoop.run_in_executor(self, executor, func, *args)

    def add_reader(self, fd, callback, *args):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return SelectorEventLoop.add_reader(self, fd, callback, *args)

    def add_writer(self, fd, callback, *args):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return SelectorEventLoop.add_writer(self, fd, callback, *args)

    # Signal handling.

    def add_signal_handler(self, sig, callback, *args):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return SelectorEventLoop.add_signal_handler(self, sig, callback, *args)


class DerivedFromUVLoop(UVLoop):
    def call_soon(self, callback, *args, context=None):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return UVLoop.call_soon(self, callback, *args, context=context)

    def call_later(self, delay, callback, *args, context=None):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return UVLoop.call_later(self, delay, callback, *args, context=context)

    def call_at(self, when, callback, *args, context=None):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return UVLoop.call_at(self, when, callback, *args, context=context)

    # Method scheduling a coroutine object: create a task.

    def create_task(self, coro, *, name=None, context=None):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return UVLoop.create_task(self, coro, name=name, context=context)

    # Methods for interacting with threads.

    def call_soon_threadsafe(self, callback, *args, context=None):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return UVLoop.call_soon_threadsafe(self, callback, *args, context=context)

    def run_in_executor(self, executor, func, *args):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return UVLoop.run_in_executor(self, executor, func, *args)

    def add_reader(self, fd, callback, *args):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return UVLoop.add_reader(self, fd, callback, *args)

    def add_writer(self, fd, callback, *args):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return UVLoop.add_writer(self, fd, callback, *args)

    # Signal handling.

    def add_signal_handler(self, sig, callback, *args):
        from .asyncio_loop import AsyncioLoop
        cs: CoroScheduler = self._cs
        service: AsyncioLoop = cs.get_service_instance(AsyncioLoop)
        service.register_new_asyncio_request()
        return UVLoop.add_signal_handler(self, sig, callback, *args)
