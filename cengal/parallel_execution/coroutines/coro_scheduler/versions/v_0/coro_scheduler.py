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


__all__ = [
    'Counter', 'Iterable', 'ServiceResponseTypeVar', 'ServiceType', 'TypedServiceType', 'NormalizableServiceType', 
    'ItemID', 'CoroID', 'Worker', 'GreenetCoro', 'ACoro', 'Coro', 'OnCoroDelHandler', 'cs_coro', 'cs_acoro',
    'OutsideCoroSchedulerContext', 'current_coro_scheduler', 'get_current_coro_scheduler', 'set_primary_coro_scheduler', 
    'PrimaryCoroSchedulerWasNotSet', 'primary_coro_scheduler', 'get_primary_coro_scheduler', 'CoroSchedulerContextIsNotAvailable', 
    'available_coro_scheduler', 'get_available_coro_scheduler', 'WrongTypeOfShedulerError', 'InterfaceIsNotAvailableError', 
    'CurrentCoroIsNotAliveError', 'loop_with_backup_loop', 'get_loop_with_backup_loop', 'loop_with_explicit_loop', 
    'get_loop_with_explicit_loop', 'interface_and_loop_with_backup_loop', 'get_interface_and_loop_with_backup_loop', 
    'interface_and_loop_with_explicit_loop', 'get_interface_and_loop_with_explicit_loop', 'interface_for_an_explicit_loop', 
    'get_interface_for_an_explicit_loop', 'service_with_backup_loop', 'get_service_with_backup_loop', 'service_with_explicit_loop', 
    'get_service_with_explicit_loop', 'service_fast_with_backup_loop', 'get_service_fast_with_backup_loop', 
    'service_fast_with_explicit_loop', 'get_service_fast_with_explicit_loop', 'CoroType', 'ExplicitWorker', 'AnyWorker', 
    'CoroScheduler', 'CoroSchedulerGreenlet', 'CoroSchedulerAwaitable', 'current_interface', 'execute_coro', 'exec_coro', 'ecoro', 'aexecute_coro', 'aexec_coro', 'aecoro', 
    'around_await', 'Request', 'Response', 'DirectResponse', 'Interface', 'InterfaceGreenlet', 'find_coro_type', 
    'InterfaceAsyncAwait', 'InterfaceFake', 'InterfaceFakeAsyncAwait', 'CallerCoroInfo', 'ServiceRequest', 'TypedServiceRequest', 
    'ServiceRequestMethodMixin', 'DualImmediateProcessingServiceMixin', 'WrongServiceRequestError', 'Service', 'TypedService', 
    'CoroWrapperBase', 'CoroWrapperGreenlet', 'CoroWrapperAsyncAwait', 'dlog', 'log_exception_traceback_info', 
    'log_uncatched_exception', 'func_info', 'ServiceProcessingResultExists', 'ServiceProcessingResult', 'ServiceProcessingException', 
    'ServiceProcessingResponse', 'full_func_info_to_dict', 'full_func_info_to_printable_dict', 'GreenletWorkerWrapper', 
    'EntityStatsMixin', 'CoroSchedulerIsCurrentlyDestroingError', 'CoroSchedulerDestroyException', 
    'CoroSchedulerDestroyRequestedException', 'greenlet_awailable', 'GreenletExit'
]

import sys
import os
import inspect
from contextlib import contextmanager
from typing import Coroutine, Dict, Tuple, List, Callable, Awaitable, Any, Optional, Type, Set, Union, Generator, AsyncGenerator, overload, Generic, TypeVar
from enum import Enum
import types
from cengal.time_management.load_best_timer import perf_counter
import traceback
from contextlib import contextmanager
import logging
from datetime import datetime
from cengal.introspection.inspect import get_exception, exception_to_printable_text, is_async
from cengal.code_flow_control.args_manager import args_kwargs
from threading import local
from cengal.time_management.sleep_tools import sleep
from collections import deque
from cengal.code_flow_control.args_manager import EntityArgsHolder, EntityArgsHolderExplicit
from cengal.time_management.cpu_clock_cycles import cpu_clock_cycles
from functools import wraps, update_wrapper


greenlet_awailable: bool = True
try:
    from greenlet import greenlet, GreenletExit
except ImportError:
    greenlet_awailable = False
    class GreenletExit(Exception):
        pass

# greenlet_awailable = False

class Counter:
    def __init__(self):
        self._index = -1  # type: int

    def get(self) -> int:
        self._index += 1
        return self._index


class Iterable:
    def iteration(self) -> bool:
        """
        should return False if ready to stop looping
        :return:
        """
        raise NotImplementedError


ServiceResponseTypeVar = TypeVar('ServiceResponseTypeVar')


ServiceType = Type['Service']
TypedServiceType = Type['TypedService[ServiceResponseTypeVar]']
NormalizableServiceType = Union[Type['Service'], Type['TypedService[ServiceResponseTypeVar]'], Type['ServiceRequest'], Type['TypedServiceRequest[ServiceResponseTypeVar]'], 'Service', 'TypedService[ServiceResponseTypeVar]', 'ServiceRequest', 'TypedServiceRequest[ServiceResponseTypeVar]']
ItemID = int
CoroID = ItemID
Worker = Callable[['Interface'], None]
GreenetCoro = greenlet
ACoro = Union[Awaitable, Coroutine, Generator, AsyncGenerator, Callable]
Coro = Union[GreenetCoro, ACoro]
OnCoroDelHandler = Callable[['CoroWrapperBase'], bool]


def cs_coro(coro_worker: Worker):
    """Decorator. Without arguments. Makes a greenlet Cengal coroutine from a pain function (which don't have an interface parameter)

    Args:
        coro_worker (Worker): _description_
    """
    if is_async(coro_worker):
        async def wrapper(i: Interface, *args, **kwargs):
            return await coro_worker(*args, **kwargs)
            
        coro_worker_sign: inspect.Signature = inspect.signature(coro_worker)
        update_wrapper(wrapper, coro_worker)
        wrapper.__signature__ = coro_worker_sign.replace(parameters=(inspect.Parameter('_interface_param_', inspect.Parameter.POSITIONAL_ONLY),) + tuple(coro_worker_sign.parameters.values()), return_annotation=coro_worker_sign.return_annotation)
        # wrapper.__name__ = coro_worker.__name__
        return wrapper
    else:
        def wrapper(i: Interface, *args, **kwargs):
            return coro_worker(*args, **kwargs)
            
        coro_worker_sign: inspect.Signature = inspect.signature(coro_worker)
        update_wrapper(wrapper, coro_worker)
        wrapper.__signature__ = coro_worker_sign.replace(parameters=(inspect.Parameter('_interface_param_', inspect.Parameter.POSITIONAL_ONLY),) + tuple(coro_worker_sign.parameters.values()), return_annotation=coro_worker_sign.return_annotation)
        # wrapper.__name__ = coro_worker.__name__
        return wrapper


def cs_acoro(coro_aworker: Worker):
    """Decorator. Without arguments. Makes an async Cengal coroutine from an async function (which don't have an interface parameter)

    Args:
        coro_aworker (Worker): _description_
    """    
    if is_async(coro_aworker):
        async def wrapper(i: Interface, *args, **kwargs):
            return await coro_aworker(*args, **kwargs)
            
        coro_worker_sign: inspect.Signature = inspect.signature(coro_aworker)
        update_wrapper(wrapper, coro_aworker)
        wrapper.__signature__ = coro_worker_sign.replace(parameters=(inspect.Parameter('_interface_param_', inspect.Parameter.POSITIONAL_ONLY),) + tuple(coro_worker_sign.parameters.values()), return_annotation=coro_worker_sign.return_annotation)
        # wrapper.__name__ = coro_aworker.__name__
        return wrapper
    else:
        def wrapper(i: Interface, *args, **kwargs):
            return coro_aworker(*args, **kwargs)
            
        coro_worker_sign: inspect.Signature = inspect.signature(coro_aworker)
        update_wrapper(wrapper, coro_aworker)
        wrapper.__signature__ = coro_worker_sign.replace(parameters=(inspect.Parameter('_interface_param_', inspect.Parameter.POSITIONAL_ONLY),) + tuple(coro_worker_sign.parameters.values()), return_annotation=coro_worker_sign.return_annotation)
        wrapper.__name__ = coro_aworker.__name__
        return wrapper


class _ThreadLocalCoroScheduler(local):
    scheduler: Optional['CoroScheduler'] = None


_primary_coro_scheduler: _ThreadLocalCoroScheduler = _ThreadLocalCoroScheduler()
_current_coro_scheduler: _ThreadLocalCoroScheduler = _ThreadLocalCoroScheduler()


_debug_log_counter = 0


def _debug_log(*args, **kwargs):
    print(*args, **kwargs)
    global _debug_log_counter
    _debug_log_counter += 1


def _fake_debug_log(*args, **kwargs):
    pass


dlog = _fake_debug_log
if False and __debug__:
    dlog = _debug_log


def log_exception_traceback_info():
    exception = sys.exc_info()
    formattedTraceback = traceback.format_exception(exception[0], exception[1], exception[2])
    exception = exception[:2] + (formattedTraceback,)
    trace = ''
    for line in exception[2]:
        trace += line
    if __debug__: dlog(trace, file=sys.stderr)
    if __debug__: dlog(exception[0])
    if __debug__: dlog(exception[1])


@contextmanager
def log_uncatched_exception():
    try:
        yield
    except:
        log_exception_traceback_info()
        raise


def func_info(func, full_name: Optional[bool]=True):
    if full_name:
        # return f'{func.__class__}({func.__module__}.{func.__qualname__}) @ {func.__code__.co_filename}:{func.__code__.co_firstlineno}'
        return f'{func.__class__}({func.__qualname__}) @ {func.__code__.co_filename}:{func.__code__.co_firstlineno}'
    else:
        return f'{func.__class__}({func.__qualname__}) @ {os.path.basename(func.__code__.co_filename)}:{func.__code__.co_firstlineno}'


def full_func_info(my):
    if __debug__: dlog(repr(my), 
        my.__module__, 
        my.__name__, 
        my.__qualname__, 
        my.__annotations__, 
        my.__class__, 
        my.__closure__, 
        my.__code__, 
        my.__code__.co_argcount,
        my.__code__.co_cellvars,
        my.__code__.co_code,
        my.__code__.co_consts,
        my.__code__.co_filename,
        my.__code__.co_firstlineno,
        my.__code__.co_flags,
        my.__code__.co_freevars,
        my.__code__.co_kwonlyargcount,
        my.__code__.co_lnotab,
        my.__code__.co_name,
        my.__code__.co_names,
        my.__code__.co_nlocals,
        my.__code__.co_stacksize,
        my.__code__.co_varnames,
        )


def full_func_info_to_dict(my):
    return {
        'repr': repr(my), 
        'module': str(my.__module__), 
        'name': str(my.__name__), 
        'qualname': str(my.__qualname__), 
        'annotations': str(my.__annotations__), 
        'class': str(my.__class__), 
        'closure': str(my.__closure__), 
        'code': str(my.__code__), 
        'co_argcount': str(my.__code__.co_argcount),
        'co_cellvars': str(my.__code__.co_cellvars),
        'co_code': str(my.__code__.co_code),
        'co_consts': str(my.__code__.co_consts),
        'co_filename': str(my.__code__.co_filename),
        'co_firstlineno': str(my.__code__.co_firstlineno),
        'co_flags': str(my.__code__.co_flags),
        'co_freevars': str(my.__code__.co_freevars),
        'co_kwonlyargcount': str(my.__code__.co_kwonlyargcount),
        'co_lnotab': str(my.__code__.co_lnotab),
        'co_name': str(my.__code__.co_name),
        'co_names': str(my.__code__.co_names),
        'co_nlocals': str(my.__code__.co_nlocals),
        'co_stacksize': str(my.__code__.co_stacksize),
        'co_varnames': str(my.__code__.co_varnames),
    }


def full_func_info_to_printable_dict(func: Callable) -> Dict[str, str]:
    func_info: Dict[str, str] = full_func_info_to_dict(func)
    good_keys = {'module', 'qualname', 'class', 'co_filename', 'co_firstlineno'}
    result: Dict[str, str] = dict()
    for key, value in func_info.items():
        if key in good_keys:
            result[key] = value
    
    return result


class OutsideCoroSchedulerContext(Exception):
    pass


def current_coro_scheduler() -> 'CoroScheduler':
    if _current_coro_scheduler.scheduler is None:
        raise OutsideCoroSchedulerContext
    
    return _current_coro_scheduler.scheduler


def get_current_coro_scheduler() -> Optional['CoroScheduler']:
    return _current_coro_scheduler.scheduler


def set_primary_coro_scheduler(coro_scheduler: 'CoroScheduler'):
    _primary_coro_scheduler.scheduler = coro_scheduler


class PrimaryCoroSchedulerWasNotSet(Exception):
    pass


def primary_coro_scheduler() -> 'CoroScheduler':
    if _primary_coro_scheduler.scheduler is None:
        raise PrimaryCoroSchedulerWasNotSet
    
    return _primary_coro_scheduler.scheduler


def get_primary_coro_scheduler() -> Optional['CoroScheduler']:
    return _primary_coro_scheduler.scheduler


class CoroSchedulerContextIsNotAvailable(Exception):
    pass


def available_coro_scheduler() -> 'CoroScheduler':
    if _current_coro_scheduler.scheduler:
        return _current_coro_scheduler.scheduler
    elif _primary_coro_scheduler.scheduler:
        return _primary_coro_scheduler.scheduler
    else:
        raise CoroSchedulerContextIsNotAvailable


def get_available_coro_scheduler() -> Optional['CoroScheduler']:
    if _current_coro_scheduler.scheduler:
        return _current_coro_scheduler.scheduler
    elif _primary_coro_scheduler.scheduler:
        return _primary_coro_scheduler.scheduler
    else:
        return None


class WrongTypeOfShedulerError(Exception):
    pass


class InterfaceIsNotAvailableError(Exception):
    pass


class CurrentCoroIsNotAliveError(Exception):
    pass


# ==========================================================


def loop_with_backup_loop(backup_scheduler: Optional['CoroScheduler'] = None) -> 'CoroScheduler':
    if backup_scheduler is not None:
        if not isinstance(backup_scheduler, CoroScheduler):
            raise WrongTypeOfShedulerError(f'Wrong type of the backup_scheduler ({repr(backup_scheduler)}): {type(backup_scheduler)}')

    loop = CoroScheduler.current_loop()
    if loop is None:
        # Outside the loop
        loop = get_available_coro_scheduler()
        if loop is None:
            loop = backup_scheduler

    if loop is None:
        raise CoroSchedulerContextIsNotAvailable
    
    return loop


