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

import enum
import gc
from functools import lru_cache
from typing import Set, Union, Optional, Any, Dict, Tuple
from cengal.modules_management.alternative_import import alt_import
from cengal.time_management.repeat_for_a_time import Tracer


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


class Tags(enum.Enum):
    tested = 0
    deep = 1  # can work with nested data structures
    superficial = 2  # can work with only single-layer of data
    multi_platform = 3  # serialized data can be deserialized by other languages/interpreters
    current_platform = 4  # serialized data can be deserialized by current type of python interpreter (only by CPython or only by PyPy for example)
    multicast = 5  # ?
    unique = 6  # ?
    can_use_set = 7  # can serialize set type
    can_use_bytes = 8  # can serialize bytes type
    can_use_custom_types = 9  # can serialize custom types
    can_use_lambda_functions = 10
    decode_str_as_str = 11  # does not convert strings to bytes
    decode_bytes_as_bytes = 12  # does not convert bytes to strings
    decode_str_and_bytes_as_requested = 13  # can chose: convert all str/bytes to str or to convert all str/bytes to bytes.
    decode_list_and_tuple_as_requested = 14  # can chose: convert all list/tuple to list or to convert all list/tuple to tuple.
    decode_tuple_as_tuple = 15  # does not conver tuples to list/set
    decode_list_as_list = 16  # does not convert lists to tuple/set
    explicit_format_version = 17  # Example: pickle can be of a different versions since python-version depent so it is Not tagged as an explicit_format_version.
    fast = 17
    compat = 18
    compat_with_python_below_3_8 = 19
    compat_with_python_abowe_3_8 = 20
    decode_set_as_set = 21  # does not convert sets to tuple/list


class DataFormats(enum.Enum):
    any = 0  # we don't care about the serialized data format
    json = 1  # serialized data is json
    binary = 2  # serialized data is binary (not really human-readable)
    text = 3  # serialized data is human-readable
    yaml = 4
    toml = 5
    messagepack = 6


SerializerFeatures = Set[Union[Tags, DataFormats]]


# !!! Keep an order! Add new serializers to the end of the list only !!!
class Serializers(enum.Enum):
    json = 0
    simplejson = 1
    ujson = 2
    orjson = 3
    tnetstring = 4
    pynetstring = 5
    msgpack_fast = 6
    msgpack = 7
    cbor = 8
    cbor2 = 9
    marshal = 10
    marshal_compat_4 = 11
    marshal_compat_3 = 12
    marshal_compat_2 = 13
    marshal_compat_1 = 14
    marshal_compat_0 = 15
    pickle = 16
    pickle_default = 17
    pickle_compat_5 = 18
    pickle_compat_4 = 19
    pickle_compat_3 = 20
    pickle_compat_2 = 21
    pickle_compat_1 = 22
    cpickle = 23
    cpickle_default = 24
    cpickle_compat_5 = 25
    cpickle_compat_4 = 26
    cpickle_compat_3 = 27
    cpickle_compat_2 = 28
    cpickle_compat_1 = 29
    cloudpickle = 30
    cloudpickle_compat_5 = 31
    cloudpickle_compat_4 = 32
    cloudpickle_compat_3 = 33
    cloudpickle_compat_2 = 34
    cloudpickle_compat_1 = 35
    msgspec_json = 36
    msgspec_messagepack = 37
    msgspec_yaml = 38
    msgspec_toml = 39


