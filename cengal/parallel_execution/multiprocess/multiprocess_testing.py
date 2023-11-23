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

from multiprocessing import Process, Queue
import os
from cengal.parallel_execution.multiprocess.multiprocessing_task_runner import *
import sys

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


def funct(inputData):
    result = inputData[0] / inputData[1]
    return result

if __name__ == '__main__':
    process0 = SubprocessWorker(funct)
    process1 = SubprocessWorker(funct)
    process0.start()
    process1.start()
    data0 = (3, 2)
    data1 = (5, 0)
    process0.send_data_to_subprocess(data0)
    process1.send_data_to_subprocess(data1)
    try:
        answer0 = process0.get_answer_from_subprocess()
        print('answer0 = ', answer0)
        answer1 = process1.get_answer_from_subprocess()
        print('answer1 = ', answer1)
    except:
        print()
        print('<<< BROAD EXCEPTION:')
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        print('>>>')
        raise
    process0.stop()
    process1.stop()


#class Multi_Test:
#
#    def __init__(self, queue):
#        self.queue = queue
#
#    def info(self, title):
#        print(title)
#        print('module name:', __name__)
#        if hasattr(os, 'getppid'):  # only available on Unix
#            print('parent process:', os.getppid())
#        print('process id:', os.getpid())
#
#    def f(self, name):
#        self.info('function f')
#        print('hello', name[1])
#        name[0].put('hello')
#
#    def start_process(self, ):
#        self.info('main line')
#        p = Process(target=self.f, args=((self.queue, 'bob'),))
#        p.start()
#        p.join()
#        print(self.queue.get())
#
#if __name__ == '__main__':
#    q = Queue()
#    mp = Multi_Test(q)
#    mp.start_process()

