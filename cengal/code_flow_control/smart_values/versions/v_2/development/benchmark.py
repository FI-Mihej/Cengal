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
__version__ = "4.3.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.code_flow_control.smart_values.versions.v_2 import ValueExistenceNamedTuple, ValueExistence, ValueCache
from cengal.code_flow_control.gc import DisableGC, EnableGC
from cengal.performance_test_lib import MeasureTime, measure_func_isolated_performance
from cengal.introspection.inspect import cen, func_name
from pprint import pprint
from typing import Any, Dict, Optional, Callable, Set, Type, Tuple, List, FrozenSet, Deque, Generator


'''
>>> "Create: create__tuple": create__tuple()
         It was used 15.271485328674316 seconds to make 8388608 iterations. Performance: 549298.75 iterations/seconds
         Isolated run time: 1.1176416592206806e-07 seconds; Isolated performance: 8947411.647998959 iterations/seconds

>>> "Create: create__named_tuple": create__named_tuple()
         It was used 3.465820074081421 seconds to make 5340024 iterations. Performance: 1540767.75 iterations/seconds
         Isolated run time: 3.332352207507938e-07 seconds; Isolated performance: 3000883.2732235068 iterations/seconds

>>> "Create: create__value_existence": create__value_existence()
         It was used 5.389648914337158 seconds to make 1248545 iterations. Performance: 231656.09375 iterations/seconds
         Isolated run time: 2.481763658579439e-06 seconds; Isolated performance: 402939.2551313286 iterations/seconds

>>> "Create: create__value_cache": create__value_cache()
         It was used 4.496094226837158 seconds to make 1025354 iterations. Performance: 228054.390625 iterations/seconds
         Isolated run time: 2.8617650968953967e-06 seconds; Isolated performance: 349434.6901794477 iterations/seconds
'''


def benchmark():
    gen = None
    gen_type = None
    def create__tuple():
        return (True, 12)
    
    def create__named_tuple():
        return ValueExistenceNamedTuple(True, 12)
    
    def create__value_existence():
        return ValueExistence[int](True, 12)
    
    def create__value_cache():
        return ValueCache[int]()
    
    
    with DisableGC():
    # with EnableGC():
        functions = (
            create__tuple,
            create__named_tuple,
            create__value_existence,
            create__value_cache,
        )
        for fun in functions:
            measure_func_isolated_performance(fun, 5.1, f'Create: {func_name(fun)}', do_print=True)
            print()


def main():
    benchmark()


if __name__ == '__main__':
    main()