SERIALIZERS_DESCRIPTION = {
    Serializers.json: ('json', {
        Tags.deep,
        Tags.tested,
        Tags.superficial,
        Tags.multi_platform,
        Tags.current_platform,
        Tags.decode_str_as_str,
        Tags.decode_list_as_list,
        Tags.explicit_format_version,
        DataFormats.any,
        DataFormats.json,
        DataFormats.text,
    }),
    Serializers.simplejson: ('simplejson', {
        Tags.deep,
        Tags.tested,
        Tags.superficial,
        Tags.multi_platform,
        Tags.current_platform,
        Tags.can_use_bytes,
        Tags.decode_str_as_str,
        Tags.decode_list_as_list,
        Tags.explicit_format_version,
        DataFormats.any,
        DataFormats.json,
        DataFormats.text,
    }),
    Serializers.ujson: ('ujson', {
        Tags.deep,
        Tags.superficial,
        Tags.multi_platform,
        Tags.current_platform,
        Tags.can_use_bytes,
        Tags.decode_str_as_str,
        Tags.decode_list_as_list,
        Tags.explicit_format_version,
        DataFormats.any,
        DataFormats.json,
        DataFormats.text,
    }),
    Serializers.orjson: ('orjson', {
        Tags.deep,
        Tags.superficial,
        Tags.multi_platform,
        Tags.current_platform,
        Tags.can_use_bytes,
        Tags.decode_str_as_str,
        Tags.decode_list_as_list,
        Tags.explicit_format_version,
        DataFormats.any,
        DataFormats.json,
        DataFormats.text,
    }),
    Serializers.tnetstring: ('tnetstring', {
        Tags.superficial,
        Tags.current_platform,
        Tags.decode_str_as_str,
        Tags.explicit_format_version,
        DataFormats.any,
        DataFormats.text,
    }),
    Serializers.pynetstring: ('pynetstring', {
        Tags.superficial,
        Tags.multi_platform,
        Tags.current_platform,
        Tags.decode_str_as_str,
        Tags.explicit_format_version,
        DataFormats.any,
        DataFormats.text,
    }),
    Serializers.msgpack: ('msgpack', {
        Tags.tested,
        Tags.deep,
        Tags.superficial,
        Tags.multi_platform,
        Tags.current_platform,
        Tags.can_use_bytes,
        Tags.decode_str_as_str,
        Tags.decode_bytes_as_bytes,
        Tags.decode_str_and_bytes_as_requested,
        Tags.decode_list_and_tuple_as_requested,
        Tags.decode_list_as_list,
        Tags.explicit_format_version,
        DataFormats.any,
        DataFormats.binary,
        DataFormats.messagepack,
    }),
    Serializers.msgpack_fast: ('msgpack_fast', {
        Tags.tested,
        Tags.deep,
        Tags.superficial,
        Tags.multi_platform,
        Tags.current_platform,
        Tags.can_use_bytes,
        Tags.decode_str_as_str,
        Tags.decode_bytes_as_bytes,
        Tags.decode_str_and_bytes_as_requested,
        Tags.decode_list_and_tuple_as_requested,
        Tags.decode_tuple_as_tuple,
        Tags.explicit_format_version,
        DataFormats.any,
        DataFormats.binary,
        DataFormats.messagepack,
    }),
    Serializers.cbor: ('cbor', {
        Tags.tested,
        Tags.deep,
        Tags.superficial,
        Tags.multi_platform,
        Tags.current_platform,
        Tags.can_use_bytes,
        Tags.decode_str_as_str,
        Tags.decode_bytes_as_bytes,
        Tags.decode_list_as_list,
        Tags.explicit_format_version,
        DataFormats.any,
        DataFormats.binary,
    }),
    Serializers.cbor2: ('cbor2', {
        Tags.tested,
        Tags.deep,
        Tags.superficial,
        Tags.multi_platform,
        Tags.current_platform,
        Tags.can_use_bytes,
        Tags.decode_str_as_str,
        Tags.decode_bytes_as_bytes,
        Tags.decode_list_as_list,
        Tags.explicit_format_version,
        DataFormats.any,
        DataFormats.binary,
    }),
    Serializers.marshal: ('marshal', {
        Tags.tested,
        Tags.deep,
        Tags.superficial,
        Tags.current_platform,
        Tags.can_use_bytes,
        Tags.decode_str_as_str,
        Tags.decode_bytes_as_bytes,
        Tags.can_use_set,
        Tags.decode_tuple_as_tuple,
        Tags.decode_list_as_list,
        Tags.explicit_format_version,
        DataFormats.any,
        DataFormats.binary,
    }),
    Serializers.pickle: ('pickle', {
        Tags.tested,
        Tags.deep,
        Tags.superficial,
        Tags.current_platform,
        Tags.can_use_bytes,
        Tags.can_use_set,
        Tags.can_use_custom_types,
        Tags.decode_str_as_str,
        Tags.decode_bytes_as_bytes,
        Tags.decode_tuple_as_tuple,
        Tags.decode_list_as_list,
        DataFormats.any,
        DataFormats.binary,
    }),
    Serializers.cpickle: ('cPickle', {
        Tags.deep,
        Tags.superficial,
        Tags.current_platform,
        Tags.can_use_bytes,
        Tags.can_use_set,
        Tags.can_use_custom_types,
        Tags.decode_str_as_str,
        Tags.decode_bytes_as_bytes,
        Tags.decode_tuple_as_tuple,
        Tags.decode_list_as_list,
        DataFormats.any,
        DataFormats.binary,
    }),
    Serializers.cloudpickle: ('cloudpickle', {
        Tags.deep,
        Tags.superficial,
        Tags.current_platform,
        Tags.can_use_bytes,
        Tags.can_use_set,
        Tags.can_use_custom_types,
        Tags.can_use_lambda_functions,
        Tags.decode_str_as_str,
        Tags.decode_bytes_as_bytes,
        Tags.decode_tuple_as_tuple,
        Tags.decode_list_as_list,
        DataFormats.any,
        DataFormats.binary,
    }),
    Serializers.msgspec_messagepack: ('msgspec_messagepack', {
        Tags.tested,
        Tags.deep,
        Tags.superficial,
        Tags.multi_platform,
        Tags.current_platform,
        Tags.can_use_set,
        Tags.can_use_bytes,
        Tags.decode_str_as_str,
        Tags.decode_bytes_as_bytes,
        Tags.decode_list_as_list,
        Tags.explicit_format_version,
        DataFormats.any,
        DataFormats.binary,
        DataFormats.messagepack,
    }),
    Serializers.msgspec_json: ('msgspec_json', {
        Tags.tested,
        Tags.deep,
        Tags.superficial,
        Tags.multi_platform,
        Tags.current_platform,
        Tags.can_use_set,
        Tags.decode_str_as_str,
        Tags.decode_list_as_list,
        Tags.explicit_format_version,
        DataFormats.any,
        DataFormats.json,
        DataFormats.text,
    }),
    Serializers.msgspec_yaml: ('msgspec_yaml', {
        Tags.tested,
        Tags.deep,
        Tags.superficial,
        Tags.multi_platform,
        Tags.current_platform,
        Tags.can_use_set,
        Tags.decode_str_as_str,
        Tags.decode_list_as_list,
        Tags.explicit_format_version,
        DataFormats.any,
        DataFormats.yaml,
        DataFormats.text,
    }),
    Serializers.msgspec_toml: ('msgspec_toml', {
        Tags.tested,
        Tags.deep,
        Tags.superficial,
        Tags.multi_platform,
        Tags.current_platform,
        Tags.can_use_set,
        Tags.decode_str_as_str,
        Tags.decode_list_as_list,
        Tags.explicit_format_version,
        DataFormats.any,
        DataFormats.toml,
        DataFormats.text,
    }),
}


