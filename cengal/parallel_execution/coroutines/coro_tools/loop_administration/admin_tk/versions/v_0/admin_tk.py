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


__all__ = ['start_admin', 'cs_init']


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.2.5"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from time import perf_counter
import ttkbootstrap as ttkb
from ttkbootstrap.scrolled import ScrolledText as TtkbScrolledText
from tkinter import simpledialog
from ttkbootstrap import Style
from pprintpp import pformat as pf
from typing import Callable, Hashable, Optional, Set, Dict, Tuple, Union, List, Sequence, Any, cast

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.tkinter import *
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro, PutCoroRequest
from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.simple_yield import Yield
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import AsyncioLoopRequest
from cengal.parallel_execution.coroutines.coro_standard_services.fast_aggregator import *
from cengal.parallel_execution.coroutines.coro_tools.coro_flow_control import graceful_coro_destroyer, GracefulCoroDestroy
from cengal.statistics.normal_distribution import average
from cengal.parallel_execution.multiprocess.multiprocessing_task_runner import *
from cengal.text_processing.text_processing import normalize_line_separators_and_tabs
from cengal.introspection.inspect import get_exception, exception_to_printable_text
from cengal.system import OS_TYPE
from cengal.data_manipulation.dict_path import *
from cengal.user_interface.gui.tkinter.components.read_only_text import *
from cengal.user_interface.gui.tkinter.components.tool_tip import *
from cengal.user_interface.gui.tkinter.components.aggregator_view import *
from greenlet import GreenletExit


command_executor_aggregator_view_key = 'command_executor_aggregator'
command_executor_aggregator_append_view_key = 'command_executor_aggregator_append'

coro_holder_header = 'async def coro_holder(i: Interface, fac: FastAggregatorClient, aggregator_key, aggregator_append_key):'
coro_holder_template = f'''from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro_list import *
from cengal.parallel_execution.coroutines.coro_standard_services.kill_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.kill_coro_list import *
from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import *
from cengal.parallel_execution.coroutines.coro_standard_services.throw_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.throw_coro_list import *
from cengal.parallel_execution.coroutines.coro_standard_services.wait_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_loop import *
from cengal.parallel_execution.coroutines.coro_standard_services.fast_aggregator import *
from cengal.parallel_execution.coroutines.coro_tools.coro_flow_control import graceful_coro_destroyer, GracefulCoroDestroy
import asyncio


{coro_holder_header}
{{coro_body}}


result = i(RunCoro, coro_holder, FastAggregatorClient(), aggregator_key, aggregator_append_key)
'''


def prepare_coro_body(text: str) -> str:
    if (not text) or ('\n' == text):
        text = 'pass'
    
    text = normalize_line_separators_and_tabs(text)
    text_lines = text.splitlines()
    return '\n'.join([' ' * 4 + line for line in text_lines])


