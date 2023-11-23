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
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


__all__ = ['LowLatencyJSONDecoder', 'LowLatencyJSONEncoder', 'LowLatencyObjectPairsHook', 'original_json_dump', 'original_json_dumps', 'original_json_load', 'original_json_loads']


import json

original_json_dump = json.dump
original_json_dumps = json.dumps
original_json_load = json.load
original_json_loads = json.loads


def dump(*args, **kwargs):
    # You may use
    # ly = None, priority: CoroPriority = CoroPriority.normal
    # as an additional parameters in order to configure LowLatencyJSONEncoder
    
    kwargs['cls'] = LowLatencyJSONEncoder
    return original_json_dump(*args, **kwargs)


def dumps(*args, **kwargs):
    # You may use
    # ly = None, priority: CoroPriority = CoroPriority.normal
    # as an additional parameters in order to configure LowLatencyJSONEncoder
    
    kwargs['cls'] = LowLatencyJSONEncoder
    return original_json_dumps(*args, **kwargs)


def load(*args, **kwargs):
    # You may use
    # ly = None, priority: CoroPriority = CoroPriority.normal
    # as an additional parameters in order to configure LowLatencyJSONEncoder
    
    kwargs['cls'] = LowLatencyJSONDecoder
    kwargs['object_pairs_hook'] = LowLatencyObjectPairsHook(**kwargs)
    return original_json_load(*args, **kwargs)


def loads(*args, **kwargs):
    # You may use
    # ly = None, priority: CoroPriority = CoroPriority.normal
    # as an additional parameters in order to configure LowLatencyJSONEncoder
    
    kwargs['cls'] = LowLatencyJSONDecoder
    kwargs['object_pairs_hook'] = LowLatencyObjectPairsHook(**kwargs)
    return original_json_loads(*args, **kwargs)


# json.dump = dump
# json.dumps = dumps
# json.load = load
# json.loads = loads


def low_latency_json_mock_all():
    json.dump = dump
    json.dumps = dumps
    json.load = load
    json.loads = loads


def low_latency_json_demock_all():
    json.dump = original_json_dump
    json.dumps = original_json_dumps
    json.load = original_json_load
    json.loads = original_json_loads
    

from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import *
from typing import Any, Optional, Callable, Tuple, Dict, List


class LowLatencyJSONDecoder(json.JSONDecoder):
    def __init__(self, *, object_hook: Optional[Callable[[Dict[str, Any]], Any]] = None, parse_float: Optional[Callable[[str], Any]] = None, parse_int: Optional[Callable[[str], Any]] = None, parse_constant: Optional[Callable[[str], Any]] = None, strict: bool = True, object_pairs_hook: Optional[Callable[[List[Tuple[str, Any]]], Any]] = None, ly = None, priority: CoroPriority = CoroPriority.normal) -> None:
        super().__init__(object_hook=object_hook, parse_float=parse_float, parse_int=parse_int, parse_constant=parse_constant, strict=strict, object_pairs_hook=object_pairs_hook)
        self.ly = ly or gly(priority)
        self.ly()


class LowLatencyJSONEncoder(json.JSONEncoder):
    def __init__(self, *, skipkeys: bool = False, ensure_ascii: bool = True, check_circular: bool = True, allow_nan: bool = True, sort_keys: bool = False, indent: Optional[int] = None, separators: Optional[Tuple[str, str]] = None, default: Optional[Callable[..., Any]] = None, ly = None, priority: CoroPriority = CoroPriority.normal) -> None:
        super().__init__(skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan, sort_keys=sort_keys, indent=indent, separators=separators, default=default)
        self._original_iterencode = self.iterencode
        self.iterencode = self._low_latency_iterencode
        self.ly = ly or gly(priority)
        self.ly()
    
    def _low_latency_iterencode(self, *args, **kwargs):
        self.ly()
        return self._original_iterencode(*args, **kwargs)


class LowLatencyObjectPairsHook:
    def __init__(self, ly = None, priority: CoroPriority = CoroPriority.normal, **kwargs) -> None:
        self.ly = ly or gly(priority)
    
    def __call__(self, pairs) -> Any:
        self.ly()
        return dict(pairs)
