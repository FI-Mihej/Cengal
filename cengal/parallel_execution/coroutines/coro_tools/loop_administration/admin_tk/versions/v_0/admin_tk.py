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


__all__ = ['start_admin', 'cs_init', 'SchedulerPerformanceFormatter', 'scheduler_stats_aggregator_provider', 'CSStatsFormatterMultiprocess',
           'CorosLogsProvider', 'CoroLogsAppendFormatter', 'CoroLogsAppendFormatterParts']


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


from cengal.time_management.load_best_timer import perf_counter
import ttkbootstrap as ttkb
from ttkbootstrap.scrolled import ScrolledText as TtkbScrolledText
from tkinter import simpledialog
import tkinter as tk
from ttkbootstrap import Style
from pprintpp import pformat as pf
from typing import Callable, Hashable, Optional, Set, Dict, Tuple, Union, List, Sequence, Any, cast

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.tkinter import *
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro, PutCoroRequest
from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.simple_yield import Yield
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import AsyncioLoopRequest, run_in_thread_pool, run_in_thread_pool_fast
from cengal.parallel_execution.coroutines.coro_standard_services.fast_aggregator import *
from cengal.parallel_execution.coroutines.coro_standard_services.log import *
from cengal.parallel_execution.coroutines.coro_standard_services.instance import InstanceRequest
from cengal.parallel_execution.coroutines.coro_tools.coro_flow_control import graceful_coro_destroyer, agraceful_coro_destroyer, GracefulCoroDestroy
from cengal.parallel_execution.coroutines.coro_tools.lock import Lock
from cengal.statistics.normal_distribution import average
from cengal.parallel_execution.multiprocess.multiprocessing_task_runner import *
from cengal.text_processing.text_processing import normalize_line_separators_and_tabs
from cengal.introspection.inspect import get_exception, exception_to_printable_text
from cengal.system import OS_TYPE
from cengal.data_manipulation.dict_path import *
from cengal.user_interface.gui.tkinter.components.read_only_text import *
from cengal.user_interface.gui.tkinter.components.tool_tip import *
from cengal.user_interface.gui.tkinter.components.aggregator_view import *
from cengal.math.numbers import RationalNumber
from cengal.code_flow_control.args_manager import args_kwargs_to_str, ArgsKwargs
from greenlet import GreenletExit
from enum import IntFlag, auto
from uuid import uuid4


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
from cengal.parallel_execution.coroutines.coro_standard_services.log import *
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
        
        self.worker_lock: Lock = Lock(f'CSStatsFormatterMultiprocess.worker__{uuid4()}')
        self.worker: SubprocessWorker = SubprocessWorker(settings)
        self.worker.start(wait_for_process_readyness=False)
        self.worker_is_ready: bool = False
    
    async def _worker_readyness_waiting_coro(self, i: Interface):
        need_to_wait = True
        while need_to_wait:
            try:
                async with self.worker_lock:
                    self.worker.wait_for_subprocess_readines(block=False)

                need_to_wait = False
            except SubprocessIsNotReadyError:
                await i(Sleep, 0.1)
        
        self.worker_is_ready = True
    
    async def wait_for_worker_readyness(self, i: Interface):
        while not self.worker_is_ready:
            await i(Sleep, 0.1)
    
    def start(self, wr: Optional[TkObjWrapper] = None):
        if wr is None:
            i = current_interface()
            i(PutCoro, self._worker_readyness_waiting_coro)
        else:
            wr.put_coro(self._worker_readyness_waiting_coro)
    
    def stop(self):
        self._stop = True
        need_to_block = False
        try:
            i: Interface = current_interface()
        except:
            need_to_block = True
        
        with self.worker_lock:
            if need_to_block:
                self.worker.stop()
            else:
                run_in_thread_pool_fast(i, self.worker.stop)
        
    def update_filtered_paths(self, filtered_paths: List[Sequence[str]]):
        i: Interface = current_interface()
        self.filtered_paths = filtered_paths
        with self.worker_lock:
            if not self._stop:
                self.worker.send_data_to_subprocess({
                    'type': 'filter',
                    'data': self.filtered_paths
                })
    
    def __call__(self, data):
        with self.worker_lock:
            if not self.worker_is_ready:
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
                    result = self.worker.get_answer_from_subprocess(block=False)
                except Empty:
                    pass
                else:
                    got_result = True
                
                if got_result:
                    if 'data' != result['type']:
                        got_result = False
                
                if not got_result:
                    i(Sleep, 0.01)
            
            result = '' if result is None else result['data']
            result = f'{i.coro_id}. CoroScheduler stats:\n{result}'
            return result
    
    @staticmethod
    def process_initializer(init_data) -> Any:
        from pprintpp import pformat as pf
        return init_data
    
    @staticmethod
    def process_worker(global_data, data_msg):
        data = data_msg['data']
        if 'filter' == data_msg['type']:
            if global_data is None:
                global_data = dict()
            
            global_data['filtered_paths'] = data
            return None  # no answer to parent process
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