class CommandExecutor(ttkb.Frame):
    def __init__(self, width, height, allow_asyncio: bool = True, priority: Optional[CoroPriority] = None, interrupt_when_no_requests: Optional[bool] = None, *args, **kwargs) -> None:
        self.width = width
        self.height = height
        self.allow_asyncio = allow_asyncio
        self.priority = priority
        self.interrupt_when_no_requests = interrupt_when_no_requests
        self.current_coro_id: CoroID = None
        if allow_asyncio:
            i = current_interface()
            i(AsyncioLoopRequest().ensure_loop(interrupt_when_no_requests=interrupt_when_no_requests, priority=priority))
            i(AsyncioLoopRequest().turn_on_loops_intercommunication())

        super().__init__(*args, **kwargs)
        text_area_config = {
            'highlightcolor': Style.instance.colors.primary,
            'highlightbackground': Style.instance.colors.border,
            'highlightthickness': 1,
            'wrap': 'none',
        }
        if width is not None:
            text_area_config.update({
                'width': (width - 20) >> 1,
            })
        
        if height is not None:
            text_area_config.update({
                'height': height,
            })
        
        self.text_in_area = TtkbScrolledText(self, **text_area_config)

        if 'Darwin' == OS_TYPE:
            self.control_key_name = 'Cmd'
        else:
            self.control_key_name = 'Ctrl'

        self.buttons_frame = ttkb.Frame(self)
        self.run_button_text = '>>'
        self.run_button_width = len(self.run_button_text) + 1
        self.run_button = ttkb.Button(self.buttons_frame, text=self.run_button_text, width=self.run_button_width, command=self.run)
        self.run_button_tooltip = ToolTipHovered(self.run_button, f'<{self.control_key_name}+Enter> Run and clear input field. Prevents human missclicks')

        self.run_button_2_text = 'R>'
        self.run_button_2_width = len(self.run_button_2_text) + 1
        self.run_button_2 = ttkb.Button(self.buttons_frame, text=self.run_button_2_text, width=self.run_button_2_width, command=self.run_2)
        self.run_button_2_tooltip = ToolTipHovered(self.run_button_2, f'<{self.control_key_name}+Alt+Enter> Run')

        self.stop_button_text = 'X'
        self.stop_button_width = len(self.stop_button_text) + 1
        self.stop_button = ttkb.Button(self.buttons_frame, text=self.stop_button_text, width=self.stop_button_width, command=self.kill)
        self.stop_button['state'] = 'disabled'
        self.stop_button_tooltip = ToolTipHovered(self.stop_button, f'<{self.control_key_name}+x> Stop execution')

        self.text_out_area = ReadOnlyText(self, **text_area_config)


        self.func_header_read_only = ttkb.Label(self, text=coro_holder_header, font=('Helvetica', 8, 'bold'))
        self.func_header_read_only.pack(fill='x', expand='yes', side='top')

        self.text_in_area.pack(fill='both', side='left')
        self.run_button.pack(fill='both', side='top', pady=1)
        self.run_button_2.pack(fill='both', side='top', pady=1)
        self.stop_button.pack(fill='both', side='top', pady=1)
        self.buttons_frame.pack(fill='both', side='left')
        self.text_out_area.pack(fill='both', expand='yes', side='left')

        self.text_in_area._text.bind("<Control-Return>", self.ctrl_enter)
        self.text_in_area._text.bind("<Control-Alt-Return>", self.ctrl_alt_enter)
        self.text_in_area._text.bind("<Control-x>", self.ctrl_x)

    def ctrl_enter(self, event):
        self.run()
        return 'break'

    def ctrl_alt_enter(self, event):
        self.run_2()
        return 'break'

    def ctrl_x(self, event):
        self.kill()
        return 'break'

    def run(self, clear_input: bool = True):
        text = self.text_in_area._text.get('1.0', 'end')
        if clear_input:
            self.text_in_area._text.delete('1.0', 'end')
        
        self.text_out_area._text.insert('end', text)
        
        # disable the intput
        self.run_button['text'] = '...'
        self.run_button_width = len(self.run_button['text']) + 1
        self.run_button['state'] = 'disabled'
        self.run_button_2['text'] = '...'
        self.run_button_2_width = len(self.run_button_2['text']) + 1
        self.run_button_2['state'] = 'disabled'
        self.stop_button['state'] = 'normal'
        self.text_in_area._text['state'] = 'disabled'
        self.text_in_area.state(["disabled"])
        
        self.current_coro_id = current_interface()(PutCoro, self.eval_text, text)
    
    def run_2(self):
        return self.run(clear_input = False)

    def kill(self):
        if self.current_coro_id is not None:
            graceful_coro_destroyer(current_interface(), None, self.current_coro_id, first_phase_is_wait=False)
            self.current_coro_id = None
            self.run_button['text'] = self.run_button_text
            self.run_button_width = self.run_button_width
            self.run_button['state'] = 'normal'
            self.run_button_2['text'] = self.run_button_2_text
            self.run_button_2_width = self.run_button_2_width
            self.run_button_2['state'] = 'normal'
            self.stop_button['state'] = 'disabled'
            self.text_in_area._text['state'] = 'normal'
            self.text_in_area.state(["!disabled"])
    
    def eval_text(self, i: Interface, text):
        self.text_out_area._text.delete('1.0', 'end')

        # evalueate the text
        try:
            result = None
            local_vars = {
                'i': i,
                'result': result,
                'aggregator_key': command_executor_aggregator_view_key,
                'aggregator_append_key': command_executor_aggregator_append_view_key,
            }
            text = coro_holder_template.format(coro_body=prepare_coro_body(text))
            exec(text, local_vars)
            self.text_out_area._text.insert('1.0', f'{local_vars["result"]}')
        except GracefulCoroDestroy as ex:
            # self.text_out_area._text.insert('1.0', f'{type(ex)}')
            pass
        except GreenletExit as ex:
            # self.text_out_area._text.insert('1.0', f'{type(ex)}')
            pass
        except:
            self.text_out_area._text.insert('1.0', f'{exception_to_printable_text(get_exception())}')
        finally:
            # enable the intput
            self.run_button['text'] = self.run_button_text
            self.run_button_width = len(self.run_button['text']) + 1
            self.run_button['state'] = 'normal'
            self.run_button_2['text'] = self.run_button_2_text
            self.run_button_2_width = len(self.run_button_2['text']) + 1
            self.run_button_2['state'] = 'normal'
            self.stop_button['state'] = 'disabled'
            self.text_in_area._text['state'] = 'normal'
            self.text_in_area.state(["!disabled"])


