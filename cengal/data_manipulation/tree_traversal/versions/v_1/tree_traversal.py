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


__all__ = ['AnAppropriateValues', 'AllPossibleValues', 'AnAppropriateContainers', 'data_2_tuple', 'data_2_ordered', 'TreeTraversalType', 'TreeTraversal']
__all__ = ['AnAppropriateValues', 'AllPossibleValues', 'AnAppropriateContainers', 'TupledDict', 'Contaiters', 'data_2_tuple', 'data_2_ordered', 'TreeTraversalType', 'NodeType', 'EntityType', 'findout_entity_type', 'TreeTraversal', 'KeyMultiValueTreeTraversal', 'KeyValueTreeTraversal']


from functools import partial
from typing import Any, Hashable, Union, Dict, Set, List, Tuple, Optional, Callable
from enum import Enum
from collections import deque
from cengal.code_flow_control.smart_values import ValueExistence, ValueType
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


class TupledDict:
    def __init__(self, data: Dict) -> None:
        self.dict: Dict = data
        self.items: Tuple[Tuple[Hashable, Any]] = tuple(data.items())


Contaiters = (TupledDict, dict, tuple, list, set, deque)


def data_2_tuple(data: AllPossibleValues) -> AllPossibleValues:
    if isinstance(data, Contaiters):
        if isinstance(data, dict):
            return tuple(data.values())
        elif isinstance(data, (tuple, list, deque)):
            return data
        elif isinstance(data, set):
            return tuple(data)
    else:
        return data


def data_2_ordered(data: AllPossibleValues) -> AllPossibleValues:
    if isinstance(data, Contaiters):
        if isinstance(data, dict):
            return TupledDict(data)
        elif isinstance(data, set):
            return tuple(data)
        else:
            return data
    else:
        return data


class TreeTraversalType(Enum):
    recursive = 0
    stack_based = 1
    recursive_with_stack_based_insureness = 2


class NodeType(Enum):
    dict = 0
    dict_item = 1
    sequence = 2


class EntityType(Enum):
    dict = 0
    dict_item = 1
    sequence = 2
    child = 3


def findout_entity_type(entity) -> EntityType:
    if isinstance(entity, Contaiters):
        if isinstance(entity, TupledDict):
            entity_type: EntityType = EntityType.dict
        else:
            entity_type = EntityType.sequence
    else:
        entity_type = EntityType.child
    
    return entity_type


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
        ordered_tree = data_2_ordered(self.tree)
        self._traversal_recursive_impl(ordered_tree)

    def _traversal_recursive_impl(self, entity: AnAppropriateContainers, deep: int = 0, index: Optional[int] = None):
        if isinstance(entity, Contaiters):
            last_tree_node_bak = self._last_tree_node
            if isinstance(entity, TupledDict):
                node_type: NodeType = NodeType.dict
            else:
                node_type = NodeType.sequence
            
            self._last_tree_node.value = ValueType(node_type, entity)
            if self._callback_on_node:
                self._callback_on_node(deep, self._last_tree_node, self._empty_child, index)

            new_deep = deep + 1
            if isinstance(entity, TupledDict):
                value_deep = new_deep + 1
                for index, node in enumerate(entity.items):
                    self._last_tree_node.value = ValueType(NodeType.dict_item, node)
                    if self._callback_on_node:
                        self._callback_on_node(new_deep, self._last_tree_node, self._empty_child, index)
                    
                    item = node[1]
                    self._traversal_recursive_impl(data_2_ordered(item), value_deep, 0)
            else:
                for index, item in enumerate(entity):
                    self._traversal_recursive_impl(data_2_ordered(item), new_deep, index)

            self._last_tree_node = last_tree_node_bak
        else:
            self._last_tree_child.value = entity
            if self._callback_on_child:
                self._callback_on_child(deep, self._last_tree_node, self._last_tree_child, index)

    def _traversal_stack_based(self):
        index: Optional[int] = None
        deep: int = 0
        entity = data_2_ordered(self.tree)
        entity_type: EntityType = findout_entity_type(entity)
        stack = Stack(TreeStackItem((entity_type, entity, deep, index)))
        while stack:
            top = stack.top()
            entity_type, entity, deep, index = top.node
            if EntityType.child == entity_type:
                self._last_tree_child.value = entity
                if self._callback_on_child:
                    self._callback_on_child(deep, self._last_tree_node, self._last_tree_child, index)
                
                stack.pop()
            elif EntityType.sequence == entity_type:
                self._last_tree_node.value = ValueType(NodeType.sequence, entity)
                if top.child is None:
                    child_index = 0
                    if self._callback_on_node:
                        self._callback_on_node(deep, self._last_tree_node, self._empty_child, index)
                else:
                    child_index = top.child + 1
                
                if len(entity) > child_index:
                    top.child = child_index
                    child = data_2_ordered(entity[child_index])
                    child_type = findout_entity_type(child)
                    stack.push(TreeStackItem((child_type, child, deep + 1, child_index)))
                else:
                    stack.pop()
            elif EntityType.dict_item == entity_type:
                self._last_tree_node.value = ValueType(NodeType.dict_item, entity)
                if top.child is None:
                    child_index = 0
                    if self._callback_on_node:
                        self._callback_on_node(deep, self._last_tree_node, self._empty_child, index)

                    top.child = child_index
                    child = data_2_ordered(entity[1])
                    child_type = findout_entity_type(child)
                    stack.push(TreeStackItem((child_type, child, deep + 1, child_index)))
                else:
                    stack.pop()
            elif EntityType.dict == entity_type:
                self._last_tree_node.value = ValueType(NodeType.dict, entity.dict)
                if top.child is None:
                    child_index = 0
                    if self._callback_on_node:
                        self._callback_on_node(deep, self._last_tree_node, self._empty_child, index)
                else:
                    child_index = top.child + 1
                
                if len(entity.items) > child_index:
                    top.child = child_index
                    child = entity.items[child_index]
                    stack.push(TreeStackItem((EntityType.dict_item, child, deep + 1, child_index)))
                else:
                    stack.pop()

    def __call__(self, traversal_type: TreeTraversalType=TreeTraversalType.recursive_with_stack_based_insureness):
        if TreeTraversalType.recursive == traversal_type:
            self._traversal_recursive()
        elif TreeTraversalType.stack_based == traversal_type:
            self._traversal_stack_based()
        else:
            recursion_insureness(self._traversal_recursive,
                                 self._traversal_stack_based,
                                 self._on_switched_to_stack_based_implementation)


