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

import difflib

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
from cengal.time_management.cpu_clock import cpu_clock
from cengal.time_management.high_precision_sync_sleep import hps_sleep

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


_MAX_LENGTH = 80

DIFF_OMITTED = ('\nDiff is %s characters long. '
                 'Set self.maxDiff to None to see it.')


def safe_repr(obj, short=False):
    try:
        result = repr(obj)
    except Exception:
        result = object.__repr__(obj)
    if not short or len(result) < _MAX_LENGTH:
        return result
    return result[:_MAX_LENGTH] + ' [truncated]...'


class FakeTestCase:

    failureException = AssertionError

    longMessage = True

    _diffThreshold = 2**16

    maxDiff = 80*8

    def __init__(self):
        self._outcome = None
        self._testMethodDoc = 'No test'
        self._cleanups = []
        self._subtest = None

        # Map types to custom assertEqual functions that will compare
        # instances of said type in more detail to generate a more useful
        # error message.
        self._type_equality_funcs = {}
        self.addTypeEqualityFunc(dict, 'assertDictEqual')
        self.addTypeEqualityFunc(list, 'assertListEqual')
        self.addTypeEqualityFunc(tuple, 'assertTupleEqual')
        self.addTypeEqualityFunc(set, 'assertSetEqual')
        self.addTypeEqualityFunc(frozenset, 'assertSetEqual')
        self.addTypeEqualityFunc(str, 'assertMultiLineEqual')

    def _truncateMessage(self, message, diff):
        max_diff = self.maxDiff
        if max_diff is None or len(diff) <= max_diff:
            return message + diff
        return message + (DIFF_OMITTED % len(diff))

    def _baseAssertEqual(self, first, second, msg=None):
        """The default assertEqual implementation, not type specific."""
        if not first == second:
            standardMsg = str()
            msg = self._formatMessage(msg, standardMsg)
            raise self.failureException(msg)

    def assertMultiLineEqual(self, first, second, msg=None):
        """Assert that two multi-line strings are equal."""
        self.assertIsInstance(first, str, 'First argument is not a string')
        self.assertIsInstance(second, str, 'Second argument is not a string')

        if first != second:
            # don't use difflib if the strings are too long
            if (len(first) > self._diffThreshold or
                len(second) > self._diffThreshold):
                self._baseAssertEqual(first, second, msg)
            firstlines = first.splitlines(keepends=True)
            secondlines = second.splitlines(keepends=True)
            if len(firstlines) == 1 and first.strip('\r\n') == first:
                firstlines = [first + '\n']
                secondlines = [second + '\n']
            standardMsg = str()
            diff = '\n' + ''.join(difflib.ndiff(firstlines, secondlines))
            standardMsg = self._truncateMessage(standardMsg, diff)
            self.fail(self._formatMessage(msg, standardMsg))

    def assertSetEqual(self, set1, set2, msg=None):
        """A set-specific equality assertion.

        Args:
            set1: The first set to compare.
            set2: The second set to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        assertSetEqual uses ducktyping to support different types of sets, and
        is optimized for sets specifically (parameters must support a
        difference method).
        """
        try:
            difference1 = set1.difference(set2)
        except TypeError as e:
            self.fail('invalid type when attempting set difference: %s' % e)
        except AttributeError as e:
            self.fail('first argument does not support set difference: %s' % e)

        try:
            difference2 = set2.difference(set1)
        except TypeError as e:
            self.fail('invalid type when attempting set difference: %s' % e)
        except AttributeError as e:
            self.fail('second argument does not support set difference: %s' % e)

        if not (difference1 or difference2):
            return

        lines = []
        if difference1:
            lines.append('Items in the first set but not the second:')
            for item in difference1:
                lines.append(repr(item))
        if difference2:
            lines.append('Items in the second set but not the first:')
            for item in difference2:
                lines.append(repr(item))

        standardMsg = '\n'.join(lines)
        self.fail(self._formatMessage(msg, standardMsg))

    def assertTupleEqual(self, tuple1, tuple2, msg=None):
        """A tuple-specific equality assertion.

        Args:
            tuple1: The first tuple to compare.
            tuple2: The second tuple to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.
        """
        self.assertSequenceEqual(tuple1, tuple2, msg, seq_type=tuple)

    def assertSequenceEqual(self, seq1, seq2, msg=None, seq_type=None):
        """An equality assertion for ordered sequences (like lists and tuples).

        For the purposes of this function, a valid ordered sequence type is one
        which can be indexed, has a length, and has an equality operator.

        Args:
            seq1: The first sequence to compare.
            seq2: The second sequence to compare.
            seq_type: The expected datatype of the sequences, or None if no
                    datatype should be enforced.
            msg: Optional message to use on failure instead of a list of
                    differences.
        """
        if seq_type is not None:
            seq_type_name = seq_type.__name__
            if not isinstance(seq1, seq_type):
                raise self.failureException('First sequence is not a %s: %s'
                                        % (seq_type_name, safe_repr(seq1)))
            if not isinstance(seq2, seq_type):
                raise self.failureException('Second sequence is not a %s: %s'
                                        % (seq_type_name, safe_repr(seq2)))
        else:
            seq_type_name = "sequence"

        differing = None
        try:
            len1 = len(seq1)
        except (TypeError, NotImplementedError):
            differing = 'First %s has no length.    Non-sequence?' % (
                    seq_type_name)

        if differing is None:
            try:
                len2 = len(seq2)
            except (TypeError, NotImplementedError):
                differing = 'Second %s has no length.    Non-sequence?' % (
                        seq_type_name)

        if differing is None:
            if seq1 == seq2:
                return

            differing = str()

            for i in range(min(len1, len2)):
                try:
                    item1 = seq1[i]
                except (TypeError, IndexError, NotImplementedError):
                    differing += ('\nUnable to index element %d of first %s\n' %
                                 (i, seq_type_name))
                    break

                try:
                    item2 = seq2[i]
                except (TypeError, IndexError, NotImplementedError):
                    differing += ('\nUnable to index element %d of second %s\n' %
                                 (i, seq_type_name))
                    break

                if item1 != item2:
                    differing += str()
                    break
            else:
                if (len1 == len2 and seq_type is None and
                    type(seq1) != type(seq2)):
                    # The sequences are the same, but have differing types.
                    return

            if len1 > len2:
                differing += ('\nFirst %s contains %d additional '
                             'elements.\n' % (seq_type_name, len1 - len2))
                try:
                    differing += ('First extra element %d:\n%s\n' %
                                  (len2, safe_repr(seq1[len2])))
                except (TypeError, IndexError, NotImplementedError):
                    differing += ('Unable to index element %d '
                                  'of first %s\n' % (len2, seq_type_name))
            elif len1 < len2:
                differing += ('\nSecond %s contains %d additional '
                             'elements.\n' % (seq_type_name, len2 - len1))
                try:
                    differing += ('First extra element %d:\n%s\n' %
                                  (len1, safe_repr(seq2[len1])))
                except (TypeError, IndexError, NotImplementedError):
                    differing += ('Unable to index element %d '
                                  'of second %s\n' % (len1, seq_type_name))
        standardMsg = differing
        diffMsg = '\n' + '\n'.join(
            difflib.ndiff(pprint.pformat(seq1).splitlines(),
                          pprint.pformat(seq2).splitlines()))

        standardMsg = self._truncateMessage(standardMsg, diffMsg)
        msg = self._formatMessage(msg, standardMsg)
        self.fail(msg)

    def assertListEqual(self, list1, list2, msg=None):
        """A list-specific equality assertion.

        Args:
            list1: The first list to compare.
            list2: The second list to compare.
            msg: Optional message to use on failure instead of a list of
                    differences.

        """
        self.assertSequenceEqual(list1, list2, msg, seq_type=list)

    def addTypeEqualityFunc(self, typeobj, function):
        """Add a type specific assertEqual style function to compare a type.

        This method is for use by TestCase subclasses that need to register
        their own type equality functions to provide nicer error messages.

        Args:
            typeobj: The data type to call this function on when both values
                    are of the same type in assertEqual().
            function: The callable taking two arguments and an optional
                    msg= argument that raises self.failureException with a
                    useful error message when the two arguments are not equal.
        """
        self._type_equality_funcs[typeobj] = function

    def assertIsInstance(self, obj, cls, msg=None):
        """Same as self.assertTrue(isinstance(obj, cls)), with a nicer
        default message."""
        if not isinstance(obj, cls):
            standardMsg = '%s is not an instance of %r' % (safe_repr(obj), cls)
            self.fail(self._formatMessage(msg, standardMsg))

    def assertDictEqual(self, d1, d2, msg=None):
        self.assertIsInstance(d1, dict, 'First argument is not a dictionary')
        self.assertIsInstance(d2, dict, 'Second argument is not a dictionary')

        if d1 != d2:
            self.fail(self._formatMessage(str(), str()))

    def fail(self, msg=None):
        """Fail immediately, with the given message."""
        raise self.failureException(msg)

    def _formatMessage(self, msg, standardMsg):
        """Honour the longMessage attribute when generating failure messages.
        If longMessage is False this means:
        * Use only an explicit message if it is provided
        * Otherwise use the standard message for the assert

        If longMessage is True:
        * Use the standard message
        * If an explicit message is provided, plus ' : ' and the explicit message
        """
        if not self.longMessage:
            return msg or standardMsg
        if msg is None:
            return standardMsg
        try:
            # don't switch to '{}' formatting in Python 2.X
            # it changes the way unicode input is handled
            return '%s : %s' % (standardMsg, msg)
        except UnicodeDecodeError:
            return  '%s : %s' % (safe_repr(standardMsg), safe_repr(msg))

    def assertIsNot(self, expr1, expr2, msg=None):
        """Just like self.assertTrue(a is not b), but with a nicer default message."""
        if expr1 is expr2:
            standardMsg = 'unexpectedly identical: %s' % (safe_repr(expr1),)
            self.fail(self._formatMessage(msg, standardMsg))

    def assertIs(self, expr1, expr2, msg=None):
        """Just like self.assertTrue(a is b), but with a nicer default message."""
        if expr1 is not expr2:
            standardMsg = '%s is not %s' % (safe_repr(expr1),
                                             safe_repr(expr2))
            self.fail(self._formatMessage(msg, standardMsg))

    def assertNotEqual(self, first, second, msg=None):
        """Fail if the two objects are equal as determined by the '!='
           operator.
        """
        if not first != second:
            msg = self._formatMessage(msg, '%s == %s' % (safe_repr(first),
                                                          safe_repr(second)))
            raise self.failureException(msg)

    def _getAssertEqualityFunc(self, first, second):
        """Get a detailed comparison function for the types of the two args.

        Returns: A callable accepting (first, second, msg=None) that will
        raise a failure exception if first != second with a useful human
        readable error message for those types.
        """
        #
        # NOTE(gregory.p.smith): I considered isinstance(first, type(second))
        # and vice versa.  I opted for the conservative approach in case
        # subclasses are not intended to be compared in detail to their super
        # class instances using a type equality func.  This means testing
        # subtypes won't automagically use the detailed comparison.  Callers
        # should use their type specific assertSpamEqual method to compare
        # subclasses if the detailed comparison is desired and appropriate.
        # See the discussion in http://bugs.python.org/issue2578.
        #
        if type(first) is type(second):
            asserter = self._type_equality_funcs.get(type(first))
            if asserter is not None:
                if isinstance(asserter, str):
                    asserter = getattr(self, asserter)
                return asserter

        return self._baseAssertEqual

    def assertEqual(self, first, second, msg=None):
        """Fail if the two objects are unequal as determined by the '=='
           operator.
        """
        assertion_func = self._getAssertEqualityFunc(first, second)
        assertion_func(first, second, msg=msg)

