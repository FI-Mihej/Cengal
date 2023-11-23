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


from threading import current_thread
from cengal.text_processing.text_processing import find_text, normalize_text
from cengal.text_processing.utf_bom_processing import remove_bom, determine_text_bom
from cengal.performance_test_lib.performance_test_lib import test_performance
from array import array

s_p =('qwertyuiop'*102)*25
s0 = 'Hello World!'
s = s_p + s0 + s_p
s_1 = s0 + s_p + s_p
s2 = 'orl'
s3 = 'World!'
s4 = 'Hello'

b_1 = normalize_text(s_1, bytearray, 'utf-32')
b_1 = remove_bom(b_1, determine_text_bom(b_1))
b4 = normalize_text(s4, bytearray, 'utf-32')
b4 = remove_bom(b4, determine_text_bom(b4))
a_1 = array('L', b_1)
a4 = array('L', b4)

print(f'> len(s): {len(s)}')
print(f'> len(s2): {len(s2)}')
s2_place = find_text(s, s2)
print('s2_place:', s2_place)
print('s[s2_place]:', s[s2_place])
b = normalize_text(s, bytearray, 'utf-32')
print(f'> len(b): {len(b)}')
b = remove_bom(b, determine_text_bom(b))
print(f'> len(b): {len(b)}')
b2 = normalize_text(s2, bytearray, 'utf-32')
bom = determine_text_bom(b2)
print(f'> len(b2): {len(b2)}')
print(f'b2: {b2}; len: {len(b2)}')
b2 = remove_bom(b2, bom)

ba = bytearray(b)
ba2 = bytearray(b2)

print(f'> len(b2): {len(b2)}')
print(f'b2: {b2}; len: {len(b2)}')
b2_place = find_text(b, b2)
print('b2_place:', b2_place)
print('b->str slice:', (bom + (b[b2_place])).decode('utf-32'))
print('b2->str:', (bom + b2).decode('utf-32'))
print(b[b2_place] == b2)
m = memoryview(b)
m2 = memoryview(b2)
print(m[b2_place] == m2)

print()
print('itemsize:', array('L').itemsize)
print(f'len b: {len(b)}')
a = array('L', b)
print(f'> len(a): {len(a)}')
a2 = array('L', b2)
print(f'> len(a2): {len(a2)}')
print(f'a2: {a2}')
a2_place = slice(int(b2_place.start / 4), int(b2_place.stop / 4))
ma = memoryview(a)
ma2 = memoryview(a2)
print(ma[a2_place] == ma2)

b2_len = len(b2)
ba2_len = len(ba2)
s2_len = len(s2)
s3_len = len(s3)
s4_len = len(s4)
b4_len = len(b4)
b4_len = len(b4)
a4_len = len(a4)

with test_performance('b[b2_place] == b2', 1) as tracer:
    while tracer.iter():
        b[b2_place] == b2

with test_performance('m[b2_place] == m2', 1) as tracer:
    while tracer.iter():
        m[b2_place] == m2

with test_performance('a[a2_place] == a2', 1) as tracer:
    while tracer.iter():
        a[a2_place] == a2

with test_performance('ma[a2_place] == ma2', 1) as tracer:
    while tracer.iter():
        ma[a2_place] == ma2

with test_performance('bytes(ma)', 1) as tracer:
    while tracer.iter():
        result = bytes(ma)

with test_performance('ma.tobytes()', 1) as tracer:
    while tracer.iter():
        result = ma.tobytes()

with test_performance('a.tobytes()', 1) as tracer:
    while tracer.iter():
        result = a.tobytes()

with test_performance('str.find(s2)', 1) as tracer:
    while tracer.iter():
        start = s.find(s2)
        place = slice(start, start + s2_len)

with test_performance('find_text(s, s2)', 1) as tracer:
    while tracer.iter():
        place = find_text(s, s2)

with test_performance('str.find(s3)', 1) as tracer:
    while tracer.iter():
        start = s.find(s3)
        place = slice(start, start + s3_len)

with test_performance('find_text(s, s3)', 1) as tracer:
    while tracer.iter():
        place = find_text(s, s3)

