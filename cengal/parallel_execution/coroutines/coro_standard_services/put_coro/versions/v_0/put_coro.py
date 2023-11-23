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


__all__ = ['PutCoro', 'PutCoroRequest', 'put_current_from_other_service', 'put_from_other_service', 'put_root_from_other_service', 'put_coro_to', 'try_put_coro_to', 'aput_coro_to', 'atry_put_coro_to', 'put_coro', 'try_put_coro', 'aput_coro', 'atry_put_coro', 'travers_through_all_coro_children_on', 'try_travers_through_all_coro_children_on', 'travers_through_all_coro_children', 'try_travers_through_all_coro_children', 'get_set_of_all_coro_children_on', 'try_get_set_of_all_coro_children_on', 'get_set_of_all_coro_children', 'try_get_set_of_all_coro_children', 'travers_through_all_coro_parents_on', 'try_travers_through_all_coro_parents_on', 'travers_through_all_coro_parents', 'try_travers_through_all_coro_parents', 'get_set_of_all_coro_parents_on', 'try_get_set_of_all_coro_parents_on', 'get_set_of_all_coro_parents', 'try_get_set_of_all_coro_parents']

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services_internal_lib.service_with_a_direct_request import *
from cengal.code_flow_control.smart_values import ValueExistence
from cengal.introspection.inspect import get_exception, get_exception_tripple
from cengal.data_manipulation.tree_traversal import KeyMultiValueTreeTraversal, KeyValueTreeTraversal
from typing import Hashable, Tuple, List, Optional, Any, Union, cast, Dict, Callable, Set


class PutCoroRequest(ServiceRequest):
    def turn_on_tree_monitoring(self, turn_on: bool) -> bool:
        return self._save(0, turn_on)

    def tree_monitoring_state(self) -> bool:
        return self._save(1)

    # TODO: An implementation required:
    def set_on_children_start_handler(self, parent_coro_id: CoroID, handler: Callable) -> ServiceRequest:
        return self._save(2, parent_coro_id, handler)

    # TODO: An implementation required:
    def set_on_children_del_handler(self, parent_coro_id: CoroID, handler: Callable) -> ServiceRequest:
        return self._save(3, parent_coro_id, handler)

    def put_background_coro(self, coro_worker: AnyWorker, *args, **kwargs) -> ServiceRequest:
        return self._save(4, coro_worker, args, kwargs)


