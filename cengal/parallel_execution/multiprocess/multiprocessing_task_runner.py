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

import cProfile
# import multiprocessing
from multiprocessing import Process, Queue, Pipe
from threading import Thread
import sys
import traceback
from queue import Empty, Full
import marshal
import pickle
import os
from cengal.data_manipulation.front_triggerable_variable import FrontTriggerableVariable, FrontTriggerableVariableType
from cengal.base.classes import BaseClassSettings

# import time

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


class SendableDataType:
    pickable = 0
    marshalable = 1
    custom = 2


class Transport:
    queue = 0
    pipe = 1
    tcp = 2


class SubprocessWorkerSettings(BaseClassSettings):
    def __init__(self):
        self.initiation_function = None  # self.data_shelf = self.settings.initiation_function(
        #   self.initialization_data)
        self.working_function = None  # 1) 'answer = self.settings.working_function(input_data)'
        #       if initiation_function is None;
        #   2) 'answer = self.settings.working_function(self.data_shelf, input_data)' if initiation_function
        #       is not None.
        self.stopping_function = None

        self.on_input_queue_is_too_big = None  # self.on_input_queue_is_too_big(self.data_shelf,
        #   average_input_size_trigger_result) where: average_input_size_trigger_result =
        #   self.input_queue_average_size_trigger.test_trigger(average_input_size)
        self.on_another_bunch_of_data_was_processed = None  # self.on_another_bunch_of_data_was_processed(
        #   self.data_shelf)
        self.on_exit = None  # on process exit; self.on_exit(self.data_shelf)

        self.need_multithreading = False  # will use multithread mode if True; and multiprocess else.
        self.process_name = None  # str()
        self.profile = False  # will start worker in profiling mode
        self.initialization_data = None  # any pickable Python data
        self.transport = None  # Transport()
        self.tcp_settings = None  # tcp_link.TCPSettings(). Is used when (self.transport == Transport.tcp)
        self.use_internal_subprocess_input_buffer = False  # will be able to get input data in nonblocking mode
        self.sendable_data_type = SendableDataType.pickable
        self.sendable_data__encoder = None  # Will be in use when sendable_data_type == SendableDataType.custom.
        #   Function will encode data in to bytes()
        self.sendable_data__decoder = None  # Will be in use when sendable_data_type == SendableDataType.custom.
        #   Function will decode data from bytes()
        self.queue_to_subprocess = None  # only needed if you want to directly connect this worker with another.
        #   For example to connect output from this worker to input of another worker.
        self.queue_from_subprocess = None  # only needed if you want to directly connect this worker with another.
        #   For example to connect output from this worker to input of another worker.
        self.input_queue_average_size_trigger_limit = 30

    def check(self):
        if self.working_function is None:
            raise Exception('working_function cannot be None!')

        if self.transport is None:
            raise Exception('transport can\'t be None')
        else:
            if Transport.tcp == self.transport:
                if self.tcp_settings is None:
                    raise Exception('tcp_settings can\'t be None while (Transport.tcp == self.transport)')
                else:
                    self.tcp_settings.check()


