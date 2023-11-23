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

from typing import Union, Set, Tuple, Dict
from math import modf
from enum import Enum
from copy import copy
from cengal.data_manipulation.help_tools import inverse_mapping
from cengal.text_processing.optional_formatter.versions.v_0 import OptionalFormatter
from ....constants import *

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


SECONDS_PER_YEAR = SECONDS_PER_DAY * 365
SECONDS_PER_MONTH = round(SECONDS_PER_YEAR / 12)
SECONDS_PER_DECADE = SECONDS_PER_YEAR * 10
SECONDS_PER_CENTURY = SECONDS_PER_YEAR * 100
SECONDS_PER_MILLENIA = SECONDS_PER_YEAR * 1000


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


ATTRIBUTES_ASCENDING = sorted(TimeAttributes, key=lambda item: item.value, reverse=False)
ATTRIBUTES_DESCENDING = sorted(TimeAttributes, key=lambda item: item.value, reverse=True)


DIVIDER_PER_ATTRIBUTE = {
    TimeAttributes.millennia: SECONDS_PER_MILLENIA,
    TimeAttributes.centuries: SECONDS_PER_CENTURY,
    TimeAttributes.decades: SECONDS_PER_DECADE,
    TimeAttributes.years: SECONDS_PER_YEAR,
    TimeAttributes.months: SECONDS_PER_MONTH,
    TimeAttributes.weeks: SECONDS_PER_WEEK,
    TimeAttributes.days: SECONDS_PER_DAY,
    TimeAttributes.hours: SECONDS_PER_HOUR,
    TimeAttributes.minutes: SECONDS_PER_MINUTE
}

ATTRIBUTE_PER_DIVIDER = inverse_mapping(DIVIDER_PER_ATTRIBUTE)

DIV_ATTRIBUTES = set(DIVIDER_PER_ATTRIBUTE)
DIV_ATTRIBUTES_ASCENDING = sorted(DIV_ATTRIBUTES, key=lambda item: item.value, reverse=False)
DIV_ATTRIBUTES_DESCENDING = sorted(DIV_ATTRIBUTES, key=lambda item: item.value, reverse=True)


MULTIPLIER_PER_ATTRIBUTE = {
    TimeAttributes.milliseconds: 1 / SECONDS_PER_MILLISECOND,
    TimeAttributes.microseconds: 1 / SECONDS_PER_MICROSECOND
}

ATTRIBUTE_PER_MULTIPLIER = inverse_mapping(MULTIPLIER_PER_ATTRIBUTE)

MUL_ATTRIBUTES = set(MULTIPLIER_PER_ATTRIBUTE)
MUL_ATTRIBUTES_ASCENDING = sorted(MUL_ATTRIBUTES, key=lambda item: item.value, reverse=False)
MUL_ATTRIBUTES_DESCENDING = sorted(MUL_ATTRIBUTES, key=lambda item: item.value, reverse=True)


DEFAULT_ATTRIBUTES = {
    TimeAttributes.years
    , TimeAttributes.months
    , TimeAttributes.days
    , TimeAttributes.hours
    , TimeAttributes.minutes
    , TimeAttributes.seconds
    , TimeAttributes.microseconds
}

DEFAULT_ATTRIBUTES_ASCENDING = sorted(DEFAULT_ATTRIBUTES, key=lambda item: item.value, reverse=False)
DEFAULT_ATTRIBUTES_DESCENDING = sorted(DEFAULT_ATTRIBUTES, key=lambda item: item.value, reverse=True)


DEFAULT_FORMATTER = OptionalFormatter(tuple(DEFAULT_ATTRIBUTES_DESCENDING), {
    TimeAttributes.years: ('',  'Y', '{}', '', '-'),
    TimeAttributes.months: ('', 'M',  '{}', '', '-'),
    TimeAttributes.days: ('', 'D', '{}', '', ' '),
    TimeAttributes.hours: ('', 'h', '{}', '', ''),
    TimeAttributes.minutes: (':', 'm', '{}', '', ''),
    TimeAttributes.seconds: (':', 's', '{}', '', ''),
    TimeAttributes.microseconds: ('.', 'μs', '{0:0>6}', '', '')
})

