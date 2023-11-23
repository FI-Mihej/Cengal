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


from cengal.data_manipulation.serialization import Serializer, Serializers, SerializerFeatures, DataFormats, Tags, best_serializer
from enum import Enum
from typing import Dict, Any

from .commands import *


class SerializerID(Enum):
    multi_platform__initial_communication = -1
    multi_platform_fast = 0
    multi_platform = 1
    current_platform = 2
    current_platform__custom_types = 3


desired_features: Dict[SerializerID, SerializerFeatures] = {
    SerializerID.multi_platform__initial_communication.value: {
        DataFormats.json,
        Tags.deep,
        Tags.multi_platform,
    },
    SerializerID.multi_platform_fast.value: {
        DataFormats.any,
        Tags.deep,
        Tags.multi_platform,
        Tags.can_use_bytes,
    },
    SerializerID.multi_platform.value: {
        DataFormats.any,
        Tags.deep,
        Tags.multi_platform,
        Tags.can_use_bytes,
        Tags.decode_str_as_str,
        Tags.decode_list_as_list,
    },
    SerializerID.current_platform.value: {
        DataFormats.any,
        Tags.deep,
        Tags.can_use_set,
        Tags.can_use_bytes,
        Tags.decode_str_as_str,
        Tags.decode_bytes_as_bytes,
        Tags.decode_tuple_as_tuple,
        Tags.decode_list_as_list,
    },
    SerializerID.current_platform__custom_types.value: {
        DataFormats.any,
        Tags.current_platform,
        Tags.deep,
        Tags.can_use_custom_types,
        Tags.can_use_bytes,
        Tags.can_use_set,
        Tags.decode_str_as_str,
        Tags.decode_bytes_as_bytes,
        Tags.decode_tuple_as_tuple,
        Tags.decode_list_as_list,
    },
}


test_data: Dict[SerializerID, Any] = {
    SerializerID.multi_platform__initial_communication.value: {
        Fields.command_name.value: Commands.declare_client_node.value,
        Fields.request_id.value: 10,
        Fields.in_response_to.value: 10,
        Fields.is_response_required.value: True,
        Fields.data.value: {
            CommandDataFieldsDeclareClientNode.platform_name.value: 'Python 3.11.0',
            CommandDataFieldsDeclareClientNode.suggested_serializers.value: {
                SerializerID.multi_platform_fast.value: [
                    Serializers.msgpack_fast,
                    Serializers.orjson,
                    Serializers.cbor2,
                    Serializers.ujson,
                    Serializers.simplejson,
                    Serializers.json,
                ],
                SerializerID.multi_platform.value: [
                    Serializers.msgpack,
                    Serializers.orjson,
                    Serializers.cbor2,
                    Serializers.ujson,
                    Serializers.simplejson,
                    Serializers.json,
                ],
                SerializerID.current_platform.value: [
                    Serializers.marshal_compat_4,
                    Serializers.msgpack,
                    Serializers.orjson,
                    Serializers.cbor2,
                    Serializers.ujson,
                    Serializers.simplejson,
                    Serializers.json,
                    Serializers.cloudpickle_compat_5,
                    Serializers.cpickle_compat_5,
                    Serializers.pickle_compat_5,
                ],
                SerializerID.current_platform__custom_types.value: [
                    Serializers.cloudpickle_compat_5,
                    Serializers.cpickle_compat_5,
                    Serializers.pickle_compat_5,
                ],
            }
        }
    },
    SerializerID.multi_platform_fast.value: {
        DataFormats.any,
        Tags.deep,
        Tags.multi_platform,
        Tags.can_use_bytes,
    },
    SerializerID.multi_platform.value: {
        DataFormats.any,
        Tags.deep,
        Tags.multi_platform,
        Tags.can_use_bytes,
        Tags.decode_str_as_str,
        Tags.decode_list_as_list,
    },
    SerializerID.current_platform.value: {
        DataFormats.any,
        Tags.deep,
        Tags.can_use_set,
        Tags.can_use_bytes,
        Tags.decode_str_as_str,
        Tags.decode_bytes_as_bytes,
        Tags.decode_tuple_as_tuple,
        Tags.decode_list_as_list,
    },
    SerializerID.current_platform__custom_types.value: {
        DataFormats.any,
        Tags.current_platform,
        Tags.deep,
        Tags.can_use_custom_types,
        Tags.can_use_bytes,
        Tags.can_use_set,
        Tags.decode_str_as_str,
        Tags.decode_bytes_as_bytes,
        Tags.decode_tuple_as_tuple,
        Tags.decode_list_as_list,
    },
}


def benchmark(test_data: Dict[SerializerID, Any]) -> Dict[SerializerID, Serializer]:
    ...