class CoroLogsAppendFormatterParts(IntFlag):
    none = 0
    prompt_string = auto()
    time = auto()
    caller_info = auto()
    logging_level = auto()
    log = auto()
    coros_traceback = auto()
    file_name_and_line_number = auto()
    traceback = auto()
    all = prompt_string | time | caller_info | logging_level | log | coros_traceback | file_name_and_line_number | traceback


class CoroLogsAppendFormatter(AggregatorAppendFormatter):
    def __init__(self, initial_text: str, desired_parts: CoroLogsAppendFormatterParts = CoroLogsAppendFormatterParts.all) -> None:
        super().__init__(initial_text)
        self._prompt_string: str = f'>>> {"-"*80}'
        self.desired_parts: CoroLogsAppendFormatterParts = desired_parts

    def __call__(self, data: List[Tuple[Tuple, Dict, Dict[str, Any]]]) -> Any:
        if data:
            data_part = '\n\n'.join([self._format(*log_info) for log_info in data])
            return super().__call__(f'\n{data_part}\n')
        else:
            return super().__call__(str())

    def _format(self, args, kwargs, info=None) -> str:
        if info is None:
            return f'{self._prompt_string}\n{args_kwargs_to_str(args, kwargs)}'
        else:
            output_strings: List[str] = list()
            if CoroLogsAppendFormatterParts.prompt_string in self.desired_parts:
                output_strings.append(self._prompt_string)

            if CoroLogsAppendFormatterParts.time in self.desired_parts:
                output_strings.append(f'> Time: {info[InfoFields.current_time]}; Perf Counter: {info[InfoFields.perf_counter_time]:17.6f}')

            if CoroLogsAppendFormatterParts.caller_info in self.desired_parts:
                output_strings.append(f'> λ: {info[InfoFields.caller_info]}')

            if CoroLogsAppendFormatterParts.logging_level in self.desired_parts:
                if InfoFields.logging_level in info:
                    output_strings.append(f'> Logging level: {info[InfoFields.logging_level]}')
            
            if CoroLogsAppendFormatterParts.log in self.desired_parts:
                output_strings.append(args_kwargs_to_str(args, kwargs))

            if CoroLogsAppendFormatterParts.coros_traceback in self.desired_parts:
                coro_parents_strings: List[str] = info[InfoFields.coro_parents_strings]
                if coro_parents_strings:
                    coro_parents_text: str = '\n'.join(coro_parents_strings)
                    output_strings.append(f'> Coros traceback:\n{coro_parents_text}')
            
            if CoroLogsAppendFormatterParts.file_name_and_line_number in self.desired_parts:
                output_strings.append(f'> @ {info[InfoFields.file_name]}:{info[InfoFields.line_number]}')

            if CoroLogsAppendFormatterParts.traceback in self.desired_parts:
                traceback_strings: List[str] = info[InfoFields.traceback_strings]
                if traceback_strings:
                    traceback_text: str = '\n'.join(traceback_strings)
                    traceback_text = traceback_text.strip('\n')
                    output_strings.append(f'> Traceback:\n{traceback_text}')
            
            return '\n'.join(output_strings)


