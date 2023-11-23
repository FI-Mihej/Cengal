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

from cengal.performance_test_lib import PrecisePerformanceTestTracer
from cengal.help_tools import json_to_printable_string, make_readable_json
import json
from cengal.data_manipulation.serialization import test_data_factory, TestDataType
from cengal.data_manipulation.objects_counter import objects_counter, objects_counter_recursive, object_counter_uni
from cengal.introspection.inspect import intro_func_repr
from pprint import pprint


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


def test_objects_counter():
    print(f'\n<<< {intro_func_repr()} >>>')
    data = {
            1: 'Hello',
            2: ('W', 0),
            3: [
                'r',
                1,
                {
                    'd': '.',
                    'dd': {
                        43: [0],
                        15: {
                            'world': 42
                        }
                    }
                }
            ],
            'To all!': '!!1'
        }
    print(make_readable_json(json.dumps(data)))
    
    num_of_objects = objects_counter(data)
    print('<<objects_counter>>: Number of objects in container: {}'.format(num_of_objects))
    assert(16 == num_of_objects)

    num_of_objects = objects_counter_recursive(data)
    print('<<objects_counter_recursive>>: Number of objects in container: {}'.format(num_of_objects))
    assert(16 == num_of_objects)

    num_of_objects = object_counter_uni(data)
    print('<<object_counter_uni>>: Number of objects in container: {}'.format(num_of_objects))
    assert(16 == num_of_objects)


def test_objects_counter_performance():
    print(f'\n<<< {intro_func_repr()} >>>')
    counter = objects_counter

    print()
    data = test_data_factory(TestDataType.small)
    # pprint(data)
    print('Small: {}'.format(counter(data)))
    tr = PrecisePerformanceTestTracer(1.0, turn_off_gc=True)
    while tr.iter():
        counter(data)
    with tr as fast_iter:
        for i in fast_iter:
            counter(data)
    print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))

    print()
    data = test_data_factory(TestDataType.deep_small)
    print('Small, Deep: {}'.format(counter(data)))
    tr = PrecisePerformanceTestTracer(1.0, turn_off_gc=True)
    while tr.iter():
        counter(data)
    with tr as fast_iter:
        for i in fast_iter:
            counter(data)
    print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))

    print()
    data = test_data_factory(TestDataType.large)
    # pprint(data)
    print('Large: {}'.format(counter(data)))
    tr = PrecisePerformanceTestTracer(1.0, turn_off_gc=True)
    while tr.iter():
        counter(data)
    with tr as fast_iter:
        for i in fast_iter:
            counter(data)
    print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))

    print()
    data = test_data_factory(TestDataType.deep_large)
    print('Large, Deep: {}'.format(counter(data)))
    tr = PrecisePerformanceTestTracer(1.0, turn_off_gc=True)
    while tr.iter():
        counter(data)
    with tr as fast_iter:
        for i in fast_iter:
            counter(data)
    print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))


def test_objects_counter_recursive_performance():
    print(f'\n<<< {intro_func_repr()} >>>')
    counter = objects_counter_recursive

    print()
    data = test_data_factory(TestDataType.small)
    # pprint(data)
    print('Small: {}'.format(counter(data)))
    tr = PrecisePerformanceTestTracer(1.0, turn_off_gc=True)
    while tr.iter():
        counter(data)
    with tr as fast_iter:
        for i in fast_iter:
            counter(data)
    print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))

    print()
    data = test_data_factory(TestDataType.deep_small)
    print('Small, Deep: {}'.format(counter(data)))
    tr = PrecisePerformanceTestTracer(1.0, turn_off_gc=True)
    while tr.iter():
        counter(data)
    with tr as fast_iter:
        for i in fast_iter:
            counter(data)
    print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))

    print()
    data = test_data_factory(TestDataType.large)
    # pprint(data)
    print('Large: {}'.format(counter(data)))
    tr = PrecisePerformanceTestTracer(1.0, turn_off_gc=True)
    while tr.iter():
        counter(data)
    with tr as fast_iter:
        for i in fast_iter:
            counter(data)
    print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))

    print()
    data = test_data_factory(TestDataType.deep_large)
    print('Large, Deep: {}'.format(counter(data)))
    tr = PrecisePerformanceTestTracer(1.0, turn_off_gc=True)
    while tr.iter():
        counter(data)
    with tr as fast_iter:
        for i in fast_iter:
            counter(data)
    print('{} iter/s; {} seconds; {} iterations'.format(tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))


def main():
    test_objects_counter()
    test_objects_counter_performance()
    test_objects_counter_recursive_performance()


if __name__ == '__main__':
    main()
