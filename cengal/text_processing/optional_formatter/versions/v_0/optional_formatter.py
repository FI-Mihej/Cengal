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

from typing import Hashable, Dict, Tuple, List, Any, AnyStr

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


class OptionalFormatter:
    def __init__(self, item_positions: Tuple[Hashable, ...],
                 template_per_item: Dict[Hashable, Tuple[str, str, str, str, str]]):
        self._item_positions = item_positions
        self._template_per_item = template_per_item

    def __call__(self, arguments_per_item: Dict[Hashable, Tuple[Tuple[Any, ...], Dict[str, Any]]]):
        result = str()
        is_first = True
        last_postfix = str()
        last_r_delimiter = str()
        for item in self._item_positions:
            if item in arguments_per_item:
                item_l_delimiter, item_prefix, item_template, item_postfix, item_r_delimiter = \
                    self._template_per_item[item]
                item_args, item_kwargs = arguments_per_item[item]

                rendered_item = str()
                if is_first:
                    rendered_item += item_prefix
                else:
                    rendered_item += last_r_delimiter
                    rendered_item += item_l_delimiter
                last_r_delimiter = item_r_delimiter
                last_postfix = item_postfix
                rendered_item += item_template.format(*item_args, **item_kwargs)
                result += rendered_item
                if is_first:
                    is_first = False
        result += last_postfix
        return result


class OptionalFormatterHandy(OptionalFormatter):
    """
    template_per_item second tuple format:
    [left_delimiter(shown if not first), prefix(shown if first), template, postfix(shown if last), right_delimiter(shown if not last)]

    Example:
        f = OptionalFormatterHandy('hour', 'word', 'minute', 'second', 'millisecond',
                                   hour=('', '|(hours)', '{}', '|', ''),
                                   word=('', '|(word)', '-"{}"-', '|', ''),
                                   minutes=(':', '|(minutes)', '{}', '|', ''),
                                   seconds=(':', '|(seconds)', '{}', '|', ''),
                                   millisecond=('.', '|(millisecond)', '{}', '|', ''))

        f(hour=((4,), dict()), minutes=((15,), dict()), seconds=((54,), dict()), millisecond=((341,), dict()))
        >> |(hours)4:15:54.341|

        f(hour=((0,), dict()), minutes=((15,), dict()), seconds=((54,), dict()), millisecond=((0,), dict()))
        >> |(hours)0:15:54.0|

        f(minutes=((15,), dict()), seconds=((54,), dict()))
        >> |(minutes)15:54|

        f(word=(('HELLO!',), dict()), hour=((4,), dict()), minutes=((15,), dict()), seconds=((54,), dict()), millisecond=((341,), dict()))
        >> |(hours)4-"HELLO!"-:15:54.341|
    """
    def __init__(self, *item_positions: [str, ...], **template_per_item: [str, Tuple[str, str, str, str, str]]):
        super().__init__(item_positions, template_per_item)

    def __call__(self, **arguments_per_item: [str, Tuple[Tuple[Any, ...], Dict[str, Any]]]):
        return super(OptionalFormatterHandy, self).__call__(arguments_per_item)
