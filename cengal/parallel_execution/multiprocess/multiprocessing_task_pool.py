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

from .multiprocessing_task_runner import SubprocessWorker
from cengal.data_generation.id_generator import IDGenerator

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


class SingleTaskInfo:
    def __init__(self, process=None, taskId=None):
        super().__init__()
        self.process = process
        self.isNeedToBeClosed = False
        self.uncompletedTasksQnt = 0  # хочу что бы оно было тут, а не в классе процесса: хочу чтобы класс процесса был
            # thread safe без локов
        self.taskId = taskId


class TaskPool:
    def __init__(self, processesQnt, working_function, initiation_function=None):
        super().__init__()
        self._processesQnt = processesQnt
        self._working_function = working_function
        self._initiation_function = initiation_function
        self._processesIdGenerator = IDGenerator()
        self._taskList = set()
        self._taskDict = dict()
        for processNumber in range(self._processesQnt):
            taskId = self._processesIdGenerator.get_new_ID()
            process = SubprocessWorker(self._working_function, self._initiation_function)
            task = SingleTaskInfo(process, taskId)
            self._taskList.add(taskId)
            self._taskDict[taskId] = task
        ...

    def get_processes_qnt(self):
        return self._processesQnt

    def set_processes_qnt(self, processesQnt):
        ...

    def _send_data_to_subprocess(self, inputData, processId):
        ...

    def _get_answer_from_subprocess(self, processId):
        ...

    def send_data_to_the_pool(self, inputData):
        ...

    def get_answer_from_the_pool(self):
        ...

    def send_list_of_data_to_the_pool(self, listOfData):
        ...

    def get_list_of_answers_from_the_pool(self):
        ...

    def stop_pool(self):
        ...

    ...



def rpc_blocking():
    pass
