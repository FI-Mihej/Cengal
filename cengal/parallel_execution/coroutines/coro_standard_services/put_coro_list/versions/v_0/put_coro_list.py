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


__all__ = ['PutSingleCoroParams', 'PSCP', 'PutCoroList', 'put_coro_list_to', 'try_put_coro_list_to', 'aput_coro_list_to', 'atry_put_coro_list_to', 'put_coro_list', 'try_put_coro_list', 'aput_coro_list', 'atry_put_coro_list']


from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro
from cengal.parallel_execution.coroutines.coro_standard_services_internal_lib.service_with_a_direct_request import *
from cengal.code_flow_control.smart_values import ValueExistence
from cengal.introspection.inspect import get_exception, get_exception_tripple
from cengal.code_flow_control.args_manager import EntityArgsHolder
from typing import Sequence, Tuple, List, Optional, Any, cast, Dict, Union


class PutSingleCoroParams:
    def __init__(self, coro_worker: AnyWorker, *args, **kwargs) -> None:
        self.coro_worker: AnyWorker = coro_worker
        self.args: Tuple = args
        self.kwargs: Dict = kwargs
    
    def __call__(self) -> Any:
        return self.coro_worker, self.args, self.kwargs


PSCP = PutSingleCoroParams


class PutCoroList(TypedService[List[Tuple[Optional[CoroID], Optional[Exception]]]], ServiceWithADirectRequestMixin):
    def __init__(self, loop: CoroScheduler):
        super(PutCoroList, self).__init__(loop)
        self.direct_requests: List[Tuple] = list()

    def single_task_registration_or_immediate_processing(
            self, coro_list: Sequence[PutSingleCoroParams]
    ) -> Tuple[bool, Optional[CoroID], Any]:
        results = list()
        try:
            put_coro: PutCoro = self._loop.get_service_instance(PutCoro)
            caller_coro_id: CoroID = self.current_caller_coro_info.coro_id
            for request in coro_list:
                result_coro_id = None
                exception = None
                try:
                    coro_worker, args, kwargs = request()
                    coro = put_coro.put_from_other_service(caller_coro_id, coro_worker, *args, **kwargs)
                    result_coro_id = coro.coro_id
                except:
                    exception = get_exception()

                results.append((result_coro_id, exception))
        except:
            return True, results, get_exception()

        return True, results, None

    def full_processing_iteration(self):
        put_coro: PutCoro = self._loop.get_service_instance(PutCoro)
        direct_requests_buff = self.direct_requests
        self.direct_requests = type(direct_requests_buff)()
        for coro_list in direct_requests_buff:
            for request in coro_list:
                coro_worker, args, kwargs = request()
                try:
                    coro = put_coro.put_root_from_other_service(coro_worker, *args, **kwargs)
                except:
                    ex_type, exception, tracback = get_exception_tripple()
                    if __debug__: dlog(ex_type, exception, tracback)
                    raise

        self.make_dead()
    
    def _add_direct_request(self, coro_list: Sequence[PutSingleCoroParams]) -> ValueExistence[None]:
        self.direct_requests.append(coro_list)
        self.make_live()
        return ValueExistence()

    def in_work(self) -> bool:
        result = bool(self.direct_requests)
        return self.thrifty_in_work(result)


def put_coro_list_to(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], coro_list: Sequence[PutSingleCoroParams]) -> ValueExistence[CoroID]:
    return make_request_to_service_with_context(context, PutCoroList, coro_list)


def try_put_coro_list_to(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], coro_list: Sequence[PutSingleCoroParams]) -> ValueExistence[Optional[CoroID]]:
    return try_make_request_to_service_with_context(context, PutCoroList, coro_list)


async def aput_coro_list_to(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], coro_list: Sequence[PutSingleCoroParams]) -> ValueExistence[CoroID]:
    return await amake_request_to_service_with_context(context, PutCoroList, coro_list)


async def atry_put_coro_list_to(context: Tuple[Optional[CoroScheduler], Optional[Interface], bool], coro_list: Sequence[PutSingleCoroParams]) -> ValueExistence[Optional[CoroID]]:
    return await atry_make_request_to_service_with_context(context, PutCoroList, coro_list)


def put_coro_list(coro_list: Sequence[PutSingleCoroParams]) -> ValueExistence[CoroID]:
    return make_request_to_service(PutCoroList, coro_list)


def try_put_coro_list(coro_list: Sequence[PutSingleCoroParams]) -> ValueExistence[Optional[CoroID]]:
    return try_make_request_to_service(PutCoroList, coro_list)


async def aput_coro_list(coro_list: Sequence[PutSingleCoroParams]) -> ValueExistence[CoroID]:
    return await amake_request_to_service(PutCoroList, coro_list)


async def atry_put_coro_list(coro_list: Sequence[PutSingleCoroParams]) -> ValueExistence[Optional[CoroID]]:
    return await atry_make_request_to_service(PutCoroList, coro_list)
