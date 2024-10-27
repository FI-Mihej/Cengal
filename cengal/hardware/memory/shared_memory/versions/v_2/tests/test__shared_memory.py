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
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.unittest.behavior_stabilizer import UnittestTestCaseWithState, UnittestTestCaseState
from cengal.performance_test_lib import PrecisePerformanceTestTracer
from cengal.introspection.inspect import func_name, pdi, pifrl
from threading import Lock, RLock
from pprint import pprint
from typing import Callable


def func_perf_test(func: Callable, *args, **kwargs):
    tr = PrecisePerformanceTestTracer(1.0)
    while tr.iter():
        func(*args, **kwargs)

    with tr as fast_iter:
        for i in fast_iter:
            func(*args, **kwargs)

    print('{}(): {} iter/s; {} seconds; {} iterations'.format(func_name(func), tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))


from cengal.hardware.memory.shared_memory import *
from cengal.hardware.memory.shared_memory_external_types.numpy_types import types_collection as numpy_types_collection
from cengal.time_management.cpu_clock import cpu_clock
from cengal.time_management.high_precision_sync_sleep import hps_sleep

import numpy as np
import unittest

from dataclasses import dataclass
from typing import Any, Dict, Optional, Callable, Set, Type, Tuple, List, FrozenSet, Deque


class SimpleClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __eq__(self, other):
        if isinstance(other, SimpleClass):
            return (self.a == other.a) and (self.b == other.b)
        
        return False


class SimpleClassWithSlots:
    __slots__ = ['a', 'b']

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
        self.x += 1


# Complex dataclass:

class Positions(IntEnum):
    manager = 0
    designer = 1
    accountant = 2
    lawyer = 3


class Employee:
    def __init__(self, name: str, age: int, position: Positions, years_of_employment: int = 0):
        self.name = name
        self.age = age
        self.position = position
        self.years_of_employment = years_of_employment
    
    def increase_years_of_employment(self):
        self.years_of_employment += 1
        self.age += 1
    
    def __repr__(self):
        return f'Employee(name={self.name}, age={self.age}, position={self.position}, years_of_employment={self.years_of_employment})'
    
    def __str__(self):
        return self.__repr__()


@dataclass
class CompanyInfo:
    company_id: int
    emails: Tuple[str, str]
    websites: List[str]
    income: float
    employees: int
    some_employee: Employee


@dataclass
class SomeSharedObject:
    some_processing_stage_control: bool
    str_value: str
    data_dict: Dict[Hashable, Any]
    company_info: CompanyInfo


