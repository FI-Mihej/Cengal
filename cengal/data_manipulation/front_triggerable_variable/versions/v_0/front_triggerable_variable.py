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


__all__ = ['FrontTriggerableVariableType', 'FrontTriggerableVariable']


from enum import Enum
from typing import Union

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


class FrontTriggerableVariableType(Enum):
    equal = 0
    lesser = 1
    lesser_or_equal = 2
    bigger = 3
    bigger_or_equal = 4
    not_equal = 5


class FrontTriggerableVariable:
    def __init__(self, triggerable_variable_type, value_limit):
        self.triggerable_variable_type = triggerable_variable_type
        self.value_limit = value_limit
        self._last_result = None
        self.test_worker = None
        self.set_triggerable_variable_type(triggerable_variable_type)
    
    def set_triggerable_variable_type(self, triggerable_variable_type):
        self._last_result = None
        self.triggerable_variable_type = triggerable_variable_type
        if FrontTriggerableVariableType.equal == triggerable_variable_type:
            self.test_worker = FrontTriggerableVariable._equal
        elif FrontTriggerableVariableType.lesser == triggerable_variable_type:
            self.test_worker = FrontTriggerableVariable._lesser
        elif FrontTriggerableVariableType.lesser_or_equal == triggerable_variable_type:
            self.test_worker = FrontTriggerableVariable._lesser_or_equal
        elif FrontTriggerableVariableType.bigger == triggerable_variable_type:
            self.test_worker = FrontTriggerableVariable._bigger
        elif FrontTriggerableVariableType.bigger_or_equal == triggerable_variable_type:
            self.test_worker = FrontTriggerableVariable._bigger_or_equal
        elif FrontTriggerableVariableType.not_equal == triggerable_variable_type:
            self.test_worker = FrontTriggerableVariable._not_equal

    def test_trigger(self, value) -> Union[None, bool]:
        result = None
        new_test_result = self.test_worker(value, self.value_limit)
        if new_test_result != self._last_result:
            self._last_result = new_test_result
            result = new_test_result
        
        return result

    def __call__(self, value) -> Union[None, bool]:
        return self.test_trigger(value)

    @staticmethod
    def _equal(value, value_limit) -> bool:
        return value == value_limit

    @staticmethod
    def _lesser(value, value_limit) -> bool:
        return value < value_limit

    @staticmethod
    def _lesser_or_equal(value, value_limit) -> bool:
        return value <= value_limit

    @staticmethod
    def _bigger(value, value_limit) -> bool:
        return value > value_limit

    @staticmethod
    def _bigger_or_equal(value, value_limit) -> bool:
        return value >= value_limit

    @staticmethod
    def _not_equal(value, value_limit) -> bool:
        return value != value_limit