with test_performance('s_1.startswith(s4)', 1) as tracer:
    while tracer.iter():
        if s_1.startswith(s4):
            place = slice(0, s4_len)
        else:
            place = None

with test_performance('b_1.startswith(b4)', 1) as tracer:
    while tracer.iter():
        if b_1.startswith(b4):
            place = slice(0, b4_len)
        else:
            place = None

with test_performance('a_1[:a4_len] == a4', 1) as tracer:
    while tracer.iter():
        if a_1[:a4_len] == a4:
            place = slice(0, a4_len)
        else:
            place = None

with test_performance('b_1[:b4_len] == a4', 1) as tracer:
    while tracer.iter():
        if b_1[:b4_len] == b4:
            place = slice(0, b4_len)
        else:
            place = None

with test_performance('s_1[:s4_len] == s4', 1) as tracer:
    while tracer.iter():
        if s_1[:s4_len] == s4:
            place = slice(0, s4_len)
        else:
            place = None

with test_performance('s[s2_place] == s2', 1) as tracer:
    while tracer.iter():
        if s[s2_place] == s2:
            place = slice(s2_place)
        else:
            place = None

with test_performance('s[place] == s2', 1) as tracer:
    while tracer.iter():
        place = slice(102028, 102040)
        if s[place] == s2:
            place = slice(place)
        else:
            place = None

with test_performance('s[slice(102028, 102040)] == s2', 1) as tracer:
    while tracer.iter():
        if s[slice(102028, 102040)] == s2:
            place = slice(102028, 102040)
        else:
            place = None

with test_performance('s[25507:25510] == s2', 1) as tracer:
    while tracer.iter():
        if s[25507:25510] == s2:
            place = slice(25507, 25510)
        else:
            place = None

with test_performance('s[place] == s2 ; slice(s2_place.start, s2_place.start + s2_len)', 1) as tracer:
    while tracer.iter():
        place = slice(s2_place.start, s2_place.start + s2_len)
        if s[place] == s2:
            place = slice(place)
        else:
            place = None

with test_performance('s[slice(s2_place.start, s2_place.start + s2_len)] == s2', 1) as tracer:
    while tracer.iter():
        if s[slice(s2_place.start, s2_place.start + s2_len)] == s2:
            place = slice(s2_place.start, s2_place.start + s2_len)
        else:
            place = None

with test_performance('s[place] == s2 ; slice(start, start + s2_len)', 1) as tracer:
    while tracer.iter():
        start = s2_place.start
        place = slice(start, start + s2_len)
        if s[place] == s2:
            place = slice(place)
        else:
            place = None

with test_performance('s[slice(start, end)] == s2', 1) as tracer:
    # Fastest
    while tracer.iter():
        start = s2_place.start
        end = start + s2_len
        if s[slice(start, end)] == s2:
            place = slice(start, end)
        else:
            place = None

with test_performance('bytearray.find', 1) as tracer:
    while tracer.iter():
        start = ba.find(ba2)
        place = slice(start, start + ba2_len)

with test_performance('find_text(b, b2)', 1) as tracer:
    while tracer.iter():
        place = find_text(ba, ba2)

with test_performance('bytes.find', 1) as tracer:
    while tracer.iter():
        start = b.find(b2)
        place = slice(start, start + b2_len)

with test_performance('find_text(b, b2)', 1) as tracer:
    while tracer.iter():
        place = find_text(b, b2)

with test_performance('ma.tobytes().find(b2) /', 1) as tracer:
    while tracer.iter():
        start = ma.tobytes().find(b2)
        place = slice(int(start / 4), int((start + b2_len) / 4))

with test_performance('ma.tobytes().find(b2) >>', 1) as tracer:
    while tracer.iter():
        start = ma.tobytes().find(b2)
        place = slice(start >> 2, (start + b2_len) >> 2)

with test_performance('a.tobytes().find(b2) >>', 1) as tracer:
    while tracer.iter():
        start = a.tobytes().find(b2)
        place = slice(start >> 2, (start + b2_len) >> 2)

with test_performance('find_text(ma.tobytes(), b2)', 1) as tracer:
    while tracer.iter():
        place = find_text(ma.tobytes(), b2)
        place = slice(place.start >> 2, (place.start + b2_len) >> 2)

