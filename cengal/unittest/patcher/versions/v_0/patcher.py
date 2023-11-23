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

from contextlib import contextmanager
from typing import List, Tuple, Optional, Any, Dict, cast

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

EntityExactHolder = Any
EntityHolder = Optional[Any]
EntityName = str
OriginalExactEntity = Tuple[EntityExactHolder, EntityName]
OriginalEntity = Tuple[EntityHolder, EntityName]
EntityMock = Any

@contextmanager
def patch_entity(original: OriginalExactEntity, mock: EntityMock):
    holder, name = original
    buff_original_value = getattr(holder, name)
    setattr(holder, name, mock)
    try:
        yield buff_original_value
    finally:
        setattr(holder, name, buff_original_value)

@contextmanager
def patch_builtins(name: EntityName, mock: EntityMock):
    buff_original_value = __builtins__[name]
    __builtins__[name] = mock
    try:
        yield buff_original_value
    finally:
        __builtins__[name] = buff_original_value

@contextmanager
def patch(original: OriginalEntity, mock: EntityMock):
    holder, name = original
    if holder is None:
        return patch_builtins(name, mock)
    else:
        return patch_entity(cast(OriginalExactEntity, original), mock)
        
@contextmanager
def patch_set(patch_set: Dict[OriginalEntity, EntityMock]):
    buff = dict()
    for original, mock in patch_set.items():
        original: OriginalEntity = original
        mock: EntityMock = mock
        holder, name = original
        holder: EntityHolder = holder
        name: EntityName = name
        if holder is None:
            buff[original] = __builtins__[name]
            __builtins__[name] = mock
        else:
            buff[original] = getattr(holder, name)
            setattr(holder, name, mock)
    try:
        yield buff
    finally:
        for original, mock in patch_set.items():
            holder, name = original
            if holder is None:
                __builtins__[name] = buff[original]
            else:
                setattr(holder, name, buff[original])
        