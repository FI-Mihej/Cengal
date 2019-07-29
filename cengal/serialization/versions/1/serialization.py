#!/usr/bin/env python
# coding=utf-8

# Copyright © 2017 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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
from typing import Set, Union
from cengal.modules_management import alt_import


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2017 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "0.0.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
__status__ = "Prototype"
# __status__ = "Development"
# __status__ = "Production"


class Tags(enum.Enum):
    deep = 0
    superficial = 1
    multi_platform = 2
    current_platform = 3
    multicast = 4
    unique = 5


class DataFormats(enum.Enum):
    any = 0
    json = 1


class Serializers(enum.Enum):
    json = 0
    simplejson = 1
    ujson = 2
    tnetstring = 3
    msgpack = 4
    cbor = 5
    marshal = 6
    pickle = 7
    cpickle = 8


SERIALIZERS_DESCRIPTION = {
    Serializers.json: ('json', {Tags.superficial, Tags.multi_platform, Tags.current_platform, DataFormats.any,
                                DataFormats.json}),
    Serializers.simplejson: ('simplejson', {Tags.superficial, Tags.multi_platform, Tags.current_platform,
                                            DataFormats.any, DataFormats.json}),
    Serializers.ujson: ('ujson', {Tags.superficial, Tags.multi_platform, Tags.current_platform, DataFormats.any,
                                  DataFormats.json}),
    Serializers.tnetstring: ('tnetstring', {Tags.superficial, Tags.current_platform, DataFormats.any}),
    Serializers.msgpack: ('msgpack', {Tags.superficial, Tags.multi_platform, Tags.current_platform, DataFormats.any}),
    Serializers.cbor: ('cbor', {Tags.superficial, Tags.multi_platform, Tags.current_platform, DataFormats.any}),
    Serializers.marshal: ('marshal', {Tags.superficial, Tags.current_platform, DataFormats.any}),
    Serializers.pickle: ('pickle', {Tags.deep, Tags.superficial, Tags.current_platform, DataFormats.any}),
    Serializers.cpickle: ('cPickle', {Tags.deep, Tags.superficial, Tags.current_platform, DataFormats.any}),
}

EXISTING_SERIALIZERS = set()
with alt_import('json') as json:
    if json is not None:
        EXISTING_SERIALIZERS.add(Serializers.json)
with alt_import('simplejson') as simplejson:
    if simplejson is not None:
        EXISTING_SERIALIZERS.add(Serializers.simplejson)
with alt_import('ujson') as ujson:
    if ujson is not None:
        EXISTING_SERIALIZERS.add(Serializers.ujson)
with alt_import('tnetstring') as tnetstring:
    if tnetstring is not None:
        EXISTING_SERIALIZERS.add(Serializers.tnetstring)
with alt_import('msgpack') as msgpack:
    if msgpack is not None:
        EXISTING_SERIALIZERS.add(Serializers.msgpack)
with alt_import('cbor') as cbor:
    if cbor is not None:
        EXISTING_SERIALIZERS.add(Serializers.cbor)
with alt_import('marshal') as marshal:
    if marshal is not None:
        EXISTING_SERIALIZERS.add(Serializers.marshal)
with alt_import('pickle') as pickle:
    if pickle is not None:
        EXISTING_SERIALIZERS.add(Serializers.pickle)
with alt_import('cPickle') as cPickle:
    if cPickle is not None:
        EXISTING_SERIALIZERS.add(Serializers.cpickle)


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
        json.load(*args, **kwargs)

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
        simplejson.load(*args, **kwargs)

    @staticmethod
    def _simplejson__loads(*args, **kwargs):
        return simplejson.loads(*args, **kwargs)

    # ujson
    @staticmethod
    def _ujson__dump(*args, **kwargs):
        ujson.dump(*args, **kwargs)

    @staticmethod
    def _ujson__dumps(*args, **kwargs):
        return ujson.dumps(*args, **kwargs)

    @staticmethod
    def _ujson__load(*args, **kwargs):
        ujson.load(*args, **kwargs)

    @staticmethod
    def _ujson__loads(*args, **kwargs):
        return ujson.loads(*args, **kwargs)

    # tnetstring
    @staticmethod
    def _tnetstring__dump(*args, **kwargs):
        tnetstring.dump(*args, **kwargs)

    @staticmethod
    def _tnetstring__dumps(*args, **kwargs):
        return tnetstring.dumps(*args, **kwargs)

    @staticmethod
    def _tnetstring__load(*args, **kwargs):
        tnetstring.load(*args, **kwargs)

    @staticmethod
    def _tnetstring__loads(*args, **kwargs):
        return tnetstring.loads(*args, **kwargs)

    # msgpack
    @staticmethod
    def _msgpack__dump(*args, **kwargs):
        msgpack.dump(*args, **kwargs)

    @staticmethod
    def _msgpack__dumps(*args, **kwargs):
        return msgpack.dumps(*args, **kwargs)

    @staticmethod
    def _msgpack__load(*args, **kwargs):
        msgpack.load(*args, **kwargs)

    @staticmethod
    def _msgpack__loads(*args, **kwargs):
        return msgpack.loads(*args, **kwargs)

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

    # marshal
    @staticmethod
    def _marshal__dump(*args, **kwargs):
        marshal.dump(*args, **kwargs)

    @staticmethod
    def _marshal__dumps(*args, **kwargs):
        return marshal.dumps(*args, **kwargs)

    @staticmethod
    def _marshal__load(*args, **kwargs):
        marshal.load(*args, **kwargs)

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
        pickle.load(*args, **kwargs)

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
        cPickle.load(*args, **kwargs)

    @staticmethod
    def _cpickle__loads(*args, **kwargs):
        return cPickle.loads(*args, **kwargs)


def get_most_efficient_serializer(tags: Set[Tags])->Serializer:
    # TODO: сделать класс, который бы подбирал количество итераций под нужное время выдержки в секундах (float)
    # это необходимо для того чтобы правильно протестировать производительность под PyPy
    # в дальнейшем этот функционал стоит перенести в модуль performance_test_lib
    pass
