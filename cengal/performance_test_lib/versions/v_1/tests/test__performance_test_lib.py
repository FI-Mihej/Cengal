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

from cengal.introspection.inspect import pdi, cen
from cengal.performance_test_lib import *
from cengal.code_inspection.auto_line_tracer import alt
from cengal.code_flow_control.context_management import Conditional, Combine
from unittest import TestCase, skip, main


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


"""
test_precise_auto_while_performance_test_tracer: 4470019.441473938 iter/s; 0.3111310852691531 seconds; 1390762 iterations
.test_precise_performance_test_tracer: 4684909.0 iter/s; 0.4987010061740875 seconds; 2256036 iterations
test_precise_performance_test_tracer: 3008048.0 iter/s; 0.75 seconds; 2256036 iterations
test_precise_performance_test_tracer: 4512072.0 iter/s; 0.5 seconds; 2256036 iterations
.test_precise_while_performance_test_tracer: 4673761.5 iter/s; 0.500423014163971 seconds; 2354938 iterations
test_precise_while_performance_test_tracer: 9419752.0 iter/s; 0.25 seconds; 2354938 iterations
test_precise_while_performance_test_tracer: 4709876.0 iter/s; 0.5 seconds; 2354938 iterations
"""

"""
test_precise_auto_while_performance_test_tracer: 4551373.437799173 iter/s; 0.33796501671895385 seconds; 1538205 iterations
.test_precise_performance_test_tracer: 4649269.0 iter/s; 0.5050010085105896 seconds; 2476444 iterations
test_precise_performance_test_tracer: 9905776.0 iter/s; 0.25 seconds; 2476444 iterations
test_precise_performance_test_tracer: 4952888.0 iter/s; 0.5 seconds; 2476444 iterations
.test_precise_while_performance_test_tracer: 5063401.5 iter/s; 0.49692198634147644 seconds; 2412450 iterations
test_precise_while_performance_test_tracer: 4824900.0 iter/s; 0.5 seconds; 2412450 iterations
test_precise_while_performance_test_tracer: 4824900.0 iter/s; 0.5 seconds; 2412450 iterations
"""

class TestPerformanceTestLib(TestCase):
    # @skip('')
    def test_precise_performance_test_tracer(self):
        pptt = PrecisePerformanceTestTracer(0.5)

        while pptt.iter():
            i = '456'
            k = int('1243' + i)
        print('{}: {} iter/s; {} seconds; {} iterations'.format(cen(), pptt.iter_per_time_unit, pptt.time_spent, pptt.iterations_made))

        with pptt as fast_iter:
            for j in fast_iter:
                i = '456'
                k = int('1243' + i)

        print('{}: {} iter/s; {} seconds; {} iterations'.format(cen(), pptt.iter_per_time_unit, pptt.time_spent, pptt.iterations_made))

        start_time = pptt._clock()
        for i in range(pptt.iterations_made):
            i = '456'
            k = int('1243' + i)
        
        end_time = pptt._clock()
        time_diff = end_time - start_time
        speed = 0
        if time_diff:
            speed = pptt.iterations_made / time_diff
        print('{}: {} iter/s; {} seconds; {} iterations'.format(cen(), speed, time_diff, pptt.iterations_made))
    
    # @skip('')
    def test_precise_while_performance_test_tracer(self):
        pptt = PreciseWhilePerformanceTestTracer(0.5)

        while pptt.iter():
            i = '456'
            k = int('1243' + i)
        print('{}: {} iter/s; {} seconds; {} iterations'.format(cen(), pptt.iter_per_time_unit, pptt.time_spent, pptt.iterations_made))

        with pptt as fast_iter:
            while fast_iter():
                i = '456'
                k = int('1243' + i)

        print('{}: {} iter/s; {} seconds; {} iterations'.format(cen(), pptt.iter_per_time_unit, pptt.time_spent, pptt.iterations_made))

        start_time = pptt._clock()
        for i in range(pptt.iterations_made):
            i = '456'
            k = int('1243' + i)
        
        end_time = pptt._clock()
        time_diff = end_time - start_time
        speed = 0
        if time_diff:
            speed = pptt.iterations_made / time_diff
        print('{}: {} iter/s; {} seconds; {} iterations'.format(cen(), speed, time_diff, pptt.iterations_made))
    
    # @skip('')
    def test_precise_auto_while_performance_test_tracer(self):
        with PreciseAutoWhilePerformanceTestTracer(0.5, turn_off_gc=True) as pt:
            while pt():
                i = '456'
                k = int('1243' + i)

        print('{}: {} iter/s; {} seconds; {} iterations'.format(cen(), pt.iter_per_time_unit, pt.time_spent, pt.iterations_made))
    
    # @skip('')
    def test_measure_performance_trace_line(self):
        with MeasurePerformanceTraceLine(0.5, turn_off_gc=True) as pt:
            while pt():
                i = '456'
                k = int('1243' + i)
    
    # @skip('')
    def test_measure_time_trace_line(self):
        for index in range(2):
            with Combine(alt.different_print_setting(False), Conditional(alt.different_rich_setting(False), bool(index))):  # testing print turning on inside MeasureTimeTraceLine
                with MeasureTimeTraceLine(iterations=2329894) as mt:
                    for _ in range(mt.iterations):
                        i = '456'
                        k = int('1243' + i)
    
    # @skip('')
    def test_measure_time_trace_line_combined(self):
        for index in range(2):
            with Combine(MeasureTimeTraceLine(iterations=2329894, depth=2), alt.different_print_setting(False), Conditional(alt.different_rich_setting(False), bool(index))) as combined:  # testing print turning on inside MeasureTimeTraceLine
                mt: MeasureTime = combined[0]
                for _ in range(mt.iterations):
                    i = '456'
                    k = int('1243' + i)


if __name__ == '__main__':
    main()
