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


__all__ = ['AnAppropriateValues', 'AllPossibleValues', 'AnAppropriateContainers', 'data_2_tuple', 'TreeTraversalType', 'TreeTraversal']


from typing import Union, Dict, Set, List, Tuple, Optional, Callable
from enum import Enum
from collections import deque
from cengal.code_flow_control.smart_values import ValueExistence
from cengal.data_containers.stack import StackItem, TreeStackItem, Stack, recursion_insureness

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


AnAppropriateValues = Union[str, bytes, int, float, None]
AllPossibleValues = Union['AnAppropriateContainers', AnAppropriateValues]
AnAppropriateContainers = Union[Dict[AnAppropriateValues, AllPossibleValues],
                                Set[AllPossibleValues],
                                List[AllPossibleValues],
                                Tuple[AllPossibleValues]]


def data_2_tuple(data: AllPossibleValues) -> AllPossibleValues:
    if isinstance(data, (dict, tuple, list, set, deque)):
        if isinstance(data, dict):
            return tuple(data.values())
        elif isinstance(data, (tuple, list, deque)):
            return data
        elif isinstance(data, set):
            return tuple(data)
    else:
        return data


class TreeTraversalType(Enum):
    recursive = 0
    stack_based = 1
    recursive_with_stack_based_insureness = 2


class TreeTraversal:
    def __init__(self,
                 tree: AnAppropriateContainers=None,
                 on_node: Optional[Callable]=None,
                 on_child: Optional[Callable]=None,
                 on_switched_to_stack_based_implementation: Optional[Callable]=None
                 ):
        self._tree = tree  # type: AnAppropriateContainers

        self._callback_on_node = on_node  # type: Optional[Callable]
        self._callback_on_child = on_child  # type: Optional[Callable]
        self._on_switched_to_stack_based_implementation = \
            on_switched_to_stack_based_implementation  # type: Optional[Callable]

        self._last_tree_node = ValueExistence(False, None)
        self._last_tree_child = ValueExistence(False, None)
        self._empty_child = ValueExistence(False, None)

    def set_callback_on_node(self, functor: Optional[Callable]):
        self._callback_on_node = functor

    def set_callback_on_child(self, functor: Optional[Callable]):
        self._callback_on_child = functor

    def set_callback_on_both_node_and_child(self, functor: Optional[Callable]):
        self._callback_on_node = self._callback_on_child = functor

    def set_callback_on_switched_to_stack_based_implementation(self, functor: Optional[Callable]):
        self._on_switched_to_stack_based_implementation = functor

    @property
    def tree(self) -> AnAppropriateContainers:
        return self._tree

    @tree.setter
    def tree(self, tree: AnAppropriateContainers):
        self._tree = tree

    def _traversal_recursive(self):
        tree_tuple = data_2_tuple(self.tree)
        if isinstance(self.tree, dict):
            self._last_tree_node.value = self.tree
            if self._callback_on_node:
                self._callback_on_node(self._last_tree_node, self._empty_child, None)
            self._last_tree_node.value = tree_tuple
        else:
            self._last_tree_child.value = self.tree
            if self._callback_on_child:
                self._callback_on_child(self._last_tree_node, self._last_tree_child, None)

        self._traversal_recursive_impl(tree_tuple)

    def _traversal_recursive_impl(self, tree: AnAppropriateContainers):
        if isinstance(tree, (tuple, list, deque)):
            index = 0
            for item in tree:
                next_child = item
                next_child_tuple = data_2_tuple(next_child)
                if isinstance(next_child, (dict, set, tuple, list, deque)):
                    self._last_tree_node.value = next_child
                    if self._callback_on_node:
                        self._callback_on_node(self._last_tree_node, self._empty_child, None)
                    self._last_tree_node.value = next_child_tuple
                else:
                    self._last_tree_child.value = next_child
                    if self._callback_on_child:
                        self._callback_on_child(self._last_tree_node, self._last_tree_child, index)

                self._traversal_recursive_impl(next_child_tuple)
                index += 1

    def _traversal_stack_based(self):
        tree_tuple = data_2_tuple(self.tree)
        if isinstance(self.tree, dict):
            self._last_tree_node.value = self.tree
            if self._callback_on_node:
                self._callback_on_node(self._last_tree_node, self._empty_child, None)
            self._last_tree_node.value = tree_tuple
        else:
            self._last_tree_child.value = self.tree
            if self._callback_on_child:
                self._callback_on_child(self._last_tree_node, self._last_tree_child, None)

        stack = Stack(TreeStackItem(tree_tuple))
        while stack:
            if stack.top().child is None:
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
                    next_child = stack.top().node[stack.top().child]
                    next_child_tuple = data_2_tuple(next_child)
                    if isinstance(next_child, (dict, set, tuple, list, deque)):
                        self._last_tree_node.value = next_child
                        if self._callback_on_node:
                            self._callback_on_node(self._last_tree_node, self._empty_child, None)
                        self._last_tree_node.value = next_child_tuple
                    else:
                        self._last_tree_child.value = next_child
                        if self._callback_on_child:
                            self._callback_on_child(self._last_tree_node, self._last_tree_child, stack.top().child)

                    stack.push(TreeStackItem(next_child_tuple))
                    continue
                else:
                    stack.pop()
                    continue

    def __call__(self, traversal_type: TreeTraversalType=TreeTraversalType.recursive_with_stack_based_insureness):
        if TreeTraversalType.recursive == traversal_type:
            self._traversal_recursive()
        elif TreeTraversalType.stack_based == traversal_type:
            self._traversal_stack_based()
        else:
            recursion_insureness(self._traversal_recursive,
                                 self._traversal_stack_based,
                                 self._on_switched_to_stack_based_implementation)
