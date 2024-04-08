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
__version__ = "4.3.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.time_management.cpu_clock_cycles import cpu_clock_cycles, set_cycles_per_second, cpu_clock
from cengal.time_management.cpu_clock import cpu_clock as py_cpu_clock, CPU_TICKS_PER_SECOND
from cengal.time_management.cpu_clock_cycles import perf_counter
from cengal.time_management.timer_precision import timer_precision_99_95_68
from rdtsc import get_cycles
from hwcounter import Timer, count, count_end


'''
CPU_TICKS_PER_SECOND=3400000000

=== cpu_clock_cycles ===
1186878839609124 1186878839610499 1186878839615332
99%: 8212.103415338614, 95%: 5585.238492802462, 68%: 2958.3735702663116, max: 2361434.49135227, min: -76.50864773016127
99%: 2.4153245339231214e-06, 95%: 1.64271720376543e-06, 68%: 8.701098736077387e-07, max: 0.0006945395562800794, min: -2.2502543450047434e-08
====================

=== cpu_clock ===
349084.1567586538 349084.1567596156 349084.1567600485
99%: 1.2908953866088769e-05, 95%: 8.63804277239931e-06, 68%: 4.367131678709853e-06, max: 0.006016337600474743, min: -2.6254976602406376e-08
====================

=== py_cpu_clock ===
349086.43543525675 349086.4354360312 349086.4354364738
99%: 2.3624063931893485e-06, 95%: 1.6042666935329496e-06, 68%: 8.461269938765508e-07, max: 0.0004945910995474227, min: -1.9767915629568215e-08
====================

=== get_cycles ===
1186901550218546 1186901550232500 1186901550234815
99%: 27309.252760208357, 95%: 18580.55647901168, 68%: 9851.860197815005, max: 5624223.836083381, min: -162.1639166183279
99%: 8.032133164767164e-06, 95%: 5.464869552650495e-06, 68%: 2.897605940533825e-06, max: 0.0016541834812009945, min: -4.7695269593625857e-08
====================

=== hwcounter count ===
1186906231227317 1186906231234664 1186906231238856
99%: 39700.589469141836, 95%: 27239.384564697615, 68%: 14778.179660253401, max: 7269040.02524419, min: -249.97475580918808
99%: 1.1676643961512305e-05, 95%: 8.011583695499298e-06, 68%: 4.346523429486294e-06, max: 0.0021379529486012325, min: -7.352198700270237e-08
====================

=== hwcounter count_end ===
1186910351218384 1186910351230247 1186910351234574
99%: 18754.107945107724, 95%: 13276.481677477506, 68%: 7798.855409847286, max: 1771500.770857783, min: -230.2291422170656
99%: 5.515914101502272e-06, 95%: 3.904847552199266e-06, 68%: 2.2937810028962607e-06, max: 0.0005210296384875832, min: -6.771445359325459e-08
====================

=== perf_counter ===
348750.768464202 348750.768465602 348750.768466002
99%: 3.090979216930911e-06, 95%: 2.0961266001807853e-06, 68%: 1.1012739834306596e-06, max: 0.0009239995674487463, min: -6.478812892110169e-09
============================================================

============================================================
cpu_clock_cycles(): 18708634.0 iter/s; 0.59375 seconds; 11108252 iterations
cpu_clock(): 21019172.0 iter/s; 0.5625 seconds; 11823284 iterations
py_cpu_clock(): 19782964.0 iter/s; 0.59375 seconds; 11746135 iterations
get_cycles(): 3644693.25 iter/s; 0.84375 seconds; 3075210 iterations
count(): 1523767.75 iter/s; 0.96875 seconds; 1476150 iterations
count_end(): 1567566.875 iter/s; 0.9375 seconds; 1469594 iterations
perf_counter(): 16126142.0 iter/s; 0.625 seconds; 10078839 iterations
'''


print(f'{CPU_TICKS_PER_SECOND=}')
set_cycles_per_second(CPU_TICKS_PER_SECOND)
print()
print('=== cpu_clock_cycles ===')

a = cpu_clock_cycles()
b = cpu_clock_cycles()
c = cpu_clock_cycles()
print(a, b, c)
val_99, val_95, val_68, max_deviation, min_deviation = timer_precision_99_95_68(cpu_clock_cycles)
print(f'99%: {val_99}, 95%: {val_95}, 68%: {val_68}, max: {max_deviation}, min: {min_deviation}')
val_99 = val_99 / CPU_TICKS_PER_SECOND
val_95 = val_95 / CPU_TICKS_PER_SECOND
val_68 = val_68 / CPU_TICKS_PER_SECOND
max_deviation = max_deviation / CPU_TICKS_PER_SECOND
min_deviation = min_deviation / CPU_TICKS_PER_SECOND
print(f'99%: {val_99}, 95%: {val_95}, 68%: {val_68}, max: {max_deviation}, min: {min_deviation}')


