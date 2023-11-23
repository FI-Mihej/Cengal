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


__all__ = ['StreamType', 'GateSecurityPolicy', 'IOCoreMemoryManagement', 'StreamManagerIOCoreMemoryManagement']


from enum import Enum
from cengal.hardware.info.cpu.versions.v_1 import CpuInfo
from cengal.io.core.memory_management import IOCoreMemoryManagement
from cengal.code_flow_control.smart_values.versions import ValueExistence
from typing import Optional
from .efficient_streams_base_internal import *


class StreamType(Enum):
    general = 0
    message_based_anonymous = 1
    message_based_names = 2
    gate = 3


class GateSecurityPolicy(Enum):
    # gate will allow only or ban selected stream names to conect to this gate
    allowed = 0
    disabled = 1


class StreamManagerIOCoreMemoryManagement(IOCoreMemoryManagement):
    def __init__(self):
        super(StreamManagerIOCoreMemoryManagement, self).__init__()

        self.socket_write_fixed_buffer_size = ValueExistence(True,
                                                             CpuInfo().l2_cache_size_per_virtual_core)

    def link_to(self, parent):
        super(StreamManagerIOCoreMemoryManagement, self).link_to(parent)
        try:
            self.socket_write_fixed_buffer_size = parent.socket_write_fixed_buffer_size
        except AttributeError:
            pass
