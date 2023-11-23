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


__all__ = ['tag_db_interface', 'SMART_TREE_TYPE', 'SMART_TREE_TYPE_WITH_INTERNAL_MENU', 'FULL_TREE_TYPE', 'PLAIN_PSEUDO_TREE_TYPE', 'USUAL_TREE_TYPE', 'ToManyIdenticalItemsOnTheGivenTagPathError', 'UnknownTreeTypeError', ]
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
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly, CoroPriority
from cengal.parallel_execution.coroutines.coro_standard_services.read_write_locker import grwl, RWOperation
from cengal.parallel_execution.coroutines.coro_scheduler import EntityStatsMixin
from cengal.data_manipulation.tree_traversal import *


class tag_db_interface(EntityStatsMixin):
    def __init__(self, max_writers_in_progress: int, max_readers_in_progress: int, lock_entity_id: Hashable = None, default_priority: CoroPriority = CoroPriority.normal):
        self.default_priority: CoroPriority = default_priority
        self.__db = TagDB(default_priority)
        self.cache = RequestCache(300000, default_priority=default_priority)
        self.lock_entity_id: Hashable = lock_entity_id or type(self)
        self.max_writers_in_progress: int = max_writers_in_progress
        self.max_readers_in_progress: int = max_readers_in_progress
        self.last_fill_cache_result_time: float = None
        self.last_fill_cache_tags = None
        self.last_tested_fill_cache_result_time: float = None
        self.last_tested_fill_cache_tags = None
        self.fill_cache_iterations: int = 0
        self.fill_cache_iterations_per_second: float = None
        self.fill_cache_last_time_measurement: float = None
        self.fill_cache_last_time_measurement_iterations: int = 0

    def get_entity_stats(self, stats_level: 'EntityStatsMixin.StatsLevel' = EntityStatsMixin.StatsLevel.debug) -> Tuple[str, Dict[str, Any]]:
        tag_db_name, tag_db_stats = self.__db.get_entity_stats(stats_level)
        return type(self).__name__, {
            'interface': {
                'cache size': len(self.cache._requestsAndData),
                'last fill cache result time': self.last_fill_cache_result_time,
                'last fill cache tags': self.last_fill_cache_tags,
                'last tested fill cache result time': self.last_tested_fill_cache_result_time,
                'last tested fill cache tags': self.last_tested_fill_cache_tags,
                'fill cache iterations': self.fill_cache_iterations,
                'fill cache iterations per second': self.fill_cache_iterations_per_second,
            },
            'db': {
                tag_db_name: tag_db_stats,
            }
        }
    
    def _glock(self):
        return grwl(self.lock_entity_id, self.max_writers_in_progress, self.max_readers_in_progress, False)
    
    def _wlock(self):
        return self._glock()(RWOperation.write)
    
    def _rlock(self):
        return self._glock()(RWOperation.read)

    def get_db(self):
        return self.__db
    
    def new_empty(self) -> 'tag_db_interface':
        return tag_db_interface(
            self.max_writers_in_progress,
            self.max_readers_in_progress,
            self.lock_entity_id,
            self.default_priority
            )

    def add_item(self, binItem, binTags):
        with self._wlock():
            binItem = copy.deepcopy(binItem)
            binTags = copy.deepcopy(binTags)

            result = self.__db.add_item(binItem, binTags)

            result = copy.deepcopy(result)
            self.cache.clear()
            return result

    def remove_item(self, binTags, binItem):
        with self._wlock():
            binTags = copy.deepcopy(binTags)
            binItem = copy.deepcopy(binItem)

            result = self.__db.remove_item(binTags, binItem)

            result = copy.deepcopy(result)
            self.cache.clear()
            return result

    def get_items(self, binTags, treeType=USUAL_TREE_TYPE):
        with self._rlock():
            binTags = copy.deepcopy(binTags)
            treeType = copy.deepcopy(treeType)

            # request = ('get_items', tuple(self.__db.sort_tag_list_by_hash(binTags)), treeType)
            request = ('get_items', frozenset(binTags), treeType)
            result = self.cache.try_to_get_data_for_request(request)
            if result is None:
                
                self.cache.put_new_request(request, result)

            result = copy.deepcopy(result)
            return result

    def get_tags(self, binTags, treeType=USUAL_TREE_TYPE):
        with self._rlock():
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
        with self._rlock():
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
        with self._rlock():
            binTags = copy.deepcopy(binTags)

            # request = ('is_smart_redirection_for_a_tag_path_reduction_needed'
            #            , tuple(self.__db.sort_tag_list_by_hash(binTags)))
            request = ('is_smart_redirection_for_a_tag_path_reduction_needed', frozenset(binTags))
            result = self.cache.try_to_get_data_for_request(request)
            if result is None:
                self.__db.get_tags_for_a_smart_redirection(binTags)
                self.cache.put_new_request(request, result)

            result = copy.deepcopy(result)
            return result

    def fill_cache(self, max_answer_time_in_seconds=0.5, path=list()):
        ly = gly(self.default_priority)
        
        current_path = list(path)
        startTime = time.perf_counter()
        self.last_tested_fill_cache_tags = current_path

        tags_and_items_inside_curent_path = self.get_all(current_path, SMART_TREE_TYPE)
        internal_tags = tags_and_items_inside_curent_path[0]
        self.get_items(current_path, PLAIN_PSEUDO_TREE_TYPE)
        
        self.fill_cache_iterations += 1

        endTime = time.perf_counter()
        resultTime = endTime - startTime
        self.last_tested_fill_cache_result_time = resultTime
        if resultTime >= max_answer_time_in_seconds:
            self.last_fill_cache_tags = current_path
            self.last_fill_cache_result_time = resultTime
            for additional_tag in internal_tags:
                ly()
                new_path = current_path + [additional_tag]
                self.fill_cache(max_answer_time_in_seconds, new_path)

    def fill_web_cache(self, depth: int, max_answer_time_in_seconds=0.5, path=None):
        ly = gly(self.default_priority)
        ly()

        path = path or set()
        current_path = list(path)
        startTime = time.perf_counter()

        result, is_cached = self.web_browse_to(current_path, True)
        optimized_path, tags, items = result
        current_path = list(optimized_path)
        self.last_tested_fill_cache_tags = current_path
        
        self.fill_cache_iterations += 1
        depth -= 1
        
        if self.fill_cache_last_time_measurement_iterations == 0:
            self.fill_cache_last_time_measurement_iterations = self.fill_cache_iterations
        
        if self.fill_cache_last_time_measurement is None:
            self.fill_cache_last_time_measurement = time.perf_counter()
        else:
            dtime = time.perf_counter() - self.fill_cache_last_time_measurement
            if dtime >= 1.0:
                self.fill_cache_last_time_measurement = time.perf_counter()
                iterations = self.fill_cache_iterations - self.fill_cache_last_time_measurement_iterations
                self.fill_cache_iterations_per_second = iterations / dtime
                self.fill_cache_last_time_measurement_iterations = self.fill_cache_iterations

        endTime = time.perf_counter()
        resultTime = endTime - startTime
        self.last_tested_fill_cache_result_time = resultTime
        # if (depth > 0) and (is_cached or (resultTime >= max_answer_time_in_seconds)):
        # if (depth > 0) and (resultTime >= max_answer_time_in_seconds):
        if depth > 0:
            self.last_fill_cache_tags = current_path
            self.last_fill_cache_result_time = resultTime
            for additional_tag in tags:
                new_path = current_path + [additional_tag]
                self.fill_web_cache(depth, max_answer_time_in_seconds, new_path)
    
    def clear_cache(self):
        self.cache.clear()
        self.fill_cache_iterations = 0
    
    def web_browse_to(self, binTags, return_is_cached_result: bool = False, use_cache: bool = True):
        with self._rlock():
            binTags = copy.deepcopy(binTags)
            additional_tags = self.get_tags_for_a_smart_redirection(binTags)
            if additional_tags is not None:
                optimized_path = set(binTags) | set(additional_tags)
            else:
                optimized_path = binTags

            request = ('web_browse_to', frozenset(optimized_path))
            result = None
            if use_cache:
                result = self.cache.try_to_get_data_for_request(request)
                is_cached_result = True
            
            if result is None:
                is_cached_result = False
                items, items_ids = self.__db.get_items_from_tags(optimized_path, treeType=PLAIN_PSEUDO_TREE_TYPE, isAlsoNeedSetOfAllInternalItemIDsForThisSetOfTags=True)
                tags = self.__db.get_tags_from_tags(optimized_path, treeType=SMART_TREE_TYPE, prePreparedSetOfAllInternalItemIDsForThisSetOfTags=items_ids)
                result = (optimized_path, tags, items)
                if use_cache:
                    self.cache.put_new_request(request, result)

            result = copy.deepcopy(result)
            if return_is_cached_result:
                return result, is_cached_result
            else:
                return result
    
    def fs_browse_to(self, binTags):
        with self._rlock():
            binTags = copy.deepcopy(binTags)

            request = ('web_browse_to', frozenset(binTags))
            result = self.cache.try_to_get_data_for_request(request)
            if result is None:
                optimized_path = set(binTags) | set(self.__db.get_tags_for_a_smart_redirection(binTags))
                items = self.__db.get_items_from_tags(optimized_path, treeType=SMART_TREE_TYPE)
                tags = self.__db.get_tags_from_tags(optimized_path, treeType=SMART_TREE_TYPE)
                result = (optimized_path, tags, items)
                self.cache.put_new_request(request, result)

            result = copy.deepcopy(result)
            return result
