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


# import TagDB
# from TagDB import USUAL_TREE_TYPE as USUAL_TREE_TYPE
# from TagDB import SMART_TREE_TYPE as SMART_TREE_TYPE
# from TagDB import FULL_TREE_TYPE as FULL_TREE_TYPE
# from TagDB import PLAIN_PSEUDO_TREE_TYPE as PLAIN_PSEUDO_TREE_TYPE
from .TagDB import *
import copy
from cengal.web_tools.request_cache import RequestCache
import time


class tag_db_interface:

    def __init__(self):
        super().__init__()
        self.__db = TagDB()
        self.cache = RequestCache(300000)

    def get_db(self):
        return self.__db

    def add_item(self, binItem, binTags):
        binItem = copy.deepcopy(binItem)
        binTags = copy.deepcopy(binTags)

        result = self.__db.add_item(binItem, binTags)

        result = copy.deepcopy(result)
        self.cache.clear()
        return result

    def remove_item(self, binTags, binItem):
        binTags = copy.deepcopy(binTags)
        binItem = copy.deepcopy(binItem)

        result = self.__db.remove_item(binItem, binTags)

        result = copy.deepcopy(result)
        self.cache.clear()
        return result

    def get_items(self, binTags, treeType=USUAL_TREE_TYPE):
        binTags = copy.deepcopy(binTags)
        treeType = copy.deepcopy(treeType)

        # request = ('get_items', tuple(self.__db.sort_tag_list_by_hash(binTags)), treeType)
        request = ('get_items', frozenset(binTags), treeType)
        result = self.cache.try_to_get_data_for_request(request)
        if result is None:
            result = self.__db.get_items_from_tags(binTags, treeType=treeType)
            self.cache.put_new_request(request, result)

        result = copy.deepcopy(result)
        return result

    def get_tags(self, binTags, treeType=USUAL_TREE_TYPE):
        binTags = copy.deepcopy(binTags)
        treeType = copy.deepcopy(treeType)

        # request = ('get_tags', tuple(self.__db.sort_tag_list_by_hash(binTags)), treeType)
        request = ('get_tags', frozenset(binTags), treeType)
        result = self.cache.try_to_get_data_for_request(request)
        if result is None:
            result = self.__db.get_tags_from_tags(binTags, treeType=treeType)
            self.cache.put_new_request(request, result)

        result = copy.deepcopy(result)
        return result

    def get_all(self, binTags, treeType=USUAL_TREE_TYPE):
        binTags = copy.deepcopy(binTags)
        treeType = copy.deepcopy(treeType)

        # request = ('get_all', tuple(self.__db.sort_tag_list_by_hash(binTags)), treeType)
        request = ('get_all', frozenset(binTags), treeType)
        result = self.cache.try_to_get_data_for_request(request)
        if result is None:
            result = self.__db.get_all_from_tags(binTags, treeType=treeType)
            self.cache.put_new_request(request, result)

        result = copy.deepcopy(result)
        return result

    def get_tags_for_a_smart_redirection(self, binTags):
        binTags = copy.deepcopy(binTags)

        # request = ('is_smart_redirection_for_a_tag_path_reduction_needed'
        #            , tuple(self.__db.sort_tag_list_by_hash(binTags)))
        request = ('is_smart_redirection_for_a_tag_path_reduction_needed', frozenset(binTags))
        result = self.cache.try_to_get_data_for_request(request)
        if result is None:
            result = self.__db.get_tags_for_a_smart_redirection(binTags)
            self.cache.put_new_request(request, result)

        result = copy.deepcopy(result)
        return result

    def fill_cache(self, max_answer_time_in_miliseconds=500, path=list()):
        current_path = list(path)
        startTime = time.time()

        tags_and_items_inside_curent_path = self.get_all(current_path, SMART_TREE_TYPE)
        internal_tags = tags_and_items_inside_curent_path[0]
        self.get_items(current_path, PLAIN_PSEUDO_TREE_TYPE)

        endTime = time.time()
        resultTime = endTime - startTime
        if (resultTime*1000) >= max_answer_time_in_miliseconds:
            for additional_tag in internal_tags:
                new_path = current_path + [additional_tag]
                self.fill_cache(max_answer_time_in_miliseconds, new_path)
