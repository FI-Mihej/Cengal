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


__all__ = ['adump', 'adumps', 'aload', 'aloads']

from cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler import CoroScheduler, Interface
from .json import *
from cengal.parallel_execution.coroutines.coro_tools.await_coro import await_coro


async def adump(cs: CoroScheduler, *args, **kwargs):
    # You may use
    # ly = None, priority: CoroPriority = CoroPriority.normal
    # as an additional parameters in order to configure LowLatencyJSONEncoder
    
    def coro(i: Interface):
        kwargs['cls'] = LowLatencyJSONEncoder
        return original_json_dump(*args, **kwargs)
    
    return await await_coro(cs, coro)


async def adumps(cs: CoroScheduler, *args, **kwargs):
    # You may use
    # ly = None, priority: CoroPriority = CoroPriority.normal
    # as an additional parameters in order to configure LowLatencyJSONEncoder
    
    def coro(i: Interface):
        kwargs['cls'] = LowLatencyJSONEncoder
        return original_json_dumps(*args, **kwargs)
    
    return await await_coro(cs, coro)


async def aload(cs: CoroScheduler, *args, **kwargs):
    # You may use
    # ly = None, priority: CoroPriority = CoroPriority.normal
    # as an additional parameters in order to configure LowLatencyJSONEncoder
    
    def coro(i: Interface):
        kwargs['cls'] = LowLatencyJSONDecoder
        kwargs['object_pairs_hook'] = LowLatencyObjectPairsHook(**kwargs)
        return original_json_load(*args, **kwargs)
    
    return await await_coro(cs, coro)


async def aloads(cs: CoroScheduler, *args, **kwargs):
    # You may use
    # ly = None, priority: CoroPriority = CoroPriority.normal
    # as an additional parameters in order to configure LowLatencyJSONEncoder
    
    def coro(i: Interface):
        kwargs['cls'] = LowLatencyJSONDecoder
        kwargs['object_pairs_hook'] = LowLatencyObjectPairsHook(**kwargs)
        return original_json_loads(*args, **kwargs)
    
    return await await_coro(cs, coro)
