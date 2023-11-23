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


__all__ = ['Db', 'DbRequest', 'KeyType', 'RawKeyType', 'ValueType', 'RawValueType', 'DbId', 'DbName', 'DbKeyError']

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_tools.await_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import *
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import CoroPriority
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.timer_func_runner import *
from cengal.parallel_execution.coroutines.coro_standard_services.instance import *
from cengal.file_system.file_manager import path_relative_to_current_dir
from cengal.time_management.load_best_timer import perf_counter
from cengal.data_manipulation.serialization import *
from cengal.introspection.inspect import get_exception
from cengal.file_system.app_fs_structure.app_dir_path import AppDirPath, AppDirectoryType
from cengal.file_system.path_manager import RelativePath
from typing import Hashable, Tuple, List, Any, Dict, Callable, Sequence
import sys
import os
import asyncio
try:
    import lmdb
except ImportError:
    from warnings import warn
    warn('''WARNING: `lmdb` library is not installed. Db service will not work.
         To install `lmdb` use: `pip install lmdb`''')
    raise

from os.path import normpath
from uuid import uuid4


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


SingleKeyType = Union[bytes, str]
CompoundKeyType = Union[List[SingleKeyType], Set[SingleKeyType], Tuple[SingleKeyType], List['CompoundKeyType'], Set['CompoundKeyType'], Tuple['CompoundKeyType']]
KeyType = Union[SingleKeyType, CompoundKeyType]
NormalizedCompoundKeyType = Union[Tuple[SingleKeyType], Tuple['NormalizedCompoundKeyType']]
NormalizedKeyType = Union[SingleKeyType, NormalizedCompoundKeyType]
RawKeyType = bytes  # By default record keys are limited to 511 bytes in length, however this can be adjusted by rebuilding the library. The compile-time key length can be queried via Environment.max_key_size()
ValueType = Any
RawValueType = bytes
DbId = Hashable
DbName = bytes
EnvId = Hashable


class KeyInfo:
    def __init__(self, key: KeyType, db_id: DbId = None, env_id: EnvId = None):
        self.key: KeyType = key
        self.db_id: DbId = db_id
        self.env_id: EnvId = env_id


class EnvInitInfo:
    def __init__(self, path_to_db_environment: str, *args, **kwargs):
        self.path_to_default_db_environment: str = normpath(path_to_db_environment)
        self.args: Tuple = (self.path_to_default_db_environment,) + args
        self.kwargs: Dict = kwargs


class EnvInfo:
    db_name_prefix = '__db_name_key__'

    def __init__(self, init_info: EnvInitInfo, env: lmdb.Environment):
        self.init_info: EnvInitInfo = init_info
        self.env: lmdb.Environment = env
        self.env_id: EnvId = init_info.path_to_default_db_environment
        self.databases: Dict[Hashable, lmdb._Database] = dict()
        self.db_names: Dict[DbId, DbName] = dict()
    
    @staticmethod
    def gen_db_name_from_db_id(db_id: DbId) -> bytes:
        return f'{EnvInfo.db_name_prefix}{db_id}'.encode('utf-8')
    
    def db_name_by_db_id(self, db_id: DbId) -> bytes:
        db_name: bytes = EnvInfo.gen_db_name_from_db_id(db_id)
        try:
            return self.db_names[db_name]
        except KeyError:
            raise UnknownEnvDBError(self.env_id, db_id)
    
    def db_by_db_id(self, db_id: DbId) -> lmdb._Database:
        try:
            return self.databases[db_id]
        except KeyError:
            raise UnknownEnvDBError(self.env_id, db_id)


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


class UnknownEnvError(Exception):
    pass


class UnknownEnvDBError(Exception):
    pass


class WrongKeyTypeError(TypeError):
    pass


class RawKeyIsTooLargeError(ValueError):
    pass


class NormalizedCompoundKey:
    def __init__(self, normalized_key: NormalizedKeyType) -> None:
        self.normalized_key: NormalizedKeyType = normalized_key
    
    def __call__(self) -> Any:
        return self.normalized_key

    @staticmethod
    def from_key(key: KeyType):
        return NormalizedCompoundKey(normalize_compound_key(key))


NCK = NormalizedCompoundKey
InputKeyType = Union[NormalizedCompoundKey, KeyType]


def is_normalized_compound_key(key: KeyType) -> bool:
    if isinstance(key, (bytes, str, int, float)):
        return True
    elif isinstance(key, tuple):
        return all(is_normalized_compound_key(item) for item in key)
    else:
        return False


def normalize_compound_key(key: KeyType) -> NormalizedKeyType:
    if isinstance(key, NormalizedCompoundKey):
        return key()
    elif is_normalized_compound_key(key):
        return key
    elif isinstance(key, list):
        need_to_sort: bool = False
    elif isinstance(key, (set, frozenset)):
        need_to_sort = True
    elif isinstance(key, dict):
        key = tuple(key.items())
        need_to_sort = True
    else:
        raise WrongKeyTypeError(f'Wrong key type: {type(key)}: {key}')

    new_key = list()
    for item in key:
        new_key.append(normalize_compound_key(item))
    
    if need_to_sort:
        new_key.sort()
    
    key = tuple(new_key)

    return key