ujson_dump_skip_parameters = {'skipkeys', 'check_circular', 'allow_nan', 'cls', 'separators', 'default'}
ujson_dumps_skip_parameters = {'skipkeys', 'check_circular', 'allow_nan', 'cls', 'separators', 'default'}
ujson_load_skip_parameters = {'cls', 'object_hook', 'parse_float', 'parse_int', 'parse_constant', 'object_pairs_hook'}
ujson_loads_skip_parameters = {'cls', 'object_hook', 'parse_float', 'parse_int', 'parse_constant', 'object_pairs_hook'}


orjson_dump_skip_parameters = {'skipkeys', 'check_circular', 'allow_nan', 'cls', 'separators', 'default'}
orjson_dumps_skip_parameters = {'skipkeys', 'check_circular', 'allow_nan', 'cls', 'separators', 'default'}
orjson_load_skip_parameters = {'cls', 'object_hook', 'parse_float', 'parse_int', 'parse_constant', 'object_pairs_hook'}
orjson_loads_skip_parameters = {'cls', 'object_hook', 'parse_float', 'parse_int', 'parse_constant', 'object_pairs_hook'}


EXISTING_SERIALIZERS = set()  # type: Set[Serializers]
with alt_import('json') as json:
    if json is not None:
        EXISTING_SERIALIZERS.add(Serializers.json)
