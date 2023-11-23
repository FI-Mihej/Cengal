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

from time import clock

perf_counter = process_time = clock

try:
    from time import perf_counter as _perf_counter
    perf_counter = _perf_counter
except ImportError:
    pass

try:
    from time import process_time as _process_time
    process_time = _process_time
except ImportError:
    pass

from cengal.time_management.repeat_for_a_time.versions.v_0.repeat_for_a_time__python import \
    Tracer as TracerNative, TracerCounter as TracerCounterNative, TracerIterator as TracerIteratorNative, \
    ClockType as ClockTypeNative

repeat_for_a_time_cython_module_was_loaded = True
try:
    from cengal.time_management.repeat_for_a_time.versions import \
        Tracer as TracerCompiled, TracerCounter as TracerCounterCompiled, TracerIterator as TracerIteratorCompiled, \
        ClockType as ClockTypeCompiled
except ImportError:
    repeat_for_a_time_cython_module_was_loaded = False

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

__doc__ = '''
Native .iter(): 1314866.836082816 iter/s; 1.0101098936807824 seconds. Internal: 1267625.7394312301 iter/s; 1.0100524425506592 seconds; 1328160 iters
Native Counter: 1374039.594745121 iter/s; 0.9225542006561607 seconds. Internal: 1373622.4018055892 iter/s; 0.9228343963623047 seconds; 1267626 iters
Native Counter Iterator: 833126.4583887773 iter/s; 1.5215289194530226 seconds. Internal: 833211.1709637797 iter/s; 1.521374225616455 seconds; 1267626 iters
PASS - Native .iter(): 2679790.563039528 iter/s; 0.9975746003702035 seconds. Internal: 2704377.710817054 iter/s; 0.9975225925445557 seconds; 2673291 iters
PASS - Native Counter: 2573459.392848136 iter/s; 1.050872614316627 seconds. Internal: 2573991.52006913 iter/s; 1.0506553649902344 seconds; 2704378 iters
PASS - Native Counter Iterator: 1358141.8445628048 iter/s; 1.991233839695557 seconds. Internal: 1357936.3387444955 iter/s; 1.9915351867675781 seconds; 2704378 iters

Compiled .iter(): 2662605.4954643254 iter/s; 0.9982654225448746 seconds. Internal: 2670643.0 iter/s; 0.9990000128746033 seconds; 2657987 iters
Compiled Counter: 2552670.609531415 iter/s; 1.0462152813716301 seconds. Internal: 2553196.0 iter/s; 1.0460000038146973 seconds; 2670643 iters
Compiled Counter Iterator: 2412906.0912160017 iter/s; 1.1068159717123969 seconds. Internal: 2412505.0 iter/s; 1.1069999933242798 seconds; 2670643 iters
PASS - Compiled .iter(): 10369459.449145418 iter/s; 1.0086939489273004 seconds. Internal: 10004845.0 iter/s; 1.0089999437332153 seconds; 10459611 iters
PASS - Compiled Counter: 10717891.79297866 iter/s; 0.9334713573572575 seconds. Internal: 10723306.0 iter/s; 0.9330000281333923 seconds; 10004845 iters
PASS - Compiled Counter Iterator: 8438850.11835808 iter/s; 1.1855696996247413 seconds. Internal: 8435788.0 iter/s; 1.1859999895095825 seconds; 10004845 iters

for i in range(): 3257425.63035198 iter/s
PASS - for i in range(): 27120025.0597179 iter/s

while iter_qnt > 0: 2441599.852625212 iter/s
PASS - while iter_qnt > 0: 9778029.90225164 iter/s

while True: 2592510.421169292 iter/s
PASS - while True: 9770496.61187559 iter/s
'''

test_time = 1.0

# =============================================================
clock_type_for_native = ClockTypeNative.perf_counter
clock_type_for_native_tracer = clock_type_for_native
clock_type_for_native_tracer_counter = ClockTypeNative.fake

tr = TracerNative(test_time, clock_type_for_native_tracer)
start_time = perf_counter()
while tr.iter():
    k = int('1243')