class DbRequest(ServiceRequest):
    def __init__(self, env_id: EnvId = None, db_id: DbId = None):
        super().__init__()
        self.env_id: EnvId = env_id
        self.db_id: DbId = db_id
        self.provide_to_request_handler = True
    
    def _copy(self) -> 'DbRequest':
        return DbRequest(self.env_id, self.db_id)
    
    def _get_db_id(self, db_id: DbId) -> DbId:
        if self.db_id is None:
            return db_id
        else:
            return self.db_id
    
    def set_default_db_environment_path(self, path_to_db_environment: str) -> bool:
        return self._save_to_copy(0, path_to_db_environment)
    
    def open_databases(self, db_names: Dict[DbId, DbName]) -> None:
        return self._save_to_copy(1, db_names)
    
    def drop_db(self, db_id: DbId, delete: bool = False) -> None:
        return self._save_to_copy(2, db_id, delete)
    
    def sync(self) -> None:
        return self._save_to_copy(3)
    
    def get(self, key: InputKeyType, db_id: DbId = None) -> ValueType:
        return self._save_to_copy(4, key, db_id)
    
    def get_first(self, db_id: DbId = None) -> Dict[NormalizedKeyType, ValueType]:
        # Returns first item in DB
        return self._save_to_copy(14, db_id)
    
    def get_last(self, db_id: DbId = None) -> Dict[NormalizedKeyType, ValueType]:
        # Returns last item in DB
        return self._save_to_copy(15, db_id)
    
    def get_items(self, db_keys: Sequence[InputKeyType], db_id: DbId = None) -> List[Tuple[NormalizedKeyType, Tuple[ValueType, Optional[Exception]]]]:
        return self._save_to_copy(5, db_keys, db_id)
    
    def get_n_items(self, desired_key: InputKeyType, num: Optional[int] = None, db_id: DbId = None) -> List[Tuple[NormalizedKeyType, ValueType]]:
        return self._save_to_copy(16, desired_key, num, db_id, reverse=False)
    
    def get_reverse_n_items(self, desired_key: InputKeyType, num: Optional[int] = None, db_id: DbId = None) -> List[Tuple[NormalizedKeyType, ValueType]]:
        return self._save_to_copy(16, desired_key, num, db_id, reverse=True)
    
    def get_items_range(self, first_desired_key: InputKeyType, last_desired_key: InputKeyType, num: Optional[int] = None, db_id: DbId = None) -> List[Tuple[NormalizedKeyType, ValueType]]:
        return self._save_to_copy(17, first_desired_key, last_desired_key, num, db_id, reverse=False)
    
    def get_reverse_items_range(self, first_desired_key: InputKeyType, last_desired_key: InputKeyType, num: Optional[int] = None, db_id: DbId = None) -> List[Tuple[NormalizedKeyType, ValueType]]:
        return self._save_to_copy(17, first_desired_key, last_desired_key, num, db_id, reverse=True)
    
    def get_all_items(self, db_id: DbId = None) -> List[Tuple[NormalizedKeyType, ValueType]]:
        # Returns all items from DB
        return self._save_to_copy(6, db_id)
    
    def put(self, key: InputKeyType, value: Optional[ValueType] = None, db_id: DbId = None) -> RawValueType:
        return self._save_to_copy(7, key, value, db_id)
    
    def put_items(self, db_items: Dict[InputKeyType, ValueType], db_id: DbId = None) -> Dict[DbId, Dict[RawKeyType, Tuple[RawValueType, Optional[Exception]]]]:
        return self._save_to_copy(8, db_items, db_id)
    
    def delete(self, key: InputKeyType, db_id: DbId = None) -> RawValueType:
        return self._save_to_copy(9, key, db_id)
    
    def delete_kv(self, key: InputKeyType, value: ValueType, db_id: DbId = None) -> RawValueType:
        return self._save_to_copy(10, key, value, db_id)
    
    def delete_items(self, db_items: Set[InputKeyType], db_id: DbId = None) -> Dict[DbId, Dict[RawKeyType, Tuple[RawValueType, Optional[Exception]]]]:
        return self._save_to_copy(11, db_items, db_id)
    
    def delete_kv_items(self, db_items: Dict[InputKeyType, Tuple[ValueType]], db_id: DbId = None) -> Dict[DbId, Dict[RawKeyType, Tuple[RawValueType, Optional[Exception]]]]:
        return self._save_to_copy(12, db_items, db_id)

    def open_db_environment(self, path_to_db_environment: str) -> EnvId:
        return self._save_to_copy(13, path_to_db_environment)
    
    def lock_databases(self, db_names: Optional[Set[DbId]] = None) -> None:
        # Lock all databases if db_names is None. Databases will be released automatically wnen coroutine execution will be finished
        return self._save_to_copy(18, db_names)
    
    def try_lock_databases(self, db_names: Optional[Set[DbId]] = None) -> bool:
        # Tries to lock all databases if db_names is None. Returns True if try was successfull. False otherwise. Databases will be released automatically wnen coroutine execution will be finished
        return self._save_to_copy(19, db_names)
    
    def unlock_databases(self, db_names: Optional[Set[DbId]] = None) -> None:
        # Unlock all databases if db_names is None
        return self._save_to_copy(18, db_names)
    

