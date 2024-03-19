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
__version__ = "4.2.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.data_manipulation.remote_objects.versions.v_0_fast_optimized.remote_objects import *
from cengal.data_manipulation.remote_objects.versions.v_0_fast.remote_objects import RemoteObjectsManager as FastRemoteObjectsManager
from cengal.data_manipulation.remote_objects.versions.v_0.remote_objects import RemoteObjectsManager as UniversalRemoteObjectsManager
from cengal.data_manipulation.remote_objects.versions.v_0_optimized.remote_objects import RemoteObjectsManager as UniversalOptimizedRemoteObjectsManager
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
from unittest import TestCase, main
from typing import Any, Dict, Optional, Callable, Set, Type, Tuple, List, FrozenSet, Deque, Generator


'''
>>> "DataClass": func()
         It was used 0.375 seconds to make 1842 iterations. Performance: 4912.0 iterations/seconds
         Isolated run time: 6.055354606360197e-05 seconds; Isolated performance: 16514.309483207762 iterations/seconds

>>> "DataClass": func_marshal()
         It was used 1.75 seconds to make 5318 iterations. Performance: 3038.857177734375 iterations/seconds
         Isolated run time: 4.380743484944105e-05 seconds; Isolated performance: 22827.175419807973 iterations/seconds

>>> "TestDataType.small": func()
         It was used 0.0625 seconds to make 97 iterations. Performance: 1552.0 iterations/seconds
         Isolated run time: 0.00015537731815129519 seconds; Isolated performance: 6435.945811770753 iterations/seconds

>>> "TestDataType.small": func_marshal()
         It was used 0.0625 seconds to make 223 iterations. Performance: 3568.0 iterations/seconds
         Isolated run time: 0.0001032799482345581 seconds; Isolated performance: 9682.421584186986 iterations/seconds

>>> "TestDataType.deep_small": func()
         It was used 0.4375 seconds to make 2 iterations. Performance: 4.5714287757873535 iterations/seconds
         Isolated run time: 0.21644665556959808 seconds; Isolated performance: 4.620076006110668 iterations/seconds

>>> "TestDataType.deep_small": func_marshal()
         It was used 0.5 seconds to make 2 iterations. Performance: 4.0 iterations/seconds
         Isolated run time: 0.15614438650663942 seconds; Isolated performance: 6.404328854675022 iterations/seconds

>>> "TestDataType.large": func()
         It was used 0.0625 seconds to make 63 iterations. Performance: 1008.0 iterations/seconds
         Isolated run time: 0.00015381828416138887 seconds; Isolated performance: 6501.177707526514 iterations/seconds

>>> "TestDataType.large": func_marshal()
         It was used 0.125 seconds to make 96 iterations. Performance: 768.0 iterations/seconds
         Isolated run time: 0.000106387073174119 seconds; Isolated performance: 9399.638228258656 iterations/seconds

>>> "TestDataType.deep_large": func()
         It was used 0.6875 seconds to make 2 iterations. Performance: 2.909090995788574 iterations/seconds
         Isolated run time: 0.28062836138997227 seconds; Isolated performance: 3.5634317039337318 iterations/seconds

>>> "TestDataType.deep_large": func_marshal()
         It was used 0.25 seconds to make 2 iterations. Performance: 8.0 iterations/seconds
         Isolated run time: 0.12075315089896321 seconds; Isolated performance: 8.28135740190102 iterations/seconds

=== Serializers on DataClass: ==========================================================================
[(<Serializers.pickle: 16>, 84079.85779726713, 113),
 (<Serializers.cloudpickle: 30>, 1526.005642177909, 3094)]

=== Serializers on TestDataType: =======================================================================
        == TestDataType.small: ==
                == current_platform: ==
[(<Serializers.msgspec_messagepack: 37>, 257731.54286057188, 77),
 (<Serializers.cbor: 8>, 243044.86297145122, 81),
 (<Serializers.marshal: 10>, 228973.3331200853, 129),
 (<Serializers.msgspec_json: 36>, 226468.08837331927, 151),
 (<Serializers.pickle: 16>, 226289.10937829295, 116),
 (<Serializers.orjson: 3>, 210043.39280125196, 151),
 (<Serializers.cloudpickle: 30>, 128098.999239453, 116),
 (<Serializers.msgpack: 7>, 123695.84977823858, 77),
 (<Serializers.ujson: 2>, 111154.83626858526, 151),
 (<Serializers.cbor2: 9>, 55260.28236353694, 81),
 (<Serializers.json: 0>, 54488.06576677154, 180),
 (<Serializers.simplejson: 1>, 37297.109525815096, 180),
 (<Serializers.msgspec_toml: 39>, 2870.8551811309517, 236),
 (<Serializers.msgspec_yaml: 38>, 5.70717582925687, 176)]

                == multi_platform: ==
[(<Serializers.msgspec_messagepack: 37>, 256354.73892801718, 77),
 (<Serializers.cbor: 8>, 242564.44221048767, 81),
 (<Serializers.msgspec_json: 36>, 225777.60058876098, 151),
 (<Serializers.orjson: 3>, 210279.9165728274, 151),
 (<Serializers.msgpack: 7>, 126290.99478071659, 77),
 (<Serializers.ujson: 2>, 112623.86217566309, 151),
 (<Serializers.cbor2: 9>, 55535.73704695036, 81),
 (<Serializers.json: 0>, 53815.913041843916, 180),
 (<Serializers.simplejson: 1>, 36832.36896109632, 180),
 (<Serializers.msgspec_toml: 39>, 2860.5225212084883, 236),
 (<Serializers.msgspec_yaml: 38>, 1865.1935922838156, 176)]

        == TestDataType.deep_small: ==
                == current_platform: ==
[(<Serializers.marshal: 10>, 34535.87131168962, 5389),
 (<Serializers.pickle: 16>, 33390.9987133289, 2220),
 (<Serializers.cloudpickle: 30>, 28798.032036797395, 2220),
 (<Serializers.msgspec_messagepack: 37>, 3144.473588417121, 20529),
 (<Serializers.orjson: 3>, 2168.3754029132183, 41007),
 (<Serializers.msgspec_json: 36>, 1774.1164134899966, 41007),
 (<Serializers.cbor: 8>, 1144.593445973379, 20568),
 (<Serializers.msgpack: 7>, 1120.6912215157654, 20529),
 (<Serializers.ujson: 2>, 791.5599158746937, 41007),
 (<Serializers.cbor2: 9>, 516.688571982815, 20568),
 (<Serializers.json: 0>, 317.2189294063965, 61194),
 (<Serializers.simplejson: 1>, 222.95206437015122, 61194),
 (<Serializers.msgspec_toml: 39>, 3.254262227964867, 141522),
 (<Serializers.msgspec_yaml: 38>, 1.0197201679345653, 161098)]

                == multi_platform: ==
[(<Serializers.msgspec_messagepack: 37>, 3134.421203006586, 20529),
 (<Serializers.orjson: 3>, 2171.4334734959234, 41007),
 (<Serializers.msgspec_json: 36>, 1870.9012938502635, 41007),
 (<Serializers.cbor: 8>, 1146.3791282140733, 20568),
 (<Serializers.msgpack: 7>, 1118.7989337595654, 20529),
 (<Serializers.ujson: 2>, 805.304983882059, 41007),
 (<Serializers.cbor2: 9>, 519.821482140335, 20568),
 (<Serializers.json: 0>, 372.63981276767424, 61194),
 (<Serializers.simplejson: 1>, 235.25868771211785, 61194),
 (<Serializers.msgspec_toml: 39>, 10.792663591483793, 141522),
 (<Serializers.msgspec_yaml: 38>, 1.5124533193200795, 161098)]

        == TestDataType.large: ==
                == current_platform: ==
[(<Serializers.pickle: 16>, 198703.09026139256, 1510),
 (<Serializers.marshal: 10>, 185844.84524350404, 1523),
 (<Serializers.msgspec_messagepack: 37>, 184892.79993112208, 2065),
 (<Serializers.cbor: 8>, 181993.99546600564, 2069),
 (<Serializers.orjson: 3>, 131864.76608025545, 2129),
 (<Serializers.msgspec_json: 36>, 131650.54242275626, 2129),
 (<Serializers.cloudpickle: 30>, 119035.1647243047, 1510),
 (<Serializers.msgpack: 7>, 104186.08810401708, 2065),
 (<Serializers.ujson: 2>, 69493.91694645125, 2129),
 (<Serializers.cbor2: 9>, 47493.36299802063, 2069),
 (<Serializers.json: 0>, 38580.2650426003, 2158),
 (<Serializers.simplejson: 1>, 29288.194592382966, 2158),
 (<Serializers.msgspec_yaml: 38>, 1768.7227299073936, 2172),
 (<Serializers.msgspec_toml: 39>, 1755.31904382405, 2214)]

                == multi_platform: ==
[(<Serializers.cbor: 8>, 190934.10815977238, 2069),
 (<Serializers.msgspec_messagepack: 37>, 176030.46419935243, 2065),
 (<Serializers.msgspec_json: 36>, 125230.4840435613, 2129),
 (<Serializers.orjson: 3>, 124770.27847659995, 2129),
 (<Serializers.msgpack: 7>, 109767.1052954406, 2065),
 (<Serializers.ujson: 2>, 65987.59048972536, 2129),
 (<Serializers.cbor2: 9>, 49679.794755531904, 2069),
 (<Serializers.json: 0>, 36743.98186313511, 2158),
 (<Serializers.simplejson: 1>, 27627.030930288656, 2158),
 (<Serializers.msgspec_yaml: 38>, 1739.2710742439529, 2172),
 (<Serializers.msgspec_toml: 39>, 1683.5819118815534, 2214)]

        == TestDataType.deep_large: ==
                == current_platform: ==
[(<Serializers.marshal: 10>, 33605.10219315061, 6783),
 (<Serializers.pickle: 16>, 31551.06276101449, 3614),
 (<Serializers.cloudpickle: 30>, 28131.53012454601, 3614),
 (<Serializers.msgspec_messagepack: 37>, 3021.7945839460226, 33245),
 (<Serializers.orjson: 3>, 2130.981857242975, 53659),
 (<Serializers.msgspec_json: 36>, 1848.7170993644584, 53659),
 (<Serializers.cbor: 8>, 1104.750371714677, 33284),
 (<Serializers.msgpack: 7>, 1099.680116364709, 33245),
 (<Serializers.ujson: 2>, 788.3222605179876, 53659),
 (<Serializers.cbor2: 9>, 500.9584529072141, 33284),
 (<Serializers.json: 0>, 367.9899350773419, 73846),
 (<Serializers.simplejson: 1>, 260.480108583734, 73846),
 (<Serializers.msgspec_toml: 39>, 10.986507566842041, 154174),
 (<Serializers.msgspec_yaml: 38>, 3.073031855751556, 173930)]

                == multi_platform: ==
[(<Serializers.msgspec_messagepack: 37>, 3129.803900078701, 33245),
 (<Serializers.orjson: 3>, 2071.6953354664643, 53659),
 (<Serializers.msgspec_json: 36>, 1872.0045991950972, 53659),
 (<Serializers.cbor: 8>, 1144.0966152329834, 33284),
 (<Serializers.msgpack: 7>, 1098.575114462423, 33245),
 (<Serializers.ujson: 2>, 802.7893724457039, 53659),
 (<Serializers.cbor2: 9>, 515.0703656235943, 33284),
 (<Serializers.json: 0>, 361.8401938939023, 73846),
 (<Serializers.simplejson: 1>, 259.5755346231525, 73846),
 (<Serializers.msgspec_toml: 39>, 10.768618751382412, 154174),
 (<Serializers.msgspec_yaml: 38>, 3.9636315642372315, 173930)]

=== RemoteObjectsManager: ==============================================================================
>>> "0, Serializers.marshal, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 256 iterations. Performance: 4096.0 iterations/seconds
         Isolated run time: 0.0002806582488119602 seconds; Isolated performance: 3563.0522325035795 iterations/seconds

>>> "0, Serializers.marshal, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 798 iterations. Performance: 12768.0 iterations/seconds
         Isolated run time: 9.579467587172985e-05 seconds; Isolated performance: 10438.993512948582 iterations/seconds

>>> "0, Serializers.marshal, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 200 iterations. Performance: 1600.0 iterations/seconds
         Isolated run time: 0.0003355335211381316 seconds; Isolated performance: 2980.328155017103 iterations/seconds

>>> "0, Serializers.marshal, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 216 iterations. Performance: 3456.0 iterations/seconds
         Isolated run time: 0.00012660003267228603 seconds; Isolated performance: 7898.892116312302 iterations/seconds

>>> "0, Serializers.pickle, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 377 iterations. Performance: 6032.0 iterations/seconds
         Isolated run time: 0.00017896434292197227 seconds; Isolated performance: 5587.705258337388 iterations/seconds

>>> "0, Serializers.pickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 1008 iterations. Performance: 5376.0 iterations/seconds
         Isolated run time: 7.234816439449787e-05 seconds; Isolated performance: 13822.050750966264 iterations/seconds

>>> "0, Serializers.pickle, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 125 iterations. Performance: 1000.0 iterations/seconds
         Isolated run time: 0.00019822618924081326 seconds; Isolated performance: 5044.742088973719 iterations/seconds

>>> "0, Serializers.pickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 408 iterations. Performance: 6528.0 iterations/seconds
         Isolated run time: 8.212903048843145e-05 seconds; Isolated performance: 12175.962556149474 iterations/seconds

>>> "0, Serializers.cloudpickle, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 50 iterations. Performance: 800.0 iterations/seconds
         Isolated run time: 0.0009289330337196589 seconds; Isolated performance: 1076.5038637885154 iterations/seconds

>>> "0, Serializers.cloudpickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 98 iterations. Performance: 784.0 iterations/seconds
         Isolated run time: 0.0007491244468837976 seconds; Isolated performance: 1334.891691440311 iterations/seconds

>>> "0, Serializers.cloudpickle, universal=True, optimized=False": benchmark_single_item()
         It was used 0.1875 seconds to make 88 iterations. Performance: 469.3333435058594 iterations/seconds
         Isolated run time: 0.0009302576072514057 seconds; Isolated performance: 1074.9710533995624 iterations/seconds

>>> "0, Serializers.cloudpickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 92 iterations. Performance: 736.0 iterations/seconds
         Isolated run time: 0.000772637315094471 seconds; Isolated performance: 1294.2683202890987 iterations/seconds

>>> "0, Serializers.msgspec_messagepack, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 263 iterations. Performance: 2104.0 iterations/seconds
         Isolated run time: 0.00028666818980127573 seconds; Isolated performance: 3488.353558492906 iterations/seconds

>>> "0, Serializers.msgspec_messagepack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 697 iterations. Performance: 11152.0 iterations/seconds
         Isolated run time: 0.00010353734251111746 seconds; Isolated performance: 9658.351042693836 iterations/seconds

>>> "0, Serializers.msgspec_messagepack, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 201 iterations. Performance: 1608.0 iterations/seconds
         Isolated run time: 0.0003793839132413268 seconds; Isolated performance: 2635.8524046429407 iterations/seconds

>>> "0, Serializers.msgspec_messagepack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 335 iterations. Performance: 5360.0 iterations/seconds
         Isolated run time: 0.0001441108761355281 seconds; Isolated performance: 6939.101522494088 iterations/seconds

>>> "0, Serializers.orjson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 211 iterations. Performance: 3376.0 iterations/seconds
         Isolated run time: 0.0003095826832577586 seconds; Isolated performance: 3230.154831261669 iterations/seconds

>>> "0, Serializers.orjson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 658 iterations. Performance: 5264.0 iterations/seconds
         Isolated run time: 0.00011941057164222002 seconds; Isolated performance: 8374.46790721526 iterations/seconds

>>> "0, Serializers.orjson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 132 iterations. Performance: 2112.0 iterations/seconds
         Isolated run time: 0.00040324265137314796 seconds; Isolated performance: 2479.8964013224677 iterations/seconds

>>> "0, Serializers.orjson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 207 iterations. Performance: 3312.0 iterations/seconds
         Isolated run time: 0.00016040436457842588 seconds; Isolated performance: 6234.24432762909 iterations/seconds

>>> "0, Serializers.msgspec_json, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 130 iterations. Performance: 2080.0 iterations/seconds
         Isolated run time: 0.00029032560996711254 seconds; Isolated performance: 3444.408504345441 iterations/seconds

>>> "0, Serializers.msgspec_json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 442 iterations. Performance: 7072.0 iterations/seconds
         Isolated run time: 0.00011189084034413099 seconds; Isolated performance: 8937.282059232053 iterations/seconds

>>> "0, Serializers.msgspec_json, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 212 iterations. Performance: 1696.0 iterations/seconds
         Isolated run time: 0.00037433707620948553 seconds; Isolated performance: 2671.389139771938 iterations/seconds

>>> "0, Serializers.msgspec_json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 563 iterations. Performance: 9008.0 iterations/seconds
         Isolated run time: 0.00014174007810652256 seconds; Isolated performance: 7055.167552881307 iterations/seconds

>>> "0, Serializers.cbor, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 242 iterations. Performance: 3872.0 iterations/seconds
         Isolated run time: 0.00027696089819073677 seconds; Isolated performance: 3610.6179844611943 iterations/seconds

>>> "0, Serializers.cbor, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 696 iterations. Performance: 5568.0 iterations/seconds
         Isolated run time: 9.596534073352814e-05 seconds; Isolated performance: 10420.428796024922 iterations/seconds

>>> "0, Serializers.cbor, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 209 iterations. Performance: 1672.0 iterations/seconds
         Isolated run time: 0.00035776791628450155 seconds; Isolated performance: 2795.108097968146 iterations/seconds

>>> "0, Serializers.cbor, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 373 iterations. Performance: 2984.0 iterations/seconds
         Isolated run time: 0.00013779383152723312 seconds; Isolated performance: 7257.218911155419 iterations/seconds

>>> "0, Serializers.msgpack, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 155 iterations. Performance: 2480.0 iterations/seconds
         Isolated run time: 0.0003367925528436899 seconds; Isolated performance: 2969.186793343717 iterations/seconds

>>> "0, Serializers.msgpack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 492 iterations. Performance: 7872.0 iterations/seconds
         Isolated run time: 0.00013641652185469866 seconds; Isolated performance: 7330.490371724402 iterations/seconds

>>> "0, Serializers.msgpack, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 192 iterations. Performance: 1536.0 iterations/seconds
         Isolated run time: 0.00042097328696399927 seconds; Isolated performance: 2375.447637573065 iterations/seconds

>>> "0, Serializers.msgpack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 288 iterations. Performance: 1536.0 iterations/seconds
         Isolated run time: 0.0001829200191423297 seconds; Isolated performance: 5466.870191074614 iterations/seconds

>>> "0, Serializers.ujson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 97 iterations. Performance: 1552.0 iterations/seconds
         Isolated run time: 0.00034592265728861094 seconds; Isolated performance: 2890.8196064349663 iterations/seconds

>>> "0, Serializers.ujson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 202 iterations. Performance: 3232.0 iterations/seconds
         Isolated run time: 0.00013985077384859324 seconds; Isolated performance: 7150.478845992164 iterations/seconds

>>> "0, Serializers.ujson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 170 iterations. Performance: 2720.0 iterations/seconds
         Isolated run time: 0.00041919376235455275 seconds; Isolated performance: 2385.5316796298202 iterations/seconds

>>> "0, Serializers.ujson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 440 iterations. Performance: 3520.0 iterations/seconds
         Isolated run time: 0.00017518852837383747 seconds; Isolated performance: 5708.136310535612 iterations/seconds

>>> "0, Serializers.cbor2, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 124 iterations. Performance: 1984.0 iterations/seconds
         Isolated run time: 0.0004588782321661711 seconds; Isolated performance: 2179.227363388803 iterations/seconds

>>> "0, Serializers.cbor2, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 311 iterations. Performance: 4976.0 iterations/seconds
         Isolated run time: 0.00023057474754750729 seconds; Isolated performance: 4336.988376378734 iterations/seconds

>>> "0, Serializers.cbor2, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 124 iterations. Performance: 1984.0 iterations/seconds
         Isolated run time: 0.0005508470349013805 seconds; Isolated performance: 1815.386008529632 iterations/seconds

>>> "0, Serializers.cbor2, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 281 iterations. Performance: 2248.0 iterations/seconds
         Isolated run time: 0.0002779026981443167 seconds; Isolated performance: 3598.381759793831 iterations/seconds

>>> "0, Serializers.json, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 115 iterations. Performance: 1840.0 iterations/seconds
         Isolated run time: 0.00043530913535505533 seconds; Isolated performance: 2297.218042953223 iterations/seconds

>>> "0, Serializers.json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 377 iterations. Performance: 3016.0 iterations/seconds
         Isolated run time: 0.00020241155289113522 seconds; Isolated performance: 4940.429465198752 iterations/seconds

>>> "0, Serializers.json, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 156 iterations. Performance: 1248.0 iterations/seconds
         Isolated run time: 0.000503272982314229 seconds; Isolated performance: 1986.9932127125971 iterations/seconds

>>> "0, Serializers.json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 307 iterations. Performance: 2456.0 iterations/seconds
         Isolated run time: 0.00023740611504763365 seconds; Isolated performance: 4212.191416380989 iterations/seconds

>>> "0, Serializers.simplejson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.1875 seconds to make 128 iterations. Performance: 682.6666870117188 iterations/seconds
         Isolated run time: 0.0004994800547137856 seconds; Isolated performance: 2002.0819461410217 iterations/seconds

>>> "0, Serializers.simplejson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 133 iterations. Performance: 709.3333129882812 iterations/seconds
         Isolated run time: 0.00026223529130220413 seconds; Isolated performance: 3813.369264808771 iterations/seconds

>>> "0, Serializers.simplejson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 50 iterations. Performance: 800.0 iterations/seconds
         Isolated run time: 0.0006034626858308911 seconds; Isolated performance: 1657.1032865489067 iterations/seconds

>>> "0, Serializers.simplejson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 237 iterations. Performance: 3792.0 iterations/seconds
         Isolated run time: 0.0003024700563400984 seconds; Isolated performance: 3306.112387123691 iterations/seconds

>>> "0, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 23 iterations. Performance: 184.0 iterations/seconds
         Isolated run time: 0.003502200823277235 seconds; Isolated performance: 285.53473957105507 iterations/seconds

>>> "0, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 24 iterations. Performance: 384.0 iterations/seconds
         Isolated run time: 0.00302437343634665 seconds; Isolated performance: 330.64699880712124 iterations/seconds

>>> "0, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 24 iterations. Performance: 384.0 iterations/seconds
         Isolated run time: 0.0033045709133148193 seconds; Isolated performance: 302.611148688257 iterations/seconds

>>> "0, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 26 iterations. Performance: 208.0 iterations/seconds
         Isolated run time: 0.00302398344501853 seconds; Isolated performance: 330.6896410584921 iterations/seconds

>>> "0, Serializers.msgspec_yaml, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 16 iterations. Performance: 128.0 iterations/seconds
         Isolated run time: 0.0025470209075137973 seconds; Isolated performance: 392.61554432080493 iterations/seconds

>>> "0, Serializers.msgspec_yaml, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 39 iterations. Performance: 624.0 iterations/seconds
         Isolated run time: 0.0019713385263457894 seconds; Isolated performance: 507.2695463694253 iterations/seconds

>>> "0, Serializers.msgspec_yaml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 34 iterations. Performance: 544.0 iterations/seconds
         Isolated run time: 0.0024683665251359344 seconds; Isolated performance: 405.12622003935553 iterations/seconds

>>> "0, Serializers.msgspec_yaml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 44 iterations. Performance: 704.0 iterations/seconds
         Isolated run time: 0.0020248856162652373 seconds; Isolated performance: 493.85505628926904 iterations/seconds

>>> "1, Serializers.marshal, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 91 iterations. Performance: 1456.0 iterations/seconds
         Isolated run time: 0.0008453736081719398 seconds; Isolated performance: 1182.908941482605 iterations/seconds

>>> "1, Serializers.marshal, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 128 iterations. Performance: 2048.0 iterations/seconds
         Isolated run time: 0.0002721799537539482 seconds; Isolated performance: 3674.0398629944807 iterations/seconds

>>> "1, Serializers.marshal, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 40 iterations. Performance: 320.0 iterations/seconds
         Isolated run time: 0.0009854146046563983 seconds; Isolated performance: 1014.8012778323774 iterations/seconds

>>> "1, Serializers.marshal, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 129 iterations. Performance: 2064.0 iterations/seconds
         Isolated run time: 0.00032548257149755955 seconds; Isolated performance: 3072.3611264313054 iterations/seconds

>>> "1, Serializers.pickle, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 81 iterations. Performance: 648.0 iterations/seconds
         Isolated run time: 0.0009101399919018149 seconds; Isolated performance: 1098.7320729752958 iterations/seconds

>>> "1, Serializers.pickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 266 iterations. Performance: 2128.0 iterations/seconds
         Isolated run time: 0.00029449432622641325 seconds; Isolated performance: 3395.6511584239474 iterations/seconds

>>> "1, Serializers.pickle, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 79 iterations. Performance: 632.0 iterations/seconds
         Isolated run time: 0.001000366173684597 seconds; Isolated performance: 999.6339603494905 iterations/seconds

>>> "1, Serializers.pickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.25 seconds to make 205 iterations. Performance: 820.0 iterations/seconds
         Isolated run time: 0.000346930930390954 seconds; Isolated performance: 2882.4181195752913 iterations/seconds

>>> "1, Serializers.cloudpickle, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 34 iterations. Performance: 544.0 iterations/seconds
         Isolated run time: 0.001132475328631699 seconds; Isolated performance: 883.0214440152432 iterations/seconds

>>> "1, Serializers.cloudpickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 165 iterations. Performance: 2640.0 iterations/seconds
         Isolated run time: 0.0004302131710574031 seconds; Isolated performance: 2324.429067436828 iterations/seconds

>>> "1, Serializers.cloudpickle, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 60 iterations. Performance: 480.0 iterations/seconds
         Isolated run time: 0.0011957543902099133 seconds; Isolated performance: 836.2921417536684 iterations/seconds

>>> "1, Serializers.cloudpickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 176 iterations. Performance: 2816.0 iterations/seconds
         Isolated run time: 0.000480318209156394 seconds; Isolated performance: 2081.953132187822 iterations/seconds

>>> "1, Serializers.msgspec_messagepack, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 93 iterations. Performance: 1488.0 iterations/seconds
         Isolated run time: 0.0008552558720111847 seconds; Isolated performance: 1169.2407298513378 iterations/seconds

>>> "1, Serializers.msgspec_messagepack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 199 iterations. Performance: 1592.0 iterations/seconds
         Isolated run time: 0.0002988508203998208 seconds; Isolated performance: 3346.1510952592976 iterations/seconds

>>> "1, Serializers.msgspec_messagepack, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 38 iterations. Performance: 304.0 iterations/seconds
         Isolated run time: 0.0011214744299650192 seconds; Isolated performance: 891.6832816519872 iterations/seconds

>>> "1, Serializers.msgspec_messagepack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 100 iterations. Performance: 800.0 iterations/seconds
         Isolated run time: 0.0003879438154399395 seconds; Isolated performance: 2577.6928519042663 iterations/seconds

>>> "1, Serializers.orjson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 68 iterations. Performance: 544.0 iterations/seconds
         Isolated run time: 0.0009632299188524485 seconds; Isolated performance: 1038.173732385055 iterations/seconds

>>> "1, Serializers.orjson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 235 iterations. Performance: 1253.3333740234375 iterations/seconds
         Isolated run time: 0.0003308698069304228 seconds; Isolated performance: 3022.336819661172 iterations/seconds

>>> "1, Serializers.orjson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 60 iterations. Performance: 960.0 iterations/seconds
         Isolated run time: 0.0011929599568247795 seconds; Isolated performance: 838.2511032990848 iterations/seconds

>>> "1, Serializers.orjson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 101 iterations. Performance: 808.0 iterations/seconds
         Isolated run time: 0.00044839445035904646 seconds; Isolated performance: 2230.1792522170203 iterations/seconds

>>> "1, Serializers.msgspec_json, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 57 iterations. Performance: 912.0 iterations/seconds
         Isolated run time: 0.0008861626265570521 seconds; Isolated performance: 1128.4610409324443 iterations/seconds

>>> "1, Serializers.msgspec_json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 250 iterations. Performance: 4000.0 iterations/seconds
         Isolated run time: 0.000300672953017056 seconds; Isolated performance: 3325.872812854151 iterations/seconds

>>> "1, Serializers.msgspec_json, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 76 iterations. Performance: 1216.0 iterations/seconds
         Isolated run time: 0.0011155385291203856 seconds; Isolated performance: 896.4280245779686 iterations/seconds

>>> "1, Serializers.msgspec_json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 214 iterations. Performance: 3424.0 iterations/seconds
         Isolated run time: 0.00038392271380871534 seconds; Isolated performance: 2604.690902706625 iterations/seconds

>>> "1, Serializers.cbor, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 101 iterations. Performance: 808.0 iterations/seconds
         Isolated run time: 0.0008222202304750681 seconds; Isolated performance: 1216.219162379662 iterations/seconds

>>> "1, Serializers.cbor, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 313 iterations. Performance: 2504.0 iterations/seconds
         Isolated run time: 0.00027243385557085276 seconds; Isolated performance: 3670.6157459931655 iterations/seconds

>>> "1, Serializers.cbor, universal=True, optimized=False": benchmark_single_item()
         It was used 0.25 seconds to make 43 iterations. Performance: 172.0 iterations/seconds
         Isolated run time: 0.0011006708955392241 seconds; Isolated performance: 908.5367879288705 iterations/seconds

>>> "1, Serializers.cbor, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 93 iterations. Performance: 1488.0 iterations/seconds
         Isolated run time: 0.0003714247141033411 seconds; Isolated performance: 2692.3356524998794 iterations/seconds

>>> "1, Serializers.msgpack, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 48 iterations. Performance: 768.0 iterations/seconds
         Isolated run time: 0.0010566673008725047 seconds; Isolated performance: 946.3716717402784 iterations/seconds

>>> "1, Serializers.msgpack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 202 iterations. Performance: 3232.0 iterations/seconds
         Isolated run time: 0.0003928329097107053 seconds; Isolated performance: 2545.611569907501 iterations/seconds

>>> "1, Serializers.msgpack, universal=True, optimized=False": benchmark_single_item()
         It was used 0.1875 seconds to make 53 iterations. Performance: 282.6666564941406 iterations/seconds
         Isolated run time: 0.0013008699752390385 seconds; Isolated performance: 768.7163352480691 iterations/seconds

>>> "1, Serializers.msgpack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 48 iterations. Performance: 768.0 iterations/seconds
         Isolated run time: 0.0005075300578027964 seconds; Isolated performance: 1970.3266528276351 iterations/seconds

>>> "1, Serializers.ujson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 28 iterations. Performance: 448.0 iterations/seconds
         Isolated run time: 0.0010799691081047058 seconds; Isolated performance: 925.9524115045774 iterations/seconds

>>> "1, Serializers.ujson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 123 iterations. Performance: 1968.0 iterations/seconds
         Isolated run time: 0.00039702479261904955 seconds; Isolated performance: 2518.734392890957 iterations/seconds

>>> "1, Serializers.ujson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 54 iterations. Performance: 864.0 iterations/seconds
         Isolated run time: 0.001291462336666882 seconds; Isolated performance: 774.3160381903871 iterations/seconds

>>> "1, Serializers.ujson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 174 iterations. Performance: 1392.0 iterations/seconds
         Isolated run time: 0.0004812729312106967 seconds; Isolated performance: 2077.8230711716665 iterations/seconds

>>> "1, Serializers.cbor2, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 56 iterations. Performance: 448.0 iterations/seconds
         Isolated run time: 0.0014327315147966146 seconds; Isolated performance: 697.9674765805346 iterations/seconds

>>> "1, Serializers.cbor2, universal=False, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 121 iterations. Performance: 645.3333129882812 iterations/seconds
         Isolated run time: 0.0006749002495780587 seconds; Isolated performance: 1481.7004448067557 iterations/seconds

>>> "1, Serializers.cbor2, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 47 iterations. Performance: 376.0 iterations/seconds
         Isolated run time: 0.0017391329165548086 seconds; Isolated performance: 574.9991794652374 iterations/seconds

>>> "1, Serializers.cbor2, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 54 iterations. Performance: 432.0 iterations/seconds
         Isolated run time: 0.0008115472737699747 seconds; Isolated performance: 1232.2141079404826 iterations/seconds

>>> "1, Serializers.json, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 31 iterations. Performance: 248.0 iterations/seconds
         Isolated run time: 0.0013661317061632872 seconds; Isolated performance: 731.9938447285219 iterations/seconds

>>> "1, Serializers.json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 51 iterations. Performance: 816.0 iterations/seconds
         Isolated run time: 0.0006226717960089445 seconds; Isolated performance: 1605.9824877400345 iterations/seconds

>>> "1, Serializers.json, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 43 iterations. Performance: 344.0 iterations/seconds
         Isolated run time: 0.0016000053146854043 seconds; Isolated performance: 624.9979239579098 iterations/seconds

>>> "1, Serializers.json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 70 iterations. Performance: 1120.0 iterations/seconds
         Isolated run time: 0.0007193082710728049 seconds; Isolated performance: 1390.224525721858 iterations/seconds

>>> "1, Serializers.simplejson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0 seconds to make 22 iterations. Performance: 0.0 iterations/seconds
         Isolated run time: 0.0015618717297911644 seconds; Isolated performance: 640.2574429935476 iterations/seconds

>>> "1, Serializers.simplejson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 109 iterations. Performance: 1744.0 iterations/seconds
         Isolated run time: 0.000766547629609704 seconds; Isolated performance: 1304.550378049125 iterations/seconds

>>> "1, Serializers.simplejson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 49 iterations. Performance: 784.0 iterations/seconds
         Isolated run time: 0.0017996785463765264 seconds; Isolated performance: 555.6547873582205 iterations/seconds

>>> "1, Serializers.simplejson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 93 iterations. Performance: 1488.0 iterations/seconds
         Isolated run time: 0.0008633049437776208 seconds; Isolated performance: 1158.339248729694 iterations/seconds

>>> "1, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 10 iterations. Performance: 160.0 iterations/seconds
         Isolated run time: 0.010459218523465097 seconds; Isolated performance: 95.60943752695435 iterations/seconds

>>> "1, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 11 iterations. Performance: 88.0 iterations/seconds
         Isolated run time: 0.009011557092890143 seconds; Isolated performance: 110.96861393565058 iterations/seconds

>>> "1, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 9 iterations. Performance: 72.0 iterations/seconds
         Isolated run time: 0.01117266295477748 seconds; Isolated performance: 89.50417676140455 iterations/seconds

>>> "1, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.25 seconds to make 10 iterations. Performance: 40.0 iterations/seconds
         Isolated run time: 0.009097612579353154 seconds; Isolated performance: 109.9189475565798 iterations/seconds

>>> "1, Serializers.msgspec_yaml, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 7 iterations. Performance: 56.0 iterations/seconds
         Isolated run time: 0.016271531814709306 seconds; Isolated performance: 61.457028839534935 iterations/seconds

>>> "1, Serializers.msgspec_yaml, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 7 iterations. Performance: 112.0 iterations/seconds
         Isolated run time: 0.006149194668978453 seconds; Isolated performance: 162.62292118426737 iterations/seconds

>>> "1, Serializers.msgspec_yaml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 7 iterations. Performance: 56.0 iterations/seconds
         Isolated run time: 0.007870391476899385 seconds; Isolated performance: 127.05848278768967 iterations/seconds

>>> "1, Serializers.msgspec_yaml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 9 iterations. Performance: 144.0 iterations/seconds
         Isolated run time: 0.005934227025136352 seconds; Isolated performance: 168.513943899378 iterations/seconds
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
    def __init__(self, serializer_type: Serializers, single_benchmarking_item: Any, universal: bool = False, optimized: bool = True,
                 test_case: Optional[TestCase] = None) -> None:
        self.serializer: Serializer = Serializer(serializer_type)
        self.transport: List = [None] * 1024
        self.transport.clear()
        self.universal: bool = universal
        self.optimized: bool = optimized
        self.test_case: Optional[TestCase] = test_case
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
            if self.test_case is not None:
                self.test_case.assertEqual(self.single_benchmarking_item, received_obj)


def benchmark(test_case: TestCase):
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
        measure_func_isolated_performance(func, 0.1, 'DataClass', do_print=True)
        print()
    
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func_marshal, 0.1, 'DataClass', do_print=True)
        print()
    
    obj = test_data_factory(TestDataType.small)
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func, 0.1, 'TestDataType.small', do_print=True)
        print()
    
    obj = test_data_factory(TestDataType.small)
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func_marshal, 0.1, 'TestDataType.small', do_print=True)
        print()
    
    obj = test_data_factory(TestDataType.deep_small)
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func, 0.1, 'TestDataType.deep_small', do_print=True)
        print()
    
    obj = test_data_factory(TestDataType.deep_small)
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func_marshal, 0.1, 'TestDataType.deep_small', do_print=True)
        print()
    
    obj = test_data_factory(TestDataType.large)
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func, 0.1, 'TestDataType.large', do_print=True)
        print()
    
    obj = test_data_factory(TestDataType.large)
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func_marshal, 0.1, 'TestDataType.large', do_print=True)
        print()
    
    obj = test_data_factory(TestDataType.deep_large)
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func, 0.1, 'TestDataType.deep_large', do_print=True)
        print()
    
    obj = test_data_factory(TestDataType.deep_large)
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func_marshal, 0.1, 'TestDataType.deep_large', do_print=True)
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
                                                0.1)
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
            # test_data_factory(TestDataType.deep_small),
            # test_data_factory(TestDataType.large),
            # test_data_factory(TestDataType.deep_large),
        )
        best_serializers, serializers_data = get_most_efficient_serializers({DataFormats.any,
                                                    Tags.decode_str_as_str,
                                                    Tags.decode_list_as_list,
                                                    Tags.deep,
                                                    Tags.current_platform,
                                                },
                                                test_data_factory(TestDataType.deep_small),
                                                0.1)
        sorted_serializers = sorted(serializers_data, key=lambda x: x[1], reverse=True)
        for data_item_index, data_item in enumerate(data_set):
            for serializer_type, serializer_performance, serialized_data_size in sorted_serializers:
                for universal in {False, True}:
                    for optimized in {False, True}:
                        if serializer_type in {
                                Serializers.msgspec_toml,
                            }:
                            universal = True
                            codec: CoDec = CoDec(serializer_type, data_item, universal=universal, optimized=optimized, test_case=test_case)
                        else:
                            codec = CoDec(serializer_type, data_item, universal=universal, optimized=optimized, test_case=test_case)

                        measure_func_isolated_performance(codec.benchmark_single_item, 0.1, f'{data_item_index}, {serializer_type}, {universal=}, {optimized=}', do_print=True)
                        print()


class TestBenchmark(TestCase):
    def test_benchmark(self):
        benchmark(self)


if __name__ == '__main__':
    main()
