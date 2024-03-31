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
__version__ = "4.3.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal_cpu_info import cpu_info, CpuInfo


ci: CpuInfo = cpu_info()

print(f'{ci.is_arm=}')
print(f'{ci.is_x86=}')
print(f'{ci.arch=}')
print(f'{ci.arch_string_raw=}')
print(f'{ci.bits=}')
print(f'{ci.brand_raw=}')
print(f'{ci.cores_num=}')
print(f'{ci.count=}')
print(f'{ci.cpuinfo_version=}')
print(f'{ci.cpuinfo_version_string=}')
print(f'{ci.family=}')
print(f'{ci.flags=}')
print(f'{ci.hardware_raw=}')
print(f'{ci.hz_actual=}')
print(f'{ci.hz_actual_friendly=}')
print(f'{ci.hz_advertised=}')
print(f'{ci.l1_data_cache_size=}')
print(f'{ci.l1_instruction_cache_size=}')
print(f'{ci.l2_cache_associativity=}')
print(f'{ci.l2_cache_line_size=}')
print(f'{ci.l2_cache_size=}')
print(f'{ci.l2_cache_size_per_core=}')
print(f'{ci.l2_cache_size_per_virtual_core=}')
print(f'{ci.l3_cache_size=}')
print(f'{ci.l3_cache_size_per_core=}')
print(f'{ci.l3_cache_size_per_virtual_core=}')
print(f'{ci.model=}')
print(f'{ci.processor_type=}')
print(f'{ci.python_hz_advertised_friendlyversion=}')
print(f'{ci.python_version=}')
print(f'{ci.stepping=}')
print(f'{ci.vendor_id_raw=}')
print(f'{ci.virtual_cores_num=}')
