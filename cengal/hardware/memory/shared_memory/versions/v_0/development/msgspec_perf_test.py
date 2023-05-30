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
__version__ = "3.2.6"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from struct import pack, unpack, pack_into, unpack_from
import msgspec
import sys

from cengal.performance_test_lib import PrecisePerformanceTestTracer
from cengal.introspection.inspect import func_name, entity_properties
from threading import Lock, RLock
from multiprocessing import Process, Manager
from pprint import pprint
from typing import Callable, Set, Optional, Dict, Type


def func_perf_test(func: Callable, *args, **kwargs):
    tr = PrecisePerformanceTestTracer(1.0)
    while tr.iter():
        func(*args, **kwargs)

    with tr as fast_iter:
        for i in fast_iter:
            func(*args, **kwargs)

    print('{}(): {} iter/s; {} seconds; {} iterations'.format(func_name(func), tr.iter_per_time_unit, tr.time_spent, tr.iterations_made))


def print_size(func: Callable):
    print(f'{func_name(func)}: {func()}')


class User(msgspec.Struct):
    """A new type describing a User"""
    name: str
    groups: Set[str] = set()
    email: Optional[str] = None
    id: int = 0
    sessions: Dict[int, str] = {}


class UserInt(msgspec.Struct):
    """A new type describing a User"""
    _0: str
    _1: Set[str] = set()
    _2: Optional[str] = None
    _3: int = 0
    _4: Dict[int, str] = {}


# user_type: Type = UserInt
user_type: Type = User


def make_user():
    if user_type is User:
        user = User("alice", groups={"admin", "engineering"}, email='me@mail.com', id=123456789)
        user.sessions[1] = 'session1'
        user.sessions[2] = 'session2'
    elif user_type is UserInt:
        user = UserInt("alice", _1={"admin", "engineering"}, _2='me@mail.com', _3=123456789)
        user._4[1] = 'session1'
        user._4[2] = 'session2'
    else:
        raise NotImplementedError
    
    return user


def struct_info():
    pprint(entity_properties(user_type))
    pprint(user_type.__slots__)
    # for slot_name in user_type.__slots__:
    #     pprint(dir(getattr(user_type, slot_name)))
    
    alice = make_user()
    pprint(entity_properties(alice))


def struck_size_json_test():
    alice = make_user()
    return len(msgspec.json.encode(alice))


def struck_size_msgpack_test():
    alice = make_user()
    return len(msgspec.msgpack.encode(alice))


def struck_full_json_test():
    alice = make_user()
    msg = msgspec.json.encode(alice)
    msgspec.json.decode(msg, type=user_type)


def struck_full_msgpack_test():
    alice = make_user()
    msg = msgspec.msgpack.encode(alice)
    msgspec.msgpack.decode(msg, type=user_type)


def struck_create_msgpack_test():
    alice = make_user()


global_alice = make_user()
global_msg = msgspec.msgpack.encode(global_alice)
global_ba = bytearray(800)
global_mv = memoryview(global_ba)  # does not supported by msgspec
global_encoder = msgspec.msgpack.Encoder()
global_decoder = msgspec.msgpack.Decoder()


def struck_encode_msgpack_test():
    msgspec.msgpack.encode(global_alice)


def struck_decode_msgpack_test():
    msgspec.msgpack.decode(global_msg, type=user_type)


def struck_encode_into_msgpack_test():
    global_encoder.encode_into(global_alice, global_ba, 100)


def struck_decode_from_msgpack_test():
    global_decoder.decode(global_ba[100:])


def struck_full_into_msgpack_test():
    alice = make_user()
    global_encoder.encode_into(global_alice, global_ba, 100)
    global_decoder.decode(global_ba[100:])


def struck_full_into_msgpack_with_size_test():
    alice = make_user()
    global_encoder.encode_into(global_alice, global_ba, 8)
    n = len(global_ba) - 8
    global_ba[:8] = n.to_bytes(8, "big")
    n = int.from_bytes(global_ba[:8], "big")
    global_decoder.decode(global_ba[8: 8 + n])