def get_loop_with_backup_loop(backup_scheduler: Optional['CoroScheduler'] = None) -> Optional['CoroScheduler']:
    if backup_scheduler is not None:
        if not isinstance(backup_scheduler, CoroScheduler):
            raise WrongTypeOfShedulerError(f'Wrong type of the backup_scheduler ({repr(backup_scheduler)}): {type(backup_scheduler)}')

    loop = CoroScheduler.current_loop()
    if loop is None:
        # Outside the loop
        loop = get_available_coro_scheduler()
        if loop is None:
            loop = backup_scheduler
    
    return loop


def loop_with_explicit_loop(explicit_scheduler: Optional['CoroScheduler'] = None) -> 'CoroScheduler':
    loop = explicit_scheduler
    current_loop = CoroScheduler.current_loop()
    if loop is None:
        loop = current_loop
        if loop is None:
            # Outside the loop
            loop = get_available_coro_scheduler()
    else:
        if not isinstance(loop, CoroScheduler):
            raise WrongTypeOfShedulerError(f'Wrong type of the explicit_scheduler ({repr(loop)}): {type(loop)}')

    if loop is None:
        raise CoroSchedulerContextIsNotAvailable
    
    return loop


def get_loop_with_explicit_loop(explicit_scheduler: Optional['CoroScheduler'] = None) -> Optional['CoroScheduler']:
    loop = explicit_scheduler
    current_loop = CoroScheduler.current_loop()
    if loop is None:
        loop = current_loop
        if loop is None:
            # Outside the loop
            loop = get_available_coro_scheduler()
    else:
        if not isinstance(loop, CoroScheduler):
            raise WrongTypeOfShedulerError(f'Wrong type of the explicit_scheduler ({repr(loop)}): {type(loop)}')
    
    return loop
# ==========================================================


def interface_and_loop_with_backup_loop(backup_scheduler: Optional['CoroScheduler'] = None) -> Tuple['CoroScheduler', 'Interface', bool]:
    if backup_scheduler is not None:
        if not isinstance(backup_scheduler, CoroScheduler):
            raise WrongTypeOfShedulerError(f'Wrong type of the backup_scheduler ({repr(backup_scheduler)}): {type(backup_scheduler)}')

    loop = CoroScheduler.current_loop()
    if loop is None:
        # Outside the loop
        interface = None
        loop = get_available_coro_scheduler()
        if loop is None:
            loop = backup_scheduler
    else:
        # In the loop (in coroutine or in the service)
        interface = loop.current_interface()

    if loop is None:
        raise CoroSchedulerContextIsNotAvailable
    
    if interface is None:
        raise InterfaceIsNotAvailableError
    
    coro_alive: bool = False
    if interface is not None:
        if interface._coro:
            coro_alive = True
    
    if not coro_alive:
        raise CurrentCoroIsNotAliveError
    
    return loop, interface, coro_alive


def get_interface_and_loop_with_backup_loop(backup_scheduler: Optional['CoroScheduler'] = None) -> Tuple[Optional['CoroScheduler'], Optional['Interface'], bool]:
    if backup_scheduler is not None:
        if not isinstance(backup_scheduler, CoroScheduler):
            raise WrongTypeOfShedulerError(f'Wrong type of the backup_scheduler ({repr(backup_scheduler)}): {type(backup_scheduler)}')

    loop = CoroScheduler.current_loop()
    if loop is None:
        # Outside the loop
        interface = None
        loop = get_available_coro_scheduler()
        if loop is None:
            loop = backup_scheduler
    else:
        # In the loop (in coroutine or in the service)
        interface = loop.current_interface()
    
    coro_alive: bool = False
    if interface is not None:
        if interface._coro:
            coro_alive = True
    
    return loop, interface, coro_alive


def interface_and_loop_with_explicit_loop(explicit_scheduler: Optional['CoroScheduler'] = None) -> Tuple['CoroScheduler', 'Interface', bool]:
    loop = explicit_scheduler
    current_loop = CoroScheduler.current_loop()
    interface = None
    if loop is None:
        loop = current_loop
        if loop is None:
            # Outside the loop
            loop = get_available_coro_scheduler()
        else:
            # In the loop (in coroutine or in the service)
            interface = loop.current_interface()
    else:
        if isinstance(loop, CoroScheduler):
            if loop is current_loop:
                interface = loop.current_interface()
        else:
            raise WrongTypeOfShedulerError(f'Wrong type of the explicit_scheduler ({repr(loop)}): {type(loop)}')

    if loop is None:
        raise CoroSchedulerContextIsNotAvailable
    
    if interface is None:
        raise InterfaceIsNotAvailableError
    
    coro_alive: bool = False
    if interface is not None:
        if interface._coro:
            coro_alive = True
    
    if not coro_alive:
        raise CurrentCoroIsNotAliveError
    
    return loop, interface, coro_alive


def get_interface_and_loop_with_explicit_loop(explicit_scheduler: Optional['CoroScheduler'] = None) -> Tuple[Optional['CoroScheduler'], Optional['Interface'], bool]:
    loop = explicit_scheduler
    current_loop = CoroScheduler.current_loop()
    interface = None
    if loop is None:
        loop = current_loop
        if loop is None:
            # Outside the loop
            loop = get_available_coro_scheduler()
        else:
            # In the loop (in coroutine or in the service)
            interface = loop.current_interface()
    else:
        if isinstance(loop, CoroScheduler):
            if loop is current_loop:
                interface = loop.current_interface()
        else:
            raise WrongTypeOfShedulerError(f'Wrong type of the explicit_scheduler ({repr(loop)}): {type(loop)}')
    
    coro_alive: bool = False
    if interface is not None:
        if interface._coro:
            coro_alive = True
    
    return loop, interface, coro_alive


def interface_for_an_explicit_loop(explicit_scheduler: 'CoroScheduler') -> Tuple['CoroScheduler', 'Interface', bool]:
    loop = explicit_scheduler
    interface = None
    if loop is None:
        raise CoroSchedulerContextIsNotAvailable
    else:
        if isinstance(loop, CoroScheduler):
            if loop is CoroScheduler.current_loop():
                interface = loop.current_interface()
        else:
            raise WrongTypeOfShedulerError(f'Wrong type of the explicit_scheduler ({repr(loop)}): {type(loop)}')
    
    if interface is None:
        raise InterfaceIsNotAvailableError
    
    coro_alive: bool = False
    if interface is not None:
        if interface._coro:
            coro_alive = True
    
    if not coro_alive:
        raise CurrentCoroIsNotAliveError
    
    return loop, interface, coro_alive


def get_interface_for_an_explicit_loop(explicit_scheduler: 'CoroScheduler') -> Tuple[Optional['CoroScheduler'], Optional['Interface'], bool]:
    loop = explicit_scheduler
    interface = None
    if loop is not None:
        if isinstance(loop, CoroScheduler):
            if loop is CoroScheduler.current_loop():
                interface = loop.current_interface()
        else:
            raise WrongTypeOfShedulerError(f'Wrong type of the explicit_scheduler ({repr(loop)}): {type(loop)}')
    
    coro_alive: bool = False
    if interface is not None:
        if interface._coro:
            coro_alive = True
    
    return loop, interface, coro_alive


# ==========================================================

def service_with_backup_loop(service_type: Type['Service'], backup_scheduler: Optional['CoroScheduler'] = None) -> 'Service':
    if backup_scheduler is not None:
        if not isinstance(backup_scheduler, CoroScheduler):
            raise WrongTypeOfShedulerError(f'Wrong type of the backup_scheduler ({repr(backup_scheduler)}): {type(backup_scheduler)}')

    loop = CoroScheduler.current_loop()
    if loop is None:
        # Outside the loop
        loop = get_available_coro_scheduler()
        if loop is None:
            loop = backup_scheduler

    if loop is None:
        raise CoroSchedulerContextIsNotAvailable

    return loop.get_service_instance(service_type)


def get_service_with_backup_loop(service_type: Type['Service'], backup_scheduler: Optional['CoroScheduler'] = None) -> Optional['Service']:
    if backup_scheduler is not None:
        if not isinstance(backup_scheduler, CoroScheduler):
            raise WrongTypeOfShedulerError(f'Wrong type of the backup_scheduler ({repr(backup_scheduler)}): {type(backup_scheduler)}')

    loop = CoroScheduler.current_loop()
    if loop is None:
        # Outside the loop
        loop = get_available_coro_scheduler()
        if loop is None:
            loop = backup_scheduler

    if loop is None:
        return None
    else:
        return loop.get_service_instance(service_type)


def service_with_explicit_loop(service_type: Type['Service'], explicit_scheduler: Optional['CoroScheduler'] = None) -> 'Service':
    loop = explicit_scheduler
    current_loop = CoroScheduler.current_loop()
    if loop is None:
        loop = current_loop
        if loop is None:
            # Outside the loop
            loop = get_available_coro_scheduler()
    else:
        if not isinstance(loop, CoroScheduler):
            raise WrongTypeOfShedulerError(f'Wrong type of the explicit_scheduler ({repr(loop)}): {type(loop)}')

    if loop is None:
        raise CoroSchedulerContextIsNotAvailable

    return loop.get_service_instance(service_type)


def get_service_with_explicit_loop(service_type: Type['Service'], explicit_scheduler: Optional['CoroScheduler'] = None) -> Optional['Service']:
    loop = explicit_scheduler
    current_loop = CoroScheduler.current_loop()
    if loop is None:
        loop = current_loop
        if loop is None:
            # Outside the loop
            loop = get_available_coro_scheduler()
    else:
        if not isinstance(loop, CoroScheduler):
            raise WrongTypeOfShedulerError(f'Wrong type of the explicit_scheduler ({repr(loop)}): {type(loop)}')

    if loop is None:
        return None
    else:
        return loop.get_service_instance(service_type)
# ==========================================================


def service_fast_with_backup_loop(service_type: Type['Service'], backup_scheduler: Optional['CoroScheduler'] = None) -> 'Service':
    if backup_scheduler is not None:
        if not isinstance(backup_scheduler, CoroScheduler):
            raise WrongTypeOfShedulerError(f'Wrong type of the backup_scheduler ({repr(backup_scheduler)}): {type(backup_scheduler)}')

    loop = CoroScheduler.current_loop()
    if loop is None:
        # Outside the loop
        loop = get_available_coro_scheduler()
        if loop is None:
            loop = backup_scheduler

    if loop is None:
        raise CoroSchedulerContextIsNotAvailable

    return loop.get_service_instance_fast(service_type)


def get_service_fast_with_backup_loop(service_type: Type['Service'], backup_scheduler: Optional['CoroScheduler'] = None) -> Optional['Service']:
    if backup_scheduler is not None:
        if not isinstance(backup_scheduler, CoroScheduler):
            raise WrongTypeOfShedulerError(f'Wrong type of the backup_scheduler ({repr(backup_scheduler)}): {type(backup_scheduler)}')

    loop = CoroScheduler.current_loop()
    if loop is None:
        # Outside the loop
        loop = get_available_coro_scheduler()
        if loop is None:
            loop = backup_scheduler

    if loop is None:
        return None
    else:
        return loop.get_service_instance_fast(service_type)


def service_fast_with_explicit_loop(service_type: Type['Service'], explicit_scheduler: Optional['CoroScheduler'] = None) -> 'Service':
    loop = explicit_scheduler
    current_loop = CoroScheduler.current_loop()
    if loop is None:
        loop = current_loop
        if loop is None:
            # Outside the loop
            loop = get_available_coro_scheduler()
    else:
        if not isinstance(loop, CoroScheduler):
            raise WrongTypeOfShedulerError(f'Wrong type of the explicit_scheduler ({repr(loop)}): {type(loop)}')

    if loop is None:
        raise CoroSchedulerContextIsNotAvailable

    return loop.get_service_instance_fast(service_type)


def get_service_fast_with_explicit_loop(service_type: Type['Service'], explicit_scheduler: Optional['CoroScheduler'] = None) -> Optional['Service']:
    loop = explicit_scheduler
    current_loop = CoroScheduler.current_loop()
    if loop is None:
        loop = current_loop
        if loop is None:
            # Outside the loop
            loop = get_available_coro_scheduler()
    else:
        if not isinstance(loop, CoroScheduler):
            raise WrongTypeOfShedulerError(f'Wrong type of the explicit_scheduler ({repr(loop)}): {type(loop)}')

    if loop is None:
        return None
    else:
        return loop.get_service_instance_fast(service_type)
# ==========================================================


class CoroType(Enum):
    auto = 0
    awaitable = 1
    greenlet = 2


class ExplicitWorker:
    def __init__(self, coro_type: CoroType, worker: Worker) -> None:
        self.coro_type: CoroType = coro_type
        self.worker: Worker = worker


AnyWorker = Union[ExplicitWorker, Worker]


@types.coroutine
def yield_task_from_asyncawait(request: 'Request') -> 'Response':
    response = yield request  # type: Response
    return response


class EntityStatsMixin:
    class StatsLevel(Enum):
        info = 0
        debug = 1
    
    def get_entity_stats(self, stats_level: 'EntityStatsMixin.StatsLevel') -> Tuple[str, Dict[str, Any]]:
        raise NotImplementedError


class CoroSchedulerIsCurrentlyDestroingError(Exception):
    pass


class CoroSchedulerDestroyException(Exception):
    pass


class CoroSchedulerDestroyRequestedException(Exception):
    pass


