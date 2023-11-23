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

from cengal.math.numbers import RationalNumber
from cengal.time_management.repeat_for_a_time import Tracer
from math import sqrt, pi, factorial

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

class Ellipse:
    """
    https://www.youtube.com/watch?v=5nW3nJhBHL0
    http://www.ebyte.it/library/docs/math05a/EllipsePerimeterApprox05.html
    """
    def __init__(self, a: RationalNumber, b: RationalNumber):
        self.a = a
        self.b = b
    
    def y(self, x: RationalNumber) -> RationalNumber:
        return self.b * sqrt(1 - (x / self.a)**2)
    
    @property
    def area(self):
        return pi * self.a * self.b
    
    @property
    def h(self):
        return ((self.a - self.b)**2) / ((self.a + self.b)**2)
    
    @property
    def e(self):
        return sqrt(self.a**2 - self.b**2) / self.a
    
    @property
    def c(self):
        return self.a * self.e
    
    @property
    def perimeter__kepler(self):
        return 2 * pi * sqrt(self.a * self.b)
    
    @property
    def perimeter__naive(self):
        return 2 * pi * ((self.a + self.b) / 2)
    
    @property
    def perimeter__euler(self):
        return 2 * pi * sqrt((self.a**2 - self.b**2) / 2)
    
    @property
    def perimeter__matt_parker__lazy(self):
        """Computationly efficient. Not more that 6.1% deviation (less than 5% for `1 / 75` ellipses)

        Returns:
            _type_: _description_
        """
        a = max(self.a, self.b)
        b = min(self.a, self.b)
        return pi * ((6 * a) / 5 + (3 * b) / 4)
    
    @property
    def perimeter__best_of__euler__and__matt_parker__lazy(self):
        a = max(self.a, self.b)
        b = min(self.a, self.b)
        if (a / b) >= 0.8:
            return self.perimeter__matt_parker__lazy
        else:
            return self.perimeter__euler
    
    @property
    def perimeter__ramanujan_1(self):
        return pi * (3 * (self.a + self.b) - sqrt((3 * self.a + self.b) * (self.a + 3 * self.b)))
    
    @property
    def perimeter__matt_parker__precise(self):
        a = max(self.a, self.b)
        b = min(self.a, self.b)
        return pi * ((53 * a) / 3 + (717 * b) / 35 - sqrt(269 * a ** 2 + 667 * a * b + 371 * b ** 2))
    
    @property
    def perimeter__best_of__ramanujan_1__and__matt_parker__precise(self):
        a = max(self.a, self.b)
        b = min(self.a, self.b)
        if (a / b) >= 2.4:
            return self.perimeter__matt_parker__precise
        else:
            return self.perimeter__ramanujan_1
    
    @property
    def perimeter__ramanujan_2(self):
        return pi * (self.a + self.b) * (1 + (3 * self.h) / (10 + sqrt(4 - 3 * self.h)))
    
    def perimeter__infinite_sum__time_lim(self, desired_approximation_time: float, return_iterations_num: bool = False):
        e = self.e
        first_multiplier = 2 * self.a * pi
        second_multiplier = 1
        tr = Tracer(desired_approximation_time)
        while tr.iter():
            i = tr.total_number_of_iterations_made
            second_multiplier -= ((factorial(2 * i) ** 2) / ((2 ** i * factorial(i)) ** 4)) * ((e ** (2 * i)) / (2 * i - 1))

        if return_iterations_num:
            return first_multiplier * second_multiplier, tr.total_number_of_iterations_made
        else:
            return first_multiplier * second_multiplier
    
    def perimeter__infinite_sum__iter_lim(self, iterations_num: int):
        e = self.e
        first_multiplier = 2 * self.a * pi
        second_multiplier = 1
        for i in range(1, iterations_num + 1):
            second_multiplier -= ((factorial(2 * i) ** 2) / ((2 ** i * factorial(i)) ** 4)) * ((e ** (2 * i)) / (2 * i - 1))

        return first_multiplier * second_multiplier
    
    @staticmethod
    def from_r1_r2(r1: RationalNumber, r2: RationalNumber):
        return Ellipse((r1 + r2) / 2, 1)
