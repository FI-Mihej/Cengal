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

from cengal.modules_management.alternative_import import alt_import
from enum import Enum
UUID_PRESENT = True
with alt_import('uuid') as uuid:
    if not uuid:
        UUID_PRESENT = False

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


class GeneratorType(Enum):
    integer = 0
    guid_string = 1
    reusable_integer = 2


class IDGenerator:
    def __init__(self, generator_type=GeneratorType.integer):
        self.counter = 0
        self.type = generator_type
        self.get_new_id = None
        if GeneratorType.integer == self.type:
            self.get_new_id = self._get_new_id__int
        elif GeneratorType.guid_string == self.type:
            if UUID_PRESENT:
                self.get_new_id = self._get_new_id__uuid
            else:
                self.get_new_id = self._get_new_id__uuid_fake
        elif GeneratorType.reusable_integer == self.type:
            raise NotImplementedError
        else:
            raise RuntimeError('Wrong `generator_type` value')

    def _get_new_id__int(self):
        current_counter = self.counter
        self.counter += 1
        return current_counter

    def _get_new_id__uuid(self):
        seq = self.counter
        self.counter += 1
        current_counter = uuid.uuid1(clock_seq=seq).hex
        return current_counter

    def _get_new_id__uuid_fake(self):
        current_counter = self.counter
        self.counter += 1
        return str(current_counter)

    def remove_id(self, id_to_be_removed):
        if GeneratorType.integer == self.type:
            pass
        elif GeneratorType.guid_string == self.type:
            pass
        elif GeneratorType.reusable_integer == self.type:
            raise NotImplementedError
        else:
            raise RuntimeError('Wrong `self.type` value')

    def clear(self):
        self.counter = 0

    def __call__(self):
        return self.get_new_id()