# class TestCaseForRunInLoop(UnittestTestCaseWithState):
class TestCaseForRunInLoop(FakeTestCase):
    repeats_num: int = 1

    # @classmethod
    # def setUpClass(cls):
    #     cls.state = UnittestTestCaseState()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.state.unregister()
    
    # @unittest.skip('temp skip')
    def test_dict(self):
        pifrl()
        for _ in range(self.repeats_num):
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

            with creator:
                val = {
                    'hello': 'world',
                }
                mapped_obj = creator.put_message(val)
                obj: Dict = creator.get_message()
                obj.update({i: str(i) for i in range(20)})
                # print(f'{val.a=}, {obj.a=}')
                self.assertIsNot(val, mapped_obj)
                self.assertIsNot(val, obj)
                self.assertIsNot(mapped_obj, obj)

                self.assertNotEqual(val, obj)
                self.assertEqual(mapped_obj, obj)
    
    def test_np_ndarray(self):
        pifrl()
        for _ in range(self.repeats_num):
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

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
    
    def test_simple_class_obj(self):
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
    
    def test_complex_dataclass_obj(self):
        pifrl()
        for _ in range(self.repeats_num):
            creator: SharedMemory = SharedMemory('test_shmem', True, 200 * 1024 * 1024)

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
                self.assertEqual(val.some_processing_stage_control, obj.some_processing_stage_control)
    
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
                self.assertIsNot(val, mapped_obj)
                self.assertIsNot(val, obj)

                self.assertNotEqual(val, obj)
                self.assertEqual(mapped_obj, obj)

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

                self.assertNotEqual(val, obj)
                print(f'{mapped_obj=}, {obj=}')
                self.assertNotEqual(mapped_obj, obj)
    
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

                self.assertNotEqual(val, obj)
                self.assertNotEqual(mapped_obj, obj)
                self.assertEqual(mapped_obj, val)


if __name__ == '__main__':
    test: TestCaseForRunInLoop = TestCaseForRunInLoop()
    test.test_set()
