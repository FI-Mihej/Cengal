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


from typing import Optional


DEFAULT_PROTOCOL_GREETING = b'<<MessageProtocol>>'
MESSAGE_SIZE_MAX_POSSIBLE_LEN = 8
MESSAGE_SIZE_LEN = MESSAGE_SIZE_MAX_POSSIBLE_LEN
SERVER_ANSWER__KEYWORD_ACCEPTED = b'OK'


# DEFAULT_LIMIT = 2 ** 24  # 64 KiB
# DEFAULT_LIMIT = CpuInfo().l2_cache_size_per_virtual_core
# DEFAULT_LIMIT = CpuInfo().l3_cache_size
DEFAULT_LIMIT = 10 * 1024**2


class MessageProtocolSettings:
    def __init__(self, protocol_greeting: Optional[str], message_size_len: Optional[int], max_message_size_len: Optional[int]) -> None:
        self.protocol_greeting = protocol_greeting or DEFAULT_PROTOCOL_GREETING
        self.max_message_size_len = max_message_size_len or MESSAGE_SIZE_MAX_POSSIBLE_LEN
        self.message_size_len = message_size_len or MESSAGE_SIZE_LEN