class CSStatsFormatterMultiprocess:
    def __init__(self, filtered_paths: List[Sequence[str]] = None):
        self.filtered_paths: List[Sequence[str]] = [
            ['CoroSchedulerBase', 'loop', 'coroutines execution times'],
            ['CoroSchedulerBase', 'loop', 'longest continuous execution time of coroutines'],
            ['CoroSchedulerGreenlet', 'loop', 'coroutines execution times'],
            ['CoroSchedulerGreenlet', 'loop', 'longest continuous execution time of coroutines'],
            ['CoroSchedulerAwaitable', 'loop', 'coroutines execution times'],
            ['CoroSchedulerAwaitable', 'loop', 'longest continuous execution time of coroutines'],
        ] if filtered_paths is None else filtered_paths
        self._stop: bool = False
        self._subprocess_started: bool = False
        settings = SubprocessWorkerSettings()
        settings.initiation_function = self.process_initializer
        settings.working_function = self.process_worker
        settings.transport = Transport.queue
        settings.sendable_data_type = SendableDataType.marshalable
        settings.use_internal_subprocess_input_buffer = True
        settings.initialization_data = {
            'filtered_paths': self.filtered_paths
        }
        
        self.worker = SubprocessWorker(settings)
    
    def start(self, wr: TkObjWrapper):
        self.worker.start()
        wr.put_coro(self.start_and_wait_for_subprocess)
    
    def stop(self):
        self._stop = True
        self.worker.stop()
    
    async def start_and_wait_for_subprocess(self, i: Interface):
        self.worker.send_data_to_subprocess({
            'type': 'init',
            'data': None,
        })
        got_result = False
        while (not got_result) and (not self._stop):
            try:
                result = self.worker.get_answer_from_subprocess(block_queue=False, time_out=0.1)
            except Empty:
                pass
            else:
                got_result = True
            
            if not got_result:
                await i(Sleep, 0.01)
        
        self._subprocess_started = True
    
    def update_filtered_paths(self, filtered_paths: List[Sequence[str]]):
        i: Interface = current_interface()
        self.filtered_paths = filtered_paths
        self.worker.send_data_to_subprocess({
            'type': 'filter',
            'data': self.filtered_paths
        })
    
    def __call__(self, data):
        if not self._subprocess_started:
            # return data
            return '<<Waiting for subprocess to start...>>'
        
        i: Interface = current_interface()
        self.worker.send_data_to_subprocess({
            'type': 'data',
            'data': data
        })
        result = None
        got_result = False
        while (not got_result) and (not self._stop):
            try:
                result = self.worker.get_answer_from_subprocess(block_queue=False, time_out=0.1)
            except Empty:
                pass
            else:
                got_result = True
            
            if got_result:
                if 'data' != result['type']:
                    got_result = False
            
            if not got_result:
                i(Sleep, 0.01)
        
        result = result['data']
        result = f'{i.coro_id}. CoroScheduler stats:\n{result}'
        return result
    
    @staticmethod
    def process_initializer(init_data) -> Any:
        from pprintpp import pformat as pf
        return init_data
    
    @staticmethod
    def process_worker(global_data, data_msg):
        data = data_msg['data']
        if 'init' == data_msg['type']:
            pass
        elif 'filter' == data_msg['type']:
            if global_data is None:
                global_data = dict()
            
            global_data['filtered_paths'] = data
        elif 'data' == data_msg['type']:
            filtered_paths = global_data['filtered_paths']
            for path in filtered_paths:
                try_del_dict_item(data, path)
            
            data = pf(data, indent=4, width=120)

        data_msg['data'] = data
        return data_msg