with alt_import('simplejson') as simplejson:
    if simplejson is not None:
        EXISTING_SERIALIZERS.add(Serializers.simplejson)
with alt_import('ujson') as ujson:
    if ujson is not None:
        EXISTING_SERIALIZERS.add(Serializers.ujson)
with alt_import('orjson') as orjson:
    if orjson is not None:
        EXISTING_SERIALIZERS.add(Serializers.orjson)
with alt_import('tnetstring') as tnetstring:
    if tnetstring is not None:
        EXISTING_SERIALIZERS.add(Serializers.tnetstring)
# with alt_import('pynetstring') as pynetstring:
#     if pynetstring is not None:
#         EXISTING_SERIALIZERS.add(Serializers.pynetstring)
with alt_import('msgpack') as msgpack:
    if msgpack is not None:
        EXISTING_SERIALIZERS.add(Serializers.msgpack_fast)
        EXISTING_SERIALIZERS.add(Serializers.msgpack)
with alt_import('msgspec') as msgspec:
    if msgspec is not None:
        EXISTING_SERIALIZERS.add(Serializers.msgspec_messagepack)
        EXISTING_SERIALIZERS.add(Serializers.msgspec_json)
        EXISTING_SERIALIZERS.add(Serializers.msgspec_yaml)
        EXISTING_SERIALIZERS.add(Serializers.msgspec_toml)
with alt_import('cbor') as cbor:
    if cbor is not None:
        EXISTING_SERIALIZERS.add(Serializers.cbor)
with alt_import('cbor2') as cbor2:
    if cbor2 is not None:
        EXISTING_SERIALIZERS.add(Serializers.cbor2)
with alt_import('marshal') as marshal:
    if marshal is not None:
        EXISTING_SERIALIZERS.add(Serializers.marshal)
with alt_import('pickle') as pickle:
    if pickle is not None:
        EXISTING_SERIALIZERS.add(Serializers.pickle)
with alt_import('cPickle') as cPickle:
    if cPickle is not None:
        EXISTING_SERIALIZERS.add(Serializers.cpickle)
with alt_import('cloudpickle') as cloudpickle:
    if cloudpickle is not None:
        EXISTING_SERIALIZERS.add(Serializers.cloudpickle)


