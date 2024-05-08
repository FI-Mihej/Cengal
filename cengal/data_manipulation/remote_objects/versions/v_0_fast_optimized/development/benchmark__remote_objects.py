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
__version__ = "4.4.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.data_manipulation.remote_objects.versions.v_0_fast_optimized import *
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
from typing import Any, Dict, Optional, Callable, Set, Type, Tuple, List, FrozenSet, Deque, Generator


'''
>>> "DataClass": func()
         It was used 0.9375 seconds to make 11027 iterations. Performance: 11762.1337890625 iterations/seconds
         Isolated run time: 5.7861790992319584e-05 seconds; Isolated performance: 17282.56216840466 iterations/seconds

>>> "DataClass": func_marshal()
         It was used 1.625 seconds to make 18837 iterations. Performance: 11592.0 iterations/seconds
         Isolated run time: 4.21315198764205e-05 seconds; Isolated performance: 23735.198799691632 iterations/seconds

>>> "TestDataType.small": func()
         It was used 0.0625 seconds to make 436 iterations. Performance: 6976.0 iterations/seconds
         Isolated run time: 0.0001495529431849718 seconds; Isolated performance: 6686.5952531818 iterations/seconds

>>> "TestDataType.small": func_marshal()
         It was used 0.125 seconds to make 806 iterations. Performance: 6448.0 iterations/seconds
         Isolated run time: 9.687920100986958e-05 seconds; Isolated performance: 10322.133023146267 iterations/seconds

>>> "TestDataType.deep_small": func()
         It was used 0.3125 seconds to make 3 iterations. Performance: 9.600000381469727 iterations/seconds
         Isolated run time: 0.0682142263976857 seconds; Isolated performance: 14.659698611401783 iterations/seconds

>>> "TestDataType.deep_small": func_marshal()
         It was used 0.1875 seconds to make 4 iterations. Performance: 21.33333396911621 iterations/seconds
         Isolated run time: 0.046809628838673234 seconds; Isolated performance: 21.363126023631676 iterations/seconds

>>> "TestDataType.large": func()
         It was used 0.125 seconds to make 463 iterations. Performance: 3704.0 iterations/seconds
         Isolated run time: 0.0001498182537034154 seconds; Isolated performance: 6674.75407889635 iterations/seconds

>>> "TestDataType.large": func_marshal()
         It was used 0.125 seconds to make 409 iterations. Performance: 3272.0 iterations/seconds
         Isolated run time: 0.00010474538430571556 seconds; Isolated performance: 9546.96005583736 iterations/seconds

>>> "TestDataType.deep_large": func()
         It was used 0.4375 seconds to make 2 iterations. Performance: 4.5714287757873535 iterations/seconds
         Isolated run time: 0.19176428171340376 seconds; Isolated performance: 5.214735460978722 iterations/seconds

>>> "TestDataType.deep_large": func_marshal()
         It was used 0.125 seconds to make 2 iterations. Performance: 16.0 iterations/seconds
         Isolated run time: 0.045424150535836816 seconds; Isolated performance: 22.014720984403716 iterations/seconds

=== Serializers on DataClass: ==========================================================================
[(<Serializers.pickle: 16>, 90096.96344699552, 113),
 (<Serializers.cloudpickle: 30>, 1590.1508733308378, 3094)]

=== Serializers on TestDataType: =======================================================================
        == TestDataType.small: ==
                == current_platform: ==
[(<Serializers.msgspec_messagepack: 37>, 264281.2845583485, 77),
 (<Serializers.pickle: 16>, 242557.59281640028, 116),
 (<Serializers.cbor: 8>, 235437.42886117584, 81),
 (<Serializers.msgspec_json: 36>, 235392.2665789762, 151),
 (<Serializers.marshal: 10>, 233289.00877216805, 129),
 (<Serializers.orjson: 3>, 216202.32543857442, 151),
 (<Serializers.cloudpickle: 30>, 134265.97983650374, 116),
 (<Serializers.msgpack: 7>, 126700.80670236146, 77),
 (<Serializers.ujson: 2>, 111768.06443302323, 151),
 (<Serializers.cbor2: 9>, 60586.79065305863, 81),
 (<Serializers.json: 0>, 53587.95348605081, 180),
 (<Serializers.simplejson: 1>, 38485.542462107805, 180),
 (<Serializers.msgspec_toml: 39>, 2995.2429990456294, 236),
 (<Serializers.msgspec_yaml: 38>, 1701.712084367526, 176)]

                == multi_platform: ==
[(<Serializers.msgspec_messagepack: 37>, 280277.166275124, 77),
 (<Serializers.cbor: 8>, 248321.420906568, 81),
 (<Serializers.msgspec_json: 36>, 244985.72831759974, 151),
 (<Serializers.orjson: 3>, 223126.77520910176, 151),
 (<Serializers.msgpack: 7>, 128476.43721208496, 77),
 (<Serializers.ujson: 2>, 110863.61467179474, 151),
 (<Serializers.cbor2: 9>, 59998.56527600249, 81),
 (<Serializers.json: 0>, 56815.49435809247, 180),
 (<Serializers.simplejson: 1>, 39878.06500313363, 180),
 (<Serializers.msgspec_toml: 39>, 3070.2384374619123, 236),
 (<Serializers.msgspec_yaml: 38>, 1948.7032499354586, 176)]

        == TestDataType.deep_small: ==
                == current_platform: ==
[(<Serializers.marshal: 10>, 36731.726327312535, 5389),
 (<Serializers.pickle: 16>, 33338.25425754871, 2220),
 (<Serializers.cloudpickle: 30>, 29990.065818047246, 2220),
 (<Serializers.msgspec_messagepack: 37>, 3278.489620772424, 20529),
 (<Serializers.orjson: 3>, 2296.508689905337, 41007),
 (<Serializers.msgspec_json: 36>, 1885.7607932637213, 41007),
 (<Serializers.msgpack: 7>, 1134.2831971500884, 20529),
 (<Serializers.cbor: 8>, 1130.7240996392713, 20568),
 (<Serializers.ujson: 2>, 680.3920444059388, 41007),
 (<Serializers.cbor2: 9>, 530.3602428068186, 20568),
 (<Serializers.json: 0>, 362.40727817235984, 61194),
 (<Serializers.simplejson: 1>, 259.8560329743179, 61194),
 (<Serializers.msgspec_toml: 39>, 11.016748235791885, 141522),
 (<Serializers.msgspec_yaml: 38>, 1.6041019135139802, 161098)]

                == multi_platform: ==
[(<Serializers.msgspec_messagepack: 37>, 3169.34449118351, 20529),
 (<Serializers.orjson: 3>, 2180.7172334586007, 41007),
 (<Serializers.msgspec_json: 36>, 1941.2351755396178, 41007),
 (<Serializers.cbor: 8>, 1176.7019180387313, 20568),
 (<Serializers.msgpack: 7>, 1163.8960479805235, 20529),
 (<Serializers.ujson: 2>, 666.1748716925019, 41007),
 (<Serializers.cbor2: 9>, 502.8498216157408, 20568),
 (<Serializers.json: 0>, 394.14613701037007, 61194),
 (<Serializers.simplejson: 1>, 229.86431084014092, 61194),
 (<Serializers.msgspec_yaml: 38>, 4.200673009960399, 161098),
 (<Serializers.msgspec_toml: 39>, 4.117517914286068, 141522)]

        == TestDataType.large: ==
                == current_platform: ==
[(<Serializers.pickle: 16>, 209730.5611250824, 1510),
 (<Serializers.msgspec_messagepack: 37>, 188429.4775264878, 2065),
 (<Serializers.marshal: 10>, 186782.37387201286, 1523),
 (<Serializers.cbor: 8>, 168843.9231842752, 2069),
 (<Serializers.msgspec_json: 36>, 131874.88818950826, 2129),
 (<Serializers.orjson: 3>, 127479.25429262573, 2129),
 (<Serializers.cloudpickle: 30>, 117156.77294053465, 1510),
 (<Serializers.msgpack: 7>, 103142.7510386398, 2065),
 (<Serializers.ujson: 2>, 67714.0583969225, 2129),
 (<Serializers.cbor2: 9>, 52458.57690217225, 2069),
 (<Serializers.json: 0>, 38959.093058062645, 2158),
 (<Serializers.simplejson: 1>, 30000.85425201608, 2158),
 (<Serializers.msgspec_yaml: 38>, 1779.7786990982524, 2172),
 (<Serializers.msgspec_toml: 39>, 1739.5148057327879, 2214)]

                == multi_platform: ==
[(<Serializers.msgspec_messagepack: 37>, 184559.10860924306, 2065),
 (<Serializers.cbor: 8>, 171312.16529057478, 2069),
 (<Serializers.msgspec_json: 36>, 136754.08899431647, 2129),
 (<Serializers.orjson: 3>, 131804.06604063095, 2129),
 (<Serializers.msgpack: 7>, 107245.48781462245, 2065),
 (<Serializers.ujson: 2>, 64253.11425771754, 2129),
 (<Serializers.cbor2: 9>, 52158.52055692852, 2069),
 (<Serializers.json: 0>, 38897.17118055398, 2158),
 (<Serializers.simplejson: 1>, 29635.383993320775, 2158),
 (<Serializers.msgspec_yaml: 38>, 1800.2304463410928, 2172),
 (<Serializers.msgspec_toml: 39>, 1686.907006333903, 2214)]

        == TestDataType.deep_large: ==
                == current_platform: ==
[(<Serializers.pickle: 16>, 34074.872434448014, 3614),
 (<Serializers.marshal: 10>, 33723.709212256836, 6783),
 (<Serializers.cloudpickle: 30>, 29355.4552078136, 3614),
 (<Serializers.msgspec_messagepack: 37>, 3093.609070718137, 33245),
 (<Serializers.orjson: 3>, 2067.699896710503, 53659),
 (<Serializers.msgspec_json: 36>, 1801.8228528254015, 53659),
 (<Serializers.cbor: 8>, 1119.428937288957, 33284),
 (<Serializers.msgpack: 7>, 1080.9505480863695, 33245),
 (<Serializers.ujson: 2>, 670.7536823798615, 53659),
 (<Serializers.cbor2: 9>, 520.6760324814609, 33284),
 (<Serializers.json: 0>, 309.5650189873997, 73846),
 (<Serializers.simplejson: 1>, 260.904504549052, 73846),
 (<Serializers.msgspec_toml: 39>, 10.856764919679652, 154174),
 (<Serializers.msgspec_yaml: 38>, 2.0442949508148325, 173930)]

                == multi_platform: ==
[(<Serializers.msgspec_messagepack: 37>, 2992.878216802404, 33245),
 (<Serializers.orjson: 3>, 2100.1540512622414, 53659),
 (<Serializers.msgspec_json: 36>, 1862.659697071547, 53659),
 (<Serializers.cbor: 8>, 1162.0015029027938, 33284),
 (<Serializers.msgpack: 7>, 1097.422977248166, 33245),
 (<Serializers.ujson: 2>, 662.272295289034, 53659),
 (<Serializers.cbor2: 9>, 521.1604962674857, 33284),
 (<Serializers.json: 0>, 383.2150781782557, 73846),
 (<Serializers.simplejson: 1>, 257.69793210384785, 73846),
 (<Serializers.msgspec_toml: 39>, 11.026371032783382, 154174),
 (<Serializers.msgspec_yaml: 38>, 1.6004298905915029, 173930)]

=== RemoteObjectsManager: ==============================================================================
>>> "0, Serializers.marshal, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 231 iterations. Performance: 3696.0 iterations/seconds
         Isolated run time: 0.00027865974698215723 seconds; Isolated performance: 3588.605856532378 iterations/seconds

>>> "0, Serializers.marshal, universal=False, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 819 iterations. Performance: 4368.0 iterations/seconds
         Isolated run time: 9.855825919657946e-05 seconds; Isolated performance: 10146.283103534217 iterations/seconds

>>> "0, Serializers.marshal, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 237 iterations. Performance: 1896.0 iterations/seconds
         Isolated run time: 0.00032929505687206984 seconds; Isolated performance: 3036.7901950878572 iterations/seconds

>>> "0, Serializers.marshal, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 638 iterations. Performance: 5104.0 iterations/seconds
         Isolated run time: 0.00012792437337338924 seconds; Isolated performance: 7817.118611800208 iterations/seconds

>>> "0, Serializers.pickle, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 448 iterations. Performance: 3584.0 iterations/seconds
         Isolated run time: 0.00017481297254562378 seconds; Isolated performance: 5720.399266930913 iterations/seconds

>>> "0, Serializers.pickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 1116 iterations. Performance: 8928.0 iterations/seconds
         Isolated run time: 6.946094799786806e-05 seconds; Isolated performance: 14396.578636253174 iterations/seconds

>>> "0, Serializers.pickle, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 372 iterations. Performance: 5952.0 iterations/seconds
         Isolated run time: 0.00020031642634421587 seconds; Isolated performance: 4992.101837328304 iterations/seconds

>>> "0, Serializers.pickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.25 seconds to make 787 iterations. Performance: 3148.0 iterations/seconds
         Isolated run time: 8.173647802323103e-05 seconds; Isolated performance: 12234.43955727798 iterations/seconds

>>> "0, Serializers.cloudpickle, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 33 iterations. Performance: 264.0 iterations/seconds
         Isolated run time: 0.0009244091343134642 seconds; Isolated performance: 1081.772088657124 iterations/seconds

>>> "0, Serializers.cloudpickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 68 iterations. Performance: 544.0 iterations/seconds
         Isolated run time: 0.0008030018070712686 seconds; Isolated performance: 1245.3272099688404 iterations/seconds

>>> "0, Serializers.cloudpickle, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 35 iterations. Performance: 560.0 iterations/seconds
         Isolated run time: 0.0009731355821713805 seconds; Isolated performance: 1027.6060379671621 iterations/seconds

>>> "0, Serializers.cloudpickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 41 iterations. Performance: 656.0 iterations/seconds
         Isolated run time: 0.0007974191103130579 seconds; Isolated performance: 1254.0456919917697 iterations/seconds

>>> "0, Serializers.msgspec_messagepack, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 207 iterations. Performance: 3312.0 iterations/seconds
         Isolated run time: 0.00028913444839417934 seconds; Isolated performance: 3458.598605437329 iterations/seconds

>>> "0, Serializers.msgspec_messagepack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 712 iterations. Performance: 5696.0 iterations/seconds
         Isolated run time: 0.00010077911429107189 seconds; Isolated performance: 9922.690897161327 iterations/seconds

>>> "0, Serializers.msgspec_messagepack, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 195 iterations. Performance: 3120.0 iterations/seconds
         Isolated run time: 0.00036807823926210403 seconds; Isolated performance: 2716.8136915801538 iterations/seconds

>>> "0, Serializers.msgspec_messagepack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 505 iterations. Performance: 8080.0 iterations/seconds
         Isolated run time: 0.0001444999361410737 seconds; Isolated performance: 6920.4182832559245 iterations/seconds

>>> "0, Serializers.orjson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 218 iterations. Performance: 3488.0 iterations/seconds
         Isolated run time: 0.00032365089282393456 seconds; Isolated performance: 3089.748930629393 iterations/seconds

>>> "0, Serializers.orjson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 680 iterations. Performance: 5440.0 iterations/seconds
         Isolated run time: 0.0001200834522023797 seconds; Isolated performance: 8327.542068949471 iterations/seconds

>>> "0, Serializers.orjson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 190 iterations. Performance: 1520.0 iterations/seconds
         Isolated run time: 0.0003991005942225456 seconds; Isolated performance: 2505.63395413634 iterations/seconds

>>> "0, Serializers.orjson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 502 iterations. Performance: 4016.0 iterations/seconds
         Isolated run time: 0.00016411638353019953 seconds; Isolated performance: 6093.236875500533 iterations/seconds

>>> "0, Serializers.msgspec_json, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 107 iterations. Performance: 856.0 iterations/seconds
         Isolated run time: 0.0002940329723060131 seconds; Isolated performance: 3400.9791220260013 iterations/seconds

>>> "0, Serializers.msgspec_json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 439 iterations. Performance: 7024.0 iterations/seconds
         Isolated run time: 0.00011055089998990297 seconds; Isolated performance: 9045.607046992234 iterations/seconds

>>> "0, Serializers.msgspec_json, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 118 iterations. Performance: 944.0 iterations/seconds
         Isolated run time: 0.0003849391359835863 seconds; Isolated performance: 2597.8132814290925 iterations/seconds

>>> "0, Serializers.msgspec_json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 255 iterations. Performance: 4080.0 iterations/seconds
         Isolated run time: 0.00014836469199508429 seconds; Isolated performance: 6740.148121179213 iterations/seconds

>>> "0, Serializers.msgpack, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 100 iterations. Performance: 1600.0 iterations/seconds
         Isolated run time: 0.0003431891091167927 seconds; Isolated performance: 2913.845379806864 iterations/seconds

>>> "0, Serializers.msgpack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 574 iterations. Performance: 4592.0 iterations/seconds
         Isolated run time: 0.00013982155360281467 seconds; Isolated performance: 7151.9731703215 iterations/seconds

>>> "0, Serializers.msgpack, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 149 iterations. Performance: 2384.0 iterations/seconds
         Isolated run time: 0.0004248755285516381 seconds; Isolated performance: 2353.6304936387105 iterations/seconds

>>> "0, Serializers.msgpack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 362 iterations. Performance: 5792.0 iterations/seconds
         Isolated run time: 0.00018445169553160667 seconds; Isolated performance: 5421.473611928091 iterations/seconds

>>> "0, Serializers.cbor, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 221 iterations. Performance: 3536.0 iterations/seconds
         Isolated run time: 0.0002741225762292743 seconds; Isolated performance: 3648.0030713107217 iterations/seconds

>>> "0, Serializers.cbor, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 767 iterations. Performance: 12272.0 iterations/seconds
         Isolated run time: 9.736267384141684e-05 seconds; Isolated performance: 10270.876512992938 iterations/seconds

>>> "0, Serializers.cbor, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 198 iterations. Performance: 3168.0 iterations/seconds
         Isolated run time: 0.00035613204818218946 seconds; Isolated performance: 2807.947235033511 iterations/seconds

>>> "0, Serializers.cbor, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 502 iterations. Performance: 4016.0 iterations/seconds
         Isolated run time: 0.0001330662053078413 seconds; Isolated performance: 7515.056115762491 iterations/seconds

>>> "0, Serializers.ujson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 119 iterations. Performance: 952.0 iterations/seconds
         Isolated run time: 0.000359206460416317 seconds; Isolated performance: 2783.914294974008 iterations/seconds

>>> "0, Serializers.ujson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 161 iterations. Performance: 2576.0 iterations/seconds
         Isolated run time: 0.00014816620387136936 seconds; Isolated performance: 6749.177436361608 iterations/seconds

>>> "0, Serializers.ujson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0 seconds to make 75 iterations. Performance: 0.0 iterations/seconds
         Isolated run time: 0.00044709735084325075 seconds; Isolated performance: 2236.6493519005285 iterations/seconds

>>> "0, Serializers.ujson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 371 iterations. Performance: 5936.0 iterations/seconds
         Isolated run time: 0.00018646917305886745 seconds; Isolated performance: 5362.816725123271 iterations/seconds

>>> "0, Serializers.cbor2, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 81 iterations. Performance: 648.0 iterations/seconds
         Isolated run time: 0.00045791093725711107 seconds; Isolated performance: 2183.8307815707685 iterations/seconds

>>> "0, Serializers.cbor2, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 157 iterations. Performance: 2512.0 iterations/seconds
         Isolated run time: 0.00022344349417835474 seconds; Isolated performance: 4475.40441343882 iterations/seconds

>>> "0, Serializers.cbor2, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 62 iterations. Performance: 992.0 iterations/seconds
         Isolated run time: 0.0005685817450284958 seconds; Isolated performance: 1758.7620579515487 iterations/seconds

>>> "0, Serializers.cbor2, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 254 iterations. Performance: 4064.0 iterations/seconds
         Isolated run time: 0.00026302854530513287 seconds; Isolated performance: 3801.868724323913 iterations/seconds

>>> "0, Serializers.json, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 181 iterations. Performance: 2896.0 iterations/seconds
         Isolated run time: 0.00042752677109092474 seconds; Isolated performance: 2339.0348104945315 iterations/seconds

>>> "0, Serializers.json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 339 iterations. Performance: 5424.0 iterations/seconds
         Isolated run time: 0.0001999059459194541 seconds; Isolated performance: 5002.352458305162 iterations/seconds

>>> "0, Serializers.json, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 146 iterations. Performance: 1168.0 iterations/seconds
         Isolated run time: 0.0005276835290715098 seconds; Isolated performance: 1895.075258004658 iterations/seconds

>>> "0, Serializers.json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 273 iterations. Performance: 4368.0 iterations/seconds
         Isolated run time: 0.0002550064818933606 seconds; Isolated performance: 3921.4689468881147 iterations/seconds

>>> "0, Serializers.simplejson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 153 iterations. Performance: 2448.0 iterations/seconds
         Isolated run time: 0.0004942043451592326 seconds; Isolated performance: 2023.4544875921722 iterations/seconds

>>> "0, Serializers.simplejson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 256 iterations. Performance: 1365.3333740234375 iterations/seconds
         Isolated run time: 0.000262377317994833 seconds; Isolated performance: 3811.3050611322014 iterations/seconds

>>> "0, Serializers.simplejson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 52 iterations. Performance: 832.0 iterations/seconds
         Isolated run time: 0.0006111447000876069 seconds; Isolated performance: 1636.2737005763956 iterations/seconds

>>> "0, Serializers.simplejson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 181 iterations. Performance: 2896.0 iterations/seconds
         Isolated run time: 0.0003020691219717264 seconds; Isolated performance: 3310.500568454659 iterations/seconds

>>> "0, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 25 iterations. Performance: 200.0 iterations/seconds
         Isolated run time: 0.0033530935179442167 seconds; Isolated performance: 298.23206380867674 iterations/seconds

>>> "0, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 22 iterations. Performance: 176.0 iterations/seconds
         Isolated run time: 0.0030260017374530435 seconds; Isolated performance: 330.46907661120196 iterations/seconds

>>> "0, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 12 iterations. Performance: 96.0 iterations/seconds
         Isolated run time: 0.003631648840382695 seconds; Isolated performance: 275.35701934623785 iterations/seconds

>>> "0, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 12 iterations. Performance: 192.0 iterations/seconds
         Isolated run time: 0.00294125999789685 seconds; Isolated performance: 339.9903445173329 iterations/seconds

>>> "0, Serializers.msgspec_yaml, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 35 iterations. Performance: 560.0 iterations/seconds
         Isolated run time: 0.0023216973058879375 seconds; Isolated performance: 430.7193696025538 iterations/seconds

>>> "0, Serializers.msgspec_yaml, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 30 iterations. Performance: 480.0 iterations/seconds
         Isolated run time: 0.002008201787248254 seconds; Isolated performance: 497.95792750999084 iterations/seconds

>>> "0, Serializers.msgspec_yaml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 26 iterations. Performance: 416.0 iterations/seconds
         Isolated run time: 0.002414867398329079 seconds; Isolated performance: 414.1014122315497 iterations/seconds

>>> "0, Serializers.msgspec_yaml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 40 iterations. Performance: 640.0 iterations/seconds
         Isolated run time: 0.0020103476708754897 seconds; Isolated performance: 497.42639767603396 iterations/seconds

>>> "1, Serializers.marshal, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 98 iterations. Performance: 1568.0 iterations/seconds
         Isolated run time: 0.0008597670821473002 seconds; Isolated performance: 1163.105707074133 iterations/seconds

>>> "1, Serializers.marshal, universal=False, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 250 iterations. Performance: 1333.3333740234375 iterations/seconds
         Isolated run time: 0.00026532530318945646 seconds; Isolated performance: 3768.958286220996 iterations/seconds

>>> "1, Serializers.marshal, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 44 iterations. Performance: 352.0 iterations/seconds
         Isolated run time: 0.000992339919321239 seconds; Isolated performance: 1007.719210453612 iterations/seconds

>>> "1, Serializers.marshal, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 128 iterations. Performance: 2048.0 iterations/seconds
         Isolated run time: 0.0003258147044107318 seconds; Isolated performance: 3069.2291859834845 iterations/seconds

>>> "1, Serializers.pickle, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 78 iterations. Performance: 624.0 iterations/seconds
         Isolated run time: 0.0009396064560860395 seconds; Isolated performance: 1064.2753607351015 iterations/seconds

>>> "1, Serializers.pickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 217 iterations. Performance: 3472.0 iterations/seconds
         Isolated run time: 0.00028946856036782265 seconds; Isolated performance: 3454.6066029737995 iterations/seconds

>>> "1, Serializers.pickle, universal=True, optimized=False": benchmark_single_item()
         It was used 0.1875 seconds to make 78 iterations. Performance: 416.0 iterations/seconds
         Isolated run time: 0.0010301026050001383 seconds; Isolated performance: 970.7770809878359 iterations/seconds

>>> "1, Serializers.pickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 100 iterations. Performance: 1600.0 iterations/seconds
         Isolated run time: 0.0003462409367784858 seconds; Isolated performance: 2888.1622413116593 iterations/seconds

>>> "1, Serializers.cloudpickle, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0 seconds to make 34 iterations. Performance: 0.0 iterations/seconds
         Isolated run time: 0.0011490744072943926 seconds; Isolated performance: 870.2656622164244 iterations/seconds

>>> "1, Serializers.cloudpickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 170 iterations. Performance: 2720.0 iterations/seconds
         Isolated run time: 0.00045263906940817833 seconds; Isolated performance: 2209.2657651216264 iterations/seconds

>>> "1, Serializers.cloudpickle, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 62 iterations. Performance: 992.0 iterations/seconds
         Isolated run time: 0.001217302051372826 seconds; Isolated performance: 821.4887988336492 iterations/seconds

>>> "1, Serializers.cloudpickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 178 iterations. Performance: 1424.0 iterations/seconds
         Isolated run time: 0.0004913246957585216 seconds; Isolated performance: 2035.3139352300834 iterations/seconds

>>> "1, Serializers.msgspec_messagepack, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 88 iterations. Performance: 1408.0 iterations/seconds
         Isolated run time: 0.0008873126935213804 seconds; Isolated performance: 1126.9984158926093 iterations/seconds

>>> "1, Serializers.msgspec_messagepack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 231 iterations. Performance: 1848.0 iterations/seconds
         Isolated run time: 0.00029017264023423195 seconds; Isolated performance: 3446.224286317222 iterations/seconds

>>> "1, Serializers.msgspec_messagepack, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 32 iterations. Performance: 512.0 iterations/seconds
         Isolated run time: 0.0011735244188457727 seconds; Isolated performance: 852.1339513186749 iterations/seconds

>>> "1, Serializers.msgspec_messagepack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 99 iterations. Performance: 1584.0 iterations/seconds
         Isolated run time: 0.0003880535950884223 seconds; Isolated performance: 2576.963627336422 iterations/seconds

>>> "1, Serializers.orjson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 55 iterations. Performance: 880.0 iterations/seconds
         Isolated run time: 0.0010076999897137284 seconds; Isolated performance: 992.3588470851172 iterations/seconds

>>> "1, Serializers.orjson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 200 iterations. Performance: 3200.0 iterations/seconds
         Isolated run time: 0.0003506500506773591 seconds; Isolated performance: 2851.846158494134 iterations/seconds

>>> "1, Serializers.orjson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 58 iterations. Performance: 928.0 iterations/seconds
         Isolated run time: 0.0012051508529111743 seconds; Isolated performance: 829.7716402758958 iterations/seconds

>>> "1, Serializers.orjson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 168 iterations. Performance: 1344.0 iterations/seconds
         Isolated run time: 0.0004326773341745138 seconds; Isolated performance: 2311.191090949694 iterations/seconds

>>> "1, Serializers.msgspec_json, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 39 iterations. Performance: 624.0 iterations/seconds
         Isolated run time: 0.0009179373737424612 seconds; Isolated performance: 1089.3989378850179 iterations/seconds

>>> "1, Serializers.msgspec_json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 128 iterations. Performance: 2048.0 iterations/seconds
         Isolated run time: 0.00030017655808478594 seconds; Isolated performance: 3331.3727307031963 iterations/seconds

>>> "1, Serializers.msgspec_json, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 76 iterations. Performance: 608.0 iterations/seconds
         Isolated run time: 0.0011532200733199716 seconds; Isolated performance: 867.1371780072551 iterations/seconds

>>> "1, Serializers.msgspec_json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 171 iterations. Performance: 2736.0 iterations/seconds
         Isolated run time: 0.0003840400604531169 seconds; Isolated performance: 2603.895017671154 iterations/seconds

>>> "1, Serializers.msgpack, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 80 iterations. Performance: 640.0 iterations/seconds
         Isolated run time: 0.0010623320704326034 seconds; Isolated performance: 941.3252483216285 iterations/seconds

>>> "1, Serializers.msgpack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 183 iterations. Performance: 1464.0 iterations/seconds
         Isolated run time: 0.00040979741606861353 seconds; Isolated performance: 2440.2301253958303 iterations/seconds

>>> "1, Serializers.msgpack, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 64 iterations. Performance: 512.0 iterations/seconds
         Isolated run time: 0.001334214466623962 seconds; Isolated performance: 749.5046898497184 iterations/seconds

>>> "1, Serializers.msgpack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 77 iterations. Performance: 1232.0 iterations/seconds
         Isolated run time: 0.0005106700118631124 seconds; Isolated performance: 1958.2117155296262 iterations/seconds

>>> "1, Serializers.cbor, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 72 iterations. Performance: 1152.0 iterations/seconds
         Isolated run time: 0.0008738961769267917 seconds; Isolated performance: 1144.3006920074583 iterations/seconds

>>> "1, Serializers.cbor, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 287 iterations. Performance: 2296.0 iterations/seconds
         Isolated run time: 0.0002660896861925721 seconds; Isolated performance: 3758.1313815984913 iterations/seconds

>>> "1, Serializers.cbor, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 79 iterations. Performance: 1264.0 iterations/seconds
         Isolated run time: 0.001097478554584086 seconds; Isolated performance: 911.1795358761907 iterations/seconds

>>> "1, Serializers.cbor, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 184 iterations. Performance: 1472.0 iterations/seconds
         Isolated run time: 0.0003760926192626357 seconds; Isolated performance: 2658.9195022241925 iterations/seconds

>>> "1, Serializers.ujson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 32 iterations. Performance: 256.0 iterations/seconds
         Isolated run time: 0.0011149129131808877 seconds; Isolated performance: 896.9310411402116 iterations/seconds

>>> "1, Serializers.ujson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 80 iterations. Performance: 640.0 iterations/seconds
         Isolated run time: 0.00042137084528803825 seconds; Isolated performance: 2373.206431300262 iterations/seconds

>>> "1, Serializers.ujson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 31 iterations. Performance: 496.0 iterations/seconds
         Isolated run time: 0.0013374900445342064 seconds; Isolated performance: 747.6691165564971 iterations/seconds

>>> "1, Serializers.ujson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 145 iterations. Performance: 2320.0 iterations/seconds
         Isolated run time: 0.000512479105964303 seconds; Isolated performance: 1951.2990644142583 iterations/seconds

>>> "1, Serializers.cbor2, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 63 iterations. Performance: 504.0 iterations/seconds
         Isolated run time: 0.0014220329467207193 seconds; Isolated performance: 703.2185873794634 iterations/seconds

>>> "1, Serializers.cbor2, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 101 iterations. Performance: 1616.0 iterations/seconds
         Isolated run time: 0.0006534452550113201 seconds; Isolated performance: 1530.3500826288443 iterations/seconds

>>> "1, Serializers.cbor2, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 35 iterations. Performance: 280.0 iterations/seconds
         Isolated run time: 0.0017752618296071887 seconds; Isolated performance: 563.2971899256514 iterations/seconds

>>> "1, Serializers.cbor2, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 48 iterations. Performance: 384.0 iterations/seconds
         Isolated run time: 0.0007843081839382648 seconds; Isolated performance: 1275.0090085490078 iterations/seconds

>>> "1, Serializers.json, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0 seconds to make 12 iterations. Performance: 0.0 iterations/seconds
         Isolated run time: 0.0014704599743708968 seconds; Isolated performance: 680.0593130240267 iterations/seconds

>>> "1, Serializers.json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 95 iterations. Performance: 1520.0 iterations/seconds
         Isolated run time: 0.0005989919882267714 seconds; Isolated performance: 1669.47141139626 iterations/seconds

>>> "1, Serializers.json, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 52 iterations. Performance: 416.0 iterations/seconds
         Isolated run time: 0.0016266482416540384 seconds; Isolated performance: 614.7610616682323 iterations/seconds

>>> "1, Serializers.json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 111 iterations. Performance: 888.0 iterations/seconds
         Isolated run time: 0.0007070861756801605 seconds; Isolated performance: 1414.2547745868171 iterations/seconds

>>> "1, Serializers.simplejson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.25 seconds to make 52 iterations. Performance: 208.0 iterations/seconds
         Isolated run time: 0.001613980857655406 seconds; Isolated performance: 619.5860349004868 iterations/seconds

>>> "1, Serializers.simplejson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 47 iterations. Performance: 376.0 iterations/seconds
         Isolated run time: 0.000796817010268569 seconds; Isolated performance: 1254.9932884376399 iterations/seconds

>>> "1, Serializers.simplejson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 18 iterations. Performance: 288.0 iterations/seconds
         Isolated run time: 0.0018991591641679406 seconds; Isolated performance: 526.5488111093205 iterations/seconds

>>> "1, Serializers.simplejson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 83 iterations. Performance: 1328.0 iterations/seconds
         Isolated run time: 0.0008720908081158996 seconds; Isolated performance: 1146.6695792384749 iterations/seconds

>>> "1, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 9 iterations. Performance: 72.0 iterations/seconds
         Isolated run time: 0.010422422084957361 seconds; Isolated performance: 95.94698735558751 iterations/seconds

>>> "1, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.25 seconds to make 11 iterations. Performance: 44.0 iterations/seconds
         Isolated run time: 0.009423961746506393 seconds; Isolated performance: 106.11248505658624 iterations/seconds

>>> "1, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 6 iterations. Performance: 48.0 iterations/seconds
         Isolated run time: 0.019937285571359098 seconds; Isolated performance: 50.157279255534654 iterations/seconds

>>> "1, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 6 iterations. Performance: 96.0 iterations/seconds
         Isolated run time: 0.009231918840669096 seconds; Isolated performance: 108.31984306390672 iterations/seconds

>>> "1, Serializers.msgspec_yaml, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 11 iterations. Performance: 176.0 iterations/seconds
         Isolated run time: 0.0069456156343221664 seconds; Isolated performance: 143.97571830183654 iterations/seconds

>>> "1, Serializers.msgspec_yaml, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 14 iterations. Performance: 112.0 iterations/seconds
         Isolated run time: 0.005888314684852958 seconds; Isolated performance: 169.82788005070282 iterations/seconds

>>> "1, Serializers.msgspec_yaml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 13 iterations. Performance: 104.0 iterations/seconds
         Isolated run time: 0.007326763006858528 seconds; Isolated performance: 136.4859214176721 iterations/seconds

>>> "1, Serializers.msgspec_yaml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 15 iterations. Performance: 80.0 iterations/seconds
         Isolated run time: 0.006015603896230459 seconds; Isolated performance: 166.2343494103106 iterations/seconds

>>> "2, Serializers.marshal, universal=False, optimized=False": benchmark_single_item()
         It was used 1.125 seconds to make 2 iterations. Performance: 1.7777777910232544 iterations/seconds
         Isolated run time: 0.5448330085491762 seconds; Isolated performance: 1.835424771092482 iterations/seconds

>>> "2, Serializers.marshal, universal=False, optimized=True": benchmark_single_item()
         It was used 0.25 seconds to make 2 iterations. Performance: 8.0 iterations/seconds
         Isolated run time: 0.12533736240584403 seconds; Isolated performance: 7.978466921634961 iterations/seconds

>>> "2, Serializers.marshal, universal=True, optimized=False": benchmark_single_item()
         It was used 1.4375 seconds to make 2 iterations. Performance: 1.39130437374115 iterations/seconds
         Isolated run time: 0.687125772703439 seconds; Isolated performance: 1.455337639375079 iterations/seconds

>>> "2, Serializers.marshal, universal=True, optimized=True": benchmark_single_item()
         It was used 0.3125 seconds to make 2 iterations. Performance: 6.400000095367432 iterations/seconds
         Isolated run time: 0.15405131387524307 seconds; Isolated performance: 6.491343532518263 iterations/seconds

>>> "2, Serializers.pickle, universal=False, optimized=False": benchmark_single_item()
         It was used 1.1875 seconds to make 2 iterations. Performance: 1.6842105388641357 iterations/seconds
         Isolated run time: 0.4811697870027274 seconds; Isolated performance: 2.078268476142563 iterations/seconds

>>> "2, Serializers.pickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.25 seconds to make 2 iterations. Performance: 8.0 iterations/seconds
         Isolated run time: 0.1406483673490584 seconds; Isolated performance: 7.109929669629363 iterations/seconds

>>> "2, Serializers.pickle, universal=True, optimized=False": benchmark_single_item()
         It was used 1.3125 seconds to make 2 iterations. Performance: 1.523809552192688 iterations/seconds
         Isolated run time: 0.5264779306016862 seconds; Isolated performance: 1.899414850793742 iterations/seconds

>>> "2, Serializers.pickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.4375 seconds to make 2 iterations. Performance: 4.5714287757873535 iterations/seconds
         Isolated run time: 0.15968615654855967 seconds; Isolated performance: 6.262283604376849 iterations/seconds

>>> "2, Serializers.cloudpickle, universal=False, optimized=False": benchmark_single_item()
         It was used 1.1875 seconds to make 2 iterations. Performance: 1.6842105388641357 iterations/seconds
         Isolated run time: 0.5853171941125765 seconds; Isolated performance: 1.7084753532930825 iterations/seconds

>>> "2, Serializers.cloudpickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.8125 seconds to make 2 iterations. Performance: 2.461538553237915 iterations/seconds
         Isolated run time: 0.32653530209790915 seconds; Isolated performance: 3.062456014940025 iterations/seconds

>>> "2, Serializers.cloudpickle, universal=True, optimized=False": benchmark_single_item()
         It was used 2.0 seconds to make 2 iterations. Performance: 1.0 iterations/seconds
         Isolated run time: 0.6610871100565419 seconds; Isolated performance: 1.512659957799618 iterations/seconds

>>> "2, Serializers.cloudpickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.5 seconds to make 2 iterations. Performance: 4.0 iterations/seconds
         Isolated run time: 0.24586357560474426 seconds; Isolated performance: 4.067296253787597 iterations/seconds

>>> "2, Serializers.msgspec_messagepack, universal=False, optimized=False": benchmark_single_item()
         It was used 1.5 seconds to make 2 iterations. Performance: 1.3333333730697632 iterations/seconds
         Isolated run time: 0.48115537979174405 seconds; Isolated performance: 2.0783307056294884 iterations/seconds

>>> "2, Serializers.msgspec_messagepack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.25 seconds to make 2 iterations. Performance: 8.0 iterations/seconds
         Isolated run time: 0.13533596089109778 seconds; Isolated performance: 7.389019100434663 iterations/seconds

>>> "2, Serializers.msgspec_messagepack, universal=True, optimized=False": benchmark_single_item()
         It was used 1.75 seconds to make 2 iterations. Performance: 1.1428571939468384 iterations/seconds
         Isolated run time: 0.6366218064213172 seconds; Isolated performance: 1.5707913079845064 iterations/seconds

>>> "2, Serializers.msgspec_messagepack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.3125 seconds to make 2 iterations. Performance: 6.400000095367432 iterations/seconds
         Isolated run time: 0.18560003058519214 seconds; Isolated performance: 5.387930146600868 iterations/seconds

>>> "2, Serializers.orjson, universal=False, optimized=False": benchmark_single_item()
         It was used 1.625 seconds to make 2 iterations. Performance: 1.2307692766189575 iterations/seconds
         Isolated run time: 0.48893960006535053 seconds; Isolated performance: 2.0452423977651684 iterations/seconds

>>> "2, Serializers.orjson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.3125 seconds to make 2 iterations. Performance: 6.400000095367432 iterations/seconds
         Isolated run time: 0.15625350852496922 seconds; Isolated performance: 6.399856294044115 iterations/seconds

>>> "2, Serializers.orjson, universal=True, optimized=False": benchmark_single_item()
         It was used 1.75 seconds to make 2 iterations. Performance: 1.1428571939468384 iterations/seconds
         Isolated run time: 0.6158275221241638 seconds; Isolated performance: 1.6238312905384877 iterations/seconds

>>> "2, Serializers.orjson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.4375 seconds to make 2 iterations. Performance: 4.5714287757873535 iterations/seconds
         Isolated run time: 0.20708424062468112 seconds; Isolated performance: 4.828952686034651 iterations/seconds

>>> "2, Serializers.msgspec_json, universal=False, optimized=False": benchmark_single_item()
         It was used 0.9375 seconds to make 2 iterations. Performance: 2.133333444595337 iterations/seconds
         Isolated run time: 0.44886281504295766 seconds; Isolated performance: 2.227852177740089 iterations/seconds

>>> "2, Serializers.msgspec_json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.3125 seconds to make 2 iterations. Performance: 6.400000095367432 iterations/seconds
         Isolated run time: 0.12965471181087196 seconds; Isolated performance: 7.71279335731898 iterations/seconds

>>> "2, Serializers.msgspec_json, universal=True, optimized=False": benchmark_single_item()
         It was used 1.375 seconds to make 2 iterations. Performance: 1.454545497894287 iterations/seconds
         Isolated run time: 0.5817440240643919 seconds; Isolated performance: 1.718969097462207 iterations/seconds

>>> "2, Serializers.msgspec_json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.4375 seconds to make 2 iterations. Performance: 4.5714287757873535 iterations/seconds
         Isolated run time: 0.22124416823498905 seconds; Isolated performance: 4.5198931478179105 iterations/seconds

>>> "2, Serializers.msgpack, universal=False, optimized=False": benchmark_single_item()
         It was used 1.4375 seconds to make 2 iterations. Performance: 1.39130437374115 iterations/seconds
         Isolated run time: 0.6646169220330194 seconds; Isolated performance: 1.5046261490620279 iterations/seconds

>>> "2, Serializers.msgpack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.5625 seconds to make 2 iterations. Performance: 3.555555582046509 iterations/seconds
         Isolated run time: 0.1992311867652461 seconds; Isolated performance: 5.019294500204423 iterations/seconds

>>> "2, Serializers.msgpack, universal=True, optimized=False": benchmark_single_item()
         It was used 1.6875 seconds to make 2 iterations. Performance: 1.185185194015503 iterations/seconds
         Isolated run time: 0.8098821417661384 seconds; Isolated performance: 1.2347475619344623 iterations/seconds

>>> "2, Serializers.msgpack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.625 seconds to make 2 iterations. Performance: 3.200000047683716 iterations/seconds
         Isolated run time: 0.27630055823829025 seconds; Isolated performance: 3.619247121236609 iterations/seconds

>>> "2, Serializers.cbor, universal=False, optimized=False": benchmark_single_item()
         It was used 1.3125 seconds to make 2 iterations. Performance: 1.523809552192688 iterations/seconds
         Isolated run time: 0.43526260450016707 seconds; Isolated performance: 2.297463622330588 iterations/seconds

>>> "2, Serializers.cbor, universal=False, optimized=True": benchmark_single_item()
         It was used 0.4375 seconds to make 2 iterations. Performance: 4.5714287757873535 iterations/seconds
         Isolated run time: 0.17275596654508263 seconds; Isolated performance: 5.788512084409187 iterations/seconds

>>> "2, Serializers.cbor, universal=True, optimized=False": benchmark_single_item()
         It was used 1.5 seconds to make 2 iterations. Performance: 1.3333333730697632 iterations/seconds
         Isolated run time: 0.5544332133140415 seconds; Isolated performance: 1.803643750024732 iterations/seconds

>>> "2, Serializers.cbor, universal=True, optimized=True": benchmark_single_item()
         It was used 0.4375 seconds to make 2 iterations. Performance: 4.5714287757873535 iterations/seconds
         Isolated run time: 0.1828704052604735 seconds; Isolated performance: 5.468353387064675 iterations/seconds

>>> "2, Serializers.ujson, universal=False, optimized=False": benchmark_single_item()
         It was used 1.75 seconds to make 2 iterations. Performance: 1.1428571939468384 iterations/seconds
         Isolated run time: 0.6465606143465266 seconds; Isolated performance: 1.5466453999996452 iterations/seconds

>>> "2, Serializers.ujson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.375 seconds to make 2 iterations. Performance: 5.333333492279053 iterations/seconds
         Isolated run time: 0.19276346173137426 seconds; Isolated performance: 5.187705133629272 iterations/seconds

>>> "2, Serializers.ujson, universal=True, optimized=False": benchmark_single_item()
         It was used 1.875 seconds to make 2 iterations. Performance: 1.0666667222976685 iterations/seconds
         Isolated run time: 0.6826941409381106 seconds; Isolated performance: 1.4647847989816785 iterations/seconds

>>> "2, Serializers.ujson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.625 seconds to make 2 iterations. Performance: 3.200000047683716 iterations/seconds
         Isolated run time: 0.24205546674784273 seconds; Isolated performance: 4.131284508611134 iterations/seconds

>>> "2, Serializers.cbor2, universal=False, optimized=False": benchmark_single_item()
         It was used 2.0 seconds to make 2 iterations. Performance: 1.0 iterations/seconds
         Isolated run time: 0.7341758331749588 seconds; Isolated performance: 1.3620715294801777 iterations/seconds

>>> "2, Serializers.cbor2, universal=False, optimized=True": benchmark_single_item()
         It was used 0.6875 seconds to make 2 iterations. Performance: 2.909090995788574 iterations/seconds
         Isolated run time: 0.3302569752559066 seconds; Isolated performance: 3.0279451303795444 iterations/seconds

>>> "2, Serializers.cbor2, universal=True, optimized=False": benchmark_single_item()
         It was used 2.125 seconds to make 2 iterations. Performance: 0.9411764740943909 iterations/seconds
         Isolated run time: 1.051347427885048 seconds; Isolated performance: 0.9511603619097242 iterations/seconds

>>> "2, Serializers.cbor2, universal=True, optimized=True": benchmark_single_item()
         It was used 0.8125 seconds to make 2 iterations. Performance: 2.461538553237915 iterations/seconds
         Isolated run time: 0.39205688796937466 seconds; Isolated performance: 2.5506502517515126 iterations/seconds

>>> "2, Serializers.json, universal=False, optimized=False": benchmark_single_item()
         It was used 1.75 seconds to make 2 iterations. Performance: 1.1428571939468384 iterations/seconds
         Isolated run time: 0.8296469129854813 seconds; Isolated performance: 1.205332032637238 iterations/seconds

>>> "2, Serializers.json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.75 seconds to make 2 iterations. Performance: 2.6666667461395264 iterations/seconds
         Isolated run time: 0.31115128088276833 seconds; Isolated performance: 3.2138707485403777 iterations/seconds

>>> "2, Serializers.json, universal=True, optimized=False": benchmark_single_item()
         It was used 2.0625 seconds to make 2 iterations. Performance: 0.9696969985961914 iterations/seconds
         Isolated run time: 0.8901168562006205 seconds; Isolated performance: 1.1234479979049101 iterations/seconds

>>> "2, Serializers.json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.875 seconds to make 2 iterations. Performance: 2.2857143878936768 iterations/seconds
         Isolated run time: 0.36900080961640924 seconds; Isolated performance: 2.710021154261258 iterations/seconds

>>> "2, Serializers.simplejson, universal=False, optimized=False": benchmark_single_item()
         It was used 1.9375 seconds to make 2 iterations. Performance: 1.0322580337524414 iterations/seconds
         Isolated run time: 0.8695168235572055 seconds; Isolated performance: 1.1500640044076271 iterations/seconds

>>> "2, Serializers.simplejson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.875 seconds to make 2 iterations. Performance: 2.2857143878936768 iterations/seconds
         Isolated run time: 0.38933296559844166 seconds; Isolated performance: 2.5684955766920616 iterations/seconds

>>> "2, Serializers.simplejson, universal=True, optimized=False": benchmark_single_item()
         It was used 2.125 seconds to make 2 iterations. Performance: 0.9411764740943909 iterations/seconds
         Isolated run time: 1.0391524870647117 seconds; Isolated performance: 0.9623226739558642 iterations/seconds

>>> "2, Serializers.simplejson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.9375 seconds to make 2 iterations. Performance: 2.133333444595337 iterations/seconds
         Isolated run time: 0.4413337988080457 seconds; Isolated performance: 2.2658586373869394 iterations/seconds

>>> "2, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 14.1875 seconds to make 2 iterations. Performance: 0.1409691572189331 iterations/seconds
         Isolated run time: 6.777986847329885 seconds; Isolated performance: 0.14753643264945834 iterations/seconds

>>> "2, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 14.0 seconds to make 2 iterations. Performance: 0.1428571492433548 iterations/seconds
         Isolated run time: 6.751577097340487 seconds; Isolated performance: 0.14811354230019974 iterations/seconds

>>> "2, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 17.125 seconds to make 2 iterations. Performance: 0.11678832024335861 iterations/seconds
         Isolated run time: 8.445064898231067 seconds; Isolated performance: 0.11841235230879796 iterations/seconds

>>> "2, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 14.0625 seconds to make 2 iterations. Performance: 0.14222222566604614 iterations/seconds
         Isolated run time: 6.823065337026492 seconds; Isolated performance: 0.14656169193827512 iterations/seconds

>>> "2, Serializers.msgspec_yaml, universal=False, optimized=False": benchmark_single_item()
         It was used 12.0625 seconds to make 2 iterations. Performance: 0.16580310463905334 iterations/seconds
         Isolated run time: 6.052803850849159 seconds; Isolated performance: 0.1652126889688831 iterations/seconds

>>> "2, Serializers.msgspec_yaml, universal=False, optimized=True": benchmark_single_item()
         It was used 8.125 seconds to make 2 iterations. Performance: 0.2461538463830948 iterations/seconds
         Isolated run time: 4.037821230944246 seconds; Isolated performance: 0.24765831442372935 iterations/seconds

>>> "2, Serializers.msgspec_yaml, universal=True, optimized=False": benchmark_single_item()
         It was used 9.9375 seconds to make 2 iterations. Performance: 0.2012578547000885 iterations/seconds
         Isolated run time: 4.6089627663604915 seconds; Isolated performance: 0.21696855685160132 iterations/seconds

>>> "2, Serializers.msgspec_yaml, universal=True, optimized=True": benchmark_single_item()
         It was used 7.6875 seconds to make 2 iterations. Performance: 0.2601625919342041 iterations/seconds
         Isolated run time: 3.64894257648848 seconds; Isolated performance: 0.2740519969931506 iterations/seconds

>>> "3, Serializers.marshal, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 64 iterations. Performance: 512.0 iterations/seconds
         Isolated run time: 0.0009211900178343058 seconds; Isolated performance: 1085.5523623138845 iterations/seconds

>>> "3, Serializers.marshal, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 187 iterations. Performance: 1496.0 iterations/seconds
         Isolated run time: 0.00028857355937361717 seconds; Isolated performance: 3465.3209468345526 iterations/seconds

>>> "3, Serializers.marshal, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0 seconds to make 32 iterations. Performance: 0.0 iterations/seconds
         Isolated run time: 0.0010317008709535003 seconds; Isolated performance: 969.2731955104368 iterations/seconds

>>> "3, Serializers.marshal, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 183 iterations. Performance: 2928.0 iterations/seconds
         Isolated run time: 0.0003472864627838135 seconds; Isolated performance: 2879.467261649361 iterations/seconds

>>> "3, Serializers.pickle, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 80 iterations. Performance: 640.0 iterations/seconds
         Isolated run time: 0.0009705517441034317 seconds; Isolated performance: 1030.3417680463515 iterations/seconds

>>> "3, Serializers.pickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 250 iterations. Performance: 1333.3333740234375 iterations/seconds
         Isolated run time: 0.0003048982471227646 seconds; Isolated performance: 3279.782712549865 iterations/seconds

>>> "3, Serializers.pickle, universal=True, optimized=False": benchmark_single_item()
         It was used 0.1875 seconds to make 39 iterations. Performance: 208.0 iterations/seconds
         Isolated run time: 0.0010680644772946835 seconds; Isolated performance: 936.2730633387555 iterations/seconds

>>> "3, Serializers.pickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 119 iterations. Performance: 1904.0 iterations/seconds
         Isolated run time: 0.0003630165010690689 seconds; Isolated performance: 2754.6957150846874 iterations/seconds

>>> "3, Serializers.cloudpickle, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 57 iterations. Performance: 912.0 iterations/seconds
         Isolated run time: 0.0011688309023156762 seconds; Isolated performance: 855.55575063836 iterations/seconds

>>> "3, Serializers.cloudpickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 117 iterations. Performance: 1872.0 iterations/seconds
         Isolated run time: 0.0004628265742212534 seconds; Isolated performance: 2160.6365228327445 iterations/seconds

>>> "3, Serializers.cloudpickle, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 48 iterations. Performance: 384.0 iterations/seconds
         Isolated run time: 0.0012635209131985903 seconds; Isolated performance: 791.4392152548629 iterations/seconds

>>> "3, Serializers.cloudpickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 124 iterations. Performance: 1984.0 iterations/seconds
         Isolated run time: 0.0005255836294963956 seconds; Isolated performance: 1902.6467794633963 iterations/seconds

>>> "3, Serializers.msgspec_messagepack, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 84 iterations. Performance: 1344.0 iterations/seconds
         Isolated run time: 0.0009125546785071492 seconds; Isolated performance: 1095.8247473301028 iterations/seconds

>>> "3, Serializers.msgspec_messagepack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 128 iterations. Performance: 1024.0 iterations/seconds
         Isolated run time: 0.0003054200205951929 seconds; Isolated performance: 3274.1795971699285 iterations/seconds

>>> "3, Serializers.msgspec_messagepack, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 31 iterations. Performance: 496.0 iterations/seconds
         Isolated run time: 0.0011907817097380757 seconds; Isolated performance: 839.7844809188075 iterations/seconds

>>> "3, Serializers.msgspec_messagepack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 205 iterations. Performance: 3280.0 iterations/seconds
         Isolated run time: 0.00041144550777971745 seconds; Isolated performance: 2430.4555064807923 iterations/seconds

>>> "3, Serializers.orjson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 73 iterations. Performance: 1168.0 iterations/seconds
         Isolated run time: 0.0010283882729709148 seconds; Isolated performance: 972.3953746682623 iterations/seconds

>>> "3, Serializers.orjson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 171 iterations. Performance: 2736.0 iterations/seconds
         Isolated run time: 0.00035725999623537064 seconds; Isolated performance: 2799.08193063177 iterations/seconds

>>> "3, Serializers.orjson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 43 iterations. Performance: 344.0 iterations/seconds
         Isolated run time: 0.0012811199994757771 seconds; Isolated performance: 780.5670041910133 iterations/seconds

>>> "3, Serializers.orjson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 82 iterations. Performance: 1312.0 iterations/seconds
         Isolated run time: 0.00046631647273898125 seconds; Isolated performance: 2144.466383797996 iterations/seconds

>>> "3, Serializers.msgspec_json, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 35 iterations. Performance: 280.0 iterations/seconds
         Isolated run time: 0.0009786691516637802 seconds; Isolated performance: 1021.7957706135484 iterations/seconds

>>> "3, Serializers.msgspec_json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 135 iterations. Performance: 2160.0 iterations/seconds
         Isolated run time: 0.00031530437991023064 seconds; Isolated performance: 3171.5385631011754 iterations/seconds

>>> "3, Serializers.msgspec_json, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 51 iterations. Performance: 816.0 iterations/seconds
         Isolated run time: 0.0011982426512986422 seconds; Isolated performance: 834.5555041929204 iterations/seconds

>>> "3, Serializers.msgspec_json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 167 iterations. Performance: 2672.0 iterations/seconds
         Isolated run time: 0.00042055477388203144 seconds; Isolated performance: 2377.81155298574 iterations/seconds

>>> "3, Serializers.msgpack, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 63 iterations. Performance: 1008.0 iterations/seconds
         Isolated run time: 0.0010996934724971652 seconds; Isolated performance: 909.3443082181956 iterations/seconds

>>> "3, Serializers.msgpack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 158 iterations. Performance: 1264.0 iterations/seconds
         Isolated run time: 0.00041771086398512125 seconds; Isolated performance: 2394.0004587374574 iterations/seconds

>>> "3, Serializers.msgpack, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 39 iterations. Performance: 312.0 iterations/seconds
         Isolated run time: 0.0013445926597341895 seconds; Isolated performance: 743.7196631712153 iterations/seconds

>>> "3, Serializers.msgpack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 103 iterations. Performance: 1648.0 iterations/seconds
         Isolated run time: 0.000528492615558207 seconds; Isolated performance: 1892.174025825839 iterations/seconds

>>> "3, Serializers.cbor, universal=False, optimized=False": benchmark_single_item()
         It was used 0.1875 seconds to make 82 iterations. Performance: 437.3333435058594 iterations/seconds
         Isolated run time: 0.0008930147159844637 seconds; Isolated performance: 1119.802375146299 iterations/seconds

>>> "3, Serializers.cbor, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 256 iterations. Performance: 2048.0 iterations/seconds
         Isolated run time: 0.0002838517539203167 seconds; Isolated performance: 3522.9657248505905 iterations/seconds

>>> "3, Serializers.cbor, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 74 iterations. Performance: 592.0 iterations/seconds
         Isolated run time: 0.0011424608528614044 seconds; Isolated performance: 875.3035147728718 iterations/seconds

>>> "3, Serializers.cbor, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 186 iterations. Performance: 1488.0 iterations/seconds
         Isolated run time: 0.0003994574071839452 seconds; Isolated performance: 2503.3958114575967 iterations/seconds

>>> "3, Serializers.ujson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 37 iterations. Performance: 296.0 iterations/seconds
         Isolated run time: 0.0011476909276098013 seconds; Isolated performance: 871.3147206649227 iterations/seconds

>>> "3, Serializers.ujson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 79 iterations. Performance: 632.0 iterations/seconds
         Isolated run time: 0.00043716176878660917 seconds; Isolated performance: 2287.482738427952 iterations/seconds

>>> "3, Serializers.ujson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.1875 seconds to make 26 iterations. Performance: 138.6666717529297 iterations/seconds
         Isolated run time: 0.0014088944299146533 seconds; Isolated performance: 709.7763883278161 iterations/seconds

>>> "3, Serializers.ujson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 72 iterations. Performance: 1152.0 iterations/seconds
         Isolated run time: 0.0005465447902679443 seconds; Isolated performance: 1829.6762091717105 iterations/seconds

>>> "3, Serializers.cbor2, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 48 iterations. Performance: 768.0 iterations/seconds
         Isolated run time: 0.0014754865551367402 seconds; Isolated performance: 677.7425361950013 iterations/seconds

>>> "3, Serializers.cbor2, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 106 iterations. Performance: 848.0 iterations/seconds
         Isolated run time: 0.000691163819283247 seconds; Isolated performance: 1446.834993528775 iterations/seconds

>>> "3, Serializers.cbor2, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 26 iterations. Performance: 416.0 iterations/seconds
         Isolated run time: 0.0017953373026102781 seconds; Isolated performance: 556.998397207076 iterations/seconds

>>> "3, Serializers.cbor2, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 90 iterations. Performance: 720.0 iterations/seconds
         Isolated run time: 0.0008078644750639796 seconds; Isolated performance: 1237.8313824491465 iterations/seconds

>>> "3, Serializers.json, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 49 iterations. Performance: 784.0 iterations/seconds
         Isolated run time: 0.001386974356137216 seconds; Isolated performance: 720.9938637834974 iterations/seconds

>>> "3, Serializers.json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 76 iterations. Performance: 1216.0 iterations/seconds
         Isolated run time: 0.0006399273406714201 seconds; Isolated performance: 1562.6774110804313 iterations/seconds

>>> "3, Serializers.json, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 30 iterations. Performance: 480.0 iterations/seconds
         Isolated run time: 0.0016540746437385678 seconds; Isolated performance: 604.5676377335565 iterations/seconds

>>> "3, Serializers.json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 105 iterations. Performance: 1680.0 iterations/seconds
         Isolated run time: 0.0007603482808917761 seconds; Isolated performance: 1315.1867704983142 iterations/seconds

>>> "3, Serializers.simplejson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 47 iterations. Performance: 376.0 iterations/seconds
         Isolated run time: 0.0016305390745401382 seconds; Isolated performance: 613.2941035356853 iterations/seconds

>>> "3, Serializers.simplejson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.1875 seconds to make 89 iterations. Performance: 474.6666564941406 iterations/seconds
         Isolated run time: 0.0008145472966134548 seconds; Isolated performance: 1227.6757950797696 iterations/seconds

>>> "3, Serializers.simplejson, universal=True, optimized=False": benchmark_single_item()
         It was used 0.125 seconds to make 20 iterations. Performance: 160.0 iterations/seconds
         Isolated run time: 0.0018861417192965746 seconds; Isolated performance: 530.1828541139231 iterations/seconds

>>> "3, Serializers.simplejson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 35 iterations. Performance: 280.0 iterations/seconds
         Isolated run time: 0.0009606146486476064 seconds; Isolated performance: 1041.000156938937 iterations/seconds

>>> "3, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 5 iterations. Performance: 80.0 iterations/seconds
         Isolated run time: 0.01142996596172452 seconds; Isolated performance: 87.48932440819998 iterations/seconds

>>> "3, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 9 iterations. Performance: 72.0 iterations/seconds
         Isolated run time: 0.012109661474823952 seconds; Isolated performance: 82.57869157440983 iterations/seconds

>>> "3, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 5 iterations. Performance: 80.0 iterations/seconds
         Isolated run time: 0.011553502641618252 seconds; Isolated performance: 86.55383834836205 iterations/seconds

>>> "3, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.0625 seconds to make 9 iterations. Performance: 144.0 iterations/seconds
         Isolated run time: 0.009789641480892897 seconds; Isolated performance: 102.14878675095176 iterations/seconds

>>> "3, Serializers.msgspec_yaml, universal=False, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 13 iterations. Performance: 208.0 iterations/seconds
         Isolated run time: 0.007029578206129372 seconds; Isolated performance: 142.25604590728642 iterations/seconds

>>> "3, Serializers.msgspec_yaml, universal=False, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 14 iterations. Performance: 112.0 iterations/seconds
         Isolated run time: 0.006233323481865227 seconds; Isolated performance: 160.42806103506845 iterations/seconds

>>> "3, Serializers.msgspec_yaml, universal=True, optimized=False": benchmark_single_item()
         It was used 0.0625 seconds to make 11 iterations. Performance: 176.0 iterations/seconds
         Isolated run time: 0.007421185378916562 seconds; Isolated performance: 134.74936266125084 iterations/seconds

>>> "3, Serializers.msgspec_yaml, universal=True, optimized=True": benchmark_single_item()
         It was used 0.125 seconds to make 16 iterations. Performance: 128.0 iterations/seconds
         Isolated run time: 0.0060815856559202075 seconds; Isolated performance: 164.43080087617207 iterations/seconds

>>> "4, Serializers.marshal, universal=False, optimized=False": benchmark_single_item()
         It was used 1.375 seconds to make 2 iterations. Performance: 1.454545497894287 iterations/seconds
         Isolated run time: 0.46657085057813674 seconds; Isolated performance: 2.143297205045881 iterations/seconds

>>> "4, Serializers.marshal, universal=False, optimized=True": benchmark_single_item()
         It was used 0.25 seconds to make 2 iterations. Performance: 8.0 iterations/seconds
         Isolated run time: 0.14080141321755946 seconds; Isolated performance: 7.102201442075364 iterations/seconds

>>> "4, Serializers.marshal, universal=True, optimized=False": benchmark_single_item()
         It was used 1.5 seconds to make 2 iterations. Performance: 1.3333333730697632 iterations/seconds
         Isolated run time: 0.5350036958698183 seconds; Isolated performance: 1.8691459661305379 iterations/seconds

>>> "4, Serializers.marshal, universal=True, optimized=True": benchmark_single_item()
         It was used 0.375 seconds to make 2 iterations. Performance: 5.333333492279053 iterations/seconds
         Isolated run time: 0.16634045774117112 seconds; Isolated performance: 6.011766551442457 iterations/seconds

>>> "4, Serializers.pickle, universal=False, optimized=False": benchmark_single_item()
         It was used 1.4375 seconds to make 2 iterations. Performance: 1.39130437374115 iterations/seconds
         Isolated run time: 0.49470164941158146 seconds; Isolated performance: 2.021420387802307 iterations/seconds

>>> "4, Serializers.pickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.3125 seconds to make 2 iterations. Performance: 6.400000095367432 iterations/seconds
         Isolated run time: 0.14409869408700615 seconds; Isolated performance: 6.939688151484596 iterations/seconds

>>> "4, Serializers.pickle, universal=True, optimized=False": benchmark_single_item()
         It was used 1.4375 seconds to make 2 iterations. Performance: 1.39130437374115 iterations/seconds
         Isolated run time: 0.5738384170690551 seconds; Isolated performance: 1.7426508408196397 iterations/seconds

>>> "4, Serializers.pickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.4375 seconds to make 2 iterations. Performance: 4.5714287757873535 iterations/seconds
         Isolated run time: 0.22333421790972352 seconds; Isolated performance: 4.477594205489019 iterations/seconds

>>> "4, Serializers.cloudpickle, universal=False, optimized=False": benchmark_single_item()
         It was used 1.75 seconds to make 2 iterations. Performance: 1.1428571939468384 iterations/seconds
         Isolated run time: 0.6710207358701155 seconds; Isolated performance: 1.4902669120996621 iterations/seconds

>>> "4, Serializers.cloudpickle, universal=False, optimized=True": benchmark_single_item()
         It was used 0.75 seconds to make 2 iterations. Performance: 2.6666667461395264 iterations/seconds
         Isolated run time: 0.34402123966719955 seconds; Isolated performance: 2.906797269166821 iterations/seconds

>>> "4, Serializers.cloudpickle, universal=True, optimized=False": benchmark_single_item()
         It was used 2.0 seconds to make 2 iterations. Performance: 1.0 iterations/seconds
         Isolated run time: 0.8453295411309227 seconds; Isolated performance: 1.18297060654257 iterations/seconds

>>> "4, Serializers.cloudpickle, universal=True, optimized=True": benchmark_single_item()
         It was used 0.5 seconds to make 2 iterations. Performance: 4.0 iterations/seconds
         Isolated run time: 0.26722323172725737 seconds; Isolated performance: 3.742189605058944 iterations/seconds

>>> "4, Serializers.msgspec_messagepack, universal=False, optimized=False": benchmark_single_item()
         It was used 1.375 seconds to make 2 iterations. Performance: 1.454545497894287 iterations/seconds
         Isolated run time: 0.6841303700348362 seconds; Isolated performance: 1.4617097030045305 iterations/seconds

>>> "4, Serializers.msgspec_messagepack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.375 seconds to make 2 iterations. Performance: 5.333333492279053 iterations/seconds
         Isolated run time: 0.15419654024299234 seconds; Isolated performance: 6.485229814003212 iterations/seconds

>>> "4, Serializers.msgspec_messagepack, universal=True, optimized=False": benchmark_single_item()
         It was used 1.3125 seconds to make 2 iterations. Performance: 1.523809552192688 iterations/seconds
         Isolated run time: 0.6206011123722419 seconds; Isolated performance: 1.6113409725894776 iterations/seconds

>>> "4, Serializers.msgspec_messagepack, universal=True, optimized=True": benchmark_single_item()
         It was used 0.8125 seconds to make 2 iterations. Performance: 2.461538553237915 iterations/seconds
         Isolated run time: 0.2735129155917093 seconds; Isolated performance: 3.6561344748076383 iterations/seconds

>>> "4, Serializers.orjson, universal=False, optimized=False": benchmark_single_item()
         It was used 0.9375 seconds to make 2 iterations. Performance: 2.133333444595337 iterations/seconds
         Isolated run time: 0.5038758490700275 seconds; Isolated performance: 1.9846158569529344 iterations/seconds

>>> "4, Serializers.orjson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.75 seconds to make 2 iterations. Performance: 2.6666667461395264 iterations/seconds
         Isolated run time: 0.2532276412239298 seconds; Isolated performance: 3.9490159730062704 iterations/seconds

>>> "4, Serializers.orjson, universal=True, optimized=False": benchmark_single_item()
         It was used 1.5625 seconds to make 2 iterations. Performance: 1.2799999713897705 iterations/seconds
         Isolated run time: 0.6972597505664453 seconds; Isolated performance: 1.434185752422411 iterations/seconds

>>> "4, Serializers.orjson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.625 seconds to make 2 iterations. Performance: 3.200000047683716 iterations/seconds
         Isolated run time: 0.23136201850138605 seconds; Isolated performance: 4.3222306170967695 iterations/seconds

>>> "4, Serializers.msgspec_json, universal=False, optimized=False": benchmark_single_item()
         It was used 1.1875 seconds to make 2 iterations. Performance: 1.6842105388641357 iterations/seconds
         Isolated run time: 0.4843317193444818 seconds; Isolated performance: 2.064700617488875 iterations/seconds

>>> "4, Serializers.msgspec_json, universal=False, optimized=True": benchmark_single_item()
         It was used 0.5 seconds to make 2 iterations. Performance: 4.0 iterations/seconds
         Isolated run time: 0.17374476825352758 seconds; Isolated performance: 5.755568988073382 iterations/seconds

>>> "4, Serializers.msgspec_json, universal=True, optimized=False": benchmark_single_item()
         It was used 1.75 seconds to make 2 iterations. Performance: 1.1428571939468384 iterations/seconds
         Isolated run time: 0.6465948825934902 seconds; Isolated performance: 1.546563430859525 iterations/seconds

>>> "4, Serializers.msgspec_json, universal=True, optimized=True": benchmark_single_item()
         It was used 0.375 seconds to make 2 iterations. Performance: 5.333333492279053 iterations/seconds
         Isolated run time: 0.20369832182768732 seconds; Isolated performance: 4.909220611281819 iterations/seconds

>>> "4, Serializers.msgpack, universal=False, optimized=False": benchmark_single_item()
         It was used 1.9375 seconds to make 2 iterations. Performance: 1.0322580337524414 iterations/seconds
         Isolated run time: 0.9579148372868076 seconds; Isolated performance: 1.043934138062204 iterations/seconds

>>> "4, Serializers.msgpack, universal=False, optimized=True": benchmark_single_item()
         It was used 0.625 seconds to make 2 iterations. Performance: 3.200000047683716 iterations/seconds
         Isolated run time: 0.20975798915605992 seconds; Isolated performance: 4.767398867730374 iterations/seconds

>>> "4, Serializers.msgpack, universal=True, optimized=False": benchmark_single_item()
         It was used 1.75 seconds to make 2 iterations. Performance: 1.1428571939468384 iterations/seconds
         Isolated run time: 0.7045088306767866 seconds; Isolated performance: 1.4194286238248421 iterations/seconds

>>> "4, Serializers.msgpack, universal=True, optimized=True": benchmark_single_item()
         It was used 1.1875 seconds to make 2 iterations. Performance: 1.6842105388641357 iterations/seconds
         Isolated run time: 0.5202566941734403 seconds; Isolated performance: 1.9221280786953707 iterations/seconds

>>> "4, Serializers.cbor, universal=False, optimized=False": benchmark_single_item()
         It was used 1.0 seconds to make 2 iterations. Performance: 2.0 iterations/seconds
         Isolated run time: 0.4665730781853199 seconds; Isolated performance: 2.1432869720845877 iterations/seconds

>>> "4, Serializers.cbor, universal=False, optimized=True": benchmark_single_item()
         It was used 0.5 seconds to make 2 iterations. Performance: 4.0 iterations/seconds
         Isolated run time: 0.2190139137674123 seconds; Isolated performance: 4.56591995822684 iterations/seconds

>>> "4, Serializers.cbor, universal=True, optimized=False": benchmark_single_item()
         It was used 1.3125 seconds to make 2 iterations. Performance: 1.523809552192688 iterations/seconds
         Isolated run time: 0.5917743726167828 seconds; Isolated performance: 1.68983323082761 iterations/seconds

>>> "4, Serializers.cbor, universal=True, optimized=True": benchmark_single_item()
         It was used 0.875 seconds to make 2 iterations. Performance: 2.2857143878936768 iterations/seconds
         Isolated run time: 0.3202063391217962 seconds; Isolated performance: 3.1229862679877556 iterations/seconds

>>> "4, Serializers.ujson, universal=False, optimized=False": benchmark_single_item()
         It was used 1.5625 seconds to make 2 iterations. Performance: 1.2799999713897705 iterations/seconds
         Isolated run time: 0.7329792814562097 seconds; Isolated performance: 1.3642950425737823 iterations/seconds

>>> "4, Serializers.ujson, universal=False, optimized=True": benchmark_single_item()
         It was used 0.375 seconds to make 2 iterations. Performance: 5.333333492279053 iterations/seconds
         Isolated run time: 0.20154433499556035 seconds; Isolated performance: 4.961687462076412 iterations/seconds

>>> "4, Serializers.ujson, universal=True, optimized=False": benchmark_single_item()
         It was used 2.0 seconds to make 2 iterations. Performance: 1.0 iterations/seconds
         Isolated run time: 0.8367933261906728 seconds; Isolated performance: 1.1950382115883877 iterations/seconds

>>> "4, Serializers.ujson, universal=True, optimized=True": benchmark_single_item()
         It was used 0.625 seconds to make 2 iterations. Performance: 3.200000047683716 iterations/seconds
         Isolated run time: 0.2638940685428679 seconds; Isolated performance: 3.7893993052653867 iterations/seconds

>>> "4, Serializers.cbor2, universal=False, optimized=False": benchmark_single_item()
         It was used 1.9375 seconds to make 2 iterations. Performance: 1.0322580337524414 iterations/seconds
         Isolated run time: 0.7566012882161885 seconds; Isolated performance: 1.3217001022528838 iterations/seconds

>>> "4, Serializers.cbor2, universal=False, optimized=True": benchmark_single_item()
         It was used 0.6875 seconds to make 2 iterations. Performance: 2.909090995788574 iterations/seconds
         Isolated run time: 0.34513379051350057 seconds; Isolated performance: 2.897427106491571 iterations/seconds

>>> "4, Serializers.cbor2, universal=True, optimized=False": benchmark_single_item()
         It was used 2.6875 seconds to make 2 iterations. Performance: 0.7441860437393188 iterations/seconds
         Isolated run time: 1.1810598673764616 seconds; Isolated performance: 0.8466971299442614 iterations/seconds

>>> "4, Serializers.cbor2, universal=True, optimized=True": benchmark_single_item()
         It was used 0.875 seconds to make 2 iterations. Performance: 2.2857143878936768 iterations/seconds
         Isolated run time: 0.43372462363913655 seconds; Isolated performance: 2.3056103930866754 iterations/seconds

>>> "4, Serializers.json, universal=False, optimized=False": benchmark_single_item()
         It was used 2.125 seconds to make 2 iterations. Performance: 0.9411764740943909 iterations/seconds
         Isolated run time: 0.8919488159008324 seconds; Isolated performance: 1.1211405656613158 iterations/seconds

>>> "4, Serializers.json, universal=False, optimized=True": benchmark_single_item()
         It was used 1.0625 seconds to make 2 iterations. Performance: 1.8823529481887817 iterations/seconds
         Isolated run time: 0.31803777848836035 seconds; Isolated performance: 3.1442805466476944 iterations/seconds

>>> "4, Serializers.json, universal=True, optimized=False": benchmark_single_item()
         It was used 2.5 seconds to make 2 iterations. Performance: 0.800000011920929 iterations/seconds
         Isolated run time: 1.0652844853466377 seconds; Isolated performance: 0.9387163839850775 iterations/seconds

>>> "4, Serializers.json, universal=True, optimized=True": benchmark_single_item()
         It was used 1.4375 seconds to make 2 iterations. Performance: 1.39130437374115 iterations/seconds
         Isolated run time: 0.695153959444724 seconds; Isolated performance: 1.4385302513399785 iterations/seconds

>>> "4, Serializers.simplejson, universal=False, optimized=False": benchmark_single_item()
         It was used 2.3125 seconds to make 2 iterations. Performance: 0.8648648858070374 iterations/seconds
         Isolated run time: 1.0442872799467295 seconds; Isolated performance: 0.9575909035787655 iterations/seconds

>>> "4, Serializers.simplejson, universal=False, optimized=True": benchmark_single_item()
         It was used 1.0 seconds to make 2 iterations. Performance: 2.0 iterations/seconds
         Isolated run time: 0.3920300919562578 seconds; Isolated performance: 2.550824593617111 iterations/seconds

>>> "4, Serializers.simplejson, universal=True, optimized=False": benchmark_single_item()
         It was used 2.625 seconds to make 2 iterations. Performance: 0.761904776096344 iterations/seconds
         Isolated run time: 0.977112969965674 seconds; Isolated performance: 1.023423115584199 iterations/seconds

>>> "4, Serializers.simplejson, universal=True, optimized=True": benchmark_single_item()
         It was used 1.375 seconds to make 2 iterations. Performance: 1.454545497894287 iterations/seconds
         Isolated run time: 0.4682101608486846 seconds; Isolated performance: 2.1357930340242626 iterations/seconds

>>> "4, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 19.125 seconds to make 2 iterations. Performance: 0.10457516461610794 iterations/seconds
         Isolated run time: 8.969450570060872 seconds; Isolated performance: 0.11148954913001025 iterations/seconds

>>> "4, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 13.8125 seconds to make 2 iterations. Performance: 0.14479638636112213 iterations/seconds
         Isolated run time: 6.772281531826593 seconds; Isolated performance: 0.14766072486804663 iterations/seconds

>>> "4, Serializers.msgspec_toml, universal=True, optimized=False": benchmark_single_item()
         It was used 15.0 seconds to make 2 iterations. Performance: 0.13333334028720856 iterations/seconds
         Isolated run time: 7.403362989425659 seconds; Isolated performance: 0.1350737497848364 iterations/seconds

>>> "4, Serializers.msgspec_toml, universal=True, optimized=True": benchmark_single_item()
         It was used 12.8125 seconds to make 2 iterations. Performance: 0.15609756112098694 iterations/seconds
         Isolated run time: 6.222542279399931 seconds; Isolated performance: 0.1607060193565185 iterations/seconds

>>> "4, Serializers.msgspec_yaml, universal=False, optimized=False": benchmark_single_item()
         It was used 9.5 seconds to make 2 iterations. Performance: 0.21052631735801697 iterations/seconds
         Isolated run time: 4.623770350939594 seconds; Isolated performance: 0.21627371692384992 iterations/seconds

>>> "4, Serializers.msgspec_yaml, universal=False, optimized=True": benchmark_single_item()
         It was used 8.3125 seconds to make 2 iterations. Performance: 0.24060150980949402 iterations/seconds
         Isolated run time: 4.123945177649148 seconds; Isolated performance: 0.24248624967658985 iterations/seconds

>>> "4, Serializers.msgspec_yaml, universal=True, optimized=False": benchmark_single_item()
         It was used 11.125 seconds to make 2 iterations. Performance: 0.17977528274059296 iterations/seconds
         Isolated run time: 5.063111592549831 seconds; Isolated performance: 0.19750700369145738 iterations/seconds

>>> "4, Serializers.msgspec_yaml, universal=True, optimized=True": benchmark_single_item()
         It was used 8.8125 seconds to make 2 iterations. Performance: 0.22695034742355347 iterations/seconds
         Isolated run time: 4.381748521816917 seconds; Isolated performance: 0.2282193957551321 iterations/seconds
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
        measure_func_isolated_performance(func, 1.0, 'DataClass', do_print=True)
        print()
    
    with DisableGC():
    # with EnableGC():
        # transport.clear()
        # obj_id_result: ResultExistence[int] = rom_src.serialize(obj)
        measure_func_isolated_performance(func_marshal, 1.0, 'DataClass', do_print=True)
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
    
    # print('=== Serializers on DataClass: ==========================================================================')
    
    # with DisableGC():
    #     obj = ({'a': 1, 'b': 2}, dtcl)
    #     best_serializers, serializers_data = get_most_efficient_serializers({DataFormats.binary,
    #                                                 Tags.can_use_bytes,
    #                                                 Tags.decode_str_as_str,
    #                                                 Tags.decode_list_as_list,
    #                                                 Tags.decode_bytes_as_bytes,
    #                                                 Tags.deep,
    #                                                 Tags.can_use_custom_types,
    #                                                 Tags.current_platform,
    #                                                 # Tags.multi_platform,
    #                                             },
    #                                             obj,
    #                                             1.0)
    #     sorted_serializers = sorted(serializers_data, key=lambda x: x[1], reverse=True)
    #     pprint(sorted_serializers)
    #     print()
    
    # print('=== Serializers on TestDataType: =======================================================================')

    # with DisableGC():
    #     test_data_types = (
    #         TestDataType.small,
    #         TestDataType.deep_small,
    #         TestDataType.large,
    #         TestDataType.deep_large,
    #     )
    
    #     for test_data_type in test_data_types:
    #         print(f'\t== {test_data_type}: ==')
    #         print(f'\t\t== current_platform: ==')
    #         best_serializers, serializers_data = get_most_efficient_serializers({DataFormats.any,
    #                                                     Tags.decode_str_as_str,
    #                                                     Tags.decode_list_as_list,
    #                                                     Tags.deep,
    #                                                     Tags.current_platform,
    #                                                 },
    #                                                 test_data_factory(test_data_type),
    #                                                 0.1)
    #         sorted_serializers = sorted(serializers_data, key=lambda x: x[1], reverse=True)
    #         pprint(sorted_serializers)
    #         print()

    #         print(f'\t\t== multi_platform: ==')
    #         best_serializers, serializers_data = get_most_efficient_serializers({DataFormats.any,
    #                                                     Tags.decode_str_as_str,
    #                                                     Tags.decode_list_as_list,
    #                                                     Tags.deep,
    #                                                     Tags.multi_platform,
    #                                                 },
    #                                                 test_data_factory(test_data_type),
    #                                                 0.1)
    #         sorted_serializers = sorted(serializers_data, key=lambda x: x[1], reverse=True)
    #         pprint(sorted_serializers)
    #         print()
    
    # print('=== RemoteObjectsManager: ==============================================================================')

    # with DisableGC():
    #     data_set = (
    #         ({'a': 1, 'b': 2}, dtcl),
    #         test_data_factory(TestDataType.small),
    #         test_data_factory(TestDataType.deep_small),
    #         test_data_factory(TestDataType.large),
    #         test_data_factory(TestDataType.deep_large),
    #     )
    #     best_serializers, serializers_data = get_most_efficient_serializers({DataFormats.any,
    #                                                 Tags.decode_str_as_str,
    #                                                 Tags.decode_list_as_list,
    #                                                 Tags.deep,
    #                                                 Tags.current_platform,
    #                                             },
    #                                             test_data_factory(TestDataType.deep_small),
    #                                             0.1)
    #     sorted_serializers = sorted(serializers_data, key=lambda x: x[1], reverse=True)
    #     for data_item_index, data_item in enumerate(data_set):
    #         for serializer_type, serializer_performance, serialized_data_size in sorted_serializers:
    #             for universal in {False, True}:
    #                 for optimized in {False, True}:
    #                     if serializer_type in {
    #                             Serializers.msgspec_toml,
    #                         }:
    #                         universal = True
    #                         codec: CoDec = CoDec(serializer_type, data_item, universal=universal, optimized=optimized)
    #                     else:
    #                         codec = CoDec(serializer_type, data_item, universal=universal, optimized=optimized)

    #                     measure_func_isolated_performance(codec.benchmark_single_item, 0.1, f'{data_item_index}, {serializer_type}, {universal=}, {optimized=}', do_print=True)
    #                     print()


def main():
    benchmark()


if __name__ == '__main__':
    main()