def struck_full_into_msgpack_with_size_pack_into_test():
    alice = make_user()
    global_encoder.encode_into(global_alice, global_ba, 8)
    n = len(global_ba) - 8
    pack_into('Q', global_ba, 0, n)
    n = unpack_from('Q', global_ba, 0)[0]
    global_decoder.decode(global_ba[8: 8 + n])


def buff_size_test():
    encoder = msgspec.msgpack.Encoder()
    buffer = bytearray(800)
    print(f'0 - buffer size: {len(buffer)}')
    print(f'0 - buffer size: {buffer.__sizeof__()}')
    print(f'0 - buffer size: {sys.getsizeof(buffer)}')
    encoder.encode_into(global_alice, buffer, 100)
    print(f'1 - buffer size: {len(buffer)}')
    print(f'1 - buffer size: {buffer.__sizeof__()}')
    print(f'1 - buffer size: {sys.getsizeof(buffer)}')
    encoder.encode_into(global_alice, buffer, 10)
    print(f'2 - buffer size: {len(buffer)}')
    print(f'2 - buffer size: {buffer.__sizeof__()}')
    print(f'2 - buffer size: {sys.getsizeof(buffer)}')
    data: User = global_decoder.decode(buffer[10:])
    print(data)


def main():
    '''
    Output:
        struck_size_json_test: 129
        struck_size_msgpack_test: 94
        0 - buffer size: 800
        0 - buffer size: 857
        0 - buffer size: 857
        1 - buffer size: 194
        1 - buffer size: 857
        1 - buffer size: 857
        2 - buffer size: 104
        2 - buffer size: 857
        2 - buffer size: 857
        {'name': 'alice', 'groups': ['admin', 'engineering'], 'email': 'me@mail.com', 'id': 123456789, 'sessions': {1: 'session1', 2: 'session2'}}
        struck_full_json_test(): 388722.75 iter/s; 0.90625 seconds; 352280 iterations
        struck_full_msgpack_test(): 393309.1875 iter/s; 0.890625 seconds; 350291 iterations
        struck_create_msgpack_test(): 2894812.0 iter/s; 0.75 seconds; 2171109 iterations
        struck_encode_msgpack_test(): 1994355.875 iter/s; 0.90625 seconds; 1807385 iterations
        struck_decode_msgpack_test(): 947713.125 iter/s; 0.875 seconds; 829249 iterations
        struck_encode_into_msgpack_test(): 2896200.75 iter/s; 0.90625 seconds; 2624682 iterations
        struck_decode_from_msgpack_test(): 1088295.75 iter/s; 0.90625 seconds; 986268 iterations
        struck_full_into_msgpack_test(): 497090.28125 iter/s; 0.875 seconds; 434954 iterations
        struck_full_into_msgpack_with_size_test(): 258692.203125 iter/s; 0.953125 seconds; 246566 iterations
        struck_full_into_msgpack_with_size_pack_into_test(): 347835.59375 iter/s; 0.90625 seconds; 315226 iterations
    '''
    struct_info()
    print_size(struck_size_json_test)
    print_size(struck_size_msgpack_test)
    buff_size_test()
    func_perf_test(struck_full_json_test)
    func_perf_test(struck_full_msgpack_test)
    func_perf_test(struck_create_msgpack_test)
    func_perf_test(struck_encode_msgpack_test)
    func_perf_test(struck_decode_msgpack_test)
    func_perf_test(struck_encode_into_msgpack_test)
    func_perf_test(struck_decode_from_msgpack_test)
    func_perf_test(struck_full_into_msgpack_test)
    func_perf_test(struck_full_into_msgpack_with_size_test)
    func_perf_test(struck_full_into_msgpack_with_size_pack_into_test)


if '__main__' == __name__:
    main()
