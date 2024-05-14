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
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.data_manipulation.conversion.binary.versions.v_0.binary import *
from unittest import TestCase, main, skip


class TestBinaryConversions(TestCase):
    def test_bigint(self):
        data_values = [
            0,
            1,
            2,
            127,
            128,
            255,
            256,
            65535,
            65536,
            4294967295,
            4294967296,
            18446744073709551615,
            18446744073709551616,
            -0,
            -1,
            -2,
            -127,
            -128,
            -255,
            -256,
            -65535,
            -65536,
            -4294967295,
            -4294967296,
            -18446744073709551615,
            -18446744073709551616,
        ]

        for data_value in data_values:
            print(f'Testing: {data_value=}')
            self.assertEqual(data_value, bytes_to_bigint(bigint_to_bytes(data_value)))
    
    def test_ubigint(self):
        data_values = [
            0,
            1,
            2,
            127,
            128,
            255,
            256,
            65535,
            65536,
            4294967295,
            4294967296,
            18446744073709551615,
            18446744073709551616,
        ]

        for data_value in data_values:
            print(f'Testing: {data_value=}')
            self.assertEqual(data_value, bytes_to_ubigint(ubigint_to_bytes(data_value)))


if '__main__' == __name__:
    main()
