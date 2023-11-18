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
__version__ = "3.4.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from enum import Enum
from cengal.introspection.inspect import pdi


class Fields(Enum):
    command_name = 0  # See Commands class. Optional: if ommited then: 1) if `in_response_to` present then default is `send_response`; 2) if `in_response_to` is not present then default is `send_request`
    request_id = 1  # id of either request or response (requests and responses must have an independent counters)
    in_response_to = 2  # current response is a response to request with this ID. Optional: can be present only in `send_response`
    is_response_required = 3  # int. 1 = required; 0 = not required. Optional: if ommited then default is 0 (not required). This gives us ability to send smallest response-less request as possible. Even is not required, response still can be send. If required - response must be send.
    data = 4  # Data. Format depends on request type (command type). Optional: if ommited then default is None.


pdi(int(Fields.in_response_to.value))