class CorosMaxExecutionTimesProvider:
    def __init__(self, lifetime_stats_key: Hashable, stats_key: Hashable, period: float):
        self.lifetime_stats_key: Hashable = lifetime_stats_key
        self.stats_key: Hashable = stats_key
        self.period: float = period
        self.i: Interface = None
        self.fac = FastAggregatorClient()
        self._stop = False
        self.lifetime_stats: Dict[CoroID, float] = dict()
    
    def start(self):
        if self.i is None:
            self.i = current_interface()
        
        self.i(PutCoro, self._update)
    
    def stop(self):
        self._stop = True
    
    async def _update(self, i: Interface):
        while not self._stop:
            data = copy(i._loop.coro_longest_execution_time)
            new_coro_longest_execution_time = dict()
            for key, value in data.items():
                new_coro_longest_execution_time[key] = 0.0
                
                if key not in self.lifetime_stats:
                    self.lifetime_stats[key] = 0.0
                    
                self.lifetime_stats[key] = max(self.lifetime_stats[key], value)
            
            i._loop.coro_longest_execution_time = new_coro_longest_execution_time
            self.fac(self.lifetime_stats_key, self.lifetime_stats)
            self.fac(self.stats_key, data)
            await i(Sleep, self.period)
    
    def _formatter(self, title: str, data):
        i: Interface = current_interface()
        return f'{i.coro_id}. {title}:\n' + '\n'.join([f'{coro_id}: {value * 1000}' for coro_id, value in data.items()])
    
    def stats_formatter(self, data):
        return self._formatter('Coros Max Execution Times', data)
    
    def lifetime_stats_formatter(self, data):
        return self._formatter('Coros Lifetime Max Execution Times', data)


class SchedulerPerformanceFormatter:
    def __init__(self, external_items_key: Hashable, internal_items_key: Hashable, lifetime_stats_key: Hashable, stats_key: Hashable, window_size: int):
        self.external_items_key: Hashable = external_items_key
        self.internal_items_key: Hashable = internal_items_key
        self.lifetime_stats_key: Hashable = lifetime_stats_key
        self.stats_key: Hashable = stats_key
        self.window_size: int = window_size
        self.fac = FastAggregatorClient()
        self.i: Interface = None
        self.data_window: List = list()
        self.max_deviation: float = None
        self.min_deviation: float = None
        self.max_iter_per_sec: float = None
        self.min_iter_per_sec: float = None
        self._stop: bool = False

        settings = SubprocessWorkerSettings()
        settings.initiation_function = self.process_initializer
        settings.working_function = self.process_worker
        settings.transport = Transport.queue
        settings.sendable_data_type = SendableDataType.marshalable
        self.worker = SubprocessWorker(settings)
        self.worker.start()
    
    def start(self, wr: Optional[TkObjWrapper] = None):
        if self.i is None:
            self.i = current_interface()
        
        if wr:
            wr.put_coro(self._update)
            wr.put_coro(self._update_stats)
        else:
            self.i(PutCoro, self._update)
            self.i(PutCoro, self._update_stats)
    
    def stop(self):
        self._stop = True
    
    def _update(self, i: Interface):
        while not self._stop:
            start = perf_counter()
            i(Yield)
            stop = perf_counter()
            self.fac(self.external_items_key, stop - start)
            self.fac(self.internal_items_key, stop - start)

    def _update_stats(self, i: Interface):
        while not self._stop:
            try:
                data = i(FastAggregator, self.internal_items_key)
                if len(data) >= self.window_size:
                    self.data_window = data[-self.window_size:]
                else:
                    additional_data_len = self.window_size - len(data)
                    if len(self.data_window) >= additional_data_len:
                        self.data_window = self.data_window[-additional_data_len:] + data
                    else:
                        self.data_window.extend(data)
                
                iter_per_sec, val_99, val_95, val_68, max_deviation, min_deviation = self.compute_stats(i, self.data_window)
                if self.max_deviation is None:
                    self.max_deviation = max_deviation
                else:
                    self.max_deviation = max(self.max_deviation, max_deviation)
                
                if self.min_deviation is None:
                    self.min_deviation = min_deviation
                else:
                    self.min_deviation = min(self.min_deviation, min_deviation)
                
                if self.max_iter_per_sec is None:
                    self.max_iter_per_sec = iter_per_sec
                else:
                    self.max_iter_per_sec = max(self.max_iter_per_sec, iter_per_sec)
                
                if self.min_iter_per_sec is None:
                    self.min_iter_per_sec = iter_per_sec
                else:
                    self.min_iter_per_sec = min(self.min_iter_per_sec, iter_per_sec)
                
                self.fac(self.stats_key, (iter_per_sec, val_99, val_95, val_68, max_deviation, min_deviation))
                self.fac(self.lifetime_stats_key, (self.max_iter_per_sec, self.min_iter_per_sec, self.max_deviation, self.min_deviation))
                
                self.window_size = 2 * int(round(iter_per_sec))
            except KeyError:
                pass
            
            i(Sleep, 0.2)
    
    def compute_stats(self, i: Interface, data):
        self.worker.send_data_to_subprocess(data)
        result = None
        got_result = False
        while not got_result:
            try:
                result = self.worker.get_answer_from_subprocess(block_queue=False, time_out=0.1)
            except Empty:
                pass
            else:
                got_result = True
            
            if not got_result:
                i(Sleep, 0.005)
            
        return result
    
    @staticmethod
    def process_initializer(init_data):
        pass
    
    @staticmethod
    def process_worker(global_data, data):
        from cengal.statistics.normal_distribution import count_99_95_68
        val_99, val_95, val_68, max_deviation, min_deviation = count_99_95_68(data)
        iter_per_sec = 1 / average(data)
        return (iter_per_sec, val_99, val_95, val_68, max_deviation, min_deviation)
        
    @staticmethod
    def item_formatter(data) -> str:
        return f'{data}'
        
    @staticmethod
    def stats_formatter(data) -> str:
        i: Interface = current_interface()
        iter_per_sec, val_99, val_95, val_68, max_deviation, min_deviation = data
        return f'{i.coro_id}. Stats:\niter_per_sec: {iter_per_sec}\nval_99: {val_99}\nval_95: {val_95}\nval_68: {val_68}\nmax_deviation: {max_deviation}\nmin_deviation: {min_deviation}'
        
    @staticmethod
    def lifetime_stats_formatter(data) -> str:
        i: Interface = current_interface()
        max_iter_per_sec, min_iter_per_sec, max_deviation, min_deviation = data
        return f'{i.coro_id}. Lifetime Stats:\nmax_iter_per_sec: {max_iter_per_sec}\nmin_iter_per_sec: {min_iter_per_sec}\nmax_deviation: {max_deviation}\nmin_deviation: {min_deviation}'