class KeyMultiValueTreeTraversal:
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

    def _traversal_recursive(self, initial_key: Hashable):
        index: Optional[int] = None
        deep: int = 0
        self._last_tree_child.value = initial_key
        if self._callback_on_child:
            self._callback_on_child(deep, self._last_tree_node, self._last_tree_child, index)

        try:
            entity = self.tree[initial_key]
        except KeyError:
            return

        self._last_tree_node.value = initial_key
        if self._callback_on_node:
            self._callback_on_node(deep, self._last_tree_node, self._empty_child, index)

        entity = data_2_ordered(entity)
        self._traversal_recursive_impl(entity, deep, index)

    def _traversal_recursive_impl(self, entity: AnAppropriateContainers, deep: int = 0, index: Optional[int] = None):
        if isinstance(entity, Contaiters):
            last_tree_node_bak = self._last_tree_node
            new_deep = deep + 1
            for index, item in enumerate(entity):
                self._traversal_recursive_impl(item, new_deep, index)
                self._last_tree_node = last_tree_node_bak
        else:
            key = entity
            index: Optional[int] = None
            deep: int = 0
            self._last_tree_child.value = key
            if self._callback_on_child:
                self._callback_on_child(deep, self._last_tree_node, self._last_tree_child, index)
            
            try:
                entity = self.tree[key]
            except KeyError:
                return

            self._last_tree_node.value = key
            if self._callback_on_node:
                self._callback_on_node(deep, self._last_tree_node, self._empty_child, index)

            entity = data_2_ordered(entity)
            self._traversal_recursive_impl(entity, deep, index)

    def _traversal_stack_based(self, initial_key: Hashable):
        raise NotImplementedError
        index: Optional[int] = None
        deep: int = 0
        key: Hashable = initial_key
        entity = data_2_ordered(self.tree)
        entity_type: EntityType = findout_entity_type(entity)
        stack = Stack(TreeStackItem((entity_type, entity, key, deep, index)))
        while stack:
            top = stack.top()
            entity_type, entity, key, deep, index = top.node
            if EntityType.child == entity_type:
                self._last_tree_child.value = entity
                if self._callback_on_child:
                    self._callback_on_child(deep, self._last_tree_node, self._last_tree_child, index)
                
                stack.pop()
            elif EntityType.sequence == entity_type:
                self._last_tree_node.value = ValueType(NodeType.sequence, entity)
                if top.child is None:
                    child_index = 0
                    if self._callback_on_node:
                        self._callback_on_node(deep, self._last_tree_node, self._empty_child, index)
                else:
                    child_index = top.child + 1
                
                if len(entity) > child_index:
                    top.child = child_index
                    child = data_2_ordered(entity[child_index])
                    child_type = findout_entity_type(child)
                    stack.push(TreeStackItem((child_type, child, deep + 1, child_index)))
                else:
                    stack.pop()
            elif EntityType.dict_item == entity_type:
                self._last_tree_node.value = ValueType(NodeType.dict_item, entity)
                if top.child is None:
                    child_index = 0
                    if self._callback_on_node:
                        self._callback_on_node(deep, self._last_tree_node, self._empty_child, index)

                    top.child = child_index
                    child = data_2_ordered(entity[1])
                    child_type = findout_entity_type(child)
                    stack.push(TreeStackItem((child_type, child, deep + 1, child_index)))
                else:
                    stack.pop()
            elif EntityType.dict == entity_type:
                self._last_tree_node.value = ValueType(NodeType.dict, entity.dict)
                if top.child is None:
                    child_index = 0
                    if self._callback_on_node:
                        self._callback_on_node(deep, self._last_tree_node, self._empty_child, index)
                else:
                    child_index = top.child + 1
                
                if len(entity.items) > child_index:
                    top.child = child_index
                    child = entity.items[child_index]
                    stack.push(TreeStackItem((EntityType.dict_item, child, deep + 1, child_index)))
                else:
                    stack.pop()

    def __call__(self, initial_key: Hashable, traversal_type: TreeTraversalType=TreeTraversalType.recursive_with_stack_based_insureness):
        if TreeTraversalType.recursive == traversal_type:
            self._traversal_recursive(initial_key)
        elif TreeTraversalType.stack_based == traversal_type:
            self._traversal_stack_based(initial_key)
        else:
            recursive = partial(self._traversal_recursive, initial_key)
            stack_based = partial(self._traversal_stack_based, initial_key)
            recursion_insureness(recursive,
                                 stack_based,
                                 self._on_switched_to_stack_based_implementation)


