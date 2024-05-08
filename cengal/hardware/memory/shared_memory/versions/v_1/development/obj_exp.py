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


from cengal.data_manipulation.remote_objects.versions.v_0.remote_objects import *
from cengal.code_flow_control.smart_values import ResultExistence
from cengal.performance_test_lib import MeasureTime
from cengal.introspection.inspect import *
from collections import deque
from dataclasses import dataclass
from unittest import TestCase, main
from pickle import loads as pickle_loads, dumps as pickle_dumps
from typing import Any, Dict, Optional, Callable, Set, Type, Tuple, List, FrozenSet, Deque


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


from pprint import pprint

sc = SimpleClass(1, 2)
dc_sc = pickle_dumps(type(sc))

dc = DataClass(1, 'test', 7)
dc_dc = pickle_dumps(type(dc))
d_dc = pickle_dumps(dc)


print(dir(sc))

print('===========================================')
pprint(sc.__dict__)

print('===========================================')
print(dir(dc))

print('===========================================')
pprint(dc.__dict__)


print('===========================================')
print(dir(object))


print('===========================================')
print(set(dir(dc)) - set(dir(object)))


print('===========================================')
print(DataClass.__mro__)


print('===========================================')
print(entity_properties(dc))


print('===========================================')
print(class_properties(DataClass))


print('===========================================')
pprint(class_properties_withot_object_values(DataClass))
