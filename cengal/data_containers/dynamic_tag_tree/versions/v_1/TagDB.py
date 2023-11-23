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


__author__ = 'Mikhail Butenko <gtalk@mikhail-butenko.in.ua>'

from cengal.data_generation.id_generator import IDGenerator
from contextlib import contextmanager
from typing import Hashable, Tuple, Dict, Any
from cengal.data_containers.compound_dict_management.standard_library.key__hashable__to__value__set import AddToCompoundDict__Set
from cengal.data_containers.compound_dict_management.standard_library.key_counter import KeyCounter
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly, CoroPriority
from cengal.parallel_execution.coroutines.coro_scheduler import EntityStatsMixin


SMART_TREE_TYPE = 0  # smart tree. Умное дерево тегов: сеть отображенная на древо. Возвращает только список
    # непосредственных подтегов текущего пути, но не их подтеги; возвращает элементы текущего пути, но не элементы
    # из подпутей
SMART_TREE_TYPE_WITH_INTERNAL_MENU = 1   # smart tree with internal menu. В древо встроено меню, позволяющее прямо из
    # древа производить смену типа вывода: SMART_TREE_TYPE, FULL_TREE_TYPE и PLAIN_PSEUDO_TREE_TYPE. На каждый тип
    # вывода будет доступен подтег/подпапка, внутри когорого уже будет нормальное древо элементов, но уже выбранного
    # типа
FULL_TREE_TYPE = 2  # full tree with all tags - with repeats and without filtering. Список айтемов - как у
    # SMART_TREE_TYPE, но при этом список тегов - как у PLAIN_PSEUDO_TREE_TYPE
PLAIN_PSEUDO_TREE_TYPE = 3   # plain tags and items set (will show all tags, subtags and items of
    # current hm... dir - current tag set). Показывает все теги и подтеги единым списком - как у примитивных теговых
    # файловых систем; показывает все элементы текущего пути + все элементы всех под-путей

USUAL_TREE_TYPE = PLAIN_PSEUDO_TREE_TYPE

_ROOT_TAG = r'k{1+vdcY#m8t-4m9`)G2\b]/O\'Rzqyr@FEO~%./nGPzl)[^q 0RS!.bCPh ?fag{8~{SGj;Ss3U85Q-:'


class ToManyIdenticalItemsOnTheGivenTagPathError(Exception):
    pass


class UnknownTreeTypeError(Exception):
    pass


class LockableMixin:
    @property
    def lock(self) -> bool:
        raise NotImplementedError
    
    @lock.setter
    def lock(self, value: bool) -> bool:
        raise NotImplementedError


@contextmanager
def obj_locker(obj: LockableMixin):
    obj.lock = True
    try:
        yield obj.lock
    finally:
        obj.lock = False


class Example(LockableMixin):
    def __init__(self) -> None:
        super().__init__()
        self.lock: bool = False
    
    def write_coroutine(self):
        with obj_locker(self):
            pass
    
    def read_coroutine(self):
        if not self.lock:
            pass


