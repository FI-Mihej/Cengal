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


__all__ = ['AggregatorAppendFormatter', 'AggregatorView']


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


from math import ceil
import ttkbootstrap as ttkb
from ttkbootstrap.constants import INSERT as ttkb__INSERT, CURRENT as ttkb__CURRENT, SEL_FIRST as ttkb__SEL_FIRST, SEL_LAST as ttkb__SEL_LAST, SEL as ttkb__SEL, END as ttkb__END
from ttkbootstrap import Style
from typing import Callable, Hashable, Optional, Tuple, Any

from cengal.parallel_execution.coroutines.coro_standard_services.tkinter import *
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.fast_aggregator import *
from cengal.user_interface.gui.tkinter.components.read_only_text import *


class AggregatorAppendFormatter:
    def __init__(self, initial_text: str) -> None:
        self.initial_text: str = initial_text
        self._items_num: int = 0
        self.initiated: bool = False
    
    def reset(self):
        self._items_num = 0
        self.initiated = False
    
    def __call__(self, data: Any) -> Any:
        self._items_num += 1
        
        if self.initiated:
            return f'{data}'
        else:
            self.initiated = True
            return f'{current_interface().coro_id}. {self.initial_text}:\n{data}'


class AggregatorView(ttkb.Frame):
    def __init__(self, append_data: bool, default_auto_scroll: bool, aggregator_key: Hashable, updating_interval: float, data_formatter_func: Optional[Callable], width, height, *args, **kwargs):
        self.append_data: bool = append_data
        self.updating_interval: float = updating_interval
        self.aggregator_key: Hashable = aggregator_key
        self._default_data_formatter_func: Callable = lambda x: f'{x}'
        self.data_formatter_func: Optional[Callable] = data_formatter_func or self._default_data_formatter_func
        self._stop: bool = False
        self.updates_num: int = 0
        self.max_len: int = None
        super().__init__(*args, **kwargs)

        text_area_config = {
            'highlightcolor': Style.instance.colors.primary,
            'highlightbackground': Style.instance.colors.border,
            'highlightthickness': 1,
            'wrap': 'none',
        }
        if width is not None:
            text_area_config.update({
                'width': width,
            })
        
        if height is not None:
            text_area_config.update({
                'height': height,
            })
        
        self.text_area = ReadOnlyText(self, **text_area_config)
        self.text_area.pack(fill='both', expand='yes')

        self.text_area._text['yscrollcommand'] = self.yscroll
        self.text_area._vbar.config(command=self.yview)
        self.auto_scroll: bool = default_auto_scroll
        self.last_yscroll: Tuple[str, str] = None
        self.last_lines_num: int = None
        self.last_yview: Tuple[str] = None
        self.last_line: int = 0
        self.desired_line: int = 0
        self.selection_started = False
        self.selection_first = None
        self.selection_last = None
        self.selection = None
        self.previously_was_mouse_b1_double = False
        
        self.text_area._text.bind("<Button-3>", self.mouse_b3_down)
        if not append_data:
            self.text_area._text.bind("<<Selection>>", self.selection_changed)
            self.text_area._text.bind("<Double-Button-1>", self.mouse_b1_double)
            self.text_area._text.bind("<Button-1>", self.mouse_b1_down)
            self.text_area._text.bind("<B1-Motion>", self.mouse_b1_motion)
            self.text_area._text.bind("<ButtonRelease-1>", self.mouse_b1_up)
            self.text_area._text.bind("<Control-a>", self.ctrl_a)

    def ctrl_a(self, event):
        self.clear_selection()
        self.selection_first = self.text_area._text.index('@%s,%s' % (1, 0))
        self.selection_last = 'end'
        self.selection = (self.selection_first, self.selection_last)
        self.apply_selection()
        
        self.text_area._text.tag_remove(ttkb__INSERT, '1.0', 'end')
        self.text_area._text.tag_add(ttkb__INSERT, self.selection_last)
        self.text_area._text.mark_unset(ttkb__INSERT)
        self.text_area._text.mark_set(ttkb__INSERT, self.selection_last)
        return 'break'

    def clear_selection(self):
        self.text_area._text.tag_remove(ttkb__SEL, '1.0', 'end')
    
    def normalize_selection(self):
        if self.selection is not None:
            if 'end' == self.selection[0]:
                self.selection = (self.selection[1], self.selection[0])
            elif 'end' == self.selection[1]:
                pass
            else:
                sel_left = [int(x) for x in self.selection[0].split('.')]
                sel_right = [int(x) for x in self.selection[1].split('.')]
                if sel_left > sel_right:
                    self.selection = (self.selection[1], self.selection[0])
    
    def apply_selection(self):
        if self.selection is not None:
            if self.selection[0] == self.selection[1]:
                return
            
            self.normalize_selection()
            self.text_area._text.tag_remove(ttkb__SEL, '1.0', 'end')
            self.text_area._text.tag_add(ttkb__SEL, *self.selection)

    def mouse_b1_down(self, event):
        self.previously_was_mouse_b1_double = False
        self.selection_first = self.text_area._text.index('@%s,%s' % (event.x, event.y))
        self.selection_last = None
        self.clear_selection()

    def mouse_b1_up(self, event):
        selection_last = self.text_area._text.index('@%s,%s' % (event.x, event.y))
        if self.selection_first is not None:
            if self.selection_last is None:
                if self.selection_first != selection_last:
                    self.selection = (self.selection_first, selection_last)
                    self.apply_selection()
                    self.selection_first = None
                else:
                    self.selection = None
            else:
                self.selection = (self.selection_first, self.selection_last)
                self.apply_selection()
        
        self.text_area._text.tag_remove(ttkb__INSERT, '1.0', 'end')
        self.text_area._text.tag_add(ttkb__INSERT, selection_last)
        self.text_area._text.mark_unset(ttkb__INSERT)
        self.text_area._text.mark_set(ttkb__INSERT, selection_last)
        return 'break'

    def mouse_b1_motion(self, event):
        selection_last = self.text_area._text.index('@%s,%s' % (event.x, event.y))
        if self.selection_first is not None:
            self.selection = (self.selection_first, selection_last)
            self.apply_selection()
        
        return 'break'
    
    def mouse_b1_double(self, event):
        if self.previously_was_mouse_b1_double:
            self.selection_first = self.text_area._text.index('@%s,%s linestart' % (event.x, event.y))
            self.selection_last = self.text_area._text.index('@%s,%s lineend' % (event.x, event.y))
            self.selection = (self.selection_first, self.selection_last)
            self.apply_selection()
            self.previously_was_mouse_b1_double = False
        else:
            self.selection_first = self.text_area._text.index('@%s,%s wordstart' % (event.x, event.y))
            self.selection_last = self.text_area._text.index('@%s,%s wordend' % (event.x, event.y))
            self.selection = (self.selection_first, self.selection_last)
            self.apply_selection()
            self.previously_was_mouse_b1_double = True
        
        return 'break'

    def mouse_b3_down(self, event):
        self.text_area._text.mark_unset(ttkb__INSERT)
        selection = None
        if self.selection is not None:
            self.normalize_selection()
            selection = self.selection
        else:
            current_selection = self.text_area._text.index(ttkb__SEL)
            current_selection_first = self.text_area._text.index(ttkb__SEL_FIRST)
            current_selection_last = self.text_area._text.index(ttkb__SEL_LAST)
            if current_selection_first and current_selection_last:
                selection = (current_selection_first, current_selection_last)

        if selection is not None:
            self.text_area._text.clipboard_clear()
            text_content = self.text_area._text.get(selection[0], selection[1])
            self.text_area._text.clipboard_append(text_content)
            self.selection_last = None
            self.selection = None
            self.previously_was_mouse_b1_double = False
            self.clear_selection()
    
    def selection_changed(self, event):
        return

    def put(self, text: str):
        lines_num_before = self.index_to_line_number(self.text_area._text.index('end'))
        view_fractions_before = self.text_area._text.yview()
        line_before = int(ceil(lines_num_before * float(view_fractions_before[0])))
        tag_insert_before = self.text_area._text.index(ttkb__INSERT)
        tag_current_before = self.text_area._text.index(ttkb__CURRENT)
        
        if not self.append_data:
            self.clear_context()
        
        self.text_area._text.insert('end', text)
        
        if self.auto_scroll:
            self.text_area._text.yview(ttkb__END)

        if not self.append_data:
            self.text_area._text.tag_remove(ttkb__INSERT, '1.0', 'end')
            self.text_area._text.tag_add(ttkb__INSERT, tag_insert_before)
            self.text_area._text.tag_remove(ttkb__CURRENT, '1.0', 'end')
            self.text_area._text.tag_add(ttkb__CURRENT, tag_current_before)
            self.text_area._text.mark_unset(ttkb__INSERT)
            self.text_area._text.mark_set(ttkb__INSERT, tag_insert_before)
            self.apply_selection()
            
            lines_num_after = self.index_to_line_number(self.text_area._text.index('end'))
            view_fractions_after = self.text_area._text.yview()
            line_after = int(ceil(lines_num_after * float(view_fractions_after[0])))
            
            line_before = line_before or 1
            line_after = line_after or 1
            if line_after != line_before:
                movement = line_before - line_after
                self.text_area._text.yview_scroll(movement, 'units')
    
    def index_to_line_number(self, index: str):
        return int(index.split('.')[0])

    def clear_context(self):
        self.text_area._text.delete('1.0', 'end')

    def yscroll(self, *args):
        first, last = args
        lines_num = self.index_to_line_number(self.text_area._text.index('end')) - 1
        last_line_index = lines_num - 1
        first_visible_line_index = int(ceil(lines_num * float(first)))
        last_visible_line_index = int(ceil(lines_num * float(last))) - 1

        if self.auto_scroll:
            if (0 < first_visible_line_index) and (last_visible_line_index < last_line_index):
                self.auto_scroll = False
        else:
            if (0 <= last_line_index) and (0 <= last_visible_line_index) and (0 < first_visible_line_index) and (last_visible_line_index >= first_visible_line_index) and (last_visible_line_index == last_line_index):
                self.auto_scroll = True
        
        self.text_area._vbar.set(*args)

    def yview(self, *args):
        self.text_area._text.yview(*args)
    
    def start(self, wr: TkObjWrapper):
        wr.put_coro(self._updater)
    
    def stop(self):
        self._stop = True
    
    def _updater(self, i: Interface):
        while not self._stop:
            try:
                self.updates_num += 1
                if (self.max_len is not None) and (self.updates_num >= self.max_len):
                    if isinstance(self.data_formatter_func, AggregatorAppendFormatter):
                        self.updates_num = 1
                        self.data_formatter_func.reset()
                        auto_scroll_buff = self.auto_scroll
                        self.clear_context()
                        self.auto_scroll = auto_scroll_buff
                    
                data = i(FastAggregator, self.aggregator_key)
                if self.append_data:
                    text = '\n'.join([self.data_formatter_func(item) for item in data]) + '\n'
                else:
                    text = self.data_formatter_func(data[-1])
                    
                self.put(text)
            except KeyError:
                pass

            i(Sleep, self.updating_interval)
