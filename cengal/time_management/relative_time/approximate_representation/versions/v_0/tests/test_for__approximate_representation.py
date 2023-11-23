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
from cengal.time_management.relative_time.approximate_representation.versions.v_0 import ApproximateTimeRepresentation, FULL_FORMATTER

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


class TestApproximateTimeRepresentation(unittest.TestCase):
    def setUp(self):
        self.tr = ApproximateTimeRepresentation(3.045678, crop=False)
        self.trc = ApproximateTimeRepresentation(3.045678, crop=True)

    # def test_all_parameters_are_present(self):
    #     tr = ApproximateTimeRepresentation(3.045678, crop=True)
    #     tr_res = tr.format(FULL_FORMATTER)
    #     print(tr_res)
    #     tr_res = tr.format_cropped(FULL_FORMATTER)
    #     print(tr_res)
    #     tr_res = str(tr)
    #     print(tr_res)
    #     expected_result = '|(years)%4%; - %2%; - %1%|.'
    #     self.assertEqual(1, 1, 'incorrect result')

    def test__uncroped__format(self):
        tr_res = self.tr.format()
        expected_result = 'Y0-0-0 0:0:3.045678'
        self.assertEqual(tr_res, expected_result, 'incorrect result')

    def test__uncroped__format__full(self):
        tr_res = self.tr.format(FULL_FORMATTER)
        expected_result = 'Millennia: 0, Centuries: 0, Decades: 0, Years: 0, Months: 0, Weeks: 0, Days: 0, Hours: 0, Minutes: 0, Seconds: 3, Milliseconds: 000, Microseconds: 045678'
        self.assertEqual(tr_res, expected_result, 'incorrect result')

    def test__uncroped__format_cropped(self):
        tr_res = self.tr.format_cropped()
        expected_result = 'Y0-0-0 0:0:3.045678'
        self.assertEqual(tr_res, expected_result, 'incorrect result')

    def test__uncroped__format_cropped__full(self):
        tr_res = self.tr.format_cropped(FULL_FORMATTER)
        expected_result = 'Years: 0, Months: 0, Days: 0, Hours: 0, Minutes: 0, Seconds: 3, Microseconds: 045678'
        self.assertEqual(tr_res, expected_result, 'incorrect result')

    def test__uncroped__str(self):
        tr_res = str(self.tr)
        expected_result = 'ApproximateTimeRepresentation{Millennia: 0, Centuries: 0, Decades: 0, Years: 0, Months: 0, Weeks: 0, Days: 0, Hours: 0, Minutes: 0, Seconds: 3, Milliseconds: 000, Microseconds: 045678}'
        self.assertEqual(tr_res, expected_result, 'incorrect result')

    def test__croped__format(self):
        tr_res = self.trc.format()
        expected_result = 'Y0-0-0 0:0:3.045678'
        self.assertEqual(tr_res, expected_result, 'incorrect result')

    def test__croped__format__full(self):
        tr_res = self.trc.format(FULL_FORMATTER)
        expected_result = 'Millennia: 0, Centuries: 0, Decades: 0, Years: 0, Months: 0, Weeks: 0, Days: 0, Hours: 0, Minutes: 0, Seconds: 3, Milliseconds: 000, Microseconds: 045678'
        self.assertEqual(tr_res, expected_result, 'incorrect result')

    def test__croped__format_cropped(self):
        tr_res = self.trc.format_cropped()
        expected_result = 's3.045678'
        self.assertEqual(tr_res, expected_result, 'incorrect result')

    def test__croped__format_cropped__full(self):
        tr_res = self.trc.format_cropped(FULL_FORMATTER)
        expected_result = 'Seconds: 3, Microseconds: 045678'
        self.assertEqual(tr_res, expected_result, 'incorrect result')

    def test__croped__str(self):
        tr_res = str(self.trc)
        expected_result = 'ApproximateTimeRepresentation{Millennia: 0, Centuries: 0, Decades: 0, Years: 0, Months: 0, Weeks: 0, Days: 0, Hours: 0, Minutes: 0, Seconds: 3, Milliseconds: 000, Microseconds: 045678}'
        self.assertEqual(tr_res, expected_result, 'incorrect result')


if __name__ == '__main__':
    unittest.main()
