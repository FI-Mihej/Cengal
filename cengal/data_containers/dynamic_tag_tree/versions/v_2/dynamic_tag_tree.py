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


from typing import Set, Dict, Tuple, Any, Hashable, Optional, FrozenSet, Callable


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


ItemID = Hashable
TagID = Hashable
UniqueItemID = Hashable


class UniqueIdGen:
    def __init__(self):
        self.index = 0

    def __call__(self):
        result = self.index
        self.index += 1
        return result


def tags_set_2_tuple(tags: Set[TagID]) -> Tuple[TagID]:
    tags_list = list(tags)
    tags_list.sort()
    return tuple(tags_list)


def default_growth_during_the_search_checker(): return True


def default_scheduler(): pass


class TagNotFound(Exception):
    pass


class DynamicTagTree:
    def __init__(self,
                 growth_during_the_search_is_allowed: Optional[Callable] = None,
                 scheduler: Optional[Callable] = None):
        self.growth_during_the_search_is_allowed: Callable = \
            growth_during_the_search_is_allowed or default_growth_during_the_search_checker
        self.scheduler: Callable = scheduler or default_scheduler
        self.uiidg = UniqueIdGen()
        self.item_by_uiid: Dict[UniqueItemID, Tuple[ItemID, FrozenSet[TagID]]] = dict()
        self.uiid_by_item: Dict[Tuple[ItemID, FrozenSet[TagID]], UniqueItemID] = dict()
        self.item_tags_by_tag: Dict[TagID, Set[FrozenSet[TagID]]] = dict()
        self.neighbor_tags_of_a_tag: Dict[TagID, Set[TagID]] = dict()
        self.set_of_tags: Set[TagID] = set()
        self.direct_items_by_tags: Dict[FrozenSet[TagID], Set[ItemID]] = dict()
        self.tags_by_number_of_tags: Dict[int, Set[FrozenSet[TagID]]] = dict()
        
        # self.tags_by_number_of_tags_by_tag: Dict[TagID, Dict[int, Set[FrozenSet[TagID]]]] = dict()
        self.tags_len_by_tag: Dict[TagID, int] = dict()  # key: tag; value: keyb  from self.tags_by_number_of_tags
        
        self.tags_by_number_of_tags_by_tag_by_near_tag: Dict[TagID, Dict[TagID, Dict[int, Set[FrozenSet[TagID]]]]] = \
            dict()  # Dict[interested tag, Dict[near tag, Dict[len of tags set, Set[tag sets]]]]
        self.tags_len_by_tag_by_near_tag: Dict[TagID, Dict[TagID, int]] = \
            dict()  # Dict[interested tag, Dict[near tag, len of tags set]]
        
        self.tags_inclusion_by_tags: Dict[FrozenSet[TagID], Set[FrozenSet[TagID]]] = dict()  # key: interested tags set;
        # value: bigger tags sets which includes interested tags set
        self.tag_weight_by_tag_by_tags: Dict[FrozenSet[TagID], Dict[TagID, int]] = dict()
        self.tags_by_tag_weight_by_tags: Dict[FrozenSet[TagID], Dict[int, Set[TagID]]] = dict()
        self.nearest_non_empty_tags_by_some_tags: Dict[FrozenSet[TagID], Set[FrozenSet[TagID]]] = dict()  # key: any
        # interested tags set (input from user); value: set of known tags sets which has an item(-s) and includes given
        # interested tags set
        self.tags_by_itself: Dict[FrozenSet[TagID], FrozenSet[TagID]] = dict()  # key: tags; value: same tags object

    def set_scheduler(self, scheduler: Optional[Callable]):
        self.scheduler = scheduler or default_scheduler

    def get_scheduler(self):
        return self.scheduler

    def put(self, item_id: ItemID, tags: FrozenSet[TagID]) -> UniqueItemID:
        unique_item_id: UniqueItemID = self.uiidg()
        item = (item_id, tags)
        tags_len = len(tags)
        
        self.item_by_uiid[unique_item_id] = item
        
        self.uiid_by_item[item] = unique_item_id
        
        for tag in tags:
            # self.item_tags_by_tag
            if tag not in self.item_tags_by_tag:
                self.item_tags_by_tag[tag] = set()
            
            self.item_tags_by_tag[tag].add(tags)
        
            # self.neighbor_tags_of_a_tag
            if tag not in self.neighbor_tags_of_a_tag:
                self.neighbor_tags_of_a_tag[tag] = set()
            
            self.neighbor_tags_of_a_tag[tag].update(tags - tag)
            
            # self.set_of_tags
            self.set_of_tags.add(tag)
        
        # self.direct_items_by_tags
        if tags not in self.direct_items_by_tags:
            self.direct_items_by_tags[tags] = set()
        
        self.direct_items_by_tags[tags].add(item_id)
        
        # self.tags_by_number_of_tags
        if tags_len not in self.tags_by_number_of_tags:
            self.tags_by_number_of_tags[tags_len] = set()
        
        self.tags_by_number_of_tags[tags_len].add(tags)
        
        # self.tags_len_by_tag
        for tag in tags:
            self.tags_len_by_tag[tag] = tags_len

    def get(self, item_id: ItemID, tags: FrozenSet[TagID]) -> Optional[UniqueItemID]:
        return self.uiid_by_item.get((item_id, tags), None)

    def item(self, unique_item_id: UniqueItemID) -> Optional[Tuple[ItemID, FrozenSet[TagID]]]:
        return self.item_by_uiid.get(unique_item_id, None)

    def delete(self, unique_item_id: UniqueItemID):
        pass

    def list_direct_items(self, tags: FrozenSet[TagID]):
        pass

    def list_all_items(self, tags: FrozenSet[TagID]):
        pass

    def list_direct_tags(self, tags: FrozenSet[TagID]):
        pass

    def list_all_tags(self, tags: FrozenSet[TagID]):
        pass

    def get_nearest_non_empty_tags_set(self, tags: FrozenSet[TagID]) -> Optional[FrozenSet[TagID]]:
        return self._gen_nearest_non_empty_tags_by_some_tags(True, self._normalise_tags(self._check_tags(tags)))

    def _gen_nearest_non_empty_tags_by_some_tags(
            self, is_search_request: bool, tags: FrozenSet[TagID]) -> Optional[Set[FrozenSet[TagID]]]:
        if tags in self.tags_by_itself:
            return set(self.tags_by_itself[tags])

        if tags in self.nearest_non_empty_tags_by_some_tags:
            return self.nearest_non_empty_tags_by_some_tags[tags]

        nearest_non_empty_tags_set = set()

        if tags in self.tags_inclusion_by_tags:
            inclusion_tags = self.tags_inclusion_by_tags[tags]
            min_tags_len = len(min(inclusion_tags))
            for tags2 in inclusion_tags:
                if len(tags2) == min_tags_len:
                    nearest_non_empty_tags_set.add(tags2)
        else:
            minimal_nearest_non_empty_tags_size = len(tags) + 1
            tags_by_number_of_tags: Dict[int, Set[FrozenSet[TagID]]] = dict()
            for tag in tags:
                lookup1: Dict[TagID, Dict[int, Set[FrozenSet[TagID]]]] = \
                    self.near_tags_by_number_of_tags_by_tag_by_tag[tag]
                for tag2 in tags:
                    if tag == tag2:
                        continue
                    if tag2 not in lookup1:
                        return None
                    lookup2: Dict[int, Set[FrozenSet[TagID]]] = lookup1[tag2]
                    sorted_tags_sizes = sorted(lookup2.keys())
                    for tags_size in sorted_tags_sizes:
                        if tags_size < minimal_nearest_non_empty_tags_size:
                            continue
                        lookup3 = lookup2[tags_size]
                        for another_tags in lookup3:
                            if tags != (tags & another_tags):
                                continue
                            if tags_size not in tags_by_number_of_tags:
                                tags_by_number_of_tags[tags_size] = set()
                            tags_by_number_of_tags[tags_size].add(another_tags)
            min_tags_len = min(tags_by_number_of_tags.keys())
            nearest_non_empty_tags_set = tags_by_number_of_tags[min_tags_len]

            if self._is_growth_allowed(is_search_request):
                self.tags_inclusion_by_tags[tags] = set()
                for inclusion_tags_set in tags_by_number_of_tags.values():
                    self.tags_inclusion_by_tags[tags].update(inclusion_tags_set)

        if self._is_growth_allowed(is_search_request):
            self.nearest_non_empty_tags_by_some_tags[tags] = nearest_non_empty_tags_set

        return nearest_non_empty_tags_set

    def _normalise_tags(self, tags: FrozenSet[TagID]) -> FrozenSet[TagID]:
        if tags in self.tags_by_itself:
            return self.tags_by_itself[tags]
        else:
            return tags

    def _check_tags(self, tags: FrozenSet[TagID]) -> FrozenSet[TagID]:
        if not (tags == (tags & self.set_of_tags)):
            raise TagNotFound(tags - (tags & self.set_of_tags))
        return tags

    def _is_growth_allowed(self, is_search_request: bool):
        return (not is_search_request) or (is_search_request and self.growth_during_the_search_is_allowed())
