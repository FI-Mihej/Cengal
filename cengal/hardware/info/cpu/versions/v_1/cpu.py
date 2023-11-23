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


__all__ = ['CpuInfo', 'cpu_info']


# from operator import is_
from typing import Dict
from cengal.modules_management.alternative_import import alt_import
with alt_import('cpuinfo') as cpuinfo:
    if cpuinfo is None:
        CPUINFO_PRESENT: bool = False
    else:
        CPUINFO_PRESENT = True

from cengal.modules_management.ignore_in_build_mode import ignore_in_build_mode
PSUTIL_PRESENT: bool = False
with ignore_in_build_mode():
    with alt_import('psutil') as psutil:
        if psutil is not None:
            PSUTIL_PRESENT = True


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


class CpuInfo:
    _cache: Dict = None

    def __init__(self):
        if self._cache is None:
            self._cache_friendly: Dict = cpuinfo.get_cpu_info() if CPUINFO_PRESENT else dict()
            self._cache = self._normalize_cpu_info_values(self._cache_friendly)
    
    def _normalize_cpu_info_values(self, cpu_info_dict: Dict) -> Dict:
        result = dict()
        frequency: Dict[str, int] = {
                'ghz': 10 ** 9, 'mhz': 10 ** 6, 'khz': 10 ** 3, 'hz': 1
            }
        memory_size: Dict[str, int] = {
                'tib': 10 ** 12, 'gib': 10 ** 9, 'mib': 10 ** 6, 'kib': 10 ** 3, 'b': 1,
                'tb': 10 ** 12, 'gb': 10 ** 9, 'mb': 10 ** 6, 'kb': 10 ** 3,
                't': 10 ** 12, 'g': 10 ** 9, 'm': 10 ** 6, 'k': 10 ** 3,
            }
        modif_per_key: Dict[str, Dict[str, int]] = {
            'l1_data_cache_size': memory_size,
            'l1_instruction_cache_size': memory_size,
            'l2_cache_size': memory_size,
            'l3_cache_size': memory_size,
        }
        for key, text_value in cpu_info_dict.items():
            value = text_value
            if isinstance(text_value, str):
                if key in modif_per_key:
                    conversion_required = False
                    try:
                        value = int(text_value)
                    except ValueError:
                        conversion_required = True
                    
                    if conversion_required:
                        modif: Dict[str, int] = modif_per_key[key]
                        is_ok = False
                        minus_data_len = -len(text_value)
                        index = -1
                        while index > minus_data_len:
                            try:
                                value = int(text_value[:index])
                                is_ok = True
                                break
                            except ValueError:
                                pass

                            index -= 1
                        
                        if not is_ok:
                            index = -1
                            while index > minus_data_len:
                                try:
                                    value = float(text_value[:index])
                                    is_ok = True
                                    break
                                except ValueError:
                                    pass

                            index -= 1
                        
                        if is_ok:
                            modif_text: str = text_value[index:]
                            modif_text = modif_text.strip().casefold()
                            modif_value = modif.get(modif_text, 1)
                            value = int(value * modif_value)
                        else:
                            value = 0
                else:
                    try_with_float: bool = False
                    try:
                        value = int(text_value)
                    except ValueError:
                        try_with_float = True
                    
                    if try_with_float:
                        try:
                            value = float(text_value)
                        except ValueError:
                            value = text_value
            
            result[key] = value
        
        return result
    
    @property
    def python_version(self):
        return self._cache.get('python_version', str())
    
    @property
    def cpuinfo_version(self):
        return self._cache.get('cpuinfo_version', (0, 0, 0))
    
    @property
    def cpuinfo_version_string(self):
        return self._cache.get('cpuinfo_version_string', str())
    
    @property
    def python_hz_advertised_friendlyversion(self):
        return self._cache.get('hz_advertised_friendly', str())
    
    @property
    def hz_actual_friendly(self):
        return self._cache.get('hz_actual_friendly', str())
    
    @property
    def hz_advertised(self):
        return self._cache.get('hz_advertised', (0, 0))
    
    @property
    def hz_actual(self):
        return self._cache.get('hz_actual', (0, 0))
    
    @property
    def arch(self):
        return self._cache.get('arch', str())
    
    @property
    def bits(self):
        return self._cache.get('bits', 0)
    
    @property
    def count(self):
        return self._cache.get('count', 0)
    
    @property
    def l1_data_cache_size(self):
        return self._cache.get('l1_data_cache_size', 0)
    
    @property
    def l1_instruction_cache_size(self):
        return self._cache.get('l1_instruction_cache_size', 0)
    
    @property
    def l2_cache_size(self):
        return self._cache.get('l2_cache_size', 0)
    
    @property
    def l2_cache_line_size(self):
        return self._cache.get('l2_cache_line_size', 0)
    
    @property
    def l2_cache_associativity(self):
        return self._cache.get('l2_cache_associativity', 0)
    
    @property
    def l3_cache_size(self):
        return self._cache.get('l3_cache_size', 0)
    
    @property
    def stepping(self):
        return self._cache.get('stepping', 0)
    
    @property
    def model(self):
        return self._cache.get('model', 0)
    
    @property
    def family(self):
        return self._cache.get('family', 0)
    
    @property
    def processor_type(self):
        return self._cache.get('processor_type', 0)
    
    @property
    def flags(self):
        return self._cache.get('flags', list())
    
    @property
    def vendor_id_raw(self):
        return self._cache.get('vendor_id_raw', str())
    
    @property
    def hardware_raw(self):
        return self._cache.get('hardware_raw', str())
    
    @property
    def brand_raw(self):
        return self._cache.get('brand_raw', str())
    
    @property
    def arch_string_raw(self):
        return self._cache.get('arch_string_raw', str())
    
    @property
    def cores_num(self):
        return psutil.cpu_count(logical=False) if PSUTIL_PRESENT else 0
    
    @property
    def virtual_cores_num(self):
        return psutil.cpu_count(logical=True) if PSUTIL_PRESENT else 0
    
    @property
    def l2_cache_size_per_core(self) -> int:
        if 0 == self.count:
            return self.l2_cache_size
        
        return int(self.l2_cache_size / self.cores_num)
    
    @property
    def l2_cache_size_per_virtual_core(self) -> int:
        if 0 == self.count:
            return self.l2_cache_size
        
        return int(self.l2_cache_size / self.virtual_cores_num)
    
    @property
    def l3_cache_size_per_core(self) -> int:
        if 0 == self.count:
            return self.l3_cache_size
        
        return int(self.l3_cache_size / self.cores_num)
    
    @property
    def l3_cache_size_per_virtual_core(self) -> int:
        if 0 == self.count:
            return self.l3_cache_size
        
        return int(self.l3_cache_size / self.virtual_cores_num)
    
    @property
    def is_x86(self) -> bool:
        return self.arch.lower().startswith('x86')
    
    @property
    def is_arm(self) -> bool:
        return self.arch.lower().startswith('arm')


_CPU_INFO = None


def cpu_info() -> CpuInfo:
    global _CPU_INFO
    if _CPU_INFO is None:
        _CPU_INFO = CpuInfo()
    
    return _CPU_INFO
