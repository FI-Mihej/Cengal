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
    'ProcessInfoError', 
    'GetProcessMemoryInfoError', 
    'GetProcessStartTimeError', 
    'GetProcessPeakMemoryUsageError', 
    'ProcessMemoryInfo', 
    'get_peak_memory_usage__macos_vmmap', 
    'get_peak_memory_usage__macos_top', 
    'get_process_memory_info_raw', 
    'get_process_start_timestamp', 
    'aget_process_start_timestamp', 
    'get_process_start_time', 
    'aget_process_start_time', 
    'ProcessMemoryInfoGetter', 
    'get_process_memory_info', 
    'aget_process_memory_info', 
    'get_process_tree_memory_info', 
    'aget_process_tree_memory_info', 
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
from cengal.hardware.memory.info import get_memory_info
from cengal.modules_management.alternative_import import alt_import
from cengal.modules_management.ignore_in_build_mode import ignore_in_build_mode
PSUTIL_PRESENT: bool = False
# import psutil
with ignore_in_build_mode():
    with alt_import('psutil') as psutil:
        if psutil is not None:
            PSUTIL_PRESENT = True

# if 'Windows' != OS_TYPE:
#     from resource import getrusage, RUSAGE_SELF

import asyncio
import subprocess
from datetime import datetime
from dataclasses import dataclass, replace
from typing import Callable, Optional, Dict, Tuple, Set


class ProcessInfoError(CengalError):
    pass


class GetProcessMemoryInfoError(ProcessInfoError):
    pass


class GetProcessStartTimeError(ProcessInfoError):
    pass


class GetProcessPeakMemoryUsageError(ProcessInfoError):
    pass


@dataclass
class ProcessMemoryInfo:
    ram_usage: int = 0
    peak_total_ram_usage: int = 0
    peak_own_ram_usage: int = 0
    swap_usage: int = 0
    peak_total_memory_usage: int = 0
    ram_usage_percent: float = 0
    peak_total_ram_usage_percent: float = 0
    peak_own_ram_usage_percent: float = 0
    swap_usage_percent: float = 0
    peak_total_memory_usage_percent: float = 0


if 'Darwin' == OS_TYPE:
    import re
    _GET_PEAK_MEMORY_USAGE__MACOS_VMMAP__PEAK_MEMORY_PATTERN: re.Pattern = re.compile(r'(\d+)\s+\(peak\)')
else:
    _GET_PEAK_MEMORY_USAGE__MACOS_VMMAP__PEAK_MEMORY_PATTERN = None


def get_peak_memory_usage__macos_vmmap(pid) -> int:
    try:
        result = subprocess.run(['vmmap', str(pid)], capture_output=True, text=True)
        output = result.stdout

        match = _GET_PEAK_MEMORY_USAGE__MACOS_VMMAP__PEAK_MEMORY_PATTERN.search(output)
        if match:
            peak_memory_kb = int(match.group(1))
            peak_memory_bytes = peak_memory_kb * 1024  # Convert from KB to bytes
            return peak_memory_bytes
        else:
            raise GetProcessPeakMemoryUsageError('Peak memory usage not found in vmmap output')
    except subprocess.CalledProcessError as ex:
        raise GetProcessPeakMemoryUsageError(f'Error running vmmap: {ex}')
    except Exception as ex:
        raise GetProcessPeakMemoryUsageError(f'Error occurred: {ex}')


def get_peak_memory_usage__macos_top(pid) -> int:
    try:
        result = subprocess.run(['top', '-l', '1', '-pid', str(pid), '-stats', 'pid,rsize'], capture_output=True, text=True)
        output = result.stdout

        memory_pattern: re.Pattern = re.compile(rf'^\s*{pid}\s+(\d+)[KMG]?$', re.MULTILINE)
        match = memory_pattern.search(output)
        if match:
            memory_value = match.group(1)
            memory_value_casefold = memory_value.casefold()
            if 'm' in memory_value_casefold:
                memory_bytes = int(memory_value[:-1]) * 1024 * 1024
            elif 'k' in memory_value_casefold:
                memory_bytes = int(memory_value[:-1]) * 1024
            elif 'g' in memory_value_casefold:
                memory_bytes = int(memory_value[:-1]) * 1024 * 1024 * 1024
            else:
                memory_bytes = int(memory_value)

            return memory_bytes
        else:
            raise GetProcessPeakMemoryUsageError('Memory usage not found in top output')
    except subprocess.CalledProcessError as ex:
        raise GetProcessPeakMemoryUsageError(f'Error running top: {ex}')
    except Exception as ex:
        raise GetProcessPeakMemoryUsageError(f'Error occurred: {ex}')