class KeyValueTreeTraversal:
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

    def _traversal_recursive(self, initial_key: Hashable):
        index: Optional[int] = None
        deep: int = 0
        self._last_tree_child.value = initial_key
        if self._callback_on_child:
            self._callback_on_child(deep, self._last_tree_node, self._last_tree_child, index)

        try:
            entity = self.tree[initial_key]
        except KeyError:
            return

        self._last_tree_node.value = initial_key
        if self._callback_on_node:
            self._callback_on_node(deep, self._last_tree_node, self._empty_child, index)

        self._traversal_recursive_impl(entity, deep + 1, index)

    def _traversal_recursive_impl(self, entity: AnAppropriateContainers, deep: int = 0, index: Optional[int] = None):
        key = entity
        index: Optional[int] = None
        deep: int = 0
        self._last_tree_child.value = key
        if self._callback_on_child:
            self._callback_on_child(deep, self._last_tree_node, self._last_tree_child, index)
        
        try:
            entity = self.tree[key]
        except KeyError:
            return

        self._last_tree_node.value = key
        if self._callback_on_node:
            self._callback_on_node(deep, self._last_tree_node, self._empty_child, index)

        self._traversal_recursive_impl(entity, deep + 1, index)

    def _traversal_stack_based(self, initial_key: Hashable):
        raise NotImplementedError
        index: Optional[int] = None
        deep: int = 0
        key: Hashable = initial_key
        entity = data_2_ordered(self.tree)
        entity_type: EntityType = findout_entity_type(entity)
        stack = Stack(TreeStackItem((entity_type, entity, key, deep, index)))
        while stack:
            top = stack.top()
            entity_type, entity, key, deep, index = top.node
            if EntityType.child == entity_type:
                self._last_tree_child.value = entity
                if self._callback_on_child:
                    self._callback_on_child(deep, self._last_tree_node, self._last_tree_child, index)
                
                stack.pop()
            elif EntityType.sequence == entity_type:
                self._last_tree_node.value = ValueType(NodeType.sequence, entity)
                if top.child is None:
                    child_index = 0
                    if self._callback_on_node:
                        self._callback_on_node(deep, self._last_tree_node, self._empty_child, index)
                else:
                    child_index = top.child + 1
                
                if len(entity) > child_index:
                    top.child = child_index
                    child = data_2_ordered(entity[child_index])
                    child_type = findout_entity_type(child)
                    stack.push(TreeStackItem((child_type, child, deep + 1, child_index)))
                else:
                    stack.pop()
            elif EntityType.dict_item == entity_type:
                self._last_tree_node.value = ValueType(NodeType.dict_item, entity)
                if top.child is None:
                    child_index = 0
                    if self._callback_on_node:
                        self._callback_on_node(deep, self._last_tree_node, self._empty_child, index)

                    top.child = child_index
                    child = data_2_ordered(entity[1])
                    child_type = findout_entity_type(child)
                    stack.push(TreeStackItem((child_type, child, deep + 1, child_index)))
                else:
                    stack.pop()
            elif EntityType.dict == entity_type:
                self._last_tree_node.value = ValueType(NodeType.dict, entity.dict)
                if top.child is None:
                    child_index = 0
                    if self._callback_on_node:
                        self._callback_on_node(deep, self._last_tree_node, self._empty_child, index)
                else:
                    child_index = top.child + 1
                
                if len(entity.items) > child_index:
                    top.child = child_index
                    child = entity.items[child_index]
                    stack.push(TreeStackItem((EntityType.dict_item, child, deep + 1, child_index)))
                else:
                    stack.pop()

    def __call__(self, initial_key: Hashable, traversal_type: TreeTraversalType=TreeTraversalType.recursive_with_stack_based_insureness):
        if TreeTraversalType.recursive == traversal_type:
            self._traversal_recursive(initial_key)
        elif TreeTraversalType.stack_based == traversal_type:
            self._traversal_stack_based(initial_key)
        else:
            recursive = partial(self._traversal_recursive, initial_key)
            stack_based = partial(self._traversal_stack_based, initial_key)
            recursion_insureness(recursive,
                                 stack_based,
                                 self._on_switched_to_stack_based_implementation)
