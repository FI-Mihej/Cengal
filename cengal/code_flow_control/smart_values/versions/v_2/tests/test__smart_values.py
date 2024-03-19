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


from cengal.code_flow_control.smart_values.versions.v_2 import *
from unittest import TestCase, main


class TestSmartValues(TestCase):
    def test__value_existence(self):
        ve_classess = (
            ValueExistence,
            ValueHolder,
            ResultExistence,
            ErrorExistence,
        )
        for ve_class in ve_classess:
            value_existence = ve_class()
            self.assertEqual(value_existence.existence, False)
            self.assertEqual(value_existence[0], False)
            self.assertEqual(value_existence.value, None)
            self.assertEqual(value_existence[1], None)
            self.assertEqual(tuple(value_existence), (False, None))
            self.assertEqual(tuple(value_existence), value_existence.to_tuple())
            self.assertEqual(tuple(ve_class.from_tuple((True, 30))), (True, 30))

        for ve_class in ve_classess:
            value_existence = ve_class(True, 10)
            self.assertEqual(value_existence.existence, True)
            self.assertEqual(value_existence[0], True)
            self.assertEqual(value_existence.value, 10)
            self.assertEqual(value_existence[1], 10)
            self.assertEqual(tuple(value_existence), (True, 10))
            self.assertEqual(tuple(value_existence), value_existence.to_tuple())
            self.assertEqual(tuple(ve_class.from_tuple((True, 30))), (True, 30))

        for ve_class in ve_classess:
            value_existence = ve_class[int]()
            self.assertEqual(value_existence.existence, False)
            self.assertEqual(value_existence[0], False)
            self.assertEqual(value_existence.value, None)
            self.assertEqual(value_existence[1], None)
            self.assertEqual(tuple(value_existence), (False, None))
            self.assertEqual(tuple(value_existence), value_existence.to_tuple())
            self.assertEqual(tuple(ve_class.from_tuple((True, 30))), (True, 30))

        for ve_class in ve_classess:
            value_existence = ve_class[int](True, 10)
            self.assertEqual(value_existence.existence, True)
            self.assertEqual(value_existence[0], True)
            self.assertEqual(value_existence.value, 10)
            self.assertEqual(value_existence[1], 10)
            self.assertEqual(tuple(value_existence), (True, 10))
            self.assertEqual(tuple(value_existence), value_existence.to_tuple())
            self.assertEqual(tuple(ve_class.from_tuple((True, 30))), (True, 30))
            
        value_cache = ValueCache()
        self.assertFalse(value_cache)
        self.assertEqual(value_cache.existence, False)
        self.assertEqual(value_cache[0], False)
        self.assertEqual(value_cache.get(), None)
        self.assertEqual(value_cache.value, None)
        self.assertEqual(value_cache[1], None)
        self.assertEqual(tuple(value_cache), (False, None))
        self.assertEqual(tuple(value_cache), value_cache.to_tuple())
        value_cache.set(10)
        self.assertTrue(value_cache)
        self.assertEqual(value_cache.existence, True)
        self.assertEqual(value_cache[0], True)
        self.assertEqual(value_cache.get(), 10)
        self.assertEqual(value_cache.value, 10)
        self.assertEqual(value_cache[1], 10)
        self.assertEqual(tuple(value_cache), (True, 10))
        self.assertEqual(tuple(value_cache), value_cache.to_tuple())
        self.assertEqual(tuple(ValueCache.from_tuple((True, 30))), (True, 30))
            
        value_cache = ValueCache[int]()
        self.assertFalse(value_cache)
        self.assertEqual(value_cache.existence, False)
        self.assertEqual(value_cache[0], False)
        self.assertEqual(value_cache.get(), None)
        self.assertEqual(value_cache.value, None)
        self.assertEqual(value_cache[1], None)
        self.assertEqual(tuple(value_cache), (False, None))
        self.assertEqual(tuple(value_cache), value_cache.to_tuple())
        value_cache.set(10)
        self.assertTrue(value_cache)
        self.assertEqual(value_cache.existence, True)
        self.assertEqual(value_cache[0], True)
        self.assertEqual(value_cache.get(), 10)
        self.assertEqual(value_cache.value, 10)
        self.assertEqual(value_cache[1], 10)
        self.assertEqual(tuple(value_cache), (True, 10))
        self.assertEqual(tuple(value_cache), value_cache.to_tuple())
        self.assertEqual(tuple(ValueCache[int].from_tuple((True, 30))), (True, 30))

        value_type = ValueType(4, 'hello')
        self.assertEqual(value_type.type_id, 4)
        self.assertEqual(value_type[0], 4)
        self.assertEqual(value_type.value, 'hello')
        self.assertEqual(value_type[1], 'hello')
        self.assertEqual(tuple(value_type), (4, 'hello'))
        self.assertEqual(tuple(value_type), value_type.to_tuple())
        self.assertEqual(tuple(ValueType.from_tuple(('nullable', 30))), ('nullable', 30))

        value_type = ValueType[int, str](4, 'hello')
        self.assertEqual(value_type.type_id, 4)
        self.assertEqual(value_type[0], 4)
        self.assertEqual(value_type.value, 'hello')
        self.assertEqual(value_type[1], 'hello')
        self.assertEqual(tuple(value_type), (4, 'hello'))
        self.assertEqual(tuple(value_type), value_type.to_tuple())
        self.assertEqual(tuple(ValueType[str, int].from_tuple(('nullable', 30))), ('nullable', 30))

        value_with_type = ValueWithType(4, 'hello')
        self.assertEqual(value_with_type.type_id, 4)
        self.assertEqual(value_with_type[0], 4)
        self.assertEqual(value_with_type.value, 'hello')
        self.assertEqual(value_with_type[1], 'hello')
        self.assertEqual(tuple(value_with_type), (4, 'hello'))
        self.assertEqual(tuple(value_with_type), value_with_type.to_tuple())
        self.assertEqual(tuple(ValueWithType.from_tuple(('nullable', 30))), ('nullable', 30))

        value_with_type = ValueWithType[int, str](4, 'hello')
        self.assertEqual(value_with_type.type_id, 4)
        self.assertEqual(value_with_type[0], 4)
        self.assertEqual(value_with_type.value, 'hello')
        self.assertEqual(value_with_type[1], 'hello')
        self.assertEqual(tuple(value_with_type), (4, 'hello'))
        self.assertEqual(tuple(value_with_type), value_with_type.to_tuple())
        self.assertEqual(tuple(ValueWithType[str, int].from_tuple(('nullable', 30))), ('nullable', 30))



if '__main__' == __name__:
    main()
