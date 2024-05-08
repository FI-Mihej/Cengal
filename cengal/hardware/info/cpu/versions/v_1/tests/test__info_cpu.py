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


from cengal.introspection.inspect import entity_properties, is_descriptor
from unittest import TestCase, main, skip
from typing import List


methods_to_run: List[str] = [
    'python_version', 
    'cpuinfo_version', 
    'cpuinfo_version_string', 
    'python_hz_advertised_friendlyversion', 
    'hz_actual_friendly', 
    'hz_advertised', 
    'hz_actual', 
    'arch', 
    'count', 
    'l1_data_cache_size', 
    'l1_instruction_cache_size', 
    'l2_cache_size', 
    'l2_cache_line_size', 
    'l2_cache_associativity', 
    'l3_cache_size', 
    'stepping', 
    'model', 
    'family', 
    'processor_type', 
    'vendor_id_raw', 
    'hardware_raw', 
    'brand_raw', 
    'arch_string_raw', 
    'cores_num', 
    'virtual_cores_num', 
    'l2_cache_size_per_core', 
    'l2_cache_size_per_virtual_core', 
    'l3_cache_size_per_core', 
    'l3_cache_size_per_virtual_core', 
    'is_x86', 
    'is_arm', 
    'flags', 
]


class TestCpuInfo(TestCase):
    def test__run_methods(self):
        from cengal.hardware.info.cpu import cpu_info
        ci = cpu_info()
        for method in methods_to_run:
            print(f'{method}:', getattr(ci, method))
        
        ci.gather_all()
    
    def test__run_methods_2(self):
        from cengal.hardware.info.cpu import cpu_info, CpuInfo
        ci = cpu_info()
        for property in entity_properties(CpuInfo):
            if property.startswith('_'):
                continue

            if is_descriptor(getattr(CpuInfo, property)):
                print(f'{property}:', getattr(ci, property))
        
        ci.gather_all()


if '__main__' == __name__:
    main()
