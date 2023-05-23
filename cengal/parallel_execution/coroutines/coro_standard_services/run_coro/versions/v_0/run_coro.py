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
__version__ = "3.2.2"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


__all__ = ['RunCoro']

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.introspection.inspect import get_exception, get_exception_tripple
from cengal.parallel_execution.coroutines.coro_standard_services_internal_lib.service_with_a_direct_request import *
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import put_current_from_other_service
from cengal.code_flow_control.smart_values import ValueExistence
from typing import Any, Optional, Tuple, Dict, Set, Union
import sys


class RunCoro(ServiceWithADirectRequestMixin, TypedService[Any]):
    def __init__(self, loop: CoroScheduler):
        super(RunCoro, self).__init__(loop)
        self.called_by: Dict[CoroID, CoroID] = dict()  # Dict[CoroID, CoroID] # key - callable; value - requester
        self.results: Set[Tuple[CoroID, Any, Optional[BaseException]]] = set()  # (id, result, exception)
    
    def single_task_registration_or_immediate_processing(
            self, coro_worker: AnyWorker, *args, **kwargs) -> Tuple[bool, Any, Optional[BaseException]]:
        requester_id = self.current_caller_coro_info.coro_id
        try:
            coro: CoroWrapperBase = put_current_from_other_service(self, coro_worker, *args, **kwargs)
        except:
            ex_type, exception, tracback = get_exception_tripple()
            if __debug__: dlog(ex_type, exception, tracback)
            exception = exception.with_traceback(tracback)
            return True, None, exception
        
        coro.add_on_coro_del_handler(self._on_coro_del_handler)
        self.called_by[coro.coro_id] = requester_id
        return False, None, None

    def full_processing_iteration(self):
        for coro_id, result, exception in self.results:
            self.register_response(self.called_by[coro_id], result, exception)
            del self.called_by[coro_id]
        
        self.results = type(self.results)()
        self.make_dead()

    def in_work(self) -> bool:
        result: bool = bool(self.results)
        return self.thrifty_in_work(result)

    def _on_coro_del_handler(self, coro: CoroWrapperBase) -> bool:
        self.results.add((coro.coro_id, coro.last_result, coro.exception))
        self.make_live()
        return True
