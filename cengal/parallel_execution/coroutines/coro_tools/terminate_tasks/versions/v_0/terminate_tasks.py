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
    'aterminate_tasks_explicit',
    'aterminate_tasks_implicit',
    'aterminate_tasks',
    'aterminate_tasks_im',
    'terminate_tasks_explicit',
    'terminate_tasks_implicit',
    'terminate_tasks',
    'terminate_tasks_im',
]


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.2.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.parallel_execution.coroutines.coro_scheduler import Interface, current_interface
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import Task
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro_list import PutCoroList, PSCP
from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
from cengal.parallel_execution.coroutines.coro_standard_services.kill_coro_list import KillCoroList, KillSingleCoroParams
from cengal.parallel_execution.coroutines.coro_tools.wait_tasks import GracefulTerminationSettings, \
    atask_graceful_destroyer, await_tasks_explicit

from typing import Optional, List, Callable


async def aterminate_tasks_explicit(
        i: Interface, 
        tasks: List[Task], 
        tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        wait_for_termination: bool = False, 
        ) -> bool:
    if not tasks:
        return False
    
    if graceful_termination_settings is None:
        termination_tasks_params: List[KillSingleCoroParams] = list([KillSingleCoroParams(task.coro_id, tree) for task in tasks if not task.done])
        if not termination_tasks_params:
            return False
        
        i(KillCoroList, termination_tasks)
    else:
        termination_tasks_params: List[PSCP] = [PSCP(atask_graceful_destroyer, task, tree, graceful_termination_settings) for task in tasks if not task.done]
        if not termination_tasks_params:
            return False
        
        termination_tasks: List[Task] = await i(PutCoroList, termination_tasks_params, True)
        if wait_for_termination:
            await await_tasks_explicit(i, termination_tasks, False, None, None, False, False, False, False)
    
    return True


async def aterminate_tasks_implicit(
        tasks: List[Task], 
        tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        wait_for_termination: bool = False, 
        ) -> bool:
    i: Interface = current_interface()
    return await aterminate_tasks_explicit(
        i, 
        tasks, 
        tree, 
        graceful_termination_settings, 
        wait_for_termination, 
        )


aterminate_tasks: Callable = aterminate_tasks_explicit
aterminate_tasks_im: Callable = aterminate_tasks_implicit


def terminate_tasks_explicit(
        i: Interface, 
        tasks: List[Task], 
        tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        wait_for_termination: bool = False, 
        ) -> bool:
    i(RunCoro, aterminate_tasks_explicit,
        tasks, 
        tree, 
        graceful_termination_settings, 
        wait_for_termination, 
        )


def terminate_tasks_implicit(
        tasks: List[Task], 
        tree: bool = False,
        graceful_termination_settings: Optional[GracefulTerminationSettings] = None,
        wait_for_termination: bool = False, 
        ) -> bool:
    i: Interface = current_interface()
    return terminate_tasks_explicit(
        i, 
        tasks, 
        tree, 
        graceful_termination_settings, 
        wait_for_termination, 
        )


terminate_tasks: Callable = terminate_tasks_explicit
terminate_tasks_im: Callable = terminate_tasks_implicit
