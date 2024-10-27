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
from cengal.code_flow_control.smart_values import ValueType
from enum import IntEnum
from collections import namedtuple
from typing import Hashable, Dict, Tuple, List, Any, AnyStr, Union, Sequence, Mapping, cast, NamedTuple

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


ItemTemplate = namedtuple("ItemTemplate", "l_delimiter, prefix, template, postfix, r_delimiter", defaults=('', '', '{}', '', ''))
IT = ItemTemplate


ItemTemplate0 = namedtuple("ItemTemplate0", "template, l_delimiter, prefix, postfix, r_delimiter", defaults=('{}', '', '', '', ''))
IT0 = ItemTemplate0


ItemTemplate1 = namedtuple("ItemTemplate1", "l_delimiter, template, prefix, postfix, r_delimiter", defaults=('', '{}', '', '', ''))
IT1 = ItemTemplate1


ItemTemplate2 = namedtuple("ItemTemplate2", "l_delimiter, prefix, template, postfix, r_delimiter", defaults=('', '', '{}', '', ''))
IT2 = ItemTemplate2


ItemTemplate3 = namedtuple("ItemTemplate3", "l_delimiter, prefix, postfix, template, r_delimiter", defaults=('', '', '', '{}', ''))
IT3 = ItemTemplate3


ItemTemplate4 = namedtuple("ItemTemplate4", "l_delimiter, prefix, postfix, r_delimiter, template", defaults=('', '', '', '', '{}'))
IT4 = ItemTemplate4


class ItemType:
    str_slice = 0
    obj = 1


