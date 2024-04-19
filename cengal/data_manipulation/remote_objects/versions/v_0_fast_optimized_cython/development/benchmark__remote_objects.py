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


from cengal.data_manipulation.remote_objects.versions.v_0_fast_optimized_cython import *
from cengal.data_manipulation.remote_objects.versions.v_0_fast import RemoteObjectsManager as FastRemoteObjectsManager
from cengal.data_manipulation.remote_objects.versions.v_0 import RemoteObjectsManager as UniversalRemoteObjectsManager
from cengal.data_manipulation.remote_objects.versions.v_0_optimized import RemoteObjectsManager as UniversalOptimizedRemoteObjectsManager
from cengal.code_flow_control.smart_values import ResultExistence
from cengal.code_flow_control.gc import DisableGC, EnableGC
from cengal.performance_test_lib import MeasureTime, measure_func_isolated_performance
from cengal.data_manipulation.serialization import test_data_factory, TestDataType, best_serializer, \
    SerializerFeatures, Tags, DataFormats, get_most_efficient_serializers, SUPPORTED_TYPES, Serializers, \
    Serializer
from cengal.introspection.inspect import cen
# from cengal.code_inspection.line_profiling import set_profiler, profiler_result
from collections import deque
from dataclasses import dataclass
from pickle import loads as pickle_loads, dumps as pickle_dumps
from marshal import loads as marshal_loads, dumps as marshal_dumps
from pprint import pprint
from typing import Any, Dict, Optional, Callable, Set, Type, Tuple, List, FrozenSet, Deque, Generator