class Db(Service, EntityStatsMixin):
    def __init__(self, loop: CoroScheduler):
        super(Db, self).__init__(loop)
        self.default_db_id: DbName = b'__default__'
        self.default_env_name: str = '__default__.dbenv'
        # self.drop_db_requests: Dict[CoroID, Tuple[Hashable, bool]] = dict()
        # self.drop_db_requests: Dict[EnvId, Dict[CoroID, Tuple[DbId, bool]]] = dict()
        self.drop_db_requests: Dict[EnvId, Dict[DbId, List[bool, Set[CoroID]]]] = dict()
        # self.read_queue: List[Tuple[CoroID, Tuple[RawKeyType, DbId]]] = list()
        self.read_queue: Dict[EnvId, Dict[DbId, Dict[RawKeyType, Set[CoroID]]]] = dict()
        self.massive_read_queue: Dict[EnvId, Dict[CoroID, Dict[DbId, Set[RawKeyType]]]] = dict()
        # self.massive_read_queue: List[Tuple[CoroID, Set[Tuple[KeyType, DbId]]]] = list()
        self.data_cache: Dict[EnvId, Dict[DbId, Dict[RawKeyType, RawValueType]]] = dict()
        # self.data_cache: Dict[EnvId, Dict[Tuple[RawKeyType, DbId], RawValueType]] = dict()
        self.deletion_cache: Dict[EnvId, Dict[DbId, Set[RawKeyType]]] = dict()
        self.kv_deletion_cache: Dict[EnvId, Dict[DbId, Dict[RawKeyType, RawValueType]]] = dict()
        # self.kv_deletion_cache: Dict[Tuple[Hashable, Hashable], Any] = dict()
        self.get_first_queue: Dict[EnvId, Dict[DbId, Set[CoroID]]] = dict()
        self.get_last_queue: Dict[EnvId, Dict[DbId, Set[CoroID]]] = dict()
        self.get_n_items_queue: Dict[EnvId, Dict[CoroID, Tuple[DbId, RawKeyType, int, bool]]] = dict()
        self.get_items_range_queue: Dict[EnvId, Dict[CoroID, Tuple[DbId, RawKeyType, RawKeyType, int, bool]]] = dict()
        self.get_all_items_queue: List[Tuple[CoroID, DbId, EnvId]] = list()
        self.path_to_default_db_environment: str = None
        self.app_name_waiter: CoroWrapperBase = None
        self.default_db_environment: lmdb.Environment = None
        self.db_environments: Dict[EnvId, EnvInfo] = dict()
        # self.databases: Dict[Hashable, Any] = dict()
        # self.db_names: Dict[DbId, DbName] = dict()
        self.async_loop = None
        self.sync_time_interval = 1.0
        self.last_sync_time = perf_counter()
        self.force_sync: Set[EnvId] = set()
        self.write_locked: Set[EnvId] = set()
        self.writes_num: int = 0
        self.reads_num: int = 0
        self.deletes_num: int = 0
        self.db_drops_num: int = 0
        self.write_locked_coro_id: Set[CoroID] = set()
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
            0: self._on_set_default_db_environment_path,
            1: self._on_open_databases,
            2: self._on_drop_db,
            3: self._on_sync,
            4: self._on_get,
            5: self._on_get_items,
            6: self._on_get_all_items,
            7: self._on_put,
            8: self._on_put_items,
            9: self._on_delete,
            10: self._on_delete_kv,
            11: self._on_delete_items,
            12: self._on_delete_kv_items,
            13: self._on_open_db_environment,
            14: self._on_get_first,
            15: self._on_get_last,
            16: self._on_get_n_items,
            17: self._on_get_items_range,
        }

    # TODO: sync with last implementation
    def get_entity_stats(self, stats_level: 'EntityStatsMixin.StatsLevel' = EntityStatsMixin.StatsLevel.debug) -> Tuple[str, Dict[str, Any]]:
        return type(self).__name__, {
            'db_names': list(self.db_names.keys()),
            'writes num': self.writes_num,
            'reads num': self.reads_num,
            'deletes num': self.deletes_num,
            'db drops num': self.db_drops_num,
        }
    
    def norm_key(self, key: InputKeyType) -> NormalizedKeyType:
        return normalize_compound_key(key)

    def raw_key(self, env_or_id: Union[lmdb.Environment, EnvId], key: InputKeyType) -> RawKeyType:
        raw_key: bytes = self.serializer.dumps(normalize_compound_key(key))
        if isinstance(env_or_id, lmdb.Environment):
            env = env_or_id
        else:
            env = self.db_environments[env_or_id].env
        
        if len(raw_key) > env.max_key_size():
            raise RawKeyIsTooLargeError(f'Raw form ({raw_key=}) of the key ({key=}) is too large: {len(raw_key)} > {env.max_key_size()}')

    def single_task_registration_or_immediate_processing(
            self, *args, **kwargs) -> ServiceProcessingResponse:
        result = self.try_resolve_request(*args, **kwargs)
        if result is None:
            return True, None, None
        else:
            return result

    def full_processing_iteration(self):
        if self.default_db_environment is None:
            if self.path_to_default_db_environment is None:
                if self.app_name_waiter is None:
                    async def coro(i: Interface, self: 'Db'):
                        app_name_for_fs = await i(InstanceRequest().wait('app_name_for_fs'))
                        app_data_dir_path_type: AppDirectoryType = await i(InstanceRequest().wait('app_data_dir_path_type'))
                        app_dir_path: AppDirPath = await i(InstanceRequest().wait(AppDirPath))
                        app_data_dir_path: str = app_dir_path.cached(app_data_dir_path_type, app_name_for_fs)
                        self.path_to_default_db_environment = RelativePath(app_data_dir_path)(self.default_env_name)
                        self.app_name_waiter = None
                        self.make_live()
                    
                    self.app_name_waiter = put_root_from_other_service(self, coro, self)
                    self.app_name_waiter.is_background_coro = True
                
                self.make_dead()
                return
            else:
                self._init_default_db()
        
        if self.force_sync:
            envs_need_to_be_sync: Set[DbId] = self.force_sync
            self.force_sync = set()
        else:
            envs_need_to_be_sync = set()
        
        data_cache_buff = self.data_cache
        self.data_cache = type(data_cache_buff)()
        
        read_queue_buff = self.read_queue
        self.read_queue = type(read_queue_buff)()
        
        massive_read_queue_buff = self.massive_read_queue
        self.massive_read_queue = type(massive_read_queue_buff)()
        
        kv_deletion_cache_buff = self.kv_deletion_cache
        self.kv_deletion_cache = type(kv_deletion_cache_buff)()
        
        get_all_items_queue_buff = self.get_all_items_queue
        self.get_all_items_queue = type(get_all_items_queue_buff)()

        get_first_queue_buff = self.get_first_queue
        self.get_first_queue = type(get_first_queue_buff)()

        get_last_queue_buff = self.get_last_queue
        self.get_last_queue = type(get_last_queue_buff)()

        get_n_items_queue_buff = self.get_n_items_queue
        self.get_n_items_queue = type(get_n_items_queue_buff)()

        get_items_range_queue_buff = self.get_items_range_queue
        self.get_items_range_queue = type(get_items_range_queue_buff)()

        # put
        def put_handler(env_info: EnvInfo, put_info: Dict[DbId, Dict[RawKeyType, RawValueType]]):
            try:
                with env_info.env.begin(write=True) as txn:
                    for db_id, db_put_info in put_info.items():
                        if db_id in env_info.databases:
                            for raw_key, value in db_put_info.items():
                                txn.put(raw_key, value, db=env_info.databases[db_id], dupdata=False, append=False)
                        
                        self.writes_num += len(db_put_info)
            except lmdb.MapFullError:
                raise DBError.from_exception(db_id)
        
        for env_id, put_info in data_cache_buff.items():
            if env_id in self.db_environments:
                envs_need_to_be_sync.add(env_id)
                lmdb_reapplier(self.db_environments[env_id], put_handler, put_info)

        # TODO: implement delete* methods processing
        # delete
        for env_id, kv_deletion_cache_buff_db_info in kv_deletion_cache_buff.items():
            if env_id in self.db_environments:
                envs_need_to_be_sync.add(env_id)
                ...

        for key_info, value in kv_deletion_cache_buff.items():
            with self.default_db_environment.begin(write=True) as txn:
                key, db_id = key_info
                txn.delete(key, value, db=self.databases[db_id])
                self.deletes_num += 1

        # drop
        drop_db_requests_buff = self.drop_db_requests
        self.drop_db_requests = type(drop_db_requests_buff)()
        
        def drop_handler(env_info: EnvInfo, drop_info: Dict[DbId, List[bool, Set[CoroID]]]):
            for db_id, db_drop_info in drop_info.items():
                delete_db, coro_id = db_drop_info
                if db_id in env_info.databases:
                    try:
                        with env_info.env.begin(write=True) as txn:
                            txn.drop(db=env_info.databases[db_id], delete=delete_db)
                            if delete_db:
                                del env_info.databases[db_id]
                                del env_info.db_names[db_id]
                        
                        self.db_drops_num += 1
                    except lmdb.MapFullError:
                        raise DBError.from_exception(db_id)
                    
                    self.register_response(coro_id, None, UnknownEnvError(env_id))
                else:
                    self.register_response(coro_id, None, UnknownEnvDBError(env_id, db_id))
        
        for env_id, drop_info in drop_db_requests_buff.items():
            if env_id in self.db_environments:
                envs_need_to_be_sync.add(env_id)
                lmdb_reapplier(self.db_environments[env_id], drop_handler, drop_info)
            else:
                for db_id, db_drop_info in drop_info.items():
                    delete_db, coro_id = db_drop_info
                    self.register_response(coro_id, None, UnknownEnvError(env_id))

        # get
        def get_item(txn, key_info: Tuple[RawKeyType, DbId, EnvId], data_cache_buff: Dict[EnvId, Dict[DbId, Dict[RawKeyType, RawValueType]]]) -> Tuple[ValueType, Optional[Exception]]:
            key, db_id, env_id = key_info
            need_to_get_from_db = True
            try:
                value = data_cache_buff[env_id][db_id][key]
                need_to_get_from_db = False
            except KeyError:
                pass
            
            if need_to_get_from_db:
                value = txn.get(key, db=self.db_environments[env_id].databases[db_id])
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
        
        # _on_get
        for env_id, read_queue_buff_db_info in read_queue_buff.items():
            if env_id in self.db_environments:
                env_info = self.db_environments[env_id]
                for db_id, read_queue_buff_db_key_info in read_queue_buff_db_info.items():
                    if db_id in env_info.databases:
                        with env_info.env.begin() as txn:
                            for raw_key, coro_ids in read_queue_buff_db_key_info.items():
                                value, exception = get_item(txn, (raw_key, db_id, env_id), data_cache_buff)
                                for coro_id in coro_ids:
                                    self.register_response(coro_id, value, exception)
                    else:
                        for raw_key, coro_ids in read_queue_buff_db_key_info.items():
                            for coro_id in coro_ids:
                                self.register_response(coro_id, None, UnknownEnvDBError(env_id, db_id))
            else:
                for db_id, read_queue_buff_db_key_info in read_queue_buff_db_info.items():
                    for raw_key, coro_ids in read_queue_buff_db_key_info.items():
                        for coro_id in coro_ids:
                            self.register_response(coro_id, None, UnknownEnvError(env_id))
        
        # _on_get_items
        results: Dict[CoroID, Dict[DbId, Dict[NormalizedKeyType, Tuple[ValueType, Optional[Exception]]]]] = dict()
        for env_id, massive_read_queue_buff_coro_info in massive_read_queue_buff.items():
            if env_id in self.db_environments:
                env_info = self.db_environments[env_id]
                for coro_id, read_queue_buff_db_info in massive_read_queue_buff_coro_info.items():
                    if coro_id not in results:
                        results[coro_id] = dict()
                    
                    coro_results = results[coro_id]
                    for db_id, raw_keys in read_queue_buff_db_info.items():
                        if db_id not in coro_results:
                            coro_results[db_id] = dict()
                        
                        coro_db_results = coro_results[db_id]
                        if db_id in env_info.databases:
                            with env_info.env.begin() as txn:
                                for raw_key in raw_keys:
                                    value, exception = get_item(txn, (raw_key, db_id, env_id), data_cache_buff)
                                    coro_db_results[normalize_compound_key(raw_key)] = (value, exception)
                        else:
                            for coro_id in coro_ids:
                                self.register_response(coro_id, None, UnknownEnvDBError(env_id, db_id))
            else:
                for coro_id, read_queue_buff_db_info in massive_read_queue_buff_coro_info.items():
                    for db_id, raw_keys in read_queue_buff_db_info.items():
                        for coro_id in coro_ids:
                            self.register_response(coro_id, None, UnknownEnvError(env_id))
        
        for coro_id, coro_results in results.items():
            self.register_response(coro_id, coro_results, None)

        # get all items
        for coro_id, db_id, env_id in get_all_items_queue_buff:
            if env_id in self.db_environments:
                env_info = self.db_environments[env_id]
                env = env_info.env
                if db_id in env_info.databases:
                    db = env_info.databases[db_id]
                    with env.begin(db=db) as txn:
                        result = list()
                        exception = None
                        try:
                            result = [(normalize_compound_key(self.serializer.loads(k)), self.serializer.loads(v)) for k, v in txn.cursor()]
                            self.reads_num += len(result)
                        except:
                            exception = get_exception()
                        
                        self.register_response(coro_id, result, exception)
                else:
                    self.register_response(coro_id, None, UnknownEnvDBError(env_id, db_id))
            else:
                self.register_response(coro_id, None, UnknownEnvError(env_id))
        
        # get_first
        for env_id, get_first_queue_buff_db_info in get_first_queue_buff.items():
            if env_id in self.db_environments:
                env_info = self.db_environments[env_id]
                for db_id, coro_ids in get_first_queue_buff_db_info.items():
                    if db_id in env_info.databases:
                        db = env_info.databases[db_id]
                        with env_info.env.begin(db=db) as txn:
                            result = None
                            exception = None
                            try:
                                cursor: lmdb.Cursor = txn.cursor()
                                if cursor.first():
                                    result = (normalize_compound_key(self.serializer.loads(cursor.key())), self.serializer.loads(cursor.value()))
                                    self.reads_num += 1
                                else:
                                    exception = KeyError()
                            except:
                                exception = get_exception()
                            
                            for coro_id in coro_ids:
                                self.register_response(coro_id, result, exception)
                    else:
                        for coro_id in coro_ids:
                            self.register_response(coro_id, None, UnknownEnvDBError(env_id, db_id))
            else:
                for db_id, coro_ids in get_first_queue_buff_db_info.items():
                    for coro_id in coro_ids:
                        self.register_response(coro_id, None, UnknownEnvError(env_id))
        
        # get_last
        for env_id, get_last_queue_buff_db_info in get_last_queue_buff.items():
            if env_id in self.db_environments:
                env_info = self.db_environments[env_id]
                for db_id, coro_ids in get_last_queue_buff_db_info.items():
                    if db_id in env_info.databases:
                        db = env_info.databases[db_id]
                        with env_info.env.begin(db=db) as txn:
                            result = None
                            exception = None
                            try:
                                cursor: lmdb.Cursor = txn.cursor()
                                if cursor.first():
                                    result = (normalize_compound_key(self.serializer.loads(cursor.key())), self.serializer.loads(cursor.value()))
                                    self.reads_num += 1
                                else:
                                    exception = KeyError()
                            except:
                                exception = get_exception()
                            
                            for coro_id in coro_ids:
                                self.register_response(coro_id, result, exception)
                    else:
                        for coro_id in coro_ids:
                            self.register_response(coro_id, None, UnknownEnvDBError(env_id, db_id))
            else:
                for db_id, coro_ids in get_last_queue_buff_db_info.items():
                    for coro_id in coro_ids:
                        self.register_response(coro_id, None, UnknownEnvError(env_id))
        
        # get_n_items
        for env_id, get_n_items_queue_buff_coro_info in get_n_items_queue_buff.items():
            if env_id in self.db_environments:
                env_info = self.db_environments[env_id]
                for coro_id, read_queue_buff_db_info in get_n_items_queue_buff_coro_info.items():
                    coro_results: List[Tuple[NormalizedKeyType, ValueType]] = list()
                    db_id, first_desired_raw_key, num_items, reverse = read_queue_buff_db_info
                    if db_id in env_info.databases:
                        db = env_info.databases[db_id]
                        with env_info.env.begin(db=db) as txn:
                            result = None
                            exception = None
                            try:
                                cursor: lmdb.Cursor = txn.cursor()
                                if cursor.set_range(first_desired_raw_key):
                                    if reverse:
                                        cursor_iterator = cursor.iterprev(keys=True, values=True)
                                    else:
                                        cursor_iterator = cursor.iternext(keys=True, values=True)
                                    
                                    for raw_key, raw_value in cursor_iterator:
                                        if (num_items is not None) and (num_items <= 0):
                                            break
                                        
                                        coro_results.append((normalize_compound_key(self.serializer.loads(raw_key)), self.serializer.loads(raw_value)))
                                        self.reads_num += 1
                                        if num_items is not None:
                                            num_items -= 1
                                else:
                                    exception = KeyError()
                            except:
                                exception = get_exception()
                            
                            self.register_response(coro_id, result, exception)
                    else:
                        self.register_response(coro_id, None, UnknownEnvDBError(env_id, db_id))
            else:
                for coro_id, read_queue_buff_db_info in get_n_items_queue_buff_coro_info.items():
                    for coro_id in coro_ids:
                        self.register_response(coro_id, None, UnknownEnvError(env_id))
        
        # get_items_range
        for env_id, get_items_range_queue_buff_coro_info in get_items_range_queue_buff.items():
            if env_id in self.db_environments:
                env_info = self.db_environments[env_id]
                for coro_id, read_queue_buff_db_info in get_items_range_queue_buff_coro_info.items():
                    coro_results: List[Tuple[NormalizedKeyType, ValueType]] = list()
                    db_id, first_desired_raw_key, last_desired_raw_key, num_items, reverse = read_queue_buff_db_info
                    if db_id in env_info.databases:
                        db = env_info.databases[db_id]
                        with env_info.env.begin(db=db) as txn:
                            result = None
                            exception = None
                            try:
                                cursor: lmdb.Cursor = txn.cursor()
                                if cursor.set_range(first_desired_raw_key):
                                    if reverse:
                                        cursor_iterator = cursor.iterprev(keys=True, values=True)
                                    else:
                                        cursor_iterator = cursor.iternext(keys=True, values=True)
                                    
                                    for raw_key, raw_value in cursor_iterator:
                                        if reverse:
                                            if raw_key < last_desired_raw_key:
                                                break
                                        else:
                                            if raw_key > last_desired_raw_key:
                                                break

                                        if (num_items is not None) and (num_items <= 0):
                                            break

                                        coro_results.append((normalize_compound_key(self.serializer.loads(raw_key)), self.serializer.loads(raw_value)))
                                        self.reads_num += 1
                                        if num_items is not None:
                                            num_items -= 1
                                else:
                                    exception = KeyError()
                            except:
                                exception = get_exception()
                            
                            self.register_response(coro_id, result, exception)
                    else:
                        self.register_response(coro_id, None, UnknownEnvDBError(env_id, db_id))
            else:
                for coro_id, read_queue_buff_db_info in get_items_range_queue_buff_coro_info.items():
                    for coro_id in coro_ids:
                        self.register_response(coro_id, None, UnknownEnvError(env_id))
        
        # sync
        if envs_need_to_be_sync:
            for env_id in envs_need_to_be_sync:
                self.sync_in_thread_pool(env_id)
            
            self.last_sync_time = perf_counter()

        self.make_dead()

    def in_work(self) -> bool:
        result: bool = (bool(self.get_first_queue) or bool(self.get_last_queue) or bool(self.get_n_items_queue) or bool(self.get_items_range_queue) or bool(self.read_queue) or bool(self.massive_read_queue) or bool(self.get_all_items_queue)) or (bool(self.force_sync) or ((not bool(self.write_locked)) and (bool(self.data_cache) or bool(self.kv_deletion_cache) or bool(self.drop_db_requests)) and ((perf_counter() - self.last_sync_time) >= self.sync_time_interval)))
        return self.thrifty_in_work(result)
    
    def time_left_before_next_event(self) -> Tuple[bool, Optional[Union[int, float]]]:
        time_since_last_sync_time: float = perf_counter() - self.last_sync_time
        if self.sync_time_interval > time_since_last_sync_time:
            return True, self.sync_time_interval - time_since_last_sync_time
        else:
            return True, 0

    def _init_db(self, db_id: DbId):
        # print(f'{self.path_to_default_db_environment=}')
        if db_id in self.db_environments:
            return self.db_environments[db_id]

        env_init_info: EnvInitInfo = EnvInitInfo(
            db_id, 
            map_size=20 * 1024**2, 
            writemap=True, 
            max_dbs=10,
            map_async=True, 
            lock=False, 
            metasync=False, 
            sync=False, 
            meminit=False,
        )
        env_info: EnvInfo = EnvInfo(env_init_info, lmdb.open(*env_init_info.args, **env_init_info.kwargs))
        db_environment = env_info.env
        self.db_environments[env_info.env_id] = env_info
        env_info.databases[self.default_db_id] = env_info.databases[None] = db_environment.open_db(self.default_db_id)
        db_environment.sync(True)

    def _init_default_db(self):
        env_info: EnvInfo = self._init_db(self.path_to_default_db_environment)
        self.db_environments[None] = env_info

    def _on_open_db_environment(self, request: DbRequest, path_to_db_environment: str) -> ServiceProcessingResponse:
        result: EnvInfo = None
        try:
            result = self._init_db(path_to_db_environment)
        except:
            exception = get_exception()
            return True, result, exception
        
        return True, result.env_id, None

    def _on_set_default_db_environment_path(self, request: DbRequest, path_to_db_environment: str) -> ServiceProcessingResponse:
        if {None, path_to_db_environment} & self.write_locked:
            return True, False, None
        
        if self.default_db_environment is None:
            self.path_to_default_db_environment = path_to_db_environment
            try:
                self._init_default_db()
            except:
                exception = get_exception()
                return True, False, exception
            return True, True, None
        else:
            return True, False, None
    
    def _on_sync(self, request: DbRequest) -> ServiceProcessingResponse:
        if self.data_cache:
            self.force_sync.add(request.env_id)
            self.make_live()
        else:
            # self.default_db_environment.sync(True)
            self.sync_in_thread_pool(request.env_id)
        
        return True, None, None
    
    def _on_get(self, request: DbRequest, key: KeyType, db_id: DbId = None) -> ServiceProcessingResponse:
        coro_id = self.current_caller_coro_info.coro_id
        key = self.serializer.dumps(normalize_compound_key(key))
        env_id = request.env_id
        db_id = request._get_db_id(db_id)
        
        if env_id in self.data_cache:
            env_cache = self.data_cache[env_id]
            if db_id in env_cache:
                db_cache = env_cache[db_id]
                if key in db_cache:
                    return True, db_cache[key], None
        
        if env_id not in self.read_queue:
            self.read_queue[env_id] = dict()
        
        read_queue_env = self.read_queue[env_id]
        if db_id not in read_queue_env:
            read_queue_env[db_id] = dict()
        
        read_queue_env_db = read_queue_env[db_id]
        if key not in read_queue_env_db:
            read_queue_env_db[key] = set()
        
        read_queue_env_db_key = read_queue_env_db[key]
        read_queue_env_db_key.add(coro_id)
        self.make_live()
        return False, None, None
    
    def _on_get_first(self, request: DbRequest, db_id: DbId = None) -> ServiceProcessingResponse:
        coro_id = self.current_caller_coro_info.coro_id
        env_id = request.env_id
        db_id = request._get_db_id(db_id)
        
        if env_id not in self.get_first_queue:
            self.get_first_queue[env_id] = dict()
        
        get_first_queue_env = self.get_first_queue[env_id]
        if db_id not in get_first_queue_env:
            get_first_queue_env[db_id] = set()
        
        get_first_queue_env_db = get_first_queue_env[db_id]
        get_first_queue_env_db.add(coro_id)
        
        self.make_live()
        return False, None, None
    
    def _on_get_last(self, request: DbRequest, db_id: DbId = None) -> ServiceProcessingResponse:
        coro_id = self.current_caller_coro_info.coro_id
        env_id = request.env_id
        db_id = request._get_db_id(db_id)
        
        if env_id not in self.get_last_queue:
            self.get_last_queue[env_id] = dict()
        
        get_last_queue_env = self.get_last_queue[env_id]
        if db_id not in get_last_queue_env:
            get_last_queue_env[db_id] = set()
        
        get_last_queue_env_db = get_last_queue_env[db_id]
        get_last_queue_env_db.add(coro_id)
        
        self.make_live()
        return False, None, None
    
    def _on_get_n_items(self, request: DbRequest, desired_key: InputKeyType, num: Optional[int] = None, db_id: DbId = None, reverse: bool = False) -> Tuple[bool, List[Tuple[NormalizedKeyType, ValueType]], Optional[Exception]]:
        coro_id = self.current_caller_coro_info.coro_id
        desired_key = self.serializer.dumps(normalize_compound_key(desired_key))
        db_id = request._get_db_id(db_id)
        env_id = request.env_id

        if env_id not in self.get_n_items_queue:
            self.get_n_items_queue[env_id] = dict()
        
        get_n_items_queue_env = self.get_n_items_queue[env_id]
        get_n_items_queue_env[coro_id] = (db_id, desired_key, num, reverse)
        self.make_live()
        return False, None, None
    
    def _on_get_items_range(self, request: DbRequest, first_desired_key: InputKeyType, last_desired_key: InputKeyType, num: Optional[int] = None, db_id: DbId = None, reverse: bool = False) -> Tuple[bool, List[Tuple[NormalizedKeyType, ValueType]], Optional[Exception]]:
        coro_id = self.current_caller_coro_info.coro_id
        first_desired_key = self.serializer.dumps(normalize_compound_key(first_desired_key))
        last_desired_key = self.serializer.dumps(normalize_compound_key(last_desired_key))
        db_id = request._get_db_id(db_id)
        env_id = request.env_id

        if env_id not in self.get_items_range_queue:
            self.get_items_range_queue[env_id] = dict()
        
        get_items_range_queue_env = self.get_items_range_queue[env_id]
        get_items_range_queue_env[coro_id] = (db_id, first_desired_key, last_desired_key, num, reverse)
        self.make_live()
        return False, None, None
    
    def _on_get_items(self, request: DbRequest, db_keys: Union[Set[InputKeyType], Dict[DbId, Set[InputKeyType]]]) -> Tuple[bool, Dict[DbId, Dict[NormalizedKeyType, Tuple[ValueType, Optional[Exception]]]], Optional[Exception]]:
        coro_id = self.current_caller_coro_info.coro_id
        env_id = request.env_id

        if env_id not in self.massive_read_queue:
            self.massive_read_queue[env_id] = dict()
        
        massive_read_queue_env = self.massive_read_queue[env_id]
        if coro_id not in massive_read_queue_env:
            massive_read_queue_env[coro_id] = dict()
        
        massive_read_queue_env_coro = massive_read_queue_env[coro_id]
        if request.db_id is not None:
            db_keys = {request.db_id: db_keys}
        
        for db_id, keys in db_keys.items():
            if db_id not in massive_read_queue_env_coro:
                massive_read_queue_env_coro[db_id] = set()
            
            massive_read_queue_env_coro_db = massive_read_queue_env_coro[db_id]
            for key in keys:
                massive_read_queue_env_coro_db.add(self.serializer.dumps(normalize_compound_key(key)))

        self.make_live()
        return False, None, None
    
    def _on_get_all_items(self, request: DbRequest, db_id: DbId) -> Tuple[bool, List[Tuple[NormalizedKeyType, ValueType]], Optional[Exception]]:
        db_id = request._get_db_id(db_id)
        coro_id = self.current_caller_coro_info.coro_id
        self.get_all_items_queue.append((coro_id, db_id, request.env_id))
        self.make_live()
        return False, None, None
    
    def _on_put(self, request: DbRequest, key: KeyType, value: Any, db_id: DbId = None) -> Tuple[bool, RawValueType, Optional[Exception]]:
        key = self.serializer.dumps(normalize_compound_key(key))
        env_id = request.env_id
        db_id = request._get_db_id(db_id)
        
        exception = None
        result = None
        try:
            if env_id not in self.data_cache:
                self.data_cache[env_id] = dict()
            
            env_data_cache = self.data_cache[env_id]
            if db_id not in env_data_cache:
                env_data_cache[db_id] = dict()
            
            env_data_cache_db = env_data_cache[db_id]
            result = env_data_cache_db[key] = self.serializer.dumps(value)
        except:
            exception = get_exception()
        
        self.make_live()
        return True, result, exception
    
    def _on_put_items(self, request: DbRequest, db_items: Dict[InputKeyType, ValueType], db_id: DbId = None) -> Tuple[bool, Dict[DbId, Dict[RawKeyType, Tuple[RawValueType, Optional[Exception]]]], Optional[Exception]]:
        result_items: Dict[DbId, Dict[RawKeyType, Tuple[RawValueType, Optional[Exception]]]] = dict()
        env_id = request.env_id
        db_id = request._get_db_id(db_id)

        if env_id not in self.data_cache:
            self.data_cache[env_id] = dict()
        
        env_data_cache = self.data_cache[env_id]
        if db_id not in result_items:
            result_items[db_id] = dict()
        
        result_db_items = result_items[db_id]
        
        if db_id not in env_data_cache:
            env_data_cache[db_id] = dict()
        
        env_data_cache_db = env_data_cache[db_id]
        for key, value in db_items.items():
            key = self.serializer.dumps(normalize_compound_key(key))
            
            exception = None
            result = None
            try:
                result = env_data_cache_db[key] = self.serializer.dumps(value)
            except:
                exception = get_exception()
            
            result_db_items[key] = (result, exception)
        
        self.make_live()
        return True, result_items, None
    
    def _on_delete(self, request: DbRequest, key: KeyType, db_id: DbId = None) -> Tuple[bool, None, Optional[Exception]]:
        key = self.serializer.dumps(normalize_compound_key(key))
        db_id = request._get_db_id(db_id)
        env_id = request.env_id
        
        exception = None
        result = None
        try:
            if env_id not in self.deletion_cache:
                self.deletion_cache[env_id] = dict()
            
            env_deletion_cache = self.deletion_cache[env_id]
            if db_id not in env_deletion_cache:
                env_deletion_cache[db_id] = set()
            
            env_deletion_cache_db = env_deletion_cache[db_id]
            env_deletion_cache_db.add(key)
        except:
            exception = get_exception()
        
        self.make_live()
        return True, result, exception
    
    def _on_delete_kv(self, request: DbRequest, key: InputKeyType, value: ValueType, db_id: DbId = None) -> Tuple[bool, RawValueType, Optional[Exception]]:
        key = self.serializer.dumps(normalize_compound_key(key))
        db_id = request._get_db_id(db_id)
        env_id = request.env_id
        
        exception = None
        result = None
        try:
            if env_id not in self.kv_deletion_cache:
                self.kv_deletion_cache[env_id] = dict()
            
            env_kv_deletion_cache = self.kv_deletion_cache[env_id]
            if db_id not in env_kv_deletion_cache:
                env_kv_deletion_cache[db_id] = dict()
            
            env_kv_deletion_cache_db = env_kv_deletion_cache[db_id]
            result = env_kv_deletion_cache_db[key] = self.serializer.dumps(value)
        except:
            exception = get_exception()
        
        self.make_live()
        return True, result, exception
    
    def _on_delete_items(self, request: DbRequest, db_items: Set[InputKeyType], db_id: DbId = None) -> Tuple[bool, Dict[DbId, Dict[RawKeyType, Optional[Exception]]], Optional[Exception]]:
        result_items: Dict[DbId, Dict[RawKeyType, Optional[Exception]]] = dict()
        env_id = request.env_id

        if env_id not in self.deletion_cache:
            self.deletion_cache[env_id] = dict()
        
        env_deletion_cache = self.deletion_cache[env_id]
        if db_id not in result_items:
            result_items[db_id] = dict()
        
        result_db_items = result_items[db_id]
        
        if db_id not in env_deletion_cache:
            env_deletion_cache[db_id] = set()
        
        env_deletion_cache_db = env_deletion_cache[db_id]
        for key in db_items:
            key = self.serializer.dumps(normalize_compound_key(key))
            
            exception = None
            try:
                env_deletion_cache_db.add(key)
            except:
                exception = get_exception()
            
            result_db_items[key] = exception

        self.make_live()
        return True, result_items, None
    
    def _on_delete_kv_items(self, request: DbRequest, db_items: Dict[InputKeyType, Tuple[ValueType]], db_id: DbId = None) -> Tuple[bool, Dict[DbId, Dict[RawKeyType, Tuple[RawValueType, Optional[Exception]]]], Optional[Exception]]:
        result_items: Dict[DbId, Dict[RawKeyType, Tuple[RawValueType, Optional[Exception]]]] = dict()
        env_id = request.env_id

        if env_id not in self.kv_deletion_cache:
            self.kv_deletion_cache[env_id] = dict()
        
        env_kv_deletion_cache = self.kv_deletion_cache[env_id]
        if db_id not in result_items:
            result_items[db_id] = dict()
        
        result_db_items = result_items[db_id]
        
        if db_id not in env_kv_deletion_cache:
            env_kv_deletion_cache[db_id] = dict()
        
        env_kv_deletion_cache_db = env_kv_deletion_cache[db_id]
        for key, value in db_items.items():
            exception = None
            result = None
            try:
                key = self.serializer.dumps(normalize_compound_key(key))
                result = env_kv_deletion_cache_db[key] = self.serializer.dumps(value)
            except:
                exception = get_exception()
            
            result_db_items[key] = (result, exception)
        
        self.make_live()
        return True, result_items, None
    
    def _on_open_databases(self, request: DbRequest, db_names: Dict[DbId, DbName]) -> ServiceProcessingResponse:
        exception = None
        try:
            env_info: EnvInfo = self.db_environments[request.env_id]
        except KeyError:
            exception = UnknownEnvError(request.env_id)
        
        for db_id, db_name in db_names.items():
            env_info.databases[db_id] = env_info.env.open_db(db_name)
            env_info.db_names[db_id] = db_name
        
        env_info.env.sync(True)
        return True, None, exception
    
    def _on_drop_db(self, request: DbRequest, db_id: DbId, delete: bool = False) -> ServiceProcessingResponse:
        coro_id = self.current_caller_coro_info.coro_id
        env_id = request.env_id

        if env_id not in self.drop_db_requests:
            self.drop_db_requests[env_id] = dict()
        
        drop_db_requests_env = self.drop_db_requests[env_id]

        if db_id not in drop_db_requests_env:
            drop_db_requests_env[db_id] = [False, set()]
        
        drop_db_requests_env_db = drop_db_requests_env[db_id]

        if delete:
            drop_db_requests_env_db[0] = delete
        
        drop_db_requests_env_db[1].add(coro_id)
        self.make_live()
        return False, None, None
    
    def sync_in_thread_pool(self, env_id: EnvId = None):
        async def sync_db_coro(i: Interface, self: 'Db', env_id: EnvId, asyncio_loop, need_to_ensure_asyncio_loop: bool):
            if need_to_ensure_asyncio_loop:
                asyncio_loop = await i(AsyncioLoop, AsyncioLoopRequest().ensure_loop(None,CoroPriority.low, True))
            else:
                if asyncio_loop is None:
                    asyncio_loop = await i(AsyncioLoop, AsyncioLoopRequest.get())
            
            async def sync_db(self: 'Db', asyncio_loop, env: lmdb.Environment):
                def sync_worker():
                    env.sync(True)
                    self.write_locked.discard(env_id)
                
                await task_in_thread_pool(asyncio_loop, sync_worker)

            env: lmdb.Environment = self.db_environments[env_id].env
            await i(AsyncioLoop, AsyncioLoopRequest.wait(sync_db(self, asyncio_loop, env)))
            self.write_locked_coro_id.discard(i.coro_id)
            def make_service_live_for_a_next_sync(self: 'Db'):
                self.make_live()
            
            await i(TimerFuncRunner, self.sync_time_interval, make_service_live_for_a_next_sync, self)

        asyncio_loop = None
        need_to_ensure_asyncio_loop = False
        try:
            asyncio_loop = self._loop.get_service_instance(AsyncioLoop).inline_get()
        except AsyncioLoopWasNotSetError:
            need_to_ensure_asyncio_loop = True

        coro: CoroWrapperBase = put_root_from_other_service(self, sync_db_coro, env_id, self, asyncio_loop, need_to_ensure_asyncio_loop)
        coro.is_background_coro = True
        self.write_locked.add(env_id)
        self.write_locked_coro_id.add(coro.coro_id)


DbRequest.default_service_type = Db


def lmdb_reapplier(env_info: EnvInfo, handler: Callable, *args, **kwargs):
    environment: lmdb.Environment = env_info.env
    databases: Dict[Hashable, Any] = env_info.databases
    failed = True
    while failed:
        need_to_resize: bool = False
        try:
            handler(environment, databases, *args, **kwargs)
            failed = False
        except DBError as err:
            if isinstance(err.original_exception, lmdb.MapFullError):
                need_to_resize = True
        
        if need_to_resize:
            environment.set_mapsize(environment.info()['map_size'] + 2 * 1024**2)
