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
    'MemoryInfo', 
    'get_memory_info__psutil', 
    'PROC_MEMINFO_FILE', 
    'DOCKER_CGROUP_MEMORY_LIMIT_FILE', 
    'DOCKER_CGROUP_MEMORY_USAGE_FILE', 
    'DOCKER_CGROUP_MEMORY_STAT_FILE', 
    'DOCKER_CGROUP_SWAP_LIMIT_FILE', 
    'DOCKER_CGROUP_SWAP_USAGE_FILE', 
    'DOCKER_CGROUP_SWAP_STAT_FILE', 
    'MemoryInfoError', 
    'WrongOSError', 
    'ProcMeminfoFileNotFoundError', 
    'NotInDockerError', 
    'get_memory_info__linux', 
    'is_inside_docker', 
    'get_memory_info__linux_docker', 
    'MemoryInfoGetter', 
    'get_memory_info', 
    'aget_memory_info', 
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


from cengal.system import OS_TYPE
from cengal.base.exceptions import CengalError
from cengal.modules_management.alternative_import import alt_import
from cengal.modules_management.ignore_in_build_mode import ignore_in_build_mode
PSUTIL_PRESENT: bool = False
# import psutil
with ignore_in_build_mode():
    with alt_import('psutil') as psutil:
        if psutil is not None:
            PSUTIL_PRESENT = True

if 'Windows' != OS_TYPE:
    from resource import getrusage, RUSAGE_SELF

import asyncio
from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class MemoryInfo:
    ram_total: int = 0
    ram_peak_usage: int = 0
    ram_free: int = 0
    ram_used : int = 0
    ram_usage_percent: float = 0
    swap_total: int = 0
    swap_free: int = 0
    swap_used : int = 0
    swap_usage_percent: float = 0


def get_memory_info__psutil() -> MemoryInfo:
    memory_info = psutil.virtual_memory()
    swap_info = psutil.swap_memory()

    ram_total = memory_info.total
    ram_peak_usage = memory_info.total - memory_info.free
    ram_free = memory_info.available
    swap_total = swap_info.total
    swap_free = swap_info.free

    return MemoryInfo(
        ram_total=ram_total,
        ram_peak_usage=ram_peak_usage,
        ram_free=ram_free,
        ram_used=(ram_total - ram_free),
        ram_usage_percent=memory_info.percent,
        swap_total=swap_total,
        swap_free=swap_free,
        swap_used=(swap_total - swap_free),
        swap_usage_percent=swap_info.percent
    )


PROC_MEMINFO_FILE = '/proc/meminfo'
DOCKER_CGROUP_MEMORY_LIMIT_FILE = '/sys/fs/cgroup/memory/memory.limit_in_bytes'
DOCKER_CGROUP_MEMORY_USAGE_FILE = '/sys/fs/cgroup/memory/memory.usage_in_bytes'
DOCKER_CGROUP_MEMORY_STAT_FILE = '/sys/fs/cgroup/memory/memory.stat'
DOCKER_CGROUP_SWAP_LIMIT_FILE = '/sys/fs/cgroup/memory/memory.memsw.limit_in_bytes'
DOCKER_CGROUP_SWAP_USAGE_FILE = '/sys/fs/cgroup/memory/memory.memsw.usage_in_bytes'
DOCKER_CGROUP_SWAP_STAT_FILE = '/sys/fs/cgroup/memory/memory.memsw.stat'


class MemoryInfoError(CengalError):
    pass


class WrongOSError(MemoryInfoError):
    pass


class ProcMeminfoFileNotFoundError(MemoryInfoError):
    pass


class NotInDockerError(MemoryInfoError):
    pass


