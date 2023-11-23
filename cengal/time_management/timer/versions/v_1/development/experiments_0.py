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


from cengal.performance_test_lib import PrecisePerformanceTestTracer
from cengal.time_management.timer.versions.v_1 import Timer, TimerRequest, TimerHandler
from copy import copy


"""Performance test results:

mb@DESKTOP-E49H4V3:~/dev/workspace/my/Cengal$ /usr/bin/python3 /home/mb/dev/workspace/my/Cengal/cengal/time_management/timer/versions/v_1/development/experiments_0.py
778738.0479635013 iter/s; 0.7898240000067744 seconds; 615066 iterations
834289.3588508256 iter/s; 0.762619100016309 seconds; 636245 iterations
784407.3593367807 iter/s; 0.7968041000131052 seconds; 625019 iterations
802340.248604422 iter/s; 0.7631325999973342 seconds; 612292 iterations
========== Register tests:
173651.73192200443 iter/s; 0.8944512000016402 seconds; 155323 iterations
24130.718404025185 iter/s; 0.9778821999789216 seconds; 23597 iterations
2674.5021968600595 iter/s; 0.9369967999809887 seconds; 2506 iterations
249.82152901632722 iter/s; 0.9246600999904331 seconds; 231 iterations
"""


test_time = 1.0


data = {
    type(''): 'ase;orijuh oasewrhjifaserhfc as',
    type(2): 2222222,
    type((12, 23)): ('ase;orijuh oasewrhjifaserhfc as', 34),
    type([12, 23]): ['ase;orijuh oasewrhjifaserhfc as', 34],
    type({12, 23}): {'ase;orijuh oasewrhjifaserhfc as', 34},
}

def handler():
    pass


timer = Timer()
for i in range(1):
    timer.register(handler, 10)

tr = PrecisePerformanceTestTracer(test_time)
while tr.iter():
    timer()

with tr as fast_iter:
    for i in fast_iter:
        timer()

print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))


timer = Timer()
for i in range(10):
    timer.register(handler, 10)

tr = PrecisePerformanceTestTracer(test_time)
while tr.iter():
    timer()

with tr as fast_iter:
    for i in fast_iter:
        timer()

print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))


timer = Timer()
for i in range(100):
    timer.register(handler, 10)

tr = PrecisePerformanceTestTracer(test_time)
while tr.iter():
    timer()

with tr as fast_iter:
    for i in fast_iter:
        timer()

print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))


timer = Timer()
for i in range(1000):
    timer.register(handler, 10)

tr = PrecisePerformanceTestTracer(test_time)
while tr.iter():
    timer()

with tr as fast_iter:
    for i in fast_iter:
        timer()

print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))


print(f'{"="*10} Register tests:')


events_num = 1
tr = PrecisePerformanceTestTracer(test_time)
while tr.iter():
    timer = Timer()
    for i in range(events_num):
        timer.register(handler, 10)

with tr as fast_iter:
    for i in fast_iter:
        timer = Timer()
        for i in range(events_num):
            timer.register(handler, 10)

print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))


events_num = 10
tr = PrecisePerformanceTestTracer(test_time)
while tr.iter():
    timer = Timer()
    for i in range(events_num):
        timer.register(handler, 10)

with tr as fast_iter:
    for i in fast_iter:
        timer = Timer()
        for i in range(events_num):
            timer.register(handler, 10)

print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))


events_num = 100
tr = PrecisePerformanceTestTracer(test_time)
while tr.iter():
    timer = Timer()
    for i in range(events_num):
        timer.register(handler, 10)

with tr as fast_iter:
    for i in fast_iter:
        timer = Timer()
        for i in range(events_num):
            timer.register(handler, 10)

print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))


events_num = 1000
tr = PrecisePerformanceTestTracer(test_time)
while tr.iter():
    timer = Timer()
    for i in range(events_num):
        timer.register(handler, 10)

with tr as fast_iter:
    for i in fast_iter:
        timer = Timer()
        for i in range(events_num):
            timer.register(handler, 10)

print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))
