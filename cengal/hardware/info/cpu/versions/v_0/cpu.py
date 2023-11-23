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

import cpuinfo

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


def get_cpu_info()->dict:
    return cpuinfo.get_cpu_info()


def get_l2_cache_size()->int:
    size_text = cpuinfo.get_cpu_info()['l2_cache_size']
    size_text_list = size_text.split()
    size_text_list_size = len(size_text_list)
    size_text_number = None
    size_text_dimension = None
    if 0 == size_text_list_size:
        return 0
    elif 1 == size_text_list_size:
        return int(size_text_list)
    elif 2 == size_text_list_size:
        size_text_number, size_text_dimension = size_text_list
    else:
        return 0
    size_text_number = int(size_text_number)
    size_text_dimension = size_text_dimension.lower()
    factor = 1
    if 'kb' == size_text_dimension:
        factor = 1024
    elif 'mb' == size_text_dimension:
        factor = 1024**2
    elif 'gb' == size_text_dimension:
        factor = 1024**3  # :)
    return size_text_number * factor


def l2_cache_per_core()->int:
    core_count = cpuinfo.get_cpu_info()['count']
    if core_count:
        return int(get_l2_cache_size() / core_count)
    else:
        return 0
