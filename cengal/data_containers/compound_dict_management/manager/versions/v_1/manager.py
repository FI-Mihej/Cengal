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

from cengal.code_flow_control.smart_values import ValueExistence

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


class AddToCompoundDict:
    def __init__(self, original_dict, default_value, mediator):
        """

        :param original_dict:
        :param default_value: functor. list(); {1:set(), 2:[set(), set(), list()]}; etc.
        :param mediator: functor. original_dict[index].add(y), original_dict[index] += y, etc. Should return
            ValueExistence(True, ...) or None/nothing
        :return:
        """
        self.original_dict = original_dict
        self._mediator = mediator
        self._default_value = default_value

    def add(self, key, value=None):
        # if key not in self.original_dict:
        #     self.original_dict[key] = self._default_value()
        self.original_dict.setdefault(key, self._default_value())
        result = self._mediator(self.original_dict, key, value)
        # if result is not None:
        if isinstance(result, ValueExistence):
            self.original_dict[key] = result.value