class TagDB(EntityStatsMixin):
    def __init__(self, default_priority: CoroPriority = CoroPriority.normal):
        self.default_priority: CoroPriority = default_priority

        self.itemsID = IDGenerator()

        self.itemIDsForItem = {}  # key - item hash; data - set of itemIDs

        self.itemsSet = {}  # key - ItemID; data - binItem
        # TODO: заменить список тегов на хеш единожды сохраненного списка тегов
        self.itemWithTags = {}  # key - ItemID; data - sorted common TagsTuple's hash

        # TODO: убрать tagsNumPerItemID из кода. Заменить этот список itemID - на список hashOfTheTagHashTuple
        self.tagsNumPerItemID = {}  # key - number of tags in this ItemID group; data - set of itemIDs which are have
            # needed number of tags

        self.tagsSet = {}  # key - tag hash; data - binTag
        self.tagWithItems = {}  # key - Tag hash; data - set of itemIDs
        self.tagsQnt = {}    # key - Tag hash; data - quantity of the items with this tag


        self.commonTagSets = {}  # key - sorted common TagsTuple's hash; data - sorted TagsTuple
        self.itemsOnTheCommonTagSets = {}   # key - sorted common TagsTuple's hash; data - set of itemIDs
        self.tagsQntPerCommonTagSet = {}    # key - number of tags; data - set of TagsTuple hashes
        self.setOfTagGroupQnt = set()   # {tagQntInGroup1, tagQntInGroup2, ..., tagQntInGroupN} where
            # each Group is an key of the self.tagsQntPerCommonTagSet

        # TODO: добавить словарь tagHashTuplesIDs вида [tagHashTuple.__hash__():tagHashTuple]
        # где tagHashSet - это {tagHash_1, tagHash_2, ..., tagHash_3}
        # TODO: добавить словарь itemsOnThePath вида [tagHashTuple.__hash__():{itemID_1, itemID_2, ..., itemID_3}]

        # TODO: добавить словарь вида [tagQnt:{itemID_1, itemID_2, ..., itemID_3}] и вычитывать это из него
        # и/или
        # TODO: добавить словарь вида [tagQnt:{hashOfTheTagHashTuple_1, hashOfTheTagHashTuple_2, ...
        # , hashOfTheTagHashTuple_N}] и вычитывать это из него, а потом уже и из каждого tagHashSet
        # где hashOfTheTagHashTuple - это tagHashTuple.__hash__()

    def get_entity_stats(self, stats_level: 'EntityStatsMixin.StatsLevel' = EntityStatsMixin.StatsLevel.debug) -> Tuple[str, Dict[str, Any]]:
        return type(self).__name__, {
            'items num': len(self.itemsSet),
            'tags num': len(self.tagsSet),
        }

    def get_root_tag(self):
        return str(_ROOT_TAG)

    def add_tag(self, binTag):
        tagHash = binTag.__hash__()
        self.tagsSet[tagHash] = binTag
        if tagHash not in self.tagsSet:
            self.tagsQnt[tagHash] = 0
        if tagHash not in self.tagWithItems:
            self.tagWithItems[tagHash] = set()

    def remove_tag(self, binTag):
        # will try to delete given tag. If there is at least one item with this tag, than function will fail
        # and will return False; otherwise it will delete given tag and will return True.
        functionResult = False
        tagHash = binTag.__hash__()
        if tagHash in self.tagsSet:
            if tagHash in self.tagsQnt:
                if self.tagsQnt[tagHash] == 0:
                    del self.tagsSet[tagHash]
                    del self.tagsQnt[tagHash]
                    functionResult = True
                else:
                    functionResult = False
            else:
                del self.tagsSet[tagHash]
                functionResult = True

        if functionResult:
            if tagHash in self.tagWithItems:
                del self.tagWithItems[tagHash]

        return functionResult

    def add_item(self, binItem, binTags):
        # will add new item and return it's dynamic ID or None object If this Item already exist on the given tag path
        # Or will raise an exception if we already have more than one binItem (another item that is identical to
        # the given binItem)  on this tag path
        binTags = set(binTags)

        if self.get_root_tag() not in binTags:
            binTags.add(self.get_root_tag())

        # may raise an exception in this place. Nope - from now it will be not
        if self.get_itemID_from_item_and_tags(binTags, binItem) is not None:
            return None

        itemID = self.itemsID.get_new_ID()
        self.itemsSet[itemID] = binItem

        itemHash = binItem.__hash__()
        if itemHash in self.itemIDsForItem:
            IDsSet = self.itemIDsForItem[itemHash]
            IDsSet.add(itemID)
            # self.itemIDsForItem[itemHash] = IDsSet
        else:
            self.itemIDsForItem[itemHash] = {itemID}

        tagQnt = len(binTags)
        if tagQnt in self.tagsNumPerItemID:
            itemIDsSet = self.tagsNumPerItemID[tagQnt]
            itemIDsSet.add(itemID)
            # self.tagsNumPerItemID[tagQnt] = itemIDsSet
        else:
            self.tagsNumPerItemID[tagQnt] = {itemID}

        binTagHashes = set()

        for tag in binTags:
            self.add_tag(tag)
            tagHash = tag.__hash__()
            binTagHashes.add(tagHash)
            setOfItems = self.tagWithItems[tagHash]
            if itemID not in setOfItems:
                setOfItems.add(itemID)
                if tagHash in self.tagsQnt:
                    self.tagsQnt[tagHash] += 1
                else:
                    self.tagsQnt[tagHash] = 1
            self.tagWithItems[tagHash] = setOfItems

        sortedTagTuple = tuple(self.sort_tag_hash_list_by_hash(binTagHashes))
        hashOfTheSortedTagTuple = sortedTagTuple.__hash__()
        self.itemWithTags[itemID] = hashOfTheSortedTagTuple

        self.commonTagSets[hashOfTheSortedTagTuple] = sortedTagTuple

        if hashOfTheSortedTagTuple in self.itemsOnTheCommonTagSets:
            itemIDsSet = self.itemsOnTheCommonTagSets[hashOfTheSortedTagTuple]
            itemIDsSet.add(itemID)
            # self.itemsOnTheCommonTagSets[tagQnt] = itemIDsSet
        else:
            self.itemsOnTheCommonTagSets[hashOfTheSortedTagTuple] = {itemID}

        lenOfTheSortedTagTuple = len(sortedTagTuple)
        if lenOfTheSortedTagTuple in self.tagsQntPerCommonTagSet:
            itemIDsSet = self.tagsQntPerCommonTagSet[lenOfTheSortedTagTuple]
            itemIDsSet.add(hashOfTheSortedTagTuple)
            # self.tagsQntPerCommonTagSet[lenOfTheSortedTagTuple] = itemIDsSet
        else:
            self.tagsQntPerCommonTagSet[lenOfTheSortedTagTuple] = {hashOfTheSortedTagTuple}
            self.setOfTagGroupQnt.add(lenOfTheSortedTagTuple)

        return itemID

    def remove_item_by_itemID(self, itemID):
        ly = gly(self.default_priority)

        if itemID in self.itemsSet:
            itemHash = self.itemsSet[itemID].__hash__()
            del self.itemsSet[itemID]

            if itemHash in self.itemIDsForItem:
                IDsSet = self.itemIDsForItem[itemHash]
                IDsSet.difference_update({itemID})
                # self.itemIDsForItem[itemHash] = IDsSet
                if len(IDsSet) < 1:
                    del self.itemIDsForItem[itemHash]

        if itemID in self.itemWithTags:
            commonTagTupleHash = self.itemWithTags[itemID]
            tagTuple = self.commonTagSets[commonTagTupleHash]
            numberOfTags = len(tagTuple)

            if commonTagTupleHash in self.itemsOnTheCommonTagSets:
                IDsSet = self.itemsOnTheCommonTagSets[commonTagTupleHash]
                IDsSet.difference_update({itemID})
                # self.itemsOnTheCommonTagSets[commonTagTupleHash] = IDsSet
                if len(IDsSet) < 1:
                    del self.itemsOnTheCommonTagSets[commonTagTupleHash]
                    del self.commonTagSets[commonTagTupleHash]
                    if numberOfTags in self.tagsQntPerCommonTagSet:
                        setOfTagTuplesHashes = self.tagsQntPerCommonTagSet[numberOfTags]
                        setOfTagTuplesHashes.difference_update({numberOfTags})
                        # self.tagsQntPerCommonTagSet[numberOfTags] = setOfTagTuplesHashes
                        if len(setOfTagTuplesHashes) < 1:
                            del self.tagsQntPerCommonTagSet[numberOfTags]
                            self.setOfTagGroupQnt.difference_update({numberOfTags})

            del self.itemWithTags[itemID]

            setOfTagHashes = set(tagTuple)

            tagsQnt = len(setOfTagHashes)
            if tagsQnt in self.tagsNumPerItemID:
                IDsSet = self.tagsNumPerItemID[tagsQnt]
                IDsSet.difference_update({itemID})
                # self.tagsNumPerItemID[tagsQnt] = IDsSet
                if len(IDsSet) < 1:
                    del self.tagsNumPerItemID[tagsQnt]

            for tagHash in setOfTagHashes:
                ly()
                if tagHash in self.tagsQnt:
                    tagsQuantity = self.tagsQnt[tagHash]
                    tagsQuantity -= 1
                    if tagsQuantity < 1:
                        tagsQuantity = 0
                    self.tagsQnt[tagHash] = tagsQuantity
                    if tagsQuantity < 1:
                        del self.tagsQnt[tagHash]
                        del self.tagsSet[tagHash]
                if tagHash in self.tagWithItems:
                    IDsSet = self.tagWithItems[tagHash]
                    IDsSet.difference_update({itemID})
                    if len(IDsSet) < 1:
                        del self.tagWithItems[tagHash]
                    # self.tagWithItems[tagHash] = IDsSet

        self.itemsID.remove_ID(itemID)

    def remove_item(self, binTags, binItem):
        # will return ItemId for deleted item or None object if Item is not exist
        # Or will raise an exception if we already have more than one binItem (another item that is identical to
        # the given binItem) on this tag path
        binTags = set(binTags)
        if self.get_root_tag() not in binTags:
            binTags.add(self.get_root_tag())
        itemID = self.get_itemID_from_item_and_tags(binTags, binItem)
        if itemID is not None:
            self.remove_item_by_itemID(itemID)
        return itemID

    def __OLD__get_itemID_from_item_and_tags(self, binTags, binItem):
        if self.get_root_tag() not in binTags:
            binTags.append(self.get_root_tag())
        potentialIDs = set(self.get_potential_itemIDs_from_item(binItem))
        itemIDsSet = set(self.get_itemIDs_from_tags(binTags, SMART_TREE_TYPE))
        resultItemIDsList = potentialIDs & itemIDsSet
        if len(resultItemIDsList) == 0:
            return None
        elif len(resultItemIDsList) == 1:
            resultItemID = resultItemIDsList.pop()  # we have assume that we'll have only one item in intersection
                # between potential IDs and Items that have (and have only) given tag list (without another tags in the
                # path to this items). We need to check it in the adding new item to the given tag path.
            return resultItemID
        elif len(resultItemIDsList) > 1:
            raise ToManyIdenticalItemsOnTheGivenTagPathError()

    def get_itemID_from_item_and_tags(self, binTags, binItem):
        ly = gly(self.default_priority)

        binTags = set(binTags)

        if self.get_root_tag() not in binTags:
            binTags.add(self.get_root_tag())

        potentialIDs = self.get_potential_itemIDs_from_item(binItem)
        setOfBinTagsHashes = set()
        for tag in binTags:
            ly()
            setOfBinTagsHashes.add(tag.__hash__())
        for itemID in potentialIDs:
            ly()
            currentItemTagsSet = self.get_tagsHashes_from_single_item(itemID, isWithoutRootHash=False)
            if setOfBinTagsHashes == currentItemTagsSet:
                return itemID
        return None

    def tag_hash_list_2_tag_list(self, tagHashList):
        ly = gly(self.default_priority)

        tagList = list()
        for tagHash in tagHashList:
            ly()
            tagList.append(self.tagsSet[tagHash])
        return tagList

    def get_item_and_tags_from_itemID(self, itemID):
        commonTagTupleHash = self.itemWithTags[itemID]
        tagSet = set(self.commonTagSets[commonTagTupleHash]) - {self.get_root_tag().__hash__()}
        sortedTagHashList = self.sort_tag_hash_list_by_qnt(tagSet)
        result = (self.itemsSet[itemID], self.tag_hash_list_2_tag_list(sortedTagHashList))
        return result

    # @profile
    def get_top_tag_hash_list_by_qnt(self, tagHashSet, local_tags_qnt=None):
        ly = gly(self.default_priority)

        tagsQnt = self.tagsQnt
        if local_tags_qnt is not None:
            tagsQnt = local_tags_qnt
        tag_hash_set = set(tagHashSet)
        tag_by_qnt = dict()
        tag_by_qnt__filler = AddToCompoundDict__Set(tag_by_qnt)
        biggest_qnt = 0
        for tag_hash in tag_hash_set:
            ly()
            qnt = tagsQnt[tag_hash]
            if qnt > biggest_qnt:
                biggest_qnt = qnt
            # if qnt not in tag_by_qnt:
            #     tag_by_qnt[qnt] = set()
            # tag_by_qnt[qnt].add(tag_hash)
            tag_by_qnt__filler.add(qnt, tag_hash)

        result = None
        if len(tag_by_qnt) > 0:
            # biggest_qnt = max(tag_by_qnt)
            result = tuple(tag_by_qnt[biggest_qnt])
        else:
            result = tuple()
        return result

    def sort_tag_hash_list_by_qnt(self, tagHashSet):
        # will return sorted tag list - not sorted tag hash list
        ly = gly(self.default_priority)

        tagHashSet = set(tagHashSet)
        rawTagList = list()
        for tagHash in tagHashSet:
            ly()
            tagWithWeight = (tagHash, self.tagsQnt[tagHash])
            rawTagList.append(tagWithWeight)
        return self.sort_raw_tag_list(rawTagList)

    def sort_tag_list_by_qnt(self, binTags):
        ly = gly(self.default_priority)

        binTags = set(binTags)
        rawTagList = list()
        for tag in binTags:
            ly()
            tagHash = tag.__hash__()
            tagWithWeight = (tag, self.tagsQnt[tagHash])
            rawTagList.append(tagWithWeight)
        return self.sort_raw_tag_list(rawTagList)

    def sort_tag_hash_list_by_hash(self, tagHashSet):
        # will return sorted tag list - not sorted tag hash list
        ly = gly(self.default_priority)

        tagHashSet = set(tagHashSet)
        rawTagList = list()
        for tagHash in tagHashSet:
            ly()
            tagWithWeight = (tagHash, tagHash)
            rawTagList.append(tagWithWeight)
        return self.sort_raw_tag_list(rawTagList)

    def sort_tag_list_by_hash(self, binTags):
        ly = gly(self.default_priority)

        binTags = set(binTags)
        rawTagList = list()
        for tag in binTags:
            ly()
            tagHash = tag.__hash__()
            tagWithWeight = (tag, tagHash)
            rawTagList.append(tagWithWeight)
        return self.sort_raw_tag_list(rawTagList)

    def sort_raw_tag_list(self, rawTagList):
        # will return sorted tag list
        ly = gly(self.default_priority)

        rawTagList = sorted(rawTagList, key=lambda tagAndWeight: tagAndWeight[1], reverse=True)
        tagList = list()
        for rawTag in rawTagList:
            ly()
            tagList.append(rawTag[0])
        return tagList

    def get_itemIDs_from_tags(self, binTags, treeType=USUAL_TREE_TYPE,
                              isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags=False):
        # TODO: исправить ошибку: SMART_TREE_TYPE: возвращает не только список файлов в текущей директории, но и из
        # непосредственных подпапок данной папки

        # treeType - type of the graph tree representation: show all tags with replies (pure representation);
        # show only relevant tags; etc.
        # return set of itemIDs
        ly = gly(self.default_priority)

        binTags = set(binTags)

        if self.get_root_tag() not in binTags:
            binTags.add(self.get_root_tag())

        tagHashSet = set()
        for binTag in binTags:
            ly()
            tagHashSet.add(binTag.__hash__())

        # PLAIN_PSEUDO_TREE_TYPE
        interceptionOfItemsWithTags = set()
        if (treeType == PLAIN_PSEUDO_TREE_TYPE) or isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags:
            binTagsQnt = len(tagHashSet)
            commonTagGroupHashSet = set()
            tagSet = set()
            itemIDSet = set()
            binTagHashTuple = tuple(self.sort_tag_hash_list_by_hash(tagHashSet))
            hashOfTheBinTagHashTuple = binTagHashTuple.__hash__()
            if hashOfTheBinTagHashTuple in self.itemsOnTheCommonTagSets:
                itemIDSet = self.itemsOnTheCommonTagSets[hashOfTheBinTagHashTuple]
            for commonTagQnt in self.setOfTagGroupQnt:
                ly()
                if commonTagQnt > binTagsQnt:
                    setOfTheCommonTagGroupHashes = self.tagsQntPerCommonTagSet[commonTagQnt]
                    commonTagGroupHashSet.update(setOfTheCommonTagGroupHashes)
            for commonTagGroupHash in commonTagGroupHashSet:
                ly()
                commonTagHashTuple = self.commonTagSets[commonTagGroupHash]
                commonTagHashSet = set(commonTagHashTuple)
                if tagHashSet.issubset(commonTagHashSet):
                    itemIDSet.update(self.itemsOnTheCommonTagSets[commonTagGroupHash])
                # # if len(tagHashSet & commonTagHashSet) == len(tagHashSet):
                # res_set = tagHashSet.intersection(commonTagHashSet)
                # if len(res_set) == binTagsQnt:
                #     itemIDSet = itemIDSet | self.itemsOnTheCommonTagSets[commonTagGroupHash]
            interceptionOfItemsWithTags = itemIDSet

            # isFirstHash = True
            # for tag in binTags:
            #     tagHash = tag.__hash__()
            #     if tagHash in self.tagWithItems:
            #         if isFirstHash:
            #             interceptionOfItemsWithTags = self.tagWithItems[tagHash]
            #             isFirstHash = False
            #         else:
            #             itemsWithTag = self.tagWithItems[tagHash]
            #             interceptionOfItemsWithTags = interceptionOfItemsWithTags & itemsWithTag
            #     else:
            #         # TODO: произвести такую же провеку в get_items_from_tags() и build_smart_tree()
            #         if isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags:
            #             result = (set(), set())
            #             return result
            #         else:
            #             return set()

        resultItemIDSet = interceptionOfItemsWithTags
        setOfAllInternalItemIDsForThisSetOfTags = interceptionOfItemsWithTags

        # SMART_TREE_TYPE or FULL_TREE_TYPE
        if (treeType == SMART_TREE_TYPE) or (treeType == FULL_TREE_TYPE):
            resultItemIDSet = set()
            binTagHashTuple = self.sort_tag_hash_list_by_hash(tagHashSet)
            binTagHashTuple = tuple(binTagHashTuple)
            hashOfTheBinTagHashTuple = binTagHashTuple.__hash__()
            if hashOfTheBinTagHashTuple in self.itemsOnTheCommonTagSets:
                resultItemIDSet = self.itemsOnTheCommonTagSets[hashOfTheBinTagHashTuple]

            # filteredItemIDsSet = set()
            # tagQnt = len(binTags)
            # # for itemID in setOfAllInternalItemIDsForThisSetOfTags:
            # #     if len(self.itemWithTags[itemID]) == tagQnt:
            # #         # _TODO: добавить словарь вида [tagQnt:{itemID_1, itemID_2, ..., itemID_3}]
            # #         # и вычитывать это из него
            # #         # и/или
            # #         # _TODO: добавить словарь вида [tagQnt:{hashOfTheTagHashSet_1, hashOfTheTagHashSet_2, ...
            # #         # , hashOfTheTagHashSet_3}] и вычитывать это из него, а потом уже и из каждого tagHashSet
            # #         # где hashOfTheTagHashSet - это tagHashSet.__hash__()
            # #         filteredItemIDsSet.add(itemID)
            # if tagQnt in self.tagsNumPerItemID:
            #     filteredItemIDsSet = setOfAllInternalItemIDsForThisSetOfTags & self.tagsNumPerItemID[tagQnt]
            #
            # resultItemIDSet = set()
            # tagHashSet = set()
            # for binTag in binTags:
            #     tagHashSet.add(binTag.__hash__())
            # for itemID in filteredItemIDsSet:
            #     commonTagTupleHash = self.itemWithTags[itemID]
            #     tagSet = set(self.commonTagSets[commonTagTupleHash])
            #     if tagSet == tagHashSet:
            #         # _TODO: добавить словарь tagHashTuplesIDs вида [tagHashTuple.__hash__():tagHashTuple]
            #         # где tagHashSet - это {tagHash_1, tagHash_2, ..., tagHash_3}
            #         # _TODO: добавить словарь itemsOnThePath вида [tagHashTuple.__hash__():{itemID_1, itemID_2, ...
            #         # , itemID_3}]
            #         resultItemIDSet.add(itemID)
        elif treeType == PLAIN_PSEUDO_TREE_TYPE:
            # already implemented (see bellow). Don't touch this code!
            pass
        else:
            raise UnknownTreeTypeError()

        if isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags:
            result = (set(resultItemIDSet), set(setOfAllInternalItemIDsForThisSetOfTags))
            return result
        else:
            return set(resultItemIDSet)

    def get_items_from_tags(self, binTags, treeType=USUAL_TREE_TYPE,
                            isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags=False):
        # treeType - type of the graph tree representation: show all tags with replies (pure representation);
        # show only relevant tags; etc.
        # return set of itemIDs
        ly = gly(self.default_priority)

        binTags = set(binTags)
        itemIDsSet = self.get_itemIDs_from_tags(binTags, treeType=treeType,
                                                isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags=
                                                isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags)
        if isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags:
            itemSet = set()
            for itemID in itemIDsSet[0]:
                ly()
                itemSet.add(self.itemsSet[itemID])
            result = (tuple(itemSet), tuple(itemIDsSet[1]))  # result == (usual items set, additional set of all
                # internal itemIDs)
            return result
        else:
            itemSet = set()
            for itemID in itemIDsSet:
                ly()
                itemSet.add(self.itemsSet[itemID])
            return tuple(itemSet)

    def get_tagHashes_from_tags(self, binTags, treeType=USUAL_TREE_TYPE,
                                prePreparedSetOfAllInternalItemIDsForThisSetOfTags=None):
        # where "itemIDsSet" is externally given "get_itemIDs_from_tags(binTags, treeType=PLAIN_PSEUDO_TREE_TYPE)"
        # so "itemIDsSet" is a set of the all items inside the "folder" binTags (including items from "subfolders")
        # treeType - the same as in the "get_items_from_tags()" method
        # return set of itemIDs
        # prePreparedSetOfAllInternalItemIDsForThisSetOfTags can be generated by:
        #   a) get_itemIDs_from_tags(..., treeType=PLAIN_PSEUDO_TREE_TYPE)
        #   a) get_itemIDs_from_tags(..., isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags = True)
        #   c) get_items_from_tags(..., isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags = True)
        #   d) get_items_from_tags(..., treeType=PLAIN_PSEUDO_TREE_TYPE) || BUT: it'll return item set - not itemID
        #       set
        ly = gly(self.default_priority)

        binTags = set(binTags)

        resultTagHashSet = set()

        setOfAllInternalItemIDs = set()
        if prePreparedSetOfAllInternalItemIDsForThisSetOfTags is None:
            setOfAllInternalItemIDs = self.get_itemIDs_from_tags(binTags, treeType=PLAIN_PSEUDO_TREE_TYPE)
        else:
            setOfAllInternalItemIDs = prePreparedSetOfAllInternalItemIDsForThisSetOfTags

        if (treeType == PLAIN_PSEUDO_TREE_TYPE) or (treeType == FULL_TREE_TYPE):
            binTagHashes = set()
            for tag in binTags:
                ly()
                binTagHashes.add(tag.__hash__())
            tagHashSet = set()
            for itemID in setOfAllInternalItemIDs:
                ly()
                if itemID in self.itemWithTags:
                    commonTagTupleHash = self.itemWithTags[itemID]
                    tagSet = set(self.commonTagSets[commonTagTupleHash])
                    tagHashSet.update(tagSet)
            resultTagHashSet = tagHashSet - binTagHashes
        elif treeType == SMART_TREE_TYPE:
            # smartTree = self.build_smart_tree(binTags, prePreparedSetOfAllInternalItemIDs=setOfAllInternalItemIDs)
            smartTree = self.build_smart_tree(binTags, prePreparedSetOfAllInternalItemIDs=setOfAllInternalItemIDs,
                                              zeroSliceOnly=True)
            if 0 in smartTree:
                resultTagHashSet = smartTree[0]
            # filteredItemIDsList = list()
            # tagQnt = len(binTags)
            # for itemID in listOfAllInternalItemIDs:
            #     if len(self.itemWithTags[itemID]) == (tagQnt + 1):
            #         filteredItemIDsList.append(itemID)
            #
            # tagHashSet = set()
            # for itemID in filteredItemIDsList:
            #     tagHashSet.update(set(self.itemWithTags[itemID]))
            # givenTagHashes = set()
            # for tag in binTags:
            #     givenTagHashes.add(tag.__hash__())
            # tagHashSet.difference_update(givenTagHashes)
            # ##resultTagHashList = list(tagHashSet)
            # # если остановиться тут - то мы увидим не все папки: мы не увидим папки непосредственно в которых есть
            # # только другие подпапки, но ни одного файла.
            # #
            # # значит далее мы должны исключить все файлы, которые имеют только что найденные теги, и начать строить
            # # древо тегов для оставшихся
            # #
            # # а далее - повторить все это в цикле, увеличив при проверке кол-во тегов еще раз на единицу (и используя
            # # уже оставшийся после отсеивания набор файлов). В итоге кол-во итераций зависит не от количества файлов,
            # # а от максимальной фактически имеющейся вложенности файлов внутри тегов-каталогов
        else:
            raise UnknownTreeTypeError()

        sortedTagHashList = self.sort_tag_hash_list_by_qnt(resultTagHashSet - {self.get_root_tag().__hash__()})
        return list(sortedTagHashList)

    def get_tags_from_tags(self, binTags, treeType=USUAL_TREE_TYPE,
                           prePreparedSetOfAllInternalItemIDsForThisSetOfTags=None):
        result = self.get_tagHashes_from_tags(binTags, treeType=treeType,
                                              prePreparedSetOfAllInternalItemIDsForThisSetOfTags=
                                              prePreparedSetOfAllInternalItemIDsForThisSetOfTags)
        return tuple(self.tag_hash_list_2_tag_list(result))

    def build_smart_tree(self, startingBinTags, prePreparedSetOfAllInternalItemIDs=None, zeroSliceOnly=False):
        ly = gly(self.default_priority)

        startingBinTags = set(startingBinTags)

        if self.get_root_tag() not in startingBinTags:
            startingBinTags.add(self.get_root_tag())

        startingTagHashes = set()
        for tag in startingBinTags:
            ly()
            startingTagHashes.add(tag.__hash__())

        if prePreparedSetOfAllInternalItemIDs is None:
            setOfAllInternalItemIDs = self.get_itemIDs_from_tags(startingBinTags, treeType=PLAIN_PSEUDO_TREE_TYPE)
        else:
            setOfAllInternalItemIDs = prePreparedSetOfAllInternalItemIDs

        smartTree = {0: set()}
        smartTree__filler = AddToCompoundDict__Set(smartTree)
        local_tags_qnt = dict()
        local_tags_qnt__filler = KeyCounter(local_tags_qnt)
        for itemID in setOfAllInternalItemIDs:
            ly()
            commonTagTupleHash = self.itemWithTags[itemID]
            tagSet = set(self.commonTagSets[commonTagTupleHash])
            setOfTags = tagSet
            setOfTags = setOfTags - startingTagHashes
            for tag_hash in setOfTags:
                ly()
                # if tag_hash not in local_tags_qnt:
                #     local_tags_qnt[tag_hash] = 0
                # local_tags_qnt[tag_hash] += 1
                local_tags_qnt__filler.add(tag_hash)

        for itemID in setOfAllInternalItemIDs:
            ly()
            commonTagTupleHash = self.itemWithTags[itemID]
            tagSet = set(self.commonTagSets[commonTagTupleHash])
            setOfTags = tagSet
            setOfTags = setOfTags - startingTagHashes
            listOfTagHashes = None
            if zeroSliceOnly:
                listOfTagHashes = self.get_top_tag_hash_list_by_qnt(setOfTags, local_tags_qnt)
            else:
                listOfTagHashes = self.sort_tag_hash_list_by_qnt(setOfTags)

            lastTagHash = None
            lastTagHashQnt = None
            treeLevel = 0
            for tagHash in listOfTagHashes:
                ly()
                # currentTagHashQnt = self.tagsQnt[tagHash]
                currentTagHashQnt = local_tags_qnt[tagHash]
                if (lastTagHash is None) or (currentTagHashQnt == lastTagHashQnt):
                    pass
                else:
                    treeLevel += 1
                    lastTagHash = None
                    lastTagHashQnt = None
                # if treeLevel not in smartTree:
                #     smartTree[treeLevel] = set()
                # # tagsSetOnTheLevel = smartTree[treeLevel]
                # # tagsSetOnTheLevel.add(tagHash)
                # # smartTree[treeLevel] = tagsSetOnTheLevel
                # smartTree[treeLevel].add(tagHash)
                smartTree__filler.add(treeLevel, tagHash)
                lastTagHash = tagHash
                lastTagHashQnt = currentTagHashQnt
        return dict(smartTree)

    def build_smart_tree_2(self, startingBinTags, prePreparedSetOfAllInternalItemIDs=None, zeroSliceOnly=False):
        ly = gly(self.default_priority)

        startingBinTags = set(startingBinTags)

        if self.get_root_tag() not in startingBinTags:
            startingBinTags.add(self.get_root_tag())

        startingTagHashes = set()
        for tag in startingBinTags:
            ly()
            startingTagHashes.add(tag.__hash__())

        if prePreparedSetOfAllInternalItemIDs is None:
            setOfAllInternalItemIDs = self.get_itemIDs_from_tags(startingBinTags, treeType=PLAIN_PSEUDO_TREE_TYPE)
        else:
            setOfAllInternalItemIDs = prePreparedSetOfAllInternalItemIDs

        smartTree = {0: set()}
        smartTree__filler = AddToCompoundDict__Set(smartTree)
        local_tags_qnt = dict()
        local_tags_qnt__filler = KeyCounter(local_tags_qnt)
        for itemID in setOfAllInternalItemIDs:
            ly()
            commonTagTupleHash = self.itemWithTags[itemID]
            tagSet = set(self.commonTagSets[commonTagTupleHash])
            setOfTags = tagSet
            setOfTags = setOfTags - startingTagHashes
            for tag_hash in setOfTags:
                ly()
                # if tag_hash not in local_tags_qnt:
                #     local_tags_qnt[tag_hash] = 0
                # local_tags_qnt[tag_hash] += 1
                local_tags_qnt__filler.add(tag_hash)

        for itemID in setOfAllInternalItemIDs:
            ly()
            commonTagTupleHash = self.itemWithTags[itemID]
            tagSet = set(self.commonTagSets[commonTagTupleHash])
            setOfTags = tagSet
            setOfTags = setOfTags - startingTagHashes
            listOfTagHashes = None
            if zeroSliceOnly:
                listOfTagHashes = self.get_top_tag_hash_list_by_qnt(setOfTags, local_tags_qnt)
            else:
                listOfTagHashes = self.sort_tag_hash_list_by_qnt(setOfTags)

            lastTagHash = None
            lastTagHashQnt = None
            treeLevel = 0
            for tagHash in listOfTagHashes:
                ly()
                # currentTagHashQnt = self.tagsQnt[tagHash]
                currentTagHashQnt = local_tags_qnt[tagHash]
                if (lastTagHash is None) or (currentTagHashQnt == lastTagHashQnt):
                    pass
                else:
                    treeLevel += 1
                    lastTagHash = None
                    lastTagHashQnt = None
                # if treeLevel not in smartTree:
                #     smartTree[treeLevel] = set()
                # # tagsSetOnTheLevel = smartTree[treeLevel]
                # # tagsSetOnTheLevel.add(tagHash)
                # # smartTree[treeLevel] = tagsSetOnTheLevel
                # smartTree[treeLevel].add(tagHash)
                smartTree__filler.add(treeLevel, tagHash)
                lastTagHash = tagHash
                lastTagHashQnt = currentTagHashQnt
        return dict(smartTree)

    def get_all_from_tags(self, binTags, treeType=USUAL_TREE_TYPE):
        binTags = set(binTags)
        items = self.get_items_from_tags(binTags, treeType=treeType,
                                         isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags=True)
        if len(items[1]) > 0:
            tags = self.get_tags_from_tags(binTags, treeType=treeType,
                                           prePreparedSetOfAllInternalItemIDsForThisSetOfTags=items[1])
            result = (tuple(tags), set(items[0]))
            return result
        else:
            result = (tuple(), set())
            return result

    def get_tagsHashes_from_single_item(self, itemID, isWithoutRootHash=True):
        if itemID in self.itemWithTags:
            commonTagTupleHash = self.itemWithTags[itemID]
            tagSet = set(self.commonTagSets[commonTagTupleHash])
            if isWithoutRootHash:
                return set(tagSet - {self.get_root_tag().__hash__()})
            else:
                return set(tagSet)
        else:
            return set()

    def get_potential_itemIDs_from_item(self, binItem):
        itemHash = binItem.__hash__()
        if itemHash in self.itemIDsForItem:
            return set(self.itemIDsForItem[itemHash])
        else:
            return set()

    def is_smart_redirection_for_a_tag_path_reduction_needed(self, binTags):
        ly = gly(self.default_priority)

        binTags = set(binTags)

        if self.get_root_tag() not in binTags:
            binTags.add(self.get_root_tag())

        tagHashSet = set()
        for binTag in binTags:
            ly()
            tagHashSet.add(binTag.__hash__())

        binTagsQnt = len(tagHashSet)
        commonTagGroupHashSet = set()
        # setOfLenOfTheCommonTagHashSetForChecking = set()
        setOfTheTagsIntersection = None
        for commonTagQnt in self.setOfTagGroupQnt:
            ly()
            if commonTagQnt > binTagsQnt:
                setOfTheCommonTagGroupHashes = self.tagsQntPerCommonTagSet[commonTagQnt]
                commonTagGroupHashSet.update(setOfTheCommonTagGroupHashes)
        for commonTagGroupHash in commonTagGroupHashSet:
            ly()
            commonTagHashTuple = self.commonTagSets[commonTagGroupHash]
            commonTagHashSet = set(commonTagHashTuple)
            if len(tagHashSet & commonTagHashSet) == len(tagHashSet):
                if tagHashSet != commonTagHashSet:
                    if setOfTheTagsIntersection is None:
                        setOfTheTagsIntersection = commonTagHashSet
                    else:
                        setOfTheTagsIntersection = setOfTheTagsIntersection & commonTagHashSet
        #         if tagHashSet != commonTagHashSet:
        #             setOfLenOfTheCommonTagHashSetForChecking.add(len(commonTagHashSet))
        # minimalTagPath = min(setOfLenOfTheCommonTagHashSetForChecking)
        # pathDiff = minimalTagPath - len(tagHashSet)
        # if pathDiff > 0:
        if setOfTheTagsIntersection is None:
            return list()

        setOfTheTagsForAReduction = setOfTheTagsIntersection - tagHashSet

        sortedTagHashList = self.sort_tag_hash_list_by_qnt(setOfTheTagsForAReduction - {self.get_root_tag().__hash__()})
        return list(sortedTagHashList)

    def get_tags_for_a_smart_redirection(self, binTags):
        result = self.is_smart_redirection_for_a_tag_path_reduction_needed(binTags)
        return tuple(self.tag_hash_list_2_tag_list(result))
