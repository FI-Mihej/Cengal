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

from cengal.time_management.repeat_for_a_time import BaseTracer, GreedyTracer
from cengal.time_management.load_best_timer import perf_counter
from enum import Enum
from typing import Tuple

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


class ViewIndicator:
    def __init__(self):
        self._view_set = ('-', '\\', '|', '/')
        self._view_set_size = len(self._view_set)
        self._counter = 0

    def __call__(self):
        result = self._view_set[self._counter]
        self._counter += 1
        if self._counter >= self._view_set_size:
            self._counter = 0
        return result

    @property
    def view_set(self):
        return self._view_set

    @view_set.setter
    def view_set(self, view_set: Tuple):
        self._view_set = view_set
        self._view_set_size = len(self._view_set)
        self._counter = 0


class ProgressOutType(Enum):
    none = 0
    short = 1
    full = 2


class ProgressMeter:
    """
    Example of use:
        pm = ProgressMeter(0.1, 'files')
        while True:
            ...
            pm(ProgressOutType.short)
        pm(ProgressOutType.full, force_print=True, erasable=False)

    """

    def __init__(self, update_time: float=1.0, _items_readable_name: str='iterations'
                 , default_indicator: ViewIndicator=None
                 , default_tracer: BaseTracer=GreedyTracer):
        self._update_time = update_time
        self._items_readable_name = _items_readable_name
        self._last_iterations_per_second = 0.0
        self.template_short = '  {indicator}'
        self.template_full = '  {indicator} ## {items_count} ## {items_readable_name} per second: ' \
                             '{iterations_per_second}'
        self._view_indicator = default_indicator or ViewIndicator()
        self._default_tracer = default_tracer
        self._tracer = self._default_tracer(self._update_time)
        self._iterations = 0
        self._start_time = 0.0
        self._last_tracked_time = 0.0
        self._is_first_call = True

    def __call__(self, output_type: ProgressOutType=ProgressOutType.full,
                 force_print: bool=False, erasable: bool=True) -> bool:
        self._iterations += 1
        if self._is_first_call:
            self._is_first_call = False
            self._start_time = perf_counter()
        result = not self._tracer.iter()
        if result or force_print:
            self._last_tracked_time = perf_counter()
            time_delta = self._last_tracked_time - self._start_time
            if time_delta != 0.0:
                self._last_iterations_per_second = self._iterations / time_delta
            self.print(output_type, erasable)
            self._tracer = self._default_tracer(self._update_time)
        return result
    
    def print(self, output_type: ProgressOutType=ProgressOutType.full, erasable: bool=True):
        out_message = None
        if ProgressOutType.full == output_type:
            out_message = self.template_full.format(indicator=self._view_indicator(),
                                                    items_count=self._iterations,
                                                    items_readable_name=self._items_readable_name,
                                                    iterations_per_second=self._last_iterations_per_second)
        elif ProgressOutType.short == output_type:
            out_message = self.template_short.format(indicator=self._view_indicator())

        if out_message is not None:
            if erasable:
                print(out_message, end='\r', flush=True)
            else:
                print(out_message, flush=True)

    @property
    def iterations_per_second(self):
        return self._last_iterations_per_second
