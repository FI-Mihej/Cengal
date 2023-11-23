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


__all__ = ['WaitCoro', 'PutSingleCoroParams', 'PSCP', 'WaitCoroRequest', 'CoroutineNotFoundError', 'SubCoroutineNotFoundError', 'TimeoutError', 'SubTimeoutError']

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro_list import PutSingleCoroParams, PSCP
from cengal.parallel_execution.coroutines.coro_standard_services.timer_func_runner import timer_func_run_on
from cengal.parallel_execution.coroutines.coro_standard_services.kill_coro import kill_coro_on
from cengal.introspection.inspect import get_exception
from cengal.data_manipulation.conversion.reinterpret_cast import reinterpret_cast
from typing import Any, Optional, Sequence, Tuple, Dict, Set, Union, List, overload, Type


class CoroutineNotFoundError(Exception):
    pass


class SubCoroutineNotFoundError(CoroutineNotFoundError):
    pass


class TimeoutError(Exception):
    pass


class SubTimeoutError(TimeoutError):
    pass


class ServParams:
    @overload
    def __init__(self, service_request_type: Type[TypedServiceRequest[ServiceResponseTypeVar]], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    def __init__(self, service_request: TypedServiceRequest[ServiceResponseTypeVar]) -> ServiceResponseTypeVar: ...

    @overload
    def __init__(self, service_type: Type[TypedService[ServiceResponseTypeVar]], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    def __init__(self, service_type: ServiceType, service_request: TypedServiceRequest[ServiceResponseTypeVar]) -> ServiceResponseTypeVar: ...

    @overload
    def __init__(self, service_request_type: Type[ServiceRequest], *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    def __init__(self, service_request: ServiceRequest) -> ServiceResponseTypeVar: ...

    @overload
    def __init__(self, service_type: ServiceType, *args, **kwargs) -> ServiceResponseTypeVar: ...

    @overload
    def __init__(self, service_type: ServiceType, service_request: ServiceRequest) -> ServiceResponseTypeVar: ...

    def __init__(self, service_type, *args, **kwargs) -> None:
        self.service_type: NormalizableServiceType = service_type
        self.args: Tuple = args
        self.kwargs: Dict = kwargs
    
    def __call__(self) -> Tuple[NormalizableServiceType, Tuple, Dict]:
        return self.service_type, self.args, self.kwargs


SP = ServParams


class WaitCoroRequest(ServiceRequest):
    def __init__(self, timeout: Optional[float] = None, kill_on_timeout: bool = True, tree: bool = True, result_required: bool = True):
        super().__init__()
        self.provide_to_request_handler = True
        self.timeout: Optional[float] = timeout
        self.kill_on_timeout: bool = kill_on_timeout
        self.tree: bool = tree
        self.result_required: bool = result_required

    def single(self, coro_id: CoroID) -> Union[Any, None]:
        return self._save(0, coro_id)

    def list(self, coro_list: Sequence[CoroID]) -> ServiceRequest:
        return self._save(1, coro_list)

    def atomic(self, coro_list: Sequence[CoroID]) -> ServiceRequest:
        return self._save(2, coro_list)

    def fastest(self, coro_list: Sequence[CoroID], num: int = 1, measure_time: bool = False) -> ServiceRequest:
        return self._save(3, coro_list, num, measure_time)

    def put_single(self, coro_worker: Worker, *args, **kwargs) -> ServiceRequest:
        return self._save(4, coro_worker, *args, **kwargs)

    def put_list(self, coro_list: Sequence[PutSingleCoroParams]) -> List[Tuple[CoroID, Any, Optional[Exception]]]:
        return self._save(5, coro_list)

    def put_atomic(self, coro_list: Sequence[PutSingleCoroParams]) -> ServiceRequest:
        return self._save(6, coro_list)

    def put_fastest(self, coro_list: Sequence[PutSingleCoroParams], num: int=1, measure_time: bool=False) -> ServiceRequest:
        return self._save(7, coro_list, num, measure_time)

    def serv_list(self, serv_params_list: Sequence[ServParams]) -> List[Tuple[CoroID, Any, Optional[Exception]]]:
        """Creates a coroutine for each service request and waits for the result of each of them.

        Args:
            serv_params_list (Sequence[ServParams]): _description_

        Returns:
            List[Tuple[CoroID, Any, Optional[Exception]]]: _description_
        """        
        return self._save(8, serv_params_list)

    def serv_atomic(self, serv_params_list: Sequence[ServParams]) -> ServiceRequest:
        """Creates a coroutine for each service request and waits for the result of each of them. If one of the coroutines fails, the others are killed which may lead to cancel request processing in some services (see documentation of the service you are trying to use here).

        Args:
            serv_params_list (Sequence[ServParams]): _description_

        Returns:
            ServiceRequest: _description_
        """        
        return self._save(9, serv_params_list)

    def serv_fastest(self, serv_params_list: Sequence[ServParams], num: int=1, measure_time: bool=False) -> ServiceRequest:
        """Creates a coroutine for each service request and waits for the result of each of them. When one of coroutines finished, the others are killed which may lead to cancel request processing in some services (see documentation of the service you are trying to use here)

        Args:
            serv_params_list (Sequence[ServParams]): _description_
            num (int, optional): _description_. Defaults to 1.
            measure_time (bool, optional): _description_. Defaults to False.

        Returns:
            ServiceRequest: _description_
        """        
        return self._save(10, serv_params_list, num, measure_time)

    def serv_and_forget_single(self, serv_params: ServParams) -> None:
        """Creates a coroutine for a service request and returns immediately.

        Args:
            serv_params (ServParams): _description_

        Returns:
            _type_: _description_
        """        
        return self._save(11, serv_params)

    def serv_and_forget_list(self, serv_params_list: Sequence[ServParams]) -> None:
        """Creates a coroutine for each service request and returns immediately.

        Args:
            serv_params_list (Sequence[ServParams]): _description_

        Returns:
            _type_: _description_
        """        
        return self._save(12, serv_params_list)


class SingleMethod(ServiceRequestMethodMixin):

    def __init__(self, service):
        super().__init__(service)
        self.single_called_by: Dict[CoroID, CoroID] = dict()  # Dict[CoroID, CoroID] # key - callable; value - requester
        self.new_single_results: Set[Tuple[CoroID, Any, Optional[BaseException]]] = set()  # (id, result, exception)
        self.result_required_by: Dict[CoroID, bool] = dict()

    def __call__(self, request: WaitCoroRequest, coro_id: CoroID) -> ServiceProcessingResponse:
        requester_id: CoroID = self.service.current_caller_coro_info.coro_id
        coro: CoroWrapperBase = self.service._loop.get_coro(coro_id)
        if coro is None:
            return (True, None, CoroutineNotFoundError(coro_id))

        coro.add_on_coro_del_handler(self._on_coro_del_handler)
        self.single_called_by[coro_id] = requester_id
        self.result_required_by[requester_id] = request.result_required
        timeout: Optional[float] = request.timeout
        if timeout is not None:
            def timeout_handler(coro_id: CoroID, kill_on_timeout: bool, tree: bool):
                if coro_id in self.single_called_by:
                    self.new_single_results.add((coro_id, None, TimeoutError(coro_id)))
                    self.service.make_live()
                    if kill_on_timeout:
                        kill_coro_on(get_interface_and_loop_with_explicit_loop(self.service._loop), coro_id, tree)
            
            timer_func_run_on(get_interface_and_loop_with_explicit_loop(self.service._loop), timeout, timeout_handler, coro_id, request.kill_on_timeout, request.tree)

        return (False, None, None)

    def full_processing_iteration(self):
        for coro_id, result, exception in self.new_single_results:
            try:
                requester_id: CoroID = self.single_called_by[coro_id]
                if self.result_required_by[requester_id]:
                    if CoroutineNotFoundError == type(exception):
                        reinterpret_cast(SubCoroutineNotFoundError, exception)
                    elif TimeoutError == type(exception):
                        reinterpret_cast(SubTimeoutError, exception)
                    
                    self.service.register_response(requester_id, result, exception)
                else:
                    self.service.register_response(requester_id, None, None)
                
                del self.result_required_by[requester_id]
                del self.single_called_by[coro_id]
            except KeyError:
                pass

        self.new_single_results = type(self.new_single_results)()

    def in_work(self) -> bool:
        return bool(self.new_single_results)

    def _on_coro_del_handler(self, coro: CoroWrapperBase) -> bool:
        if coro.coro_id in self.single_called_by:
            self.new_single_results.add((coro.coro_id, coro.last_result, coro.exception))
            self.service.make_live()
        
        return True


class ListMethod(ServiceRequestMethodMixin):

    def __init__(self, service):
        super().__init__(service)

    def __call__(self, request: WaitCoroRequest, coro_list: Sequence[Tuple[(Optional[CoroType], Worker, Tuple, Dict)]]) -> ServiceProcessingResponse:
        requester_id = self.service.current_caller_coro_info.coro_id
        for coro_id in coro_list:
            coro = self.service._loop.get_coro(coro_id)
            if coro is None:
                return (True, None, CoroutineNotFoundError(coro_id))
            else:
                coro.add_on_coro_del_handler(self._on_coro_del_handler)
                self.list_called_by[coro_id] = requester_id
                if requester_id not in self.list_wait_by_caller:
                    self.list_wait_by_caller[requester_id] = set()
                
                self.list_wait_by_caller[requester_id].add(coro_id)
                # timeout: Optional[float] = request.timeout
                # if timeout is not None:
                #     def timeout_handler(requester_id: CoroID, coro_id: CoroID, kill_on_timeout: bool, tree: bool):
                #         if coro_id in self.single_called_by:
                #             self.new_single_results.add((coro_id, None, TimeoutError(coro_id)))
                #             self.service.make_live()
                #             if kill_on_timeout:
                #                 kill_coro_on(get_interface_and_loop_with_explicit_loop(self.service._loop), coro_id, tree)
                    
                #     timer_func_run_on(get_interface_and_loop_with_explicit_loop(self.service._loop), timeout, timeout_handler, requester_id, coro_id, request.kill_on_timeout, request.tree)


        self.service.make_dead()
        return (False, None, None)

    def full_processing_iteration(self):
        raise NotImplementedError

    def in_work(self) -> bool:
        raise NotImplementedError

    def _on_coro_del_handler(self, coro: CoroWrapperBase) -> bool:
        if coro.coro_id in self.single_called_by:
            self.new_list_results.add((coro.coro_id, coro.last_result, coro.exception))
            self.service.make_live()
        
        return True


class PutListMethod(ServiceRequestMethodMixin):

    def __init__(self, service):
        super().__init__(service)
        self.called_by = dict()
        self.caller_waiting_set: Dict[CoroID, Set[CoroID]] = dict()
        self.coro_indexes = dict()
        self.caller_results = dict()
        self.ready_requesters = set()

    def __call__(self, request: WaitCoroRequest, coro_list: Sequence[PutSingleCoroParams]) -> ServiceProcessingResponse:
        coroutines_list = list()
        results = list()
        requester_id = self.service.current_caller_coro_info.coro_id
        try:
            put_coro: PutCoro = self.service._loop.get_service_instance(PutCoro)
            for coro_request in coro_list:
                exception = None
                result_coro_id = None
                try:
                    coro_worker, args, kwargs = coro_request()
                    coro: CoroWrapperBase = put_coro.put_from_other_service(requester_id, coro_worker, *args, **kwargs)
                    coroutines_list.append(coro)
                    result_coro_id = coro.coro_id
                except:
                    exception = get_exception()

                results.append((result_coro_id, exception))
        except:
            return True, results, get_exception()
        else:
            if not coroutines_list:
                return True, results, None
            
            if requester_id not in self.caller_waiting_set:
                self.caller_waiting_set[requester_id] = set()
            if requester_id not in self.coro_indexes:
                self.coro_indexes[requester_id] = dict()
            if requester_id not in self.caller_results:
                self.caller_results[requester_id] = [
                 None] * len(coroutines_list)
            for index, coro in enumerate(coroutines_list):
                coro_id = coro.coro_id
                self.called_by[coro_id] = requester_id
                self.caller_waiting_set[requester_id].add(coro_id)
                self.coro_indexes[requester_id][coro_id] = index
                coro.add_on_coro_del_handler(self._on_coro_del_handler)

            timeout: Optional[float] = request.timeout
            if timeout is not None:
                def timeout_handler(requester_id: CoroID, kill_on_timeout: bool, tree: bool):
                    if requester_id not in self.caller_waiting_set:
                        return
                    
                    caller_waiting_set = self.caller_waiting_set[requester_id]
                    del self.caller_waiting_set[requester_id]
                    for coro_id in caller_waiting_set:
                        del self.called_by[coro_id]
                        index = self.coro_indexes[requester_id][coro_id]
                        del self.coro_indexes[requester_id][coro_id]
                        self.caller_results[requester_id][index] = (coro_id, None, coro.exception)  # TODO: should return TimeoutError exception instead
                        if kill_on_timeout:
                            kill_coro_on(get_interface_and_loop_with_explicit_loop(self.service._loop), coro_id, tree)

                    del self.coro_indexes[requester_id]
                    self.ready_requesters.add(requester_id)
                    self.service.make_live()
                
                timer_func_run_on(get_interface_and_loop_with_explicit_loop(self.service._loop), timeout, timeout_handler, requester_id, request.kill_on_timeout, request.tree)

            return False, None, None

    def full_processing_iteration(self):
        ready_requesters_buff = self.ready_requesters
        self.ready_requesters = type(ready_requesters_buff)()
        for requester_id in ready_requesters_buff:
            self.service.register_response(requester_id, self.caller_results[requester_id], None)
            del self.caller_results[requester_id]

    def in_work(self) -> bool:
        return bool(self.ready_requesters)

    def _on_coro_del_handler(self, coro: CoroWrapperBase) -> bool:
        coro_id = coro.coro_id
        if coro_id in self.called_by:
            requester_id = self.called_by[coro_id]
            del self.called_by[coro_id]
            self.caller_waiting_set[requester_id].remove(coro_id)
            if not self.caller_waiting_set[requester_id]:
                del self.caller_waiting_set[requester_id]
            
            index = self.coro_indexes[requester_id][coro_id]
            del self.coro_indexes[requester_id][coro_id]
            self.caller_results[requester_id][index] = (coro.coro_id, coro.last_result, coro.exception)
            if not self.coro_indexes[requester_id]:
                del self.coro_indexes[requester_id]
                self.ready_requesters.add(requester_id)
                self.service.make_live()

        return True


class WaitCoro(Service):

    def __init__(self, loop):
        super(WaitCoro, self).__init__(loop)
        self._single = SingleMethod(self)
        self._list = ListMethod(self)
        self._put_list = PutListMethod(self)

        self._request_workers = {
            0:self._single,
            1:self.not_implemented,
            2:self.not_implemented,
            3:self.not_implemented,
            4:self.not_implemented,
            5:self._put_list,
            6:self.not_implemented,
            7:self.not_implemented
        }

    def single_task_registration_or_immediate_processing(self, request: Optional[WaitCoroRequest]) -> ServiceProcessingResponse:
        if request is not None:
            return self.resolve_request(request)
            
        return (True, None, WrongServiceRequestError())

    def full_processing_iteration(self):
        self._single.full_processing_iteration()
        self._put_list.full_processing_iteration()
        if not self.in_work():
            self.make_dead()

    def in_work(self) -> bool:
        result: bool = self._single.in_work() or self._put_list.in_work()
        return self.thrifty_in_work(result)

    def not_implemented(self):
        raise NotImplementedError


WaitCoroRequest.default_service_type = WaitCoro