class Serializer:
    def __init__(self, serializer: Union[None, Serializers]):
        self.dump = None
        self.dumps = None
        self.load = None
        self.loads = None
        self._serializer = None
        self.serializer = serializer

    @property
    def serializer(self):
        return self._serializer

    @serializer.setter
    def serializer(self, serializer: Serializers):
        self._serializer = serializer
        if self._serializer is None:
            self.dump = None
            self.dumps = None
            self.load = None
            self.loads = None
        else:
            serializer_name, serializer_tags = SERIALIZERS_DESCRIPTION[self._serializer]
            self.dump = getattr(self, '_{}__dump'.format(serializer_name))
            self.dumps = getattr(self, '_{}__dumps'.format(serializer_name))
            self.load = getattr(self, '_{}__load'.format(serializer_name))
            self.loads = getattr(self, '_{}__loads'.format(serializer_name))

    # json
    @staticmethod
    def _json__dump(*args, **kwargs):
        json.dump(*args, **kwargs)

    @staticmethod
    def _json__dumps(*args, **kwargs):
        return json.dumps(*args, **kwargs)

    @staticmethod
    def _json__load(*args, **kwargs):
        return json.load(*args, **kwargs)

    @staticmethod
    def _json__loads(*args, **kwargs):
        return json.loads(*args, **kwargs)

    # simplejson
    @staticmethod
    def _simplejson__dump(*args, **kwargs):
        simplejson.dump(*args, **kwargs)

    @staticmethod
    def _simplejson__dumps(*args, **kwargs):
        return simplejson.dumps(*args, **kwargs)

    @staticmethod
    def _simplejson__load(*args, **kwargs):
        return simplejson.load(*args, **kwargs)

    @staticmethod
    def _simplejson__loads(*args, **kwargs):
        return simplejson.loads(*args, **kwargs)

    # ujson
    @staticmethod
    def _ujson__dump(*args, **kwargs):
        for unnecessary_parameter in ujson_dump_skip_parameters:
            kwargs.pop(unnecessary_parameter, None)
        ujson.dump(*args, **kwargs)

    @staticmethod
    def _ujson__dumps(*args, **kwargs):
        for unnecessary_parameter in ujson_dumps_skip_parameters:
            kwargs.pop(unnecessary_parameter, None)
        return ujson.dumps(*args, **kwargs)

    @staticmethod
    def _ujson__load(*args, **kwargs):
        for unnecessary_parameter in ujson_load_skip_parameters:
            kwargs.pop(unnecessary_parameter, None)
        return ujson.load(*args, **kwargs)

    @staticmethod
    def _ujson__loads(*args, **kwargs):
        for unnecessary_parameter in ujson_loads_skip_parameters:
            kwargs.pop(unnecessary_parameter, None)
        return ujson.loads(*args, **kwargs)

    # orjson
    @staticmethod
    def _orjson__dump(*args, **kwargs):
        for unnecessary_parameter in orjson_dump_skip_parameters:
            kwargs.pop(unnecessary_parameter, None)
        kwargs['option'] = orjson.OPT_NON_STR_KEYS
        orjson.dump(*args, **kwargs)

    @staticmethod
    def _orjson__dumps(*args, **kwargs):
        for unnecessary_parameter in orjson_dumps_skip_parameters:
            kwargs.pop(unnecessary_parameter, None)
        kwargs['option'] = orjson.OPT_NON_STR_KEYS
        return orjson.dumps(*args, **kwargs).decode('utf-8')

    @staticmethod
    def _orjson__load(*args, **kwargs):
        for unnecessary_parameter in orjson_load_skip_parameters:
            kwargs.pop(unnecessary_parameter, None)
        return orjson.load(*args, **kwargs)

    @staticmethod
    def _orjson__loads(*args, **kwargs):
        for unnecessary_parameter in orjson_loads_skip_parameters:
            kwargs.pop(unnecessary_parameter, None)
        return orjson.loads(*args, **kwargs)

    # tnetstring
    @staticmethod
    def _tnetstring__dump(*args, **kwargs):
        tnetstring.dump(*args, **kwargs)

    @staticmethod
    def _tnetstring__dumps(*args, **kwargs):
        return tnetstring.dumps(*args, **kwargs)

    @staticmethod
    def _tnetstring__load(*args, **kwargs):
        return tnetstring.load(*args, **kwargs)

    @staticmethod
    def _tnetstring__loads(*args, **kwargs):
        return tnetstring.loads(*args, **kwargs)

    # msgpack
    @staticmethod
    def _msgpack__dump(*args, **kwargs):
        result_kwargs = {
            # 'encoding': 'utf-8',  # PendingDeprecationWarning: encoding is deprecated.
            'use_bin_type': True
        }
        result_kwargs.update(kwargs)
        msgpack.dump(*args, **result_kwargs)

    @staticmethod
    def _msgpack__dumps(*args, **kwargs):
        result_kwargs = {
            # 'encoding': 'utf-8',  # PendingDeprecationWarning: encoding is deprecated.
            'use_bin_type': True
        }
        result_kwargs.update(kwargs)
        return msgpack.dumps(*args, **result_kwargs)

    @staticmethod
    def _msgpack__load(*args, **kwargs):
        result_kwargs = {
            # 'encoding': 'utf-8',  # PendingDeprecationWarning: encoding is deprecated, Use raw=False instead.
            'raw': False,
            'use_list': True
        }
        result_kwargs.update(kwargs)
        gc.disable()
        result = msgpack.load(*args, **result_kwargs)
        gc.enable()
        return result

    @staticmethod
    def _msgpack__loads(*args, **kwargs):
        result_kwargs = {
            # 'encoding': 'utf-8',  # PendingDeprecationWarning: encoding is deprecated, Use raw=False instead.
            'raw': False,
            'use_list': True
        }
        result_kwargs.update(kwargs)
        gc.disable()
        result = msgpack.loads(*args, **result_kwargs)
        gc.enable()
        return result

    # msgpack_fast
    @staticmethod
    def _msgpack_fast__dump(*args, **kwargs):
        result_kwargs = {
            'encoding': 'utf-8',
            'use_bin_type': True
        }
        result_kwargs.update(kwargs)
        msgpack.dump(*args, **result_kwargs)

    @staticmethod
    def _msgpack_fast__dumps(*args, **kwargs):
        result_kwargs = {
            'encoding': 'utf-8',
            'use_bin_type': True
        }
        result_kwargs.update(kwargs)
        return msgpack.dumps(*args, **result_kwargs)

    @staticmethod
    def _msgpack_fast__load(*args, **kwargs):
        result_kwargs = {
            'encoding': 'utf-8',
            'raw': False,
            'use_list': False
        }
        result_kwargs.update(kwargs)
        gc.disable()
        result = msgpack.load(*args, **result_kwargs)
        gc.enable()
        return result

    @staticmethod
    def _msgpack_fast__loads(*args, **kwargs):
        result_kwargs = {
            'encoding': 'utf-8',
            'raw': False,
            'use_list': False
        }
        result_kwargs.update(kwargs)
        gc.disable()
        result = msgpack.loads(*args, **result_kwargs)
        gc.enable()
        return result

    # msgspec_messagepack
    @staticmethod
    def _msgspec_messagepack__dump(obj, fp, *args, **kwargs):
        fp.write(msgspec.msgpack.encode(obj, *args, **kwargs))

    @staticmethod
    def _msgspec_messagepack__dumps(*args, **kwargs):
        return msgspec.msgpack.encode(*args, **kwargs)

    @staticmethod
    def _msgspec_messagepack__load(fp, *args, **kwargs):
        gc.disable()
        result = msgspec.msgpack.decode(fp.read(), *args, **kwargs)
        gc.enable()
        return result

    @staticmethod
    def _msgspec_messagepack__loads(*args, **kwargs):
        gc.disable()
        result = msgspec.msgpack.decode(*args, **kwargs)
        gc.enable()
        return result

    # msgspec_json
    @staticmethod
    def _msgspec_json__dump(obj, fp, *args, **kwargs):
        fp.write(msgspec.json.encode(obj, *args, **kwargs))

    @staticmethod
    def _msgspec_json__dumps(*args, **kwargs):
        return msgspec.json.encode(*args, **kwargs)

    @staticmethod
    def _msgspec_json__load(fp, *args, **kwargs):
        gc.disable()
        result = msgspec.json.decode(fp.read(), *args, **kwargs)
        gc.enable()
        return result

    @staticmethod
    def _msgspec_json__loads(*args, **kwargs):
        gc.disable()
        result = msgspec.json.decode(*args, **kwargs)
        gc.enable()
        return result

    # msgspec_yaml
    @staticmethod
    def _msgspec_yaml__dump(obj, fp, *args, **kwargs):
        fp.write(msgspec.yaml.encode(obj, *args, **kwargs))

    @staticmethod
    def _msgspec_yaml__dumps(*args, **kwargs):
        return msgspec.yaml.encode(*args, **kwargs)

    @staticmethod
    def _msgspec_yaml__load(fp, *args, **kwargs):
        gc.disable()
        result = msgspec.yaml.decode(fp.read(), *args, **kwargs)
        gc.enable()
        return result

    @staticmethod
    def _msgspec_yaml__loads(*args, **kwargs):
        gc.disable()
        result = msgspec.yaml.decode(*args, **kwargs)
        gc.enable()
        return result

    # msgspec_toml
    @staticmethod
    def _msgspec_toml__dump(obj, fp, *args, **kwargs):
        fp.write(msgspec.toml.encode(obj, *args, **kwargs))

    @staticmethod
    def _msgspec_toml__dumps(*args, **kwargs):
        return msgspec.toml.encode(*args, **kwargs)

    @staticmethod
    def _msgspec_toml__load(fp, *args, **kwargs):
        gc.disable()
        result = msgspec.toml.decode(fp.read(), *args, **kwargs)
        gc.enable()
        return result

    @staticmethod
    def _msgspec_toml__loads(*args, **kwargs):
        gc.disable()
        result = msgspec.toml.decode(*args, **kwargs)
        gc.enable()
        return result

    # cbor
    @staticmethod
    def _cbor__dump(*args, **kwargs):
        cbor.dump(*args, **kwargs)

    @staticmethod
    def _cbor__dumps(*args, **kwargs):
        return cbor.dumps(*args, **kwargs)

    @staticmethod
    def _cbor__load(*args, **kwargs):
        cbor.load(*args, **kwargs)

    @staticmethod
    def _cbor__loads(*args, **kwargs):
        return cbor.loads(*args, **kwargs)

    # cbor2
    @staticmethod
    def _cbor2__dump(*args, **kwargs):
        cbor2.dump(*args, **kwargs)

    @staticmethod
    def _cbor2__dumps(*args, **kwargs):
        return cbor2.dumps(*args, **kwargs)

    @staticmethod
    def _cbor2__load(*args, **kwargs):
        cbor2.load(*args, **kwargs)

    @staticmethod
    def _cbor2__loads(*args, **kwargs):
        return cbor2.loads(*args, **kwargs)

    # marshal
    @staticmethod
    def _marshal__dump(*args, **kwargs):
        if len(args) == 2:
            result_args = args
        else:
            result_args = (args[0], args[1], 4)
        marshal.dump(*result_args, **kwargs)

    @staticmethod
    def _marshal__dumps(*args, **kwargs):
        if len(args) == 1:
            result_args = args
        else:
            result_args = (args[0], 4)
        return marshal.dumps(*result_args, **kwargs)

    @staticmethod
    def _marshal__load(*args, **kwargs):
        return marshal.load(*args, **kwargs)

    @staticmethod
    def _marshal__loads(*args, **kwargs):
        return marshal.loads(*args, **kwargs)

    # pickle
    @staticmethod
    def _pickle__dump(*args, **kwargs):
        result_kwargs = {'protocol': -1}
        result_kwargs.update(kwargs)
        pickle.dump(*args, **result_kwargs)

    @staticmethod
    def _pickle__dumps(*args, **kwargs):
        result_kwargs = {'protocol': -1}
        result_kwargs.update(kwargs)
        return pickle.dumps(*args, **result_kwargs)

    @staticmethod
    def _pickle__load(*args, **kwargs):
        return pickle.load(*args, **kwargs)

    @staticmethod
    def _pickle__loads(*args, **kwargs):
        return pickle.loads(*args, **kwargs)

    # cPickle
    @staticmethod
    def _cpickle__dump(*args, **kwargs):
        result_kwargs = {'protocol': -1}
        result_kwargs.update(kwargs)
        cPickle.dump(*args, **result_kwargs)

    @staticmethod
    def _cpickle__dumps(*args, **kwargs):
        result_kwargs = {'protocol': -1}
        result_kwargs.update(kwargs)
        return cPickle.dumps(*args, **result_kwargs)

    @staticmethod
    def _cpickle__load(*args, **kwargs):
        return cPickle.load(*args, **kwargs)

    @staticmethod
    def _cpickle__loads(*args, **kwargs):
        return cPickle.loads(*args, **kwargs)

    # cloudpickle
    @staticmethod
    def _cloudpickle__dump(*args, **kwargs):
        result_kwargs = {'protocol': -1}
        result_kwargs.update(kwargs)
        cPickle.dump(*args, **result_kwargs)

    @staticmethod
    def _cloudpickle__dumps(*args, **kwargs):
        result_kwargs = {'protocol': -1}
        result_kwargs.update(kwargs)
        return cPickle.dumps(*args, **result_kwargs)

    @staticmethod
    def _cloudpickle__load(*args, **kwargs):
        return cPickle.load(*args, **kwargs)

    @staticmethod
    def _cloudpickle__loads(*args, **kwargs):
        return cPickle.loads(*args, **kwargs)