class SubprocessWorker:

    def __init__(self, settings):
        """ 
        :param settings: SubprocessWorkerSettings(); you should use copy.copy(SubprocessWorkerSettings(...)) by your 
            self if you want
        :return: 
        """
        super().__init__()
        
        self.settings = settings
        self.settings.check()

        self.data_shelf = None

        self.subprocess_was_initiated = False
        self.subprocess = None
        self.queue_to_subprocess = self.settings.queue_to_subprocess
        self.queue_from_subprocess = self.settings.queue_from_subprocess

        self.list_of_subprocess_input_data = list()
        self.input_size_print_sum = 0
        self.input_size_print_counter = 0
        self.input_size_print_counter_limit = 500
        # self.last_log_print_time = time.time()
        self.input_queue_average_size_trigger = FrontTriggerableVariable(
            FrontTriggerableVariableType.bigger_or_equal, self.settings.input_queue_average_size_trigger_limit)

    def _encode_sendable_data(self, data):
        result = data
        if Transport.queue == self.settings.transport:
            if self.settings.sendable_data_type == SendableDataType.pickable:
                pass
            elif self.settings.sendable_data_type == SendableDataType.marshalable:
                result = marshal.dumps(result)
            elif self.settings.sendable_data_type == SendableDataType.custom:
                result = self.settings.sendable_data__encoder(result)
        else:
            if self.settings.sendable_data_type == SendableDataType.pickable:
                result = pickle.dumps(result)
            elif self.settings.sendable_data_type == SendableDataType.marshalable:
                result = marshal.dumps(result)
            elif self.settings.sendable_data_type == SendableDataType.custom:
                result = self.settings.sendable_data__encoder(result)
        return result

    def _decode_sendable_data(self, data):
        result = data
        if Transport.queue == self.settings.transport:
            if self.settings.sendable_data_type == SendableDataType.pickable:
                pass
            elif self.settings.sendable_data_type == SendableDataType.marshalable:
                result = marshal.loads(result)
            elif self.settings.sendable_data_type == SendableDataType.custom:
                result = self.settings.sendable_data__decoder(result)
        else:
            if self.settings.sendable_data_type == SendableDataType.pickable:
                result = pickle.loads(result)
            elif self.settings.sendable_data_type == SendableDataType.marshalable:
                result = marshal.loads(result)
            elif self.settings.sendable_data_type == SendableDataType.custom:
                result = self.settings.sendable_data__decoder(result)
        return result

    def _parsing_worker_wrapper(self, input_data, stop=False):
        # print('===>>', self.settings.process_name, '_parsing_worker_wrapper', '0')
        exception = None
        answer = None
        result = None
        try:
            # print('===>>', self.settings.process_name, '_parsing_worker_wrapper', '1')
            if self.settings.initiation_function is None:
                # print('===>>', self.settings.process_name, '_parsing_worker_wrapper', '2')
                if stop:
                    if self.settings.stopping_function is not None:
                        self.settings.stopping_function()
                else:
                    answer = self.settings.working_function(input_data)
                # print('===>>', self.settings.process_name, '_parsing_worker_wrapper', '3')
            else:
                # print('===>>', self.settings.process_name, '_parsing_worker_wrapper', '4')
                if stop:
                    if self.settings.stopping_function is not None:
                        self.settings.stopping_function(self.data_shelf)
                else:
                    answer = self.settings.working_function(self.data_shelf, input_data)
                # print('===>>', self.settings.process_name, '_parsing_worker_wrapper', '5')
        except:
            # print('===>>', self.settings.process_name, '_parsing_worker_wrapper', '6')
            exception = sys.exc_info()
            formatted_traceback = traceback.format_exception(exception[0], exception[1], exception[2])
            exception = exception[:2] + (formatted_traceback,)
            answer = (input_data[0], None)
            # print(self.settings.process_name)
            # print(input_data)
            # print(exception)
            exception = pickle.dumps(exception)

        # print('===>>', self.settings.process_name, '_parsing_worker_wrapper', '7')
        if (answer is not None) or (exception is not None):
            # print('===>>', self.settings.process_name, '_parsing_worker_wrapper', '8')
            result = (answer, exception)

        # print('<<===', self.settings.process_name, '_parsing_worker_wrapper')
        return result

    def _subprocess_wrapper(self):
        # input_from_parent_process_queue = self.queue_to_subprocess
        # output_to_parent_process_queue = self.queue_from_subprocess

        print(' STARTED:', self.settings.process_name, '; PID:', os.getpid())

        input_from_parent_process_queue = None
        output_to_parent_process_queue = None
        if Transport.pipe == self.settings.transport:
            input_from_parent_process_queue = self.queue_to_subprocess[1]
            output_to_parent_process_queue = self.queue_from_subprocess[1]
        elif Transport.queue == self.settings.transport:
            input_from_parent_process_queue = self.queue_to_subprocess
            output_to_parent_process_queue = self.queue_from_subprocess

        if self.settings.initiation_function is not None:
            self.data_shelf = self.settings.initiation_function(self.settings.initialization_data)
        while True:
            # print('===>>', self.settings.process_name, '_subprocess_wrapper', '0')
            # print('===>>', self.settings.process_name, '_subprocess_wrapper', '1', 'qsize:',
            #       input_from_parent_process_queue.qsize())

            # input_size = input_from_parent_process_queue.qsize()
            # if input_size > 3:
            #     print('===>>', self.settings.process_name, 'input_size:', input_size)
            # output_size = output_to_parent_process_queue.qsize()
            # if output_size > 3:
            #     print('===>>', self.settings.process_name, 'output_size:', output_size)

            data = None
            if self.settings.use_internal_subprocess_input_buffer:
                while True:
                    another_chunk_of_data = None
                    if Transport.pipe == self.settings.transport:
                        if input_from_parent_process_queue.poll():
                            another_chunk_of_data = input_from_parent_process_queue.recv_bytes()
                        else:
                            break
                    elif Transport.queue == self.settings.transport:
                        if not input_from_parent_process_queue.empty():
                            another_chunk_of_data = input_from_parent_process_queue.get()
                        else:
                            break
                    self.list_of_subprocess_input_data.append(another_chunk_of_data)

                input_size = len(self.list_of_subprocess_input_data)
                self.input_size_print_counter += 1
                self.input_size_print_sum += input_size
                if self.input_size_print_counter >= self.input_size_print_counter_limit:
                    average_input_size = self.input_size_print_sum / self.input_size_print_counter
                    self.input_size_print_sum = 0
                    self.input_size_print_counter = 0
                    average_input_size_trigger_result = self.input_queue_average_size_trigger.test_trigger(
                        average_input_size)
                    if average_input_size_trigger_result is not None:
                        if average_input_size_trigger_result:
                            print('===>>', self.settings.process_name, 'average_input_size:', average_input_size)
                        else:
                            print('===>>', self.settings.process_name, 'average_input_size is OK:', average_input_size)
                        if self.settings.on_input_queue_is_too_big is not None:
                            self.settings.on_input_queue_is_too_big(self.data_shelf, average_input_size_trigger_result)

                # data = input_from_parent_process_queue.get()
                if len(self.list_of_subprocess_input_data) > 0:
                    data = self.list_of_subprocess_input_data[0]
                    # print('===>>', self.settings.process_name, 'input_data:', data)
                    self.list_of_subprocess_input_data = self.list_of_subprocess_input_data[1:]
                else:
                    continue
            else:
                if Transport.pipe == self.settings.transport:
                    data = input_from_parent_process_queue.recv_bytes()
                elif Transport.queue == self.settings.transport:
                    input_size = input_from_parent_process_queue.qsize()
                    self.input_size_print_counter += 1
                    self.input_size_print_sum += input_size
                    if self.input_size_print_counter >= self.input_size_print_counter_limit:
                        average_input_size = self.input_size_print_sum / self.input_size_print_counter
                        self.input_size_print_sum = 0
                        self.input_size_print_counter = 0
                        average_input_size_trigger_result = self.input_queue_average_size_trigger.test_trigger(
                            average_input_size)
                        if average_input_size_trigger_result is not None:
                            if average_input_size_trigger_result:
                                print('===>>', self.settings.process_name, 'average_input_size for Queue:',
                                      average_input_size)
                            else:
                                print('===>>', self.settings.process_name, 'average_input_size for Queue is OK:',
                                      average_input_size)
                            if self.settings.on_input_queue_is_too_big is not None:
                                self.settings.on_input_queue_is_too_big(self.data_shelf,
                                                                        average_input_size_trigger_result)

                    data = input_from_parent_process_queue.get()

            # print('===>>', self.settings.process_name, '_subprocess_wrapper', '2')

            # current_time = time.time()
            # if (current_time - self.last_log_print_time) > 2:
            #     print('===>>', self.settings.process_name, '_subprocess_wrapper')

            if data is None:
                continue

            is_result_was_send = False
            is_worker_is_finalized = False
            is_need_to_break_loop = False

            data = self._decode_sendable_data(data)
            # data = marshal.loads(data)
            if data[0]:
                # print('===>>', self.settings.process_name, '_subprocess_wrapper', '3')
                data_with_exception = data[1]
                data_only = data_with_exception[0]
                result = self._parsing_worker_wrapper(data_only)
                if result is not None:
                    # print('===>>', self.settings.process_name, 'output_result:', result)
                    # print('===>>', self.settings.process_name, '_subprocess_wrapper', '5')
                    result = (True, result)
                    result = self._encode_sendable_data(result)
                    # result = marshal.dumps(result)
                    # output_to_parent_process_queue.put(result)
                    if Transport.pipe == self.settings.transport:
                        output_to_parent_process_queue.send_bytes(result)
                    elif Transport.queue == self.settings.transport:
                        output_to_parent_process_queue.put(result)

                    is_result_was_send = True
                # print('===>>', self.settings.process_name, '_subprocess_wrapper', '5')
            else:
                # print('===>>', self.settings.process_name, '_subprocess_wrapper', '6')

                data_only = [None]
                self._parsing_worker_wrapper(data_only, stop=True)

                is_worker_is_finalized = True
                is_need_to_break_loop = True
                # break

            if (self.settings.on_another_bunch_of_data_was_processed is not None) and is_result_was_send:
                self.settings.on_another_bunch_of_data_was_processed(self.data_shelf)

            if (self.settings.on_exit is not None) and is_worker_is_finalized:
                self.settings.on_exit(self.data_shelf)

            if is_need_to_break_loop:
                break

            # print('<<===', self.settings.process_name, '_subprocess_wrapper')

            # if (current_time - self.last_log_print_time) > 2:
            #     print('<<===', self.settings.process_name, '_subprocess_wrapper')
            #     self.last_log_print_time = current_time

        print(' ENDED:', self.settings.process_name, '; PID:', os.getpid())
        # print('<<===>>', self.settings.process_name, '_subprocess_wrapper')

    def start(self):
        if not self.subprocess_was_initiated:
            if self.queue_to_subprocess is None:
                if Transport.pipe == self.settings.transport:
                    self.queue_to_subprocess = Pipe()
                elif Transport.queue == self.settings.transport:
                    self.queue_to_subprocess = Queue()

            if self.queue_from_subprocess is None:
                if Transport.pipe == self.settings.transport:
                    self.queue_from_subprocess = Pipe()
                elif Transport.queue == self.settings.transport:
                    self.queue_from_subprocess = Queue()

            target = None
            arguments = None
            if self.settings.profile:
                target = _subprocess_wrapper_profile
                arguments = (self,)
            else:
                target = self._subprocess_wrapper
                arguments = tuple()
            self.subprocess = None
            if self.settings.need_multithreading:
                self.subprocess = Thread(target=target, args=arguments, daemon=True)
            else:
                self.subprocess = Process(target=target, args=arguments, daemon=True)
            self.subprocess.start()
            self.subprocess_was_initiated = True

    def stop(self):
        if self.subprocess_was_initiated:
            data = (False, None)
            data = self._encode_sendable_data(data)
            # data = marshal.dumps(data)

            output_to_subprocess_queue = None
            if Transport.pipe == self.settings.transport:
                output_to_subprocess_queue = self.queue_to_subprocess[0]
            elif Transport.queue == self.settings.transport:
                output_to_subprocess_queue = self.queue_to_subprocess

            if Transport.pipe == self.settings.transport:
                output_to_subprocess_queue.send_bytes(data)
            elif Transport.queue == self.settings.transport:
                output_to_subprocess_queue.put(data)
            self.subprocess.join()

    def send_data_to_subprocess(self, input_data):
        """
        If (Transport.pipe == self.settings.transport): Very large buffers (approximately 32 MB+, though it depends on
            the OS) may raise a ValueError exception
        :param input_data:
        :return:
        """
        if self.subprocess_was_initiated:
            data = (True, (input_data, None))
            data = self._encode_sendable_data(data)
            # data = marshal.dumps(data)
            output_to_subprocess_queue = None
            if Transport.pipe == self.settings.transport:
                output_to_subprocess_queue = self.queue_to_subprocess[0]
            elif Transport.queue == self.settings.transport:
                output_to_subprocess_queue = self.queue_to_subprocess

            if Transport.pipe == self.settings.transport:
                output_to_subprocess_queue.send_bytes(data)
            elif Transport.queue == self.settings.transport:
                output_to_subprocess_queue.put(data)

    def is_input_queue_is_empty(self):
        result = None
        if self.subprocess_was_initiated:
            output_to_subprocess_queue = None
            if Transport.pipe == self.settings.transport:
                output_to_subprocess_queue = self.queue_to_subprocess[0]
            elif Transport.queue == self.settings.transport:
                output_to_subprocess_queue = self.queue_to_subprocess

            if Transport.pipe == self.settings.transport:
                result = not output_to_subprocess_queue.poll()
            elif Transport.queue == self.settings.transport:
                result = output_to_subprocess_queue.empty()

            # result = self.queue_to_subprocess.empty()
        return result

    def get_answer_from_subprocess(self, block_queue=False, time_out=None):
        """
        If (Transport.pipe == self.settings.transport): Very large buffers (approximately 32 MB+, though it depends on
            the OS) may raise a ValueError exception
        Will raise Empty() in non-blocking mode when queue is empty
        :param block_queue:
        :param time_out:
        :return:
        """
        always_true = None
        answer = None
        if Transport.pipe == self.settings.transport:
            input_from_subprocess_queue = self.queue_from_subprocess[0]
            if block_queue:
                subprocess_answer = input_from_subprocess_queue.recv_bytes()
                subprocess_answer = self._decode_sendable_data(subprocess_answer)
                # subprocess_answer = marshal.loads(subprocess_answer)
                always_true, answer = subprocess_answer
            else:
                if input_from_subprocess_queue.poll():
                    subprocess_answer = input_from_subprocess_queue.recv_bytes()
                    subprocess_answer = self._decode_sendable_data(subprocess_answer)
                    # subprocess_answer = marshal.loads(subprocess_answer)
                    always_true, answer = subprocess_answer
                else:
                    raise Empty()
        elif Transport.queue == self.settings.transport:
            input_from_subprocess_queue = self.queue_from_subprocess
            subprocess_answer = input_from_subprocess_queue.get(block=block_queue, timeout=time_out)
            subprocess_answer = self._decode_sendable_data(subprocess_answer)
            # subprocess_answer = marshal.loads(subprocess_answer)
            always_true, answer = subprocess_answer
        exception = answer[1]
        result = answer[0]
        if exception is not None:
            exception = pickle.loads(exception)
            print(self.settings.process_name)
            print(result)
            print(exception)
            print()
            print(' <<< SUBPROCESS EXCEPTION:')
            trace = ''
            for line in exception[2]:
                trace += line
            print(trace, file=sys.stderr)
            print(exception[0])
            print(exception[1])
            print(' >>>')
            raise exception[1]
        return result


def _subprocess_wrapper_profile(process_data):
    printable_name = process_data.settings.process_name.replace(' ', '_') + '.prof'
    cProfile.runctx('process_data._subprocess_wrapper()', globals(), locals(), printable_name)


class ExternalPipe:
    def __init__(self):
        self.pipe = Pipe()
        self.inverted_pipe = (self.pipe[1], self.pipe[0])