class OptionalFormatter:
    def __init__(self, item_positions: Tuple[Hashable, ...],
                 template_per_item: Dict[Hashable, Union[IT, Tuple[str, str, str, str, str]]]):
        self._item_positions = item_positions
        self._template_per_item = template_per_item

    def __call__(self, arguments_per_item: Dict[Hashable, Union[AK, Any]]) -> str:
        result = str()
        is_first = True
        last_postfix = str()
        last_r_delimiter = str()
        for item in self._item_positions:
            if item in arguments_per_item:
                item_template = self._template_per_item[item]
                parsed: bool = False
                if isinstance(item_template, (IT, IT2)):
                    item_l_delimiter, item_prefix, item__template, item_postfix, item_r_delimiter = item_template
                    parsed = True
                
                if not parsed:
                    try:
                        try:
                            item_l_delimiter = item_template.l_delimiter
                            item_prefix = item_template.prefix
                            item__template = item_template.template
                            item_postfix = item_template.postfix
                            item_r_delimiter = item_template.r_delimiter
                            parsed = True
                        except AttributeError:
                            item_l_delimiter = item_template.ld
                            item_prefix = item_template.pr
                            item__template = item_template.t
                            item_postfix = item_template.po
                            item_r_delimiter = item_template.rd
                            parsed = True
                    except AttributeError:
                        pass
                
                if not parsed:
                    if isinstance(item_template, Mapping):
                        item_template = cast(dict, item_template)
                        if 'l_delimiter' in item_template:
                            item_l_delimiter = item_template['l_delimiter']
                        else:
                            item_l_delimiter = item_template.get('ld', '')

                        if 'prefix' in item_template:
                            item_prefix = item_template['prefix']
                        else:
                            item_prefix = item_template.get('pr', '')

                        if 'template' in item_template:
                            item__template = item_template['template']
                        else:
                            item__template = item_template.get('t', '')

                        if 'postfix' in item_template:
                            item_postfix = item_template['postfix']
                        else:
                            item_postfix = item_template.get('po', '')

                        if 'r_delimiter' in item_template:
                            item_r_delimiter = item_template['r_delimiter']
                        else:
                            item_r_delimiter = item_template.get('rd', '')
                        
                        parsed = True
                    elif isinstance(item_template, (tuple, list)):
                        item_l_delimiter, item_prefix, item__template, item_postfix, item_r_delimiter = item_template
                        parsed = True

                item_args_kwargs = arguments_per_item[item]
                if isinstance(item_args_kwargs, AK):
                    item_args, item_kwargs = arguments_per_item[item]()
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
                rendered_item += item__template.format(*item_args, **item_kwargs)
                result += rendered_item
                if is_first:
                    is_first = False
                
        result += last_postfix
        return result

    def to_list(self, arguments_per_item: Dict[Hashable, Union[AK, Any]]) -> List[Union[str, Any]]:
        result = list()
        is_first = True
        last_postfix = str()
        last_r_delimiter = str()
        for item in self._item_positions:
            if item in arguments_per_item:
                item_template = self._template_per_item[item]
                parsed: bool = False
                if isinstance(item_template, (IT, IT2)):
                    item_l_delimiter, item_prefix, item__template, item_postfix, item_r_delimiter = item_template
                    parsed = True
                
                if not parsed:
                    try:
                        try:
                            item_l_delimiter = item_template.l_delimiter
                            item_prefix = item_template.prefix
                            item__template = item_template.template
                            item_postfix = item_template.postfix
                            item_r_delimiter = item_template.r_delimiter
                            parsed = True
                        except AttributeError:
                            item_l_delimiter = item_template.ld
                            item_prefix = item_template.pr
                            item__template = item_template.t
                            item_postfix = item_template.po
                            item_r_delimiter = item_template.rd
                            parsed = True
                    except AttributeError:
                        pass
                
                if not parsed:
                    if isinstance(item_template, Mapping):
                        item_template = cast(dict, item_template)
                        if 'l_delimiter' in item_template:
                            item_l_delimiter = item_template['l_delimiter']
                        else:
                            item_l_delimiter = item_template.get('ld', '')

                        if 'prefix' in item_template:
                            item_prefix = item_template['prefix']
                        else:
                            item_prefix = item_template.get('pr', '')

                        if 'template' in item_template:
                            item__template = item_template['template']
                        else:
                            item__template = item_template.get('t', '')

                        if 'postfix' in item_template:
                            item_postfix = item_template['postfix']
                        else:
                            item_postfix = item_template.get('po', '')

                        if 'r_delimiter' in item_template:
                            item_r_delimiter = item_template['r_delimiter']
                        else:
                            item_r_delimiter = item_template.get('rd', '')
                        
                        parsed = True
                    elif isinstance(item_template, (tuple, list)):
                        item_l_delimiter, item_prefix, item__template, item_postfix, item_r_delimiter = item_template
                        parsed = True

                item_args_kwargs = arguments_per_item[item]
                if isinstance(item_args_kwargs, AK):
                    item_args, item_kwargs = item_args_kwargs()
                else:
                    item_args = (item_args_kwargs,)
                    item_kwargs = dict()
                
                if is_first:
                    result.append(item_prefix)
                else:
                    result.append(last_r_delimiter)
                    result.append(item_l_delimiter)
                
                last_r_delimiter = item_r_delimiter
                last_postfix = item_postfix
                if item__template is None:
                    result.append(item_args_kwargs)
                else:
                    result.append(item__template.format(*item_args, **item_kwargs))

                if is_first:
                    is_first = False
                
        result.append(last_postfix)
        return result

    def to_joined_list(self, arguments_per_item: Dict[Hashable, Union[AK, Any]]) -> List[Union[str, Any]]:
        sub_result: List[Union[str, Any]] = self.to_list(arguments_per_item)
        result: List[Union[str, Any]] = list()
        str_items_index_slices: List[ValueType] = list()
        first = None
        for index, item in enumerate(sub_result):
            if isinstance(item, str):
                if first is None:
                    first = index
            else:
                if first is not None:
                    str_items_index_slices.append(ValueType(ItemType.str_slice, slice(first, index)))
                    first = None

                str_items_index_slices.append(ValueType(ItemType.obj, item))

        if first is not None:
            str_items_index_slices.append(ValueType(ItemType.str_slice, slice(first, -1)))
            first = None

        for items_or_slice in str_items_index_slices:
            if items_or_slice == ItemType.str_slice:
                result.append(''.join(sub_result[items_or_slice.value]))
            else:
                result.append(items_or_slice.value)
        
        return result


OF = OptionalFormatter


class OptionalFormatterHandy:
    """
    template_per_item second tuple format:
    [l_delimiter(shown if not first), prefix(shown if first), template, postfix(shown if last), r_delimiter(shown if not last)]


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
                                   hour=('', '|(hours)', '{}', '|', ''),
                                   word=('', '|(word)', '-<"{}"-"{second}">-', '|', ''),
                                   minutes=(':', '|(minutes)', '{}', '|', ''),
                                   seconds=(':', '|(seconds)', '{}', '|', ''),
                                   millisecond=('.', '|(millisecond)', '{}', '|', ''))

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
    def __init__(self, *item_positions: Sequence[str], **template_per_item: Dict[str, Union[IT, Tuple[str, str, str, str, str]]]):
        self.of: OptionalFormatter = OptionalFormatter(item_positions, template_per_item)

    def __call__(self, **arguments_per_item: Dict[str, Union[AK, Any]]) -> str:
        return self.of.__call__(arguments_per_item)
    
    def to_list(self, **arguments_per_item: Dict[str, Union[AK, Any]]) -> List[Union[str, Any]]:
        return self.of.to_list(arguments_per_item)

    def to_joined_list(self, **arguments_per_item: Dict[Hashable, Union[AK, Any]]) -> List[Union[str, Any]]:
        return self.of.to_joined_list(arguments_per_item)

OFH = OptionalFormatterHandy