print('====================')
print()
print('=== cpu_clock ===')

a = cpu_clock()
b = cpu_clock()
c = cpu_clock()
print(a, b, c)
val_99, val_95, val_68, max_deviation, min_deviation = timer_precision_99_95_68(cpu_clock)
print(f'99%: {val_99}, 95%: {val_95}, 68%: {val_68}, max: {max_deviation}, min: {min_deviation}')


print('====================')
print()
print('=== py_cpu_clock ===')

a = py_cpu_clock()
b = py_cpu_clock()
c = py_cpu_clock()
print(a, b, c)
val_99, val_95, val_68, max_deviation, min_deviation = timer_precision_99_95_68(py_cpu_clock)
print(f'99%: {val_99}, 95%: {val_95}, 68%: {val_68}, max: {max_deviation}, min: {min_deviation}')


print('====================')
print()
print('=== get_cycles ===')


a = get_cycles()
b = get_cycles()
c = get_cycles()
print(a, b, c)
val_99, val_95, val_68, max_deviation, min_deviation = timer_precision_99_95_68(get_cycles)
print(f'99%: {val_99}, 95%: {val_95}, 68%: {val_68}, max: {max_deviation}, min: {min_deviation}')
val_99 = val_99 / CPU_TICKS_PER_SECOND
val_95 = val_95 / CPU_TICKS_PER_SECOND
val_68 = val_68 / CPU_TICKS_PER_SECOND
max_deviation = max_deviation / CPU_TICKS_PER_SECOND
min_deviation = min_deviation / CPU_TICKS_PER_SECOND
print(f'99%: {val_99}, 95%: {val_95}, 68%: {val_68}, max: {max_deviation}, min: {min_deviation}')


print('====================')
print()
print('=== hwcounter count ===')


a = count()
b = count()
c = count()
print(a, b, c)
val_99, val_95, val_68, max_deviation, min_deviation = timer_precision_99_95_68(count)
print(f'99%: {val_99}, 95%: {val_95}, 68%: {val_68}, max: {max_deviation}, min: {min_deviation}')
val_99 = val_99 / CPU_TICKS_PER_SECOND
val_95 = val_95 / CPU_TICKS_PER_SECOND
val_68 = val_68 / CPU_TICKS_PER_SECOND
max_deviation = max_deviation / CPU_TICKS_PER_SECOND
min_deviation = min_deviation / CPU_TICKS_PER_SECOND
print(f'99%: {val_99}, 95%: {val_95}, 68%: {val_68}, max: {max_deviation}, min: {min_deviation}')


print('====================')
print()
print('=== hwcounter count_end ===')


a = count_end()
b = count_end()
c = count_end()
print(a, b, c)
val_99, val_95, val_68, max_deviation, min_deviation = timer_precision_99_95_68(count_end)
print(f'99%: {val_99}, 95%: {val_95}, 68%: {val_68}, max: {max_deviation}, min: {min_deviation}')
val_99 = val_99 / CPU_TICKS_PER_SECOND
val_95 = val_95 / CPU_TICKS_PER_SECOND
val_68 = val_68 / CPU_TICKS_PER_SECOND
max_deviation = max_deviation / CPU_TICKS_PER_SECOND
min_deviation = min_deviation / CPU_TICKS_PER_SECOND
print(f'99%: {val_99}, 95%: {val_95}, 68%: {val_68}, max: {max_deviation}, min: {min_deviation}')


print('====================')
print()
print('=== perf_counter ===')


a = perf_counter()
b = perf_counter()
c = perf_counter()
print(a, b, c)
val_99, val_95, val_68, max_deviation, min_deviation = timer_precision_99_95_68(perf_counter)
print(f'99%: {val_99}, 95%: {val_95}, 68%: {val_68}, max: {max_deviation}, min: {min_deviation}')

print('============================================================')
print()
print('============================================================')


from cengal.performance_test_lib import PrecisePerformanceTestTracer
from cengal.introspection.inspect import func_name, entity_properties
from typing import Callable, Set, Optional, Dict, Type


def func_perf_test(func: Callable):
    tr = PrecisePerformanceTestTracer(1.0)
    while tr.iter():
        func()

    with tr as fast_iter:
        for i in fast_iter:
            func()

    print('{}(): {} iter/s; {} seconds; {} iterations'.format(func_name(func), tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))

func_perf_test(cpu_clock_cycles)
func_perf_test(cpu_clock)
func_perf_test(py_cpu_clock)
func_perf_test(get_cycles)
func_perf_test(count)
func_perf_test(count_end)
func_perf_test(perf_counter)
