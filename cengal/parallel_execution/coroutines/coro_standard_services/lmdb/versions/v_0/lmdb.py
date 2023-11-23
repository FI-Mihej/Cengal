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


__all__ = ['Lmdb', 'LmdbRequest', 'KeyType', 'RawKeyType', 'ValueType', 'RawValueType', 'DbId', 'DbName', 'DbKeyError']

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_tools.await_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import *
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import CoroPriority
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.timer_func_runner import *
from cengal.file_system.file_manager import path_relative_to_current_dir
from cengal.time_management.load_best_timer import perf_counter
from cengal.data_manipulation.serialization import *
from cengal.introspection.inspect import get_exception
from typing import Hashable, Tuple, List, Any, Dict, Callable
import sys
import os
import asyncio
try:
    import lmdb as lmdb_lib
except ImportError:
    from warnings import warn
    warn('''WARNING: `lmdb` library is not installed. Lmdb service will not work.
         To install `lmdb` use: `pip install lmdb`''')
    raise


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


KeyType = Union[bytes, str, Any]
RawKeyType = bytes
ValueType = Any
RawValueType = bytes
DbId = Hashable
DbName = bytes


class LmdbRequest(ServiceRequest):
    def set_db_environment_path(self, path_to_db_environment: str) -> ServiceRequest:
        return self._save(0, path_to_db_environment)
    
    def open_databases(self, db_names: Dict[DbId, DbName]) -> ServiceRequest:
        return self._save(1, db_names)
    
    def drop_db(self, db_id: DbId, delete: bool = False) -> ServiceRequest:
        return self._save(2, db_id, delete)
    
    def sync(self) -> ServiceRequest:
        return self._save(3)
    
    def get(self, key: KeyType, db_id: DbId = None) -> ServiceRequest:
        return self._save(4, key, db_id)
    
    def get_items(self, keys: Set[Tuple[KeyType, DbId]]) -> ServiceRequest:
        return self._save(5, keys)
    
    def get_all_items(self, db_id: DbId = None) -> ServiceRequest:
        return self._save(6, db_id)
    
    def put(self, key: KeyType, value: Optional[ValueType] = None, db_id: DbId = None) -> ServiceRequest:
        return self._save(7, key, value, db_id)
    
    def put_items(self, items: Dict[Tuple[KeyType, DbId], Optional[ValueType]]) -> ServiceRequest:
        return self._save(8, items)
    
    def delete(self, key: KeyType, value: Optional[ValueType] = None, db_id: DbId = None) -> ServiceRequest:
        return self._save(9, key, value, db_id)
    
    def delete_items(self, items: Dict[Tuple[KeyType, DbId], Optional[ValueType]]) -> ServiceRequest:
        return self._save(10, items)

    def open_db_environment(self, path_to_db_environment: str) -> ServiceRequest:
        return self._save(11, path_to_db_environment)
    

def make_key_frozen(key):
    if isinstance(key, list) or isinstance(key, set):
        new_key = list()
        for item in key:
            new_key.append(make_key_frozen(item))
        
        key = tuple(new_key)

    return key
    

