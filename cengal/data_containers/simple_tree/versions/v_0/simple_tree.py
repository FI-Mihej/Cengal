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
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


__all__ = ['PathDoesNotExist', 'tree_to_list', 'travers_tree', 'Tree']

#!/usr/bin/env python
# coding=utf-8



from typing import Iterable, Dict, Callable, Hashable
from collections import deque






class PathDoesNotExist(Exception):
    pass


def tree_to_list(tree: Dict)->Iterable[Hashable]:
    """
    Returns all items from a tree in a iterable container.
        tree = Tree()
        ...
        all_items =  tree_to_list(tree.get_subtree())
    Is an implementation of the Tree.get_all_children() method.
    :param tree: "dict of dict of ...". F
    :return: some fast Iterable container. deque() usually
    """
    result = deque()
    for key, subtree in tree.items():
        result.append(key)
        if subtree:
            result.extend(tree_to_list(subtree))
    return result


def travers_tree(tree: Dict, functor: Callable):
    """
    Will call 'functor' for an each item in a tree
    :param tree: current traversed subtree
    :param functor: any callable with one parameter: functor(key: Hashable)
    """
    for key, subtree in tree.items():
        functor(key)
        if subtree:
            travers_tree(subtree, functor)


def travers_tree_with_path(tree: Dict, functor: Callable, path: Iterable[Hashable]=None):
    """
    The same as travers_tree(). But also gives current path to a 'functor'
    :param tree: current traversed subtree
    :param functor: any callable with two parameters: functor(key: Hashable, path: Iterable[Hashable])
    :param path: initial actual path for the current traversed subtree
    """
    current_path = path or deque()
    for key, subtree in tree.items():
        functor(key, current_path + deque((key,)))
        if subtree:
            travers_tree_with_path(subtree, functor, current_path + deque((key,)))


class Tree:
    def __init__(self):
        self._data = dict()

    def put(self, path: Iterable[Hashable]):
        current_node = self._data
        for item in path:
            if item not in current_node:
                current_node[item] = dict()
            current_node = current_node[item]

    def get_subtree(self, path: Iterable[Hashable]=None)->Dict:
        path = path or deque()
        current_path = deque()
        current_node = self._data
        for item in path:
            current_path.append(item)
            if item in current_node:
                current_node = current_node[item]
            else:
                raise PathDoesNotExist(current_path)
        return current_node

    def get_immediate_children(self, path: Iterable[Hashable]=None)->Iterable[Hashable]:
        """
        Will return immediate children list of the given path: without children of children
        :param path:
        :return:
        """
        return deque(self.get_subtree(path))

    def get_all_children(self, path: Iterable[Hashable]=None)->Iterable[Hashable]:
        """
        Will rerun all children and children of children for the given path
        The same as tree_to_list() function but for current object and for the given path
        :param path: path to subtree
        :return:
        """
        return tree_to_list(self.get_subtree(path))

    def travers_subtree(self, functor: Callable, path: Iterable[Hashable]=None):
        """
        The same as travers_tree() function but for current object and for the given path
        :param path:
        :param functor:
        """
        travers_tree(self.get_subtree(path), functor)

    def travers_tree_with_path(self, functor: Callable, path: Iterable[Hashable]=None):
        """
        The same as travers_tree_with_path() function but for current object and for the given path
        :param functor:
        :param path:
        """
        travers_tree_with_path(self.get_subtree(path), functor, path)
