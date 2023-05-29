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


"""
from cengal.introspection.inspect import get_exception, exception_to_printable_text

try:
    for j in range(100):
        await asyncio.sleep(0.1)
        fac(aggregator_append_key, j)
        fac(aggregator_key, j)
    
    return True
except GracefulCoroDestroy:
    print('GracefulCoroDestroy')
    return False
except:
    print(exception_to_printable_text(get_exception()))
"""


"""
from time import perf_counter

fac(aggregator_append_key, perf_counter())
"""


"""
for j in range(100):
    await asyncio.sleep(0.1)
    fac(aggregator_append_key, j)
    fac(aggregator_key, j)

return True
"""


"""
async def coro(i: Interface):
    for j in range(1000):
        await asyncio.sleep(0.1)
        fac(aggregator_append_key, j)
        fac(aggregator_key, j)

coro_id = await i(PutCoro, coro)
return coro_id
"""


"""
await i(KillCoro, )
"""


""" Filter:
['CoroSchedulerGreenlet', 'loop', 'coroutines']
"""