class Lmdb(Service, EntityStatsMixin):
    def __init__(self, loop: CoroScheduler):
        super(Lmdb, self).__init__(loop)
        self.default_db_name: DbName = b'__default__'
        self.drop_db_requests: Dict[CoroID, Tuple[Hashable, bool]] = dict()
        self.read_queue: List[Tuple[CoroID, Tuple[RawKeyType, DbId]]] = list()
        self.massive_read_queue: List[Tuple[CoroID, Set[Tuple[KeyType, DbId]]]] = list()
        self.data_cache: Dict[Tuple[Hashable, Hashable], Any] = dict()
        self.deletion_cache: Dict[Tuple[Hashable, Hashable], Any] = dict()
        self.get_all_items_queue: List[Tuple[CoroID, DbId]] = list()
        self.path_to_db_environment = path_relative_to_current_dir('lmdb.db')
        self.db_environment = None
        self.databases: Dict[Hashable, Any] = dict()
        self.db_names: Dict[DbId, DbName] = dict()
        self.async_loop = None
        self.sync_time_interval = 1.0
        self.last_sync_time = perf_counter()
        self.force_sync = False
        self.write_locked = False
        self.writes_num: int = 0
        self.reads_num: int = 0
        self.deletes_num: int = 0
        self.db_drops_num: int = 0
        self.write_locked_coro_id: Optional[CoroID] = None
        self.serializer = best_serializer({DataFormats.binary,
                                           Tags.can_use_bytes,
                                           Tags.decode_str_as_str,
                                           Tags.decode_list_as_list,
                                           Tags.decode_bytes_as_bytes,
                                           Tags.superficial,
                                           Tags.current_platform,
                                           Tags.multi_platform},
                                          test_data_factory(TestDataType.small),
                                          0.1)

        self._request_workers = {
            0: self._on_set_db_environment_path,
            1: self._open_databases,
            2: self._drop_db,
            3: self._on_sync,
            4: self._on_get,
            5: self._on_get_items,
            6: self._on_get_all_items,
            7: self._on_put,
            8: self._on_put_items,
            9: self._on_delete,
            10: self._on_delete_items,
            11: self._open_db_environment,
        }

    def get_entity_stats(self, stats_level: 'EntityStatsMixin.StatsLevel' = EntityStatsMixin.StatsLevel.debug) -> Tuple[str, Dict[str, Any]]:
        return type(self).__name__, {
            'db_names': list(self.db_names.keys()),
            'writes num': self.writes_num,
            'reads num': self.reads_num,
            'deletes num': self.deletes_num,
            'db drops num': self.db_drops_num,
        }

    def single_task_registration_or_immediate_processing(
            self, *args, **kwargs) -> ServiceProcessingResponse:
        result = self.try_resolve_request(*args, **kwargs)
        if result is None:
            return True, None, None
        else:
            return result

    def full_processing_iteration(self):
        self.force_sync = False
        
        if self.db_environment is None:
            self._init_db()

        data_cache_buff = self.data_cache
        self.data_cache = type(data_cache_buff)()
        
        read_queue_buff = self.read_queue
        self.read_queue = type(read_queue_buff)()
        
        massive_read_queue_buff = self.massive_read_queue
        self.massive_read_queue = type(massive_read_queue_buff)()
        
        deletion_cache_buff = self.deletion_cache
        self.deletion_cache = type(deletion_cache_buff)()
        
        get_all_items_queue_buff = self.get_all_items_queue
        self.get_all_items_queue = type(get_all_items_queue_buff)()

        # put
        def put_handler(db_environment, databases):
            db_id = None
            try:
                with db_environment.begin(write=True) as txn:
                    for key_info, value in data_cache_buff.items():
                        key, db_id = key_info
                        txn.put(key, value, db=databases[db_id], dupdata=False, append=False)

                self.writes_num += len(data_cache_buff)
            except lmdb_lib.MapFullError:
                raise DBError.from_exception(db_id)
        
        lmdb_reapplier(self.db_environment, self.databases, put_handler)
        
        # delete
        for key_info, value in deletion_cache_buff.items():
            with self.db_environment.begin(write=True) as txn:
                key, db_id = key_info
                txn.delete(key, value, db=self.databases[db_id])
                self.deletes_num += 1

        # drop
        drop_db_requests_buff = self.drop_db_requests
        self.drop_db_requests = type(drop_db_requests_buff)()
        dropped_databases: Set[Hashable] = set()
        processed_coroutines: Set[CoroID] = set()
        
        def drop_handler(db_environment, databases):
            for coro_id, request in drop_db_requests_buff.items():
                if coro_id in processed_coroutines:
                    continue
                
                db_id, delete_db = request
                if db_id not in dropped_databases:
                    try:
                        with db_environment.begin(write=True) as txn:
                            txn.drop(db=databases[db_id], delete=delete_db)
                        
                        self.db_drops_num += 1
                    except lmdb_lib.MapFullError:
                        raise DBError.from_exception(db_id)
                    
                    dropped_databases.add(db_id)
                
                self.register_response(coro_id, None, None)
                processed_coroutines.add(coro_id)
                    
        lmdb_reapplier(self.db_environment, self.databases, drop_handler)

        # get
        def get_item(txn, key_info, data_cache_buff) -> Tuple[ValueType, Optional[Exception]]:
            key, db_id = key_info
            if key_info in data_cache_buff:
                value = data_cache_buff[key_info]
            else:
                value = txn.get(key, db=self.databases[db_id])
                self.reads_num += 1
            
            exception = None
            try:
                if value is None:
                    exception = DbKeyError(key_info)
                else:
                    value = self.serializer.loads(value)
            except:
                exception = get_exception()
            
            return value, exception
            
        with self.db_environment.begin() as txn:
            for coro_id, key_info in read_queue_buff:
                value, exception = get_item(txn, key_info, data_cache_buff)
                self.register_response(coro_id, value, exception)
            
            for coro_id, set_of_key_info in massive_read_queue_buff:
                items: Dict[Tuple[KeyType, DbId], Tuple[ValueType, Optional[Exception]]] = dict()
                for key_info in set_of_key_info:
                    items[key_info] = get_item(txn, key_info, data_cache_buff)
                    self.register_response(coro_id, items, None)

        # get all items
        for coro_id, db_id in get_all_items_queue_buff:
            with self.db_environment.begin(db=self.databases[db_id]) as txn:
                result = dict()
                exception = None
                try:
                    # for k, v in txn.cursor(db=self.databases[db_id]):
                    #     key = make_key_frozen(self.serializer.loads(k))
                    #     value = self.serializer.loads(v)
                    #     result[key] = value
                    result = {make_key_frozen(self.serializer.loads(k)): self.serializer.loads(v) for k, v in txn.cursor(db=self.databases[db_id])}
                    self.reads_num += len(result)
                except:
                    exception = get_exception()
                
                self.register_response(coro_id, result, exception)
        
        # sync
        self.sync_in_thread_pool()
        
        self.last_sync_time = perf_counter()

        self.make_dead()

    def in_work(self) -> bool:
        result: bool = (bool(self.read_queue) or bool(self.massive_read_queue) or bool(self.get_all_items_queue)) or (self.force_sync or ((not bool(self.write_locked)) and (bool(self.data_cache) or bool(self.deletion_cache) or bool(self.drop_db_requests)) and ((perf_counter() - self.last_sync_time) >= self.sync_time_interval)))
        return self.thrifty_in_work(result)
    
    def time_left_before_next_event(self) -> Tuple[bool, Optional[Union[int, float]]]:
        time_since_last_sync_time: float = perf_counter() - self.last_sync_time
        if self.sync_time_interval > time_since_last_sync_time:
            return True, self.sync_time_interval - time_since_last_sync_time
        else:
            return True, 0

    def _init_db(self):
        print(f'self.path_to_db_environment: {self.path_to_db_environment}')
        self.db_environment = lmdb_lib.open(self.path_to_db_environment, map_size=20 * 1024**2, writemap=True, max_dbs=10,
                                        map_async=True, lock=False, metasync=False, sync=False, meminit=False)
        self.databases[None] = self.db_environment.open_db(self.default_db_name)
        self.db_environment.sync(True)
    
    def _open_db_environment(self, path_to_db_environment: str) -> ServiceProcessingResponse:
        raise NotImplementedError

    def _on_set_db_environment_path(self, path_to_db_environment: str) -> ServiceProcessingResponse:
        if self.write_locked:
            return True, False, None
        
        if self.db_environment is None:
            self.path_to_db_environment = path_to_db_environment
            try:
                self._init_db()
            except:
                exception = get_exception()
                return True, False, exception
            return True, True, None
        else:
            return True, False, None
    
    def _on_sync(self) -> ServiceProcessingResponse:
        if self.data_cache:
            self.force_sync = True
            self.make_live()
        else:
            # self.db_environment.sync(True)
            self.sync_in_thread_pool()
        
        return True, None, None
    
    def _on_get(self, key: KeyType, db_id: DbId = None) -> ServiceProcessingResponse:
        key = self.serializer.dumps(key)
        
        key_info = (key, db_id)
        if key_info in self.data_cache:
            return True, self.data_cache[key_info], None
        else:
            self.read_queue.append((self.current_caller_coro_info.coro_id, key_info))
            self.make_live()
            return False, None, None
    
    def _on_get_items(self, keys: Set[Tuple[KeyType, DbId]]) -> ServiceProcessingResponse:
        coro_id = self.current_caller_coro_info.coro_id
        
        raw_keys: Set[Tuple[KeyType, DbId]] = set()
        for key, db_id in keys:
            key = self.serializer.dumps(key)
            
            raw_keys.add((key, db_id))
        
        self.massive_read_queue.append((coro_id, raw_keys))
        self.make_live()
        return False, None, None
    
    def _on_get_all_items(self, db_id: DbId) -> ServiceProcessingResponse:
        coro_id = self.current_caller_coro_info.coro_id
        self.get_all_items_queue.append((coro_id, db_id))
        self.make_live()
        return False, None, None
    
    def _on_put(self, key: KeyType, value: Any, db_id: DbId = None) -> ServiceProcessingResponse:
        key = self.serializer.dumps(key)
        
        key_info = (key, db_id)
        exception = None
        result = None
        try:
            result = self.data_cache[key_info] = self.serializer.dumps(value)
        except:
            exception = get_exception()
        
        self.make_live()
        return True, result, exception
    
    def _on_put_items(self, items: Dict[Tuple[KeyType, DbId], ValueType]) -> ServiceProcessingResponse:
        result_items: Dict[Tuple[KeyType, DbId], Tuple[ValueType, Optional[Exception]]] = dict()
        for key_info, value in items.items():
            key, db_id = key_info
            key = self.serializer.dumps(key)
            
            key_info = (key, db_id)
            exception = None
            result = None
            try:
                result = self.data_cache[key_info] = self.serializer.dumps(value)
            except:
                exception = get_exception()
            
            result_items[key_info] = (result, exception)
        
        self.make_live()
        return True, result_items, None
    
    def _on_delete(self, key: KeyType, value: Any, db_id: DbId = None) -> ServiceProcessingResponse:
        key = self.serializer.dumps(key)
        
        key_info = (key, db_id)
        exception = None
        result = None
        try:
            result = self.deletion_cache[key_info] = self.serializer.dumps(value)
        except:
            exception = get_exception()
        
        self.make_live()
        return True, result, exception
    
    def _on_delete_items(self, items: Dict[Tuple[KeyType, DbId], ValueType]) -> ServiceProcessingResponse:
        result_items: Dict[Tuple[KeyType, DbId], Tuple[ValueType, Optional[Exception]]] = dict()
        for key_info, value in items.items():
            key, db_id = key_info
            key = self.serializer.dumps(key)
            
            key_info = (key, db_id)
            exception = None
            result = None
            try:
                result = self.deletion_cache[key_info] = self.serializer.dumps(value)
            except:
                exception = get_exception()
            
            result_items[key_info] = (result, exception)
        
        self.make_live()
        return True, result_items, None
    
    def _open_databases(self, db_names: Dict[DbId, DbName]) -> ServiceProcessingResponse:
        for db_id, db_name in db_names.items():
            self.databases[db_id] = self.db_environment.open_db(db_name)
            self.db_names[db_id] = db_name
        
        self.db_environment.sync(True)
        return True, None, None
    
    def _drop_db(self, db_id: DbId, delete: bool = False) -> ServiceProcessingResponse:
        coro_id = self.current_caller_coro_info.coro_id
        self.drop_db_requests[coro_id] = (db_id, delete)
        self.make_live()
        return False, None, None
    
    def sync_in_thread_pool(self):
        async def sync_db_coro(i: Interface, self, asyncio_loop, need_to_ensure_asyncio_loop: bool):
            if need_to_ensure_asyncio_loop:
                asyncio_loop = await i(AsyncioLoop, AsyncioLoopRequest().ensure_loop(None,CoroPriority.low, True))
            else:
                if asyncio_loop is None:
                    asyncio_loop = await i(AsyncioLoop, AsyncioLoopRequest().get())
            
            async def sync_db(self, asyncio_loop):
                def sync_worker():
                    self.db_environment.sync(True)
                
                await task_in_thread_pool(asyncio_loop, sync_worker)

            await i(AsyncioLoop, AsyncioLoopRequest().wait(sync_db(self, asyncio_loop)))
            self.write_locked_coro_id = None
            self.write_locked = False
            def make_service_live_for_a_next_sync(self):
                self.make_live()
            
            await i(TimerFuncRunner, self.sync_time_interval, make_service_live_for_a_next_sync, self)

        asyncio_loop = None
        need_to_ensure_asyncio_loop = False
        try:
            asyncio_loop = self._loop.get_service_instance(AsyncioLoop).inline_get()
        except AsyncioLoopWasNotSetError:
            need_to_ensure_asyncio_loop = True

        coro: CoroWrapperBase = self._loop.put_coro(sync_db_coro, self, asyncio_loop, need_to_ensure_asyncio_loop)
        self.write_locked = True
        self.write_locked_coro_id = coro.coro_id


LmdbRequest.default_service_type = Lmdb


class DbKeyError(KeyError):
    def __init__(self, key_info: Tuple[KeyType, DbId], *args: object) -> None:
        super().__init__(*args)
        self.key_info: Tuple[KeyType, DbId] = key_info


class DBError(Exception):
    def __init__(self, db_id: DbId, original_exception: Exception, *args):
        super().__init__(*args)
        self.db_id: DbId = db_id
        self.original_exception = original_exception
    
    @staticmethod
    def from_exception(db_id: DbId) -> 'DBError':
        return DBError(db_id, get_exception())


def lmdb_reapplier(environment: lmdb_lib.Environment, databases: Dict[Hashable, Any], handler: Callable):
    failed = True
    while failed:
        need_to_resize: bool = False
        try:
            handler(environment, databases)
            failed = False
        except DBError as err:
            if isinstance(err.original_exception, lmdb_lib.MapFullError):
                need_to_resize = True
        
        if need_to_resize:
            environment.set_mapsize(environment.info()['map_size'] + 2 * 1024**2)
