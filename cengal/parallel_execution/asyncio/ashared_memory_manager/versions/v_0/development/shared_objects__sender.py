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


__all__ = [
]


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


from cengal.hardware.memory.shared_memory import *
from cengal.parallel_execution.asyncio.ashared_memory_manager import *
from cengal.performance_test_lib import MeasureTimeTraceLine

import numpy as np

import asyncio
import pickle

from shared_objects__types import *


ashared_memory_manager: ASharedMemoryManager = ASharedMemoryManager(SharedMemory('shared_objects', True, 200 * 1024**2))


def printval(name, value):
    print(f'> {name}:\n\t{value}\n')


def printtitle(name):
    title_str: str = f'<<< {name}: >>>'
    header_str: str = '=' * len(title_str)
    print(header_str)
    print(title_str)
    print(header_str)
    print()

async def sender():
    sso: SomeSharedObject = SomeSharedObject(
        some_processing_stage_control=False,
        int_value=18,
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
            ),
            company_metrics=intenum_dict_to_list({
                CompanyMetrics.websites: ['http://company.com', 'http://company.org'],
                CompanyMetrics.avg_salary: 3_000.0,
                CompanyMetrics.employees: 10,
                CompanyMetrics.in_a_good_state: True,
            })
        )
    )

    with MeasureTimeTraceLine('Pickle the shared object', iterations=500) as mt:
        for _ in range(mt.iterations):
            another_sso: SomeSharedObject = SomeSharedObject(
                some_processing_stage_control=False,
                int_value=18,
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
                    ),
                    company_metrics=intenum_dict_to_list({
                        CompanyMetrics.websites: ['http://company.com', 'http://company.org'],
                        CompanyMetrics.avg_salary: 3_000.0,
                        CompanyMetrics.employees: 10,
                        CompanyMetrics.in_a_good_state: True,
                    })
                )
            )
            pickled_sso = pickle.dumps(another_sso)

    with MeasureTimeTraceLine('Unpickle the shared object', iterations=500) as mt:
        for _ in range(mt.iterations):
            unpickled_sso: SomeSharedObject = pickle.loads(pickled_sso)

    with MeasureTimeTraceLine('Processing emulation of pickle the shared object (pickle and unpickle)', iterations=500) as mt:
        for _ in range(mt.iterations):
            another_sso: SomeSharedObject = SomeSharedObject(
                some_processing_stage_control=False,
                int_value=18,
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
                    ),
                    company_metrics=intenum_dict_to_list({
                        CompanyMetrics.websites: ['http://company.com', 'http://company.org'],
                        CompanyMetrics.avg_salary: 3_000.0,
                        CompanyMetrics.employees: 10,
                        CompanyMetrics.in_a_good_state: True,
                    })
                )
            )
            pickled_sso = pickle.dumps(another_sso)
            unpickled_sso: SomeSharedObject = pickle.loads(pickled_sso)

    async with ashared_memory_manager as asmm:
        print('Sender is ready.')

        # An each coroutine should get its own context manager (ASharedMemoryContextManager). Either `asmm` or `ashared_memory_manager` can be used
        ashared_memory_context_manager: ASharedMemoryContextManager = asmm()

        async with ashared_memory_context_manager as shared_memory:
            mapped_flag_holder = shared_memory.value.put_message([False])

        async with ashared_memory_context_manager as shared_memory:
            with MeasureTimeTraceLine('Sent pickled shared object to the receiver', iterations=1000) as mt:
                for _ in range(mt.iterations):
                    shared_memory.value.put_message(pickled_sso)
            
            print(f'Throughput: {(len(pickled_sso) * mt.iterations) / mt.time_spent:.2f} bytes per second')
            print()
        
        some_data: bytes = bytes(400_000)
        while True:
            async with ashared_memory_context_manager as shared_memory:
                if mapped_flag_holder[0]:
                    mapped_flag_holder[0] = False
                    break

                # shared_memory.existence = False

        # some_data: bytes = bytes(400_000)
        # async with ashared_memory_context_manager as shared_memory:
        #     with MeasureTimeTraceLine('Sending 400_000 bytes binary', iterations=50) as mt:
        #         for _ in range(mt.iterations):
        #             shared_memory.value.put_message(some_data)
            
        #     print(f'Throughput: {(len(some_data) * mt.iterations) / mt.time_spent:.2f} bytes per second')
        #     print()

        async with ashared_memory_context_manager as shared_memory:
            for _ in range(50):
                shared_memory.value.put_message(some_data)
        
        while True:
            async with ashared_memory_context_manager as shared_memory:
                if mapped_flag_holder[0]:
                    mapped_flag_holder[0] = False
                    break

                shared_memory.existence = False

        async with ashared_memory_context_manager as shared_memory:
            with MeasureTimeTraceLine('Preparing 100 instancess of SomeSharedObject and sending them to the receiver', iterations=100) as mt:
                for _ in range(mt.iterations):
                    another_sso: SomeSharedObject = SomeSharedObject(
                        some_processing_stage_control=False,
                        int_value=18,
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
                            ),
                            company_metrics=intenum_dict_to_list({
                                CompanyMetrics.websites: ['http://company.com', 'http://company.org'],
                                CompanyMetrics.avg_salary: 3_000.0,
                                CompanyMetrics.employees: 10,
                                CompanyMetrics.in_a_good_state: True,
                            })
                        )
                    )
                    another_sso_mapped: SomeSharedObject = shared_memory.value.put_message(another_sso)
        
        while True:
            async with ashared_memory_context_manager as shared_memory:
                if mapped_flag_holder[0]:
                    mapped_flag_holder[0] = False
                    break

                shared_memory.existence = False

        async with ashared_memory_context_manager as shared_memory:
            with MeasureTimeTraceLine('Preparing the shared object and sending it to the receiver') as mt:
                sso_mapped: SomeSharedObject = shared_memory.value.put_message(sso)
        
        processing_done = False
        while not processing_done:
            async with ashared_memory_context_manager as shared_memory:
                processing_done = sso.some_processing_stage_control
                shared_memory.existence = False
        
        # The receiver has finished processing. The shared object has been changed. Let's see what has been changed
        printtitle('Fields expeced to be changed by the receiver')
        printval('sso.some_processing_stage_control', sso.some_processing_stage_control)
        printval('sso.int_value', sso.int_value)
        printval('sso.str_value', sso.str_value)
        printval('sso.data_dict', sso.data_dict)
        printval('sso.company_info.income', sso.company_info.income)
        printval('sso.company_info.some_employee.years_of_employment', sso.company_info.some_employee.years_of_employment)
        printval('sso.company_info.some_employee.age', sso.company_info.some_employee.age)
        printval('sso.company_info.company_metrics[CompanyMetrics.annual_income]', sso.company_info.company_metrics[CompanyMetrics.annual_income])
        printval('sso.company_info.company_metrics[CompanyMetrics.emails]', sso.company_info.company_metrics[CompanyMetrics.emails])
        printval('sso.company_info.company_metrics[CompanyMetrics.websites]', sso.company_info.company_metrics[CompanyMetrics.websites])
        printval('sso.company_info.company_metrics[CompanyMetrics.avg_salary]', sso.company_info.company_metrics[CompanyMetrics.avg_salary])
        printval('sso.company_info.company_metrics[CompanyMetrics.employees]', sso.company_info.company_metrics[CompanyMetrics.employees])
        printval('sso.company_info.company_metrics[CompanyMetrics.in_a_good_state]', sso.company_info.company_metrics[CompanyMetrics.in_a_good_state])

        printtitle('Resulting content')
        printval('sso', sso)
        printval('sso.company_info', sso.company_info)
        printval('sso.company_info.some_employee', sso.company_info.some_employee)

if __name__ == '__main__':
    ensure_adjusted_pythonhashseed(pythonhashseed=0)  # Ensure that the hash seed is adjusted for this process group
    # ensure_adjusted_scientific()  # Ensure (for this process group) that: 1) the hash seed is adjusted; 2) interpreter optimizations ('-OO') are turned on; 3) the integer string conversion length limitation is turned off
    print('Sender is starting its work.')
    asyncio.run(sender())
    print('Sender has finished its work.')