def get_an_appropriate_serializers(desired_features: SerializerFeatures) -> Set[Serializers]:
    appropriate_serializers = set()
    for serializer_type in EXISTING_SERIALIZERS:
        serializer_features = SERIALIZERS_DESCRIPTION[serializer_type][1]
        if desired_features.issubset(serializer_features):
            appropriate_serializers.add(serializer_type)
    return appropriate_serializers


SerializerPerformance = float
SerializerFootprint = int


def serializer_benchmark(serializer_type: Serializers, test_data: Optional[Any], test_time: float = 1.0
                         ) -> Tuple[SerializerPerformance, SerializerFootprint]:
    serializer = Serializer(serializer_type)
    tr = Tracer(test_time)
    while tr.iter():
        serializer.loads(serializer.dumps(test_data))
    data_dump = serializer.dumps(test_data)
    return tr.iter_per_time_unit, len(data_dump)


def get_most_efficient_serializers(desired_features: SerializerFeatures,
                                   test_data: Optional[Any],
                                   test_time: float = 1.0
                                   ) -> Tuple[Set[Serializers],
                                              Set[Tuple[Serializers, SerializerPerformance, SerializerFootprint]]]:
    # TODO: сделать класс, который бы подбирал количество итераций под нужное время выдержки в секундах (float)
    # это необходимо для того чтобы правильно протестировать производительность под PyPy
    # в дальнейшем этот функционал стоит перенести в модуль performance_test_lib
    # TODO: make some caching algorithm. Lru can not be used since it requires all function parameters be hashable and both desired_features and test_data are not

    appropriate_serializers = get_an_appropriate_serializers(desired_features)

    benchmark_results = dict()  # type: Dict[float, Set[Serializers]]
    serializers_data = set()  # type: Set[Tuple[Serializers, SerializerPerformance, SerializerFootprint]]
    for serializer_type in appropriate_serializers:
        gc.disable()
        performance, dump_size = serializer_benchmark(serializer_type, test_data, test_time)
        gc.enable()
        if performance not in benchmark_results:
            benchmark_results[performance] = set()
        benchmark_results[performance].add(serializer_type)
        serializers_data.add((serializer_type, performance, dump_size))
    best_performance = max(benchmark_results)
    best_serializers = benchmark_results[best_performance]
    return best_serializers, serializers_data