end_time = perf_counter()
time_spent = end_time - start_time
iter_per_second = tr.iterations_made / time_spent
print('Native .iter(): {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(iter_per_second, time_spent, tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))

trc = TracerCounterNative(tr.iter_per_time_unit, test_time, clock_type_for_native_tracer_counter)
start_time = perf_counter()
while trc.iter():
    k = int('1243')
end_time = perf_counter()
time_spent = end_time - start_time
iter_per_second = trc.iterations_made / time_spent
print('Native Counter: {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(iter_per_second, time_spent, trc.iter_per_time_unit, trc.time_spent, trc.iterations_made))

trc = TracerCounterNative(tr.iter_per_time_unit, test_time, clock_type_for_native_tracer_counter)
start_time = perf_counter()
for i in TracerIteratorNative(trc):
    k = int('1243')
end_time = perf_counter()
time_spent = end_time - start_time
iter_per_second = trc.iterations_made / time_spent
print('Native Counter Iterator: {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(iter_per_second, time_spent, trc.iter_per_time_unit, trc.time_spent, trc.iterations_made))

tr = TracerNative(test_time, clock_type_for_native_tracer)
start_time = perf_counter()
while tr.iter():
    pass
end_time = perf_counter()
time_spent = end_time - start_time
iter_per_second = tr.iterations_made / time_spent
print('PASS - Native .iter(): {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(iter_per_second, time_spent, tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))

trc = TracerCounterNative(tr.iter_per_time_unit, test_time, clock_type_for_native_tracer_counter)
start_time = perf_counter()
while trc.iter():
    pass
end_time = perf_counter()
time_spent = end_time - start_time
iter_per_second = trc.iterations_made / time_spent
print('PASS - Native Counter: {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(iter_per_second, time_spent, trc.iter_per_time_unit, trc.time_spent, trc.iterations_made))

trc = TracerCounterNative(tr.iter_per_time_unit, test_time, clock_type_for_native_tracer_counter)
start_time = perf_counter()
for i in TracerIteratorNative(trc):
    pass
end_time = perf_counter()
time_spent = end_time - start_time
iter_per_second = trc.iterations_made / time_spent
print('PASS - Native Counter Iterator: {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(iter_per_second, time_spent, trc.iter_per_time_unit, trc.time_spent, trc.iterations_made))

print()

# =============================================================

if repeat_for_a_time_cython_module_was_loaded:
    clock_type_for_compiled = ClockTypeCompiled.perf_counter
    clock_type_for_compiled_tracer = clock_type_for_compiled
    clock_type_for_compiled_tracer_counter = ClockTypeCompiled.fake

    tr = TracerCompiled(test_time, clock_type_for_compiled_tracer)
    start_time = perf_counter()
    while tr.iter():
        k = int('1243')
    end_time = perf_counter()
    time_spent = end_time - start_time
    iter_per_second = tr.iterations_made / time_spent
    print('Compiled .iter(): {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(iter_per_second, time_spent, tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))

    trc = TracerCounterCompiled(tr.iter_per_time_unit, test_time, clock_type_for_compiled_tracer_counter)
    start_time = perf_counter()
    while trc.iter():
        k = int('1243')
    end_time = perf_counter()
    time_spent = end_time - start_time
    iter_per_second = trc.iterations_made / time_spent
    print('Compiled Counter: {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(iter_per_second, time_spent, trc.iter_per_time_unit, trc.time_spent, trc.iterations_made))

    trc = TracerCounterCompiled(tr.iter_per_time_unit, test_time, clock_type_for_compiled_tracer_counter)
    start_time = perf_counter()
    for i in TracerIteratorCompiled(trc):
        k = int('1243')
    end_time = perf_counter()
    time_spent = end_time - start_time
    iter_per_second = trc.iterations_made / time_spent
    print('Compiled Counter Iterator: {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(iter_per_second, time_spent, trc.iter_per_time_unit, trc.time_spent, trc.iterations_made))

    tr = TracerCompiled(test_time, clock_type_for_compiled_tracer)
    start_time = perf_counter()
    while tr.iter():
        pass
    end_time = perf_counter()
    time_spent = end_time - start_time
    iter_per_second = tr.iterations_made / time_spent
    print('PASS - Compiled .iter(): {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(iter_per_second, time_spent, tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))

    trc = TracerCounterCompiled(tr.iter_per_time_unit, test_time, clock_type_for_compiled_tracer_counter)
    start_time = perf_counter()
    while trc.iter():
        pass
    end_time = perf_counter()
    time_spent = end_time - start_time
    iter_per_second = trc.iterations_made / time_spent
    print('PASS - Compiled Counter: {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(iter_per_second, time_spent, trc.iter_per_time_unit, trc.time_spent, trc.iterations_made))

    trc = TracerCounterCompiled(tr.iter_per_time_unit, test_time, clock_type_for_compiled_tracer_counter)
    start_time = perf_counter()
    for i in TracerIteratorCompiled(trc):
        pass
    end_time = perf_counter()
    time_spent = end_time - start_time
    iter_per_second = trc.iterations_made / time_spent
    print('PASS - Compiled Counter Iterator: {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(iter_per_second, time_spent, trc.iter_per_time_unit, trc.time_spent, trc.iterations_made))

    print()
else:
    clock_type_for_native = ClockTypeNative.perf_counter
    clock_type_for_native_tracer = clock_type_for_native
    clock_type_for_native_tracer_counter = ClockTypeNative.fake

    tr = TracerNative(test_time, clock_type_for_native_tracer)
    start_time = perf_counter()
    while tr.iter():
        k = int('1243')
    end_time = perf_counter()
    time_spent = end_time - start_time
    iter_per_second = tr.iterations_made / time_spent
    print('Native .iter(): {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(iter_per_second,
                                                                                                    time_spent,
                                                                                                    tr.iter_per_time_unit,
                                                                                                    tr.time_spent,
                                                                                                    tr.iterations_made))

    trc = TracerCounterNative(tr.iter_per_time_unit, test_time, clock_type_for_native_tracer_counter)
    start_time = perf_counter()
    while trc.iter():
        k = int('1243')
    end_time = perf_counter()
    time_spent = end_time - start_time
    iter_per_second = trc.iterations_made / time_spent
    print('Native Counter: {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(iter_per_second,
                                                                                                    time_spent,
                                                                                                    trc.iter_per_time_unit,
                                                                                                    trc.time_spent,
                                                                                                    trc.iterations_made))

    trc = TracerCounterNative(tr.iter_per_time_unit, test_time, clock_type_for_native_tracer_counter)
    start_time = perf_counter()
    for i in TracerIteratorNative(trc):
        k = int('1243')
    end_time = perf_counter()
    time_spent = end_time - start_time
    iter_per_second = trc.iterations_made / time_spent
    print('Native Counter Iterator: {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(
        iter_per_second, time_spent, trc.iter_per_time_unit, trc.time_spent, trc.iterations_made))

    tr = TracerNative(test_time, clock_type_for_native_tracer)
    start_time = perf_counter()
    while tr.iter():
        pass
    end_time = perf_counter()
    time_spent = end_time - start_time
    iter_per_second = tr.iterations_made / time_spent
    print('PASS - Native .iter(): {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(
        iter_per_second, time_spent, tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))

    trc = TracerCounterNative(tr.iter_per_time_unit, test_time, clock_type_for_native_tracer_counter)
    start_time = perf_counter()
    while trc.iter():
        pass
    end_time = perf_counter()
    time_spent = end_time - start_time
    iter_per_second = trc.iterations_made / time_spent
    print('PASS - Native Counter: {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(
        iter_per_second, time_spent, trc.iter_per_time_unit, trc.time_spent, trc.iterations_made))

    trc = TracerCounterNative(tr.iter_per_time_unit, test_time, clock_type_for_native_tracer_counter)
    start_time = perf_counter()
    for i in TracerIteratorNative(trc):
        pass
    end_time = perf_counter()
    time_spent = end_time - start_time
    iter_per_second = trc.iterations_made / time_spent
    print('PASS - Native Counter Iterator: {} iter/s; {} seconds. Internal: {} iter/s; {} seconds; {} iters'.format(
        iter_per_second, time_spent, trc.iter_per_time_unit, trc.time_spent, trc.iterations_made))

    print()

# =============================================================

start_time = perf_counter()
iter_qnt = round(tr.iter_per_time_unit)
for i in range(iter_qnt):
    k = int('1243')
end_time = perf_counter()
time_spent = end_time - start_time
iter_per_second = iter_qnt / time_spent
print('for i in range(): {} iter/s'.format(iter_per_second))

start_time = perf_counter()
iter_qnt = round(tr.iter_per_time_unit)
for i in range(iter_qnt):
    pass
end_time = perf_counter()
time_spent = end_time - start_time
iter_per_second = iter_qnt / time_spent
print('PASS - for i in range(): {} iter/s'.format(iter_per_second))

print()

# =============================================================

start_time = perf_counter()
iter_qnt = round(tr.iter_per_time_unit)
iter_qnt_buff = iter_qnt
while iter_qnt > 0:
    k = int('1243')
    iter_qnt -= 1
end_time = perf_counter()
time_spent = end_time - start_time
iter_per_second = iter_qnt_buff / time_spent
print('while iter_qnt > 0: {} iter/s'.format(iter_per_second))

start_time = perf_counter()
iter_qnt = round(tr.iter_per_time_unit)
iter_qnt_buff = iter_qnt
while iter_qnt > 0:
    pass
    iter_qnt -= 1
end_time = perf_counter()
time_spent = end_time - start_time
iter_per_second = iter_qnt_buff / time_spent
print('PASS - while iter_qnt > 0: {} iter/s'.format(iter_per_second))

print()

# =============================================================

start_time = perf_counter()
iter_qnt = round(tr.iter_per_time_unit)
iter_qnt_buff = iter_qnt
while True:
    k = int('1243')
    iter_qnt -= 1
    if iter_qnt <= 0:
        break
end_time = perf_counter()
time_spent = end_time - start_time
iter_per_second = iter_qnt_buff / time_spent
print('while True: {} iter/s'.format(iter_per_second))

start_time = perf_counter()
iter_qnt = round(tr.iter_per_time_unit)
iter_qnt_buff = iter_qnt
while True:
    pass
    iter_qnt -= 1
    if iter_qnt <= 0:
        break
end_time = perf_counter()
time_spent = end_time - start_time
iter_per_second = iter_qnt_buff / time_spent
print('PASS - while True: {} iter/s'.format(iter_per_second))

print()

# =============================================================
