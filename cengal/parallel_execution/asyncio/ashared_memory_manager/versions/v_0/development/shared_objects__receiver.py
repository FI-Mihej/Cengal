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
from cengal.code_inspection.line_tracer import cln
from cengal.time_management.cpu_clock import perf_counter

import asyncio
import numpy as np

from shared_objects__types import *


ashared_memory_manager: ASharedMemoryManager = ASharedMemoryManager(SharedMemory('shared_objects'))


def print_sso_info(sso: SomeSharedObject):
    print('sso info:')
    print(f'hashmap_offset {sso._tgeneralobject_imutablemapping_attributes._offset}: {sso._tgeneralobject_imutablemapping_attributes.hashmap_offset}')
    print(f'hashmap {sso._tgeneralobject_imutablemapping_attributes._offset}: {sso._tgeneralobject_imutablemapping_attributes.hashmap}')
    for key, bucket in sso._tgeneralobject_imutablemapping_attributes.buckets.items():
        print(f'\t> {key=}: {bucket=}')
    
    print()


async def receiver():
    # alt.rich_allowed = False
    async with ashared_memory_manager as asmm:
        print('Receiver is ready.')

        # An each coroutine should get its own context manager (ASharedMemoryContextManager). Either `asmm` or `ashared_memory_manager` can be used
        ashared_memory_context_manager: ASharedMemoryContextManager = asmm()

        async with ashared_memory_context_manager.if_has_messages() as shared_memory:
            mapped_flag_holder: List[bool] = shared_memory.value.take_message()

        async with ashared_memory_context_manager.if_has_messages() as shared_memory:
            with MeasureTimeTraceLine('Taking the message with the pickled shared object from the sender', iterations=1000, do_print=True) as mt:
                for _ in range(mt.iterations):
                   pickled_sso: bytes = shared_memory.value.take_message()
            
            if mt.do_print:
                print(f'Throughput: {(len(pickled_sso) * mt.iterations) / mt.time_spent:.2f} bytes per second')
                print()
            
            mapped_flag_holder[0] = True
            start_time = perf_counter()

        async with ashared_memory_context_manager.if_has_messages() as shared_memory:
            with MeasureTimeTraceLine('Receiving 400_000 bytes binary', iterations=50) as mt:
                for _ in range(mt.iterations):
                    some_binary: bytes = shared_memory.value.take_message()
                
                transfer_time = perf_counter() - start_time
            
            print(f'Throughput: {(len(some_binary) * mt.iterations) / mt.time_spent:.2f} bytes per second')
            print(f'Transfer throughput: {(len(some_binary) * mt.iterations) / transfer_time:.2f} bytes per second')
            print()
            
            mapped_flag_holder[0] = True

        async with ashared_memory_context_manager.if_has_messages() as shared_memory:
            with MeasureTimeTraceLine('Taking 100 messages with SomeSharedObject instances from the sender', iterations=100) as mt:
                for _ in range(mt.iterations):
                    sso: SomeSharedObject = shared_memory.value.take_message()
            
            mapped_flag_holder[0] = True

        async with ashared_memory_context_manager.if_has_messages() as shared_memory:
            with MeasureTimeTraceLine('Taking the message with the shared object from the sender'):
                sso: SomeSharedObject = shared_memory.value.take_message()

        async with ashared_memory_context_manager as shared_memory:
            with MeasureTimeTraceLine('Changing the shared object\'s content', do_print=True):
                sso.str_value += 'World!'
                data_dict = sso.data_dict
                data_dict['key1'] *= 200
                data_dict[('key', 2)] = data_dict[('key', 2)] + ' data'
                data_dict['key3'] += 10
                sso.company_info.income = 3_000_000.0
                sso.company_info.some_employee.increase_years_of_employment()
                sso.some_processing_stage_control = True

            iter_num = 1000
            
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    company_metrics = sso.company_info.company_metrics
            
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    k = company_metrics[CompanyMetrics.in_a_good_state]
            
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    company_metrics[CompanyMetrics.in_a_good_state] = False
            
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    company_metrics[CompanyMetrics.in_a_good_state] = None
            
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    k = company_metrics[CompanyMetrics.employees]
            
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    company_metrics[CompanyMetrics.employees] = 20
            
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    company_metrics[CompanyMetrics.employees] += 1
            
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    k = company_metrics[CompanyMetrics.avg_salary]
            
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    company_metrics[CompanyMetrics.avg_salary] = 5_000.0
            
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    company_metrics[CompanyMetrics.avg_salary] += 1.1

            with MeasureTimeTraceLine(iterations=iter_num, do_print=True) as mt:
                for _ in range(mt.iterations):
                    k = sso.int_value

            with MeasureTimeTraceLine(do_print=False) as mt:
                sso.int_value = 100
            
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    k = sso.int_value

            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    sso.int_value = 200
            
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    sso.int_value += 1
            
            with MeasureTimeTraceLine(f'New field: "{str(CompanyMetrics.annual_income)}"', iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    company_metrics[CompanyMetrics.annual_income] = 2_000_000.0

            with MeasureTimeTraceLine(f'New field: "{str(CompanyMetrics.emails)}"', iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    company_metrics[CompanyMetrics.emails] = tuple()
            
            with MeasureTimeTraceLine(f'New field: "{str(CompanyMetrics.emails)}"', iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    company_metrics[CompanyMetrics.emails] = ('sails@company.com',)
            
            with MeasureTimeTraceLine(f'New field: "{str(CompanyMetrics.emails)}"', iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    company_metrics[CompanyMetrics.emails] = ('sails@company.com', 'support@company.com')
            
            with MeasureTimeTraceLine(f'New field: "{str(CompanyMetrics.websites)}"', iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    k = company_metrics[CompanyMetrics.websites]
            
            with MeasureTimeTraceLine(f'New field: "{str(CompanyMetrics.websites)}"', iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    company_metrics[CompanyMetrics.websites] = ['http://company.com', 'http://company.org']

            with MeasureTimeTraceLine(iterations=iter_num, do_print=True) as mt:
                for _ in range(mt.iterations):
                    k = sso.str_value

            with MeasureTimeTraceLine(do_print=False) as mt:
                sso.str_value = 'Hello. '
            
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    k = sso.str_value

            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    sso.str_value = 'Hello. '
            
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    sso.str_value += '!'

            with MeasureTimeTraceLine() as mt:
                data_dict = sso.data_dict
            
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    k = data_dict['key1']
                
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    data_dict['key1'] = 200
                
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    data_dict['key1'] *= 1
                
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    data_dict['key1'] += 3
                
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    k = data_dict[('key', 2)]
                
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    data_dict[('key', 2)] = 'value2'
                
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    data_dict[('key', 2)] = data_dict[('key', 2)] + 'd'
            
            with MeasureTimeTraceLine():
                data_dict[('key', 2)] = 'value2'
            
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    data_dict[('key', 2)] += 'd'
                
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    ndarray: np.ndarray = data_dict['key3']
                
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    ndarray += 10
                
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    data_dict['key3'] += 10
                
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    k = sso.company_info.income
                
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    sso.company_info.income = 3_000_000.0
                
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    sso.company_info.income *= 1.1
                
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    sso.company_info.income += 500_000.0
                
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    some_employee = sso.company_info.some_employee
                
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    some_employee.increase_years_of_employment()
                
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    sso.company_info.some_employee.increase_years_of_employment()
                
            with MeasureTimeTraceLine(iterations=iter_num) as mt:
                for _ in range(mt.iterations):
                    sso.some_processing_stage_control = True


if __name__ == '__main__':
    print('Receiver is starting its work.')
    asyncio.run(receiver())
    print('Receiver has finished its work.')
