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
__version__ = "4.3.2"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.data_manipulation.remote_objects.versions.v_0_fast_optimized.remote_objects import *
from cengal.code_flow_control.smart_values import ResultExistence
from cengal.code_flow_control.gc import DisableGC, EnableGC
from cengal.performance_test_lib import MeasureTime, measure_func_isolated_performance
from cengal.data_manipulation.serialization import test_data_factory, TestDataType, best_serializer, \
    SerializerFeatures, Tags, DataFormats, get_most_efficient_serializers
from cengal.introspection.inspect import cen, entity_name
# from cengal.code_inspection.line_profiling import set_profiler, profiler_result
from collections import deque
from dataclasses import dataclass
from pickle import loads as pickle_loads, dumps as pickle_dumps
from marshal import loads as marshal_loads, dumps as marshal_dumps
from pprint import pprint
from typing import Any, Dict, Optional, Callable, Set, Type, Tuple, List, FrozenSet, Deque


'''
>>> "tuple(tuple_of_tuple_gen())": func()
         It was used 0.09375 seconds to make 2067 iterations. Performance: 22048.0 iterations/seconds
         Isolated run time: 7.294700480997562e-06 seconds; Isolated performance: 137085.82039865307 iterations/seconds

>>> "result.append((i, i + 1))": func1()
         It was used 0.15625 seconds to make 2551 iterations. Performance: 16326.400390625 iterations/seconds
         Isolated run time: 8.169969078153372e-06 seconds; Isolated performance: 122399.4840658597 iterations/seconds

>>> "result.append((i, i + 1))": func3()
         It was used 0.03125 seconds to make 1286 iterations. Performance: 41152.0 iterations/seconds
         Isolated run time: 8.511764463037252e-06 seconds; Isolated performance: 117484.4539393152 iterations/seconds

>>> "result[i] = i + 1": func4()
         It was used 0.125 seconds to make 1559 iterations. Performance: 12472.0 iterations/seconds
         Isolated run time: 5.966227035969496e-06 seconds; Isolated performance: 167610.1150645372 iterations/seconds

>>> "result[i] = i + 1": func5()
         It was used 0.09375 seconds to make 1702 iterations. Performance: 18154.666015625 iterations/seconds
         Isolated run time: 8.310889825224876e-06 seconds; Isolated performance: 120324.0592800112 iterations/seconds

>>> "dict(tuple_of_tuple_gen())": func6()
         It was used 0.0625 seconds to make 2048 iterations. Performance: 32768.0 iterations/seconds
         Isolated run time: 9.921728633344173e-06 seconds; Isolated performance: 100788.88840390956 iterations/seconds

>>> "result[i] = (i, i + 1)": func7()
         It was used 0.03125 seconds to make 709 iterations. Performance: 22688.0 iterations/seconds
         Isolated run time: 6.438232958316803e-06 seconds; Isolated performance: 155322.1212208882 iterations/seconds

>>> "result.append((i, i + 1))": func8()
         It was used 0.34375 seconds to make 3224 iterations. Performance: 9378.9091796875 iterations/seconds
         Isolated run time: 7.481721695512533e-06 seconds; Isolated performance: 133659.0748356479 iterations/seconds

>>> "deque(tuple_of_tuple_gen())": func9()
         It was used 0.09375 seconds to make 3843 iterations. Performance: 40992.0 iterations/seconds
         Isolated run time: 6.908201612532139e-06 seconds; Isolated performance: 144755.47415783355 iterations/seconds

>>> "result[i] = (i, i + 1)": func10()
         It was used 0.1875 seconds to make 4549 iterations. Performance: 24261.333984375 iterations/seconds
         Isolated run time: 6.4435298554599285e-06 seconds; Isolated performance: 155194.43882961906 iterations/seconds

>>> "result[i] = (i, i + 1)": func11()
         It was used 0.125 seconds to make 2812 iterations. Performance: 22496.0 iterations/seconds
         Isolated run time: 6.4391642808914185e-06 seconds; Isolated performance: 155299.6563494359 iterations/seconds

>>> "result[i] = (i, i + 1)": func12()
         It was used 0.0625 seconds to make 3375 iterations. Performance: 54000.0 iterations/seconds
         Isolated run time: 6.4444029703736305e-06 seconds; Isolated performance: 155173.41243203208 iterations/seconds

>>> "result[i[0]] = i": func13()
         It was used 0.09375 seconds to make 1987 iterations. Performance: 21194.666015625 iterations/seconds
         Isolated run time: 1.0837335139513016e-05 seconds; Isolated performance: 92273.60666867186 iterations/seconds

>>> "result.append(i)": func14()
         It was used 0.0625 seconds to make 1468 iterations. Performance: 23488.0 iterations/seconds
         Isolated run time: 1.1144380550831556e-05 seconds; Isolated performance: 89731.3220271703 iterations/seconds

>>> "result.add(i)": func15()
         It was used 0.0625 seconds to make 1066 iterations. Performance: 17056.0 iterations/seconds
         Isolated run time: 1.4020886737853289e-05 seconds; Isolated performance: 71322.16518804202 iterations/seconds

>>> "set(tuple_of_tuple_gen())": func16()
         It was used 0.03125 seconds to make 885 iterations. Performance: 28320.0 iterations/seconds
         Isolated run time: 9.859970305114985e-06 seconds; Isolated performance: 101420.18373840714 iterations/seconds

>>> "set(tuple_of_tuple_gen())": func17()
         It was used 0.09375 seconds to make 1125 iterations. Performance: 12000.0 iterations/seconds
         Isolated run time: 9.884708561003208e-06 seconds; Isolated performance: 101166.36154000164 iterations/seconds

>>> "2 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)": func18()
         It was used 0.53125 seconds to make 110834 iterations. Performance: 208628.703125 iterations/seconds
         Isolated run time: 1.3085082173347473e-07 seconds; Isolated performance: 7642290.56227758 iterations/seconds

>>> "2 in data_tuple": func19()
         It was used 0.09375 seconds to make 33893 iterations. Performance: 361525.34375 iterations/seconds
         Isolated run time: 1.3352837413549423e-07 seconds; Isolated performance: 7489044.97994769 iterations/seconds

>>> "2 in data_tuple": func20()
         It was used 0.40625 seconds to make 131072 iterations. Performance: 322638.78125 iterations/seconds
         Isolated run time: 1.3440148904919624e-07 seconds; Isolated performance: 7440393.75660459 iterations/seconds

>>> "2 in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}": func21()
         It was used 0.15625 seconds to make 131072 iterations. Performance: 838860.8125 iterations/seconds
         Isolated run time: 1.2264354154467583e-07 seconds; Isolated performance: 8153711.050783104 iterations/seconds

>>> "2 in data_set": func22()
         It was used 0.09375 seconds to make 192098 iterations. Performance: 2049045.375 iterations/seconds
         Isolated run time: 1.2438977137207985e-07 seconds; Isolated performance: 8039246.225549837 iterations/seconds

>>> "2 in data_set": func23()
         It was used 0.0625 seconds to make 88178 iterations. Performance: 1410848.0 iterations/seconds
         Isolated run time: 1.2700911611318588e-07 seconds; Isolated performance: 7873450.588450963 iterations/seconds

>>> "2 in (1, 2, 3)": func24()
         It was used 0.25 seconds to make 262144 iterations. Performance: 1048576.0 iterations/seconds
         Isolated run time: 1.3085082173347473e-07 seconds; Isolated performance: 7642290.56227758 iterations/seconds

>>> "2 in (1, 2)": func25()
         It was used 0.28125 seconds to make 213497 iterations. Performance: 759100.4375 iterations/seconds
         Isolated run time: 1.3085082173347473e-07 seconds; Isolated performance: 7642290.56227758 iterations/seconds

>>> "2 in {1, 2, 3}": func26()
         It was used 0.1875 seconds to make 126525 iterations. Performance: 674800.0 iterations/seconds
         Isolated run time: 1.2264354154467583e-07 seconds; Isolated performance: 8153711.050783104 iterations/seconds

>>> "2 in {1, 2}": func27()
         It was used 0.15625 seconds to make 77555 iterations. Performance: 496352.0 iterations/seconds
         Isolated run time: 1.2351665645837784e-07 seconds; Isolated performance: 8096074.073515551 iterations/seconds

>>> "(2 == 1) or (2 == 2)": func28()
         It was used 0.34375 seconds to make 131072 iterations. Performance: 381300.375 iterations/seconds
         Isolated run time: 1.4441320672631264e-07 seconds; Isolated performance: 6924574.4393389765 iterations/seconds

>>> "(2 == 1) or (2 == 2) or (2 == 3)": func29()
         It was used 0.1875 seconds to make 46990 iterations. Performance: 250613.328125 iterations/seconds
         Isolated run time: 1.4615943655371666e-07 seconds; Isolated performance: 6841843.561927519 iterations/seconds

>>> "math_impl()": func30()
         It was used 0.09375 seconds to make 65536 iterations. Performance: 699050.6875 iterations/seconds
         Isolated run time: 1.5436671674251556e-07 seconds; Isolated performance: 6478080.3861236805 iterations/seconds

>>> "k = 56 + 15": func31()
         It was used 0.125 seconds to make 241808 iterations. Performance: 1934464.0 iterations/seconds
         Isolated run time: 1.100124791264534e-07 seconds; Isolated performance: 9089877.875132276 iterations/seconds

>>> "sc.func()": func32()
         It was used 0.125 seconds to make 124743 iterations. Performance: 997944.0 iterations/seconds
         Isolated run time: 1.8998980522155762e-07 seconds; Isolated performance: 5263440.31372549 iterations/seconds

>>> "sc.func0()": func33()
         It was used 0.09375 seconds to make 110931 iterations. Performance: 1183264.0 iterations/seconds
         Isolated run time: 2.0529842004179955e-07 seconds; Isolated performance: 4870958.09016161 iterations/seconds

>>> "sc.func1()": func34()
         It was used 0.0625 seconds to make 115833 iterations. Performance: 1853328.0 iterations/seconds
         Isolated run time: 2.1175947040319443e-07 seconds; Isolated performance: 4722338.973062122 iterations/seconds

>>> "sc.func2()": func35()
         It was used 0.21875 seconds to make 270553 iterations. Performance: 1236813.75 iterations/seconds
         Isolated run time: 1.9173603504896164e-07 seconds; Isolated performance: 5215503.698846388 iterations/seconds

>>> "sc.func3()": func36()
         It was used 0.09375 seconds to make 98726 iterations. Performance: 1053077.375 iterations/seconds
         Isolated run time: 2.00001522898674e-07 seconds; Isolated performance: 4999961.92782305 iterations/seconds

>>> "sc.func4()": func37()
         It was used 0.59375 seconds to make 131072 iterations. Performance: 220752.84375 iterations/seconds
         Isolated run time: 2.2177118808031082e-07 seconds; Isolated performance: 4509152.0167979 iterations/seconds

>>> "result[i * 2 + 1] = i + 1": func38()
         It was used 0.0 seconds to make 165 iterations. Performance: 0.0 iterations/seconds
         Isolated run time: 1.179176615551114e-05 seconds; Isolated performance: 84804.93819262419 iterations/seconds

>>> "result[j + 1] = i + 1": func39()
         It was used 0.0 seconds to make 275 iterations. Performance: 0.0 iterations/seconds
         Isolated run time: 1.0835588909685612e-05 seconds; Isolated performance: 92288.47719629983 iterations/seconds

>>> "result[j: j + 1] = i, i + 1": func40()
         It was used 0.125 seconds to make 335 iterations. Performance: 2680.0 iterations/seconds
         Isolated run time: 1.9381754100322723e-05 seconds; Isolated performance: 51594.91730334919 iterations/seconds

>>> "result = {i: i + 1 for i in range(100)}": func41()
         It was used 0.1875 seconds to make 1524 iterations. Performance: 8128.0 iterations/seconds
         Isolated run time: 5.629146471619606e-06 seconds; Isolated performance: 177646.82532985896 iterations/seconds

>>> "result = {(i, i + 1) for i in range(100)}": func42()
         It was used 0.9375 seconds to make 50775 iterations. Performance: 54160.0 iterations/seconds
         Isolated run time: 7.962633389979601e-06 seconds; Isolated performance: 125586.59315628267 iterations/seconds

>>> "result = [(i, i + 1) for i in range(100)]": func43()
         It was used 0.4375 seconds to make 38632 iterations. Performance: 88301.7109375 iterations/seconds
         Isolated run time: 5.753536242991686e-06 seconds; Isolated performance: 173806.15290606505 iterations/seconds

>>> "result = tuple((i, i + 1) for i in range(100))": func44()
         It was used 1.75 seconds to make 60073 iterations. Performance: 34327.4296875 iterations/seconds
         Isolated run time: 7.323513273149729e-06 seconds; Isolated performance: 136546.4856418449 iterations/seconds

>>> "result = tuple([(i, i + 1) for i in range(100)])": func45()
         It was used 1.375 seconds to make 126056 iterations. Performance: 91677.09375 iterations/seconds
         Isolated run time: 5.792942829430103e-06 seconds; Isolated performance: 172623.8337653986 iterations/seconds
'''


