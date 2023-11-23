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

from cengal.data_manipulation.tree_traversal import *
from cengal.data_containers.stack import *

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


def objects_counter(data: AnAppropriateContainers):
    obj_sum = 0
    stack = Stack(TreeStackItem(data_2_tuple(data)))
    # stack = StackUni(TreeStackItem(data_2_tuple(data)), remove_on_pop=False)
    while stack:
        # print(obj_summ)
        # print(stack.top().node)
        # print(stack.top().child)
        # print()
        if stack.top().child is None:
            obj_sum += 1
            if isinstance(stack.top().node, (tuple, list, deque)):
                if stack.top().node:
                    stack.top().child = -1
                    continue
                else:
                    stack.pop()
                    continue
            else:
                stack.pop()
                continue
        else:
            stack.top().child += 1
            if len(stack.top().node) > stack.top().child:
                stack.push(TreeStackItem(data_2_tuple(stack.top().node[stack.top().child])))
                continue
            else:
                stack.pop()
                continue
    return obj_sum


def _objects_counter_recursive_impl(data: AnAppropriateContainers) -> int:
    obj_sum = 1
    if isinstance(data, (tuple, list, deque)):
        for item in data:
            obj_sum += _objects_counter_recursive_impl(data_2_tuple(item))
    return obj_sum


def objects_counter_recursive(data: AnAppropriateContainers) -> int:
    return _objects_counter_recursive_impl(data_2_tuple(data))


def object_counter_uni(data: AnAppropriateContainers, on_changed_to_drop_in_replacement: Optional[Callable] = None) -> int:
    return recursion_insureness(objects_counter_recursive, objects_counter, on_changed_to_drop_in_replacement, data)