class HelpDialog(simpledialog.Dialog):
    def body(self, master):
        self.title('Console Description and Help')

        text_area_config = {
            'highlightcolor': Style.instance.colors.primary,
            'highlightbackground': Style.instance.colors.border,
            'highlightthickness': 1,
            'wrap': 'none',
            'width': 120,
            'height': 30,
        }

        self.text_area = ReadOnlyText(self, **text_area_config)
        self.text_area.pack(fill='both', expand='yes')
        self.text_area._text.delete('1.0', 'end')
        self.text_area._text.insert('end', coro_holder_template)
        
        return self.text_area  # initial focus


class FilterSetupDialog(ttkb.Toplevel):
    def __init__(self, parent, filtered_paths):
        # position is centered to parent
        parent_pos_left, parent_pos_top = parent.winfo_x(), parent.winfo_y()
        parent_size_x, parent_size_y = parent.winfo_width(), parent.winfo_height()
        own_size_x, own_size_y = 600, 400
        own_pos_x = parent_pos_left + (parent_size_x - own_size_x) // 2
        own_pos_y = parent_pos_top + (parent_size_y - own_size_y) // 2
        super().__init__(parent, size=(own_size_x, own_size_y), resizable=(True, True), position=(own_pos_x, own_pos_y))
        self.filtered_paths = filtered_paths
        self.title('Filtered paths setup')
        self.transient(parent)
        self.result = None

        ttkb.Label(self, text="Enter your text:").pack(fill=None, expand='no', side='top')
        self.text_entry = TtkbScrolledText(self, width=30, height=10)
        self.text_entry.pack(fill='both', expand='yes', side='top')

        button_frame = ttkb.Frame(self)
        button_frame.pack(fill='x', expand='no', side='right')

        ttkb.Button(button_frame, text='OK', command=self.ok).pack(side=ttkb.LEFT, padx=1)
        ttkb.Button(button_frame, text='Cancel', command=self.cancel).pack(side=ttkb.LEFT, padx=1)

        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.text_entry.focus_set()
        filtered_paths_list = list()
        for path in self.filtered_paths:
            filtered_paths_list.append(dict_path_to_str(path))
        
        filtered_paths_text = '\n'.join(filtered_paths_list) + '\n'
        self.text_entry._text.insert('1.0', filtered_paths_text)

        self.text_entry._text.bind("<Control-Return>", self.ctrl_enter)
        self.text_entry._text.bind("<Escape>", self.escape)
        self.text_entry._text.focus_set()

    def ctrl_enter(self, event):
        self.ok(event)
        return 'break'

    def escape(self, event):
        self.cancel(event)
        return 'break'

    def ok(self, event=None):
        filtered_paths_text = self.text_entry.get('1.0', 'end-1c')
        result_lines = filtered_paths_text.split('\n')
        filtered_paths = list()
        for line in result_lines:
            if line:
                filtered_paths.append(srt_to_dict_path(line))
        
        self.result = filtered_paths
        self.destroy()

    def cancel(self, event=None):
        self.result = self.filtered_paths
        self.destroy()


