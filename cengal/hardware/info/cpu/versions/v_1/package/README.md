# cengal_cpu_info

Extended, cached CPU info with consistent output format.

# Advantages

Consistent output format of memory-related values (unlike backend 'py-cpuinfo' package). Provides additional information. Provides cached instance (backend 'py-cpuinfo' package requires several seconds per an each call to gather CPU information).

# Installation

```bash
pip install cengal_cpu_info
```

# Documentation

## Import

```python
from cengal_cpu_info import cpu_info, CpuInfo
```

## Cached instance

```python
ci: CpuInfo = cpu_info()
```

## Methods

```python
print(f'{ci.is_arm=}')
print(f'{ci.is_x86=}')
print(f'{ci.cores_num=}')
print(f'{ci.virtual_cores_num=}')
print(f'{ci.l2_cache_size_per_core=}')
print(f'{ci.l2_cache_size_per_virtual_core=}')
print(f'{ci.l3_cache_size_per_core=}')
print(f'{ci.l3_cache_size_per_virtual_core=}')
print(f'{ci.arch=}')
print(f'{ci.arch_string_raw=}')
print(f'{ci.bits=}')
print(f'{ci.brand_raw=}')
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
print(f'{ci.l3_cache_size=}')
print(f'{ci.model=}')
print(f'{ci.processor_type=}')
print(f'{ci.python_hz_advertised_friendlyversion=}')
print(f'{ci.python_version=}')
print(f'{ci.stepping=}')
print(f'{ci.vendor_id_raw=}')
```

## Example output

```python
ci.is_arm=False
ci.is_x86=True
ci.cores_num=4
ci.virtual_cores_num=4
ci.l2_cache_size_per_core=262144
ci.l2_cache_size_per_virtual_core=262144
ci.l3_cache_size_per_core=1572864
ci.l3_cache_size_per_virtual_core=1572864
ci.arch='X86_64'
ci.arch_string_raw='x86_64'
ci.bits=64
ci.brand_raw='Intel(R) Core(TM) i5-3570 CPU @ 3.40GHz'
ci.count=4
ci.cpuinfo_version=[9, 0, 0]
ci.cpuinfo_version_string='9.0.0'
ci.family=6
ci.flags=['aes', 'apic', 'arch_capabilities', 'arch_perfmon', 'avx', 'clflush', 'cmov', 'constant_tsc', 'cpuid', 'cx16', 'cx8', 'de', 'erms', 'f16c', 'flush_l1d', 'fpu', 'fsgsbase', 'fxsr', 'ht', 'hypervisor', 'ibpb', 'ibrs', 'lahf_lm', 'lm', 'mca', 'mce', 'md_clear', 'mmx', 'msr', 'mtrr', 'nopl', 'nx', 'osxsave', 'pae', 'pat', 'pcid', 'pclmulqdq', 'pdcm', 'pge', 'pni', 'popcnt', 'pse', 'pse36', 'pti', 'rdrand', 'rdrnd', 'rdtscp', 'rep_good', 'sep', 'smep', 'ss', 'ssbd', 'sse', 'sse2', 'sse4_1', 'sse4_2', 'ssse3', 'stibp', 'syscall', 'tsc', 'vme', 'xsave', 'xsaveopt', 'xtopology']
ci.hardware_raw=''
ci.hz_actual=[3403348000, 0]
ci.hz_actual_friendly='3.4033 GHz'
ci.hz_advertised=[3400000000, 0]
ci.l1_data_cache_size=131072
ci.l1_instruction_cache_size=131072
ci.l2_cache_associativity=6
ci.l2_cache_line_size=256
ci.l2_cache_size=1048576
ci.l3_cache_size=6291456
ci.model=58
ci.processor_type=0
ci.python_hz_advertised_friendlyversion='3.4000 GHz'
ci.python_version='3.8.10.final.0 (64 bit)'
ci.stepping=9
ci.vendor_id_raw='GenuineIntel'
```

# Based on Cengal

Represents part of Cengal library:
* https://pypi.org/project/cengal/
* https://github.com/FI-Mihej/Cengal

An equivalent import:
```python
from cengal.hardware.info.cpu import cpu_info, CpuInfo
```

Cengal library can be installed by:

```bash
pip install cengal
```


# Projects using Cengal

* [flet_async](https://github.com/FI-Mihej/flet_async) - wrapper which makes [Flet](https://github.com/flet-dev/flet) async and brings booth Cengal.coroutines and asyncio to Flet (Flutter based UI)
* [justpy_containers](https://github.com/FI-Mihej/justpy_containers) - wrapper around [JustPy](https://github.com/justpy-org/justpy) in order to bring more security and more production-needed features to JustPy (VueJS based UI)
* [Bensbach](https://github.com/FI-Mihej/Bensbach) - decompiler from Unreal Engine 3 bytecode to a Lisp-like script and compiler back to Unreal Engine 3 bytecode. Made for a game modding purposes
* [Realistic-Damage-Model-mod-for-Long-War](https://github.com/FI-Mihej/Realistic-Damage-Model-mod-for-Long-War) - Mod for both the original XCOM:EW and the mod Long War. Was made with a Bensbach, which was made with Cengal
* [SmartCATaloguer.com](http://www.smartcataloguer.com/index.html) - TagDB based catalog of images (tags), music albums (genre tags) and apps (categories)

# License

Copyright © 2012-2024 ButenkoMS. All rights reserved.

Licensed under the Apache License, Version 2.0.