class CoroSchedulerBase(Iterable, EntityStatsMixin):
    def __init__(self, logger: Optional[logging.Logger] = None):
        self.in_iteration = False
        self.services = dict()                                    # type: Dict[ServiceType, Service]
        self.live_services = dict()                               # type: Dict[ServiceType, Service]
        self.live_low_latency_services = dict()                               # type: Dict[ServiceType, Service]
        self.requests = list()                                    # type: List[Request]
        self.responses = list()                                   # type: List[Response]
        self.new_born_coroutines = list()                         # type: List[CoroWrapperBase]
        self.coroutines = dict()                                  # type: Dict[CoroID, CoroWrapperBase]
        self.coro_counter = Counter()                             # type: Counter
        self.services_in_work = 0                                 # type: int
        self.services_in_foreground_work: int = 0
        self.services_in_active_state = 0                                 # type: int
        self.services_in_active_state_list = list()               # uncomment lines in code for a debutting purposes (when some service prevents loop to go to sleep)
        self.time_left_before_next_event: Optional[float] = None  # type: Optional[float]
        self.coro_on_del_handlers = set()                         # type: Set[Callable]
        self.current_coro_interface = None                        # type: Optional['Interface']
        self.current_coro_wrapper: CoroWrapperBase = None
        self.suppress_coro_exceptions = True                      # type: bool
        self.iteration_index: int = 0
        self.context_switches = 0                                 # type: int
        self.current_coro_start_time: Optional[float] = None
        self.coro_execution_time: Dict[int, float] = dict()
        self.coro_longest_execution_time: Dict[int, float] = dict()
        self.loop_iteration_start_time = 0.0
        self.need_to_measure_loop_iteration_time = False          # type: bool
        self.need_to_measure_coro_time = False                    # type: bool
        self.need_to_gather_coro_history = False                  # type: bool
        self.permitted_use_put_coro_from_coro = False             # type: bool
        self.get_coro_start_time = self._fake_perf_counter
        self.get_loop_iteration_start_time = self._fake_perf_counter
        self.coro_history_gatherer = self._fake_method
        self.on_woke_up_callback = self._fake_method
        self.coro_on_start_handlers = set()
        self.global_on_start_handlers_turned_on = False
        self.execute_global_on_start_handlers = self._fake_execute_global_on_start_handlers
        self.coro_workers_history = dict()                                # type: Dict[Worker, Set[CoroID]]
        self.coro_full_history = dict()                                # type: Dict[CoroID, CoroWrapperBase]
        self.run_low_latency_services = self._fake_run_low_latency_services
        if logger is None:
            self.logger = logging.getLogger(f'cengal.coro_scheduler.{id(self)}')
            self.logger_stream_handler = logging.StreamHandler()
            self.logger.addHandler(self.logger_stream_handler)
            self.logger.setLevel(logging.INFO)
        else:
            self.logger = logger
        
        self._in_work: bool = None
        self._destroyed: bool = False
        self.services_impostrors: Dict = dict()
        self.keep_coro_execution_time_between_iterations = False
        self.keep_coro_longest_execution_time_between_iterations = False
        self.keep_coro_workers_history_between_iterations = False
        self.keep_coro_full_history_between_iterations = False
        self.loop_iteration_delta_time = 0.0
        self.suppress_warnings_about_responses_to_not_existant_coroutines: bool = False
        self.use_internal_sleep: bool = True
        self.high_cpu_utilisation_mode: bool = False  # For an effective, low-latency, inter-thread switching when there is more active high-CPU utilizing threads than CPU cores. Should be switched off for GUI applications in order to to decrease CPU utilization.
        self.foreground_coro_num: int = 0
        self.on_idle_handlers: Set[Callable] = set()
        self.idle_managers_num: int = 0
        self.on_wrong_request: Optional[Callable] = None
        self.get_service_by_type: Callable = self.get_service_by_type_impl
        self.get_service_instance_fast: Callable = self.get_service_instance_fast_impl
        self.get_service_instance: Callable = self.get_service_instance_impl
        self.make_service_live_fast: Callable = self.make_service_live_fast_impl
        self.make_service_live: Callable = self.make_service_live_impl
        self.make_service_dead_fast: Callable = self.make_service_dead_fast_impl
        self.make_service_dead: Callable = self.make_service_dead_impl
        self.sliding_window = deque(maxlen=1000)
        self.need_to_log_loop_start_and_end: bool = True
        self.on_destroyed_handlers: Set[Callable] = set()
        self._coroutines_can_switch_directly: bool = False
        self._next_coroutine: Optional[CoroWrapperBase] = None
        self._is_current_coro_was_new_born: Union[bool, None] = None

    def get_entity_stats(self, stats_level: 'EntityStatsMixin.StatsLevel' = EntityStatsMixin.StatsLevel.debug) -> Tuple[str, Dict[str, Any]]:
        if EntityStatsMixin.StatsLevel.info == stats_level:
            func_info = full_func_info_to_printable_dict
        else:
            func_info = full_func_info_to_dict
        
        services_stats = dict()
        for service in self.services.values():
            if isinstance(service, EntityStatsMixin):
                name, info = service.get_entity_stats(stats_level)
                services_stats[name] = info

        return type(self).__name__, {
            'loop': {
                'services': {
                    'num': len(self.services),
                    'list': [service_type.__name__ for service_type in self.services.keys()],
                },
                'live services': {
                    'in work num': self.services_in_work,
                    'in foreground work num': self.services_in_foreground_work,
                    'services in active state': self.services_in_active_state,
                    'idleble services': self.services_in_work - self.services_in_active_state,
                    'num': len(self.live_services),
                    'list': [service_type.__name__ for service_type in self.live_services.keys()],
                },
                'live low latency services': {
                    'num': len(self.live_low_latency_services),
                    'list': [service_type.__name__ for service_type in self.live_low_latency_services.keys()],
                },
                'new born coroutines': {
                    'num': len(self.new_born_coroutines),
                    "list": {
                        wrapper.coro_id: {
                            "func_info": func_info(self.purify_worker(wrapper.worker)),
                            "args": [repr(arg) for arg in wrapper.init_args],
                            "kwargs": {
                                repr(key): repr(value)
                                for key, value in wrapper.init_kwargs.items()
                            },
                        }
                        for wrapper in self.new_born_coroutines
                    },
                },
                'coroutines': {
                    'num': len(self.coroutines),
                    "list": {
                        coro_id: {
                            "func_info": func_info(self.purify_worker(wrapper.worker)),
                            "args": [repr(arg) for arg in wrapper.init_args],
                            "kwargs": {
                                repr(key): repr(value)
                                for key, value in wrapper.init_kwargs.items()
                            },
                        }
                        for coro_id, wrapper in self.coroutines.items()
                    },
                },
                'coro counter': self.coro_counter._index,
                'coro on del handlers num': len(self.coro_on_del_handlers),
                'coro on del handlers': {
                    'num': len(self.coro_on_del_handlers),
                    'list': [func_info(handler) for handler in self.coro_on_del_handlers]
                },
                'suppress coro exceptions': self.suppress_coro_exceptions,
                'context switches num': self.context_switches,
                'longest continuous execution time of coroutines': self.coro_longest_execution_time,
                'coroutines execution times': self.coro_execution_time,
                'need to measure loop iteration time': self.need_to_measure_loop_iteration_time,
                'need to measure coro time': self.need_to_measure_coro_time,
                'need to gather coro history': self.need_to_gather_coro_history,
                'coro workers history': {
                    'num': len(self.coro_workers_history),
                    'list': [{
                        'worker': func_info(self.purify_worker(worker)),
                        'coroutines': coroutines,
                    } for worker, coroutines in self.coro_workers_history.items()]
                },
                'coro full history': {
                    'num': len(self.coro_full_history),
                    'list': {coro_id: {
                        'worker': func_info(self.purify_worker(wrapper.worker)),
                        'args': [repr(arg) for arg in wrapper.init_args],
                        'kwargs': {repr(key): repr(value) for key, value in wrapper.init_kwargs.items()},
                    } for coro_id, wrapper in self.coro_full_history.items()}
                },
               'coro loop iteration delta time':self.loop_iteration_delta_time, 
            },
            'services': services_stats,
        }

    def loop(self):
        raise NotImplementedError
    
    def iteration(self):
        raise NotImplementedError
    
    def log_exc(self, coro: 'CoroWrapperBase', exception: Exception):
        worker_info = full_func_info_to_printable_dict(self.purify_worker(coro.worker))
        error_text = f'\nAn exception in coroutine "{worker_info["qualname"]}"\n\tModule "{worker_info["module"]}"\n\tFile "{worker_info["co_filename"]}", line {worker_info["co_firstlineno"]}:\n{exception_to_printable_text(exception)}'
        self.logger.error(f'{datetime.now()} >> {error_text}')

    # @property
    # def root_coro(self):
    #     return self._root_coro
    
    # @root_coro.setter
    # def root_coro(self, root_coro):
    #     if root_coro is None:
    #         if __debug__: dlog('root_coro = None')
    #     else:
    #         if __debug__: dlog(f'root_coro = {root_coro}')
    #     self._root_coro = root_coro
    
    def _fake_method(self, *args, **kwargs):
        pass
    
    @staticmethod
    def _fake_perf_counter():
        return 0.0
    
    def get_service_instance_fast_impl(self, service_type: ServiceType):
        return self.services[service_type]
    
    def get_service_instance_impl(self, service_type: ServiceType):
        self.register_service(service_type)
        return self.get_service_instance_fast_impl(service_type)
    
    def make_service_live_fast_impl(self, service_type: ServiceType, is_low_latency: bool = False):
        service: Optional[Service] = self.services.get(service_type, None)
        if service is not None:
            self.live_services[service_type] = self.services[service_type]
            if is_low_latency:
                self.live_low_latency_services[service_type] = self.services[service_type]
    
    def make_service_live_impl(self, service_type: ServiceType, is_low_latency: bool = False):
        self.register_service(service_type)
        self.make_service_live_fast_impl(service_type, is_low_latency)
    
    def make_service_dead_fast_impl(self, service_type: ServiceType):
        self.live_services.pop(service_type, None)
        self.live_low_latency_services.pop(service_type, None)
    
    def make_service_dead_impl(self, service_type: ServiceType):
        self.register_service(service_type)
        self.make_service_dead_fast_impl(service_type)
    
    def get_service_instance_fast_impostor_impl(self, service_type: ServiceType):
        return self.get_service_instance_fast_impl(self.services_impostrors.get(service_type, service_type))
    
    def get_service_instance_impostor_impl(self, service_type: ServiceType):
        return self.get_service_instance_impl(self.services_impostrors.get(service_type, service_type))
    
    def make_service_live_fast_impostor_impl(self, service_type: ServiceType, is_low_latency: bool = False):
        return self.make_service_live_fast_impl(self.services_impostrors.get(service_type, service_type), is_low_latency)
    
    def make_service_live_impostor_impl(self, service_type: ServiceType, is_low_latency: bool = False):
        return self.make_service_live_impl(self.services_impostrors.get(service_type, service_type), is_low_latency)
    
    def make_service_dead_fast_impostor_impl(self, service_type: ServiceType):
        return self.make_service_dead_fast_impl(self.services_impostrors.get(service_type, service_type))
    
    def make_service_dead_impostor_impl(self, service_type: ServiceType):
        return self.make_service_dead_impl(self.services_impostrors.get(service_type, service_type))

    def set_coro_time_measurement(self, need_to_measure_coro_time: bool):
        previous_value = self.need_to_measure_coro_time
        self.need_to_measure_coro_time = need_to_measure_coro_time
        if need_to_measure_coro_time:
            self.get_coro_start_time = perf_counter
        else:
            self.get_coro_start_time = self._fake_perf_counter
        
        return previous_value

    def set_coro_history_gathering(self, need_to_gather_coro_history: bool):
        previous_value = self.need_to_gather_coro_history
        self.need_to_gather_coro_history = need_to_gather_coro_history
        if need_to_gather_coro_history:
            self.coro_history_gatherer = self._default_coro_history_gatherer
        else:
            self.coro_history_gatherer = self._fake_method
        
        return previous_value
    
    def _default_coro_history_gatherer(self, original_worker: Callable, coro_wrapper: 'CoroWrapperBase'):
        coro_id: CoroID = coro_wrapper.coro_id
        coro_worker: Worker = coro_wrapper.worker
        
        self.coro_full_history[coro_id] = coro_wrapper
        
        if original_worker not in self.coro_workers_history:
            self.coro_workers_history[original_worker] = set()
        
        self.coro_workers_history[original_worker].add(coro_id)

    def set_loop_iteration_time_measurement(self, need_to_measure_loop_iteration_time: bool):
        previous_value = self.need_to_measure_loop_iteration_time
        self.need_to_measure_loop_iteration_time = need_to_measure_loop_iteration_time
        if need_to_measure_loop_iteration_time:
            self.get_loop_iteration_start_time = perf_counter
        else:
            self.get_loop_iteration_start_time = self._fake_perf_counter
        
        return previous_value
    
    def _new_coro_type_normalizer(self, coro_type: Optional[CoroType]) -> CoroType:
        raise NotImplementedError

    def put_coro_fast(self, coro_type: Optional[CoroType], coro_worker: Worker, *args, **kwargs) -> 'CoroWrapperBase':
        """Must not be called from coroutine. Use an appropriate service instead, since leads to incorrect greenlets switches
        """
        if (self.current_coro_interface is None) or self.permitted_use_put_coro_from_coro:
            coro_type = self._new_coro_type_normalizer(coro_type)
            coro_id = self.coro_counter.get()
            self.coro_execution_time[coro_id] = 0.0
            self.coro_longest_execution_time[coro_id] = 0.0
            coro = coro_wrapper_factory(coro_type, self, coro_id, coro_worker, *args, **kwargs)
            if isinstance(coro_worker, EntityArgsHolder):
                self.coro_history_gatherer(coro_worker.entity, coro)
            else:
                self.coro_history_gatherer(coro_worker, coro)
            
            self.new_born_coroutines.append(coro)
            if not self.in_iteration:
                self.on_woke_up_callback()
            
            return coro
        else:
            raise RuntimeError('CoroScheduler.put_coro() method must not be called from coroutine. Use an appropriate service instead')

    def put_coro(self, coro_worker: AnyWorker, *args, **kwargs) -> 'CoroWrapperBase':
        if isinstance(coro_worker, EntityArgsHolder):
            coro_worker_real, args, kwargs = coro_worker.entity_args_kwargs()
            if isinstance(coro_worker, ExplicitWorker):
                coro_type: CoroType = coro_worker.coro_type
                coro_worker: EntityArgsHolderExplicit = EntityArgsHolderExplicit(coro_worker_real.worker, args, kwargs)
                return self.put_coro_fast(coro_type, coro_worker)
            else:
                return self.put_coro_fast(None, coro_worker)
        else:
            if isinstance(coro_worker, ExplicitWorker):
                return self.put_coro_fast(coro_worker.coro_type, coro_worker.worker, *args, **kwargs)
            else:
                return self.put_coro_fast(None, coro_worker, *args, **kwargs)

    def register_service(self, service_type: ServiceType) -> bool:
        if service_type in self.services:
            return False
        else:
            service = service_type(self)
            self.services[service_type] = service
            self.live_services[service_type] = service
            return True
    
    def is_service_registered(self, service_type: ServiceType) -> bool:
        return service_type in self.services
    
    def unregister_service(self, service_type: ServiceType) -> bool:
        if service_type not in self.services:
            return True
        
        service = self.services[service_type]
        self.services.pop(service_type, None)
        self.live_services.pop(service_type, None)
        self.live_low_latency_services.pop(service_type, None)
        try:
            service.destroy()
        except:
            self.logger.exception(f'{datetime.now()} >> Service {service_type} failed to destroy')
            return False
        
        return True
    
    def destroy_services(self):
        for service_type in tuple(self.services):
            self.unregister_service(service_type)
    
    def get_service_by_type_impl(self, service_type: Type['Service']) -> 'Service':
        try:
            return self.services[service_type]
        except KeyError:
            self.register_service(service_type)
            return self.services[service_type]
    
    def get_service_by_type_impostor_impl(self, service_type: Type['Service']) -> 'Service':
        return self.get_service_by_type_impl(self.services_impostrors.get(service_type, service_type))
    
    def register_service_impostor(self, service_type: Type['Service'], service_impostor_type: Optional[Type['Service']]) -> Optional[Type['Service']]:
        if service_impostor_type is None:
            an_old_impostor: Optional[Type['Service']] = self.services_impostrors.pop(service_type, None)
        else:
            an_old_impostor = self.services_impostrors.get(service_type, None)
            self.services_impostrors[service_type] = service_impostor_type
        
        if self.services_impostrors:
            self.get_service_by_type = self.get_service_by_type_impostor_impl
            self.get_service_instance_fast = self.get_service_instance_fast_impostor_impl
            self.get_service_instance = self.get_service_instance_impostor_impl
            self.make_service_live_fast = self.make_service_live_fast_impostor_impl
            self.make_service_live = self.make_service_live_impostor_impl
            self.make_service_dead_fast = self.make_service_dead_fast_impostor_impl
            self.make_service_dead = self.make_service_dead_impostor_impl
        else:
            self.get_service_by_type = self.get_service_by_type_impl
            self.get_service_instance_fast = self.get_service_instance_fast_impl
            self.get_service_instance = self.get_service_instance_impl
            self.make_service_live_fast = self.make_service_live_fast_impl
            self.make_service_live = self.make_service_live_impl
            self.make_service_dead_fast = self.make_service_dead_fast_impl
            self.make_service_dead = self.make_service_dead_impl
        
        return an_old_impostor

    def find_new_born_coroutine(self, coro_id: CoroID) -> int:
        for index, coro in enumerate(self.new_born_coroutines):
            if coro.coro_id == coro_id:
                return index
        
        return None
    
    def get_coro(self, coro_id: CoroID) -> Optional['CoroWrapperBase']:
        if coro_id in self.coroutines:
            return self.coroutines[coro_id]
        else:
            new_born_coro_index = self.find_new_born_coroutine(coro_id)
            if new_born_coro_index is None:
                return None
            
            return self.new_born_coroutines[new_born_coro_index]
    
    @staticmethod
    def purify_worker(worker: Union[Callable, 'GreenletWorkerWrapper']) -> Callable:
        if isinstance(worker, GreenletWorkerWrapper):
            return worker.worker
        else:
            return worker

    def set_global_on_start_handlers(self, turn_on_global_on_start_handlers: bool):
        self.global_on_start_handlers_turned_on = turn_on_global_on_start_handlers
        if turn_on_global_on_start_handlers:
            self.execute_global_on_start_handlers = self._execute_global_on_start_handlers
        else:
            self.execute_global_on_start_handlers = self._fake_execute_global_on_start_handlers

    def add_on_global_on_start_handler(self, handler: Callable):
        self.coro_on_start_handlers.add(handler)

    def _execute_global_on_start_handlers(self, coro: 'CoroWrapperBase') -> bool:
        # executes before new born corotine execution
        # if at least one of the handlers will return False - coro will not be started at all and removed from the coroutines list
        result = True
        for handler in self.coro_on_start_handlers:
            result &= handler(coro)
        
        return result
    
    def _fake_execute_global_on_start_handlers(self, coro: 'CoroWrapperBase') -> bool:
        # executes before new born corotine execution
        # if at least one of the handlers will return False - coro will not be started at all and removed from the coroutines list
        return True
    
    
    def process_coro_exit_status(self, coro: 'CoroWrapperBase', coro_exit_status: Optional['CoroExitStatus']):
        try:
            if coro_exit_status is None:
                self._run_global_on_coro_del_handlers(coro)
            else:
                if coro_exit_status.exception and (not coro_exit_status.properly_handled) and (not self.coro_on_del_handlers) and (not self.suppress_coro_exceptions):
                    raise coro_exit_status.exception

                coro_exit_status.properly_handled = self._run_global_on_coro_del_handlers(coro) or coro_exit_status.properly_handled

                if coro_exit_status.exception and (not coro_exit_status.properly_handled):
                    if self.suppress_coro_exceptions:
                        # if __debug__: dlog(coro_exit_status.exception)
                        # dlog(coro_exit_status.exception)
                        self.log_exc(coro, coro_exit_status.exception)
                    else:
                        raise coro_exit_status.exception
        finally:
            coro.destroy()
            del coro
    
    def kill_coro(self, coro: 'CoroWrapperBase'):
        coro.request_close()
        coro_exit_status: 'CoroExitStatus' = coro()
        if not coro:
            self.process_coro_exit_status(coro, coro_exit_status)
    
    def throw_coro(self, coro: 'CoroWrapperBase', ex_type, ex_value=None, ex_traceback=None):
        # coro.request_close()
        coro.request_throw()  # TODO: Investigate why it raises an exception in the loop and shuts down the loop
        coro_exit_status: 'CoroExitStatus' = coro(ex_type, ex_value, ex_traceback)
        if not coro:
            self.process_coro_exit_status(coro, coro_exit_status)
    
    def forget_coro_by_id(self, coro: 'CoroWrapperBase') -> Optional['CoroWrapperBase']:
        return self.forget_coro_by_id(coro.coro_id)
    
    def find_coro_by_id(self, coro_id: CoroID) -> Tuple[Optional['CoroWrapperBase'], bool, Optional[int]]:
        coro = None
        if coro_id in self.coroutines:
            was_new_born: bool = False
            coro = self.coroutines[coro_id]
            return coro, was_new_born, None
        else:
            was_new_born = True
            new_born_index = self.find_new_born_coroutine(coro_id)
            if new_born_index is not None:
                coro = self.new_born_coroutines[new_born_index]
        
            return coro, was_new_born, new_born_index

    def del_coro_by_id(self, coro_id: CoroID, was_new_born: bool, new_born_index: Optional[int] = None, request: Optional['Request'] = None):
        if was_new_born:
            del self.new_born_coroutines[new_born_index]
        else:
            self.coroutines.pop(coro_id, None)
            if isinstance(request, Request):
                try:
                    self.requests.remove(request)
                except ValueError:
                    pass
    
    def kill_coro_by_id(self, coro_id: CoroID) -> bool:
        if self.current_coro_interface is not None:
            raise RuntimeError('CoroScheduler.kill_coro_by_id() Must not be called from the coroutine')
        
        coro, was_new_born, new_born_index = self.find_coro_by_id(coro_id)
        if coro is not None:
            request: Optional[Request] = coro.last_result
            if was_new_born:
                self.process_coro_exit_status(coro, None)
            else:
                self.kill_coro(coro)
            
            self.del_coro_by_id(coro_id, was_new_born, new_born_index, request=request)
            return True
        
        return False
    
    def throw_coro_by_id(self, coro_id: CoroID, ex_type, ex_value=None, ex_traceback=None) -> bool:
        if self.current_coro_interface is not None:
            raise RuntimeError('CoroScheduler.throw_coro_by_id() Must not be called from the coroutine')
        
        coro, was_new_born, new_born_index = self.find_coro_by_id(coro_id)
        if coro is not None:
            request: Optional[Request] = coro.last_result
            if was_new_born:
                self.process_coro_exit_status(coro, None)
            else:
                self.throw_coro(coro, ex_type, ex_value, ex_traceback)
            
            if not coro:
                self.del_coro_by_id(coro_id, was_new_born, new_born_index, request=request)

            return True
        
        return False
    
    def request_coro_throw_by_id(self, coro_id: CoroID, *args, **kwargs) -> Optional['CoroWrapperBase']:
        coro, _, _ = self.find_coro_by_id(coro_id)
        if coro is not None:
            coro.request_throw(*args, **kwargs)
        
        return coro

    def request_coro_close_by_id(self, coro_id: CoroID) -> Optional['CoroWrapperBase']:
        coro, _, _ = self.find_coro_by_id(coro_id)
        if coro is not None:
            coro.request_close()
        
        return coro
    
    def _real_run_low_latency_services(self):
        for service_type, service in tuple(self.live_low_latency_services.items()):
            if service.in_work():
                results = service.iteration()
                if results:
                    # if __debug__:
                    #     for result in results:
                    #         if __debug__: dlog(f'λ <<< {repr(result)}')

                    self.responses.extend(results)
    
    def _fake_run_low_latency_services(self):
        pass
    
    def turn_on_embedded_mode(self, turn_on: bool = False):
        if turn_on:
            self.run_low_latency_services = self._real_run_low_latency_services
        else:
            self.run_low_latency_services = self._fake_run_low_latency_services

    def add_global_on_coro_del_handler(self, callback: OnCoroDelHandler):
        self.coro_on_del_handlers.add(callback)

    def _run_global_on_coro_del_handlers(self, coro: 'CoroWrapperBase') -> bool:
        if not self.coro_on_del_handlers:
            return False

        exception_properly_handled = False
        for handler in self.coro_on_del_handlers:
            exception_properly_handled = handler(coro) or exception_properly_handled
        return exception_properly_handled

    def restore_global_state(self):
        """
        Must be run immediately after `await ...` from inside Coro or Service when running from inside external
        async loop
        :return:
        """
        _current_coro_scheduler.scheduler = self

    @staticmethod
    def current_loop() -> Optional['CoroScheduler']:
        return _current_coro_scheduler.scheduler

    def current_interface(self) -> Optional['Interface']:
        return self.current_coro_interface

    def current_wrapper(self) -> Optional['CoroWrapperBase']:
        return self.current_coro_wrapper
    
    def destroy_all_coroutines(self, ex_type=None, ex_value=None, ex_traceback=None):
        while self.new_born_coroutines or self.coroutines:
            new_born_coroutines_buff = self.new_born_coroutines
            # self.new_born_coroutines = type(new_born_coroutines_buff)()
            self.new_born_coroutines = list()
            for coro in new_born_coroutines_buff:
                coro: 'CoroWrapperBase' = coro
                coro_id: CoroID = coro.coro_id
                if (ex_type is not None) or (ex_value is not None):
                    self.throw_coro_by_id(coro_id, ex_type, ex_value, ex_traceback)
    
                if coro:
                    self.kill_coro_by_id(coro_id)

            coroutines_buff = self.coroutines
            # self.coroutines = type(coroutines_buff)()
            self.coroutines = type(coroutines_buff)()
            for coro in coroutines_buff.values():
                coro: 'CoroWrapperBase' = coro
                coro_id: CoroID = coro.coro_id
                if (ex_type is not None) or (ex_value is not None):
                    self.throw_coro_by_id(coro_id, ex_type, ex_value, ex_traceback)
                
                if coro:
                    self.kill_coro_by_id(coro_id)
    
    def destroy_new_born_coroutines(self, ex_type=None, ex_value=None, ex_traceback=None):
        while self.new_born_coroutines:
            new_born_coroutines_buff = self.new_born_coroutines
            # self.new_born_coroutines = type(new_born_coroutines_buff)()
            self.new_born_coroutines = list()
            for coro in new_born_coroutines_buff:
                coro: 'CoroWrapperBase' = coro
                coro_id: CoroID = coro.coro_id
                if (ex_type is not None) or (ex_value is not None):
                    self.throw_coro_by_id(coro_id, ex_type, ex_value, ex_traceback)
    
                if coro:
                    self.kill_coro_by_id(coro_id)
    
    def destroy_coroutines(self, ex_type=None, ex_value=None, ex_traceback=None):
        while self.coroutines:
            coroutines_buff = self.coroutines
            # self.coroutines = type(coroutines_buff)()
            self.coroutines = dict()
            coroutines_buff_values = coroutines_buff.values()
            for coro in coroutines_buff_values:
                coro: 'CoroWrapperBase' = coro
                coro_id: CoroID = coro.coro_id
                if (ex_type is not None) or (ex_value is not None):
                    self.throw_coro_by_id(coro_id, ex_type, ex_value, ex_traceback)
    
                if coro:
                    self.kill_coro_by_id(coro_id)
    
    def destroy(self):
        if self.need_to_log_loop_start_and_end:
            self.logger.info(f'{datetime.now()} >> {type(self).__name__} destroy...')
        
        if not self._destroyed:
            def create_entity_during_destroy(*args, **kwargs):
                raise CoroSchedulerIsCurrentlyDestroingError
            
            put_coro_fast_buf = self.put_coro_fast
            self.put_coro_fast = create_entity_during_destroy
            register_service_bak = self.register_service
            self.register_service = create_entity_during_destroy

            try:
                while self.new_born_coroutines or self.coroutines:
                    new_born_coroutines_buff = self.new_born_coroutines
                    # self.new_born_coroutines = type(new_born_coroutines_buff)()
                    self.new_born_coroutines = list()
                    for coro in new_born_coroutines_buff:
                        coro: 'CoroWrapperBase' = coro
                        coro_id: CoroID = coro.coro_id
                        repr_coro: str = repr(coro)
                        try:
                            self.throw_coro_by_id(coro_id, CoroSchedulerDestroyException)
                        except CoroSchedulerIsCurrentlyDestroingError:
                            self.logger.warning(f'{datetime.now()} >> Unhandled `CoroSchedulerIsCurrentlyDestroingError` exception during throw CoroSchedulerDestroyException to new born coroutine {repr_coro}')
                            pass
                        
                        try:
                            if coro:
                                self.kill_coro_by_id(coro_id)
                        except CoroSchedulerIsCurrentlyDestroingError:
                            self.logger.warning(f'{datetime.now()} >> Unhandled `CoroSchedulerIsCurrentlyDestroingError` exception during kill new born coroutine {repr_coro}')
                            pass

                    coroutines_buff = self.coroutines
                    # self.coroutines = type(coroutines_buff)()
                    self.coroutines = dict()
                    for coro in coroutines_buff.values():
                        coro: 'CoroWrapperBase' = coro
                        coro_id: CoroID = coro.coro_id
                        repr_coro: str = repr(coro)
                        try:
                            self.throw_coro_by_id(coro_id, CoroSchedulerDestroyException)
                        except CoroSchedulerIsCurrentlyDestroingError:
                            self.logger.warning(f'{datetime.now()} >> Unhandled `CoroSchedulerIsCurrentlyDestroingError` exception during throw CoroSchedulerDestroyException to coroutine {repr_coro}')
                            pass

                        try:
                            if coro:
                                self.kill_coro_by_id(coro_id)
                        except CoroSchedulerIsCurrentlyDestroingError:
                            self.logger.warning(f'{datetime.now()} >> Unhandled `CoroSchedulerIsCurrentlyDestroingError` exception during kill coroutine {repr_coro}')
                            pass

                    # self.requests = type(self.requests)()
                    self.requests = list()
                    # self.responses = type(self.responses)()
                    self.responses = list()
                
                for service_type in tuple(self.services):
                    try:
                        self.unregister_service(service_type)
                    except CoroSchedulerIsCurrentlyDestroingError:
                        self.logger.warning(f'{datetime.now()} >> Unhandled `CoroSchedulerIsCurrentlyDestroingError` exception during destroy service "{service_type}"')
                        pass

                # self.requests = type(self.requests)()
                self.requests = list()
                # self.responses = type(self.responses)()
                self.responses = list()
            finally:
                self.put_coro_fast = put_coro_fast_buf
                self.register_service = register_service_bak
                self._destroyed = True
                for on_destroyed_handler in self.on_destroyed_handlers:
                    on_destroyed_handler()

                if self.need_to_log_loop_start_and_end:
                    self.logger.info(f'{datetime.now()} >> {type(self).__name__} destroyed.')
                
                self.logger.removeHandler(self.logger_stream_handler)

    
    def _update_in_work(self):
        # self._in_work = self.new_born_coroutines or self.coroutines or self.services_in_work
        self._in_work = (self.foreground_coro_num > 0) or self.services_in_foreground_work
        return self._in_work

    def in_work(self):
        in_work_result = self._in_work
        return self._update_in_work() if in_work_result is None else in_work_result

    def _update_is_awake(self):
        self._is_awake = self.new_born_coroutines or self.coroutines or self.live_services or self.live_low_latency_services
        return self._is_awake

    def is_awake(self):
        is_awake_result = self._is_awake
        return self._update_is_awake() if is_awake_result is None else is_awake_result

    def is_idle(self) -> bool:
        # return (self.next_event_after() is not None) and (not self.new_born_coroutines) and (not self.services_in_active_state) and (not self.responses)
        return (not self.new_born_coroutines) and (not self.services_in_active_state) and (0 == (len(self.responses) - self.idle_managers_num))

    def next_event_after(self) -> Optional[Union[float, int]]:
        return self.time_left_before_next_event

    def _loop_imp(self):
        try:
            next_event_after = None
            # while self.in_work() or (next_event_after is not None):
            while self.in_work():
                self._iteration_imp()
                next_event_after = self.next_event_after()
                # if (next_event_after is not None) and (not self.new_born_coroutines) and (not self.services_in_active_state) and (not self.responses):
                #     if self.use_internal_sleep or (not self.on_idle_handlers):
                #         sleep(next_event_after)
                #     else:
                #         for handler in self.on_idle_handlers:
                #             handler(next_event_after)
                # # else:
                # #     print(self.services_in_active_state_list)

                if self.is_idle():
                    if self.use_internal_sleep:
                        if next_event_after is None:
                            sleep(high_cpu_utilisation_mode=self.high_cpu_utilisation_mode)
                        else:
                            sleep(next_event_after, high_cpu_utilisation_mode=self.high_cpu_utilisation_mode)

                    for handler in self.on_idle_handlers:
                        handler(next_event_after)
        except CoroSchedulerDestroyRequestedException:
            pass
        finally:
            self.destroy()
    
    def _iteration_imp(self):
        current_coro_scheduler_buff = _current_coro_scheduler.scheduler
        _current_coro_scheduler.scheduler = self
        
        self.in_iteration = True
        
        cpu_clock_cycles_start_time = cpu_clock_cycles()
        # minus_delta_time = 0
        try:
            self.context_switches += len(self.new_born_coroutines) + len(self.responses)
            self.loop_iteration_start_time = self.get_loop_iteration_start_time()

            if not self.keep_coro_execution_time_between_iterations:
                # self.coro_execution_time = type(self.coro_execution_time)()
                self.coro_execution_time = dict()
            if not self.keep_coro_longest_execution_time_between_iterations:
                # self.coro_longest_execution_time = type(self.coro_longest_execution_time)()
                self.coro_longest_execution_time = dict()
            if not self.keep_coro_workers_history_between_iterations:
                # self.coro_workers_history = type(self.coro_workers_history)()
                self.coro_workers_history = dict()
            if not self.keep_coro_full_history_between_iterations:
                # self.coro_full_history = type(self.coro_full_history)()
                self.coro_full_history = dict()

            # minus_start_time = cpu_clock_cycles()
            self.run_low_latency_services()
            # minus_delta_time += cpu_clock_cycles() - minus_start_time

            new_born_coroutines_buff = self.new_born_coroutines
            # self.new_born_coroutines = type(new_born_coroutines_buff)()

            # TODO: we need to give first coro a list of all coros and an index (0 at the moment)
            # coro will make required work, find next Greenlet coro in the list and will swithch
            # to it given same list and an updated index. Next coro will do the same.
            # then an every coro returns and as result we will return here. After that,
            # loop will process all Asyncio coroutines in a normal maner
            # if self._coroutines_can_switch_directly:
            #     pass
            
            self.new_born_coroutines = list()
            self._is_current_coro_was_new_born = True
            for coro in new_born_coroutines_buff:
                coro: CoroWrapperBase = coro
                if self.execute_global_on_start_handlers(coro):
                    self.current_coro_start_time = self.get_coro_start_time()
                    self.current_coro_wrapper = coro
                    # minus_start_time = cpu_clock_cycles()
                    coro_exit_status: CoroExitStatus = coro.init(self.root_coro)
                    # minus_delta_time += cpu_clock_cycles() - minus_start_time
                    self.current_coro_wrapper = None
                    coro_execution_piece_delta_time = self.get_coro_start_time() - self.current_coro_start_time
                    self.current_coro_start_time = None
                    coro_id = coro.coro_id
                    if coro_id not in self.coro_execution_time:
                        self.coro_execution_time[coro_id] = 0

                    self.coro_execution_time[coro_id] += coro_execution_piece_delta_time
                    if coro_id not in self.coro_longest_execution_time:
                        self.coro_longest_execution_time[coro_id] = 0

                    self.coro_longest_execution_time[coro_id] = max(self.coro_longest_execution_time[coro_id], coro_execution_piece_delta_time)
                    if coro:
                        coro_last_result = coro.last_result
                        if not isinstance(coro_last_result, Request):
                            if self.on_wrong_request is None:
                                # minus_start_time = cpu_clock_cycles()
                                self.logger.warning(f'{datetime.now()} >> Wrong request {repr(coro_last_result)} of type {type(coro_last_result)} from coroutine {repr(coro)}')
                                self.kill_coro_by_id(coro_id)
                                # minus_delta_time += cpu_clock_cycles() - minus_start_time
                                continue
                            else:
                                # minus_start_time = cpu_clock_cycles()
                                coro_last_result = self.on_wrong_request(coro, coro_last_result)
                                # minus_delta_time += cpu_clock_cycles() - minus_start_time
                        
                        self.requests.append(coro_last_result)
                        self.coroutines[coro_id] = coro
                        continue
                    else:
                        # minus_start_time = cpu_clock_cycles()
                        self.process_coro_exit_status(coro, coro_exit_status)
                        # minus_delta_time += cpu_clock_cycles() - minus_start_time

            responses_buff = self.responses
            # self.responses = type(responses_buff)()
            
            # TODO: we need to give first coro a list of all coros and an index (0 at the moment)
            # coro will make required work, find next Greenlet coro in the list and will swithch
            # to it given same list and an updated index. Next coro will do the same.
            # then an every coro returns and as result we will return here. After that,
            # loop will process all Asyncio coroutines in a normal maner
            # if self._coroutines_can_switch_directly:
            #     pass
            
            self.responses = list()
            self._is_current_coro_was_new_born = False
            for response in responses_buff:
                coro_id = response.coro_id
                if coro_id not in self.coroutines:
                    if not self.suppress_warnings_about_responses_to_not_existant_coroutines:
                        self.logger.warning(f'{datetime.now()} >> Coroutine {coro_id} has a response but does not exists: {repr(response)}')
                    
                    continue
                
                coro = self.coroutines[coro_id]

                self.current_coro_start_time = self.get_coro_start_time()
                self.current_coro_wrapper = coro
                if isinstance(response, DirectResponse):
                    response = response.response
                
                # minus_start_time = cpu_clock_cycles()
                coro_exit_status: CoroExitStatus = coro(response)
                # minus_delta_time += cpu_clock_cycles() - minus_start_time
                self.current_coro_wrapper = None
                coro_execution_piece_delta_time = self.get_coro_start_time() - self.current_coro_start_time
                self.current_coro_start_time = None
                coro_id = coro.coro_id
                if coro_id not in self.coro_execution_time:
                    self.coro_execution_time[coro_id] = 0

                self.coro_execution_time[coro_id] += coro_execution_piece_delta_time
                if coro_id not in self.coro_longest_execution_time:
                    self.coro_longest_execution_time[coro_id] = 0

                self.coro_longest_execution_time[coro_id] = max(self.coro_longest_execution_time[coro_id], coro_execution_piece_delta_time)
                if coro:
                    coro_last_result = coro.last_result
                    if not isinstance(coro_last_result, Request):
                        if self.on_wrong_request is None:
                            # minus_start_time = cpu_clock_cycles()
                            self.logger.warning(f'{datetime.now()} >> Wrong request {repr(coro_last_result)} of type {type(coro_last_result)} from coroutine {repr(coro)}')
                            self.kill_coro_by_id(coro_id)
                            # minus_delta_time += cpu_clock_cycles() - minus_start_time
                            continue
                        else:
                            # minus_start_time = cpu_clock_cycles()
                            coro_last_result = self.on_wrong_request(coro, coro_last_result)
                            # minus_delta_time += cpu_clock_cycles() - minus_start_time
                    
                    self.requests.append(coro_last_result)
                    continue
                else:
                    del self.coroutines[coro_id]
                    # minus_start_time = cpu_clock_cycles()
                    self.process_coro_exit_status(coro, coro_exit_status)
                    # minus_delta_time += cpu_clock_cycles() - minus_start_time

            self._is_current_coro_was_new_born = None
            requests_buff = self.requests
            # self.requests = type(requests_buff)()
            self.requests = list()
            for request in requests_buff:
                # if __debug__: dlog(f'λ >>> {repr(request)}')
                service_type = request.service_type
                service: 'Service' = self.get_service_by_type(service_type)
                # minus_start_time = cpu_clock_cycles()
                result = service.put_task(request)
                # minus_delta_time += cpu_clock_cycles() - minus_start_time
                if result is not None:
                    # if __debug__: dlog(f'λ <<< {repr(result)}')
                    self.responses.append(result)

            self.services_in_work = 0
            self.services_in_foreground_work = 0
            self.services_in_active_state = 0
            # self.services_in_active_state_list = list()
            self.time_left_before_next_event = None
            for service_type, service in tuple(self.live_services.items()):
                # minus_start_time = cpu_clock_cycles()
                in_work_result = service.in_work()
                # minus_delta_time += cpu_clock_cycles() - minus_start_time
                if in_work_result:
                    self.services_in_work += 1
                    self.services_in_active_state += 1
                    # minus_start_time = cpu_clock_cycles()
                    results = service.iteration()
                    # minus_delta_time += cpu_clock_cycles() - minus_start_time
                    # minus_start_time = cpu_clock_cycles()
                    in_work_result = service.in_work()
                    # minus_delta_time += cpu_clock_cycles() - minus_start_time
                    if in_work_result:
                        self.services_in_foreground_work += 1 if service.in_forground_work() else 0
                        # minus_start_time = cpu_clock_cycles()
                        has_planned_events, time_left_before_next_event = service.time_left_before_next_event()
                        # minus_delta_time += cpu_clock_cycles() - minus_start_time
                        if has_planned_events and (time_left_before_next_event is not None):
                            self.services_in_active_state -= 1
                            if self.time_left_before_next_event is None:
                                self.time_left_before_next_event = time_left_before_next_event
                            elif time_left_before_next_event < self.time_left_before_next_event:
                                self.time_left_before_next_event = time_left_before_next_event
                        # else:
                        #     self.services_in_active_state_list.append(service_type)
                    else:
                        self.services_in_work -= 1
                        self.services_in_active_state -= 1
                        # self.services_in_active_state_list.append(service_type)
                    
                    if results:
                        # if __debug__:
                        #     for result in results:
                        #         if __debug__: dlog(f'λ <<< {repr(result)}')

                        self.responses.extend(results)
        except CoroSchedulerDestroyRequestedException:
            raise
        except:
            # if __debug__: dlog('Loop Exception')
            self.logger.exception(f'{datetime.now()} >> Loop Exception')
            raise
        finally:
            self._update_in_work()
            self._update_is_awake()
            self.loop_iteration_delta_time = self.get_loop_iteration_start_time() - self.loop_iteration_start_time
            self.loop_cpu_clock_cycles = cpu_clock_cycles() - cpu_clock_cycles_start_time
            # self.sliding_window.append(cpu_clock_cycles() - cpu_clock_cycles_start_time - minus_delta_time)
            # self.sliding_window.append(minus_delta_time)
            self.iteration_index += 1
            # print()
            _current_coro_scheduler.scheduler = current_coro_scheduler_buff
            self.in_iteration = False


