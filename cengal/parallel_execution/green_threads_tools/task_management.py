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

from typing import Callable, Any, Hashable
from collections import deque
from greenlet import greenlet
from cengal.data_generation.id_generator import IDGenerator, GeneratorType
from cengal.data_containers.simple_tree import Tree
import copy

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


class InitialData:
    def __init__(self, name: Hashable, functor: Callable, data: Any):
        self.name = name  # Any hashable readable ID: 'counter', 124, ...
        self.functor = functor
        self.data = data


class TaskManager:
    def __init__(self):
        self.id_gen = IDGenerator(GeneratorType.integer)
        self.root_id = self.id_gen.get_new_id()
        self.api_per_child_id = dict()
        self.greenlen_per_child_id = dict()

    def run(self):
        pass

    def create_task(self, initial_data_for_the_child: InitialData, creator_id: Hashable=None)->TaskAPI:
        creator_id = creator_id or self.root_id
        task_api = TaskAPI(self, initial_data_for_the_child, self.api_per_child_id[creator_id or self.root_id])
        return task_api

    def put_task(self, task_api: TaskAPI):
        self.api_per_child_id[task_api.task_id] = task_api

    def run_task(self, task_id: Hashable):
        task_api = self.api_per_child_id[task_id]
        return task_api.greenlet(task_api)


class TaskAPI:
    def __init__(self, task_manager: TaskManager, initial_data: InitialData, parent_task: 'TaskAPI'=None):
        self._task_manager = task_manager
        self._initial_data = initial_data
        self._parent_task = parent_task
        self._task_id = task_manager.id_gen.get_new_id()
        if self._parent_task:
            self._path = deque(self._parent_task.path)
        else:
            self._path = deque()
        self._path.append(self._task_id)
        self._greenlet = greenlet(initial_data.functor)

    @property
    def task_id(self):
        return self._task_id

    @property
    def path(self):
        return self._path

    @property
    def greenlet(self):
        return self._greenlet

# class TaskManager(greenlet):
#     def __init__(self, initial_data_for_the_first_child: InitialData=None, parent: greenlet=None):
#         ## Похоже стоит этот клас сделать НЕнаследником гринлетов. Для того чтобы сделать отдельный TaskAPI для рута
#         ## в этом случае будет меньше оверхеда на if во время работы алгоритма
#         super().__init__(None, parent)
