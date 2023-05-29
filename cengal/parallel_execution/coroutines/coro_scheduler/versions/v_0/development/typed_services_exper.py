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
__version__ = "3.2.5"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.fast_aggregator import FastAggregator, FastAggregatorWaitFor, FastAggregatorPutSingle, FastAggregatorRequest, FastAggregatorPutMultiple
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro

def my_coro(i: Interface) -> None:
    result1 = i(Sleep, 1.0)
    result2 = i(FastAggregator, 1)
    result3 = i(FastAggregatorWaitFor, 1)
    result4 = i(FastAggregatorWaitFor()(1))
    result5 = i(FastAggregatorPutSingle, 1, 1)
    result6 = i(FastAggregatorPutSingle())
    result7 = i(FastAggregatorPutSingle()(1, 1))
    result8 = i(FastAggregatorRequest().put_single(1, 1))
    result9 = i(FastAggregatorPutMultiple()({1: [1]}))
    result10 = i(FastAggregatorRequest().put_multiple({1: [1]}))
    result11 = i(FastAggregatorRequest().wait(1))
    result12 = i(PutCoro, my_coro)
    