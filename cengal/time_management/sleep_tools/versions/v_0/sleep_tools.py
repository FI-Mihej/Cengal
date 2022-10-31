#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2022 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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


__all__ = ['get_min_sleep_interval', 'get_usable_min_sleep_interval', 'get_countable_delta_time', 'try_sleep', 'atry_sleep']


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2022 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "0.0.8"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"

import os
from typing import Optional, Union


if 'nt' == os.name:
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


def try_sleep(secs: Union[int, float], max_secs: Optional[Union[int, float]], sleep_func, *args, **kwargs):
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


async def atry_sleep(secs: Union[int, float], max_secs: Optional[Union[int, float]], awaitable_sleep_func, *args, **kwargs):
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