def best_serializer(desired_features: SerializerFeatures,
                                   test_data: Optional[Any],
                                   test_time: float = 1.0
                                   ) -> Serializer:
    result = get_most_efficient_serializers(
        desired_features,
        test_data,
        test_time)
    best_serializers, _ = result
    return Serializer(best_serializers.pop())


class TestDataType(enum.Enum):
    small = 0
    deep_small = 1
    large = 2
    deep_large = 3


def test_data_factory(test_data_type: TestDataType):
    if TestDataType.small == test_data_type:
        return {
            1: 'Hello',
            2: ('W', 0),
            3: [
                'r',
                1,
                {
                    'd': '.',
                    'd'*2: {
                        43: [0]*2,
                        15: {
                            'world': 42
                        }
                    }
                }
            ]*15,
            'To all!': '!!1'
        }
    elif TestDataType.deep_small == test_data_type:
        return {
            1: 'Hello',
            2: ('W', 0),
            3: [
                'r',
                1,
                {
                    'd': '.',
                    'd'*2: {
                        43: [0]*1000,
                        15: {
                            'world': 42
                        }
                    }
                }
            ]*20,
            'To all!': '!!1'
        }
    elif TestDataType.large == test_data_type:
        return {
            1: 'Hello'*100,
            2: ('W', 0),
            3: [
                'r',
                1,
                {
                    'd': '.',
                    'd'*100: {
                        43: [0]*2,
                        15: {
                            'world'*100: 42
                        }
                    }
                }
            ]*2,
            'To all!': '!!1'*100
        }
    elif TestDataType.deep_large == test_data_type:
        return {
            1: 'Hello'*100,
            2: ('W', 0),
            3: [
                'r',
                1,
                {
                    'd': '.',
                    'd'*100: {
                        43: [0]*1000,
                        15: {
                            'world'*100: 42
                        }
                    }
                }
            ]*20,
            'To all!': '!!1'*100
        }
