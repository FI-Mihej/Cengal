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
__version__ = "3.1.16"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.performance_test_lib import PrecisePerformanceTestTracer
from copy import copy


test_time = 1.0


data = {
    type(''): 'ase;orijuh oasewrhjifaserhfc as',
    type(2): 2222222,
    type((12, 23)): ('ase;orijuh oasewrhjifaserhfc as', 34),
    type([12, 23]): ['ase;orijuh oasewrhjifaserhfc as', 34],
    type({12, 23}): {'ase;orijuh oasewrhjifaserhfc as', 34},
}
data_set = set(data)


tr = PrecisePerformanceTestTracer(test_time)
while tr.iter():
    dt = type(data_set)()

with tr as fast_iter:
    for i in fast_iter:
        dt = type(data_set)()

print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))


tr = PrecisePerformanceTestTracer(test_time)
while tr.iter():
    dt = set()

with tr as fast_iter:
    for i in fast_iter:
        dt = set()

print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))