# class Application(Tk):
class Application(ttkb.Window):
    def __init__(self, style: str = 'superhero', filtered_paths: List[List[str]] = None):
        super().__init__()
        self.style_name = style
        Style(style)
        self.filtered_paths: List[Sequence[str]] = filtered_paths

        self.title('CoroScheduler Admin')
        self.resizable(width=True, height=True)

        self.sfmp = CSStatsFormatterMultiprocess(self.filtered_paths)
        
        self.scheduler_stats_frame = ttkb.Frame(self)
        self.scheduler_stats_control_frame = ttkb.Frame(self.scheduler_stats_frame)
        self.scheduler_stats_format_button_text = 'F'
        self.scheduler_stats_format_button_text_len = len('F') + 1
        self.scheduler_stats_format_button = ttkb.Button(self.scheduler_stats_control_frame, text=self.scheduler_stats_format_button_text, width=self.scheduler_stats_format_button_text_len, command=self.scheduler_stats_format_button_on_click)
        self.scheduler_stats_format_button_tooltip = ToolTipHovered(self.scheduler_stats_format_button, 'Filter our unnecessary or flickering paths')
        self.scheduler_stats_help_button_text = '?'
        self.scheduler_stats_help_button_text_len = len('?') + 1
        self.scheduler_stats_help_button = ttkb.Button(self.scheduler_stats_control_frame, text=self.scheduler_stats_help_button_text, width=self.scheduler_stats_help_button_text_len, bootstyle="info", command=self.scheduler_stats_help_button_on_click)
        self.scheduler_stats_help_button_tooltip = ToolTipHovered(self.scheduler_stats_help_button, 'Console description and help')
        self.scheduler_stats_format_button.pack(fill=None, expand='no', side='top', pady=1)
        self.scheduler_stats_help_button.pack(fill=None, expand='no', side='top', pady=1)
        self.scheduler_stats_control_frame.pack(fill='y', expand='no', side='left')
        self.coro_scheduler_view = AggregatorView(False, 'coro scheduler stats', 1, self.sfmp, 120, 23, self.scheduler_stats_frame)
        self.coro_scheduler_view.pack(fill='both', expand='yes', side='left')
        self.scheduler_stats_frame.pack(fill='both', expand='yes', side='bottom')

        self.command_executor_view = CommandExecutor(160, 6)
        self.command_executor_view.pack(fill='x', expand='no', side='bottom')
        
        self.cmet = CorosMaxExecutionTimesProvider('coros lifetime max execution times', 'coros max execution times', 0.5)
        
        self.coros_lifetime_max_execution_times = AggregatorView(False, 'coros lifetime max execution times', 0.75, self.cmet.lifetime_stats_formatter, 25, 13, self)
        self.coros_lifetime_max_execution_times.pack(fill='x', expand='no', side='left')
        
        self.coros_max_execution_times = AggregatorView(False, 'coros max execution times', 0.75, self.cmet.stats_formatter, 25, 13, self)
        self.coros_max_execution_times.pack(fill='x', expand='no', side='left')
        
        self.spf = SchedulerPerformanceFormatter('scheduler tdelta', 'internal scheduler tdelta', 'scheduler lifetime stats', 'scheduler stats', 5000)
        
        self.scheduler_tdelta_formatter = AggregatorAppendFormatter('Scheduler TDelta')
        self.scheduler_tdelta = AggregatorView(True, 'scheduler tdelta', 0.1, self.scheduler_tdelta_formatter, 22, 13, self)
        self.scheduler_tdelta.max_len = 1000
        self.scheduler_tdelta.pack(fill='x', expand='no', side='left')
        
        def aggregator_view_formatter(data: Any) -> str:
            return f'{current_interface().coro_id}. Aggregator:\n{data}'
        
        self.command_executor_aggregator_view = AggregatorView(False, command_executor_aggregator_view_key, 1, aggregator_view_formatter, 25, 13, self)
        self.command_executor_aggregator_view.pack(fill='x', expand='yes', side='right')
        FastAggregatorClient()(command_executor_aggregator_view_key, str())
        
        self.command_executor_aggregator_append_formatter = AggregatorAppendFormatter('Aggregator Append')
        self.command_executor_aggregator_append_view = AggregatorView(True, command_executor_aggregator_append_view_key, 1, self.command_executor_aggregator_append_formatter, 25, 13, self)
        self.command_executor_aggregator_append_view.max_len = 5000
        self.command_executor_aggregator_append_view.pack(fill='x', expand='yes', side='right')
        FastAggregatorClient()(command_executor_aggregator_append_view_key, str())

        self.scheduler_lifetime_stats = AggregatorView(False, 'scheduler lifetime stats', 0.3, self.spf.lifetime_stats_formatter, 36, 5, self)
        self.scheduler_lifetime_stats.pack(fill=None, expand='no', side='top')
        
        self.scheduler_stats = AggregatorView(False, 'scheduler stats', 0.3, self.spf.stats_formatter, 36, 7, self)
        self.scheduler_stats.pack(fill=None, expand='no', side='bottom')

        # hide window
        self.withdraw()
    
    def scheduler_stats_format_button_on_click(self):
        d = FilterSetupDialog(self, self.sfmp.filtered_paths)
        self.wait_window(d)
        self.sfmp.update_filtered_paths(d.result)
    
    def scheduler_stats_help_button_on_click(self):
        HelpDialog(self)

    def start(self, wr: TkObjWrapper):
        self.spf.start()
        self.sfmp.start(wr)
        self.scheduler_tdelta.start(wr)
        self.command_executor_aggregator_view.start(wr)
        self.command_executor_aggregator_append_view.start(wr)
        self.scheduler_lifetime_stats.start(wr)
        self.scheduler_stats.start(wr)
        self.coro_scheduler_view.start(wr)
        self.cmet.start()
        self.coros_lifetime_max_execution_times.start(wr)
        self.coros_max_execution_times.start(wr)
    
    def stop(self):
        self.spf.stop()
        self.sfmp.stop()
        self.scheduler_tdelta.stop()
        self.command_executor_aggregator_view.stop()
        self.command_executor_aggregator_append_view.stop()
        self.scheduler_lifetime_stats.stop()
        self.scheduler_stats.stop()
        self.coro_scheduler_view.stop()
        self.cmet.stop()
        self.coros_lifetime_max_execution_times.stop()
        self.coros_max_execution_times.stop()
    
    def prepare(self, i: Interface, wr: TkObjWrapper):
        i(Yield)
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        self.start(wr)

        i(Yield)

        # show window again
        self.deiconify()


def coro_scheduler_admin__view(i: Interface, on_close: Optional[AnyWorker] = None):
    with(TkinterContextManager(i, Application())) as wr:
        app: Application = cast(Application, wr.tk)
        app.prepare(i, wr)
    
    if on_close is not None:
        app.stop()
        i(RunCoro, on_close)


def scheduler_stats_aggregator_provider(i: Interface):
    cs: CoroScheduler = i._loop
    fac = FastAggregatorClient()
    while True:
        stats_level: EntityStatsMixin.StatsLevel = EntityStatsMixin.StatsLevel.info
        result = dict()
        name, stats = cs.get_entity_stats(stats_level)
        result[name] = stats
        fac('coro scheduler stats', result)
        i(Sleep, 0.5)


def cs_init(cs: CoroScheduler):
    cs.set_coro_time_measurement(True)
    cs.set_coro_history_gathering(True)
    cs.set_loop_iteration_time_measurement(True)


async def start_admin(i: Interface, on_close: Optional[AnyWorker] = None):
    cs_init(i._loop)
    await i(PutCoroRequest().turn_on_tree_monitoring(True))
    await i(PutCoro, scheduler_stats_aggregator_provider)
    await i(PutCoro, coro_scheduler_admin__view, on_close)
