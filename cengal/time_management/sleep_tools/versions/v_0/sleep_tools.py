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


__all__ = ['get_min_sleep_interval', 'get_usable_min_sleep_interval', 'get_countable_delta_time',
           'ensure_waitable_time_or_smaller', 'ensure_waitable_time_or_bigger', 'try_sleep', 'sleep', 'atry_sleep']


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

import os
from typing import Optional, Union

from cengal.math.numbers import RationalNumber
from cengal.code_flow_control.args_manager import EntityArgsHolder
from cengal.time_management.high_precision_sync_sleep import hps_sleep
from cengal.system import IS_INSIDE_OR_FOR_WEB_BROWSER

if IS_INSIDE_OR_FOR_WEB_BROWSER:
    default_sleep = hps_sleep
else:
    from time import sleep as default_sleep


if IS_INSIDE_OR_FOR_WEB_BROWSER:
    _default_min_sleep_interval = 0.001
elif 'nt' == os.name:
    _default_min_sleep_interval = 0.0156
else:
    _default_min_sleep_interval = 0.0001


_countable_delta_time = 0.0000001


def get_min_sleep_interval():
    return _default_min_sleep_interval


def get_usable_min_sleep_interval():
    return _default_min_sleep_interval + _countable_delta_time


def get_countable_delta_time():
    return _countable_delta_time


def ensure_waitable_time_or_smaller(secs: RationalNumber) -> RationalNumber:
    secs = abs(secs)
    intervals: int = secs // _default_min_sleep_interval
    if not intervals:
        return 0

    return _default_min_sleep_interval * intervals + _countable_delta_time


def ensure_waitable_time_or_bigger(secs: RationalNumber) -> RationalNumber:
    if secs < get_usable_min_sleep_interval():
        return 0

    intervals: int = secs // _default_min_sleep_interval
    if secs % _default_min_sleep_interval:
        intervals += 1

    return _default_min_sleep_interval * intervals + _countable_delta_time


def try_sleep(secs: RationalNumber, max_secs: Optional[RationalNumber], sleep_func, *args, **kwargs):
    result = None
    usable_min_sleep_interval = get_usable_min_sleep_interval()

    if max_secs is not None:
        if usable_min_sleep_interval > max_secs:
            max_secs = usable_min_sleep_interval

        if secs > max_secs:
            secs = max_secs

    secs = _default_min_sleep_interval * (secs // _default_min_sleep_interval) + _countable_delta_time
    if secs >= _default_min_sleep_interval:
        still_trying = True
        while still_trying:
            secs = _default_min_sleep_interval * (secs // _default_min_sleep_interval) + _countable_delta_time

            if secs < usable_min_sleep_interval:
                secs = usable_min_sleep_interval

            try:
                # print(f'Sleepting: {secs}...')
                result = sleep_func(secs, *args, **kwargs)
                # print(f'Awaken!')
            except OverflowError:
                still_trying = True
                secs /= 2
            else:
                still_trying = False

    return result, secs


def sleep(secs: Optional[RationalNumber] = None, high_cpu_utilisation_mode: bool = False, max_secs: Optional[RationalNumber] = None, sleep_func: Optional[EntityArgsHolder] = None):
    result = None
    usable_min_sleep_interval = get_usable_min_sleep_interval()
    if secs is None:
        secs = usable_min_sleep_interval

    if max_secs is not None:
        if usable_min_sleep_interval > max_secs:
            max_secs = usable_min_sleep_interval

        if secs > max_secs:
            secs = max_secs

    secs = _default_min_sleep_interval * (secs // _default_min_sleep_interval) + _countable_delta_time
    if secs >= _default_min_sleep_interval:
        still_trying = True
        while still_trying:
            secs = _default_min_sleep_interval * (secs // _default_min_sleep_interval) + _countable_delta_time

            if secs < usable_min_sleep_interval:
                secs = usable_min_sleep_interval

            try:
                # print(f'Sleepting: {secs}...')
                if sleep_func is None:
                    result = default_sleep(secs)
                else:
                    sleep_func, args, kwargs = sleep_func.entity_args_kwargs()
                    result = sleep_func(secs, *args, **kwargs)
                # print(f'Awaken!')
            except OverflowError:
                still_trying = True
                secs /= 2
            else:
                still_trying = False
    else:
        if high_cpu_utilisation_mode and (not IS_INSIDE_OR_FOR_WEB_BROWSER):
            result = hps_sleep(secs)

    return result, secs


async def atry_sleep(secs: RationalNumber, max_secs: Optional[RationalNumber], awaitable_sleep_func, *args, **kwargs):
    result = None
    usable_min_sleep_interval = get_usable_min_sleep_interval()

    if max_secs is not None:
        if usable_min_sleep_interval > max_secs:
            max_secs = usable_min_sleep_interval

        if secs > max_secs:
            secs = max_secs

    secs = _default_min_sleep_interval * (secs // _default_min_sleep_interval) + _countable_delta_time
    if secs >= _default_min_sleep_interval:
        still_trying = True
        while still_trying:
            secs = _default_min_sleep_interval * (secs // _default_min_sleep_interval) + _countable_delta_time

            if secs < usable_min_sleep_interval:
                secs = usable_min_sleep_interval

            try:
                result = await awaitable_sleep_func(secs, *args, **kwargs)
            except OverflowError:
                still_trying = True
                secs /= 2
            else:
                still_trying = False

    return result, secs
