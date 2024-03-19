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
from cengal.code_flow_control.smart_values import ResultExistence
from cengal.performance_test_lib import MeasureTime
from cengal.introspection.inspect import cen
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


class TestRemoteObjectsManager(TestCase):
    def setUp(self):
        "Hook method for setting up the test fixture before exercising it."
        self.rom_src: RemoteObjectsManager = RemoteObjectsManager(
            on_new_class_handler=self.on_new_class,
            on_new_obj_info_handler=self.on_new_object,
        )
        self.transport: Deque = deque()
        self.rom_dest: RemoteObjectsManager = RemoteObjectsManager(
            on_new_class_handler=self.on_new_class,
            on_new_obj_info_handler=self.on_new_object,
        )

        self.rom_src_pickle: RemoteObjectsManager = RemoteObjectsManager(
            on_new_class_handler=self.on_new_class_pickle,
            on_new_obj_info_handler=self.on_new_object_pickle,
            serializable_data_types=set(),
        )
        self.transport: Deque = deque()
        self.rom_dest_pickle: RemoteObjectsManager = RemoteObjectsManager(
            on_new_class_handler=self.on_new_class_pickle,
            on_new_obj_info_handler=self.on_new_object_pickle,
            serializable_data_types=set(),
        )

    def on_new_class(
            self,
            class_info,
            obj_type,
            class_id,
            class_name,
            module_importable_str,
            owning_names_path,
            module_importable_str_and_owning_names_path
        ):
        self.transport.append(
            (
                0,
                class_info,
            )
        )
    
    def on_new_object(
            self,
            adjusted_object_info,
            obj,
            object_id,
            type_id,
            serializable,
            known_container,
            known_data,
            class_id,
            is_new_class,
            new_obj_slots,
            new_obj_dict,
            obj_mapping,
            obj_sequence,
            obj_set,
    ):
        self.transport.append(
            (
                1,
                adjusted_object_info,
            )
        )

    def on_new_class_pickle(
            self,
            class_info,
            obj_type,
            class_id,
            class_name,
            module_importable_str,
            owning_names_path,
            module_importable_str_and_owning_names_path
        ):
        self.transport.append(
            pickle_dumps((
                0,
                class_info,
            ))
        )
    
    def on_new_object_pickle(
            self,
            adjusted_object_info,
            obj,
            object_id,
            type_id,
            serializable,
            known_container,
            known_data,
            class_id,
            is_new_class,
            new_obj_slots,
            new_obj_dict,
            obj_mapping,
            obj_sequence,
            obj_set,
    ):
        self.transport.append(
            pickle_dumps((
                1,
                adjusted_object_info,
            ))
        )

    def tearDown(self):
        "Hook method for deconstructing the test fixture after testing it."
        self.rom_src = None
        self.rom_dest = None
    
    def test_transmit_serializable(self):
        obj = {'a': 1, 'b': 2}
        with MeasureTime(f'{cen()} - codec'):
            with MeasureTime(f'{cen()} - serialization'):
                obj_id_exists, obj_id_value  = self.rom_src.serialize(obj)
            
            self.assertTrue(obj_id_exists)
            self.assertEqual(len(self.transport), 5)
            with MeasureTime(f'{cen()} - deserialization'):
                for item in self.transport:
                    item_type, item_info = item
                    self.assertIn(item_type, (0, 1))
                    if 0 == item_type:
                        received_class_exists, received_class_id, received_class_value = self.rom_dest.deserialize_obj(item_info)
                        self.assertTrue(received_class_exists)
                    elif 1 == item_type:
                        received_obj_exists, received_obj_id, received_obj_value = self.rom_dest.deserialize_obj(item_info)
                        self.assertTrue(received_obj_exists)
        
        self.assertDictEqual(obj, received_obj_value)
    
    def test_transmit_simple_class(self):
        obj = ({'a': 1, 'b': 2}, SimpleClass(1, 2))
        with MeasureTime(f'{cen()} - codec'):
            with MeasureTime(f'{cen()} - serialization'):
                obj_id_exists, obj_id_value = self.rom_src.serialize(obj)

            self.assertTrue(obj_id_exists)
            self.assertEqual(len(self.transport), 10)
            with MeasureTime(f'{cen()} - deserialization'):
                for item in self.transport:
                    item_type, item_info = item
                    self.assertIn(item_type, (0, 1))
                    if 0 == item_type:
                        received_class_exists, received_class_id, received_class_value = self.rom_dest.deserialize_class(item_info)
                        self.assertTrue(received_class_exists)
                    elif 1 == item_type:
                        received_obj_exists, received_obj_id, received_obj_value = self.rom_dest.deserialize_obj(item_info)
                        self.assertTrue(received_obj_exists)
        
        dict_, obj_ = received_obj_value
        self.assertEqual(obj_, SimpleClass(1, 2))
    
    def test_transmit_data_class(self):
        dtcl: DataClass = DataClass(5, SimpleClass(1, 2))
        dtcl.add_one()
        obj = ({'a': 1, 'b': 2}, dtcl)
        with MeasureTime(f'{cen()} - codec'):
            with MeasureTime(f'{cen()} - serialization'):
                obj_id_exists, obj_id_value = self.rom_src.serialize(obj)
            
            self.assertTrue(obj_id_exists)
            self.assertEqual(len(self.transport), 14)
            with MeasureTime(f'{cen()} - deserialization'):
                for item in self.transport:
                    item_type, item_info = item
                    self.assertIn(item_type, (0, 1))
                    if 0 == item_type:
                        received_class_exists, received_class_id, received_class_value = self.rom_dest.deserialize_class(item_info)
                        self.assertTrue(received_class_exists)
                    elif 1 == item_type:
                        received_obj_exists, received_obj_id, received_obj_value = self.rom_dest.deserialize_obj(item_info)
                        self.assertTrue(received_obj_exists)
        
        dict_, obj_ = received_obj_value
        self.assertEqual(obj_, dtcl)
    
    def test_transmit_data_class_pickle(self):
        dtcl: DataClass = DataClass(5, SimpleClass(1, 2))
        dtcl.add_one()
        obj = ({'a': 1, 'b': 2}, dtcl)
        with MeasureTime(f'{cen()} - codec'):
            with MeasureTime(f'{cen()} - serialization'):
                obj_id_exists, obj_id_value = self.rom_src_pickle.serialize(obj)
            
            self.assertTrue(obj_id_exists)
            self.assertEqual(len(self.transport), 7)
            with MeasureTime(f'{cen()} - deserialization'):
                for item in self.transport:
                    item_type, item_info = pickle_loads(item)
                    self.assertIn(item_type, (0, 1))
                    if 0 == item_type:
                        received_class_exists, received_class_id, received_class_value = self.rom_dest_pickle.deserialize_class(item_info)
                        self.assertTrue(received_class_exists)
                    elif 1 == item_type:
                        received_obj_exists, received_obj_id, received_obj_value = self.rom_dest_pickle.deserialize_obj(item_info)
                        self.assertTrue(received_obj_exists)
        
        dict_, obj_ = received_obj_value
        self.assertEqual(obj_, dtcl)
    
    def test_transmit_data_class__raw_pickle(self):
        dtcl: DataClass = DataClass(5, SimpleClass(1, 2))
        dtcl.add_one()
        obj = ({'a': 1, 'b': 2}, dtcl)
        with MeasureTime(f'{cen()} - codec'):
            with MeasureTime(f'{cen()} - serialization'):
                pickled_obj = pickle_dumps(obj)
            
            with MeasureTime(f'{cen()} - deserialization'):
                unpickled_obj = pickle_loads(pickled_obj)
        
        self.assertEqual(unpickled_obj, obj)


if __name__ == '__main__':
    main()