def tuple_of_tuple_gen():
    for i in range(100):
        yield (i, i + 1)


def math_impl():
    k = 56 + 15


data_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


class SimpleClass:
    def __init__(self) -> None:
        self.data_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    
    def func(self):
        2 in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    
    def func0(self):
        2 in self.data_set
    
    def func1(self):
        data_set = self.data_set
        2 in data_set
    
    def func2(self):
        2 in data_set
    
    def func3(self, data_set=data_set):
        2 in data_set
    
    def func4(self,
              data_set=data_set,
              data_set1=None,
              data_set2=None,
              data_set3=None,
              data_set4=None,
              data_set5=None,
              data_set6=None,
              data_set7=None,
              data_set8=None,
              data_set9=None,
              data_set10=None,
              data_set11=None,
              ):
        2 in data_set


def benchmark():
    def func():
        tuple(tuple_of_tuple_gen())
    
    with DisableGC():
        measure_func_isolated_performance(func, 0.1, 'tuple(tuple_of_tuple_gen())', do_print=True)
        print()

    def func1():
        result = list()
        for i in range(100):
            result.append((i, i + 1))
    
    with DisableGC():
        measure_func_isolated_performance(func1, 0.1, 'result.append((i, i + 1))', do_print=True)
        print()

    def func3():
        result = list()
        for i in range(100):
            result.append((i, i + 1))
        tuple(result)
    
    with DisableGC():
        measure_func_isolated_performance(func3, 0.1, 'result.append((i, i + 1))', do_print=True)
        print()

    def func4():
        result = dict()
        for i in range(100):
            result[i] = i + 1
    
    with DisableGC():
        measure_func_isolated_performance(func4, 0.1, 'result[i] = i + 1', do_print=True)
        print()

    def func5():
        result = dict()
        for i in range(100):
            result[i] = i + 1
            
        tuple(result.items())
    
    with DisableGC():
        measure_func_isolated_performance(func5, 0.1, 'result[i] = i + 1', do_print=True)
        print()

    def func6():
        dict(tuple_of_tuple_gen())
    
    with DisableGC():
        measure_func_isolated_performance(func6, 0.1, 'dict(tuple_of_tuple_gen())', do_print=True)
        print()

    def func7():
        result = [None] * 100
        for i in range(100):
            result[i] = (i, i + 1)
    
    with DisableGC():
        measure_func_isolated_performance(func7, 0.1, 'result[i] = (i, i + 1)', do_print=True)
        print()

    def func8():
        result = deque()
        for i in range(100):
            result.append((i, i + 1))
    
    with DisableGC():
        measure_func_isolated_performance(func8, 0.1, 'result.append((i, i + 1))', do_print=True)
        print()

    def func9():
        deque(tuple_of_tuple_gen())
    
    with DisableGC():
        measure_func_isolated_performance(func9, 0.1, 'deque(tuple_of_tuple_gen())', do_print=True)
        print()

    def func10():
        result = [0] * 100
        for i in range(100):
            result[i] = (i, i + 1)
    
    with DisableGC():
        measure_func_isolated_performance(func10, 0.1, 'result[i] = (i, i + 1)', do_print=True)
        print()

    def func11():
        result = [False] * 100
        for i in range(100):
            result[i] = (i, i + 1)
    
    with DisableGC():
        measure_func_isolated_performance(func11, 0.1, 'result[i] = (i, i + 1)', do_print=True)
        print()

    def func12():
        result = [True] * 100
        for i in range(100):
            result[i] = (i, i + 1)
    
    with DisableGC():
        measure_func_isolated_performance(func12, 0.1, 'result[i] = (i, i + 1)', do_print=True)
        print()

    def func13():
        result = [True] * 100
        for i in tuple_of_tuple_gen():
            result[i[0]] = i
    
    with DisableGC():
        measure_func_isolated_performance(func13, 0.1, 'result[i[0]] = i', do_print=True)
        print()

    def func14():
        result = list()
        for i in tuple_of_tuple_gen():
            result.append(i)
    
    with DisableGC():
        measure_func_isolated_performance(func14, 0.1, 'result.append(i)', do_print=True)
        print()

    def func15():
        result = set()
        for i in tuple_of_tuple_gen():
            result.add(i)
    
    with DisableGC():
        measure_func_isolated_performance(func15, 0.1, 'result.add(i)', do_print=True)
        print()

    def func16():
        set(tuple_of_tuple_gen())
    
    with DisableGC():
        measure_func_isolated_performance(func16, 0.1, 'set(tuple_of_tuple_gen())', do_print=True)
        print()

    def func17(set=set):
        set(tuple_of_tuple_gen())
    
    with DisableGC():
        measure_func_isolated_performance(func17, 0.1, 'set(tuple_of_tuple_gen())', do_print=True)
        print()

    def func18():
        2 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    
    with DisableGC():
        measure_func_isolated_performance(func18, 0.1, '2 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)', do_print=True)
        print()

    data_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    def func19():
        2 in data_tuple
    
    with DisableGC():
        measure_func_isolated_performance(func19, 0.1, '2 in data_tuple', do_print=True)
        print()

    data_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    def func20(data_tuple=data_tuple):
        2 in data_tuple
    
    with DisableGC():
        measure_func_isolated_performance(func20, 0.1, '2 in data_tuple', do_print=True)
        print()

    def func21():
        2 in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    
    with DisableGC():
        measure_func_isolated_performance(func21, 0.1, '2 in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}', do_print=True)
        print()

    data_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    def func22():
        2 in data_set
    
    with DisableGC():
        measure_func_isolated_performance(func22, 0.1, '2 in data_set', do_print=True)
        print()

    data_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    def func23(data_set=data_set):
        2 in data_set
    
    with DisableGC():
        measure_func_isolated_performance(func23, 0.1, '2 in data_set', do_print=True)
        print()

    def func24():
        2 in (1, 2, 3)
    
    with DisableGC():
        measure_func_isolated_performance(func24, 0.1, '2 in (1, 2, 3)', do_print=True)
        print()

    def func25():
        2 in (1, 2)
    
    with DisableGC():
        measure_func_isolated_performance(func25, 0.1, '2 in (1, 2)', do_print=True)
        print()

    def func26():
        2 in {1, 2, 3}
    
    with DisableGC():
        measure_func_isolated_performance(func26, 0.1, '2 in {1, 2, 3}', do_print=True)
        print()

    def func27():
        2 in {1, 2}
    
    with DisableGC():
        measure_func_isolated_performance(func27, 0.1, '2 in {1, 2}', do_print=True)
        print()

    def func28():
        (2 == 1) or (2 == 2)
    
    with DisableGC():
        measure_func_isolated_performance(func28, 0.1, '(2 == 1) or (2 == 2)', do_print=True)
        print()

    def func29():
        (2 == 1) or (2 == 2) or (2 == 3)
    
    with DisableGC():
        measure_func_isolated_performance(func29, 0.1, '(2 == 1) or (2 == 2) or (2 == 3)', do_print=True)
        print()

    def func30():
        math_impl()
    
    with DisableGC():
        measure_func_isolated_performance(func30, 0.1, 'math_impl()', do_print=True)
        print()

    def func31():
        k = 56 + 15
    
    with DisableGC():
        measure_func_isolated_performance(func31, 0.1, 'k = 56 + 15', do_print=True)
        print()
    
    sc = SimpleClass()

    def func32():
        sc.func()
    
    with DisableGC():
        measure_func_isolated_performance(func32, 0.1, 'sc.func()', do_print=True)
        print()

    def func33():
        sc.func0()
    
    with DisableGC():
        measure_func_isolated_performance(func33, 0.1, 'sc.func0()', do_print=True)
        print()

    def func34():
        sc.func1()
    
    with DisableGC():
        measure_func_isolated_performance(func34, 0.1, 'sc.func1()', do_print=True)
        print()

    def func35():
        sc.func2()
    
    with DisableGC():
        measure_func_isolated_performance(func35, 0.1, 'sc.func2()', do_print=True)
        print()

    def func36():
        sc.func3()
    
    with DisableGC():
        measure_func_isolated_performance(func36, 0.1, 'sc.func3()', do_print=True)
        print()

    def func37():
        sc.func4()
    
    with DisableGC():
        measure_func_isolated_performance(func37, 0.1, 'sc.func4()', do_print=True)
        print()

    def func38():
        result = [None] * 200
        for i in range(100):
            result[i * 2] = i
            result[i * 2 + 1] = i + 1
    
    with DisableGC():
        measure_func_isolated_performance(func38, 0.1, 'result[i * 2 + 1] = i + 1', do_print=True)
        print()

    def func39():
        result = [None] * 200
        for i in range(100):
            j = i * 2
            result[j] = i
            result[j + 1] = i + 1
    
    with DisableGC():
        measure_func_isolated_performance(func39, 0.1, 'result[j + 1] = i + 1', do_print=True)
        print()

    def func40():
        result = [None] * 200
        for i in range(100):
            j = i * 2
            result[j: j + 1] = i, i + 1
    
    with DisableGC():
        measure_func_isolated_performance(func40, 0.1, 'result[j: j + 1] = i, i + 1', do_print=True)
        print()

    def func41():
        result = {i: i + 1 for i in range(100)}
    
    with DisableGC():
        measure_func_isolated_performance(func41, 0.1, 'result = {i: i + 1 for i in range(100)}', do_print=True)
        print()

    def func42():
        result = {(i, i + 1) for i in range(100)}
    
    with DisableGC():
        measure_func_isolated_performance(func42, 0.1, 'result = {(i, i + 1) for i in range(100)}', do_print=True)
        print()

    def func43():
        result = [(i, i + 1) for i in range(100)]
    
    with DisableGC():
        measure_func_isolated_performance(func43, 0.1, 'result = [(i, i + 1) for i in range(100)]', do_print=True)
        print()

    def func44():
        result = tuple((i, i + 1) for i in range(100))
    
    with DisableGC():
        measure_func_isolated_performance(func44, 0.1, 'result = tuple((i, i + 1) for i in range(100))', do_print=True)
        print()

    def func45():
        result = tuple([(i, i + 1) for i in range(100)])
    
    with DisableGC():
        measure_func_isolated_performance(func45, 0.1, 'result = tuple([(i, i + 1) for i in range(100)])', do_print=True)
        print()

    def func46():
        result = dict()
        result[0] = 0
        result[1] = 1
        result[2] = 2
        result[3] = 3
        result[4] = 4
        result[5] = 5
        result[6] = 6
        result[7] = 7
        result[8] = 8
        result[9] = 9
    
    with DisableGC():
        measure_func_isolated_performance(func46, 0.1, 'result[9] = 9', do_print=True)
        print()

    def func47():
        result = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 9
        }
    
    with DisableGC():
        measure_func_isolated_performance(func47, 0.1, 'result = {', do_print=True)
        print()

    def func48():
        result = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
        }
        result[8] = 8
        result[9] = 9
    
    with DisableGC():
        measure_func_isolated_performance(func48, 0.1, 'result[8] = 8', do_print=True)
        print()

    def func49():
        result = (
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
        )
    
    with DisableGC():
        measure_func_isolated_performance(func49, 0.1, 'result = ((0, 0),', do_print=True)
        print()

    def func50():
        result = [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
        ]
    
    with DisableGC():
        measure_func_isolated_performance(func50, 0.1, 'result = [(0, 0),', do_print=True)
        print()

    def func51():
        result = (
            [0, 0],
            [1, 1],
            [2, 2],
            [3, 3],
            [4, 4],
            [5, 5],
            [6, 6],
            [7, 7],
            [8, 8],
            [9, 9],
        )
    
    with DisableGC():
        measure_func_isolated_performance(func51, 0.1, 'result = ([0, 0],', do_print=True)
        print()

    def func52():
        result = [
            [0, 0],
            [1, 1],
            [2, 2],
            [3, 3],
            [4, 4],
            [5, 5],
            [6, 6],
            [7, 7],
            [8, 8],
            [9, 9],
        ]
    
    with DisableGC():
        measure_func_isolated_performance(func52, 0.1, 'result = [[0, 0],', do_print=True)
        print()

    def func53():
        result1 = (
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
        )
        result2 = (
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
        )
        result = result1 + result2
    
    with DisableGC():
        measure_func_isolated_performance(func53, 0.1, 'result = result1 + result2', do_print=True)
        print()

    def func54():
        result1 = (
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
        )
        result = result1 + (
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
        )
    
    with DisableGC():
        measure_func_isolated_performance(func54, 0.1, 'result = result1 + (', do_print=True)
        print()

    def func55():
        result1 = [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
        ]
        result = result1 + [
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
        ]
    
    with DisableGC():
        measure_func_isolated_performance(func55, 0.1, 'result = result1 + [', do_print=True)
        print()

    def func56():
        result = [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
        ]
        result.extend((
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
        ))

    with DisableGC():
        measure_func_isolated_performance(func56, 0.1, 'result.extend((', do_print=True)
        print()

    def func57():
        result = (
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
        )
        result += (
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
        )
    
    with DisableGC():
        measure_func_isolated_performance(func57, 0.1, 'result += (', do_print=True)
        print()

    def func58():
        object_id = 1
        type_id = 2
        class_id = 3
        new_obj_slots = (('a', 1), ('b', 2))
        new_obj_dict = {'a': 1, 'b': 2}
        obj_mapping = {1: 2, 3: 4}
        obj_sequence = [1, 2, 3, 4]
        obj_set = {1, 2, 3, 4}
        object_info = (
            object_id,
            type_id,
            None,
            class_id,
            new_obj_slots if new_obj_slots else None,
            new_obj_dict if new_obj_dict else None,
            obj_mapping if obj_mapping else None,
            obj_sequence if obj_sequence else None,
            obj_set if obj_set else None,
        )
    
    with DisableGC():
        measure_func_isolated_performance(func58, 0.1, 'object_info = (new_obj_slots if new_obj_slots else None', do_print=True)
        print()

    def func59():
        object_id = 1
        type_id = 2
        class_id = 3
        new_obj_slots = (('a', 1), ('b', 2))
        new_obj_dict = {'a': 1, 'b': 2}
        obj_mapping = {1: 2, 3: 4}
        obj_sequence = [1, 2, 3, 4]
        obj_set = {1, 2, 3, 4}
        object_info = (
            object_id,
            type_id,
            None,
            class_id,
            new_obj_slots,
            new_obj_dict,
            obj_mapping,
            obj_sequence,
            obj_set,
        )
    
    with DisableGC():
        measure_func_isolated_performance(func59, 0.1, 'object_info = (', do_print=True)
        print()

    def func60():
        object_id = 1
        type_id = 2
        class_id = 3
        new_obj_slots = tuple()
        new_obj_dict = {'a': 1, 'b': 2}
        obj_mapping = dict()
        obj_sequence = list()
        obj_set = set()
        object_info = (
            object_id,
            type_id,
            None,
            class_id,
            new_obj_slots if new_obj_slots else None,
            new_obj_dict if new_obj_dict else None,
            obj_mapping if obj_mapping else None,
            obj_sequence if obj_sequence else None,
            obj_set if obj_set else None,
        )
    
    with DisableGC():
        measure_func_isolated_performance(func60, 0.1, 'object_info = (new_obj_slots if new_obj_slots else None) new_obj_slots = tuple()', do_print=True)
        print()

    def func61():
        object_id = 1
        type_id = 2
        class_id = 3
        new_obj_slots = tuple()
        new_obj_dict = {'a': 1, 'b': 2}
        obj_mapping = dict()
        obj_sequence = list()
        obj_set = set()
        object_info = (
            object_id,
            type_id,
            None,
            class_id,
            new_obj_slots,
            new_obj_dict,
            obj_mapping,
            obj_sequence,
            obj_set,
        )
    
    with DisableGC():
        measure_func_isolated_performance(func61, 0.1, 'object_info = () new_obj_slots = tuple()', do_print=True)
        print()

    def func62():
        object_id = 1
        type_id = 2
        class_id = 3
        new_obj_slots = tuple()
        new_obj_dict = {'a': 1, 'b': 2}
        obj_mapping = dict()
        obj_sequence = list()
        obj_set = set()
        object_info = (
            object_id,
            type_id,
            None,
            class_id,
            new_obj_slots if new_obj_slots else None,
            new_obj_dict if new_obj_dict else None,
            obj_mapping if obj_mapping else None,
            obj_sequence if obj_sequence else None,
            obj_set if obj_set else None,
        )
        marshal_loads(marshal_dumps(object_info))
    
    with DisableGC():
        measure_func_isolated_performance(func62, 0.1, 'marshal_loads object_info = (new_obj_slots if new_obj_slots else None) new_obj_slots = tuple()', do_print=True)
        print()

    def func63():
        object_id = 1
        type_id = 2
        class_id = 3
        new_obj_slots = tuple()
        new_obj_dict = {'a': 1, 'b': 2}
        obj_mapping = dict()
        obj_sequence = list()
        obj_set = set()
        object_info = (
            object_id,
            type_id,
            None,
            class_id,
            new_obj_slots,
            new_obj_dict,
            obj_mapping,
            obj_sequence,
            obj_set,
        )
        marshal_loads(marshal_dumps(object_info))
    
    with DisableGC():
        measure_func_isolated_performance(func63, 0.1, 'marshal_loads object_info = () new_obj_slots = tuple()', do_print=True)
        print()

    def func64():
        serialisable_set = True
        obj_set = {1, 2, 3, 4}
        if obj_set:
            if serialisable_set:
                pass
            else:
                obj_set = set(obj_set)
    
    with DisableGC():
        measure_func_isolated_performance(func64, 0.1, 'obj_set = {1, 2, 3, 4}', do_print=True)
        print()

    def func65():
        serialisable_set = True
        obj_set = {1, 2, 3, 4}
        obj_set = obj_set if serialisable_set else set(obj_set)
    
    with DisableGC():
        measure_func_isolated_performance(func65, 0.1, 'obj_set = obj_set if serialisable_set else set(obj_set)', do_print=True)
        print()

    def func67():
        result = [None] * 100
        result.clear()
        for i in range(100):
            result.append((i, i + 1))
    
    with DisableGC():
        measure_func_isolated_performance(func67, 0.1, 'result.clear()', do_print=True)
        print()


def main():
    benchmark()


if __name__ == '__main__':
    main()
