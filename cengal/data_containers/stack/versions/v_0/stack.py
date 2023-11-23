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

from typing import Any, Optional, Callable, Union
from collections import deque

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


class TreeStackItem:
    __slots__ = ('node', 'child')

    def __init__(self, node: Any, child: Optional[int]=None):
        self.node = node  # container
        self.child = child  # an item id in container


class DeepTreeStackItem(TreeStackItem):
    __slots__ = ('node', 'child', 'deep')

    def __init__(self, deep: int, node: Any, child: Optional[int] = None):
        super().__init__(node, child)
        self.deep: int = deep


StackItem = Union[TreeStackItem, DeepTreeStackItem, Any]


class Stack:
    def __init__(self, initial_state: Optional[StackItem]=None):
        self._stack = deque()
        if initial_state:
            self.push(initial_state)

    def push(self, state: StackItem):
        self._stack.append(state)

    def pop(self) -> StackItem:
        return self._stack.pop()

    def top(self) -> StackItem:
        return self._stack[-1]

    def __len__(self):
        return len(self._stack)


class StackUni(Stack):
    def __init__(self, initial_state: Optional[StackItem]=None, remove_on_pop: bool=True):
        super(StackUni, self).__init__(initial_state)
        self._stack = deque()
        self._stack_top = -1
        self._remove_on_pop = remove_on_pop
        if self._remove_on_pop:
            self.push = self._push_remove
            self.pop = self._pop_remove
            self.top = self._top_remove
            self._len__impl = self._len__impl_remove
        else:
            self.push = self._push_keep
            self.pop = self._pop_keep
            self.top = self._top_keep
            self._len__impl = self._len__impl_keep

        if initial_state:
            self.push(initial_state)

    def _push_remove(self, state: StackItem):
        self._stack.append(state)

    def _pop_remove(self) -> StackItem:
        return self._stack.pop()

    def _top_remove(self) -> StackItem:
        return self._stack[-1]

    def _push_keep(self, state: StackItem):
        # print('_push_keep: {}'.format(self._stack_top))
        self._stack_top += 1
        if len(self._stack) > self._stack_top:
            # we are not on a real top
            self._stack[self._stack_top] = state
        else:
            # We are on the real top - need to increase stack size
            self._stack.append(state)

    def _pop_keep(self) -> StackItem:
        # print('_pop_keep: {}'.format(self._stack_top))
        result = self._stack[self._stack_top]
        self._stack_top -= 1
        return result

    def _top_keep(self) -> StackItem:
        # print('_top_keep: {}'.format(self._stack_top))
        return self._stack[self._stack_top]

    def _len__impl_remove(self):
        return len(self._stack)

    def _len__impl_keep(self):
        return self._stack_top + 1

    def __len__(self):
        return self._len__impl()


def recursion_insureness(recursive_functor: Callable,
                         stack_based_functor: Callable,
                         on_changed_to_drop_in_replacement: Optional[Callable],
                         *args, **kwargs):
    try:
        return recursive_functor(*args, **kwargs)
    except RecursionError:
        pass

    if on_changed_to_drop_in_replacement:
        on_changed_to_drop_in_replacement()
    return stack_based_functor(*args, **kwargs)


recursion_drop_in_replacement = recursion_insureness
recursion_fallback_to_stack_based = recursion_insureness