class CorosLogsProvider:
    def __init__(self, coros_logs_key: Hashable, logs_limit: Union[None, int], period: float, force_stop_timeout: RationalNumber = 0.1):
        self.coros_logs_key: Hashable = coros_logs_key
        self.logs_limit: Union[None, int] = logs_limit
        self.period: float = period
        self.i: Interface = None
        self._update_coro_id: CoroID = None
        self.force_stop_timeout: RationalNumber = force_stop_timeout
        self.fac = FastAggregatorClient()
        self._stop = False
        self.lifetime_stats: Dict[CoroID, float] = dict()
        self._current_logs_taken: bool = False
        self._unsend_data: List[List[Tuple[Tuple, Dict]]] = list()
        self._log_service_handler_was_added: bool = False
    
    def start(self):
        if self.i is None:
            self.i = current_interface()
        
        self._update_coro_id = self.i(PutCoro, self._update)
    
    def stop(self):
        self._stop = True
        current_interface()(PutCoro, self._force_stop)
    
    async def _force_stop(self, i: Interface):
        if self._update_coro_id is not None:
            update_coro_id = self._update_coro_id
            self._update_coro_id = None
            await agraceful_coro_destroyer(i, self.force_stop_timeout, update_coro_id)
        
        if self._log_service_handler_was_added:
            self._log_service_handler_was_added = False
            await i(LogRequest().remove_iteration_handler(self))
        
        self._unsend_data = type(self._unsend_data)()
    
    async def _update(self, i: Interface):
        while not self._stop:
            if not self._log_service_handler_was_added:
                if i._loop.is_service_registered(Log):
                    self._log_service_handler_was_added = True
                    await i(LogRequest().add_iteration_handler(self))
                    
            logs_parts = self._unsend_data
            self._unsend_data = type(self._unsend_data)()
            for logs_part in logs_parts:
                self.fac(self.coros_logs_key, logs_part)
            
            await i(Sleep, self.period)
    
    def __call__(self, log_service: Log, data: List[Tuple[Tuple, Dict, Dict[str, Any]]], current_time: float, current_time_str: str):
        if self._current_logs_taken:
            if self.logs_limit is None:
                if data:
                    self._unsend_data.append(data)
            else:
                num_of_an_initial_logs_needed: int = self.logs_limit - len(data)
                if 0 <= num_of_an_initial_logs_needed:
                    if data:
                        self._unsend_data.append(data)
                else:
                    part_of_data = data[-self.logs_limit:]
                    if part_of_data:
                        self._unsend_data.append(part_of_data)
        else:
            self._current_logs_taken = True
            if self.logs_limit is None:
                combined_data = log_service.get_last_n_logs(None) + data
                if combined_data:
                    self._unsend_data.append(combined_data)
            else:
                num_of_an_initial_logs_needed: int = self.logs_limit - len(data)
                if 0 < num_of_an_initial_logs_needed:
                    combined_data = log_service.get_last_n_logs(num_of_an_initial_logs_needed) + data
                    if combined_data:
                        self._unsend_data.append(combined_data)
                if 0 == num_of_an_initial_logs_needed:
                    if data:
                        self._unsend_data.append(data)
                else:
                    part_of_data = data[-self.logs_limit:]
                    if part_of_data:
                        self._unsend_data.append(part_of_data)


