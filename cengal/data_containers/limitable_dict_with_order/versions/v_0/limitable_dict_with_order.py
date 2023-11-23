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


from cengal.code_flow_control.none_or import none_or
from typing import Dict, List, Optional


class LimitableDictWithOrder:
    def __init__(self, low_water: int, hi_water: int, data: Optional[Dict] = None, order: Optional[List] = None) -> None:
        self.low_water: int = low_water if low_water >= 0 else 0
        self.hi_water: int = hi_water if hi_water >= 0 else 0
        self.data: Optional[Dict] = none_or(data, dict())
        self.order: Optional[List] = none_or(order, list())
    
    def check_limits(self):
        if len(self.order) <= self.hi_water:
            return

        keys_to_delete = self.order[:-self.low_water]
        self.order = self.order[-self.low_water:]
        for key in keys_to_delete:
            self.data.pop(key, None)

    def __call__(self):
        return self.check_limits()