def get_process_memory_info_raw(process_id: int) -> ProcessMemoryInfo:
    from cengal.file_system.file_manager import file_exists

    ram_total = get_memory_info().ram_total
    swap_total = get_memory_info().swap_total
    memory_total = ram_total + swap_total
    if 'Linux' == OS_TYPE:
        process_status_file_path = f'/proc/{process_id}/status'
        if not file_exists(process_status_file_path):
            raise GetProcessMemoryInfoError
        
        peak_total_ram_usage = peak_own_ram_usage = ram_usage = swap_usage = peak_total_memory_usage = 0
        try:
            with open(process_status_file_path) as file:
                lines = file.readlines()
                for line in lines:
                    split_line: str = line.split()
                    if 'VmPeak:' == split_line[0]:
                        peak_total_ram_usage = int(split_line[1]) * 1024  # /proc/meminfo reports in KB
                    elif 'VmHWM:' == split_line[0]:
                        peak_own_ram_usage = int(split_line[1]) * 1024
                    elif 'VmRSS:' == split_line[0]:
                        ram_usage = int(split_line[1]) * 1024
                    elif 'VmSwap:' == split_line[0]:
                        swap_usage = int(split_line[1]) * 1024

            peak_total_memory_usage = peak_total_ram_usage + swap_usage
        except (OSError, IndexError, ValueError):
            peak_total_ram_usage = peak_own_ram_usage = ram_usage = swap_usage = peak_total_memory_usage = 0

        if (0 == peak_total_ram_usage) and (0 == peak_own_ram_usage) and (0 == ram_usage) and (0 == swap_usage) and (0 == peak_total_memory_usage):
            process = psutil.Process(process_id)
            peak_total_ram_usage = peak_own_ram_usage = ram_usage = process.memory_info().rss
            swap_usage = process.memory_info().vms
            peak_total_memory_usage = peak_total_ram_usage + swap_usage
    elif 'Darwin' == OS_TYPE:
        process = psutil.Process(process_id)
        peak_total_ram_usage = peak_own_ram_usage = ram_usage = process.memory_info().rss
        try:
            peak_total_ram_usage = peak_own_ram_usage = get_peak_memory_usage__macos_vmmap(process_id)
        except GetProcessPeakMemoryUsageError:
            try:
                peak_total_ram_usage = peak_own_ram_usage = get_peak_memory_usage__macos_top(process_id)
            except GetProcessPeakMemoryUsageError:
                pass
        
        swap_usage = process.memory_info().vms
        peak_total_memory_usage = peak_total_ram_usage + swap_usage
    elif 'Windows' == OS_TYPE:
        try:
            process = psutil.Process(process_id)
            peak_total_ram_usage = peak_own_ram_usage = process.memory_info().peak_wset
            ram_usage = process.memory_info().wset
            swap_usage = process.memory_info().pagefile
            peak_total_memory_usage = process.memory_info().peak_pagefile
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            raise GetProcessMemoryInfoError
    else:
        raise NotImplementedError

    peak_total_ram_usage_percent = (peak_total_ram_usage / memory_total) * 100
    peak_own_ram_usage_percent = (peak_own_ram_usage / ram_total) * 100
    ram_usage_percent = (ram_usage / ram_total) * 100
    swap_usage_percent = (swap_usage / swap_total) * 100
    peak_total_memory_usage_percent = (peak_total_memory_usage / memory_total) * 100

    return ProcessMemoryInfo(
        ram_usage=ram_usage,
        peak_total_ram_usage=peak_total_ram_usage,
        peak_own_ram_usage=peak_own_ram_usage,
        swap_usage=swap_usage,
        peak_total_memory_usage=peak_total_memory_usage,
        ram_usage_percent=ram_usage_percent,
        peak_total_ram_usage_percent=peak_total_ram_usage_percent,
        peak_own_ram_usage_percent=peak_own_ram_usage_percent,
        swap_usage_percent=swap_usage_percent,
        peak_total_memory_usage_percent=peak_total_memory_usage_percent,
    )


def get_process_start_timestamp(process_id: int) -> float:
    """Return the process start time in seconds since the epoch.

    Args:
        process_id (int): _description_

    Returns:
        float: _description_
    """    
    try:
        process = psutil.Process(process_id)
        return process.create_time()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        raise GetProcessStartTimeError


async def aget_process_start_timestamp(process_id: int) -> str:
    return await asyncio.get_event_loop().run_in_executor(None, get_process_start_timestamp, process_id)


def get_process_start_time(process_id: int, format: str = '%Y-%m-%d %H:%M:%S.%f') -> str:
    try:
        process = psutil.Process(process_id)
        start_time = process.create_time()
        return datetime.fromtimestamp(start_time).strftime(format)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        raise GetProcessStartTimeError


async def aget_process_start_time(process_id: int, format: str = '%Y-%m-%d %H:%M:%S.%f') -> str:
    return await asyncio.get_event_loop().run_in_executor(None, get_process_start_time, process_id, format)