class SchedulerPerformanceFormatter:
    def __init__(self, loop_iteration_delta_times_key: Hashable, loop_iteration_delta_times_lifetime_stats_key: Hashable, loop_iteration_delta_times_stats_key: Hashable, window_size: int):
        self.external_items_key: Hashable = loop_iteration_delta_times_key
        self.internal_items_key: Hashable = f'internal_scheduler_tdelta__{uuid4()}'
        self.lifetime_stats_key: Hashable = loop_iteration_delta_times_lifetime_stats_key
        self.stats_key: Hashable = loop_iteration_delta_times_stats_key
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
        self.worker_lock: Lock = Lock(f'SchedulerPerformanceFormatter.worker__{uuid4()}')
        self.worker: SubprocessWorker = SubprocessWorker(settings)
        self.worker.start(wait_for_process_readyness=False)
        self.worker_is_ready: bool = False
    
    async def _worker_readyness_waiting_coro(self, i: Interface):
        need_to_wait = True
        while need_to_wait:
            try:
                async with self.worker_lock:
                    self.worker.wait_for_subprocess_readines(block=False)
                
                need_to_wait = False
            except SubprocessIsNotReadyError:
                await i(Sleep, 0.1)
        
        self.worker_is_ready = True
    
    async def wait_for_worker_readyness(self, i: Interface):
        while not self.worker_is_ready:
            await i(Sleep, 0.1)
    
    def start(self, wr: Optional[TkObjWrapper] = None):
        if self.i is None:
            self.i = current_interface()
        
        if wr is None:
            self.i(PutCoro, self._worker_readyness_waiting_coro)
            self.i(PutCoro, self._update)
            self.i(PutCoro, self._update_stats)
        else:
            wr.put_coro(self._worker_readyness_waiting_coro)
            wr.put_coro(self._update)
            wr.put_coro(self._update_stats)
    
    def stop(self):
        self._stop = True
        need_to_block = False
        try:
            i: Interface = current_interface()
        except:
            need_to_block = True
        
        with self.worker_lock:
            if need_to_block:
                self.worker.stop()
            else:
                run_in_thread_pool_fast(i, self.worker.stop)
    
    def _update(self, i: Interface):
        i(RunCoro, self.wait_for_worker_readyness)
        while not self._stop:
            # start = perf_counter()
            i(Yield)
            # stop = perf_counter()
            # delta_time = stop - start
            loop: CoroScheduler = i._loop
            delta_time = loop.loop_iteration_delta_time
            self.fac(self.external_items_key, delta_time)
            self.fac(self.internal_items_key, delta_time)

    def _update_stats(self, i: Interface):
        i(RunCoro, self.wait_for_worker_readyness)
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
        with self.worker_lock:
            self.worker.send_data_to_subprocess(data)
            result = None
            got_result = False
            while not got_result:
                try:
                    result = self.worker.get_answer_from_subprocess(block=False)
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
        average_data = average(data)
        iter_per_sec = 0 if 0 == average_data else (1 / average_data)
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
    def __init__(self, style: str = 'superhero', filtered_paths: List[List[str]] = None, current_children_pack_type: int = 1):
        super().__init__(size=(1900, 900), resizable=(True, True))
        self.style_name = style
        Style(style)
        self.current_children_pack_type: int = current_children_pack_type
        self.max_children_pack_type: int = 2
        self.packed_widgets: List[tk.Widget] = list()
        self.filtered_paths: List[Sequence[str]] = filtered_paths

        self.title('CoroScheduler Admin')
        self.resizable(width=True, height=True)

        self.sfmp = CSStatsFormatterMultiprocess(self.filtered_paths)
        
        self.scheduler_stats_frame = ttkb.Frame(self)
        self.scheduler_stats_control_frame = ttkb.Frame(self.scheduler_stats_frame)
        
        self.scheduler_stats_layout_button_text = self.scheduler_stats_layout_button_name()
        self.scheduler_stats_layout_button_text_len = len('L') + 1
        self.scheduler_stats_layout_button = ttkb.Button(self.scheduler_stats_control_frame, text=self.scheduler_stats_layout_button_text, width=self.scheduler_stats_layout_button_text_len, command=self.scheduler_stats_layout_button_on_click)
        self.scheduler_stats_layout_button_tooltip = ToolTipHovered(self.scheduler_stats_layout_button, 'Layout circle switch')

        self.scheduler_stats_format_button_text = 'F'
        self.scheduler_stats_format_button_text_len = len(self.scheduler_stats_format_button_text) + 1
        self.scheduler_stats_format_button = ttkb.Button(self.scheduler_stats_control_frame, text=self.scheduler_stats_format_button_text, width=self.scheduler_stats_format_button_text_len, command=self.scheduler_stats_format_button_on_click)
        self.scheduler_stats_format_button_tooltip = ToolTipHovered(self.scheduler_stats_format_button, 'Filter our unnecessary or flickering paths')
        
        self.scheduler_stats_help_button_text = '?'
        self.scheduler_stats_help_button_text_len = len(self.scheduler_stats_help_button_text) + 1
        self.scheduler_stats_help_button = ttkb.Button(self.scheduler_stats_control_frame, text=self.scheduler_stats_help_button_text, width=self.scheduler_stats_help_button_text_len, bootstyle="info", command=self.scheduler_stats_help_button_on_click)
        self.scheduler_stats_help_button_tooltip = ToolTipHovered(self.scheduler_stats_help_button, 'Console description and help')

        self.coro_scheduler_view = AggregatorView(False, False, 'coro_scheduler_stats', 1, self.sfmp, 25, 23, self.scheduler_stats_frame)

        self.coro_logs_formatter: CoroLogsAppendFormatter = CoroLogsAppendFormatter('Coro Logs')
        self.coro_logs_provider: CorosLogsProvider = CorosLogsProvider('coro scheduler logs', None, 0.25)
        self.coro_scheduler_logs_view = AggregatorView(True, True, 'coro scheduler logs', 1, self.coro_logs_formatter, 25, 23, self.scheduler_stats_frame)

        self.command_executor_view = CommandExecutor(160, 6)
        
        self.cmet = CorosMaxExecutionTimesProvider('coros lifetime max execution times', 'coros max execution times', 0.5)
        
        self.coros_lifetime_max_execution_times = AggregatorView(False, False, 'coros lifetime max execution times', 0.75, self.cmet.lifetime_stats_formatter, 25, 13, self)
        
        self.coros_max_execution_times = AggregatorView(False, False, 'coros max execution times', 0.75, self.cmet.stats_formatter, 25, 13, self)
        
        self.spf = SchedulerPerformanceFormatter('loop_iteration_delta_times', 'loop_iteration_delta_times_lifetime_stats', 'loop_iteration_delta_times_stats', 5000)
        
        self.scheduler_tdelta_formatter = AggregatorAppendFormatter('Scheduler TDelta')
        self.scheduler_tdelta = AggregatorView(True, False, 'loop_iteration_delta_times', 0.1, self.scheduler_tdelta_formatter, 22, 13, self)
        self.scheduler_tdelta.default_auto_scroll = False
        self.scheduler_tdelta.max_len = 1000
        
        def aggregator_view_formatter(data: Any) -> str:
            return f'{current_interface().coro_id}. Aggregator:\n{data}'
        
        self.command_executor_aggregator_view = AggregatorView(False, False, command_executor_aggregator_view_key, 1, aggregator_view_formatter, 25, 13, self)
        FastAggregatorClient()(command_executor_aggregator_view_key, str())
        
        self.command_executor_aggregator_append_formatter = AggregatorAppendFormatter('Aggregator Append')
        self.command_executor_aggregator_append_view = AggregatorView(True, True, command_executor_aggregator_append_view_key, 1, self.command_executor_aggregator_append_formatter, 25, 13, self)
        self.command_executor_aggregator_append_view.max_len = 5000
        FastAggregatorClient()(command_executor_aggregator_append_view_key, str())

        self.scheduler_lifetime_stats = AggregatorView(False, False, 'loop_iteration_delta_times_lifetime_stats', 0.3, self.spf.lifetime_stats_formatter, 36, 5, self)
        
        self.scheduler_stats = AggregatorView(False, False, 'loop_iteration_delta_times_stats', 0.3, self.spf.stats_formatter, 36, 7, self)

        self.pack_children(self.current_children_pack_type)

        # set window size taking into account the size of the widgets
        self.update()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.update()
    
    def pack_forget_children(self):
        self.packed_widgets.reverse()
        for widget in self.packed_widgets:
            widget.pack_forget()
    
    def pack_children(self, pack_type: int):
        self.pack_forget_children()
        self.packed_widgets.clear()
        if 0 == pack_type:
            self.scheduler_stats_layout_button.pack(fill=None, expand='no', side='top', pady=1)
            self.packed_widgets.append(self.scheduler_stats_layout_button)
            self.scheduler_stats_format_button.pack(fill=None, expand='no', side='top', pady=1)
            self.packed_widgets.append(self.scheduler_stats_format_button)
            self.scheduler_stats_help_button.pack(fill=None, expand='no', side='top', pady=1)
            self.packed_widgets.append(self.scheduler_stats_help_button)
            self.scheduler_stats_control_frame.pack(fill='y', expand='no', side='left')
            self.packed_widgets.append(self.scheduler_stats_control_frame)
            self.coro_scheduler_view.pack(fill='both', expand='yes', side='left')
            self.packed_widgets.append(self.coro_scheduler_view)
            self.coro_scheduler_logs_view.pack(fill='both', expand='no', side='left')
            self.packed_widgets.append(self.coro_scheduler_logs_view)

            self.scheduler_stats_frame.pack(fill='both', expand='yes', side='bottom')
            self.packed_widgets.append(self.scheduler_stats_frame)
            self.command_executor_view.pack(fill='x', expand='no', side='bottom')
            self.packed_widgets.append(self.command_executor_view)
            self.coros_lifetime_max_execution_times.pack(fill='x', expand='no', side='left')
            self.packed_widgets.append(self.coros_lifetime_max_execution_times)
            self.coros_max_execution_times.pack(fill='x', expand='no', side='left')
            self.packed_widgets.append(self.coros_max_execution_times)
            self.scheduler_tdelta.pack(fill='x', expand='no', side='left')
            self.packed_widgets.append(self.scheduler_tdelta)
            self.command_executor_aggregator_view.pack(fill='x', expand='yes', side='right')
            self.packed_widgets.append(self.command_executor_aggregator_view)
            self.command_executor_aggregator_append_view.pack(fill='x', expand='yes', side='right')
            self.packed_widgets.append(self.command_executor_aggregator_append_view)
            self.scheduler_lifetime_stats.pack(fill=None, expand='no', side='top')
            self.packed_widgets.append(self.scheduler_lifetime_stats)
            self.scheduler_stats.pack(fill=None, expand='no', side='bottom')
            self.packed_widgets.append(self.scheduler_stats)
        elif 1 == pack_type:
            self.scheduler_stats_layout_button.pack(fill=None, expand='no', side='top', pady=1)
            self.packed_widgets.append(self.scheduler_stats_layout_button)
            self.scheduler_stats_format_button.pack(fill=None, expand='no', side='top', pady=1)
            self.packed_widgets.append(self.scheduler_stats_format_button)
            self.scheduler_stats_help_button.pack(fill=None, expand='no', side='top', pady=1)
            self.packed_widgets.append(self.scheduler_stats_help_button)
            self.scheduler_stats_control_frame.pack(fill='y', expand='no', side='left')
            self.packed_widgets.append(self.scheduler_stats_control_frame)
            self.coro_scheduler_view.pack(fill='both', expand='yes', side='left')
            self.packed_widgets.append(self.coro_scheduler_view)
            self.coro_scheduler_logs_view.pack(fill='both', expand='yes', side='left')
            self.packed_widgets.append(self.coro_scheduler_logs_view)

            self.scheduler_stats_frame.pack(fill='both', expand='yes', side='bottom')
            self.packed_widgets.append(self.scheduler_stats_frame)
            self.command_executor_view.pack(fill='x', expand='no', side='bottom')
            self.packed_widgets.append(self.command_executor_view)
            self.coros_lifetime_max_execution_times.pack(fill='x', expand='no', side='left')
            self.packed_widgets.append(self.coros_lifetime_max_execution_times)
            self.coros_max_execution_times.pack(fill='x', expand='no', side='left')
            self.packed_widgets.append(self.coros_max_execution_times)
            self.scheduler_tdelta.pack(fill='x', expand='no', side='left')
            self.packed_widgets.append(self.scheduler_tdelta)
            self.command_executor_aggregator_view.pack(fill='x', expand='yes', side='right')
            self.packed_widgets.append(self.command_executor_aggregator_view)
            self.command_executor_aggregator_append_view.pack(fill='x', expand='yes', side='right')
            self.packed_widgets.append(self.command_executor_aggregator_append_view)
            self.scheduler_lifetime_stats.pack(fill=None, expand='no', side='top')
            self.packed_widgets.append(self.scheduler_lifetime_stats)
            self.scheduler_stats.pack(fill=None, expand='no', side='bottom')
            self.packed_widgets.append(self.scheduler_stats)
        elif 2 == pack_type:
            self.scheduler_stats_layout_button.pack(fill=None, expand='no', side='top', pady=1)
            self.packed_widgets.append(self.scheduler_stats_layout_button)
            self.scheduler_stats_format_button.pack(fill=None, expand='no', side='top', pady=1)
            self.packed_widgets.append(self.scheduler_stats_format_button)
            self.scheduler_stats_help_button.pack(fill=None, expand='no', side='top', pady=1)
            self.packed_widgets.append(self.scheduler_stats_help_button)
            self.scheduler_stats_control_frame.pack(fill='y', expand='no', side='left')
            self.packed_widgets.append(self.scheduler_stats_control_frame)
            self.coro_scheduler_view.pack(fill='both', expand='no', side='left')
            self.packed_widgets.append(self.coro_scheduler_view)
            self.coro_scheduler_logs_view.pack(fill='both', expand='yes', side='left')
            self.packed_widgets.append(self.coro_scheduler_logs_view)

            self.scheduler_stats_frame.pack(fill='both', expand='yes', side='bottom')
            self.packed_widgets.append(self.scheduler_stats_frame)
            self.command_executor_view.pack(fill='x', expand='no', side='bottom')
            self.packed_widgets.append(self.command_executor_view)
            self.coros_lifetime_max_execution_times.pack(fill='x', expand='no', side='left')
            self.packed_widgets.append(self.coros_lifetime_max_execution_times)
            self.coros_max_execution_times.pack(fill='x', expand='no', side='left')
            self.packed_widgets.append(self.coros_max_execution_times)
            self.scheduler_tdelta.pack(fill='x', expand='no', side='left')
            self.packed_widgets.append(self.scheduler_tdelta)
            self.command_executor_aggregator_view.pack(fill='x', expand='yes', side='right')
            self.packed_widgets.append(self.command_executor_aggregator_view)
            self.command_executor_aggregator_append_view.pack(fill='x', expand='yes', side='right')
            self.packed_widgets.append(self.command_executor_aggregator_append_view)
            self.scheduler_lifetime_stats.pack(fill=None, expand='no', side='top')
            self.packed_widgets.append(self.scheduler_lifetime_stats)
            self.scheduler_stats.pack(fill=None, expand='no', side='bottom')
            self.packed_widgets.append(self.scheduler_stats)
        else:
            raise NotImplementedError
    
    def scheduler_stats_layout_button_name(self) -> str:
        return 'L' if 0 == self.current_children_pack_type else 'L' + str(self.current_children_pack_type)

    def scheduler_stats_layout_button_on_click(self):
        self.current_children_pack_type += 1
        if self.current_children_pack_type > self.max_children_pack_type:
            self.current_children_pack_type = 0
        
        self.scheduler_stats_layout_button_text = self.scheduler_stats_layout_button_name()
        self.scheduler_stats_layout_button.config(text=self.scheduler_stats_layout_button_text)
        self.pack_children(self.current_children_pack_type)
    
    def scheduler_stats_format_button_on_click(self):
        d = FilterSetupDialog(self, self.sfmp.filtered_paths)
        self.wait_window(d)
        self.sfmp.update_filtered_paths(d.result)
    
    def scheduler_stats_help_button_on_click(self):
        HelpDialog(self)

    def start(self, wr: TkObjWrapper):
        self.spf.start()
        self.sfmp.start(wr)
        self.coro_logs_provider.start()
        self.scheduler_tdelta.start(wr)
        self.command_executor_aggregator_view.start(wr)
        self.command_executor_aggregator_append_view.start(wr)
        self.scheduler_lifetime_stats.start(wr)
        self.scheduler_stats.start(wr)
        self.coro_scheduler_view.start(wr)
        self.coro_scheduler_logs_view.start(wr)
        self.cmet.start()
        self.coros_lifetime_max_execution_times.start(wr)
        self.coros_max_execution_times.start(wr)
    
    def stop(self):
        self.spf.stop()
        self.sfmp.stop()
        self.coro_logs_provider.stop()
        self.scheduler_tdelta.stop()
        self.command_executor_aggregator_view.stop()
        self.command_executor_aggregator_append_view.stop()
        self.scheduler_lifetime_stats.stop()
        self.scheduler_stats.stop()
        self.coro_scheduler_view.stop()
        self.coro_scheduler_logs_view.stop()
        self.cmet.stop()
        self.coros_lifetime_max_execution_times.stop()
        self.coros_max_execution_times.stop()
    
    def prepare(self, i: Interface, wr: TkObjWrapper):
        i(Yield)
        self.start(wr)
        i(Yield)


