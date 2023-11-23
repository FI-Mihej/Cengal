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


from cengal.code_flow_control.args_manager import ArgsKwargs, AK
from collections import namedtuple
from typing import Hashable, Dict, Tuple, List, Any, AnyStr, Union, Sequence

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


ItemTemplate = namedtuple("ItemTemplate", "l_delimiter, prefix, template, postfix, r_delimiter", defaults=('', '', '{}', '', ''))
IT = ItemTemplate


class OptionalFormatter:
    def __init__(self, item_positions: Tuple[Hashable, ...],
                 template_per_item: Dict[Hashable, Union[IT, Tuple[str, str, str, str, str]]]):
        self._item_positions = item_positions
        self._template_per_item = template_per_item

    def __call__(self, arguments_per_item: Dict[Hashable, Union[AK, Tuple[Tuple[Any, ...], Dict[str, Any]], Any]]):
        result = str()
        is_first = True
        last_postfix = str()
        last_r_delimiter = str()
        for item in self._item_positions:
            if item in arguments_per_item:
                item_l_delimiter, item_prefix, item_template, item_postfix, item_r_delimiter = \
                    self._template_per_item[item]
                item_args_kwargs = arguments_per_item[item]
                if isinstance(item_args_kwargs, AK):
                    item_args, item_kwargs = arguments_per_item[item]()
                elif isinstance(item_args_kwargs, tuple) and (2 == len(item_args_kwargs)) and isinstance(item_args_kwargs[0], tuple) and isinstance(item_args_kwargs[1], dict):
                    item_args, item_kwargs = arguments_per_item[item]
                else:
                    item_args = (item_args_kwargs,)
                    item_kwargs = dict()
                
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


    Example 1:
        f = OptionalFormatterHandy('hour', 'part_of_day', 'minute', 'second', 'millisecond',
                                   hour=IT('', '|(hours)', '{}', '|'),
                                   part_of_day=IT('-', '|(part_of_day)', '<{}.{second}>', '|'),
                                   minutes=IT(':', '|(minutes)', '{}', '|'),
                                   seconds=IT(':', '|(seconds)', '{}', '|'),
                                   millisecond=IT('.', '|(millisecond)', '{}', '|'))

        f(hour=4, minutes=15, seconds=54, millisecond=341)
        >> |(hours)4:15:54.341|

        f(seconds=54, minutes=15, hour=0, millisecond=0)
        >> |(hours)0:15:54.0|

        f(minutes=15, seconds=54)
        >> |(minutes)15:54|

        f(hour=4, part_of_day=AK('a', second='m'), minutes=15, seconds=54, millisecond=341)
        >> |(hours)4-<a.m>:15:54.341|

        f(part_of_day=AK('a', second='m'), minutes=15, seconds=54, millisecond=341)
        >> |(part_of_day)<a.m>:15:54.341|

        
    Example 2:
        f = OptionalFormatterHandy('hour', 'word', 'minute', 'second', 'millisecond',
                                   hour=IT('', '|(hours)', '{}', '|'),
                                   word=IT('', '|(word)', '-<"{}"-"{second}">-', '|'),
                                   minutes=IT(':', '|(minutes)', '{}', '|'),
                                   seconds=IT(':', '|(seconds)', '{}', '|'),
                                   millisecond=IT('.', '|(millisecond)', '{}', '|'))

        f(hour=4, minutes=15, seconds=54, millisecond=341)
        >> |(hours)4:15:54.341|

        f(seconds=54, minutes=15, hour=0, millisecond=0)
        >> |(hours)0:15:54.0|

        f(minutes=15, seconds=54)
        >> |(minutes)15:54|

        f(hour=4, word=AK('HELLO!', second='WORLD!'), minutes=15, seconds=54, millisecond=341)
        >> |(hours)4-<"HELLO!"-"WORLD!">-:15:54.341|

        f(word=AK('HELLO!', second='WORLD!'), minutes=15, seconds=54, millisecond=341)
        >> |(word)-<"HELLO!"-"WORLD!">-:15:54.341|
    """
    def __init__(self, *item_positions: [str, ...], **template_per_item: [str, Union[IT, Tuple[str, str, str, str, str]]]):
        super().__init__(item_positions, template_per_item)

    def __call__(self, **arguments_per_item: [str, Union[AK, Tuple[Tuple[Any, ...], Dict[str, Any]], Any]]):
        return super(OptionalFormatterHandy, self).__call__(arguments_per_item)