'''
>>> "DataClass": func()
         It was used 3.6875 seconds to make 16384 iterations. Performance: 4443.11865234375 iterations/seconds
         Isolated run time: 5.249737296253443e-05 seconds; Isolated performance: 19048.572215483346 iterations/seconds

>>> "DataClass": func_marshal()
         It was used 4.625 seconds to make 30751 iterations. Performance: 6648.86474609375 iterations/seconds
         Isolated run time: 3.728736191987991e-05 seconds; Isolated performance: 26818.73826710293 iterations/seconds

>>> "TestDataType.small": func()
         It was used 5.25 seconds to make 22876 iterations. Performance: 4357.33349609375 iterations/seconds
         Isolated run time: 0.00012538081500679255 seconds; Isolated performance: 7975.7018643229 iterations/seconds

>>> "TestDataType.small": func_marshal()
         It was used 4.125 seconds to make 32768 iterations. Performance: 7943.7578125 iterations/seconds
         Isolated run time: 7.8568235039711e-05 seconds; Isolated performance: 12727.790047651786 iterations/seconds

>>> "TestDataType.deep_small": func()
         It was used 3.5 seconds to make 51 iterations. Performance: 14.571428298950195 iterations/seconds
         Isolated run time: 0.05118787637911737 seconds; Isolated performance: 19.535875889705018 iterations/seconds

>>> "TestDataType.deep_small": func_marshal()
         It was used 6.3125 seconds to make 104 iterations. Performance: 16.475248336791992 iterations/seconds
         Isolated run time: 0.03493774321395904 seconds; Isolated performance: 28.62234099884447 iterations/seconds

>>> "TestDataType.large": func()
         It was used 6.125 seconds to make 25306 iterations. Performance: 4131.591796875 iterations/seconds
         Isolated run time: 0.00012238172348588705 seconds; Isolated performance: 8171.154740399771 iterations/seconds

>>> "TestDataType.large": func_marshal()
         It was used 5.1875 seconds to make 34436 iterations. Performance: 6638.26513671875 iterations/seconds
         Isolated run time: 8.24490562081337e-05 seconds; Isolated performance: 12128.701600605451 iterations/seconds

>>> "TestDataType.deep_large": func()
         It was used 5.4375 seconds to make 67 iterations. Performance: 12.321839332580566 iterations/seconds
         Isolated run time: 0.05091482272837311 seconds; Isolated performance: 19.64064581614921 iterations/seconds

>>> "TestDataType.deep_large": func_marshal()
         It was used 4.0625 seconds to make 84 iterations. Performance: 20.676923751831055 iterations/seconds
         Isolated run time: 0.034656079951673746 seconds; Isolated performance: 28.854965748995628 iterations/seconds

=== Serializers on DataClass: ==========================================================================
[(<Serializers.pickle: 16>, 80869.27689700622, 113),
 (<Serializers.cloudpickle: 30>, 1515.8113370493052, 3101)]

=== Serializers on TestDataType: =======================================================================
        == TestDataType.small: ==
                == current_platform: ==
[(<Serializers.msgspec_messagepack: 37>, 263915.8962762689, 77),
 (<Serializers.cbor: 8>, 232909.48163010765, 81),
 (<Serializers.msgspec_json: 36>, 226336.80944350758, 151),
 (<Serializers.pickle: 16>, 223173.15126006756, 116),
 (<Serializers.marshal: 10>, 216365.69839550642, 129),
 (<Serializers.orjson: 3>, 200577.56017372623, 151),
 (<Serializers.msgpack: 7>, 125512.27504785283, 77),
 (<Serializers.cloudpickle: 30>, 120626.51264551825, 116),
 (<Serializers.ujson: 2>, 112507.32929927963, 151),
 (<Serializers.cbor2: 9>, 56271.72171816759, 81),
 (<Serializers.json: 0>, 54085.97526759854, 180),
 (<Serializers.simplejson: 1>, 36191.30808770245, 180),
 (<Serializers.msgspec_toml: 39>, 2816.058999344007, 236),
 (<Serializers.msgspec_yaml: 38>, 1475.2564788124764, 176)]

                == multi_platform: ==
[(<Serializers.msgspec_messagepack: 37>, 258460.4962238604, 77),
 (<Serializers.cbor: 8>, 229016.06569265222, 81),
 (<Serializers.msgspec_json: 36>, 225227.05346233514, 151),
 (<Serializers.orjson: 3>, 204313.0745189449, 151),
 (<Serializers.msgpack: 7>, 121589.51678061347, 77),
 (<Serializers.ujson: 2>, 110440.28069273198, 151),
 (<Serializers.cbor2: 9>, 56900.54974695954, 81),
 (<Serializers.json: 0>, 53533.1832980182, 180),
 (<Serializers.simplejson: 1>, 35710.89582233382, 180),
 (<Serializers.msgspec_toml: 39>, 2957.2984174373833, 236),
 (<Serializers.msgspec_yaml: 38>, 1811.1048755778343, 176)]

        == TestDataType.deep_small: ==
                == current_platform: ==
[(<Serializers.marshal: 10>, 33983.338906274104, 5389),
 (<Serializers.pickle: 16>, 32527.158271011227, 2220),
 (<Serializers.cloudpickle: 30>, 28077.095230779792, 2220),
 (<Serializers.msgspec_messagepack: 37>, 3131.6375424588027, 20529),
 (<Serializers.orjson: 3>, 2178.281830227124, 41007),
 (<Serializers.msgspec_json: 36>, 1887.4011808322075, 41007),
 (<Serializers.cbor: 8>, 1136.8085520416125, 20568),
 (<Serializers.msgpack: 7>, 1128.3752129676652, 20529),
 (<Serializers.ujson: 2>, 654.6114060695209, 41007),
 (<Serializers.cbor2: 9>, 506.041712293243, 20568),
 (<Serializers.json: 0>, 388.0815232211861, 61194),
 (<Serializers.simplejson: 1>, 258.3876096933692, 61194),
 (<Serializers.msgspec_toml: 39>, 9.5443431040451, 141522),
 (<Serializers.msgspec_yaml: 38>, 3.8992500186687664, 161098)]

                == multi_platform: ==
[(<Serializers.msgspec_messagepack: 37>, 3155.622061603061, 20529),
 (<Serializers.orjson: 3>, 2180.731073953495, 41007),
 (<Serializers.msgspec_json: 36>, 1898.922312927095, 41007),
 (<Serializers.cbor: 8>, 1142.9997507735932, 20568),
 (<Serializers.msgpack: 7>, 1116.4621309798115, 20529),
 (<Serializers.ujson: 2>, 670.4697126465132, 41007),
 (<Serializers.cbor2: 9>, 506.5790369865076, 20568),
 (<Serializers.json: 0>, 369.75400375826166, 61194),
 (<Serializers.simplejson: 1>, 248.46085692112078, 61194),
 (<Serializers.msgspec_toml: 39>, 9.70770563116117, 141522),
 (<Serializers.msgspec_yaml: 38>, 1.7382217324525868, 161098)]

        == TestDataType.large: ==
                == current_platform: ==
[(<Serializers.pickle: 16>, 190934.10815977238, 1510),
 (<Serializers.msgspec_messagepack: 37>, 173034.15571178214, 2065),
 (<Serializers.marshal: 10>, 170597.68414362887, 1523),
 (<Serializers.cbor: 8>, 166969.92170431133, 2069),
 (<Serializers.msgspec_json: 36>, 125530.61701910009, 2129),
 (<Serializers.orjson: 3>, 119616.98033754804, 2129),
 (<Serializers.cloudpickle: 30>, 106569.58205548112, 1510),
 (<Serializers.msgpack: 7>, 101018.83494643256, 2065),
 (<Serializers.ujson: 2>, 65793.50785468638, 2129),
 (<Serializers.cbor2: 9>, 46904.41905240339, 2069),
 (<Serializers.json: 0>, 36674.95492233731, 2158),
 (<Serializers.simplejson: 1>, 26944.418767761807, 2158),
 (<Serializers.msgspec_yaml: 38>, 1695.3987813562346, 2172),
 (<Serializers.msgspec_toml: 39>, 1676.006312289766, 2214)]

                == multi_platform: ==
[(<Serializers.msgspec_messagepack: 37>, 172825.27396736614, 2065),
 (<Serializers.cbor: 8>, 165515.7152876797, 2069),
 (<Serializers.msgspec_json: 36>, 125841.4092001172, 2129),
 (<Serializers.orjson: 3>, 121441.68340095853, 2129),
 (<Serializers.msgpack: 7>, 99549.58501761543, 2065),
 (<Serializers.ujson: 2>, 65983.53542321194, 2129),
 (<Serializers.cbor2: 9>, 47226.764925475705, 2069),
 (<Serializers.json: 0>, 36628.820542997615, 2158),
 (<Serializers.simplejson: 1>, 27157.211391572666, 2158),
 (<Serializers.msgspec_toml: 39>, 1693.386750399595, 2214),
 (<Serializers.msgspec_yaml: 38>, 1665.0015733318603, 2172)]

        == TestDataType.deep_large: ==
                == current_platform: ==
[(<Serializers.marshal: 10>, 33104.546387183545, 6783),
 (<Serializers.pickle: 16>, 31936.878980986443, 3614),
 (<Serializers.cloudpickle: 30>, 27591.800746493984, 3614),
 (<Serializers.msgspec_messagepack: 37>, 2944.1671943243978, 33245),
 (<Serializers.orjson: 3>, 2038.2410609754304, 53659),
 (<Serializers.msgspec_json: 36>, 1783.6176260138564, 53659),
 (<Serializers.cbor: 8>, 1126.68784331286, 33284),
 (<Serializers.msgpack: 7>, 1108.62298323295, 33245),
 (<Serializers.ujson: 2>, 637.1769856744611, 53659),
 (<Serializers.cbor2: 9>, 507.5856320617872, 33284),
 (<Serializers.json: 0>, 376.9275158918502, 73846),
 (<Serializers.simplejson: 1>, 252.14744050786814, 73846),
 (<Serializers.msgspec_toml: 39>, 3.8503801350127294, 154174),
 (<Serializers.msgspec_yaml: 38>, 3.5977358430741084, 173930)]

                == multi_platform: ==
[(<Serializers.msgspec_messagepack: 37>, 3012.865134501427, 33245),
 (<Serializers.orjson: 3>, 2069.2444796039354, 53659),
 (<Serializers.msgspec_json: 36>, 1798.4785450763081, 53659),
 (<Serializers.cbor: 8>, 1128.1992990401038, 33284),
 (<Serializers.msgpack: 7>, 1093.7677545388206, 33245),
 (<Serializers.ujson: 2>, 652.6796077023771, 53659),
 (<Serializers.cbor2: 9>, 510.3717110035909, 33284),
 (<Serializers.json: 0>, 380.4518452365029, 73846),
 (<Serializers.simplejson: 1>, 253.57306330991233, 73846),
 (<Serializers.msgspec_toml: 39>, 9.656967307975798, 154174),
 (<Serializers.msgspec_yaml: 38>, 3.4875746096447586, 173930)]

=== RemoteObjectsManager: ==============================================================================
>>> "0, Serializers.pickle, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 467 iterations. Performance: 3736.0 iterations/seconds
         Isolated run time: 0.0001834131544455886 seconds; Isolated performance: 5452.171645064097 iterations/seconds

>>> "0, Serializers.pickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 806 iterations. Performance: 6448.0 iterations/seconds
         Isolated run time: 7.336819544434547e-05 seconds; Isolated performance: 13629.88409274104 iterations/seconds

>>> "0, Serializers.pickle, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 319 iterations. Performance: 5104.0 iterations/seconds
         Isolated run time: 0.000203109928406775 seconds; Isolated performance: 4923.44223566101 iterations/seconds

>>> "0, Serializers.pickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 902 iterations. Performance: 14432.0 iterations/seconds
         Isolated run time: 8.289376273751259e-05 seconds; Isolated performance: 12063.633824495964 iterations/seconds

>>> "0, Serializers.marshal, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 280 iterations. Performance: 4480.0 iterations/seconds
         Isolated run time: 0.00027919828426092863 seconds; Isolated performance: 3581.683901271528 iterations/seconds

>>> "0, Serializers.marshal, universal=False, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 753 iterations. Performance: 4016.0 iterations/seconds
         Isolated run time: 9.49023524299264e-05 seconds; Isolated performance: 10537.146597481615 iterations/seconds

>>> "0, Serializers.marshal, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 120 iterations. Performance: 960.0 iterations/seconds
         Isolated run time: 0.00034549995325505733 seconds; Isolated performance: 2894.356397385018 iterations/seconds

>>> "0, Serializers.marshal, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 258 iterations. Performance: 2064.0 iterations/seconds
         Isolated run time: 0.00013332092203199863 seconds; Isolated performance: 7500.698200691921 iterations/seconds

>>> "0, Serializers.cloudpickle, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 23 iterations. Performance: 368.0 iterations/seconds
         Isolated run time: 0.0009645653190091252 seconds; Isolated performance: 1036.7364244728144 iterations/seconds

>>> "0, Serializers.cloudpickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 39 iterations. Performance: 624.0 iterations/seconds
         Isolated run time: 0.0008087782189249992 seconds; Isolated performance: 1236.4329016292827 iterations/seconds

>>> "0, Serializers.cloudpickle, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0 seconds to make 20 iterations. Performance: 0.0 iterations/seconds
         Isolated run time: 0.0010007052915170789 seconds; Isolated performance: 999.295205568455 iterations/seconds

>>> "0, Serializers.cloudpickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 58 iterations. Performance: 928.0 iterations/seconds
         Isolated run time: 0.000809637364000082 seconds; Isolated performance: 1235.1208633201106 iterations/seconds

>>> "0, Serializers.msgspec_messagepack, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 248 iterations. Performance: 1984.0 iterations/seconds
         Isolated run time: 0.00029303261544555426 seconds; Isolated performance: 3412.589409132858 iterations/seconds

>>> "0, Serializers.msgspec_messagepack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 730 iterations. Performance: 5840.0 iterations/seconds
         Isolated run time: 0.00010432465933263302 seconds; Isolated performance: 9585.461446958183 iterations/seconds

>>> "0, Serializers.msgspec_messagepack, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 117 iterations. Performance: 1872.0 iterations/seconds
         Isolated run time: 0.00038936175405979156 seconds; Isolated performance: 2568.3056683744985 iterations/seconds

>>> "0, Serializers.msgspec_messagepack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 408 iterations. Performance: 6528.0 iterations/seconds
         Isolated run time: 0.00014643033500760794 seconds; Isolated performance: 6829.1860422776745 iterations/seconds

>>> "0, Serializers.orjson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 225 iterations. Performance: 3600.0 iterations/seconds
         Isolated run time: 0.00030604354105889797 seconds; Isolated performance: 3267.508918959836 iterations/seconds

>>> "0, Serializers.orjson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 637 iterations. Performance: 10192.0 iterations/seconds
         Isolated run time: 0.00012120616156607866 seconds; Isolated performance: 8250.405648353317 iterations/seconds

>>> "0, Serializers.orjson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 207 iterations. Performance: 3312.0 iterations/seconds
         Isolated run time: 0.00039742328226566315 seconds; Isolated performance: 2516.2089002413704 iterations/seconds

>>> "0, Serializers.orjson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 512 iterations. Performance: 2730.666748046875 iterations/seconds
         Isolated run time: 0.00016053230501711369 seconds; Isolated performance: 6229.275782798946 iterations/seconds

>>> "0, Serializers.msgspec_json, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 240 iterations. Performance: 1920.0 iterations/seconds
         Isolated run time: 0.0002953372895717621 seconds; Isolated performance: 3385.9591569015756 iterations/seconds

>>> "0, Serializers.msgspec_json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 308 iterations. Performance: 2464.0 iterations/seconds
         Isolated run time: 0.00010849349200725555 seconds; Isolated performance: 9217.142719796728 iterations/seconds

>>> "0, Serializers.msgspec_json, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 67 iterations. Performance: 1072.0 iterations/seconds
         Isolated run time: 0.00038968375883996487 seconds; Isolated performance: 2566.1834174892556 iterations/seconds

>>> "0, Serializers.msgspec_json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 167 iterations. Performance: 2672.0 iterations/seconds
         Isolated run time: 0.00015393621288239956 seconds; Isolated performance: 6496.197231797275 iterations/seconds

>>> "0, Serializers.msgpack, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 80 iterations. Performance: 1280.0 iterations/seconds
         Isolated run time: 0.0003532200353220105 seconds; Isolated performance: 2831.0964837777597 iterations/seconds

>>> "0, Serializers.msgpack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 166 iterations. Performance: 2656.0 iterations/seconds
         Isolated run time: 0.00014411727897822857 seconds; Isolated performance: 6938.793232080571 iterations/seconds

>>> "0, Serializers.msgpack, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 119 iterations. Performance: 952.0 iterations/seconds
         Isolated run time: 0.00046201643999665976 seconds; Isolated performance: 2164.4251447139623 iterations/seconds

>>> "0, Serializers.msgpack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 308 iterations. Performance: 2464.0 iterations/seconds
         Isolated run time: 0.0001977626234292984 seconds; Isolated performance: 5056.567225189078 iterations/seconds

>>> "0, Serializers.cbor, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 180 iterations. Performance: 2880.0 iterations/seconds
         Isolated run time: 0.0002851752797141671 seconds; Isolated performance: 3506.6153034102604 iterations/seconds

>>> "0, Serializers.cbor, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 809 iterations. Performance: 6472.0 iterations/seconds
         Isolated run time: 9.429233614355326e-05 seconds; Isolated performance: 10605.31577537301 iterations/seconds

>>> "0, Serializers.cbor, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 192 iterations. Performance: 1536.0 iterations/seconds
         Isolated run time: 0.0003681381931528449 seconds; Isolated performance: 2716.3712393862284 iterations/seconds

>>> "0, Serializers.cbor, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 579 iterations. Performance: 4632.0 iterations/seconds
         Isolated run time: 0.00013541383668780327 seconds; Isolated performance: 7384.769713788562 iterations/seconds

>>> "0, Serializers.ujson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 220 iterations. Performance: 3520.0 iterations/seconds
         Isolated run time: 0.000342061510309577 seconds; Isolated performance: 2923.4508117998043 iterations/seconds

>>> "0, Serializers.ujson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 569 iterations. Performance: 9104.0 iterations/seconds
         Isolated run time: 0.00013489823322743177 seconds; Isolated performance: 7412.995530594158 iterations/seconds

>>> "0, Serializers.ujson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 174 iterations. Performance: 1392.0 iterations/seconds
         Isolated run time: 0.0004301929147914052 seconds; Isolated performance: 2324.538516597575 iterations/seconds

>>> "0, Serializers.ujson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 370 iterations. Performance: 5920.0 iterations/seconds
         Isolated run time: 0.00018362945411354303 seconds; Isolated performance: 5445.749456847338 iterations/seconds

>>> "0, Serializers.cbor2, universal=False, optimized=False": benchmark_single_item()
         It was used 0.25 seconds to make 177 iterations. Performance: 708.0 iterations/seconds
         Isolated run time: 0.0004670838825404644 seconds; Isolated performance: 2140.943066930527 iterations/seconds

>>> "0, Serializers.cbor2, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 134 iterations. Performance: 2144.0 iterations/seconds
         Isolated run time: 0.00022884819190949202 seconds; Isolated performance: 4369.7089833049395 iterations/seconds

>>> "0, Serializers.cbor2, universal=True, optimized=False": benchmark_single_item()
         It was used 0.1875 seconds to make 64 iterations. Performance: 341.3333435058594 iterations/seconds
         Isolated run time: 0.0005759852938354015 seconds; Isolated performance: 1736.155437825759 iterations/seconds

>>> "0, Serializers.cbor2, universal=True, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 94 iterations. Performance: 501.3333435058594 iterations/seconds
         Isolated run time: 0.0002963055158033967 seconds; Isolated performance: 3374.894987319492 iterations/seconds

>>> "0, Serializers.json, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 34 iterations. Performance: 544.0 iterations/seconds
         Isolated run time: 0.0004683182341977954 seconds; Isolated performance: 2135.3001591171173 iterations/seconds

>>> "0, Serializers.json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 248 iterations. Performance: 3968.0 iterations/seconds
         Isolated run time: 0.00021067564375698566 seconds; Isolated performance: 4746.633175847797 iterations/seconds

>>> "0, Serializers.json, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 140 iterations. Performance: 1120.0 iterations/seconds
         Isolated run time: 0.0005267688538879156 seconds; Isolated performance: 1898.3658441825362 iterations/seconds

>>> "0, Serializers.json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 312 iterations. Performance: 2496.0 iterations/seconds
         Isolated run time: 0.0002622593892738223 seconds; Isolated performance: 3813.018869482344 iterations/seconds

>>> "0, Serializers.simplejson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 151 iterations. Performance: 1208.0 iterations/seconds
         Isolated run time: 0.0004905564710497856 seconds; Isolated performance: 2038.5012919307958 iterations/seconds

>>> "0, Serializers.simplejson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 308 iterations. Performance: 2464.0 iterations/seconds
         Isolated run time: 0.0002508644247427583 seconds; Isolated performance: 3986.216862057748 iterations/seconds

>>> "0, Serializers.simplejson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 120 iterations. Performance: 1920.0 iterations/seconds
         Isolated run time: 0.0005969795165583491 seconds; Isolated performance: 1675.099349748392 iterations/seconds

>>> "0, Serializers.simplejson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 237 iterations. Performance: 3792.0 iterations/seconds
         Isolated run time: 0.00032627733889967203 seconds; Isolated performance: 3064.8772708897595 iterations/seconds

>>> "0, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 25 iterations. Performance: 400.0 iterations/seconds
         Isolated run time: 0.003393023507669568 seconds; Isolated performance: 294.72239073487304 iterations/seconds

>>> "0, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 28 iterations. Performance: 448.0 iterations/seconds
         Isolated run time: 0.0030945788603276014 seconds; Isolated performance: 323.14574781724485 iterations/seconds

>>> "0, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.25 seconds to make 24 iterations. Performance: 96.0 iterations/seconds
         Isolated run time: 0.003521644393913448 seconds; Isolated performance: 283.95825590122803 iterations/seconds

>>> "0, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 5 iterations. Performance: 80.0 iterations/seconds
         Isolated run time: 0.0032367882085964084 seconds; Isolated performance: 308.9482337287793 iterations/seconds

>>> "0, Serializers.msgspec_yaml, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 9 iterations. Performance: 72.0 iterations/seconds
         Isolated run time: 0.002479569986462593 seconds; Isolated performance: 403.2957349296767 iterations/seconds

>>> "0, Serializers.msgspec_yaml, universal=False, optimized=True": benchmark_single_item()
         It was used 0.3125 seconds to make 16 iterations. Performance: 51.20000076293945 iterations/seconds
         Isolated run time: 0.0021532500395551324 seconds; Isolated performance: 464.4142489864312 iterations/seconds

>>> "0, Serializers.msgspec_yaml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 7 iterations. Performance: 112.0 iterations/seconds
         Isolated run time: 0.002588706207461655 seconds; Isolated performance: 386.29335268622305 iterations/seconds

>>> "0, Serializers.msgspec_yaml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 9 iterations. Performance: 144.0 iterations/seconds
         Isolated run time: 0.002432446461170912 seconds; Isolated performance: 411.10874009478835 iterations/seconds

>>> "1, Serializers.pickle, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 72 iterations. Performance: 1152.0 iterations/seconds
         Isolated run time: 0.0009546343935653567 seconds; Isolated performance: 1047.5214456345034 iterations/seconds

>>> "1, Serializers.pickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 300 iterations. Performance: 4800.0 iterations/seconds
         Isolated run time: 0.00026777759194374084 seconds; Isolated performance: 3734.4424256757698 iterations/seconds

>>> "1, Serializers.pickle, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 79 iterations. Performance: 1264.0 iterations/seconds
         Isolated run time: 0.0010393587872385979 seconds; Isolated performance: 962.1316645206151 iterations/seconds

>>> "1, Serializers.pickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 213 iterations. Performance: 1136.0 iterations/seconds
         Isolated run time: 0.00033541698940098286 seconds; Isolated performance: 2981.363590991285 iterations/seconds

>>> "1, Serializers.marshal, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 92 iterations. Performance: 736.0 iterations/seconds
         Isolated run time: 0.0008738852338865399 seconds; Isolated performance: 1144.3150212672367 iterations/seconds

>>> "1, Serializers.marshal, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 324 iterations. Performance: 2592.0 iterations/seconds
         Isolated run time: 0.00024461117573082447 seconds; Isolated performance: 4088.1206552084195 iterations/seconds

>>> "1, Serializers.marshal, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 80 iterations. Performance: 640.0 iterations/seconds
         Isolated run time: 0.001004255609586835 seconds; Isolated performance: 995.7624238827148 iterations/seconds

>>> "1, Serializers.marshal, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 254 iterations. Performance: 2032.0 iterations/seconds
         Isolated run time: 0.0003241718513891101 seconds; Isolated performance: 3084.783566848559 iterations/seconds

>>> "1, Serializers.cloudpickle, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 49 iterations. Performance: 784.0 iterations/seconds
         Isolated run time: 0.0011648143408820033 seconds; Isolated performance: 858.5059136916145 iterations/seconds

>>> "1, Serializers.cloudpickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 141 iterations. Performance: 2256.0 iterations/seconds
         Isolated run time: 0.00044131441973149776 seconds; Isolated performance: 2265.9581361706123 iterations/seconds

>>> "1, Serializers.cloudpickle, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 21 iterations. Performance: 168.0 iterations/seconds
         Isolated run time: 0.0013081773649901152 seconds; Isolated performance: 764.4223381036379 iterations/seconds

>>> "1, Serializers.cloudpickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 52 iterations. Performance: 416.0 iterations/seconds
         Isolated run time: 0.000516214407980442 seconds; Isolated performance: 1937.1795605478087 iterations/seconds

>>> "1, Serializers.msgspec_messagepack, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 26 iterations. Performance: 416.0 iterations/seconds
         Isolated run time: 0.0009556435979902744 seconds; Isolated performance: 1046.4152138966947 iterations/seconds

>>> "1, Serializers.msgspec_messagepack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 127 iterations. Performance: 1016.0 iterations/seconds
         Isolated run time: 0.0002761061768978834 seconds; Isolated performance: 3621.7951051846453 iterations/seconds

>>> "1, Serializers.msgspec_messagepack, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 32 iterations. Performance: 512.0 iterations/seconds
         Isolated run time: 0.001175507321022451 seconds; Isolated performance: 850.6965308648223 iterations/seconds

>>> "1, Serializers.msgspec_messagepack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 198 iterations. Performance: 3168.0 iterations/seconds
         Isolated run time: 0.0003644721582531929 seconds; Isolated performance: 2743.693797607762 iterations/seconds

>>> "1, Serializers.orjson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 81 iterations. Performance: 1296.0 iterations/seconds
         Isolated run time: 0.0009439929854124784 seconds; Isolated performance: 1059.3299054685765 iterations/seconds

>>> "1, Serializers.orjson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 222 iterations. Performance: 3552.0 iterations/seconds
         Isolated run time: 0.0003190835705026984 seconds; Isolated performance: 3133.975210395683 iterations/seconds

>>> "1, Serializers.orjson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 70 iterations. Performance: 560.0 iterations/seconds
         Isolated run time: 0.0011906579602509737 seconds; Isolated performance: 839.8717628270123 iterations/seconds

>>> "1, Serializers.orjson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 187 iterations. Performance: 1496.0 iterations/seconds
         Isolated run time: 0.00042399822268635035 seconds; Isolated performance: 2358.5004523468083 iterations/seconds

>>> "1, Serializers.msgspec_json, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 47 iterations. Performance: 376.0 iterations/seconds
         Isolated run time: 0.0009392470819875598 seconds; Isolated performance: 1064.68257307106 iterations/seconds

>>> "1, Serializers.msgspec_json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 104 iterations. Performance: 1664.0 iterations/seconds
         Isolated run time: 0.0002915408695116639 seconds; Isolated performance: 3430.050825035329 iterations/seconds

>>> "1, Serializers.msgspec_json, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 49 iterations. Performance: 784.0 iterations/seconds
         Isolated run time: 0.0011826191330328584 seconds; Isolated performance: 845.5807724296437 iterations/seconds

>>> "1, Serializers.msgspec_json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 194 iterations. Performance: 3104.0 iterations/seconds
         Isolated run time: 0.00038168265018612146 seconds; Isolated performance: 2619.977616253623 iterations/seconds

>>> "1, Serializers.msgpack, universal=False, optimized=False": benchmark_single_item()
         It was used 0.1875 seconds to make 71 iterations. Performance: 378.6666564941406 iterations/seconds
         Isolated run time: 0.0011190255172550678 seconds; Isolated performance: 893.6346710421461 iterations/seconds

>>> "1, Serializers.msgpack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 79 iterations. Performance: 1264.0 iterations/seconds
         Isolated run time: 0.0004037108737975359 seconds; Isolated performance: 2477.020226365039 iterations/seconds

>>> "1, Serializers.msgpack, universal=True, optimized=False": benchmark_single_item()
         It was used 0.1875 seconds to make 30 iterations. Performance: 160.0 iterations/seconds
         Isolated run time: 0.001356341759674251 seconds; Isolated performance: 737.2773070410863 iterations/seconds

>>> "1, Serializers.msgpack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 64 iterations. Performance: 512.0 iterations/seconds
         Isolated run time: 0.0005239835008978844 seconds; Isolated performance: 1908.457037838837 iterations/seconds

>>> "1, Serializers.cbor, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 38 iterations. Performance: 608.0 iterations/seconds
         Isolated run time: 0.0009128217352554202 seconds; Isolated performance: 1095.5041508955592 iterations/seconds

>>> "1, Serializers.cbor, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 231 iterations. Performance: 3696.0 iterations/seconds
         Isolated run time: 0.0002509981859475374 seconds; Isolated performance: 3984.09253925451 iterations/seconds

>>> "1, Serializers.cbor, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 73 iterations. Performance: 1168.0 iterations/seconds
         Isolated run time: 0.0011106852907687426 seconds; Isolated performance: 900.3450467124368 iterations/seconds

>>> "1, Serializers.cbor, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 230 iterations. Performance: 3680.0 iterations/seconds
         Isolated run time: 0.00035373587161302567 seconds; Isolated performance: 2826.9680296771376 iterations/seconds

>>> "1, Serializers.ujson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 72 iterations. Performance: 576.0 iterations/seconds
         Isolated run time: 0.0011190208606421947 seconds; Isolated performance: 893.638389749151 iterations/seconds

>>> "1, Serializers.ujson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 120 iterations. Performance: 1920.0 iterations/seconds
         Isolated run time: 0.00039715098682790995 seconds; Isolated performance: 2517.934068317729 iterations/seconds

>>> "1, Serializers.ujson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 47 iterations. Performance: 752.0 iterations/seconds
         Isolated run time: 0.0013407926307991147 seconds; Isolated performance: 745.8274881806282 iterations/seconds

>>> "1, Serializers.ujson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 164 iterations. Performance: 1312.0 iterations/seconds
         Isolated run time: 0.00048516003880649805 seconds; Isolated performance: 2061.1755297489403 iterations/seconds

>>> "1, Serializers.cbor2, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 43 iterations. Performance: 688.0 iterations/seconds
         Isolated run time: 0.0014563153963536024 seconds; Isolated performance: 686.6644426776312 iterations/seconds

>>> "1, Serializers.cbor2, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 113 iterations. Performance: 1808.0 iterations/seconds
         Isolated run time: 0.0006705425912514329 seconds; Isolated performance: 1491.3295785338573 iterations/seconds

>>> "1, Serializers.cbor2, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 48 iterations. Performance: 768.0 iterations/seconds
         Isolated run time: 0.0017144567100331187 seconds; Isolated performance: 583.2751530837327 iterations/seconds

>>> "1, Serializers.cbor2, universal=True, optimized=True": benchmark_single_item()
         It was used 0.25 seconds to make 92 iterations. Performance: 368.0 iterations/seconds
         Isolated run time: 0.0008201336022466421 seconds; Isolated performance: 1219.3135328934686 iterations/seconds

>>> "1, Serializers.json, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 25 iterations. Performance: 200.0 iterations/seconds
         Isolated run time: 0.001406296156346798 seconds; Isolated performance: 711.0877715813057 iterations/seconds

>>> "1, Serializers.json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 51 iterations. Performance: 408.0 iterations/seconds
         Isolated run time: 0.0006108682136982679 seconds; Isolated performance: 1637.0142979708871 iterations/seconds

>>> "1, Serializers.json, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 24 iterations. Performance: 192.0 iterations/seconds
         Isolated run time: 0.0016489065019413829 seconds; Isolated performance: 606.4625246019856 iterations/seconds

>>> "1, Serializers.json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 104 iterations. Performance: 832.0 iterations/seconds
         Isolated run time: 0.0007339473813772202 seconds; Isolated performance: 1362.4954940550967 iterations/seconds

>>> "1, Serializers.simplejson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.1875 seconds to make 48 iterations. Performance: 256.0 iterations/seconds
         Isolated run time: 0.0016583251999691129 seconds; Isolated performance: 603.0180329036943 iterations/seconds

>>> "1, Serializers.simplejson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 58 iterations. Performance: 928.0 iterations/seconds
         Isolated run time: 0.0007930290885269642 seconds; Isolated performance: 1260.987792840588 iterations/seconds

>>> "1, Serializers.simplejson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 40 iterations. Performance: 640.0 iterations/seconds
         Isolated run time: 0.001872990862466395 seconds; Isolated performance: 533.9054343720494 iterations/seconds

>>> "1, Serializers.simplejson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 86 iterations. Performance: 1376.0 iterations/seconds
         Isolated run time: 0.0009480114094913006 seconds; Isolated performance: 1054.8396253338303 iterations/seconds

>>> "1, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 9 iterations. Performance: 72.0 iterations/seconds
         Isolated run time: 0.010711060022003949 seconds; Isolated performance: 93.36144115948184 iterations/seconds

>>> "1, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 10 iterations. Performance: 80.0 iterations/seconds
         Isolated run time: 0.009574580006301403 seconds; Isolated performance: 104.44322355047022 iterations/seconds

>>> "1, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 9 iterations. Performance: 72.0 iterations/seconds
         Isolated run time: 0.010576286120340228 seconds; Isolated performance: 94.55114854323088 iterations/seconds

>>> "1, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 8 iterations. Performance: 128.0 iterations/seconds
         Isolated run time: 0.009896122966893017 seconds; Isolated performance: 101.0496740335028 iterations/seconds

>>> "1, Serializers.msgspec_yaml, universal=False, optimized=False": benchmark_single_item()
         It was used 0.1875 seconds to make 11 iterations. Performance: 58.66666793823242 iterations/seconds
         Isolated run time: 0.007604103768244386 seconds; Isolated performance: 131.5079370926151 iterations/seconds

>>> "1, Serializers.msgspec_yaml, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 6 iterations. Performance: 48.0 iterations/seconds
         Isolated run time: 0.006354549084790051 seconds; Isolated performance: 157.3675781958397 iterations/seconds

>>> "1, Serializers.msgspec_yaml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 4 iterations. Performance: 32.0 iterations/seconds
         Isolated run time: 0.018666955991648138 seconds; Isolated performance: 53.5705982511243 iterations/seconds

>>> "1, Serializers.msgspec_yaml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 6 iterations. Performance: 48.0 iterations/seconds
         Isolated run time: 0.017257233150303364 seconds; Isolated performance: 57.9467166776049 iterations/seconds

>>> "2, Serializers.pickle, universal=False, optimized=False": benchmark_single_item()
         It was used 1.0 seconds to make 2 iterations. Performance: 2.0 iterations/seconds
         Isolated run time: 0.5022151184966788 seconds; Isolated performance: 1.9911786068754382 iterations/seconds

>>> "2, Serializers.pickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.3125 seconds to make 2 iterations. Performance: 6.400000095367432 iterations/seconds
         Isolated run time: 0.12391539907548577 seconds; Isolated performance: 8.070022026809019 iterations/seconds

>>> "2, Serializers.pickle, universal=True, optimized=False": benchmark_single_item()
         It was used 1.125 seconds to make 2 iterations. Performance: 1.7777777910232544 iterations/seconds
         Isolated run time: 0.5377957853488624 seconds; Isolated performance: 1.8594418685362337 iterations/seconds

>>> "2, Serializers.pickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.4375 seconds to make 2 iterations. Performance: 4.5714287757873535 iterations/seconds
         Isolated run time: 0.17831924592610449 seconds; Isolated performance: 5.60791963204241 iterations/seconds

>>> "2, Serializers.marshal, universal=False, optimized=False": benchmark_single_item()
         It was used 0.9375 seconds to make 2 iterations. Performance: 2.133333444595337 iterations/seconds
         Isolated run time: 0.460874967626296 seconds; Isolated performance: 2.1697858860732433 iterations/seconds

>>> "2, Serializers.marshal, universal=False, optimized=True": benchmark_single_item()
         It was used 0.25 seconds to make 2 iterations. Performance: 8.0 iterations/seconds
         Isolated run time: 0.11946129298303276 seconds; Isolated performance: 8.370912243031148 iterations/seconds

>>> "2, Serializers.marshal, universal=True, optimized=False": benchmark_single_item()
         It was used 1.4375 seconds to make 2 iterations. Performance: 1.39130437374115 iterations/seconds
         Isolated run time: 0.5199124306673184 seconds; Isolated performance: 1.9234008287058635 iterations/seconds

>>> "2, Serializers.marshal, universal=True, optimized=True": benchmark_single_item()
         It was used 0.3125 seconds to make 2 iterations. Performance: 6.400000095367432 iterations/seconds
         Isolated run time: 0.16109416785184294 seconds; Isolated performance: 6.207549369010629 iterations/seconds

>>> "2, Serializers.cloudpickle, universal=False, optimized=False": benchmark_single_item()
         It was used 1.625 seconds to make 2 iterations. Performance: 1.2307692766189575 iterations/seconds
         Isolated run time: 0.6090845946455374 seconds; Isolated performance: 1.64180806540011 iterations/seconds

>>> "2, Serializers.cloudpickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.4375 seconds to make 2 iterations. Performance: 4.5714287757873535 iterations/seconds
         Isolated run time: 0.22295786056201905 seconds; Isolated performance: 4.485152474459787 iterations/seconds

>>> "2, Serializers.cloudpickle, universal=True, optimized=False": benchmark_single_item()
         It was used 1.375 seconds to make 2 iterations. Performance: 1.454545497894287 iterations/seconds
         Isolated run time: 0.6760296956636012 seconds; Isolated performance: 1.4792249606999655 iterations/seconds

>>> "2, Serializers.cloudpickle, universal=True, optimized=True": benchmark_single_item()
         It was used 1.125 seconds to make 2 iterations. Performance: 1.7777777910232544 iterations/seconds
         Isolated run time: 0.33317210560198873 seconds; Isolated performance: 3.0014517517700345 iterations/seconds

>>> "2, Serializers.msgspec_messagepack, universal=False, optimized=False": benchmark_single_item()
         It was used 0.9375 seconds to make 2 iterations. Performance: 2.133333444595337 iterations/seconds
         Isolated run time: 0.5099748648935929 seconds; Isolated performance: 1.960880954806766 iterations/seconds

>>> "2, Serializers.msgspec_messagepack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.5625 seconds to make 2 iterations. Performance: 3.555555582046509 iterations/seconds
         Isolated run time: 0.28735903825145215 seconds; Isolated performance: 3.479967103470589 iterations/seconds

>>> "2, Serializers.msgspec_messagepack, universal=True, optimized=False": benchmark_single_item()
         It was used 1.375 seconds to make 2 iterations. Performance: 1.454545497894287 iterations/seconds
         Isolated run time: 0.5974392096977681 seconds; Isolated performance: 1.6738104626676227 iterations/seconds

>>> "2, Serializers.msgspec_messagepack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.4375 seconds to make 2 iterations. Performance: 4.5714287757873535 iterations/seconds
         Isolated run time: 0.2062522917985916 seconds; Isolated performance: 4.848430973928351 iterations/seconds

>>> "2, Serializers.orjson, universal=False, optimized=False": benchmark_single_item()
         It was used 1.4375 seconds to make 2 iterations. Performance: 1.39130437374115 iterations/seconds
         Isolated run time: 0.5589153388282284 seconds; Isolated performance: 1.7891797389145017 iterations/seconds

>>> "2, Serializers.orjson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.375 seconds to make 2 iterations. Performance: 5.333333492279053 iterations/seconds
         Isolated run time: 0.15285868174396455 seconds; Isolated performance: 6.541990213385337 iterations/seconds

>>> "2, Serializers.orjson, universal=True, optimized=False": benchmark_single_item()
         It was used 1.625 seconds to make 2 iterations. Performance: 1.2307692766189575 iterations/seconds
         Isolated run time: 0.7641987149836496 seconds; Isolated performance: 1.3085601694860158 iterations/seconds

>>> "2, Serializers.orjson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.4375 seconds to make 2 iterations. Performance: 4.5714287757873535 iterations/seconds
         Isolated run time: 0.22661597828846425 seconds; Isolated performance: 4.412751508311912 iterations/seconds

>>> "2, Serializers.msgspec_json, universal=False, optimized=False": benchmark_single_item()
         It was used 1.5 seconds to make 2 iterations. Performance: 1.3333333730697632 iterations/seconds
         Isolated run time: 0.48804765148088336 seconds; Isolated performance: 2.048980252165335 iterations/seconds

>>> "2, Serializers.msgspec_json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.25 seconds to make 2 iterations. Performance: 8.0 iterations/seconds
         Isolated run time: 0.13028478005435318 seconds; Isolated performance: 7.6754936346579585 iterations/seconds

>>> "2, Serializers.msgspec_json, universal=True, optimized=False": benchmark_single_item()
         It was used 2.125 seconds to make 2 iterations. Performance: 0.9411764740943909 iterations/seconds
         Isolated run time: 0.8756131221307442 seconds; Isolated performance: 1.1420568910234796 iterations/seconds

>>> "2, Serializers.msgspec_json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.6875 seconds to make 2 iterations. Performance: 2.909090995788574 iterations/seconds
         Isolated run time: 0.28628140152432024 seconds; Isolated performance: 3.4930665934826637 iterations/seconds

>>> "2, Serializers.msgpack, universal=False, optimized=False": benchmark_single_item()
         It was used 1.4375 seconds to make 2 iterations. Performance: 1.39130437374115 iterations/seconds
         Isolated run time: 0.5787786958971992 seconds; Isolated performance: 1.7277761035240604 iterations/seconds

>>> "2, Serializers.msgpack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.375 seconds to make 2 iterations. Performance: 5.333333492279053 iterations/seconds
         Isolated run time: 0.19261701474897563 seconds; Isolated performance: 5.19164935300877 iterations/seconds

>>> "2, Serializers.msgpack, universal=True, optimized=False": benchmark_single_item()
         It was used 1.875 seconds to make 2 iterations. Performance: 1.0666667222976685 iterations/seconds
         Isolated run time: 0.8193171782186255 seconds; Isolated performance: 1.2205285408200746 iterations/seconds

>>> "2, Serializers.msgpack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.75 seconds to make 2 iterations. Performance: 2.6666667461395264 iterations/seconds
         Isolated run time: 0.27385796268936247 seconds; Isolated performance: 3.651527931412758 iterations/seconds

>>> "2, Serializers.cbor, universal=False, optimized=False": benchmark_single_item()
         It was used 1.0 seconds to make 2 iterations. Performance: 2.0 iterations/seconds
         Isolated run time: 0.47540723998099566 seconds; Isolated performance: 2.103459762287118 iterations/seconds

>>> "2, Serializers.cbor, universal=False, optimized=True": benchmark_single_item()
         It was used 0.25 seconds to make 2 iterations. Performance: 8.0 iterations/seconds
         Isolated run time: 0.121816131984815 seconds; Isolated performance: 8.20909335821511 iterations/seconds

>>> "2, Serializers.cbor, universal=True, optimized=False": benchmark_single_item()
         It was used 1.5 seconds to make 2 iterations. Performance: 1.3333333730697632 iterations/seconds
         Isolated run time: 0.6656691533280537 seconds; Isolated performance: 1.5022477682801416 iterations/seconds

>>> "2, Serializers.cbor, universal=True, optimized=True": benchmark_single_item()
         It was used 0.4375 seconds to make 2 iterations. Performance: 4.5714287757873535 iterations/seconds
         Isolated run time: 0.1861636770190671 seconds; Isolated performance: 5.371617149018704 iterations/seconds

>>> "2, Serializers.ujson, universal=False, optimized=False": benchmark_single_item()
         It was used 1.3125 seconds to make 2 iterations. Performance: 1.523809552192688 iterations/seconds
         Isolated run time: 0.5866693102288991 seconds; Isolated performance: 1.7045377737755412 iterations/seconds

>>> "2, Serializers.ujson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.75 seconds to make 2 iterations. Performance: 2.6666667461395264 iterations/seconds
         Isolated run time: 0.34915750881191343 seconds; Isolated performance: 2.864036931076533 iterations/seconds

>>> "2, Serializers.ujson, universal=True, optimized=False": benchmark_single_item()
         It was used 1.875 seconds to make 2 iterations. Performance: 1.0666667222976685 iterations/seconds
         Isolated run time: 0.7067091644275934 seconds; Isolated performance: 1.4150092433143424 iterations/seconds

>>> "2, Serializers.ujson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.5 seconds to make 2 iterations. Performance: 4.0 iterations/seconds
         Isolated run time: 0.25753942085430026 seconds; Isolated performance: 3.8829007096577173 iterations/seconds

>>> "2, Serializers.cbor2, universal=False, optimized=False": benchmark_single_item()
         It was used 2.25 seconds to make 2 iterations. Performance: 0.8888888955116272 iterations/seconds
         Isolated run time: 0.775465484475717 seconds; Isolated performance: 1.289548045682637 iterations/seconds

>>> "2, Serializers.cbor2, universal=False, optimized=True": benchmark_single_item()
         It was used 1.0625 seconds to make 2 iterations. Performance: 1.8823529481887817 iterations/seconds
         Isolated run time: 0.35862102976534516 seconds; Isolated performance: 2.788458893931361 iterations/seconds

>>> "2, Serializers.cbor2, universal=True, optimized=False": benchmark_single_item()
         It was used 2.4375 seconds to make 2 iterations. Performance: 0.8205128312110901 iterations/seconds
         Isolated run time: 1.1313045650022104 seconds; Isolated performance: 0.8839352645925601 iterations/seconds

>>> "2, Serializers.cbor2, universal=True, optimized=True": benchmark_single_item()
         It was used 1.4375 seconds to make 2 iterations. Performance: 1.39130437374115 iterations/seconds
         Isolated run time: 0.6907723450567573 seconds; Isolated performance: 1.4476549432763337 iterations/seconds

>>> "2, Serializers.json, universal=False, optimized=False": benchmark_single_item()
         It was used 2.0625 seconds to make 2 iterations. Performance: 0.9696969985961914 iterations/seconds
         Isolated run time: 0.9145890267100185 seconds; Isolated performance: 1.093387270998892 iterations/seconds

>>> "2, Serializers.json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.8125 seconds to make 2 iterations. Performance: 2.461538553237915 iterations/seconds
         Isolated run time: 0.36542105965781957 seconds; Isolated performance: 2.736569153776743 iterations/seconds

>>> "2, Serializers.json, universal=True, optimized=False": benchmark_single_item()
         It was used 2.5625 seconds to make 2 iterations. Performance: 0.7804877758026123 iterations/seconds
         Isolated run time: 1.2702240427024662 seconds; Isolated performance: 0.7872626925502443 iterations/seconds

>>> "2, Serializers.json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.875 seconds to make 2 iterations. Performance: 2.2857143878936768 iterations/seconds
         Isolated run time: 0.429611632716842 seconds; Isolated performance: 2.327683712091433 iterations/seconds

>>> "2, Serializers.simplejson, universal=False, optimized=False": benchmark_single_item()
         It was used 2.125 seconds to make 2 iterations. Performance: 0.9411764740943909 iterations/seconds
         Isolated run time: 0.9750255715334788 seconds; Isolated performance: 1.025614126640025 iterations/seconds

>>> "2, Serializers.simplejson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.8125 seconds to make 2 iterations. Performance: 2.461538553237915 iterations/seconds
         Isolated run time: 0.39635030389763415 seconds; Isolated performance: 2.523020646549753 iterations/seconds

>>> "2, Serializers.simplejson, universal=True, optimized=False": benchmark_single_item()
         It was used 2.375 seconds to make 2 iterations. Performance: 0.8421052694320679 iterations/seconds
         Isolated run time: 1.1118466834304854 seconds; Isolated performance: 0.8994045805979344 iterations/seconds

>>> "2, Serializers.simplejson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.9375 seconds to make 2 iterations. Performance: 2.133333444595337 iterations/seconds
         Isolated run time: 0.491249602753669 seconds; Isolated performance: 2.035625055765058 iterations/seconds

>>> "2, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 15.25 seconds to make 2 iterations. Performance: 0.13114753365516663 iterations/seconds
         Isolated run time: 7.206329262349755 seconds; Isolated performance: 0.1387669038694371 iterations/seconds

>>> "2, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 14.4375 seconds to make 2 iterations. Performance: 0.13852813839912415 iterations/seconds
         Isolated run time: 6.958145896438509 seconds; Isolated performance: 0.14371644614578213 iterations/seconds

>>> "2, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 15.1875 seconds to make 2 iterations. Performance: 0.1316872388124466 iterations/seconds
         Isolated run time: 7.588306611753069 seconds; Isolated performance: 0.1317817071929013 iterations/seconds

>>> "2, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 13.5625 seconds to make 2 iterations. Performance: 0.14746543765068054 iterations/seconds
         Isolated run time: 6.7225086621474475 seconds; Isolated performance: 0.14875399203733544 iterations/seconds

>>> "2, Serializers.msgspec_yaml, universal=False, optimized=False": benchmark_single_item()
         It was used 10.375 seconds to make 2 iterations. Performance: 0.1927710771560669 iterations/seconds
         Isolated run time: 4.924173068720847 seconds; Isolated performance: 0.20307978335533403 iterations/seconds

>>> "2, Serializers.msgspec_yaml, universal=False, optimized=True": benchmark_single_item()
         It was used 8.75 seconds to make 2 iterations. Performance: 0.22857142984867096 iterations/seconds
         Isolated run time: 4.197006570524536 seconds; Isolated performance: 0.23826505467562833 iterations/seconds

>>> "2, Serializers.msgspec_yaml, universal=True, optimized=False": benchmark_single_item()
         It was used 11.25 seconds to make 2 iterations. Performance: 0.17777778208255768 iterations/seconds
         Isolated run time: 5.406866392004304 seconds; Isolated performance: 0.1849500112447395 iterations/seconds

>>> "2, Serializers.msgspec_yaml, universal=True, optimized=True": benchmark_single_item()
         It was used 8.875 seconds to make 2 iterations. Performance: 0.22535210847854614 iterations/seconds
         Isolated run time: 4.063727087341249 seconds; Isolated performance: 0.2460795172773928 iterations/seconds

>>> "3, Serializers.pickle, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 44 iterations. Performance: 352.0 iterations/seconds
         Isolated run time: 0.0009741991525515914 seconds; Isolated performance: 1026.4841612526882 iterations/seconds

>>> "3, Serializers.pickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 132 iterations. Performance: 1056.0 iterations/seconds
         Isolated run time: 0.00028433557599782944 seconds; Isolated performance: 3516.9710877390658 iterations/seconds

>>> "3, Serializers.pickle, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 33 iterations. Performance: 528.0 iterations/seconds
         Isolated run time: 0.0010505190584808588 seconds; Isolated performance: 951.9103836593753 iterations/seconds

>>> "3, Serializers.pickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 78 iterations. Performance: 624.0 iterations/seconds
         Isolated run time: 0.00034813350066542625 seconds; Isolated performance: 2872.4612773220297 iterations/seconds

>>> "3, Serializers.marshal, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 32 iterations. Performance: 512.0 iterations/seconds
         Isolated run time: 0.0009413791121914983 seconds; Isolated performance: 1062.2712858712514 iterations/seconds

>>> "3, Serializers.marshal, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 202 iterations. Performance: 3232.0 iterations/seconds
         Isolated run time: 0.0002654308918863535 seconds; Isolated performance: 3767.4589905238254 iterations/seconds

>>> "3, Serializers.marshal, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 86 iterations. Performance: 688.0 iterations/seconds
         Isolated run time: 0.001018302864395082 seconds; Isolated performance: 982.0261092892489 iterations/seconds

>>> "3, Serializers.marshal, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 232 iterations. Performance: 1856.0 iterations/seconds
         Isolated run time: 0.0003309190506115556 seconds; Isolated performance: 3021.887069215109 iterations/seconds

>>> "3, Serializers.cloudpickle, universal=False, optimized=False": benchmark_single_item()
         It was used 0.1875 seconds to make 54 iterations. Performance: 288.0 iterations/seconds
         Isolated run time: 0.0012025764444842935 seconds; Isolated performance: 831.5479690181647 iterations/seconds

>>> "3, Serializers.cloudpickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0 seconds to make 94 iterations. Performance: 0.0 iterations/seconds
         Isolated run time: 0.00043648004066199064 seconds; Isolated performance: 2291.0555050428943 iterations/seconds

>>> "3, Serializers.cloudpickle, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 57 iterations. Performance: 912.0 iterations/seconds
         Isolated run time: 0.0012519018491730094 seconds; Isolated performance: 798.7846656353989 iterations/seconds

>>> "3, Serializers.cloudpickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 166 iterations. Performance: 1328.0 iterations/seconds
         Isolated run time: 0.000509957317262888 seconds; Isolated performance: 1960.9484287181829 iterations/seconds

>>> "3, Serializers.msgspec_messagepack, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 80 iterations. Performance: 640.0 iterations/seconds
         Isolated run time: 0.0009569708490744233 seconds; Isolated performance: 1044.9639097859608 iterations/seconds

>>> "3, Serializers.msgspec_messagepack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 175 iterations. Performance: 1400.0 iterations/seconds
         Isolated run time: 0.00028498563915491104 seconds; Isolated performance: 3508.9487419975753 iterations/seconds

>>> "3, Serializers.msgspec_messagepack, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 32 iterations. Performance: 256.0 iterations/seconds
         Isolated run time: 0.001183779095299542 seconds; Isolated performance: 844.7522041660663 iterations/seconds

>>> "3, Serializers.msgspec_messagepack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0 seconds to make 49 iterations. Performance: 0.0 iterations/seconds
         Isolated run time: 0.00039030739571899176 seconds; Isolated performance: 2562.083145152511 iterations/seconds

>>> "3, Serializers.orjson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 27 iterations. Performance: 216.0 iterations/seconds
         Isolated run time: 0.0010253782384097576 seconds; Isolated performance: 975.2498761343752 iterations/seconds

>>> "3, Serializers.orjson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 95 iterations. Performance: 1520.0 iterations/seconds
         Isolated run time: 0.0003406200557947159 seconds; Isolated performance: 2935.8224302642875 iterations/seconds

>>> "3, Serializers.orjson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 26 iterations. Performance: 416.0 iterations/seconds
         Isolated run time: 0.0012380999978631735 seconds; Isolated performance: 807.6892025893641 iterations/seconds

>>> "3, Serializers.orjson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 184 iterations. Performance: 1472.0 iterations/seconds
         Isolated run time: 0.00042882002890110016 seconds; Isolated performance: 2331.98062731028 iterations/seconds

>>> "3, Serializers.msgspec_json, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 88 iterations. Performance: 704.0 iterations/seconds
         Isolated run time: 0.0009236382320523262 seconds; Isolated performance: 1082.6749752205446 iterations/seconds

>>> "3, Serializers.msgspec_json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 287 iterations. Performance: 2296.0 iterations/seconds
         Isolated run time: 0.0002782196970656514 seconds; Isolated performance: 3594.281823130698 iterations/seconds

>>> "3, Serializers.msgspec_json, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 72 iterations. Performance: 576.0 iterations/seconds
         Isolated run time: 0.001160927931778133 seconds; Isolated performance: 861.3799122468799 iterations/seconds

>>> "3, Serializers.msgspec_json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 186 iterations. Performance: 2976.0 iterations/seconds
         Isolated run time: 0.00039944180753082037 seconds; Isolated performance: 2503.4935781549143 iterations/seconds

>>> "3, Serializers.msgpack, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 64 iterations. Performance: 1024.0 iterations/seconds
         Isolated run time: 0.001124917296692729 seconds; Isolated performance: 888.9542395161071 iterations/seconds

>>> "3, Serializers.msgpack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 188 iterations. Performance: 3008.0 iterations/seconds
         Isolated run time: 0.0003968682140111923 seconds; Isolated performance: 2519.728123078656 iterations/seconds

>>> "3, Serializers.msgpack, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 60 iterations. Performance: 960.0 iterations/seconds
         Isolated run time: 0.0013262053253129125 seconds; Isolated performance: 754.0310545533772 iterations/seconds

>>> "3, Serializers.msgpack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 152 iterations. Performance: 2432.0 iterations/seconds
         Isolated run time: 0.0005223570624366403 seconds; Isolated performance: 1914.3993101869773 iterations/seconds

>>> "3, Serializers.cbor, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 48 iterations. Performance: 384.0 iterations/seconds
         Isolated run time: 0.0009314073249697685 seconds; Isolated performance: 1073.644122384863 iterations/seconds

>>> "3, Serializers.cbor, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 134 iterations. Performance: 1072.0 iterations/seconds
         Isolated run time: 0.00026321178302168846 seconds; Isolated performance: 3799.2220124795886 iterations/seconds

>>> "3, Serializers.cbor, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 24 iterations. Performance: 384.0 iterations/seconds
         Isolated run time: 0.0011497416999191046 seconds; Isolated performance: 869.7605732403719 iterations/seconds

>>> "3, Serializers.cbor, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 83 iterations. Performance: 1328.0 iterations/seconds
         Isolated run time: 0.0003691244637593627 seconds; Isolated performance: 2709.1133159137175 iterations/seconds

>>> "3, Serializers.ujson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0 seconds to make 26 iterations. Performance: 0.0 iterations/seconds
         Isolated run time: 0.0011610226938501 seconds; Isolated performance: 861.3096068638175 iterations/seconds

>>> "3, Serializers.ujson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 154 iterations. Performance: 2464.0 iterations/seconds
         Isolated run time: 0.00040499737951904535 seconds; Isolated performance: 2469.151778679531 iterations/seconds

>>> "3, Serializers.ujson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 60 iterations. Performance: 480.0 iterations/seconds
         Isolated run time: 0.0013614583294838667 seconds; Isolated performance: 734.5065055197857 iterations/seconds

>>> "3, Serializers.ujson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 128 iterations. Performance: 1024.0 iterations/seconds
         Isolated run time: 0.0005205690395087004 seconds; Isolated performance: 1920.9747874052866 iterations/seconds

>>> "3, Serializers.cbor2, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 43 iterations. Performance: 688.0 iterations/seconds
         Isolated run time: 0.001487269066274166 seconds; Isolated performance: 672.3732932233648 iterations/seconds

>>> "3, Serializers.cbor2, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 106 iterations. Performance: 1696.0 iterations/seconds
         Isolated run time: 0.000681997393257916 seconds; Isolated performance: 1466.2812642479157 iterations/seconds

>>> "3, Serializers.cbor2, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 48 iterations. Performance: 768.0 iterations/seconds
         Isolated run time: 0.0017507914453744888 seconds; Isolated performance: 571.1702571096943 iterations/seconds

>>> "3, Serializers.cbor2, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 100 iterations. Performance: 1600.0 iterations/seconds
         Isolated run time: 0.0008007065625861287 seconds; Isolated performance: 1248.8969701586955 iterations/seconds

>>> "3, Serializers.json, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 53 iterations. Performance: 848.0 iterations/seconds
         Isolated run time: 0.0014325747033581138 seconds; Isolated performance: 698.0438769830915 iterations/seconds

>>> "3, Serializers.json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 100 iterations. Performance: 800.0 iterations/seconds
         Isolated run time: 0.0006226209225133061 seconds; Isolated performance: 1606.1137103509861 iterations/seconds

>>> "3, Serializers.json, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 49 iterations. Performance: 392.0 iterations/seconds
         Isolated run time: 0.0016627900768071413 seconds; Isolated performance: 601.3988259541345 iterations/seconds

>>> "3, Serializers.json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 64 iterations. Performance: 341.3333435058594 iterations/seconds
         Isolated run time: 0.000781959155574441 seconds; Isolated performance: 1278.8391732115247 iterations/seconds

>>> "3, Serializers.simplejson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.1875 seconds to make 16 iterations. Performance: 85.33333587646484 iterations/seconds
         Isolated run time: 0.0016848825616762042 seconds; Isolated performance: 593.5131757819078 iterations/seconds

>>> "3, Serializers.simplejson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 46 iterations. Performance: 368.0 iterations/seconds
         Isolated run time: 0.0008251082617789507 seconds; Isolated performance: 1211.9621706901578 iterations/seconds

>>> "3, Serializers.simplejson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 19 iterations. Performance: 304.0 iterations/seconds
         Isolated run time: 0.0019300964195281267 seconds; Isolated performance: 518.1088311870355 iterations/seconds

>>> "3, Serializers.simplejson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 87 iterations. Performance: 696.0 iterations/seconds
         Isolated run time: 0.0009701317176222801 seconds; Isolated performance: 1030.7878629624902 iterations/seconds

>>> "3, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 6 iterations. Performance: 96.0 iterations/seconds
         Isolated run time: 0.011994986445643008 seconds; Isolated performance: 83.368164235253 iterations/seconds

>>> "3, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 9 iterations. Performance: 72.0 iterations/seconds
         Isolated run time: 0.010044544120319188 seconds; Isolated performance: 99.55653417630892 iterations/seconds

>>> "3, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 9 iterations. Performance: 144.0 iterations/seconds
         Isolated run time: 0.011164120631292462 seconds; Isolated performance: 89.57266165657964 iterations/seconds

>>> "3, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 8 iterations. Performance: 64.0 iterations/seconds
         Isolated run time: 0.010456279036588967 seconds; Isolated performance: 95.63631541399823 iterations/seconds

>>> "3, Serializers.msgspec_yaml, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 11 iterations. Performance: 88.0 iterations/seconds
         Isolated run time: 0.007409863523207605 seconds; Isolated performance: 134.95525212684578 iterations/seconds

>>> "3, Serializers.msgspec_yaml, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 15 iterations. Performance: 120.0 iterations/seconds
         Isolated run time: 0.006323924753814936 seconds; Isolated performance: 158.12964874332914 iterations/seconds

>>> "3, Serializers.msgspec_yaml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 9 iterations. Performance: 144.0 iterations/seconds
         Isolated run time: 0.007518362603150308 seconds; Isolated performance: 133.00768435682855 iterations/seconds

>>> "3, Serializers.msgspec_yaml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 15 iterations. Performance: 240.0 iterations/seconds
         Isolated run time: 0.006526685319840908 seconds; Isolated performance: 153.21713105426318 iterations/seconds

>>> "4, Serializers.pickle, universal=False, optimized=False": benchmark_single_item()
         It was used 1.0625 seconds to make 2 iterations. Performance: 1.8823529481887817 iterations/seconds
         Isolated run time: 0.5129064308712259 seconds; Isolated performance: 1.9496733513389453 iterations/seconds

>>> "4, Serializers.pickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.25 seconds to make 2 iterations. Performance: 8.0 iterations/seconds
         Isolated run time: 0.1244108232203871 seconds; Isolated performance: 8.037885885768585 iterations/seconds

>>> "4, Serializers.pickle, universal=True, optimized=False": benchmark_single_item()
         It was used 1.75 seconds to make 2 iterations. Performance: 1.1428571939468384 iterations/seconds
         Isolated run time: 0.7398785308469087 seconds; Isolated performance: 1.3515732087202759 iterations/seconds

>>> "4, Serializers.pickle, universal=True, optimized=True": benchmark_single_item()
         It was used 1.0625 seconds to make 2 iterations. Performance: 1.8823529481887817 iterations/seconds
         Isolated run time: 0.4286585273221135 seconds; Isolated performance: 2.3328592253772067 iterations/seconds

>>> "4, Serializers.marshal, universal=False, optimized=False": benchmark_single_item()
         It was used 0.9375 seconds to make 2 iterations. Performance: 2.133333444595337 iterations/seconds
         Isolated run time: 0.46370108739938587 seconds; Isolated performance: 2.156561688497184 iterations/seconds

>>> "4, Serializers.marshal, universal=False, optimized=True": benchmark_single_item()
         It was used 0.5 seconds to make 2 iterations. Performance: 4.0 iterations/seconds
         Isolated run time: 0.1719603722449392 seconds; Isolated performance: 5.815293296618401 iterations/seconds

>>> "4, Serializers.marshal, universal=True, optimized=False": benchmark_single_item()
         It was used 1.25 seconds to make 2 iterations. Performance: 1.600000023841858 iterations/seconds
         Isolated run time: 0.5571830259868875 seconds; Isolated performance: 1.7947423976686856 iterations/seconds

>>> "4, Serializers.marshal, universal=True, optimized=True": benchmark_single_item()
         It was used 1.0 seconds to make 2 iterations. Performance: 2.0 iterations/seconds
         Isolated run time: 0.45293805352412164 seconds; Isolated performance: 2.2078074302201327 iterations/seconds

>>> "4, Serializers.cloudpickle, universal=False, optimized=False": benchmark_single_item()
         It was used 1.4375 seconds to make 2 iterations. Performance: 1.39130437374115 iterations/seconds
         Isolated run time: 0.6198306129081175 seconds; Isolated performance: 1.6133439994326937 iterations/seconds

>>> "4, Serializers.cloudpickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.625 seconds to make 2 iterations. Performance: 3.200000047683716 iterations/seconds
         Isolated run time: 0.2361779729835689 seconds; Isolated performance: 4.234095107885318 iterations/seconds

>>> "4, Serializers.cloudpickle, universal=True, optimized=False": benchmark_single_item()
         It was used 2.1875 seconds to make 2 iterations. Performance: 0.9142857193946838 iterations/seconds
         Isolated run time: 0.8488203943707049 seconds; Isolated performance: 1.1781055293109164 iterations/seconds

>>> "4, Serializers.cloudpickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.5625 seconds to make 2 iterations. Performance: 3.555555582046509 iterations/seconds
         Isolated run time: 0.26492729561869055 seconds; Isolated performance: 3.7746204960295917 iterations/seconds

>>> "4, Serializers.msgspec_messagepack, universal=False, optimized=False": benchmark_single_item()
         It was used 1.5625 seconds to make 2 iterations. Performance: 1.2799999713897705 iterations/seconds
         Isolated run time: 0.47584574797656387 seconds; Isolated performance: 2.1015213527751255 iterations/seconds

>>> "4, Serializers.msgspec_messagepack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.25 seconds to make 2 iterations. Performance: 8.0 iterations/seconds
         Isolated run time: 0.1282163355499506 seconds; Isolated performance: 7.799318204741699 iterations/seconds

>>> "4, Serializers.msgspec_messagepack, universal=True, optimized=False": benchmark_single_item()
         It was used 1.9375 seconds to make 2 iterations. Performance: 1.0322580337524414 iterations/seconds
         Isolated run time: 0.9108218296896666 seconds; Isolated performance: 1.0979095662877536 iterations/seconds

>>> "4, Serializers.msgspec_messagepack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.375 seconds to make 2 iterations. Performance: 5.333333492279053 iterations/seconds
         Isolated run time: 0.1936748728621751 seconds; Isolated performance: 5.163292404542484 iterations/seconds

>>> "4, Serializers.orjson, universal=False, optimized=False": benchmark_single_item()
         It was used 1.625 seconds to make 2 iterations. Performance: 1.2307692766189575 iterations/seconds
         Isolated run time: 0.7600803511450067 seconds; Isolated performance: 1.3156503762971525 iterations/seconds

>>> "4, Serializers.orjson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.25 seconds to make 2 iterations. Performance: 8.0 iterations/seconds
         Isolated run time: 0.15392251522280276 seconds; Isolated performance: 6.496775332396957 iterations/seconds

>>> "4, Serializers.orjson, universal=True, optimized=False": benchmark_single_item()
         It was used 2.1875 seconds to make 2 iterations. Performance: 0.9142857193946838 iterations/seconds
         Isolated run time: 0.7783390532713383 seconds; Isolated performance: 1.2847871320307347 iterations/seconds

>>> "4, Serializers.orjson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.4375 seconds to make 2 iterations. Performance: 4.5714287757873535 iterations/seconds
         Isolated run time: 0.22320834267884493 seconds; Isolated performance: 4.480119282274377 iterations/seconds

>>> "4, Serializers.msgspec_json, universal=False, optimized=False": benchmark_single_item()
         It was used 2.0625 seconds to make 2 iterations. Performance: 0.9696969985961914 iterations/seconds
         Isolated run time: 0.9457543311873451 seconds; Isolated performance: 1.057357039797589 iterations/seconds

>>> "4, Serializers.msgspec_json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 2 iterations. Performance: 10.666666984558105 iterations/seconds
         Isolated run time: 0.11897945846430957 seconds; Isolated performance: 8.404812165958642 iterations/seconds

>>> "4, Serializers.msgspec_json, universal=True, optimized=False": benchmark_single_item()
         It was used 1.875 seconds to make 2 iterations. Performance: 1.0666667222976685 iterations/seconds
         Isolated run time: 0.6389246685430408 seconds; Isolated performance: 1.5651297394422574 iterations/seconds

>>> "4, Serializers.msgspec_json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.375 seconds to make 2 iterations. Performance: 5.333333492279053 iterations/seconds
         Isolated run time: 0.1918887838255614 seconds; Isolated performance: 5.211352013721974 iterations/seconds

>>> "4, Serializers.msgpack, universal=False, optimized=False": benchmark_single_item()
         It was used 1.8125 seconds to make 2 iterations. Performance: 1.1034482717514038 iterations/seconds
         Isolated run time: 0.6536701291333884 seconds; Isolated performance: 1.5298236150484081 iterations/seconds

>>> "4, Serializers.msgpack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.375 seconds to make 2 iterations. Performance: 5.333333492279053 iterations/seconds
         Isolated run time: 0.20264732756186277 seconds; Isolated performance: 4.93468140947838 iterations/seconds

>>> "4, Serializers.msgpack, universal=True, optimized=False": benchmark_single_item()
         It was used 2.0 seconds to make 2 iterations. Performance: 1.0 iterations/seconds
         Isolated run time: 0.7228391576791182 seconds; Isolated performance: 1.3834336302570907 iterations/seconds

>>> "4, Serializers.msgpack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.5 seconds to make 2 iterations. Performance: 4.0 iterations/seconds
         Isolated run time: 0.26426102907862514 seconds; Isolated performance: 3.784137235394144 iterations/seconds

>>> "4, Serializers.cbor, universal=False, optimized=False": benchmark_single_item()
         It was used 1.125 seconds to make 2 iterations. Performance: 1.7777777910232544 iterations/seconds
         Isolated run time: 0.48938263673335314 seconds; Isolated performance: 2.043390845811442 iterations/seconds

>>> "4, Serializers.cbor, universal=False, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 2 iterations. Performance: 10.666666984558105 iterations/seconds
         Isolated run time: 0.11621763883158565 seconds; Isolated performance: 8.604545833607315 iterations/seconds

>>> "4, Serializers.cbor, universal=True, optimized=False": benchmark_single_item()
         It was used 1.6875 seconds to make 2 iterations. Performance: 1.185185194015503 iterations/seconds
         Isolated run time: 0.5882441364228725 seconds; Isolated performance: 1.699974446122022 iterations/seconds

>>> "4, Serializers.cbor, universal=True, optimized=True": benchmark_single_item()
         It was used 0.375 seconds to make 2 iterations. Performance: 5.333333492279053 iterations/seconds
         Isolated run time: 0.18854426010511816 seconds; Isolated performance: 5.303794448276892 iterations/seconds

>>> "4, Serializers.ujson, universal=False, optimized=False": benchmark_single_item()
         It was used 1.5625 seconds to make 2 iterations. Performance: 1.2799999713897705 iterations/seconds
         Isolated run time: 0.5714562017237768 seconds; Isolated performance: 1.7499153863122607 iterations/seconds

>>> "4, Serializers.ujson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.375 seconds to make 2 iterations. Performance: 5.333333492279053 iterations/seconds
         Isolated run time: 0.18972512881737202 seconds; Isolated performance: 5.270783086212014 iterations/seconds

>>> "4, Serializers.ujson, universal=True, optimized=False": benchmark_single_item()
         It was used 1.4375 seconds to make 2 iterations. Performance: 1.39130437374115 iterations/seconds
         Isolated run time: 0.6820820966968313 seconds; Isolated performance: 1.4660991761003155 iterations/seconds

>>> "4, Serializers.ujson, universal=True, optimized=True": benchmark_single_item()
         It was used 1.0 seconds to make 2 iterations. Performance: 2.0 iterations/seconds
         Isolated run time: 0.2595710785826668 seconds; Isolated performance: 3.852509322149021 iterations/seconds

>>> "4, Serializers.cbor2, universal=False, optimized=False": benchmark_single_item()
         It was used 2.0625 seconds to make 2 iterations. Performance: 0.9696969985961914 iterations/seconds
         Isolated run time: 0.7773829288780689 seconds; Isolated performance: 1.2863673266445605 iterations/seconds

>>> "4, Serializers.cbor2, universal=False, optimized=True": benchmark_single_item()
         It was used 0.6875 seconds to make 2 iterations. Performance: 2.909090995788574 iterations/seconds
         Isolated run time: 0.33687027532141656 seconds; Isolated performance: 2.968501744613336 iterations/seconds

>>> "4, Serializers.cbor2, universal=True, optimized=False": benchmark_single_item()
         It was used 2.625 seconds to make 2 iterations. Performance: 0.761904776096344 iterations/seconds
         Isolated run time: 1.2183979782275856 seconds; Isolated performance: 0.820749884577705 iterations/seconds

>>> "4, Serializers.cbor2, universal=True, optimized=True": benchmark_single_item()
         It was used 0.875 seconds to make 2 iterations. Performance: 2.2857143878936768 iterations/seconds
         Isolated run time: 0.4264100376749411 seconds; Isolated performance: 2.3451605535663194 iterations/seconds

>>> "4, Serializers.json, universal=False, optimized=False": benchmark_single_item()
         It was used 2.125 seconds to make 2 iterations. Performance: 0.9411764740943909 iterations/seconds
         Isolated run time: 0.740687851794064 seconds; Isolated performance: 1.3500963969880708 iterations/seconds

>>> "4, Serializers.json, universal=False, optimized=True": benchmark_single_item()
         It was used 1.0 seconds to make 2 iterations. Performance: 2.0 iterations/seconds
         Isolated run time: 0.34609557210933417 seconds; Isolated performance: 2.889375307246325 iterations/seconds

>>> "4, Serializers.json, universal=True, optimized=False": benchmark_single_item()
         It was used 2.375 seconds to make 2 iterations. Performance: 0.8421052694320679 iterations/seconds
         Isolated run time: 0.9349711155518889 seconds; Isolated performance: 1.0695517576601563 iterations/seconds

>>> "4, Serializers.json, universal=True, optimized=True": benchmark_single_item()
         It was used 1.0 seconds to make 2 iterations. Performance: 2.0 iterations/seconds
         Isolated run time: 0.4090100274188444 seconds; Isolated performance: 2.44492783296962 iterations/seconds

>>> "4, Serializers.simplejson, universal=False, optimized=False": benchmark_single_item()
         It was used 2.625 seconds to make 2 iterations. Performance: 0.761904776096344 iterations/seconds
         Isolated run time: 0.8724189820932224 seconds; Isolated performance: 1.1462382416309516 iterations/seconds

>>> "4, Serializers.simplejson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.8125 seconds to make 2 iterations. Performance: 2.461538553237915 iterations/seconds
         Isolated run time: 0.3911958644166589 seconds; Isolated performance: 2.556264242443294 iterations/seconds

>>> "4, Serializers.simplejson, universal=True, optimized=False": benchmark_single_item()
         It was used 2.75 seconds to make 2 iterations. Performance: 0.7272727489471436 iterations/seconds
         Isolated run time: 0.9796636385144666 seconds; Isolated performance: 1.0207585141328415 iterations/seconds

>>> "4, Serializers.simplejson, universal=True, optimized=True": benchmark_single_item()
         It was used 1.375 seconds to make 2 iterations. Performance: 1.454545497894287 iterations/seconds
         Isolated run time: 0.4832136398181319 seconds; Isolated performance: 2.069478006408039 iterations/seconds

>>> "4, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 16.4375 seconds to make 2 iterations. Performance: 0.12167300283908844 iterations/seconds
         Isolated run time: 8.060303959995508 seconds; Isolated performance: 0.12406480015681161 iterations/seconds

>>> "4, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 13.4375 seconds to make 2 iterations. Performance: 0.14883720874786377 iterations/seconds
         Isolated run time: 6.669931973796338 seconds; Isolated performance: 0.14992656655699416 iterations/seconds

>>> "4, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 15.4375 seconds to make 2 iterations. Performance: 0.1295546591281891 iterations/seconds
         Isolated run time: 7.387529099360108 seconds; Isolated performance: 0.13536325699029975 iterations/seconds

>>> "4, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 13.5 seconds to make 2 iterations. Performance: 0.14814814925193787 iterations/seconds
         Isolated run time: 6.686757550924085 seconds; Isolated performance: 0.14954931330833188 iterations/seconds

>>> "4, Serializers.msgspec_yaml, universal=False, optimized=False": benchmark_single_item()
         It was used 10.25 seconds to make 2 iterations. Performance: 0.19512194395065308 iterations/seconds
         Isolated run time: 4.9917928776703775 seconds; Isolated performance: 0.20032882463398413 iterations/seconds

>>> "4, Serializers.msgspec_yaml, universal=False, optimized=True": benchmark_single_item()
         It was used 8.1875 seconds to make 2 iterations. Performance: 0.2442748099565506 iterations/seconds
         Isolated run time: 3.84629774116911 seconds; Isolated performance: 0.25999027306087924 iterations/seconds

>>> "4, Serializers.msgspec_yaml, universal=True, optimized=False": benchmark_single_item()
         It was used 10.3125 seconds to make 2 iterations. Performance: 0.19393938779830933 iterations/seconds
         Isolated run time: 5.1652645241701975 seconds; Isolated performance: 0.1936009269845963 iterations/seconds

>>> "4, Serializers.msgspec_yaml, universal=True, optimized=True": benchmark_single_item()
         It was used 8.875 seconds to make 2 iterations. Performance: 0.22535210847854614 iterations/seconds
         Isolated run time: 4.287871201173402 seconds; Isolated performance: 0.23321596034095984 iterations/seconds
'''