class CoroSchedulerGreenlet(CoroSchedulerBase):
    def __init__(self, logger: Optional[logging.Logger] = None):
        super().__init__(logger)
        self.root_coro_loop = greenlet(self._loop_imp)            # type: Coro
        # self.root_coro_iteration = greenlet(self._iteration_imp)  # type: Coro
        self.root_coro_iteration = greenlet(self._iter_wrapper)  # type: Coro
        # self._root_coro = None                                     # type: Optional[Coro]
        self.root_coro = None                                     # type: Optional[Coro]
        self._coroutines_can_switch_directly = True
    
    def _new_coro_type_normalizer(self, coro_type: Optional[CoroType]) -> CoroType:
        return coro_type or CoroType.auto

    def loop(self):
        if self.need_to_log_loop_start_and_end:
            self.logger.info(f'{datetime.now()} >> {type(self).__name__} loop started...')
        
        self.root_coro = self.root_coro_loop

        # if __debug__: dlog('Switch to root_coro')
        self.root_coro.switch()
        # if __debug__: dlog('Switch from root_coro')
        self.root_coro = None
        self.root_coro_loop = greenlet(self._loop_imp)
    
    def iteration(self):
        # global _debug_log_counter
        # last_debug_log_counter = _debug_log_counter
        # if __debug__: dlog(f'^ λ ({id(self)}, {self}). root_coro: {self.root_coro}; root_coro_iteration: {self.root_coro_iteration}; current_loop: {self.current_loop()}; current_interface: {self.current_interface()}')
        
        self.root_coro = self.root_coro_iteration
        in_work = False
        try:
            # if __debug__: dlog('Switch to root_coro (iteration)')
            in_work = self.root_coro.switch(True)
            # if __debug__: dlog('Switch from root_coro (iteration)')
        except GreenletExit:
            self.stop_iteration()
            # if __debug__: dlog('Switch from root_coro (GreenletExit)')
        except:
            self.stop_iteration()
            # if __debug__: dlog('Switch from root_coro (Exception):')
            # if __debug__: dlog(sys.exc_info())
            raise
        finally:
            self.root_coro = None
            # if __debug__:
            #     if last_debug_log_counter < _debug_log_counter:
            #         if __debug__: dlog(f'_ λ ({id(self)}, {self}). root_coro: {self.root_coro}; root_coro_iteration: {self.root_coro_iteration}; current_loop: {self.current_loop()}; current_interface: {self.current_interface()}')
        
        return in_work
    
    def stop_iteration(self):
        try:
            in_work = self.root_coro.switch(False)
        except GreenletExit:
            self.stop_iteration()
            # if __debug__: dlog('Stop root_coro (GreenletExit)')
        except:
            self.stop_iteration()
            # if __debug__: dlog('Stop root_coro (Exception):')
            # if __debug__: dlog(sys.exc_info())
            raise
        finally:
            self.root_coro = None
            self.root_coro_iteration = greenlet(self._iter_wrapper)
    
    def _iter_wrapper(self, proceed: bool=True):
        try:
            while proceed:
                self._iteration_imp()
                proceed = greenlet.getcurrent().parent.switch(self.in_work())
        except CoroSchedulerDestroyRequestedException:
            pass
        finally:
            self.destroy()


