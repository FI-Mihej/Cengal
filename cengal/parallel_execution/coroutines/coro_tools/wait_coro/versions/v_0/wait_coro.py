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


__all__ = ['sync_coro', 'sync_coro_param']


from cengal.parallel_execution.coroutines.coro_scheduler import *
# from cengal.parallel_execution.coroutines.coro_standard_services import *
from typing import Union, Optional, Any, List, Tuple, Dict
from cengal.parallel_execution.coroutines.coro_standard_services_internal_lib.service_with_a_direct_request import *
from cengal.code_flow_control.smart_values import ValueExistence
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import put_coro_to
from cengal.parallel_execution.coroutines.coro_standard_services.wait_coro import WaitCoro, WaitCoroRequest
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro_list import PSCP
from cengal.parallel_execution.coroutines.coro_tools.prepare_loop import prepare_loop, prepare_fast_loop


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


class LoopWasEndedBeforeResultWasComputed(Exception):
    pass


def sync_coro_param(result_required: bool = True, timeout: Optional[float] = None, kill_on_timeout: bool = True, tree: bool = True, cs: Optional[CoroScheduler] = None, prepare_own_loop_if_not_found: bool = False, own_loop_shold_be_fast_loop: bool = True, own_loop_setup_coro_worker: Optional[AnyWorker] = None, own_loop_setup_coro_worker_args_kwargs: Optional[Tuple[Tuple, Dict]] = None):
    """Decorator. With an arguments. Gives ability to execute any decorated Cengal coroutine from plain sync/async 
    code as a sync function. Can postpone execution to the actual loop when possible if None as an immediate result 
    (no result) is acceptible. Can start own loop if needed.

    Args:
        result_required (bool, optional): _description_. Defaults to True.
        timeout (Optional[float], optional): _description_. Defaults to None.
        kill_on_timeout (bool, optional): _description_. Defaults to True.
        tree (bool, optional): _description_. Defaults to True.
        cs (Optional[CoroScheduler], optional): _description_. Defaults to None.
        prepare_own_loop_if_not_found (bool, optional): _description_. Defaults to False.
        own_loop_shold_be_fast_loop (bool, optional): _description_. Defaults to True.
        own_loop_setup_coro_worker (Optional[AnyWorker], optional): _description_. Defaults to None.
        own_loop_setup_coro_worker_args_kwargs (Optional[Tuple[Tuple, Dict]], optional): _description_. Defaults to None.

    Raises:
        exception: _description_
        exception: _description_
        LoopWasEndedBeforeResultWasComputed: _description_
        TypeError: _description_
        TypeError: _description_

    Returns:
        _type_: _description_
    """    
    cs0 = cs
    def sync_coro_decorator(coro_worker: Worker):
        cs1 = cs0
        def wrapper(*args, **kwargs):
            cs = cs1
            done: ValueExistence = ValueExistence()
            async def coro(i: Interface, done: ValueExistence, coro_worker: Worker, *args, **kwargs):
                results: List[Tuple[CoroID, Any, Union[None, Exception]]] = await i(WaitCoro, WaitCoroRequest(timeout, kill_on_timeout, tree).put_list([PSCP(coro_worker, *args, **kwargs)]))
                done.value = results[0]
            
            direct_execution_required: bool = False
            if cs is None:
                cs = get_available_coro_scheduler()
            
            if (cs is None) and prepare_own_loop_if_not_found:
                if own_loop_setup_coro_worker_args_kwargs is None:
                    args: Tuple = tuple()
                    kwargs: Dict = dict()
                else:
                    args, kwargs = own_loop_setup_coro_worker_args_kwargs

                if own_loop_shold_be_fast_loop:
                    cs, _ = prepare_fast_loop(own_loop_setup_coro_worker, *args, **kwargs)
                else:
                    cs, _ = prepare_loop(own_loop_setup_coro_worker, *args, **kwargs)

            if cs is None:
                direct_execution_required = True
            else:
                i: Optional[Interface] = None
                inside_loop: bool = False
                inside_coro: bool = False
                try:
                    i = current_interface()
                    inside_loop = True
                    if i is not None:
                        inside_coro = True
                except OutsideCoroSchedulerContext:
                    pass

                if inside_loop:
                    if inside_coro:
                        inside_greenlet_coro: bool = False
                        if isinstance(i, InterfaceGreenlet):
                            inside_greenlet_coro = True
                        
                        if inside_greenlet_coro:
                            results: List[Tuple[CoroID, Any, Union[None, Exception]]] = i(WaitCoro, WaitCoroRequest(timeout, kill_on_timeout, tree).put_list([PSCP(coro_worker, *args, **kwargs)]))
                            _, result, exception = results[0]
                            if exception is not None:
                                raise exception
                            
                            return result
                        else:
                            pass
                    else:
                        pass
                else:
                    put_coro_to(get_interface_and_loop_with_explicit_loop(cs), coro, done, coro_worker, *args, **kwargs)
                    in_work = True
                    while in_work and (not done):
                        in_work = cs.iteration()
                    
                    if done:
                        _, result, exception = done.value
                        if exception is not None:
                            raise exception
                    else:
                        raise LoopWasEndedBeforeResultWasComputed

            if result_required:
                direct_execution_required = True
            else:
                put_coro_to(interface_and_loop_with_explicit_loop(cs), coro_worker, *args, **kwargs)

            if direct_execution_required:
                coro_worker_type: CoroType = find_coro_type(coro_worker)
                if CoroType.greenlet == coro_worker_type:
                    return coro_worker(InterfaceFake(None, None), *args, **kwargs)
                elif CoroType.awaitable == coro_worker_type:
                    raise TypeError(f'Can not directly execute awaitable {coro_worker} from non async environment')
                else:
                    raise TypeError(f'{coro_worker} is neither an awaitable nor a greenlet')
        
        return wrapper
    return sync_coro_decorator


def sync_coro(coro_worker: Worker):
    return sync_coro_param()(coro_worker)
