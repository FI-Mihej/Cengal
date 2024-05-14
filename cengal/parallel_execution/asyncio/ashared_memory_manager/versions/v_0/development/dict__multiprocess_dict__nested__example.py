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
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import multiprocessing
from multiprocessing import shared_memory, Semaphore, Process, Manager
from cengal.performance_test_lib import MeasureTimeTraceLine, LineType
from cengal.introspection.inspect import pifrl
from enum import IntEnum
from time import sleep

from typing import List, Dict


class ControlFields(IntEnum):
    data_state = 0
    sender_ready = 1
    receiver_ready = 2


class ControlDataState(IntEnum):
    data_ready = 0
    processing_requested = 1
    processing_done = 2


def receiver(data_dict, data_list, control):
    pifrl()
    control[ControlFields.receiver_ready] = True
    d = data_dict
    l = data_list
    while ControlDataState.processing_requested.value != control[ControlFields.data_state]:
        # sleep(0.5)
        # print('Waiting for sender', control)
        pass

    try:
        d[1] = '1'
        d['2'] = 2
        d[0.25] = None
        d['hello']['w'] = 1
        d['hello']['world'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        l.reverse()
        control[0] = True
    finally:
        control[ControlFields.data_state] = ControlDataState.processing_done.value


def sender(data_dict, data_list, control: List):
    pifrl()
    d = data_dict
    l = data_list
    control[ControlFields.sender_ready] = True
    while not control[ControlFields.receiver_ready]:
        # sleep(0.5)
        # print('Waiting for receiver', control)
        pass

    with MeasureTimeTraceLine('Data processing', line_type=LineType.relative_line, line_num=-4) as mt:
        control[ControlFields.data_state] = ControlDataState.processing_requested.value
        while ControlDataState.processing_done.value != control[ControlFields.data_state]:
            # sleep(0.5)
            # print('Waiting for processed data', control)
            pass

    print(d)
    print(dict(d['hello']))
    print(l)


def main():
    pifrl()
    with Manager() as manager:
        d = manager.dict()
        d['hello'] = manager.dict({
            'world': 1,
            'world2': 2
        })
        l = manager.list(range(10))
        control = manager.list([ControlDataState.data_ready, False, False])

        # Create shared memory
        # Create and start processes
        process_receiver = Process(target=receiver, args=(d, l, control))
        process_sender = Process(target=sender, args=(d, l, control))

        process_receiver.start()
        process_sender.start()

        # Wait for processes to complete
        process_sender.join()
        process_receiver.join()

if __name__ == '__main__':
    main()
