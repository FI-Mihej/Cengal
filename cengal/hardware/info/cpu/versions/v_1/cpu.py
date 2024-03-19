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

import sys
from typing import Dict, Set, Optional


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


if hasattr(cpuinfo.cpuinfo, '_check_arch'):
    check_arch = getattr(cpuinfo.cpuinfo, '_check_arch')
    try:
        check_arch()
    except:
        CPUINFO_PRESENT = False


_known_gathering_methods_names = (
    '_get_cpu_info_from_wmic',
    '_get_cpu_info_from_registry',
    '_get_cpu_info_from_proc_cpuinfo',
    '_get_cpu_info_from_cpufreq_info',
    '_get_cpu_info_from_lscpu',
    '_get_cpu_info_from_sysctl',
    '_get_cpu_info_from_kstat',
    '_get_cpu_info_from_dmesg',
    '_get_cpu_info_from_cat_var_run_dmesg_boot',
    '_get_cpu_info_from_ibm_pa_features',
    '_get_cpu_info_from_sysinfo',
    '_get_cpu_info_from_cpuid',
    '_get_cpu_info_from_platform_uname',
)
last_stage = len(_known_gathering_methods_names) - 1
stage_after_last = last_stage + 1


_can_use_lazy_gathering = True
if hasattr(cpuinfo.cpuinfo, '_copy_new_fields'):
    copy_new_fields = getattr(cpuinfo.cpuinfo, '_copy_new_fields')
elif hasattr(cpuinfo.cpuinfo, 'CopyNewFields'):
    copy_new_fields = getattr(cpuinfo.cpuinfo, 'CopyNewFields')
else:
    _can_use_lazy_gathering = False


def get_cpu_info_lazy(desired_keys = None, stage = 0, info = None):
    stage = stage if stage is not None else 0
    stage = stage if stage >= 0 else last_stage

    arch, bits = cpuinfo.cpuinfo._parse_arch(cpuinfo.cpuinfo.DataSource.arch_string_raw)

    friendly_maxsize = { 2**31-1: '32 bit', 2**63-1: '64 bit' }.get(sys.maxsize) or 'unknown bits'
    friendly_version = "{0}.{1}.{2}.{3}.{4}".format(*sys.version_info)
    PYTHON_VERSION = "{0} ({1})".format(friendly_version, friendly_maxsize)

    info = {
        'python_version' : PYTHON_VERSION,
        'cpuinfo_version' : cpuinfo.cpuinfo.CPUINFO_VERSION,
        'cpuinfo_version_string' : cpuinfo.cpuinfo.CPUINFO_VERSION_STRING,
        'arch' : arch,
        'bits' : bits,
        'count' : cpuinfo.cpuinfo.DataSource.cpu_count,
        'arch_string_raw' : cpuinfo.cpuinfo.DataSource.arch_string_raw,
    } if info is None else info

    if desired_keys is None:
        return info, stage

    desired_keys = desired_keys if isinstance(desired_keys, set) else set(desired_keys)
    flags: bool = 'flags' in desired_keys

    if (not flags) & (not (desired_keys - set(info.keys()))):
        return info, stage
    
    current_stage = -1
    for method_name in _known_gathering_methods_names:
        current_stage += 1
        if current_stage < stage:
            continue

        if hasattr(cpuinfo.cpuinfo, method_name):
            method = getattr(cpuinfo.cpuinfo, method_name)
            copy_new_fields(info, method())
            if (not flags) & (not (desired_keys - set(info.keys()))):
                break
    
    next_stage = current_stage + 1
    if next_stage >= stage_after_last:
        next_stage = None
    
    return info, next_stage


