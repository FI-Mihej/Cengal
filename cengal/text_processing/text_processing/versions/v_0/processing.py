#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.2.2"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


__all__ = ['Text', 'BinText', 'DEFAULT_ENCODING', 'EncodingRequired', 'NotSupportedDataType', 'NotSupportedDesiredTextType', 'normalize_text', 'normalize_text_to_data', 'find_text', 'replace_slice', 'replace_text', 'normalize_line_separators', 'normalize_line_separators_and_tabs', 'removeprefix', 'removesuffix']


#!/usr/bin/env python
# coding=utf-8



from cengal.system import PYTHON_VERSION
from typing import Optional, Tuple, Union, Type, Callable







Text = Union[bytes, bytearray, str]
BinText = Union[bytes, bytearray]
DEFAULT_ENCODING = 'utf-8'


class EncodingRequired(Exception):
    pass


class NotSupportedDesiredTextType(Exception):
    pass


class NotSupportedDataType(Exception):
    pass


def _default_normalizer(text: Text, desired_type: Type, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Text:
    raise NotImplementedError


def normalize_text(text: Text, desired_type: Type, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Text:
    normalizer = normalizer or _default_normalizer
    
    need_to_use_normalizer = False
    if issubclass(desired_type, bytes):
        if isinstance(text, bytes):
            pass
        elif isinstance(text, bytearray):
            text = bytes(text)
        elif isinstance(text, str):
            if encoding:
                text = text.encode(encoding)
            else:
                raise EncodingRequired
        else:
            need_to_use_normalizer = True
    elif issubclass(desired_type, bytearray):
        if isinstance(text, bytearray):
            pass
        if isinstance(text, bytes):
            text = bytearray(text)
        elif isinstance(text, str):
            if encoding:
                text = bytearray(text, encoding)
            else:
                raise EncodingRequired
        else:
            need_to_use_normalizer = True
    elif issubclass(desired_type, str):
        if isinstance(text, str):
            pass
        if isinstance(text, bytes) or isinstance(text, bytearray):
            if encoding:
                text = text.decode(encoding)
            else:
                raise EncodingRequired
        else:
            need_to_use_normalizer = True
    else:
        need_to_use_normalizer = True
    
    if need_to_use_normalizer:
        text = normalizer(text, desired_type, encoding)

    return text


def normalize_text_to_data(data: Text, text: Text, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Text:
    data_type = type(data)
    if not isinstance(text, data_type):
        text = normalize_text(text, data_type, encoding, normalizer)
    
    return text


def find_text(data: Text, text: Text, start: int = 0, stop: int = -1, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[slice]:
    text = normalize_text_to_data(data, text, encoding, normalizer)
    start = data.find(text, start, stop)
    if -1 == start:
        return None
    
    return slice(start, start + len(text))


def replace_slice(data: Text, place: slice, text: Text, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Tuple[Text, slice]:
    text = normalize_text_to_data(data, text, encoding, normalizer)
    l_text = data[:place.start]
    r_text = data[place.stop:]
    result_text = l_text + text + r_text
    result_place = slice(place.start, place.start + len(text))
    return result_text, result_place


def replace_text(data: Text, old_text: Text, new_text: Text, count: int = -1, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Optional[Text]:
    old_text = normalize_text_to_data(data, old_text, encoding, normalizer)
    new_text = normalize_text_to_data(data, new_text, encoding, normalizer)
    return data.replace(old_text, new_text, count)


def normalize_line_separators(text: Text) -> Text:
    lines = text.splitlines()
    return normalize_text('\n', type(text)).join(lines)


def normalize_line_separators_and_tabs(text: Text, tabsize=4) -> Text:
    text = normalize_line_separators(text)
    return text.expandtabs(tabsize)


def removeprefix(data: Text, prefix: Text, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Text:
    prefix = normalize_text_to_data(data, prefix, encoding, normalizer)
    if (3 == PYTHON_VERSION[0]) and (9 == PYTHON_VERSION[1]):
        return data.removeprefix(prefix)
    else:
        if data.startswith(prefix):
            return data[len(prefix):]
        else:
            return data
        

def removesuffix(data: Text, suffix: Text, encoding: Optional[str] = DEFAULT_ENCODING, normalizer: Optional[Callable] = None) -> Text:
    suffix = normalize_text_to_data(data, suffix, encoding, normalizer)
    if (3 == PYTHON_VERSION[0]) and (9 == PYTHON_VERSION[1]):
        return data.removeprefix(suffix)
    else:
        if data.startswith(suffix):
            return data[:-len(suffix):]
        else:
            return data
