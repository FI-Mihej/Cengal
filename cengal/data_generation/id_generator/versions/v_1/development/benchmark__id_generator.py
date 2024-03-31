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


from cengal.data_generation.id_generator.versions.v_1.id_generator import IDGenerator as IDGeneratorPy, GeneratorType as GeneratorTypePy
from cengal.data_generation.id_generator.versions.v_1.compilable import IDGenerator as IDGeneratorCy, GeneratorType as GeneratorTypeCy
from cengal.code_flow_control.gc import DisableGC, EnableGC
from cengal.performance_test_lib import MeasureTime, measure_func_isolated_performance
from cengal.introspection.inspect import cen, func_name
from pprint import pprint
from typing import Any, Dict, Optional, Callable, Set, Type, Tuple, List, FrozenSet, Deque, Generator


'''
>>> "gen_class=<class 'cengal.data_generation.id_generator.versions.v_1.id_generator.IDGenerator'>, gen_type=<GeneratorType.integer: 0>, func": func()
         It was used 4.455078125 seconds to make 1348031 iterations. Performance: 302583.03125 iterations/seconds
         Isolated run time: 3.470577212283388e-07 seconds; Isolated performance: 2881365.083769661 iterations/seconds

>>> "gen_class=<class 'cengal.data_generation.id_generator.versions.v_1.id_generator.IDGenerator'>, gen_type=<GeneratorType.integer: 0>, func1": func1()
         It was used 2.566406011581421 seconds to make 2586650 iterations. Performance: 1007888.0625 iterations/seconds
         Isolated run time: 2.900014806073159e-07 seconds; Isolated performance: 3448258.2568399925 iterations/seconds

>>> "gen_class=<class 'cengal.data_generation.id_generator.versions.v_1.id_generator.IDGenerator'>, gen_type=<GeneratorType.guid_string: 1>, func": func()
         It was used 4.6142578125 seconds to make 561680 iterations. Performance: 121727.0546875 iterations/seconds
         Isolated run time: 5.407058779383078e-06 seconds; Isolated performance: 184943.43057873982 iterations/seconds

>>> "gen_class=<class 'cengal.data_generation.id_generator.versions.v_1.id_generator.IDGenerator'>, gen_type=<GeneratorType.guid_string: 1>, func1": func1()
         It was used 5.119141101837158 seconds to make 665235 iterations. Performance: 129950.5078125 iterations/seconds
         Isolated run time: 5.25058749190066e-06 seconds; Isolated performance: 190454.87796223923 iterations/seconds

>>> "gen_class=<built-in function IDGenerator>, gen_type=<GeneratorType.integer: 0>, func": func()
         It was used 5.2744140625 seconds to make 13737977 iterations. Performance: 2604645.25 iterations/seconds
         Isolated run time: 1.4205761544872075e-07 seconds; Isolated performance: 7039397.337772258 iterations/seconds

>>> "gen_class=<built-in function IDGenerator>, gen_type=<GeneratorType.integer: 0>, func1": func1()
         It was used 6.363280773162842 seconds to make 14809780 iterations. Performance: 2327381.25 iterations/seconds
         Isolated run time: 1.4911711332388222e-07 seconds; Isolated performance: 6706138.401619947 iterations/seconds

>>> "gen_class=<built-in function IDGenerator>, gen_type=<GeneratorType.guid_string: 1>, func": func()
         It was used 5.278319835662842 seconds to make 664780 iterations. Performance: 125945.3828125 iterations/seconds
         Isolated run time: 5.2044124458916485e-06 seconds; Isolated performance: 192144.6484875344 iterations/seconds

>>> "gen_class=<built-in function IDGenerator>, gen_type=<GeneratorType.guid_string: 1>, func1": func1()
         It was used 4.984375 seconds to make 620394 iterations. Performance: 124467.765625 iterations/seconds
         Isolated run time: 5.2323539421195164e-06 seconds; Isolated performance: 191118.56939764306 iterations/seconds
'''


def benchmark():
    gen = None
    gen_type = None
    def func():
        gen()
    
    def func1():
        gen.get_new_id()
    
    with DisableGC():
    # with EnableGC():
        gen_variants = {
            IDGeneratorPy: (
                GeneratorTypePy.integer,
                GeneratorTypePy.guid_string,
            ),
            IDGeneratorCy: (
                GeneratorTypeCy.integer,
                GeneratorTypeCy.guid_string,
            )
        }
        functions = (
            func,
            func1,
        )
        for gen_class, gen_types in gen_variants.items():
            for gen_type in gen_types:
                gen = gen_class(gen_type)
                for fun in functions:
                    measure_func_isolated_performance(fun, 5.1, f'{gen_class=}, {gen_type=}, {func_name(fun)}', do_print=True)
                    print()


def main():
    benchmark()


if __name__ == '__main__':
    main()