class CpuInfo:
    _cache: Dict = None
    _stage: int = None
    _cache_friendly: Dict = None
    _cores_num: int = None
    _virtual_cores_num: int = None

    def __init__(self, desired_keys: Optional[Set[str]] = None, stage: Optional[int] = 0, info: Dict = None):
        if CpuInfo._cores_num is None:
            CpuInfo._cores_num = psutil.cpu_count(logical=False) if PSUTIL_PRESENT else 0
        
        if CpuInfo._virtual_cores_num is None:
            CpuInfo._virtual_cores_num = psutil.cpu_count(logical=True) if PSUTIL_PRESENT else 0
        
        if CpuInfo._cache is None:
            if _can_use_lazy_gathering:
                CpuInfo._cache_friendly, CpuInfo._stage = get_cpu_info_lazy(desired_keys, stage, info) if CPUINFO_PRESENT else ((dict(), stage) if info is None else (info, stage))
            else:
                CpuInfo._cache_friendly = cpuinfo.get_cpu_info() if CPUINFO_PRESENT else (dict() if info is None else info)
            
            CpuInfo._cache = self._normalize_cpu_info_values(CpuInfo._cache_friendly)
    
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

    def _ensure_field(self, field_name):
        if not CPUINFO_PRESENT:
            return field_name
        
        if not _can_use_lazy_gathering:
            return field_name

        if ('flags' != field_name) & (field_name in self._cache):
            return field_name

        CpuInfo._cache_friendly, CpuInfo._stage = get_cpu_info_lazy({field_name,}, CpuInfo._stage, CpuInfo._cache_friendly)
        CpuInfo._cache = self._normalize_cpu_info_values(CpuInfo._cache_friendly)
        return field_name
    
    @property
    def python_version(self):
        return self._cache.get(self._ensure_field('python_version'), str())
    
    @property
    def cpuinfo_version(self):
        return self._cache.get(self._ensure_field('cpuinfo_version'), (0, 0, 0))
    
    @property
    def cpuinfo_version_string(self):
        return self._cache.get(self._ensure_field('cpuinfo_version_string'), str())
    
    @property
    def python_hz_advertised_friendlyversion(self):
        return self._cache.get(self._ensure_field('hz_advertised_friendly'), str())
    
    @property
    def hz_actual_friendly(self):
        return self._cache.get(self._ensure_field('hz_actual_friendly'), str())
    
    @property
    def hz_advertised(self):
        return self._cache.get(self._ensure_field('hz_advertised'), (0, 0))
    
    @property
    def hz_actual(self):
        return self._cache.get(self._ensure_field('hz_actual'), (0, 0))
    
    @property
    def arch(self):
        return self._cache.get(self._ensure_field('arch'), str())
    
    @property
    def bits(self):
        return self._cache.get(self._ensure_field('bits'), 0)
    
    @property
    def count(self):
        return self._cache.get(self._ensure_field('count'), 0)
    
    @property
    def l1_data_cache_size(self):
        return self._cache.get(self._ensure_field('l1_data_cache_size'), 0)
    
    @property
    def l1_instruction_cache_size(self):
        return self._cache.get(self._ensure_field('l1_instruction_cache_size'), 0)
    
    @property
    def l2_cache_size(self):
        return self._cache.get(self._ensure_field('l2_cache_size'), 0)
    
    @property
    def l2_cache_line_size(self):
        return self._cache.get(self._ensure_field('l2_cache_line_size'), 0)
    
    @property
    def l2_cache_associativity(self):
        return self._cache.get(self._ensure_field('l2_cache_associativity'), 0)
    
    @property
    def l3_cache_size(self):
        return self._cache.get(self._ensure_field('l3_cache_size'), 0)
    
    @property
    def stepping(self):
        return self._cache.get(self._ensure_field('stepping'), 0)
    
    @property
    def model(self):
        return self._cache.get(self._ensure_field('model'), 0)
    
    @property
    def family(self):
        return self._cache.get(self._ensure_field('family'), 0)
    
    @property
    def processor_type(self):
        return self._cache.get(self._ensure_field('processor_type'), 0)
    
    @property
    def flags(self):
        return self._cache.get(self._ensure_field('flags'), list())
    
    @property
    def vendor_id_raw(self):
        return self._cache.get(self._ensure_field('vendor_id_raw'), str())
    
    @property
    def hardware_raw(self):
        return self._cache.get(self._ensure_field('hardware_raw'), str())
    
    @property
    def brand_raw(self):
        return self._cache.get(self._ensure_field('brand_raw'), str())
    
    @property
    def arch_string_raw(self):
        return self._cache.get(self._ensure_field('arch_string_raw'), str())
    
    @property
    def cores_num(self):
        return CpuInfo._cores_num if CpuInfo._cores_num else self.count
    
    @property
    def virtual_cores_num(self):
        return CpuInfo._virtual_cores_num if CpuInfo._virtual_cores_num else CpuInfo._cores_num
    
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
    
    def gather_all(self):
        self.flags


_CPU_INFO = None


def cpu_info() -> CpuInfo:
    global _CPU_INFO
    if _CPU_INFO is None:
        _CPU_INFO = CpuInfo()
    
    return _CPU_INFO