class PutCoro(ServiceWithADirectRequestMixin, DualImmediateProcessingServiceMixin, TypedService[CoroID]):
    def __init__(self, loop: CoroScheduler):
        super(PutCoro, self).__init__(loop)
        self._tree_monitoring_turned_on: bool = None
        self._single_task_registration_or_immediate_processing_single_impl: Callable = None
        self._single_task_registration_or_immediate_processing_single_impl_impl: Callable = None
        self._turn_on_tree_monitoring(False)
        self._tree_children_by_parent: Dict[CoroID, Set[CoroID]] = dict()
        self._tree_parent_by_child: Dict[CoroID, CoroID] = dict()
        self._dead_coroutines: Set[CoroID] = set()

        self._request_workers = {
            0: self._turn_on_tree_monitoring,
            1: self._tree_monitoring_state,
            4: self._put_background_coro,
        }

        self.direct_requests: List[Tuple] = list()
    
    def single_task_registration_or_immediate_processing_single(
            self, coro_worker: AnyWorker, *args, **kwargs
    ) -> Tuple[bool, Optional[CoroID], Any]:
        try:
            coro = self._single_task_registration_or_immediate_processing_single_impl(coro_worker, *args, **kwargs)
        except:
            return True, None, get_exception()

        return True, coro.coro_id, None
    
    def _single_task_registration_or_immediate_processing_single_impl_with_tree(
            self, coro_worker: AnyWorker, *args, **kwargs
    ) -> CoroWrapperBase:
        return self._single_task_registration_or_immediate_processing_single_impl_with_tree_impl(self.current_caller_coro_info.coro_id, coro_worker, *args, **kwargs)
    
    def _single_task_registration_or_immediate_processing_single_impl_with_tree_impl(
            self, parent_coro_id: CoroID, coro_worker: AnyWorker, *args, **kwargs
    ) -> CoroWrapperBase:
        coro: CoroWrapperBase = self._loop.put_coro(coro_worker, *args, **kwargs)
        child_coro_id: CoroID = coro.coro_id
        if parent_coro_id not in self._tree_children_by_parent:
            self._tree_children_by_parent[parent_coro_id] = set()
        
        self._tree_children_by_parent[parent_coro_id].add(child_coro_id)
        self._tree_parent_by_child[child_coro_id] = parent_coro_id
        coro.add_on_coro_del_handler(self._on_coro_del_handler)
        return coro
    
    def _single_task_registration_or_immediate_processing_single_impl_without_tree(
            self, coro_worker: AnyWorker, *args, **kwargs
    ) -> CoroWrapperBase:
        return self._single_task_registration_or_immediate_processing_single_impl_without_tree_impl(self.current_caller_coro_info.coro_id, coro_worker, *args, **kwargs)
    
    def _single_task_registration_or_immediate_processing_single_impl_without_tree_impl(
            self, parent_coro_id: CoroID, coro_worker: AnyWorker, *args, **kwargs
    ) -> CoroWrapperBase:
        return self._loop.put_coro(coro_worker, *args, **kwargs)
    
    def _turn_on_tree_monitoring(self, turn_on: bool):
        previous_state: bool = self._tree_monitoring_turned_on
        self._tree_monitoring_turned_on = turn_on
        if turn_on:
            self._single_task_registration_or_immediate_processing_single_impl = self._single_task_registration_or_immediate_processing_single_impl_with_tree
            self._single_task_registration_or_immediate_processing_single_impl_impl = self._single_task_registration_or_immediate_processing_single_impl_with_tree_impl
        else:
            self._single_task_registration_or_immediate_processing_single_impl = self._single_task_registration_or_immediate_processing_single_impl_without_tree
            self._single_task_registration_or_immediate_processing_single_impl_impl = self._single_task_registration_or_immediate_processing_single_impl_without_tree_impl
        
        return True, previous_state, None
    
    def put_from_other_service(
            self, coro_id: CoroID, coro_worker: AnyWorker, *args, **kwargs
        ) -> CoroWrapperBase:
        return self._single_task_registration_or_immediate_processing_single_impl_impl(coro_id, coro_worker, *args, **kwargs)
    
    def put_root_from_other_service(
            self, coro_worker: AnyWorker, *args, **kwargs
        ) -> CoroWrapperBase:
        return self._loop.put_coro(coro_worker, *args, **kwargs)
    
    def _tree_monitoring_state(self):
        return True, self._tree_monitoring_turned_on, None
    
    def _put_background_coro(self, coro_worker: AnyWorker, args, kwargs):
        try:
            coro: CoroWrapperBase = self._single_task_registration_or_immediate_processing_single_impl(coro_worker, *args, **kwargs)
            coro.is_background_coro = True
        except:
            return True, None, get_exception()

        return True, coro.coro_id, None

    def full_processing_iteration(self):
        if self._dead_coroutines:
            dead_coroutines_buff = self._dead_coroutines
            self._dead_coroutines = type(dead_coroutines_buff)()
            for dead_coro_id in dead_coroutines_buff:
                parent_coro_id = self._tree_parent_by_child.get(dead_coro_id, None)
                children = self._tree_children_by_parent.get(dead_coro_id, None)
                if parent_coro_id is None:
                    if children is not None:
                        for child_coro_id in children:
                            self._tree_parent_by_child.pop(child_coro_id, None)
                else:
                    sibblings = self._tree_children_by_parent[parent_coro_id]
                    sibblings.discard(dead_coro_id)
                    if children is not None:
                        sibblings.update(children)
                        for child_coro_id in children:
                            self._tree_parent_by_child[child_coro_id] = parent_coro_id

        if self.direct_requests:
            direct_requests_buff = self.direct_requests
            self.direct_requests = type(direct_requests_buff)()
            for coro_worker, args, kwargs in direct_requests_buff:
                try:
                    coro = self._loop.put_coro(coro_worker, *args, **kwargs)
                except:
                    ex_type, exception, tracback = get_exception_tripple()
                    if __debug__: dlog(ex_type, exception, tracback)
                    raise

        self.make_dead()
    
    def _add_direct_request(self, coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[None]:
        self.direct_requests.append((coro_worker, args, kwargs))
        self.make_live()
        return ValueExistence()

    def _on_coro_del_handler(self, coro: CoroWrapperBase) -> bool:
        self._dead_coroutines.add(coro.coro_id)
        self.make_live()
        return False
    
    def travers_through_all_children(self, coro_id, handler: Callable[[int, CoroID, CoroID, int], None], on_switched_to_stack_based_implementation: Optional[Callable]=None):
        t = KeyMultiValueTreeTraversal(self._tree_children_by_parent, None, handler, on_switched_to_stack_based_implementation)
        t(coro_id)
    
    def get_set_of_all_children(self, coro_id) -> Set[CoroID]:
        result = set()
        def handler(deep, parent, child: ValueExistence[CoroID], index):
            if child:
                result.add(child.value)
        
        self.travers_through_all_children(coro_id, handler)
        result.discard(coro_id)
        return result
    
    def travers_through_all_parents(self, coro_id, handler: Callable[[CoroID, CoroID], None], on_switched_to_stack_based_implementation: Optional[Callable]=None):
        t = KeyValueTreeTraversal(self._tree_parent_by_child, None, handler, on_switched_to_stack_based_implementation)
        t(coro_id)
    
    def get_set_of_all_parents(self, coro_id):
        result = set()
        def handler(deep, child, parent, index):
            if parent is not None:
                result.add(parent)
        
        self.travers_through_all_parents(coro_id, handler)
        result.discard(coro_id)
        return result

    def in_work(self) -> bool:
        result: bool = bool(self.direct_requests) or bool(self._dead_coroutines)
        return self.thrifty_in_work(result)


PutCoroRequest.default_service_type = PutCoro


def put_current_from_other_service(current_service: Service, coro_worker: AnyWorker, *args, **kwargs) -> CoroWrapperBase:
    put_coro: PutCoro = current_service._loop.get_service_instance(PutCoro)
    return put_coro.put_from_other_service(current_service.current_caller_coro_info.coro_id, coro_worker, *args, **kwargs)


def put_from_other_service(current_service: Service, coro_id: CoroID, coro_worker: AnyWorker, *args, **kwargs) -> CoroWrapperBase:
    put_coro: PutCoro = current_service._loop.get_service_instance(PutCoro)
    return put_coro.put_from_other_service(coro_id, coro_worker, *args, **kwargs)


def put_root_from_other_service(current_service: Service, coro_worker: AnyWorker, *args, **kwargs) -> CoroWrapperBase:
    put_coro: PutCoro = current_service._loop.get_service_instance(PutCoro)
    return put_coro.put_root_from_other_service(coro_worker, *args, **kwargs)


def put_coro_to(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[Optional[CoroID]]:
    """_summary_
        context can be generated by one of the [interface_and_loop_with_backup_loop, get_interface_and_loop_with_backup_loop, interface_and_loop_with_explicit_loop, get_interface_and_loop_with_explicit_loop, interface_for_an_explicit_loop, get_interface_for_an_explicit_loop] functions from the cengal/parallel_execution/coroutines/coro_scheduler module
        
        An example:

        from cengal.parallel_execution.coroutines.coro_scheduler import get_interface_and_loop_with_explicit_loop, CoroScheduler, ExplicitWorker, Worker, CoroID
        from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import put_coro_to
        from typing import Optional, Union

        def my_func(loop: CoroScheduler, coro_worker: AnyWorker, a, b) -> Optional[CoroID]:
            resulting_coro_id: Optional[CoroID] = None
            try:
                result = put_coro_to(get_interface_and_loop_with_explicit_loop(loop), coro_worker, a, b)
                if result:
                    print(f'We are inside of the loop AND in the coroutine. Our requested coro already was created at this moment. Coro id: {result.value}')
                    resulting_coro_id = result.value
                else:
                    print('We are outside of the loop or not in the coroutine body. Our requested coroutine will be created in the near future.')
            except CoroSchedulerContextIsNotAvailable:
                print('We are outside of the loop AND no loop was selected as a Primary AND our given `loop` var is None)
            
            return resulting_coro_id
        
    Args:
        context (Tuple[Optional[CoroScheduler], Optional[Interface], bool]): _description_
        coro_worker (AnyWorker): _description_

    Returns:
        ValueExistence[Optional[CoroID]]: _description_
    """
    return make_request_to_service_with_context(context, PutCoro, coro_worker, *args, **kwargs)


def try_put_coro_to(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[Optional[CoroID]]:
    """_summary_
        context can be generated by one of the [interface_and_loop_with_backup_loop, get_interface_and_loop_with_backup_loop, interface_and_loop_with_explicit_loop, get_interface_and_loop_with_explicit_loop, interface_for_an_explicit_loop, get_interface_for_an_explicit_loop] functions from the cengal/parallel_execution/coroutines/coro_scheduler module
        
        An example:

        from cengal.parallel_execution.coroutines.coro_scheduler import get_interface_and_loop_with_explicit_loop, CoroScheduler, ExplicitWorker, Worker, CoroID
        from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import try_put_coro_to
        from typing import Optional, Union

        def my_func(loop: CoroScheduler, coro_worker: AnyWorker, a, b) -> Optional[CoroID]:
            resulting_coro_id: Optional[CoroID] = None
            result = put_coro_to(get_interface_and_loop_with_explicit_loop(loop), coro_worker, a, b)
            if result:
                print(f'We are inside of the loop AND in the coroutine. Our requested coro already was created at this moment. Coro id: {result.value}')
                resulting_coro_id = result.value
            else:
                print('There are two possibilities:)
                print('1) We are outside of the loop or not in the coroutine body. Our requested coroutine will be created in the near future.')
                print('2) We are outside of the loop AND no loop was selected as a Primary AND our given `loop` var is None. Our requested coroutine will NOT be created at all.)
            
            return resulting_coro_id
        
    Args:
        context (Tuple[Optional[CoroScheduler], Optional[Interface], bool]): _description_
        coro_worker (AnyWorker): _description_

    Returns:
        ValueExistence[Optional[CoroID]]: _description_
    """
    return try_make_request_to_service_with_context(context, PutCoro, coro_worker, *args, **kwargs)


async def aput_coro_to(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[CoroID]:
    return await amake_request_to_service_with_context(context, PutCoro, coro_worker, *args, **kwargs)


async def atry_put_coro_to(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[Optional[CoroID]]:
    return await atry_make_request_to_service_with_context(context, PutCoro, coro_worker, *args, **kwargs)


def put_coro(coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[CoroID]:
    return make_request_to_service(PutCoro, coro_worker, *args, **kwargs)


def try_put_coro(coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[Optional[CoroID]]:
    return try_make_request_to_service(PutCoro, coro_worker, *args, **kwargs)


async def aput_coro(coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[CoroID]:
    return await amake_request_to_service(PutCoro, coro_worker, *args, **kwargs)


async def atry_put_coro(coro_worker: AnyWorker, *args, **kwargs) -> ValueExistence[Optional[CoroID]]:
    return await atry_make_request_to_service(PutCoro, coro_worker, *args, **kwargs)


# ==================================================


def travers_through_all_coro_children_on(prioritized_coro_scheduler: Optional[CoroScheduler], coro_id, handler: Callable[[int, CoroID, CoroID, int], None], on_switched_to_stack_based_implementation: Optional[Callable]=None) -> ValueExistence[CoroID]:
    put_coro: PutCoro = service_with_explicit_loop(PutCoro, prioritized_coro_scheduler)
    return put_coro.travers_through_all_children(coro_id, handler, on_switched_to_stack_based_implementation)


def try_travers_through_all_coro_children_on(prioritized_coro_scheduler: Optional[CoroScheduler], coro_id, handler: Callable[[int, CoroID, CoroID, int], None], on_switched_to_stack_based_implementation: Optional[Callable]=None) -> ValueExistence[Optional[CoroID]]:
    put_coro: PutCoro = get_service_with_explicit_loop(PutCoro, prioritized_coro_scheduler)
    if put_coro is not None:
        return put_coro.travers_through_all_children(coro_id, handler, on_switched_to_stack_based_implementation)


def travers_through_all_coro_children(coro_id, handler: Callable[[int, CoroID, CoroID, int], None], on_switched_to_stack_based_implementation: Optional[Callable]=None) -> ValueExistence[CoroID]:
    return travers_through_all_coro_children_on(get_available_coro_scheduler(), coro_id, handler, on_switched_to_stack_based_implementation)


def try_travers_through_all_coro_children(coro_id, handler: Callable[[int, CoroID, CoroID, int], None], on_switched_to_stack_based_implementation: Optional[Callable]=None) -> ValueExistence[Optional[CoroID]]:
    return try_travers_through_all_coro_children_on(get_available_coro_scheduler(), coro_id, handler, on_switched_to_stack_based_implementation)


# ==================================================


def get_set_of_all_coro_children_on(prioritized_coro_scheduler: Optional[CoroScheduler], coro_id) -> Set[CoroID]:
    put_coro: PutCoro = service_with_explicit_loop(PutCoro, prioritized_coro_scheduler)
    return put_coro.get_set_of_all_children(coro_id)


def try_get_set_of_all_coro_children_on(prioritized_coro_scheduler: Optional[CoroScheduler], coro_id) -> Optional[Set[CoroID]]:
    put_coro: PutCoro = get_service_with_explicit_loop(PutCoro, prioritized_coro_scheduler)
    if put_coro is not None:
        return put_coro.get_set_of_all_children(coro_id)


def get_set_of_all_coro_children(coro_id) -> Set[CoroID]:
    return get_set_of_all_coro_children_on(get_available_coro_scheduler(), coro_id)


def try_get_set_of_all_coro_children(coro_id) -> Optional[Set[CoroID]]:
    return try_get_set_of_all_coro_children_on(get_available_coro_scheduler(), coro_id)


# ==================================================


def travers_through_all_coro_parents_on(prioritized_coro_scheduler: Optional[CoroScheduler], coro_id, handler: Callable[[int, CoroID, CoroID, int], None], on_switched_to_stack_based_implementation: Optional[Callable]=None) -> ValueExistence[CoroID]:
    put_coro: PutCoro = service_with_explicit_loop(PutCoro, prioritized_coro_scheduler)
    return put_coro.travers_through_all_parents(coro_id, handler, on_switched_to_stack_based_implementation)


def try_travers_through_all_coro_parents_on(prioritized_coro_scheduler: Optional[CoroScheduler], coro_id, handler: Callable[[int, CoroID, CoroID, int], None], on_switched_to_stack_based_implementation: Optional[Callable]=None) -> ValueExistence[Optional[CoroID]]:
    put_coro: PutCoro = get_service_with_explicit_loop(PutCoro, prioritized_coro_scheduler)
    if put_coro is not None:
        return put_coro.travers_through_all_parents(coro_id, handler, on_switched_to_stack_based_implementation)


def travers_through_all_coro_parents(coro_id, handler: Callable[[int, CoroID, CoroID, int], None], on_switched_to_stack_based_implementation: Optional[Callable]=None) -> ValueExistence[CoroID]:
    return travers_through_all_coro_parents_on(get_available_coro_scheduler(), coro_id, handler, on_switched_to_stack_based_implementation)


def try_travers_through_all_coro_parents(coro_id, handler: Callable[[int, CoroID, CoroID, int], None], on_switched_to_stack_based_implementation: Optional[Callable]=None) -> ValueExistence[Optional[CoroID]]:
    return try_travers_through_all_coro_parents_on(get_available_coro_scheduler(), coro_id, handler, on_switched_to_stack_based_implementation)


# ==================================================


def get_set_of_all_coro_parents_on(prioritized_coro_scheduler: Optional[CoroScheduler], coro_id) -> ValueExistence[CoroID]:
    put_coro: PutCoro = service_with_explicit_loop(PutCoro, prioritized_coro_scheduler)
    return put_coro.get_set_of_all_parents(coro_id)


def try_get_set_of_all_coro_parents_on(prioritized_coro_scheduler: Optional[CoroScheduler], coro_id) -> ValueExistence[Optional[CoroID]]:
    put_coro: PutCoro = get_service_with_explicit_loop(PutCoro, prioritized_coro_scheduler)
    if put_coro is not None:
        return put_coro.get_set_of_all_parents(coro_id)


def get_set_of_all_coro_parents(coro_id) -> ValueExistence[CoroID]:
    return get_set_of_all_coro_parents_on(get_available_coro_scheduler(), coro_id)


def try_get_set_of_all_coro_parents(coro_id) -> ValueExistence[Optional[CoroID]]:
    return try_get_set_of_all_coro_parents_on(get_available_coro_scheduler(), coro_id)