# # ALLOW_PROFILE = True
# ALLOW_PROFILE = False

# set_profiler(ALLOW_PROFILE)


class SimpleClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __eq__(self, other):
        if isinstance(other, SimpleClass):
            return (self.a == other.a) and (self.b == other.b)
        
        return False


@dataclass
class DataClass:
    x: int
    y: 'Any'
    z: int = 5

    def add_one(self):
        return self.x + 1


transport: List = list()


def on_new_class(class_info, *args, **kwargs):
    transport.append(
        (
            0,
            class_info,
        )
    )


def on_new_object(adjusted_object_info, *args, **kwargs):
    transport.append(
        (
            1,
            adjusted_object_info,
        )
    )


transport_marshal: List = list()


def on_new_class_marshal(class_info, *args, **kwargs):
    transport.append(
        marshal_dumps((
            0,
            class_info,
        ))
    )


def on_new_object_marshal(adjusted_object_info, *args, **kwargs):
    transport.append(
        marshal_dumps((
            1,
            adjusted_object_info,
        ))
    )


class CoDec:
    def __init__(self, serializer_type: Serializers, single_benchmarking_item: Any, universal: bool = False, optimized: bool = True) -> None:
        self.serializer: Serializer = Serializer(serializer_type)
        self.transport: List = [None] * 1024
        self.transport.clear()
        self.universal: bool = universal
        self.optimized: bool = optimized
        if universal:
            if optimized:
                remote_objects_manager_type = UniversalOptimizedRemoteObjectsManager
            else:
                remote_objects_manager_type = UniversalRemoteObjectsManager
        else:
            if optimized:
                remote_objects_manager_type = RemoteObjectsManager
            else:
                remote_objects_manager_type = FastRemoteObjectsManager

        self.rom_src: RemoteObjectsManager = remote_objects_manager_type(
            on_new_class_handler=self.on_new_class,
            on_new_obj_info_handler=self.on_new_object,
            serializable_data_types=SUPPORTED_TYPES[serializer_type],
        )
        self.rom_dest: RemoteObjectsManager = remote_objects_manager_type(
            on_new_class_handler=self.on_new_class,
            on_new_obj_info_handler=self.on_new_object,
            serializable_data_types=SUPPORTED_TYPES[serializer_type],
        )

        if self.rom_src.serializable_tuple:
            self.delimiter = self.serializer.dumps((
                2,
                None if self.rom_src.serializable_none else 0,
            ))
        elif self.rom_src.serializable_list:
            self.delimiter = self.serializer.dumps([
                2,
                None if self.rom_src.serializable_none else 0,
            ])
        elif self.rom_src.serializable_dict:
            self.delimiter = self.serializer.dumps({
                self.rom_src.ats(DataType.int_, 0): self.rom_src.ats(DataType.int_, 2),
                self.rom_src.ats(DataType.int_, 1): None if self.rom_src.serializable_none else self.rom_src.ats(DataType.int_, 0),
            })
        else:
            raise ValueError('Serializer does not support any of the required types (tuple, list, dict).')
        
        self.single_benchmarking_item: Any = single_benchmarking_item

    def on_new_class(self, class_info, *args, **kwargs):
        if self.rom_src.serializable_tuple:
            self.transport.append(
                self.serializer.dumps((
                    0,
                    class_info,
                ))
            )
        elif self.rom_src.serializable_list:
            self.transport.append(
                self.serializer.dumps([
                    0,
                    class_info,
                ])
            )
        elif self.rom_src.serializable_dict:
            self.transport.append(
                self.serializer.dumps({
                    self.rom_src.ats(DataType.int_, 0): self.rom_src.ats(DataType.int_, 0),
                    self.rom_src.ats(DataType.int_, 1): class_info,
                })
            )
        else:
            raise ValueError('Serializer does not support any of the required types (tuple, list, dict).')

    def on_new_object(self, adjusted_object_info, *args, **kwargs):
        if self.rom_src.serializable_tuple:
            self.transport.append(
                self.serializer.dumps((
                    1,
                    adjusted_object_info,
                ))
            )
        elif self.rom_src.serializable_list:
            self.transport.append(
                self.serializer.dumps([
                    1,
                    adjusted_object_info,
                ])
            )
        elif self.rom_src.serializable_dict:
            self.transport.append(
                self.serializer.dumps({
                    self.rom_src.ats(DataType.int_, 0): self.rom_src.ats(DataType.int_, 1),
                    self.rom_src.ats(DataType.int_, 1): adjusted_object_info,
                })
            )
        else:
            raise ValueError('Serializer does not support any of the required types (tuple, list, dict).')
    
    def send_obj(self, obj) -> Tuple[bool, int]:
        result = self.rom_src.serialize(obj)
        self.transport.append(self.delimiter)
        return result
    
    def receive_objects(self) -> Generator[Tuple[int, Any], None, None]:
        try:
            for item in self.transport:
                data_info = self.serializer.loads(item)
                if self.rom_src.serializable_tuple or self.rom_src.serializable_list:
                    item_type, item_info = data_info
                elif self.rom_src.serializable_dict:
                    item_type = self.rom_src.afs(DataType.int_, data_info[self.rom_src.ats(DataType.int_, 0)])
                    item_info = data_info[self.rom_src.ats(DataType.int_, 1)]
                else:
                    raise ValueError('Serializer does not support any of the required types (tuple, list, dict).')

                if self.optimized:
                    if 0 == item_type:
                        received_class_exists, received_class_id, received_class_value = self.rom_dest.deserialize_class(item_info)
                    elif 1 == item_type:
                        received_obj_exists, received_obj_id, received_obj_value = self.rom_dest.deserialize_obj(item_info)
                    elif 2 == item_type:
                        yield received_obj_id, received_obj_value
                    else:
                        raise ValueError('Unknown item type')
                else:
                    if 0 == item_type:
                        received_class_result: ResultExistence[Tuple[int, Type]] = self.rom_dest.deserialize_class(item_info)
                        received_class_exists = bool(received_class_result)
                        received_class_id, received_class_value = received_class_result.value if received_class_exists else (None, None)
                    elif 1 == item_type:
                        received_obj_result: ResultExistence[Tuple[int, Any]] = self.rom_dest.deserialize_obj(item_info)
                        received_obj_exists = bool(received_obj_result)
                        received_obj_id, received_obj_value = received_obj_result.value if received_obj_exists else (None, None)
                    elif 2 == item_type:
                        yield received_obj_id, received_obj_value
                    else:
                        raise ValueError('Unknown item type')
        finally:
            self.transport.clear()
    
    def benchmark_single_item(self):
        self.send_obj(self.single_benchmarking_item)
        for received_obj_id, received_obj in self.receive_objects():
            pass