class CoroSchedulerAwaitable(CoroSchedulerBase):
    def __init__(self, logger: Optional[logging.Logger] = None):
        super().__init__(logger)
        self.root_coro = None                                     # type: Optional[Coro]
    
    def _new_coro_type_normalizer(self, coro_type: Optional[CoroType]) -> CoroType:
        return CoroType.awaitable

    def loop(self):
        if self.need_to_log_loop_start_and_end:
            self.logger.info(f'{datetime.now()} >> {type(self).__name__} loop started...')
        
        self._loop_imp()
    
    def iteration(self):
        # global _debug_log_counter
        # last_debug_log_counter = _debug_log_counter
        # if __debug__: dlog(f'^ λ ({id(self)}, {self}). root_coro: {self.root_coro}; root_coro_iteration: {self.root_coro_iteration}; current_loop: {self.current_loop()}; current_interface: {self.current_interface()}')
        
        need_to_destroy = False
        try:
            self._iteration_imp()
            return self.in_work()
        except CoroSchedulerDestroyRequestedException:
            need_to_destroy = True
        except:
            need_to_destroy = True
            raise
        finally:
            # if __debug__:
            #     if last_debug_log_counter < _debug_log_counter:
            #         if __debug__: dlog(f'_ λ ({id(self)}, {self}). root_coro: {self.root_coro}; root_coro_iteration: {self.root_coro_iteration}; current_loop: {self.current_loop()}; current_interface: {self.current_interface()}')
            
            if need_to_destroy:
                self.destroy()


