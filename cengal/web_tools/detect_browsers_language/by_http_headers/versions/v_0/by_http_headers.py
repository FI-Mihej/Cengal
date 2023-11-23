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


__all__ = ['parse_accept_language', 'normalize_lang_from_parts', 'normalize_lang', 'optimize_accept_language', 
           'match_langs']


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


from cengal.text_processing.text_processing import removeprefix
from cengal.math.numbers import RationalNumber
from collections import OrderedDict
from typing import Mapping, Optional, List, Tuple, OrderedDict, Dict, Set


def parse_accept_language(headers: Mapping) -> Optional[OrderedDict[str, RationalNumber]]:
    accept_language_str = headers.get('Accept-Language'.casefold(), None)
    if accept_language_str is None:
        return None
    
    accept_lang_list = accept_language_str.split(',')
    result_list = list()
    for lang in accept_lang_list:
        lang: str = lang.strip()
        weight: Optional[RationalNumber] = None
        if ';' in lang:
            lang, weight = lang.split(';')
            lang = lang.strip()
            weight = weight.strip()
            weight = removeprefix(weight, 'q=')
            weight = weight.strip()
            try:
                weight = float(weight)
            except ValueError:
                weight = 0
        else:
            weight = 1
        
        result_list.append((lang, weight))
    
    result_list.sort(key=lambda x: x[1], reverse=True)
    return OrderedDict(result_list)


def normalize_lang_from_parts(main_lang: str, sub_lang: Optional[str]) -> str:
    if sub_lang:
        return f'{main_lang}-{sub_lang.upper()}'
    else:
        return main_lang


def normalize_lang(lang: str) -> str:
    if '-' in lang:
        main_lang, sub_lang = lang.split('-')
        main_lang = main_lang.strip()
        sub_lang = sub_lang.strip()
        lang = f'{main_lang}-{sub_lang.upper()}'
    else:
        lang = lang.strip()
    
    return lang


def optimize_accept_language(parsed_accept_language: Optional[OrderedDict[str, RationalNumber]]) -> Optional[OrderedDict[str, RationalNumber]]:
    if parsed_accept_language is None:
        return None
    
    result = OrderedDict()
    for lang, weight in parsed_accept_language.items():
        lang = lang.casefold()
        if '-' in lang:
            main_lang, sub_lang = lang.split('-')
            main_lang = main_lang.strip()
            sub_lang = sub_lang.strip()
            lang = f'{main_lang}-{sub_lang.upper()}'
            result[lang] = weight
            if main_lang in parsed_accept_language:
                pass
            else:
                result[main_lang] = weight
        else:
            result[lang] = weight
    
    return result


def match_langs(default_lang: str, 
                featured_langs: Set[str], 
                supported_langs: Set[str], 
                languages_mapping: Dict[str, str], 
                parsed_accept_language: Optional[OrderedDict[str, RationalNumber]]
                ) -> Tuple[str, OrderedDict[str, RationalNumber], OrderedDict[str, RationalNumber]]:
    better_lang: str = None
    featured_result = OrderedDict()
    result = OrderedDict()
    if parsed_accept_language is not None:
        for lang, weight in parsed_accept_language.items():
            if lang in languages_mapping:
                lang = languages_mapping[lang]
            
            if lang in featured_langs:
                featured_result[lang] = weight
            elif lang in supported_langs:
                result[lang] = weight
            else:
                pass
    
    if featured_result:
        for lang, weight in featured_result.items():
            better_lang = lang
            break
    elif result:
        for lang, weight in result.items():
            better_lang = lang
            break
    else:
        better_lang = default_lang

    return better_lang, featured_result, result