def get_memory_info__linux() -> MemoryInfo:
    if 'Linux' != OS_TYPE:
        raise WrongOSError

    from cengal.file_system.file_manager import file_exists
    if not file_exists(PROC_MEMINFO_FILE):
        raise ProcMeminfoFileNotFoundError
    
    with open(PROC_MEMINFO_FILE) as file:
        lines = file.readlines()
        for line in lines:
            split_line: str = line.split()
            if 'MemAvailable:' == split_line[0]:
                ram_free = int(split_line[1]) * 1024  # /proc/meminfo reports in KB
            elif 'MemTotal:' == split_line[0]:
                ram_total = int(split_line[1]) * 1024
            elif 'MemFree:' == split_line[0]:
                ram_free = int(split_line[1]) * 1024
            elif 'SwapFree:' == split_line[0]:
                swap_free = int(split_line[1]) * 1024
            elif 'SwapTotal:' == split_line[0]:
                swap_total = int(split_line[1]) * 1024
        
        ram_peak_usage = ram_total - ram_free
        ram_used = ram_total - ram_free
        swap_used = swap_total - swap_free
        ram_usage_percent = (ram_used / ram_total) * 100
        swap_usage_percent = (swap_used / swap_total) * 100

        return MemoryInfo(
            ram_total=ram_total,
            ram_peak_usage=ram_peak_usage,
            ram_free=ram_free,
            ram_used=ram_used,
            ram_usage_percent=ram_usage_percent,
            swap_total=swap_total,
            swap_free=swap_free,
            swap_used=swap_used,
            swap_usage_percent=swap_usage_percent
        )


def is_inside_docker() -> bool:
    from cengal.file_system.file_manager import file_exists
    if file_exists(DOCKER_CGROUP_MEMORY_LIMIT_FILE) and file_exists(DOCKER_CGROUP_MEMORY_USAGE_FILE) \
        and file_exists(DOCKER_CGROUP_MEMORY_STAT_FILE) and file_exists(DOCKER_CGROUP_SWAP_LIMIT_FILE) \
        and file_exists(DOCKER_CGROUP_SWAP_USAGE_FILE) and file_exists(DOCKER_CGROUP_SWAP_STAT_FILE):
        return True


IS_INSIDE_DOCKER: bool = is_inside_docker()


def is_inside_docker_cached() -> bool:
    return IS_INSIDE_DOCKER


def get_memory_info__linux_docker() -> MemoryInfo:
    if 'Linux' != OS_TYPE:
        raise WrongOSError

    if not is_inside_docker_cached():
        raise NotInDockerError
    
    with open(DOCKER_CGROUP_MEMORY_LIMIT_FILE) as file:
        ram_total = int(file.read())
    
    with open(DOCKER_CGROUP_MEMORY_USAGE_FILE) as file:
        ram_used = int(file.read())
    
    ram_free = ram_total - ram_used
    ram_usage_percent = (ram_used / ram_total) * 100

    with open(DOCKER_CGROUP_SWAP_LIMIT_FILE) as file:
        swap_total = int(file.read())
    
    with open(DOCKER_CGROUP_SWAP_USAGE_FILE) as file:
        swap_used = int(file.read())
    
    swap_free = swap_total - swap_used
    swap_usage_percent = (swap_used / swap_total) * 100

    return MemoryInfo(
        ram_total=ram_total,
        ram_peak_usage=ram_used,
        ram_free=ram_free,
        ram_used=ram_used,
        ram_usage_percent=ram_usage_percent,
        swap_total=swap_total,
        swap_free=swap_free,
        swap_used=swap_used,
        swap_usage_percent=swap_usage_percent
    )


class MemoryInfoGetter:
    def __init__(self, _is_inside_docker: Optional[Callable] = None):
        self.is_inside_docker: Callable = is_inside_docker_cached if _is_inside_docker is None else _is_inside_docker
        self._ram_peak_usage: int = 0

    def __call__(self, _is_inside_docker: Optional[Callable] = None) -> MemoryInfo:
        is_inside_docker: Callable = self.is_inside_docker if _is_inside_docker is None else _is_inside_docker

        if 'Linux' == OS_TYPE:
            if is_inside_docker():
                return get_memory_info__linux_docker()
            
            if PSUTIL_PRESENT:
                return get_memory_info__psutil()
            else:
                return get_memory_info__linux()
        else:
            memory_info: MemoryInfo = get_memory_info__psutil()
            memory_info.ram_peak_usage = self._ram_peak_usage = max(memory_info.ram_peak_usage, self._ram_peak_usage)
            return memory_info


get_memory_info = MemoryInfoGetter()


async def aget_memory_info(_is_inside_docker: Optional[Callable] = None):
    return await asyncio.get_event_loop().run_in_executor(None, get_memory_info, _is_inside_docker)