def benchmark():
    transport.clear()
    rom_src: RemoteObjectsManager = RemoteObjectsManager(
        on_new_class_handler=on_new_class,
        on_new_obj_info_handler=on_new_object,
    )
    rom_dest: RemoteObjectsManager = RemoteObjectsManager(
        on_new_class_handler=on_new_class,
        on_new_obj_info_handler=on_new_object,
    )

    transport_marshal.clear()
    rom_src_marshal: RemoteObjectsManager = RemoteObjectsManager(
        on_new_class_handler=on_new_class_marshal,
        on_new_obj_info_handler=on_new_object_marshal,
        serializable_data_types=SUPPORTED_TYPES[Serializers.marshal],
    )
    rom_dest_marshal: RemoteObjectsManager = RemoteObjectsManager(
        on_new_class_handler=on_new_class_marshal,
        on_new_obj_info_handler=on_new_object_marshal,
        serializable_data_types=SUPPORTED_TYPES[Serializers.marshal],
    )

    dtcl: DataClass = DataClass(5, SimpleClass(1, 2))
    dtcl.add_one()
    obj = ({'a': 1, 'b': 2}, dtcl)
    def func():
        transport.clear()
        obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        for item in transport:
            item_type, item_info = item
            if 0 == item_type:
                received_class_exists, received_class_id, received_class_value = rom_dest.deserialize_class(item_info)
            elif 1 == item_type:
                received_obj_exists, received_obj_id, received_obj_value = rom_dest.deserialize_obj(item_info)
    
        # received_object_id, received_obj = received_obj_value
        # dict_, obj_ = received_obj
        # print(dict_)
        # print(obj_)
    
    def func_marshal():
        transport_marshal.clear()
        obj_id_result: ResultExistence[int] = rom_src_marshal.serialize(obj)
        for item in transport_marshal:
            item_type, item_info = marshal_loads(item)
            if 0 == item_type:
                received_class_exists, received_class_id, received_class_value = rom_dest_marshal.deserialize_class(item_info)
            elif 1 == item_type:
                received_obj_exists, received_obj_id, received_obj_value = rom_dest_marshal.deserialize_obj(item_info)
    
        # received_object_id, received_obj = received_obj_value
        # dict_, obj_ = received_obj
        # print(dict_)
        # print(obj_)
    
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func, 5.0, 'DataClass', do_print=True)
        print()
    
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func_marshal, 5.0, 'DataClass', do_print=True)
        print()
    
    obj = test_data_factory(TestDataType.small)
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func, 5.1, 'TestDataType.small', do_print=True)
        print()
    
    obj = test_data_factory(TestDataType.small)
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func_marshal, 5.1, 'TestDataType.small', do_print=True)
        print()
    
    obj = test_data_factory(TestDataType.deep_small)
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func, 5.1, 'TestDataType.deep_small', do_print=True)
        print()
    
    obj = test_data_factory(TestDataType.deep_small)
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func_marshal, 5.1, 'TestDataType.deep_small', do_print=True)
        print()
    
    obj = test_data_factory(TestDataType.large)
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func, 5.1, 'TestDataType.large', do_print=True)
        print()
    
    obj = test_data_factory(TestDataType.large)
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func_marshal, 5.1, 'TestDataType.large', do_print=True)
        print()
    
    obj = test_data_factory(TestDataType.deep_large)
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func, 5.1, 'TestDataType.deep_large', do_print=True)
        print()
    
    obj = test_data_factory(TestDataType.deep_large)
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func_marshal, 5.1, 'TestDataType.deep_large', do_print=True)
        print()
    
    print('=== Serializers on DataClass: ==========================================================================')
    
    with DisableGC():
        obj = ({'a': 1, 'b': 2}, dtcl)
        best_serializers, serializers_data = get_most_efficient_serializers({DataFormats.binary,
                                                    Tags.can_use_bytes,
                                                    Tags.decode_str_as_str,
                                                    Tags.decode_list_as_list,
                                                    Tags.decode_bytes_as_bytes,
                                                    Tags.deep,
                                                    Tags.can_use_custom_types,
                                                    Tags.current_platform,
                                                    # Tags.multi_platform,
                                                },
                                                obj,
                                                1.0)
        sorted_serializers = sorted(serializers_data, key=lambda x: x[1], reverse=True)
        pprint(sorted_serializers)
        print()
    
    print('=== Serializers on TestDataType: =======================================================================')

    with DisableGC():
        test_data_types = (
            TestDataType.small,
            TestDataType.deep_small,
            TestDataType.large,
            TestDataType.deep_large,
        )
    
        for test_data_type in test_data_types:
            print(f'\t== {test_data_type}: ==')
            print(f'\t\t== current_platform: ==')
            best_serializers, serializers_data = get_most_efficient_serializers({DataFormats.any,
                                                        Tags.decode_str_as_str,
                                                        Tags.decode_list_as_list,
                                                        Tags.deep,
                                                        Tags.current_platform,
                                                    },
                                                    test_data_factory(test_data_type),
                                                    0.1)
            sorted_serializers = sorted(serializers_data, key=lambda x: x[1], reverse=True)
            pprint(sorted_serializers)
            print()

            print(f'\t\t== multi_platform: ==')
            best_serializers, serializers_data = get_most_efficient_serializers({DataFormats.any,
                                                        Tags.decode_str_as_str,
                                                        Tags.decode_list_as_list,
                                                        Tags.deep,
                                                        Tags.multi_platform,
                                                    },
                                                    test_data_factory(test_data_type),
                                                    0.1)
            sorted_serializers = sorted(serializers_data, key=lambda x: x[1], reverse=True)
            pprint(sorted_serializers)
            print()
    
    print('=== RemoteObjectsManager: ==============================================================================')

    with DisableGC():
        data_set = (
            ({'a': 1, 'b': 2}, dtcl),
            test_data_factory(TestDataType.small),
            test_data_factory(TestDataType.deep_small),
            test_data_factory(TestDataType.large),
            test_data_factory(TestDataType.deep_large),
        )
        best_serializers, serializers_data = get_most_efficient_serializers({DataFormats.any,
                                                    Tags.decode_str_as_str,
                                                    Tags.decode_list_as_list,
                                                    Tags.deep,
                                                    Tags.current_platform,
                                                },
                                                test_data_factory(TestDataType.deep_small),
                                                0.5)
        sorted_serializers = sorted(serializers_data, key=lambda x: x[1], reverse=True)
        for data_item_index, data_item in enumerate(data_set):
            for serializer_type, serializer_performance, serialized_data_size in sorted_serializers:
                for universal in {False, True}:
                    for optimized in {False, True}:
                        if serializer_type in {
                                Serializers.msgspec_toml,
                            }:
                            universal = True
                            codec: CoDec = CoDec(serializer_type, data_item, universal=universal, optimized=optimized)
                        else:
                            codec = CoDec(serializer_type, data_item, universal=universal, optimized=optimized)

                        measure_func_isolated_performance(codec.benchmark_single_item, 0.1, f'{data_item_index}, {serializer_type}, {universal=}, {optimized=}', do_print=True)
                        print()


def main():
    benchmark()


if __name__ == '__main__':
    main()