FULL_FORMATTER = OptionalFormatter(tuple(ATTRIBUTES_DESCENDING), {
    TimeAttributes.millennia: ('', '', 'Millennia: {}', '', ', '),
    TimeAttributes.centuries: ('', '', 'Centuries: {}', '', ', '),
    TimeAttributes.decades: ('', '', 'Decades: {}', '', ', '),
    TimeAttributes.years: ('', '', 'Years: {}', '', ', '),
    TimeAttributes.months: ('', '', 'Months: {}', '', ', '),
    TimeAttributes.weeks: ('', '', 'Weeks: {}', '', ', '),
    TimeAttributes.days: ('', '', 'Days: {}', '', ', '),
    TimeAttributes.hours: ('', '', 'Hours: {}', '', ', '),
    TimeAttributes.minutes: ('', '', 'Minutes: {}', '', ', '),
    TimeAttributes.seconds: ('', '', 'Seconds: {}', '', ', '),
    TimeAttributes.milliseconds: ('', '', 'Milliseconds: {0:0>3}', '', ', '),
    TimeAttributes.microseconds: ('', '', 'Microseconds: {0:0>6}', '', ', '),
})


class ApproximateTimeRepresentation:
    def __init__(self, seconds: Union[int, float], attributes: Union[Set[TimeAttributes], None]=None, crop: bool=False):
        self._initial__seconds = seconds
        self._initial__attributes = attributes or DEFAULT_ATTRIBUTES
        self._initial__crop = crop

        self.values = dict()

        rest = self._initial__seconds
        for attribute in DIV_ATTRIBUTES_DESCENDING:
            self.values[attribute], rest = self.compute_attribute(rest, attribute)

        rest, seconds = modf(rest)
        seconds = int(seconds)
        self.values[TimeAttributes.seconds] = seconds

        for attribute in MUL_ATTRIBUTES_DESCENDING:
            self.values[attribute], rest = self.compute_fractional_attribute(rest, attribute)

        self.cropped_values = copy(self.values)
        self._normalize()
        if self._initial__crop:
            self._crop()

    def compute_attribute(self, seconds: float,
                          attribute: TimeAttributes) -> Tuple[float, float]:
        if attribute in self._initial__attributes:
            result, rest = divmod(seconds, DIVIDER_PER_ATTRIBUTE[attribute])
            result = int(result)
            return result, rest
        else:
            return 0, seconds

    def compute_fractional_attribute(self, seconds: float,
                                     attribute: TimeAttributes) -> Tuple[float, float]:
        if attribute in self._initial__attributes:
            multiplier = MULTIPLIER_PER_ATTRIBUTE[attribute]
            rest, integer_value = modf(seconds * multiplier)
            integer_value = int(integer_value)
            rest /= multiplier
            return integer_value, rest
        else:
            return 0, seconds

    def _normalize(self):
        for attribute in TimeAttributes:
            if attribute not in self._initial__attributes:
                if attribute in self.cropped_values:
                    del self.cropped_values[attribute]

    def _crop(self):
        descending_stopped = False
        ascending_stopped = False

        for attribute in ATTRIBUTES_DESCENDING:
            descending_stopped = self._crop__check_attribute(self.values[attribute], attribute, descending_stopped)

        for attribute in ATTRIBUTES_ASCENDING:
            ascending_stopped = self._crop__check_attribute(self.values[attribute], attribute, ascending_stopped)

    def _crop__check_attribute(self, value: Union[int, float], attribute: TimeAttributes, stopped: bool) -> bool:
        if stopped or (0 != value):
            return True
        else:
            if attribute in self.cropped_values:
                del self.cropped_values[attribute]
            return False

    def format(self, formatter: Union[OptionalFormatter, None]=None) -> str:
        formatter = formatter or DEFAULT_FORMATTER
        args = tuple()
        return formatter(self._construct_formatter_dict(self.values))

    def format_cropped(self, formatter: Union[OptionalFormatter, None]=None) -> str:
        formatter = formatter or DEFAULT_FORMATTER
        return formatter(self._construct_formatter_dict(self.cropped_values))

    def __str__(self):
        formatter = FULL_FORMATTER
        return '{class_name}{{{data}}}'.format(class_name=self.__class__.__name__,
                                               data=formatter(self._construct_formatter_dict(self.values)))

    @staticmethod
    def _construct_formatter_dict(values: Dict[TimeAttributes, Union[int, float]]):
        result = dict()
        for item, value in values.items():
            result[item] = ((value,), dict())
        return result