if greenlet_awailable:
    CoroScheduler = CoroSchedulerGreenlet
else:
    CoroScheduler = CoroSchedulerAwaitable


def current_interface() -> Optional['Interface']:
    return current_coro_scheduler().current_interface()


def execute_coro(coro_worker: AnyWorker, *args, **kwargs) -> Any:
    return coro_worker(current_interface(), *args, **kwargs)


exec_coro = execute_coro
ecoro = execute_coro


async def aexecute_coro(coro_worker: AnyWorker, *args, **kwargs) -> Any:
    return await coro_worker(current_interface(), *args, **kwargs)


aexec_coro = aexecute_coro
aecoro = aexecute_coro


@contextmanager
def around_await():
    """
    It is very bad idea to await from inside the greenlet since it might lead to problems with stack
    state in an outside awaitable code and it's loop.
    Must be run around `await ...` from inside Coro or Service when running from inside external async loop
    :return:
    """
    loop = _current_coro_scheduler.scheduler
    try:
        yield
    finally:
        _current_coro_scheduler.scheduler = loop


class Request:
    def __init__(self, coro: 'CoroWrapperBase', service_type: ServiceType, *args, **kwargs):
        self.coro = coro
        self.coro_id = coro.coro_id
        self.service_type = service_type
        self.args = args
        self.kwargs = kwargs
    
    def __repr__(self):
        return f'<{self.__class__.__name__}(coro: {self.coro}, coro_id: {self.coro_id}, service_type: {self.service_type}, args: {self.args}, kwargs: {self.kwargs})>'


class Response:
    def __init__(self, coro_id: CoroID, service_type: ServiceType, response: Any, exception: Optional[BaseException]=None):
        self.coro_id = coro_id
        self.service_type = service_type
        self.response = response
        self.exception = exception

    def __call__(self) -> Any:
        if self.exception:
            raise self.exception
        return self.response
    
    def __repr__(self):
        return f'<{self.__class__.__name__}(coro_id: {self.coro_id}, service_type: {self.service_type}, response: {self.response}, exception: {self.exception})>'


class DirectResponse(Response):
    pass


class CoroExitStatus:
    def __init__(self, exception, properly_handled):
        self.exception = exception
        self.properly_handled = properly_handled


class CoroWrapperBase:
    def __init__(self, loop: CoroSchedulerBase, coro_id: CoroID, worker: Worker, *args, **kwargs):
        if isinstance(worker, EntityArgsHolder):
            worker, args, kwargs = worker.entity_args_kwargs()
        
        self.worker = worker               # type: Worker
        self.init_args = args              # type: Tuple[Any, ...]
        self.init_kwargs = kwargs          # type: Dict
        self.coro_id: CoroID = coro_id             # type: CoroID
        self.loop: CoroSchedulerBase = loop                   # type: CoroSchedulerBase
        self.coro = None                   # type: Optional[Coro]
        self.parent_coro = None            # type: Optional[Coro]
        self.interface = None              # type: Optional[Interface]
        self.last_result = None            # type: Optional[Union[Request, Any]] # return value can be any
        self.exception = None              # type: Optional[Exception] # If there was an exception
        self.coro_on_del_handlers = set()  # type: Set[Callable]
        self._make_coro_method = self._raise_not_implemented_error  # type: Callable
        self._make_interface = self._raise_not_implemented_error  # type: Callable
        self._init_method = self._raise_not_implemented_error  # type: Callable
        self._call_method = self._raise_not_implemented_error  # type: Callable
        self._throw_method = self._raise_not_implemented_error  # type: Callable
        self._close_method = self._raise_not_implemented_error  # type: Callable
        self._current_call_method = self._call_method  # type: Callable
        self._is_background_coro: bool = False
        self.loop.foreground_coro_num += 1
    
    def _travers_through_coro_on_del_handlers(self, coro_exit_status: 'CoroExitStatus'):
        if not self.coro_on_del_handlers:
            return coro_exit_status

        exception_properly_handled = coro_exit_status.properly_handled
        for handler in self.coro_on_del_handlers:
            exception_properly_handled = handler(self) or exception_properly_handled
        coro_exit_status.properly_handled = exception_properly_handled
        return coro_exit_status

    def init(self, parent_coro: Optional[Coro] = None) -> Union[None, 'CoroExitStatus']:
        self.parent_coro = parent_coro
        self.coro = self._make_coro_method()
        self.interface = self._make_interface()
        current_coro_interface_buff = self.loop.current_coro_interface
        self.loop.current_coro_interface = self.interface
        try:
            self._init_method(self.init_args, self.init_kwargs)
            if self:
                return None
            else:
                # if __debug__: dlog(f'LAST_RESULT. Type: {type(self.last_result)}; Value: {self.last_result}')
                return self._travers_through_coro_on_del_handlers(CoroExitStatus(None, True))
        except:
            self.exception = get_exception()
            if not self.coro_on_del_handlers:
                return CoroExitStatus(self.exception, False)
            return self._travers_through_coro_on_del_handlers(CoroExitStatus(self.exception, False))
        finally:
            self.loop.current_coro_interface = current_coro_interface_buff

    def __call__(self, *args, **kwargs) -> Union[None, 'CoroExitStatus']:
        current_coro_interface_buff = self.loop.current_coro_interface
        self.loop.current_coro_interface = self.interface
        try:
            self._current_call_method(*args, **kwargs)
            if self:
                return None
            else:
                # if __debug__: dlog(f'LAST_RESULT. Type: {type(self.last_result)}; Value: {self.last_result}')
                return self._travers_through_coro_on_del_handlers(CoroExitStatus(None, True))
        except:
            self.exception = get_exception()
            if not self.coro_on_del_handlers:
                return CoroExitStatus(self.exception, False)
            return self._travers_through_coro_on_del_handlers(CoroExitStatus(self.exception, False))
        finally:
            self.loop.current_coro_interface = current_coro_interface_buff
    
    def __bool__(self) -> bool:
        raise NotImplementedError

    def add_on_coro_del_handler(self, callback: OnCoroDelHandler):
        self.coro_on_del_handlers.add(callback)
    
    def _raise_not_implemented_error(self, *args, **kwargs):
        pass
        raise NotImplementedError
        return self._raise_not_implemented_error  # Suppressing lint error
    
    def _current_throw_method_helper(self, *args, **kwargs):
        self._throw_method(*args, **kwargs)
        self._current_call_method = self._call_method
    
    def request_throw(self, *args, **kwargs) -> Any:
        self._current_call_method = self._current_throw_method_helper
    
    def _current_close_method_helper(self, *args, **kwargs):
        self._close_method()
        self._current_call_method = self._call_method
    
    def request_close(self) -> Any:
        self._current_call_method = self._current_close_method_helper
    
    @property
    def is_background_coro(self):
        return self._is_background_coro
    
    @is_background_coro.setter
    def is_background_coro(self, value: bool):
        if value:
            if not self._is_background_coro:
                self.loop.foreground_coro_num -= 1
        else:
            if self._is_background_coro:
                self.loop.foreground_coro_num += 1
        
        self._is_background_coro = value

    def destroy(self):
        if self.interface is not None:
            if isinstance(self.interface, Interface):
                self.interface.destroy()
        
        if not self.is_background_coro:
            self.loop.foreground_coro_num -= 1
        
        self._is_background_coro = None
        self.init_args = None
        self.init_kwargs = None
        self.coro_id = None
        self.worker = None
        self.loop = None
        self.coro = None
        self.parent_coro = None
        self.interface = None
        self.last_result = None
        self.exception = None
        self.coro_on_del_handlers = None
        self._make_coro_method = None
        self._make_interface = None
        self._init_method = None
        self._call_method = None
        self._throw_method = None
        self._close_method = None
        self._current_call_method = None


class CoroWrapperGreenlet(CoroWrapperBase):
    def __init__(self, loop: CoroSchedulerBase, coro_id: CoroID, worker: Worker, *args, **kwargs):
        super(CoroWrapperGreenlet, self).__init__(loop, coro_id, worker, *args, **kwargs)
        self._make_coro_method = self._make_coro_method_imp
        self._make_interface = self._make_interface_imp
        self._init_method = self._init_method_imp
        self._call_method = self._call_method_imp
        self._throw_method = self._throw_method_imp  # type: Callable
        self._close_method = self._close_method_imp  # type: Callable
        self._current_call_method = self._call_method  # type: Callable
    
    def _make_coro_method_imp(self):
        return greenlet(self.worker, self.parent_coro)
    
    def _make_interface_imp(self):
        return InterfaceGreenlet(self.loop, self)

    def _init_method_imp(self, init_args, init_kwargs):
        try:
            # if __debug__: dlog(f'λ => (init): {func_info(self.worker.worker)}')
            self.last_result = self.coro.switch(self.interface, *init_args, **init_kwargs)  # TODO: wrong
            # if __debug__: dlog(f'λ <= (init): {repr(self.worker.worker)}')
        except GreenletExit:
            # if __debug__: dlog(f'λ <= (init; GreenletExit): {repr(self.worker.worker)}')
            self.last_result = self.interface.result
        except:
            # if __debug__: dlog(f'λ <= (init; Exception): {repr(self.worker.worker)}')
            self.last_result = None
            raise

    def _call_method_imp(self, *args, **kwargs):
        try:
            # if __debug__: dlog(f'λ => (call): {func_info(self.worker.worker)}')
            self.last_result = self.coro.switch(*args, **kwargs)  # TODO: wrong
            # if __debug__: dlog(f'λ <= (call): {repr(self.worker.worker)}')
        except GreenletExit:
            # if __debug__: dlog(f'λ <= (init; GreenletExit): {repr(self.worker.worker)}')
            self.last_result = self.interface.result
        except:
            # if __debug__: dlog(f'λ <= (init; Exception): {repr(self.worker.worker)}')
            self.last_result = None
            raise

    # def _throw_method_imp(self, *args, **kwargs):
    def _throw_method_imp(self, ex_type, ex_value=None, ex_traceback=None):
        try:
            # if __debug__: dlog(f'λ => (throw): {func_info(self.worker.worker)}')
            self.last_result = self.coro.throw(ex_type, ex_value, ex_traceback)
            # if __debug__: dlog(f'λ <= (throw): {repr(self.worker.worker)}')
        except GreenletExit:
            # if __debug__: dlog(f'λ <= (init; GreenletExit): {repr(self.worker.worker)}')
            self.last_result = self.interface.result
        except:
            # if __debug__: dlog(f'λ <= (init; Exception): {repr(self.worker.worker)}')
            self.last_result = None
            raise

    def _close_method_imp(self):
        try:
            # if __debug__: dlog(f'λ => (close): {func_info(self.worker.worker)}')
            self.last_result = self.coro.throw()
            # if __debug__: dlog(f'λ <= (close): {repr(self.worker.worker)}')
        except GreenletExit:
            # if __debug__: dlog(f'λ <= (init; GreenletExit): {repr(self.worker.worker)}')
            self.last_result = self.interface.result
        except:
            # if __debug__: dlog(f'λ <= (init; Exception): {repr(self.worker.worker)}')
            self.last_result = None
            raise
    
    def __bool__(self) -> bool:
        return bool(self.coro)

    def destroy(self):
        if isinstance(self.worker, GreenletWorkerWrapper):
            self.worker.destroy()
        
        return super().destroy()


