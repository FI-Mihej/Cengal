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


from enum import Enum


class Fields(Enum):
    command_name = 0  # See Commands class. Optional: if ommited then: 1) if `in_response_to` present then default is `send_response`; 2) if `in_response_to` is not present then default is `send_request`
    request_id = 1  # id of either request or response (requests and responses must have an independent counters)
    in_response_to = 2  # current response is a response to request with this ID. Optional: can be present only in `send_response`
    is_response_required = 3  # int. 1 = required; 0 = not required. Optional: if ommited then default is 0 (not required). This gives us ability to send smallest response-less request as possible. Even is not required, response still can be send. If required - response must be send.
    data_serializer_id = 4  # If data was serialized explicitly with some serializer (Pickle for example). Optional.
    data = 5  # Data. Format depends on request type (command type). Optional: if ommited then default is None.


class Commands(Enum):
    # suggest_best_serializers_list = 0  # client suggests list of it's best serializers (first is fastest)
    # declare_best_serializers_list = 1  # server respondes with a sublist of apropriate sugested serializers (first is fastest)
    declare_client_node = 0
    declare_server_node = 1
    declare_service_class = 2  # client sends service class name, it's unique ID (int starting from 0, generated on the client side), it's module importable str (path) and it's module full file path
    declare_service_request_class = 3  # client sends service ID, service request class name and it's unique ID (int starting from 0, generated on the client side)
    send_request = 4  # raw request
    send_service_request = 5
    send_service_request_with_request_class = 6
    send_response = 6


# === Commands ====================
class CommandDataFieldsDeclareClientNode(Enum):
    platform_name = 0
    suggested_serializers = 1


class CommandDataFieldsDeclareServerNode(Enum):
    platform_name = 0
    declared_serializers = 1


class CommandDataFieldsDeclareServiceClass(Enum):
    local_id = 0
    class_name = 1
    module_importable_str = 2


class CommandDataFieldsDeclareServiceRequestClass(Enum):
    local_id = 0
    class_name = 1
    module_importable_str = 2
    properties_tuple = 3


class CommandDataFieldsRequest:
    args = 0
    kwargs = 1


class CommandDataFieldsServiceRequest:
    service_class_id = 0
    args = 1
    kwargs = 2


class CommandDataFieldsServiceRequestWithRequestClass:
    service_class_id = 0
    request_class_id = 1
    properties_tuple = 3
