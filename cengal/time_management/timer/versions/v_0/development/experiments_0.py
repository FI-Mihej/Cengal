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
__version__ = "4.1.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.performance_test_lib import PrecisePerformanceTestTracer
from cengal.time_management.timer.versions.v_0 import Timer, TimerRequest, TimerHandler
from copy import copy


"""Performance test results:

mb@DESKTOP-E49H4V3:~/dev/workspace/my/Cengal$ /usr/bin/python3 /home/mb/dev/workspace/my/Cengal/cengal/time_management/timer/versions/v_0/development/experiments_0.py
484817.15475231654 iter/s; 0.9436175999871921 seconds; 457482 iterations
83451.5671891873 iter/s; 0.9488258000055794 seconds; 79181 iterations
8765.458361003815 iter/s; 0.9279606000054628 seconds; 8134 iterations
692.0368238774348 iter/s; 1.222478300012881 seconds; 846 iterations
========== Register tests:
323888.113396884 iter/s; 0.6867988999874797 seconds; 222446 iterations
44594.56445845191 iter/s; 0.8744115000008605 seconds; 38994 iterations
4694.408896671078 iter/s; 0.8514384000154678 seconds; 3997 iterations
498.69372894815746 iter/s; 0.8482160000130534 seconds; 423 iterations
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
