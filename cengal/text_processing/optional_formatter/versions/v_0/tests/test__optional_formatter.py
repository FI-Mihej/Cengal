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

import unittest
from cengal.text_processing.optional_formatter.versions.v_0 import OptionalFormatter, OptionalFormatterHandy
from enum import Enum

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


class TimeAttributes(Enum):
    microseconds = 0
    milliseconds = 1
    seconds = 2
    minutes = 3
    hours = 4
    days = 5
    weeks = 6
    months = 7
    years = 8
    decades = 9
    centuries = 10
    millennia = 11


TA = TimeAttributes


class TestOptionalFormatter(unittest.TestCase):
    def setUp(self):
        self.formatter = OptionalFormatter((TA.years, TA.months, TA.days), {
            TA.years : ('- ', '|(years)', '%{year}%', '|.', '; '),
            TA.months: ('- ', '|(months)', '%{1}%', '|.', '; '),
            TA.days  : ('- ', '|(days)', '%{}%', '|.', '; ')
        })

    def test_all_parameters_are_present(self):
        result = self.formatter({
            TA.years: ((1, "2",), {'year': 4, 'some': "5"}),
            TA.months: ((1, "2", 3, TA.months), dict()),
            TA.days : ((1, "2", 3, TA.months), {'some': 6})
        })
        expected_result = '|(years)%4%; - %2%; - %1%|.'
        self.assertEqual(result, expected_result, 'incorrect result')

    def test_some_parameters_are_present(self):
        result = self.formatter({
            TA.years: ((1, "2",), {'year': 4, 'some': "5"}),
            TA.days : ((1, "2", 3, TA.months), {'some': 6})
        })
        expected_result = '|(years)%4%; - %1%|.'
        self.assertEqual(result, expected_result, 'incorrect result')

    def test_none_of_parameters_are_present(self):
        result = self.formatter(dict())
        expected_result = ''
        self.assertEqual(result, expected_result, 'incorrect result')

    def test_none_of_parameters_are_present_2(self):
        result = self.formatter({})
        expected_result = ''
        self.assertEqual(result, expected_result, 'incorrect result')

    def test_blank_parameters_are_present_years(self):
        with self.assertRaises(KeyError) as cm:
            result = self.formatter({
                TA.years: (tuple(), dict())
            })

    def test_blank_parameters_are_present_months(self):
        with self.assertRaises(IndexError) as cm:
            result = self.formatter({
                TA.months: (tuple(), dict())
            })

    def test_blank_parameters_are_present_days(self):
        with self.assertRaises(IndexError) as cm:
            result = self.formatter({
                TA.days: (tuple(), dict())
            })

    def test_wrong_parameters_are_present_1(self):
        with self.subTest('1'):
            with self.assertRaises(TypeError) as cm:
                result = self.formatter({TA.years: (1, 2)})

    def test_wrong_parameters_are_present_2(self):
        with self.assertRaises(TypeError) as cm:
            result = self.formatter({TA.months: 1})

    def test_wrong_parameters_are_present_4(self):
        with self.assertRaises(TypeError) as cm:
            result = self.formatter(1)


if __name__ == '__main__':
    unittest.main()