async def init_asyncgenerator(entity: Callable):
    try:
        result = await entity.asend(None)
        return (result, None)
    except:
        exception = get_exception()
        return (None, exception)


async def call_asyncgenerator(entity: Callable, *args, **kwargs):
    try:
        result = await entity.asend(*args, **kwargs)
        return (result, None)
    except:
        exception = get_exception()
        return (None, exception)


async def throw_asyncgenerator(entity: Callable, *args, **kwargs):
    try:
        result = await entity.athrow(*args, **kwargs)  # await entity.athrow(type[, value[, traceback]]) ; https://docs.python.org/3/reference/expressions.html#agen.asend
        return (result, None)
    except:
        exception = get_exception()
        return (None, exception)


async def close_asyncgenerator(entity: Callable):
    try:
        result = await entity.aclose()
        return (result, None)
    except:
        exception = get_exception()
        return (None, exception)


async def init_asyncgeneratorfunction(entity: Callable, *args, **kwargs):
    try:
        entity = entity(*args, **kwargs)
        result = await entity.asend(None)
        return (entity, result, None)
    except:
        exception = get_exception()
        return (entity, None, exception)


async def awaitable_wrapper(entity: Awaitable):
    return await entity


async def callable_wrapper(entity: Callable, *args, **kwargs):
    return entity(*args, **kwargs)


class CoroWrapperAsyncAwait(CoroWrapperBase):
    def __init__(self, loop: CoroSchedulerBase, coro_id: CoroID, worker: Worker, *args, **kwargs):
        super(CoroWrapperAsyncAwait, self).__init__(loop, coro_id, worker, *args, **kwargs)
        self._make_coro_method = self._make_coro_method_imp
        self._make_interface = self._make_interface_imp
        self.in_run_state = False
        self.subtype = self._setup_subtype()
        self._current_call_method = self._call_method  # type: Callable

    def _make_coro_method_imp(self):
        return self.worker
    
    def _make_interface_imp(self):
        return InterfaceAsyncAwait(self.loop, self)

    def __bool__(self) -> bool:
        return bool(self.in_run_state)
    
    def _setup_subtype(self):
        if inspect.iscoroutine(self.worker):
            # if __debug__: dlog('λ >>>\tCOROUTINE')
            self._init_method = self._init_coroutine
            self._call_method = self._call_coroutine
            self._throw_method = self._throw_coroutine
            self._close_method = self._close_coroutine
            return 0
        elif inspect.isgenerator(self.worker):
            # if __debug__: dlog('λ >>>\tGENERATOR')
            self._init_method = self._init_generator
            self._call_method = self._call_coroutine
            self._throw_method = self._throw_coroutine
            self._close_method = self._close_coroutine
            return 1
        elif inspect.iscoroutinefunction(self.worker):
            # if __debug__: dlog('λ >>>\tCOROUTINE FUNCTION')
            self._init_method = self._init_coroutinefunction
            self._call_method = self._call_coroutine
            self._throw_method = self._throw_coroutine
            self._close_method = self._close_coroutine
            return 2
        elif inspect.isgeneratorfunction(self.worker):
            # if __debug__: dlog('λ >>>\tGENERATOR FUNCTION')
            self._init_method = self._init_generatorfunction
            self._call_method = self._call_coroutine
            self._throw_method = self._throw_coroutine
            self._close_method = self._close_coroutine
            return 3
        elif inspect.isasyncgen(self.worker):
            # if __debug__: dlog('λ >>>\tASYNC GENERATOR')
            self._init_method = self._init_asyncgenerator
            self._call_method = self._call_asyncgenerator
            self._throw_method = self._throw_asyncgenerator
            self._close_method = self._close_asyncgenerator
            return 4
        elif inspect.isasyncgenfunction(self.worker):
            # if __debug__: dlog('λ >>>\tASYNC GENERATOR FUNCTION')
            self._init_method = self._init_asyncgeneratorfunction
            self._call_method = self._call_asyncgenerator
            self._throw_method = self._throw_asyncgenerator
            self._close_method = self._close_asyncgenerator
            return 5
        elif inspect.isawaitable(self.worker):
            # if __debug__: dlog('λ >>>\tAWAITABLE')
            self._init_method = self._init_awaitable
            self._call_method = self._call_coroutine
            self._throw_method = self._throw_coroutine
            self._close_method = self._close_coroutine
            return 6
        elif callable(self.worker):
            # if __debug__: dlog('λ >>>\tCALLABLE')
            self._init_method = self._init_callable
            self._call_method = self._call_coroutine
            self._throw_method = self._throw_coroutine
            self._close_method = self._close_coroutine
            return 7
        else:
            raise TypeError(f'{self.worker} is neither an awaitable nor a wrapper for an awaitable')
    
    def _init_coroutine(self, init_args, init_kwargs):
        try:
            self.in_run_state = True
            self.last_result = self.coro.send(None)
        except StopIteration as ex:
            self.in_run_state = False
            self.last_result = ex.value
        except:
            self.in_run_state = False
            raise
            
    def _call_coroutine(self, *args, **kwargs):
        try:
            self.in_run_state = True
            self.last_result = self.coro.send(*args, **kwargs)
        except StopIteration as ex:
            self.in_run_state = False
            self.last_result = ex.value
        except:
            self.in_run_state = False
            raise
            
    # def _throw_coroutine(self, *args, **kwargs):
    def _throw_coroutine(self, ex_type, ex_value=None, ex_traceback=None):
        try:
            self.in_run_state = True
            self.last_result = self.coro.throw(ex_type, ex_value, ex_traceback)  # self.coro.throw(type[, value[, traceback]])
        except StopIteration as ex:
            self.in_run_state = False
            self.last_result = ex.value
        except:
            self.in_run_state = False
            raise
            
    def _close_coroutine(self, *args, **kwargs):
        try:
            self.in_run_state = True
            self.last_result = self.coro.close()
            self.in_run_state = False
        except GeneratorExit as ex:
            self.in_run_state = False
        except:
            self.in_run_state = False
            raise

    def _init_generator(self, init_args, init_kwargs):
        try:
            self.in_run_state = True
            self.last_result = next(self.coro)  # ToDo: investigate how to provide an initial parameters
        except StopIteration as ex:
            self.in_run_state = False
            self.last_result = ex.value
        except:
            self.in_run_state = False
            raise

    def _init_coroutinefunction(self, init_args, init_kwargs):
        self.coro = self.coro(self.interface, *init_args, **init_kwargs)
        self._init_coroutine(None, None)

    def _init_generatorfunction(self, init_args, init_kwargs):
        self.coro = self.coro(self.interface, *init_args, **init_kwargs)
        self._init_generator(None, None)

    def _init_asyncgenerator(self, init_args, init_kwargs):
        try:
            self.in_run_state = True
            entity = init_asyncgenerator(self.coro)
            result = entity.send(None)
        except StopIteration as ex:
            self.in_run_state = False
            result = ex.value
        except:
            self.in_run_state = False
            raise
        
        self.last_result, exception = result
        if exception is not None:
            self.in_run_state = False
            if not isinstance(exception, StopAsyncIteration):
                raise exception

    def _call_asyncgenerator(self, *args, **kwargs):
        try:
            self.in_run_state = True
            entity = call_asyncgenerator(self.coro, *args, **kwargs)
            result = entity.send(None)
        except StopIteration as ex:
            self.in_run_state = False
            result = ex.value
        except:
            self.in_run_state = False
            raise
        
        self.last_result, exception = result
        if exception is not None:
            self.in_run_state = False
            if not isinstance(exception, StopAsyncIteration):
                raise exception

    def _throw_asyncgenerator(self, *args, **kwargs):
        try:
            self.in_run_state = True
            entity = throw_asyncgenerator(self.coro, *args, **kwargs)
            result = entity.send(None)
        except StopIteration as ex:
            self.in_run_state = False
            result = ex.value
        except:
            self.in_run_state = False
            raise
        
        self.last_result, exception = result
        if exception is not None:
            self.in_run_state = False
            if not isinstance(exception, StopAsyncIteration):
                raise exception

    def _close_asyncgenerator(self):
        try:
            self.in_run_state = True
            entity = close_asyncgenerator(self.coro)
            result = entity.send(None)
        except StopIteration as ex:  # TODO: check maybe `GeneratorExit` will be raised
            self.in_run_state = False
            result = ex.value
        except:
            self.in_run_state = False
            raise
        
        self.last_result, exception = result
        if exception is not None:
            self.in_run_state = False
            if not isinstance(exception, StopAsyncIteration):
                raise exception

    def _init_asyncgeneratorfunction(self, init_args, init_kwargs):
        try:
            self.in_run_state = True
            entity = init_asyncgeneratorfunction(self.coro, self.interface, *init_args, **init_kwargs)
            result = entity.send(None)
        except StopIteration as ex:
            self.in_run_state = False
            result = ex.value
        except:
            self.in_run_state = False
            raise
        
        self.coro, self.last_result, exception = result
        if exception is not None:
            self.in_run_state = False
            if not isinstance(exception, StopAsyncIteration):
                raise exception

    def _init_awaitable(self, init_args, init_kwargs):
        self.coro = awaitable_wrapper(self.coro)
        self._init_coroutine()

    def _init_callable(self, init_args, init_kwargs):
        self.coro = callable_wrapper(self.coro, self.interface, *init_args, **init_kwargs)
        self._init_coroutine()

    def destroy(self):
        self._make_coro_method = None
        self._make_interface = None
        self.in_run_state = None
        self.subtype = None
        return super().destroy()


class GreenletWorkerWrapper:
    def __init__(self, worker: Worker):
        self.worker = worker
        
    def __call__(self, interface: 'InterfaceGreenlet', *args, **kwargs):
        result = None
        try:
            result = self.worker(interface, *args, **kwargs)
        finally:
            interface.register_result(result)  # in case if GreenletExit will be raised by greenlet framework
        return result

    def destroy(self):
        self.worker = None


def find_coro_type(entity) -> CoroType:
    if isinstance(entity, EntityArgsHolder):
        entity, args, kwargs = entity.entity_args_kwargs()

    if inspect.iscoroutine(entity) or inspect.isgenerator(entity) or inspect.iscoroutinefunction(entity) or inspect.isgeneratorfunction(entity) or inspect.isasyncgen(entity) or inspect.isasyncgenfunction(entity) or inspect.isawaitable(entity):
        return CoroType.awaitable
    elif callable(entity):
        return CoroType.greenlet
    else:
        raise TypeError(f'{entity} is neither an awaitable nor a greenlet')


def coro_wrapper_factory(coro_type: CoroType, loop: CoroSchedulerBase, coro_id: CoroID, worker: Worker, *args, **kwargs) -> 'CoroWrapperBase':
    if CoroType.auto == coro_type:
        coro_type = find_coro_type(worker)

    if CoroType.greenlet == coro_type:
        if isinstance(worker, EntityArgsHolder):
            worker, args, kwargs = worker.entity_args_kwargs()
            worker = GreenletWorkerWrapper(worker)
            worker: EntityArgsHolderExplicit = EntityArgsHolderExplicit(worker, args, kwargs)
            return CoroWrapperGreenlet(loop, coro_id, worker, *args, **kwargs)
        else:
            worker = GreenletWorkerWrapper(worker)
            return CoroWrapperGreenlet(loop, coro_id, worker, *args, **kwargs)
    elif CoroType.awaitable == coro_type:
        return CoroWrapperAsyncAwait(loop, coro_id, worker, *args, **kwargs)
    else:
        raise NotImplementedError


class Interface:
    def __init__(self, loop: CoroSchedulerBase, coro: CoroWrapperBase):
        self._loop: CoroSchedulerBase = loop                        # type: CoroSchedulerBase
        self._coro: CoroWrapperBase = coro                        # type: CoroWrapperBase
        self.coro_id: CoroID = coro.coro_id               # type: CoroID
        self.in_work: bool = False
        self.ignored_by_watchdog: bool = False
        self.logger: logging.Logger = self._loop.logger
        self.log: logging.Logger = self.logger
    
    @contextmanager
    def ignore_by_watchdog(self):
        current_state = self.ignored_by_watchdog
        self.ignored_by_watchdog = True
        try:
            yield
        finally:
            self.ignored_by_watchdog = current_state
    
    def _normalize_call_args_kwargs(self, service_type: Union[ServiceType, 'ServiceRequest'], args, kwargs) -> Tuple[Type['Service'], Tuple, Dict]:
        if inspect.isclass(service_type):
            if issubclass(service_type, Service):
                return service_type, args, kwargs
            elif issubclass(service_type, ServiceRequest):
                # return service_type, args, kwargs
                return self._normalize_call_args_kwargs(service_type()(*args, **kwargs))
            else:
                print(f'service_type of an unsupported type: {service_type}')
                raise TypeError(f'service_type of an unsupported type: {service_type}')
        elif isinstance(service_type, ServiceRequest):
            request: ServiceRequest = service_type
            service_type = request.default_service_type
            if service_type is None:
                print(f'Service request class {type(request)} have no default service assigned. Please provide service_type explicitly')
                raise RuntimeError(f'Service request class {type(request)} have no default service assigned. Please provide service_type explicitly')
            else:
                args, kwargs = args_kwargs(request, *args, **kwargs)
                return service_type, args, kwargs
        else:
            print(f'{service_type=}')
            raise ValueError(f'{service_type=}')

    # def __call__(self, service_type: ServiceType, *args, **kwargs) -> Any:
    #     """
    #     Should be called from inside coroutines only.
    #     Will request some long running work to some service.

    #     :param coro_id:
    #     :param service_type:
    #     :param args:
    #     :param kwargs:
    #     """

    #     response = self.__put_task_method(self.__coro, service_type, *args, *kwargs)
    #     return response()

    @overload
    def __call__(self, service_request_type: Type['TypedServiceRequest[ServiceResponseTypeVar]'], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_request: 'TypedServiceRequest[ServiceResponseTypeVar]') -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_type: Type['TypedService[ServiceResponseTypeVar]'], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_type: ServiceType, service_request: 'TypedServiceRequest[ServiceResponseTypeVar]') -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_request_type: Type['ServiceRequest'], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_request: 'ServiceRequest') -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_type: ServiceType, *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_type: ServiceType, service_request: 'ServiceRequest') -> ServiceResponseTypeVar: ...

    def __call__(self, service_type, *args, **kwargs):
        raise NotImplementedError

    # !!! Must not be present in interface since leads to incorrect greenlets switches
    # def put_coro(self, coro_type: CoroType, coro_worker: Worker, *args, **kwargs) -> CoroID:
    #     self.in_work = True
    #     coro = self._loop.put_coro(coro_type, coro_worker, *args, **kwargs)
    #     self.in_work = False
    #     return coro.coro_id

    def destroy(self):
        self._loop = None
        self._coro = None
        self.coro_id = None
        self.in_work = None


