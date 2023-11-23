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


__all__ = ['IOCoreMemoryManagement']


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


class IOCoreMemoryManagement:
    def __init__(self):
        self.global__data_size_limit = ValueExistence(True, 2 * 1024**3)
        self.global__data_full_size = ValueExistence(True, 0)
        self.global__deletable_data_full_size = ValueExistence(True, 0)

        self.global_other__data_size_limit = ValueExistence(True, 512 * 1024**2)
        self.global_other__data_full_size = ValueExistence(True, 0)
        self.global_other__deletable_data_full_size = ValueExistence(True, 0)

        self.global_in__data_size_limit = ValueExistence(True, 512 * 1024**2)
        self.global_in__data_full_size = ValueExistence(True, 0)
        self.global_in__deletable_data_full_size = ValueExistence(True, 0)

        self.global_out__data_size_limit = ValueExistence(True, 512 * 1024**2)
        self.global_out__data_full_size = ValueExistence(True, 0)
        self.global_out__deletable_data_full_size = ValueExistence(True, 0)

    def link_to(self, parent):
        self.global__data_size_limit = parent.global__data_size_limit
        self.global__data_full_size = parent.global__data_full_size
        self.global__deletable_data_full_size = parent.global__deletable_data_full_size

        self.global_other__data_size_limit = parent.global_other__data_size_limit
        self.global_other__data_full_size = parent.global_other__data_full_size
        self.global_other__deletable_data_full_size = parent.global_other__deletable_data_full_size

        self.global_in__data_size_limit = parent.global_in__data_size_limit
        self.global_in__data_full_size = parent.global_in__data_full_size
        self.global_in__deletable_data_full_size = parent.global_in__deletable_data_full_size

        self.global_out__data_size_limit = parent.global_out__data_size_limit
        self.global_out__data_full_size = parent.global_out__data_full_size
        self.global_out__deletable_data_full_size = parent.global_out__deletable_data_full_size