# class TestCaseForRunInLoop(UnittestTestCaseWithState):
class TestCaseForRunInLoop(unittest.TestCase):
    repeats_num: int = 1

    # @classmethod
    # def setUpClass(cls):
    #     cls.state = UnittestTestCaseState()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.state.unregister()
    
    # @unittest.skip('temp skip')
    def test_set(self):
        pifrl()
        for _ in range(self.repeats_num):
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

            with creator:
                val: Set = {
                    'hello',
                    'world',
                }
                mapped_obj = creator.put_message(val)
                obj: Set = creator.get_message()
                obj |= set(range(20))
                obj.discard('hello')
                # print(f'{val.a=}, {obj.a=}')
                self.assertIsNot(val, mapped_obj)
                self.assertIsNot(val, obj)
                self.assertIsNot(mapped_obj, obj)

                self.assertIn('world', val)
                self.assertIn('world', obj)
                self.assertIn('world', mapped_obj)

                self.assertNotEqual(val, obj)
                self.assertEqual(mapped_obj, obj)
    
    # @unittest.skip('temp skip')
    def test_fast_set(self):
        pifrl()
        for _ in range(self.repeats_num):
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

            with creator:
                val: Set = FastLimitedSet({
                    'hello',
                    'world',
                })
                mapped_obj = creator.put_message(val)
                obj: Set = creator.get_message()
                obj |= set(range(20))
                obj.discard('hello')
                # print(f'{val.a=}, {obj.a=}')
                self.assertIsNot(val, mapped_obj)
                self.assertIsNot(val, obj)
                self.assertIsNot(mapped_obj, obj)

                self.assertIn('world', val)
                self.assertIn('world', obj)
                self.assertIn('world', mapped_obj)

                self.assertNotEqual(val, obj)
                self.assertNotEqual(mapped_obj, obj)
                self.assertEqual(mapped_obj, val)
    
    # @unittest.skip('temp skip')
    def test_dict(self):
        pifrl()
        for _ in range(self.repeats_num):
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

            with creator:
                val = {
                    'hello': 'world',
                    'world': 'hello',
                }
                mapped_obj = creator.put_message(val)
                obj: Dict = creator.get_message()
                obj.update({i: str(i) for i in range(20)})
                del obj['world']
                # print(f'{val.a=}, {obj.a=}')
                self.assertIsNot(val, mapped_obj)
                self.assertIsNot(val, obj)
                self.assertIsNot(mapped_obj, obj)

                self.assertIn('hello', val)
                self.assertIn('hello', obj)
                self.assertIn('hello', mapped_obj)

                self.assertIn('world', val)
                self.assertNotIn('world', obj)
                self.assertNotIn('world', mapped_obj)

                self.assertNotEqual(val, obj)
                self.assertEqual(mapped_obj, obj)
    
    # @unittest.skip('temp skip')
    def test_fast_dict(self):
        pifrl()
        for _ in range(self.repeats_num):
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

            with creator:
                val = FastLimitedDict({
                    'hello': 'world',
                    'world': 'hello',
                })
                mapped_obj = creator.put_message(val)
                obj: Dict = creator.get_message()
                obj.update({i: str(i) for i in range(20)})
                obj['hello'] = 20
                del obj['world']
                # print(f'{val.a=}, {obj.a=}')
                self.assertIsNot(val, mapped_obj)
                self.assertIsNot(val, obj)
                self.assertIsNot(mapped_obj, obj)

                self.assertIn('hello', val)
                self.assertIn('hello', obj)
                self.assertIn('hello', mapped_obj)

                self.assertIn('world', val)
                self.assertNotIn('world', obj)
                self.assertIn('world', mapped_obj)

                self.assertNotEqual(val, obj)
                self.assertNotEqual(mapped_obj, obj)
                self.assertEqual(mapped_obj, val)
    
    # @unittest.skip('temp skip')
    def test_np_ndarray(self):
        pifrl()
        for _ in range(self.repeats_num):
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024, external_types_collections=numpy_types_collection())

            with creator:
                shape = (10, 10, 3)
                dtype = np.float64
                val = np.zeros(shape, dtype=dtype)
                mapped_obj = creator.put_message(val)
                obj = creator.get_message()

                obj[0, 0, 0] = 100.0
                obj[1, 1, 1] = 200.0
                obj[2, 2, 2] = 300.0
                obj[3, 3, 0] = 400.0
                obj[4, 4, 1] = 500.0
                obj[5, 5, 2] = 600.0
                obj[6, 6, 0] = 700.0
                obj[7, 7, 1] = 800.0
                obj[8, 8, 2] = 900.0
                obj[9, 9, 0] = 1000.0

                self.assertIsNot(val, mapped_obj)
                self.assertIsNot(val, obj)
                
                np.testing.assert_array_equal(mapped_obj, obj)
                try:
                    np.testing.assert_array_equal(val, mapped_obj)
                    assert False
                except AssertionError:
                    pass  # This is expected as we want them to be not equal
    
    # @unittest.skip('temp skip')
    def test_simple_class_inplace_obj(self):
        pifrl()
        for _ in range(self.repeats_num):
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

            with creator:
                val = SimpleClass(1, 2)
                mapped_obj = creator.put_message(val)
                obj = creator.get_message()
                obj.a += 1
                # print(f'{val.a=}, {obj.a=}')
                self.assertIs(val, mapped_obj)
                self.assertIsNot(val, obj)

                self.assertEqual(val, obj)
                self.assertEqual(mapped_obj, obj)
    
    # @unittest.skip('broken')
    def test_simple_class_obj_default(self):
        pifrl()
        for _ in range(self.repeats_num):
            # TODO: Fix required
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

            with creator:
                val = SimpleClass(1, 2)
                mapped_obj = creator.put_message(val)
                obj = creator.get_message()
                obj.a += 1
                # print(f'{val.a=}, {obj.a=}')
                self.assertIs(val, mapped_obj)
                self.assertIsNot(val, obj)

                self.assertEqual(val, obj)
                self.assertEqual(mapped_obj, obj)
    
    # @unittest.skip('broken')
    def test_simple_class_obj_static(self):
        pifrl()
        for _ in range(self.repeats_num):
            # TODO: Fix required
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

            with creator:
                val = SimpleClass(1, 2)
                mapped_obj = creator.put_message(ForceStaticObjectCopy(val))
                obj = creator.get_message()
                obj.a += 1
                # print(f'{val.a=}, {obj.a=}')
                self.assertIsNot(val, mapped_obj)
                self.assertIsNot(val, obj)

                self.assertNotEqual(val, obj)
                self.assertEqual(mapped_obj, obj)
    
    # @unittest.skip('broken')
    def test_simple_class_obj_general(self):
        pifrl()
        for _ in range(self.repeats_num):
            # TODO: Fix required
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

            with creator:
                val = SimpleClass(1, 2)
                mapped_obj = creator.put_message(ForceGeneralObjectCopy(val))
                obj = creator.get_message()
                obj.a += 1
                # print(f'{val.a=}, {obj.a=}')
                self.assertIsNot(val, mapped_obj)
                self.assertIsNot(val, obj)

                self.assertNotEqual(val, obj)
                self.assertEqual(mapped_obj, obj)
    
    # @unittest.skip('broken')
    def test_decimal_obj(self):
        pifrl()
        from decimal import Decimal, DecimalTuple
        for _ in range(self.repeats_num):
            # TODO: Fix required
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

            with creator:
                val = [Decimal('3.14')]
                mapped_obj = creator.put_message(val)
                obj = creator.get_message()
                obj[0] += 1
                # print(f'{val.a=}, {obj.a=}')
                self.assertIsNot(val[0], mapped_obj[0])
                self.assertIsNot(val[0], obj[0])

                self.assertNotEqual(val[0], obj[0])
                self.assertEqual(mapped_obj[0], obj[0])
    
    # @unittest.skip('broken')
    def test_simple_class_with_slots_obj_default(self):
        pifrl()
        for _ in range(self.repeats_num):
            # TODO: Fix required
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

            with creator:
                val = SimpleClassWithSlots(1, 2)
                mapped_obj = creator.put_message(val)
                obj = creator.get_message()
                obj.a += 1
                # print(f'{val.a=}, {obj.a=}')
                self.assertIsNot(val, mapped_obj)
                self.assertIsNot(val, obj)

                self.assertNotEqual(val, obj)
                self.assertEqual(mapped_obj, obj)
    
    # @unittest.skip('broken')
    def test_datetime_obj(self):
        pifrl()
        from datetime import datetime
        for _ in range(self.repeats_num):
            # TODO: Fix required
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

            with creator:
                val: datetime = datetime.now()
                mapped_obj: datetime = creator.put_message(val)
                obj: datetime = creator.get_message()

                self.assertIsNot(val, mapped_obj)
                self.assertIsNot(val, obj)
                self.assertIsNot(mapped_obj, obj)

                self.assertEqual(mapped_obj, val)
                self.assertEqual(mapped_obj, obj)
    
    # @unittest.skip('broken')
    def test_datetime_timedelta_obj(self):
        pifrl()
        from datetime import datetime, timedelta
        for _ in range(self.repeats_num):
            # TODO: Fix required
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

            with creator:
                val: timedelta = datetime.now() - datetime.now()
                mapped_obj: timedelta = creator.put_message(val)
                obj: timedelta = creator.get_message()

                self.assertIsNot(val, mapped_obj)
                self.assertIsNot(val, obj)
                self.assertIsNot(mapped_obj, obj)

                self.assertEqual(mapped_obj, val)
                self.assertEqual(mapped_obj, obj)
    
    # @unittest.skip('temp skip')
    def test_dataclass_obj(self):
        pifrl()
        for _ in range(self.repeats_num):
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

            with creator:
                val = DataClass(1, 2)
                # print(f'{dir(val)=}')
                # pprint(val)
                # pprint(val.__dict__)
                mapped_val = creator.put_message(val)
                # print(f'{dir(mapped_val)=}')
                obj = creator.get_message()
                # print(f'{dir(obj)=}')
                obj = cast(DataClass, obj)
                obj.add_one()
                # pdi(val)
                # pdi(obj)
                # pdi(obj.__dict__)
                # print(f'{val.x=}, {obj.x=}')
                mapped_val.y = 'Yes'
                val.z = 40
                self.assertIsNot(val, obj)
                self.assertIs(val, mapped_val)
                self.assertIsNot(mapped_val, obj)

                self.assertNotEqual(val, obj)  # since internal __dict__ has no info about externally updated fields

                self.assertEqual(val.x, obj.x)
                self.assertEqual(val.y, obj.y)
                self.assertEqual(val.z, obj.z)
    
    # @unittest.skip('temp skip')
    def test_complex_dataclass_obj(self):
        pifrl()
        for _ in range(self.repeats_num):
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024, external_types_collections=numpy_types_collection())

            with creator:
                val: SomeSharedObject = SomeSharedObject(
                    some_processing_stage_control=False,
                    str_value='Hello, ',
                    data_dict={
                        'key1': 1,
                        ('key', 2): 'value2',
                        'key3': np.array([1, 2, 3], dtype=np.int32),
                    },
                    company_info=CompanyInfo(
                        company_id=1,
                        emails=('sails@company.com', 'support@company.com'),
                        websites=['http://company.com', 'http://company.org'],
                        income=1_000_000.0,
                        employees=10,
                        some_employee=Employee(
                            'John Doe', 
                            30, 
                            Positions.manager,
                            2,
                        )
                    )
                )

                # print(f'{dir(val)=}')
                # pprint(val)
                # pprint(val.__dict__)
                mapped_val = creator.put_message(val)
                # print(f'{dir(mapped_val)=}')
                obj = creator.get_message()

                obj = cast(SomeSharedObject, obj)
                obj.str_value += 'World!'
                obj.data_dict['key1'] *= 200
                obj.data_dict[('key', 2)] = obj.data_dict[('key', 2)] + ' data'
                obj.data_dict['key3'] += 10
                obj.company_info.income = 3_000_000.0
                obj.company_info.some_employee.increase_years_of_employment()
                obj.some_processing_stage_control = True

                self.assertIsNot(val, obj)
                self.assertIs(val, mapped_val)
                self.assertIsNot(mapped_val, obj)

                self.assertNotEqual(val, obj)  # since internal __dict__ has no info about externally updated fields

                self.assertEqual(val.str_value, obj.str_value)
                self.assertEqual(val.data_dict['key1'], obj.data_dict['key1'])
                self.assertEqual(val.data_dict[('key', 2)], obj.data_dict[('key', 2)])
                np.testing.assert_array_equal(val.data_dict['key3'], obj.data_dict['key3'])
                self.assertEqual(val.company_info.income, obj.company_info.income)
                self.assertEqual(val.company_info.some_employee.years_of_employment, obj.company_info.some_employee.years_of_employment)
                self.assertEqual(val.company_info.some_employee.age, obj.company_info.some_employee.age)
                self.assertEqual(val.some_processing_stage_control, obj.some_processing_stage_control)
    
    # @unittest.skip('temp skip')
    def test_mutable_set_rehash(self):
        pifrl()
        for _ in range(self.repeats_num):
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

            with creator:
                val = set(range(1, 11))
                val2 = set(range(10, 101))
                val.update(val2)
                obj = creator.put_message(val)
                for item in val2:
                    obj.add(item)
                
                self.assertEqual(val, obj)
    
    # @unittest.skip('temp skip')
    def test_mutable_mapping_rehash(self):
        pifrl()
        for _ in range(self.repeats_num):
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

            with creator:
                val = {i: i for i in range(1, 11)}
                val2 = {i: i for i in range(10, 101)}
                val.update(val2)
                obj = creator.put_message(val)
                obj.update(val2)
                
                self.assertEqual(val, obj)
    
    # @unittest.skip('temp skip')
    def test_shared_memory(self):
        pifrl()
        for _ in range(self.repeats_num):
            results: List[Any] = list()
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

            with creator:
                results.append(creator.read_mem(creator.get_data_start_offset(), 50))
                offset, size = creator.malloc(ObjectType.tbool, 1)
                results.append(size)
                results.append(creator.read_mem(creator.get_data_start_offset(), 50))
                offset, size = creator.realloc(offset, 11)
                results.append(size)
                results.append(creator.read_mem(creator.get_data_start_offset(), 50))
                results.append(creator.free(offset))
                results.append(creator.read_mem(creator.get_data_start_offset(), 50))
                creator.set_free_memory_search_start(0)
                creator.commit_free_memory_search_start()
                results.append(creator.read_mem(creator.get_data_start_offset(), 50))
                offset, size = creator.malloc(ObjectType.tbool, 1)
                results.append(size)
                results.append(creator.read_mem(creator.get_data_start_offset(), 50))
                offset, size = creator.realloc(offset, 11)
                results.append(size)
                results.append(creator.read_mem(creator.get_data_start_offset(), 50))
                results.append(creator.free(offset))
                results.append(creator.read_mem(creator.get_data_start_offset(), 50))
                creator.set_free_memory_search_start(0)
                creator.commit_free_memory_search_start()

                values = [
                    0,
                    1,
                    999999999999,
                    -1,
                    -999999999999,
                    0.0,
                    1.0,
                    999999999999.0,
                    -1.0,
                    -999999999999.0,
                    (1,),
                    [1],
                    (1, 2),
                    [1, 2],
                    {1, 2},
                    (1, [2, 3]),
                    {1: 1, 2: 2},
                    {1: 1, 2: [2, (3,)]},
                    'test',
                    'test'.encode('utf-8'),
                    bytearray('test'.encode('utf-8')),
                    True,
                    False,
                    {
                        'test': 1,
                        'test2': 2.0,
                        'test3': 'test',
                        'test4': [
                            1, 
                            2.0, 
                            True, 
                            False, 
                            'test', 
                            'test'.encode('utf-8'), 
                            bytearray('test'.encode('utf-8')), 
                            ('hello', 1),
                            ['world', 2.0],
                            {
                                'hello': [1, (2, 3)],
                                'world': 'world',
                            }
                        ],
                    }
                ]
                
                results.append(creator.read_mem(creator.get_free_memory_search_start(), 100))
                results.append(creator.read_mem(creator.get_data_start_offset(), 500))
                
                for val in values:
                    creator.put_message(val)
                    results.append(creator.read_mem(creator.get_free_memory_search_start(), 100))
                    results.append(creator.read_mem(creator.get_data_start_offset(), 500))
                    
                    message = creator.take_message()
                    self.assertEqual(val, message)
                    results.append(message)
                    results.append(creator.read_mem(creator.get_free_memory_search_start(), 100))
                    results.append(creator.read_mem(creator.get_data_start_offset(), 500))


if __name__ == '__main__':
    unittest.main()