class ProcessMemoryInfoGetter:
    def __init__(self) -> None:
        self._processes_peak_memory_info: Dict[Tuple[int, float], ProcessMemoryInfo] = dict()  # [process_id, timestamp] -> ProcessMemoryInfo
        self._last_process_timestamp: Dict[int, float] = dict()  # process_id -> timestamp

    def __call__(self, process_id: int) -> ProcessMemoryInfo:
        process_memory_info: ProcessMemoryInfo = get_process_memory_info_raw(process_id)
        ram_total = get_memory_info().ram_total
        swap_total = get_memory_info().swap_total
        memory_total = ram_total + swap_total
        process_timestamp = get_process_start_timestamp(process_id)
        process_timed_id = (process_id, process_timestamp)
        try:
            process_peak_memory_info: ProcessMemoryInfo = self._processes_peak_memory_info[process_timed_id]
            
            # process_peak_memory_info.peak_total_ram_usage = process_memory_info.peak_total_ram_usage = max(process_memory_info.peak_total_ram_usage, process_peak_memory_info.peak_total_ram_usage)
            # process_memory_info.peak_total_ram_usage_percent = (process_peak_memory_info.peak_total_ram_usage / ram_total) * 100

            # process_peak_memory_info.peak_own_ram_usage = process_memory_info.peak_own_ram_usage = max(process_memory_info.peak_own_ram_usage, process_peak_memory_info.peak_own_ram_usage)
            # process_peak_memory_info.peak_own_ram_usage_percent = (process_memory_info.peak_own_ram_usage / ram_total) * 100
            
            if 'Windows' != OS_TYPE:
                process_peak_memory_info.peak_total_memory_usage = process_memory_info.peak_total_memory_usage = max(process_memory_info.peak_total_memory_usage, process_peak_memory_info.peak_total_memory_usage)
                process_memory_info.peak_total_memory_usage_percent = (process_peak_memory_info.peak_total_memory_usage / memory_total) * 100
        except KeyError:
            try:
                last_timestamp = self._last_process_timestamp[process_id]
                last_process_timed_id = (process_id, last_timestamp)
                del self._processes_peak_memory_info[last_process_timed_id]
            except KeyError:
                pass
            
            self._last_process_timestamp[process_id] = process_timestamp
            self._processes_peak_memory_info[process_timed_id] = replace(process_memory_info)
        
        return process_memory_info


get_process_memory_info = ProcessMemoryInfoGetter()


async def aget_process_memory_info(process_id: int) -> ProcessMemoryInfo:
    return await asyncio.get_event_loop().run_in_executor(None, get_process_memory_info, process_id)


def get_process_tree_memory_info(process_id: int, exclude: Optional[Set[int]] = None, exclude_tree: Optional[Set[int]] = None, progress_callback: Optional[Callable] = None) -> ProcessMemoryInfo:
    """returns summarized memory info for the process tree starting from the specified process_id.
    If exclude is specified, the specified process_id and all its children will be excluded from the result.

    Args:
        process_id (int): _description_
        exclude (Optional[Set[int]], optional): _description_. Defaults to None.
        exclude_tree (Optional[Set[int]], optional): _description_. Defaults to None.
        progress_callback (Optional[Callable], optional): _description_. Defaults to None. # progress_callback(process_id)

    Returns:
        Dict[int, ProcessMemoryInfo]: _description_
    """
    if progress_callback:
        progress_callback(process_id)

    if exclude is None:
        exclude = set()
    
    if exclude_tree is None:
        exclude_tree = set()
    
    if process_id in exclude:
        process_memory_info: ProcessMemoryInfo = ProcessMemoryInfo()
    else:
        process_memory_info = get_process_memory_info(process_id)
    
    if process_id not in exclude_tree:
        children = psutil.Process(process_id).children(recursive=False)
        for child in children:
            child_memory_info: ProcessMemoryInfo = get_process_tree_memory_info(child.pid, exclude=exclude, exclude_tree=exclude_tree, progress_callback=progress_callback)
            process_memory_info.ram_usage += child_memory_info.ram_usage
            process_memory_info.peak_total_ram_usage += child_memory_info.peak_total_ram_usage
            process_memory_info.peak_own_ram_usage += child_memory_info.peak_own_ram_usage
            process_memory_info.swap_usage += child_memory_info.swap_usage
            process_memory_info.peak_total_memory_usage += child_memory_info.peak_total_memory_usage
            process_memory_info.ram_usage_percent += child_memory_info.ram_usage_percent
            process_memory_info.peak_total_ram_usage_percent += child_memory_info.peak_total_ram_usage_percent
            process_memory_info.peak_own_ram_usage_percent += child_memory_info.peak_own_ram_usage_percent
            process_memory_info.swap_usage_percent += child_memory_info.swap_usage_percent
            process_memory_info.peak_total_memory_usage_percent += child_memory_info.peak_total_memory_usage_percent
    
    return process_memory_info


async def aget_process_tree_memory_info(process_id: int, exclude: Optional[Set[int]] = None, exclude_tree: Optional[Set[int]] = None, progress_callback: Optional[Callable] = None) -> ProcessMemoryInfo:
    return await asyncio.get_event_loop().run_in_executor(None, get_process_tree_memory_info, process_id, exclude, exclude_tree, progress_callback)