class InterfaceGreenlet(Interface):
    def __init__(self, loop: CoroSchedulerBase, coro: CoroWrapperBase):
        super(InterfaceGreenlet, self).__init__(loop, coro)
        self.result = None

    @overload
    def __call__(self, service_request_type: Type['TypedServiceRequest[ServiceResponseTypeVar]'], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_request: 'TypedServiceRequest[ServiceResponseTypeVar]') -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_type: Type['TypedService[ServiceResponseTypeVar]'], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_type: ServiceType, service_request: 'TypedServiceRequest[ServiceResponseTypeVar]') -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_request_type: Type['ServiceRequest'], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_request: 'ServiceRequest') -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_type: ServiceType, *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_type: ServiceType, service_request: 'ServiceRequest') -> ServiceResponseTypeVar: ...

    def __call__(self, service_type, *args, **kwargs):
        """
        Should be called from inside coroutines only.
        Will request some long running work to some service.

        :param coro_id:
        :param service_type:
        :param args:
        :param kwargs:
        """

        service_type, args, kwargs = self._normalize_call_args_kwargs(service_type, args, kwargs)

        self.in_work = True
        # if __debug__: dlog(f'λ <= (request): <{func_info(self._coro.worker.worker, False)}>: {service_type}, {args}, {kwargs}')
        try:
            loop: CoroSchedulerGreenlet = self._loop
            response: Response = loop.root_coro.switch(Request(self._coro, service_type, *args, **kwargs))
            # TODO: we will switch to the next coro and do necessary preparations and reactions
            # if loop._coroutines_can_switch_directly:
            #     if loop._is_current_coro_was_new_born:  
            #         ...
            #     else:
            #         ...
            # else:
            #     response: Response = loop.root_coro.switch(Request(self._coro, service_type, *args, **kwargs))
        except AttributeError:
            # if __debug__: dlog(f'x λ: {id(self._loop)}, {self._loop}, root_coro: {self._loop.root_coro}; root_coro_iteration: {self._loop.root_coro_iteration}; current_loop: {self._loop.current_loop()}; current_interface: {self._loop.current_interface()}')
            raise
        # if __debug__: dlog(f'λ => (response): <{func_info(self._coro.worker.worker)}>: {repr(response)}')
        self.in_work = False
        if isinstance(response, Response):
            return response()
        
        dlog(f"ERROR:\n\tRESPONSE TYPE: {type(response)}\n\tRESPONSE REPR: {repr(response)}\n\tRESPONSE STR: {str(response)}")
        raise RuntimeError(f'Wrong type of response from the service: {type(response)}; {repr(response)}.')
    
    def register_result(self, result: Any):
        self.result = result

    def destroy(self):
        self.result = None
        return super().destroy()


class InterfaceAsyncAwait(Interface):
    def __init__(self, loop: CoroSchedulerBase, coro: CoroWrapperBase):
        super(InterfaceAsyncAwait, self).__init__(loop, coro)

    @overload
    async def __call__(self, service_request_type: Type['TypedServiceRequest[ServiceResponseTypeVar]'], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    async def __call__(self, service_request: 'TypedServiceRequest[ServiceResponseTypeVar]') -> ServiceResponseTypeVar: ...

    @overload
    async def __call__(self, service_type: Type['TypedService[ServiceResponseTypeVar]'], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    async def __call__(self, service_type: ServiceType, service_request: 'TypedServiceRequest[ServiceResponseTypeVar]') -> ServiceResponseTypeVar: ...

    @overload
    async def __call__(self, service_request_type: Type['ServiceRequest'], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    async def __call__(self, service_request: 'ServiceRequest') -> ServiceResponseTypeVar: ...

    @overload
    async def __call__(self, service_type: ServiceType, *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    async def __call__(self, service_type: ServiceType, service_request: 'ServiceRequest') -> ServiceResponseTypeVar: ...

    async def __call__(self, service_type, *args, **kwargs):
        """
        Should be called from inside coroutines only.
        Will request some long running work to some service.

        :param coro_id:
        :param service_type:
        :param args:
        :param kwargs:
        """

        service_type, args, kwargs = self._normalize_call_args_kwargs(service_type, args, kwargs)

        self.in_work = True
        response = await yield_task_from_asyncawait(Request(self._coro, service_type, *args, **kwargs))
        self.in_work = False
        if isinstance(response, Response):
            return response()
        
        dlog(f"ERROR:\n\tRESPONSE TYPE: {type(response)}\n\tRESPONSE REPR: {repr(response)}\n\tRESPONSE STR: {str(response)}")
        raise RuntimeError('Wrong type of response from the service')


class InterfaceFake(Interface):
    def __init__(self, loop: CoroSchedulerBase, coro: CoroWrapperBase):
        self._loop: CoroSchedulerBase = None                        # type: CoroSchedulerBase
        self._coro: CoroWrapperBase = None                        # type: CoroWrapperBase
        self.coro_id: CoroID = None                      # type: CoroID
        self.in_work: bool = False

    @overload
    def __call__(self, service_request_type: Type['TypedServiceRequest[ServiceResponseTypeVar]'], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_request: 'TypedServiceRequest[ServiceResponseTypeVar]') -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_type: Type['TypedService[ServiceResponseTypeVar]'], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_type: ServiceType, service_request: 'TypedServiceRequest[ServiceResponseTypeVar]') -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_request_type: Type['ServiceRequest'], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_request: 'ServiceRequest') -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_type: ServiceType, *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    def __call__(self, service_type: ServiceType, service_request: 'ServiceRequest') -> ServiceResponseTypeVar: ...

    def __call__(self, service_type, *args, **kwargs) -> Any:
        service_type, args, kwargs = self._normalize_call_args_kwargs(service_type, args, kwargs)
        return None


class InterfaceFakeAsyncAwait(Interface):
    def __init__(self, loop: CoroSchedulerBase, coro: CoroWrapperBase):
        self._loop: CoroSchedulerBase = None                        # type: CoroSchedulerBase
        self._coro: CoroWrapperBase = None                        # type: CoroWrapperBase
        self.coro_id: CoroID = None                      # type: CoroID
        self.in_work: bool = False

    @overload
    async def __call__(self, service_request_type: Type['TypedServiceRequest[ServiceResponseTypeVar]'], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    async def __call__(self, service_request: 'TypedServiceRequest[ServiceResponseTypeVar]') -> ServiceResponseTypeVar: ...

    @overload
    async def __call__(self, service_type: Type['TypedService[ServiceResponseTypeVar]'], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    async def __call__(self, service_type: ServiceType, service_request: 'TypedServiceRequest[ServiceResponseTypeVar]') -> ServiceResponseTypeVar: ...

    @overload
    async def __call__(self, service_request_type: Type['ServiceRequest'], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    async def __call__(self, service_request: 'ServiceRequest') -> ServiceResponseTypeVar: ...

    @overload
    async def __call__(self, service_type: ServiceType, *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    async def __call__(self, service_type: ServiceType, service_request: 'ServiceRequest') -> ServiceResponseTypeVar: ...

    async def __call__(self, service_type, *args, **kwargs):
        service_type, args, kwargs = self._normalize_call_args_kwargs(service_type, args, kwargs)
        return None


class CallerCoroInfo:
    def __init__(self, coro: CoroWrapperBase):
        self.coro: CoroWrapperBase = coro
        self.coro_id: CoroID = coro.coro_id
        self.coro_type: Type = type(coro)


class WrongServiceRequestError(Exception):
    pass


class ServiceRequest:
    default_service_type: Optional[Type['Service']] = None
    default__request__type__: int = 0

    def __init__(self):
        self.request_type: int = None  # type: Optional[int]
        self.args: Optional[Tuple] = None          # type: Optional[Tuple]
        self.kwargs: Optional[Dict] = None        # type: Optional[Dict]
        self.provide_to_request_handler: bool = False

    def _save(self, __request__type__: int, *args, **kwargs) -> 'ServiceRequest':
        self.request_type = __request__type__
        self.args = args
        self.kwargs = kwargs
        return self
    
    def _copy(self) -> 'ServiceRequest':
        raise NotImplementedError

    def _save_to_copy(self, __request__type__: int, *args, **kwargs) -> 'ServiceRequest':
        return self._copy()._save(__request__type__, *args, **kwargs)
    
    def __call__(self, *args: Any, **kwds: Any) -> 'ServiceRequest':
        """should call self._save() with some default __request__type__. Required for the Interface(Type[ServiceRequest], *args, **kwargs) call. Must return self

        Returns:
            ServiceRequest: Must return self
        """
        return self._save(self.default__request__type__, *args, **kwds)
    
    def interface(self) -> Any:
        current_interface()(self.default_service_type, self)
    
    i = interface
    
    async def async_interface(self) -> Any:
        await current_interface()(self.default_service_type, self)
    
    ai = async_interface
    
    def __repr__(self):
        return f'<{self.__class__.__name__}(request_type: {self.request_type}, args: {self.args}, kwargs: {self.kwargs})>'


class TypedServiceRequest(ServiceRequest, Generic[ServiceResponseTypeVar]):
    pass


class ServiceRequestMethodMixin:
    def __init__(self, service: 'Service') -> None:
        self.service = service

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        raise NotImplementedError

    def full_processing_iteration(self):
        raise NotImplementedError

    def in_work(self) -> bool:
        raise NotImplementedError

    def _on_coro_del_handler(self, coro: CoroWrapperBase) -> bool:
        raise NotImplementedError


class DualImmediateProcessingServiceMixin:
    def single_task_registration_or_immediate_processing(self, *args, **kwargs) -> Tuple[bool, Any, None]:
        if (len(args) == 1) and (len(kwargs) == 0) and (isinstance(args[0], ServiceRequest)) or ((len(args) == 0) and (len(kwargs) == 1) and ('request' in kwargs) and isinstance(kwargs['request'], ServiceRequest)):
            return self.single_task_registration_or_immediate_processing_multiple(*args, **kwargs)
        else:
            return self.single_task_registration_or_immediate_processing_single(*args, **kwargs)

    def single_task_registration_or_immediate_processing_multiple(self, request: ServiceRequest
                                                         ) -> Tuple[bool, Any, None]:
        return self.resolve_request(request)

    def single_task_registration_or_immediate_processing_single(
            self, *args, **kwargs
    ) -> Tuple[bool, Optional[CoroID], Any]:
        raise NotImplementedError


ServiceProcessingResultExists = bool
ServiceProcessingResult = Any
ServiceProcessingException = Optional[BaseException]
ServiceProcessingResponse = Tuple[ServiceProcessingResultExists, ServiceProcessingResult, ServiceProcessingException]


class Service(Iterable):
    def __init__(self, loop: CoroSchedulerBase):
        super(Service, self).__init__()
        self._loop: CoroSchedulerBase = loop                     # type: CoroSchedulerBase
        # self._requests = list()               # type: List[Request]
        self._responses: List[Response] = list()              # type: List[Response]
        self.current_caller_coro_info: Optional[CallerCoroInfo] = None  # type: Optional[CallerCoroInfo]
        self._request_workers = dict()        # type: Dict[int, Callable]

    def iteration(self) -> Optional[List[Response]]:
        # requests = self._requests
        # self._requests = type(self._requests)()
        self._responses = list()
        # for request in requests:
        #     self.current_caller_coro_info = CallerCoroInfo(request.coro_id)
        #     result_exists, result = \
        #         self.single_task_registration_or_immediate_processing(*request.args, **request.kwargs)
        #     if result_exists:
        #         self.register_response(request.coro_id, result)
        # self.current_caller_coro_info = None
        try:
            self.full_processing_iteration()
        except:
            # if __debug__: dlog(sys.exc_info())
            raise
        return self._responses

    def make_response(self, coro_id: CoroID, response: Any, exception: Optional[BaseException]=None):
        return Response(coro_id, type(self), response, exception)

    def register_response(self, coro_id: CoroID, response: Any, exception: Optional[BaseException]=None):
        self._responses.append(self.make_response(coro_id, response, exception))

    def put_task(self, request: Request) -> Optional[Response]:
        self.current_caller_coro_info = CallerCoroInfo(request.coro)
        result_exists, result, exception = \
            self.single_task_registration_or_immediate_processing(*request.args, **request.kwargs)
        self.current_caller_coro_info = None
        if result_exists or exception:
            return self.make_response(request.coro_id, result, exception)
        return None

    def resolve_request(self, request: ServiceRequest):
        try:
            if request.provide_to_request_handler:
                return self._request_workers[request.request_type](request, *request.args, **request.kwargs)
            else:
                return self._request_workers[request.request_type](*request.args, **request.kwargs)
        except:
            return True, None, get_exception()

    def try_resolve_request(self, *args, **kwargs):
        possible_request: Optional[ServiceRequest] = None
        if (len(args) == 1) and (len(kwargs) == 0):
            possible_request = args[0]
        elif (len(kwargs) == 1) and (len(args) == 0):
            possible_request = kwargs.pop('request', None)

        if possible_request is not None:
            if isinstance(possible_request, ServiceRequest):
                return self.resolve_request(possible_request)

        return None

    def single_task_registration_or_immediate_processing(self, *args, **kwargs) -> ServiceProcessingResponse:
        raise NotImplementedError

    def full_processing_iteration(self):
        raise NotImplementedError

    def in_work(self) -> bool:
        """Will be executed twice per iteration: once before and once after the full_processing_iteration() execution

        Raises:
            NotImplementedError: _description_

        Returns:
            bool: _description_
        """        
        raise NotImplementedError
    
    def in_forground_work(self) -> bool:
        return True

    def thrifty_in_work(self, result: bool) -> bool:
        if result:
            return True
        else:
            self.make_dead()
            return False
    
    def time_left_before_next_event(self) -> Tuple[bool, Optional[Union[int, float]]]:
        return False, None
    
    def is_low_latency(self) -> bool:
        return False
    
    def make_live(self):
        self._loop.make_service_live_fast(type(self), self.is_low_latency())
    
    def make_dead(self):
        self._loop.make_service_dead_fast(type(self))
    
    @staticmethod
    def service_id_impl():
        return None
    
    @staticmethod
    def service_id(service_type: Type):
        service_id = service_type.service_id_impl()
        if service_id is None:
            service_id = service_type.__name__
        
        return service_id
    
    def destroy(self):
        pass


class TypedService(Service, Generic[ServiceResponseTypeVar]):
    pass