def coro_scheduler_admin__view(i: Interface, on_close: Optional[AnyWorker] = None, app_args_kwargs: Optional[ArgsKwargs] = None):
    app_args, app_kwargs = app_args_kwargs() if app_args_kwargs is not None else ArgsKwargs()()
    with TkinterContextManager(i, Application(*app_args, **app_kwargs)) as wr:
        app: Application = cast(Application, wr.tk)
        app.prepare(i, wr)
        i(InstanceRequest().set('admin_tk_app', app))
    
    if on_close is not None:
        app.stop()
        i(RunCoro, on_close)


def scheduler_stats_aggregator_provider(i: Interface, fac_key: str = 'coro_scheduler_stats'):
    cs: CoroScheduler = i._loop
    fac = FastAggregatorClient()
    while True:
        stats_level: EntityStatsMixin.StatsLevel = EntityStatsMixin.StatsLevel.info
        result = dict()
        name, stats = cs.get_entity_stats(stats_level)
        result[name] = stats
        fac(fac_key, result)
        i(Sleep, 0.5)


def cs_init(cs: CoroScheduler):
    cs.set_coro_time_measurement(True)
    cs.set_coro_history_gathering(True)
    cs.set_loop_iteration_time_measurement(True)


async def start_admin(i: Interface, on_close: Optional[AnyWorker] = None, app_args_kwargs: Optional[ArgsKwargs] = None):
    cs_init(i._loop)
    await i(PutCoroRequest().turn_on_tree_monitoring(True))
    await i(PutCoro, scheduler_stats_aggregator_provider)
    await i(PutCoro, coro_scheduler_admin__view, on_close, app_args_kwargs)
