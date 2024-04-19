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
__version__ = "4.3.4"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from multiprocessing import shared_memory
a = shared_memory.ShareableList(['howdy', b'HoWdY', -273.154, 100, None, True, 42])
[ type(entry) for entry in a ]
a[2]
a[2] = -78.5
a[2]
a[2] = 'dry ice'  # Changing data types is supported as well
print(a[2])
pass

from cengal.performance_test_lib import PrecisePerformanceTestTracer
from cengal.introspection.inspect import func_name
from threading import Lock, RLock
from typing import Callable


def func_perf_test(func: Callable, *args, **kwargs):
    tr = PrecisePerformanceTestTracer(1.0)
    while tr.iter():
        func(*args, **kwargs)

    with tr as fast_iter:
        for i in fast_iter:
            func(*args, **kwargs)

    print('{}(): {} iter/s; {} seconds; {} iterations'.format(func_name(func), tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))


def data_change():
    a[2] = 'dry ice'  # Changing data types is supported as well


func_perf_test(data_change)
