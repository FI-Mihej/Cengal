#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.2.2"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"
__all__ = ['create_task_awaitable', 'create_task']


import sys
import asyncio


def create_task_awaitable(asyncio_awaitable) -> asyncio.Task:
    if 7 <= sys.version_info[1] and 2 <= sys.version_info[0]:
        return asyncio.create_task(asyncio_awaitable)
    else:
        return asyncio.get_event_loop().create_task(asyncio_awaitable)


def create_task(asyncio_coroutine, *args, **kwargs) -> asyncio.Task:
    if 7 <= sys.version_info[1] and 2 <= sys.version_info[0]:
        return asyncio.create_task(asyncio_coroutine(*args, **kwargs))
    else:
        return asyncio.get_event_loop().create_task(asyncio_coroutine(*args, **kwargs))
