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


__all__ = ['default_env_path_and_params', 'Db', 'DbRequest', 'KeyType', 'RawKeyType', 'ValueType', 'RawValueType', 
           'DbId', 'EnvId', 'DbName', 'DbKeyError', 'EnvInfo']

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_scheduler.versions.v_0.coro_scheduler import ServiceRequest
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
from cengal.code_flow_control.args_manager import ArgsKwargs
from cengal.text_processing.text_processing import to_identifier
from cengal.math.numbers import RationalNumber
from typing import Hashable, Tuple, List, Any, Dict, Callable, Sequence, NamedTuple, OrderedDict as OrderedDictType
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
from collections import OrderedDict, namedtuple
from functools import update_wrapper
import inspect


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


ValueInfo = NamedTuple('ValueInfo', [('value', ValueType), ('dupdata', bool), ('overwrite', bool), ('append', bool)])
VI = ValueInfo
RawValueInfo = NamedTuple('RawValueInfo', [('value', RawValueType), ('dupdata', bool), ('overwrite', bool), ('append', bool)])
RVI = RawValueInfo


default_env_path_and_params: ArgsKwargs = ArgsKwargs(
    env_path=None,
    can_be_written_externally=False,
    map_size=20 * 1024**2, 
    writemap=True, 
    max_dbs=10,
    map_async=True, 
    lock=False, 
    metasync=False, 
    sync=False, 
    meminit=False,
)


default_env_params: ArgsKwargs = ArgsKwargs(
    can_be_written_externally=False,
    map_size=20 * 1024**2, 
    writemap=True, 
    max_dbs=10,
    map_async=True, 
    lock=False, 
    metasync=False, 
    sync=False, 
    meminit=False,
)


class EnvInitInfo:
    def __init__(self, env_id: EnvId, env_path: str, can_be_written_externally: bool, *args, **kwargs):
        self.env_id: EnvId = env_id
        self.env_path: str = normpath(env_path)
        self.can_be_written_externally: bool = can_be_written_externally
        self.args: Tuple = (self.env_path,) + args
        self.kwargs: Dict = kwargs


class EnvInfo:
    db_name_prefix = '__db_name_key_16318cf6_3e16_4881_a22f_328aa41c0d4f__'
    db_name_prefix_bytes = b'__db_name_key_16318cf6_3e16_4881_a22f_328aa41c0d4f__'

    def __init__(self, init_info: EnvInitInfo, env: Optional[lmdb.Environment] = None):
        self.init_info: EnvInitInfo = init_info
        if not os.path.exists(init_info.env_path) or (os.path.exists(init_info.env_path) and not os.path.isdir(init_info.env_path)):
            os.makedirs(init_info.env_path)
        
        self.env: lmdb.Environment = lmdb.Environment(*init_info.args, **init_info.kwargs) if env is None else env
        self.env_id: EnvId = init_info.env_id
        self.databases: Dict[DbId, lmdb._Database] = dict()
        self.db_names: Dict[DbId, DbName] = dict()
        self.prepare_main_db()
    
    @staticmethod
    def gen_db_name_from_db_id(db_id: DbId) -> Union[None, bytes]:
        if db_id is None:
            return None
        
        return f'{EnvInfo.db_name_prefix}{db_id}'.encode('utf-8')
    
    def db_name_by_db_id(self, db_id: DbId) -> Union[None, bytes]:
        try:
            return self.db_names[db_id]
        except KeyError:
            raise UnknownEnvDBError(self.env_id, db_id)
    
    def db_by_db_id(self, db_id: DbId) -> lmdb._Database:
        try:
            return self.databases[db_id]
        except KeyError:
            raise UnknownEnvDBError(self.env_id, db_id)
    
    def open_db(self, db_id: DbId, *args, **kwargs) -> lmdb._Database:
            db_name: Union[None, bytes] = self.gen_db_name_from_db_id(db_id)
            new_db: lmdb._Database = self.env.open_db(db_name, *args, **kwargs)
            self.databases[db_id] = new_db
            self.db_names[db_id] = db_name
            return new_db
    
    def prepare_main_db(self) -> lmdb._Database:
        self.open_db(None)
    
    def close(self):
        self.env.close()


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


class DefaultDbEnvironmentCanNotBeClosedManualyError(Exception):
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
    def __init__(self, env_id: EnvId = None, db_id: DbId = None, needs_sync: bool = False, can_wait: bool = False):
        super().__init__()
        self.env_id: EnvId = env_id
        self.db_id: DbId = db_id
        self.needs_sync: bool = needs_sync
        self.provide_to_request_handler = True
        self.can_wait: bool = can_wait  # TODO: implement. If True then request can wait for a next iteration in attempt to create a bunch of requests. If False then request will be processed immediately.
    
    def _copy(self) -> 'DbRequest':
        return DbRequest(self.env_id, self.db_id, self.needs_sync)
    
    def set_root_path_to_db_environments(self, root_path_to_db_environments: str) -> bool:
        return self._save_to_copy(0, root_path_to_db_environments)
    
    def open_databases(self, db_ids: Set[DbId], *args, **kwargs) -> None:
        return self._save_to_copy(1, db_ids, *args, **kwargs)
    
    def drop_db(self, db_id: DbId, delete: bool = False) -> None:
        return self._save_to_copy(2, db_id, delete)
    
    def sync(self) -> None:
        return self._save_to_copy(3)
    
    def wait_sync(self) -> None:  # TODO: implement
        return self._save_to_copy(22)
    
    def set_sync_timeout(self, timeout: RationalNumber) -> None:  # TODO: implement
        return self._save_to_copy(23, timeout)
    
    def get(self, key: InputKeyType) -> ValueType:
        return self._save_to_copy(4, key)
    
    def get_first(self) -> Tuple[NormalizedKeyType, ValueType]:
        # Returns first item in DB
        return self._save_to_copy(14)
    
    def get_last(self) -> Tuple[NormalizedKeyType, ValueType]:
        # Returns last item in DB
        return self._save_to_copy(15)
    
    def get_items(self, db_keys: Sequence[InputKeyType]) -> OrderedDictType[NormalizedKeyType, Tuple[ValueType, Optional[Exception]]]:
        return self._save_to_copy(5, db_keys)
    
    def get_n_items(self, desired_key: InputKeyType, num: Optional[int] = None) -> OrderedDictType[NormalizedKeyType, Tuple[ValueType, Optional[Exception]]]:
        return self._save_to_copy(16, desired_key, num, reverse=False)
    
    def get_reverse_n_items(self, desired_key: InputKeyType, num: Optional[int] = None) -> OrderedDictType[NormalizedKeyType, Tuple[ValueType, Optional[Exception]]]:
        return self._save_to_copy(16, desired_key, num, reverse=True)
    
    def get_items_range(self, first_desired_key: InputKeyType, last_desired_key: InputKeyType, num: Optional[int] = None) -> OrderedDictType[NormalizedKeyType, Tuple[ValueType, Optional[Exception]]]:
        return self._save_to_copy(17, first_desired_key, last_desired_key, num, reverse=False)
    
    def get_reverse_items_range(self, first_desired_key: InputKeyType, last_desired_key: InputKeyType, num: Optional[int] = None) -> OrderedDictType[NormalizedKeyType, Tuple[ValueType, Optional[Exception]]]:
        return self._save_to_copy(17, first_desired_key, last_desired_key, num, reverse=True)
    
    def get_all_items(self) -> OrderedDictType[NormalizedKeyType, Tuple[ValueType, Optional[Exception]]]:
        # Returns all items from DB
        return self._save_to_copy(6)
    
    def pop(self, key: InputKeyType) -> ValueType:  # TODO: implement
        return self._save_to_copy(24, key)
    
    def pop_items(self, db_keys: Sequence[InputKeyType]) -> OrderedDictType[NormalizedKeyType, Tuple[ValueType, Optional[Exception]]]:  # TODO: implement
        return self._save_to_copy(25, db_keys)
    
    def put(self, key: InputKeyType, value: Optional[Union[ValueType, ValueInfo]] = None) -> RawValueType:
        return self._save_to_copy(7, key, value)
    
    def put_items(self, db_items: Dict[InputKeyType, Union[ValueType, ValueInfo]]) -> Dict[DbId, Dict[RawKeyType, Tuple[RawValueType, Optional[Exception]]]]:
        return self._save_to_copy(8, db_items)
    
    def increment(self, key: InputKeyType, value: RationalNumber = 1) -> RationalNumber:  # TODO: implement
        return self._save_to_copy(19, key, value)
    
    inc = increment
    
    def increment_items(self, db_items: Dict[InputKeyType, Union[RationalNumber, ValueInfo]]) -> OrderedDictType[NormalizedKeyType, Tuple[RationalNumber, Optional[Exception]]]:  # TODO: implement
        return self._save_to_copy(8, db_items)
    
    inc_items = increment_items
    
    def replace(self, key: InputKeyType, value: Optional[Union[ValueType, ValueInfo]] = None) -> Tuple[RawValueType, ValueType]:  # TODO: implement
        return self._save_to_copy(20, key, value)
    
    def replace_items(self, db_items: Dict[InputKeyType, Union[ValueType, ValueInfo]]) -> Dict[DbId, Dict[RawKeyType, Tuple[RawValueType, ValueType, Optional[Exception]]]]:  # TODO: implement
        return self._save_to_copy(21, db_items)
    
    def delete(self, key: InputKeyType) -> RawValueType:  # TODO: finish an implementation
        return self._save_to_copy(9, key)
    
    def delete_kv(self, key: InputKeyType, value: ValueType) -> RawValueType:  # TODO: finish an implementation
        return self._save_to_copy(10, key, value)
    
    def delete_items(self, db_items: Set[InputKeyType]) -> Dict[DbId, Dict[RawKeyType, Tuple[RawValueType, Optional[Exception]]]]:  # TODO: finish an implementation
        return self._save_to_copy(11, db_items)
    
    def delete_kv_items(self, db_items: Dict[InputKeyType, Tuple[ValueType]]) -> Dict[DbId, Dict[RawKeyType, Tuple[RawValueType, Optional[Exception]]]]:  # TODO: finish an implementation
        return self._save_to_copy(12, db_items)
    
    def execute_in_transaction(self, env_id: EnvId, callable_or_coro: Union[Callable, AnyWorker]) -> None:  # TODO: implement
        # Will execute given callable or coroutine in transaction (after all other queues will be processed)
        # It will run in current thread. So, it will block current thread until it will be finished if it is not a coroutine.
        # On the other hand it will lock environment and all databases in it until coroutine will be finished.
        return self._save_to_copy(29, env_id, callable_or_coro)

    def open_db_environment(self, env_id: EnvId, env_path: Union[None, str], can_be_written_externally: bool, *args, **kwargs) -> EnvId:
        return self._save_to_copy(13, env_id, env_path, can_be_written_externally, *args, **kwargs)
    
    def close_db_environment(self, env_id: EnvId) -> None:
        return self._save_to_copy(18, env_id)
    
    def lock_databases(self, db_names: Optional[Set[DbId]] = None) -> None:  # TODO: implement
        # Lock all databases if db_names is None. Databases will be released automatically wnen coroutine execution will be finished
        return self._save_to_copy(26, db_names)
    
    def try_lock_databases(self, db_names: Optional[Set[DbId]] = None) -> bool:  # TODO: implement
        # Tries to lock all databases if db_names is None. Returns True if try was successfull. False otherwise. Databases will be released automatically wnen coroutine execution will be finished
        return self._save_to_copy(27, db_names)
    
    def unlock_databases(self, db_names: Optional[Set[DbId]] = None) -> None:  # TODO: implement
        # Unlock all databases if db_names is None
        return self._save_to_copy(28, db_names)


# class TransactionContextManager(DbRequest):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._journal_db_id: DbName = b'__journal__'
#         self._transaction: Optional[lmdb.Transaction] = None
#         self._transaction_context_manager: Optional[lmdb.Transaction] = None
#         self._transaction_history: List[DbRequest] = list()
#         self._committed: bool = False

#     @staticmethod
#     def from_request(request: DbRequest) -> 'TransactionContextManager':
#         return TransactionContextManager(request.env_id, request.db_id)
    
#     def to_request(self) -> DbRequest:
#         return DbRequest(self.env_id, self.db_id)
    
#     @staticmethod
#     def request_to_data(request: DbRequest) -> Dict:
#         result = dict()
#         result['env_id'] = request.env_id
#         result['db_id'] = request.db_id
#         result['needs_sync'] = request.needs_sync
#         result['request_type'] = request.request_type
#         result['args'] = request.args
#         result['kwargs'] = request.kwargs
#         result['provide_to_request_handler'] = request.provide_to_request_handler
#         return result
    
#     @staticmethod
#     def request_from_data(data: Dict) -> DbRequest:
#         request = DbRequest(data['env_id'], data['db_id'], data['needs_sync'])
#         request.request_type = data['request_type']
#         request.args = data['args']
#         request.kwargs = data['kwargs']
#         request.provide_to_request_handler = data['provide_to_request_handler']
#         return request
    
#     async def _commit(self):
#         i: Interface = current_interface()
#         try:
#             await i(DbRequest(self.env_id, self._journal_db_id, True).lock_databases({self._journal_db_id}))
#             last_committed_id: int = await i(DbRequest(self.env_id, self._journal_db_id, True).get(1))
#             last_id: int = await i(DbRequest(self.env_id, self._journal_db_id, True).get(0))
#             our_id = last_id
#             for request in self._transaction_history:
#                 our_id += 1
#                 await i(DbRequest(self.env_id, self._journal_db_id, True).put(our_id, TransactionContextManager.request_to_data(request)))

#             last_id: int = await i(DbRequest(self.env_id, self._journal_db_id, True).replace(0, our_id))
#             for request in self._transaction_history:
#                 await i(request)
#         except:
#             ...
#         finally:
#             await i(DbRequest(self.env_id, self._journal_db_id, True).unlock_databases({self._journal_db_id}))
    
#     def _save_to_copy(self, __request__type__: int, *args, **kwargs) -> ServiceRequest:
#         request: DbRequest = super()._save_to_copy(__request__type__, *args, **kwargs)
#         self._transaction_history.append(request)
#         return request
    
#     def __enter__(self) -> 'TransactionContextManager':
#         self._transaction = self.env.begin(write=True)
#         self._transaction_context_manager = self._transaction.__enter__()
#         return self
    
#     def __exit__(self, exc_type, exc_val, exc_tb) -> None:
#         self._transaction_context_manager.__exit__(exc_type, exc_val, exc_tb)
#         self._transaction = None
#         self._transaction_context_manager = None
    
#     async def __aenter__(self) -> 'TransactionContextManager':
#         i: Interface = current_interface()
#         db_service: Db = i._loop.get_service_instance(Db)
#         if self.env_id not in db_service.db_environments:
#             raise UnknownEnvError(self.env_id)
        
#         env_info: EnvInfo = self.db_environments[self.env_id]
#         if self._journal_db_id not in env_info.databases:
#             await i(self.to_request().open_databases({self._journal_db_id}))

#         return self
    
#     async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
#         if (exc_type is None) and (exc_val is None) and (exc_tb is None):
#             await self._commit()


def check_request(method: Callable):
    def wrapper(self: 'Db', request: DbRequest, *args, **kwargs) -> ServiceProcessingResponse:
        if request.env_id not in self.db_environments:
            return True, None, UnknownEnvError(request.env_id)
        
        if request.db_id not in self.db_environments[request.env_id].databases:
            return True, None, UnknownEnvDBError(request.env_id, request.db_id)
        
        return method(self, request, *args, **kwargs)
    
    original_func_sign: inspect.Signature = inspect.signature(method)
    update_wrapper(wrapper, method)
    wrapper.__signature__ = original_func_sign.replace(parameters=tuple(original_func_sign.parameters.values()), return_annotation=original_func_sign.return_annotation)
    return wrapper
    

class Db(Service, EntityStatsMixin):
    def __init__(self, loop: CoroScheduler):
        super(Db, self).__init__(loop)
        self.default_env_name: str = '__default__.dbenv'
        self.default_envs_dir: str = 'db_envs'
        # self.drop_db_requests: Dict[CoroID, Tuple[Hashable, bool]] = dict()
        # self.drop_db_requests: Dict[EnvId, Dict[CoroID, Tuple[DbId, bool]]] = dict()
        self.drop_db_requests: Dict[EnvId, Dict[DbId, Tuple[bool, Set[CoroID]]]] = dict()
        # self.read_queue: List[Tuple[CoroID, Tuple[RawKeyType, DbId]]] = list()
        self.read_queue: Dict[EnvId, Dict[DbId, Dict[RawKeyType, Set[CoroID]]]] = dict()
        self.massive_read_queue: Dict[EnvId, Dict[CoroID, Dict[DbId, List[RawKeyType]]]] = dict()
        # self.massive_read_queue: List[Tuple[CoroID, Set[Tuple[KeyType, DbId]]]] = list()
        self.put_queue: Dict[EnvId, Dict[DbId, Dict[RawKeyType, List[Union[RawValueType, RawValueInfo]]]]] = dict()
        self.data_cache: Dict[EnvId, Dict[DbId, Dict[RawKeyType, List[Union[RawValueType, RawValueInfo]]]]] = dict()
        # self.data_cache: Dict[EnvId, Dict[Tuple[RawKeyType, DbId], RawValueType]] = dict()
        self.max_data_cache_size: Union[None, int] = 10000
        self.deletion_cache: Dict[EnvId, Dict[DbId, Set[RawKeyType]]] = dict()
        self.kv_deletion_cache: Dict[EnvId, Dict[DbId, Dict[RawKeyType, List[RawValueType]]]] = dict()
        # self.kv_deletion_cache: Dict[Tuple[Hashable, Hashable], Any] = dict()
        self.get_first_queue: Dict[EnvId, Dict[DbId, Set[CoroID]]] = dict()
        self.get_last_queue: Dict[EnvId, Dict[DbId, Set[CoroID]]] = dict()
        self.get_n_items_queue: Dict[EnvId, Dict[CoroID, Tuple[DbId, RawKeyType, int, bool]]] = dict()
        self.get_items_range_queue: Dict[EnvId, Dict[CoroID, Tuple[DbId, RawKeyType, RawKeyType, int, bool]]] = dict()
        # self.get_all_items_queue: List[Tuple[CoroID, DbId, EnvId]] = list()
        self.get_all_items_queue: Dict[EnvId, List[Tuple[CoroID, DbId]]] = dict()
        self.open_db_environment_requests: Dict[CoroID, Tuple[EnvId, Union[None, str], bool, Tuple, Dict]] = dict()
        self.root_path_to_db_environments_rel: RelativePath = None
        self.app_name_waiter: CoroWrapperBase = None
        self.default_db_environment: lmdb.Environment = None
        self.db_environments: Dict[EnvId, EnvInfo] = dict()
        # self.databases: Dict[Hashable, Any] = dict()
        # self.db_names: Dict[DbId, DbName] = dict()
        self.async_loop = None
        self.sync_time_interval = 1.0
        self.last_sync_time = perf_counter()
        self.envs_need_to_be_sync: Set[DbId] = set()
        self.envs_in_sync: Set[DbId] = set()
        self.force_sync: Set[EnvId] = set()
        self.sync_an_each_write: bool = False
        self.write_locked: Set[EnvId] = set()
        self.writes_num: int = 0
        self.reads_num: int = 0
        self.deletes_num: int = 0
        self.db_drops_num: int = 0
        self.write_locked_coro_id: Set[CoroID] = set()
        self.wake_up_handle_registered: bool = False
        # self.serializer = best_serializer({
        #                                     DataFormats.binary,
        #                                     DataFormats.messagepack,
        #                                     Tags.can_use_bytes,
        #                                     Tags.decode_str_as_str,
        #                                     Tags.decode_list_as_list,
        #                                     Tags.decode_bytes_as_bytes,
        #                                     Tags.superficial,
        #                                     Tags.current_platform,
        #                                     Tags.multi_platform,
        #                                 },
        #                                 test_data_factory(TestDataType.small),
        #                                 0.1)
        self.serializer = Serializer(Serializers.msgspec_messagepack)
        self._request_workers = {
            0: self._on_set_root_path_to_db_environments,
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
            18: self._on_close_db_environment,
        }

    # TODO: sync with last implementation
    def get_entity_stats(self, stats_level: 'EntityStatsMixin.StatsLevel' = EntityStatsMixin.StatsLevel.debug) -> Tuple[str, Dict[str, Any]]:
        return type(self).__name__, {
            'db_env_ids': list(self.db_environments.keys()),
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

    def destroy(self):
        # TODO: we need to use some loop destroy service in order to put our coro which will write all pending queues,
        # sync envirounments and close them. Also we need to prevent new requests from being processed.
        db_environments_values = self.db_environments.values()
        self.db_environments = type(self.db_environments)()
        self.default_db_environment = None
        for env_info in db_environments_values:
            env_info.close()

    def single_task_registration_or_immediate_processing(
            self, *args, **kwargs) -> ServiceProcessingResponse:
        result = self.try_resolve_request(*args, **kwargs)
        if result is None:
            self._ensure_default_db_environment()
            return True, None, None
        else:
            return result

    def _ensure_default_db_environment(self) -> bool:
        if self.default_db_environment is None:
            if self.root_path_to_db_environments_rel is None:
                if self.app_name_waiter is None:
                    async def coro(i: Interface, self: 'Db'):
                        app_name_for_fs = await i(InstanceRequest().wait('app_name_for_fs'))
                        app_data_dir_path_type: AppDirectoryType = await i(InstanceRequest().wait('app_data_dir_path_type'))
                        app_dir_path: AppDirPath = await i(InstanceRequest().wait(AppDirPath))
                        app_data_dir_path: str = app_dir_path.cached(app_data_dir_path_type, app_name_for_fs)
                        self.root_path_to_db_environments_rel = RelativePath(RelativePath(app_data_dir_path)(self.default_envs_dir))
                        self._init_default_db_env()
                        self.app_name_waiter = None
                        self.make_live()
                    
                    self.app_name_waiter = put_root_from_other_service(self, coro, self)
                    # self.app_name_waiter.is_background_coro = True
                
                self.make_dead()
                return False
            else:
                self._init_default_db_env()
                return True
        else:
            return True

    def full_processing_iteration(self):
        # TODO: combine all queues into one single transaction by env_id. Or at most two transactions: read and write.
        # This will improve performance and will give ability to move transations to other threads or even processess if needed.

        # TODO: since DB can not handle big number of transactions per secons, it is better to combine all requests and process 
        # them at most as once a milisecond (it is frequently engough).

        if not self._ensure_default_db_environment():
            return
        
        if self.force_sync:
            self.envs_need_to_be_sync |= self.force_sync
            self.force_sync = set()
        
        put_queue_buff = self.put_queue
        self.put_queue = type(put_queue_buff)()
        
        data_cache_buff = self.data_cache  # will be cleared at the end of the iteration if necessary
        
        read_queue_buff = self.read_queue
        self.read_queue = type(read_queue_buff)()
        
        massive_read_queue_buff = self.massive_read_queue
        self.massive_read_queue = type(massive_read_queue_buff)()
        
        deletion_cache_buff = self.deletion_cache
        self.deletion_cache = type(deletion_cache_buff)()
        
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

        open_db_environment_requests_buff: Dict[CoroID, Tuple[EnvId, Union[None, str], bool, Tuple, Dict]] = self.open_db_environment_requests
        self.open_db_environment_requests = type(open_db_environment_requests_buff)()

        # open_db_environment
        for coro_id, request_info in open_db_environment_requests_buff.items():
            env_id, env_path, can_be_written_externally, args, kwargs = request_info
            if env_id in self.db_environments:
                self.register_response(coro_id, self.db_environments[env_id])
            else:
                exception = None
                try:
                    result = self._init_db_env(env_id, env_path, can_be_written_externally, *args, **kwargs)
                except:
                    exception = get_exception()

                self.register_response(coro_id, result, exception)

        # put
        def put_handler(env_info: EnvInfo, put_info: Dict[DbId, Dict[RawKeyType, List[Union[RawValueType, RawValueInfo]]]]):
            try:
                with env_info.env.begin(write=True) as txn:
                    for db_id, db_put_info in put_info.items():
                        if db_id in env_info.databases:
                            for raw_key, values in db_put_info.items():
                                for value in values:
                                    if isinstance(value, RawValueInfo):
                                        value, dupdata, overwrite, append = value
                                    else:
                                        dupdata, overwrite, append = True, True, False
                                    
                                    txn.put(raw_key, value, db=env_info.databases[db_id], dupdata=dupdata, overwrite=overwrite, append=append)
                        
                        self.writes_num += len(db_put_info)
            except lmdb.MapFullError:
                raise DBError.from_exception(db_id)
        
        for env_id, put_info in put_queue_buff.items():
            if env_id in self.db_environments:
                self.envs_need_to_be_sync.add(env_id)
                lmdb_reapplier(self.db_environments[env_id], put_handler, put_info)
        
        # TODO: implement replace* methods processing

        # delete
        for env_id, deletion_cache_buff_db_info in deletion_cache_buff.items():
            if env_id in self.db_environments:
                env_info = self.db_environments[env_id]
                self.envs_need_to_be_sync.add(env_id)
                with env_info.env.begin(write=True) as txn:
                    for db_id, del_keys in deletion_cache_buff_db_info.items():
                        if db_id in env_info.databases:
                            for del_raw_key in del_keys:
                                txn.delete(del_raw_key, db=env_info.databases[db_id])
                                self.deletes_num += 1
                                try:
                                    data_cache_buff[env_id][db_id].pop(del_raw_key, None)
                                except KeyError:
                                    pass

        # delete_kv
        for env_id, kv_deletion_cache_buff_db_info in kv_deletion_cache_buff.items():
            if env_id in self.db_environments:
                env_info = self.db_environments[env_id]
                self.envs_need_to_be_sync.add(env_id)
                with env_info.env.begin(write=True) as txn:
                    for db_id, del_keys in kv_deletion_cache_buff_db_info.items():
                        if db_id in env_info.databases:
                            for del_raw_key, del_raw_values in del_keys.items():
                                for del_raw_value in del_raw_values:
                                    txn.delete(del_raw_key, del_raw_value, db=env_info.databases[db_id])
                                    self.deletes_num += 1
                                    try:
                                        raw_values: List[Union[RawValueType, RawValueInfo]] = data_cache_buff[env_id][db_id][del_raw_key]
                                        new_raw_values: List[Union[RawValueType, RawValueInfo]] = list()
                                        for raw_value in raw_values:
                                            raw_value_original = raw_value
                                            if isinstance(raw_value, RawValueInfo):
                                                raw_value, _, _, _ = raw_value
                                            
                                            if raw_value != del_raw_value:
                                                new_raw_values.append(raw_value_original)
                                            
                                        if new_raw_values:
                                            data_cache_buff[env_id][db_id][del_raw_key] = new_raw_values
                                        else:
                                            data_cache_buff[env_id][db_id].pop(del_raw_key, None)
                                    except KeyError:
                                        pass

        # drop
        drop_db_requests_buff = self.drop_db_requests
        self.drop_db_requests = type(drop_db_requests_buff)()
        
        def drop_handler(env_info: EnvInfo, drop_info: Dict[DbId, Tuple[bool, Set[CoroID]]]):
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
                self.envs_need_to_be_sync.add(env_id)
                lmdb_reapplier(self.db_environments[env_id], drop_handler, drop_info)
            else:
                for db_id, db_drop_info in drop_info.items():
                    delete_db, coro_id = db_drop_info
                    self.register_response(coro_id, None, UnknownEnvError(env_id))

        # get
        def get_item(txn, key_info: Tuple[RawKeyType, DbId, EnvId], data_cache_buff: Dict[EnvId, Dict[DbId, Dict[RawKeyType, List[Union[RawValueType, RawValueInfo]]]]]) -> Tuple[ValueType, Optional[Exception]]:
            key, db_id, env_id = key_info
            need_to_get_from_db = True
            try:
                values = data_cache_buff[env_id][db_id][key]
                if values:
                    value = values[0]
                    if isinstance(value, RawValueInfo):
                        value, _, _, _ = value

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
                            coro_results[db_id] = OrderedDict()
                        
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
            if coro_results:
                db_id = tuple(coro_results.keys())[0]
                self.register_response(coro_id, coro_results[db_id], None)
            else:
                self.register_response(coro_id, OrderedDict(), None)

        # get all items
        for env_id, requests_info in get_all_items_queue_buff.items():
            for request_info in requests_info:
                coro_id, db_id = request_info
                if env_id in self.db_environments:
                    env_info = self.db_environments[env_id]
                    env = env_info.env
                    if db_id in env_info.databases:
                        db = env_info.databases[db_id]
                        with env.begin(db=db) as txn:
                            result = list()
                            exception = None
                            try:
                                result = [(normalize_compound_key(self.serializer.loads(k)), self.serializer.loads(v)) for k, v in txn.cursor() if not k.startswith(EnvInfo.db_name_prefix_bytes)]
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
                                    key = cursor.key()
                                    key_found: bool = True
                                    while key.startswith(EnvInfo.db_name_prefix_bytes):
                                        key_found = cursor.next_nodup()
                                        if not key_found:
                                            break

                                        key = cursor.key()

                                    if key_found:
                                        value = cursor.value()
                                        result = (normalize_compound_key(self.serializer.loads(cursor.key())), self.serializer.loads(cursor.value()))
                                        self.reads_num += 1
                                    else:
                                        exception = KeyError()
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
                                if cursor.last():
                                    key: bytes = cursor.key()
                                    key_found: bool = True
                                    key = cursor.key()
                                    while key.startswith(EnvInfo.db_name_prefix_bytes):
                                        key_found = cursor.prev_nodup()
                                        if not key_found:
                                            break

                                        key = cursor.key()

                                    if key_found:
                                        value: bytes = cursor.value()
                                        result = (normalize_compound_key(self.serializer.loads(cursor.key())), self.serializer.loads(cursor.value()))
                                        self.reads_num += 1
                                    else:
                                        exception = KeyError()
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
                            exception = None
                            try:
                                cursor: lmdb.Cursor = txn.cursor()
                                if cursor.set_range(first_desired_raw_key):
                                    if reverse:
                                        cursor_iterator = cursor.iterprev(keys=True, values=True)
                                    else:
                                        cursor_iterator = cursor.iternext(keys=True, values=True)
                                    
                                    for raw_key, raw_value in cursor_iterator:
                                        if raw_key.startswith(EnvInfo.db_name_prefix_bytes):
                                            continue

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
                            
                            self.register_response(coro_id, coro_results, exception)
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
                            exception = None
                            try:
                                cursor: lmdb.Cursor = txn.cursor()
                                if cursor.set_range(first_desired_raw_key):
                                    if reverse:
                                        cursor_iterator = cursor.iterprev(keys=True, values=True)
                                    else:
                                        cursor_iterator = cursor.iternext(keys=True, values=True)
                                    
                                    for raw_key, raw_value in cursor_iterator:
                                        if raw_key.startswith(EnvInfo.db_name_prefix_bytes):
                                            continue
                                        
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
                            
                            self.register_response(coro_id, coro_results, exception)
                    else:
                        self.register_response(coro_id, None, UnknownEnvDBError(env_id, db_id))
            else:
                for coro_id, read_queue_buff_db_info in get_items_range_queue_buff_coro_info.items():
                    for coro_id in coro_ids:
                        self.register_response(coro_id, None, UnknownEnvError(env_id))
        
        need_to_sync = self.sync_an_each_write

        # periodic sync
        if (perf_counter() - self.last_sync_time) >= self.sync_time_interval:
            for env_id, env_info in self.db_environments.items():
                self.envs_need_to_be_sync.add(env_id)
                need_to_sync = True

        # sync
        if need_to_sync and self.envs_need_to_be_sync:
            envs_need_to_be_sync_bak = self.envs_need_to_be_sync - self.envs_in_sync
            self.envs_need_to_be_sync = set(self.envs_in_sync)
            for env_id in envs_need_to_be_sync_bak:
                self.sync_in_thread_pool(env_id)
            
            self.last_sync_time = perf_counter()
        
        # invalidate data_cache for envs that can be written externally
        for env_id, env_info in self.db_environments.items():
            if env_info.init_info.can_be_written_externally:
                self.data_cache.pop(env_id, None)
        
        # clear too big caches
        for env_id, env_info in self.db_environments.items():
            if env_id in self.data_cache:
                if len(self.data_cache[env_id]) > self.max_data_cache_size:
                    del self.data_cache[env_id]

        self.make_dead()

    def in_work(self) -> bool:
        result: bool = bool(self.default_db_environment is None) \
                            or bool(self.open_db_environment_requests) \
                            or bool(self.get_first_queue) \
                            or bool(self.get_last_queue) \
                            or bool(self.get_n_items_queue) \
                            or bool(self.get_items_range_queue) \
                            or bool(self.read_queue) \
                            or bool(self.massive_read_queue) \
                            or bool(self.get_all_items_queue)\
                            or bool(self.force_sync) \
                            or bool(self.deletion_cache) \
                            or bool(self.kv_deletion_cache) \
                            or bool(self.drop_db_requests) \
                            or bool(self.put_queue) \
                            or bool(self.envs_need_to_be_sync) \
                            or ((perf_counter() - self.last_sync_time) >= self.sync_time_interval)
        return self.thrifty_in_work(result)
    
    def time_left_before_next_event(self) -> Tuple[bool, Optional[Union[int, float]]]:
        time_since_last_sync_time: float = perf_counter() - self.last_sync_time
        if self.sync_time_interval > time_since_last_sync_time:
            return True, self.sync_time_interval - time_since_last_sync_time
        else:
            return True, 0

    def _init_db_env(self, env_id: EnvId, env_path: Union[None, str], can_be_written_externally: bool, *args, **kwargs) -> EnvInfo:
        if env_id in self.db_environments:
            return self.db_environments[env_id]

        if env_path is None:
            if env_id is None:
                env_path = self.root_path_to_db_environments_rel(self.default_env_name)
            else:
                env_path = self.root_path_to_db_environments_rel(to_identifier(f'{env_id}'))
        else:
            if os.path.isabs(env_path):
                env_path = os.path.normpath(env_path)
            else:
                env_path = self.root_path_to_db_environments_rel(env_path)

        env_init_info: EnvInitInfo = EnvInitInfo(
            env_id, 
            env_path, 
            can_be_written_externally, 
            *args, **kwargs
        )
        env_info: EnvInfo = EnvInfo(env_init_info)
        self.db_environments[env_info.env_id] = env_info
        env_info.env.sync(True)
        return env_info

    def _init_default_db_env(self):
        args, kwargs = default_env_path_and_params()
        env_info: EnvInfo = self._init_db_env(None, *args, **kwargs)
        self.default_db_environment = env_info

    def _on_open_db_environment(self, request: DbRequest, env_id: EnvId, env_path: Union[None, str], can_be_written_externally: bool, *args, **kwargs) -> Tuple[bool, EnvInfo, Exception]:
        self.open_db_environment_requests[self.current_caller_coro_info.coro_id] = (env_id, env_path, can_be_written_externally, args, kwargs)
        self.make_live()
        return False, None, None
    
    @check_request
    def _on_close_db_environment(self, request: DbRequest):
        env_id: EnvId = request.env_id
        
        if env_id is None:
            return True, False, DefaultDbEnvironmentCanNotBeClosedManualyError()
        
        if env_id in self.db_environments:
            self.db_environments[env_id].close()
            del self.db_environments[env_id]
            return True, True, None
        else:
            return True, False, UnknownEnvError(env_id)

    def _on_set_root_path_to_db_environments(self, request: DbRequest, root_path_to_db_environments: str) -> ServiceProcessingResponse:
        self.root_path_to_db_environments_rel = RelativePath(root_path_to_db_environments)
        return True, True, None
    
    @check_request
    def _on_sync(self, request: DbRequest) -> ServiceProcessingResponse:
        if self.put_queue:
            self.force_sync.add(request.env_id)
            self.make_live()
        else:
            # self.default_db_environment.sync(True)
            self.sync_in_thread_pool(request.env_id)
        
        return True, None, None
    
    @check_request
    def _on_get(self, request: DbRequest, key: KeyType) -> ServiceProcessingResponse:
        coro_id = self.current_caller_coro_info.coro_id
        key = self.serializer.dumps(normalize_compound_key(key))
        db_id = request.db_id
        env_id = request.env_id
        
        if env_id in self.data_cache:
            env_cache = self.data_cache[env_id]
            if db_id in env_cache:
                db_cache = env_cache[db_id]
                if key in db_cache:
                    values = db_cache[key]
                    if values:
                        value = values[0]
                        if isinstance(value, RawValueInfo):
                            value, _, _, _ = value
                        
                        value = self.serializer.loads(value)
                        return True, value, None
        
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
    
    @check_request
    def _on_get_first(self, request: DbRequest) -> ServiceProcessingResponse:
        coro_id = self.current_caller_coro_info.coro_id
        db_id = request.db_id
        env_id = request.env_id
        
        if env_id not in self.get_first_queue:
            self.get_first_queue[env_id] = dict()
        
        get_first_queue_env = self.get_first_queue[env_id]
        if db_id not in get_first_queue_env:
            get_first_queue_env[db_id] = set()
        
        get_first_queue_env_db = get_first_queue_env[db_id]
        get_first_queue_env_db.add(coro_id)
        
        self.make_live()
        return False, None, None
    
    @check_request
    def _on_get_last(self, request: DbRequest) -> ServiceProcessingResponse:
        coro_id = self.current_caller_coro_info.coro_id
        db_id = request.db_id
        env_id = request.env_id
        
        if env_id not in self.get_last_queue:
            self.get_last_queue[env_id] = dict()
        
        get_last_queue_env = self.get_last_queue[env_id]
        if db_id not in get_last_queue_env:
            get_last_queue_env[db_id] = set()
        
        get_last_queue_env_db = get_last_queue_env[db_id]
        get_last_queue_env_db.add(coro_id)
        
        self.make_live()
        return False, None, None
    
    @check_request
    def _on_get_n_items(self, request: DbRequest, desired_key: InputKeyType, num: Optional[int] = None, reverse: bool = False) -> Tuple[bool, List[Tuple[NormalizedKeyType, ValueType]], Optional[Exception]]:
        coro_id = self.current_caller_coro_info.coro_id
        desired_key = self.serializer.dumps(normalize_compound_key(desired_key))
        db_id = request.db_id
        env_id = request.env_id

        if env_id not in self.get_n_items_queue:
            self.get_n_items_queue[env_id] = dict()
        
        get_n_items_queue_env = self.get_n_items_queue[env_id]
        get_n_items_queue_env[coro_id] = (db_id, desired_key, num, reverse)
        self.make_live()
        return False, None, None
    
    @check_request
    def _on_get_items_range(self, request: DbRequest, first_desired_key: InputKeyType, last_desired_key: InputKeyType, num: Optional[int] = None, reverse: bool = False) -> Tuple[bool, List[Tuple[NormalizedKeyType, ValueType]], Optional[Exception]]:
        coro_id = self.current_caller_coro_info.coro_id
        first_desired_key = self.serializer.dumps(normalize_compound_key(first_desired_key))
        last_desired_key = self.serializer.dumps(normalize_compound_key(last_desired_key))
        db_id = request.db_id
        env_id = request.env_id

        if env_id not in self.get_items_range_queue:
            self.get_items_range_queue[env_id] = dict()
        
        get_items_range_queue_env = self.get_items_range_queue[env_id]
        get_items_range_queue_env[coro_id] = (db_id, first_desired_key, last_desired_key, num, reverse)
        self.make_live()
        return False, None, None
    
    @check_request
    def _on_get_items(self, request: DbRequest, db_keys: Sequence[InputKeyType]) -> Tuple[bool, Dict[DbId, Dict[NormalizedKeyType, Tuple[ValueType, Optional[Exception]]]], Optional[Exception]]:
        coro_id = self.current_caller_coro_info.coro_id
        db_id = request.db_id
        env_id = request.env_id

        if env_id not in self.massive_read_queue:
            self.massive_read_queue[env_id] = dict()
        
        massive_read_queue_env = self.massive_read_queue[env_id]
        if coro_id not in massive_read_queue_env:
            massive_read_queue_env[coro_id] = dict()
        
        massive_read_queue_env_coro = massive_read_queue_env[coro_id]
        if db_id not in massive_read_queue_env_coro:
            massive_read_queue_env_coro[db_id] = list()
        
        massive_read_queue_env_coro_db = massive_read_queue_env_coro[db_id]
        for key in db_keys:
            massive_read_queue_env_coro_db.append(self.serializer.dumps(normalize_compound_key(key)))

        self.make_live()
        return False, None, None
    
    @check_request
    def _on_get_all_items(self, request: DbRequest) -> Tuple[bool, List[Tuple[NormalizedKeyType, ValueType]], Optional[Exception]]:
        env_id = request.env_id
        db_id = request.db_id
        coro_id = self.current_caller_coro_info.coro_id
        if env_id not in self.get_all_items_queue:
            self.get_all_items_queue[env_id] = list()
        
        self.get_all_items_queue[env_id].append((coro_id, db_id))
        self.make_live()
        return False, None, None
    
    @check_request
    def _on_put(self, request: DbRequest, key: KeyType, value: Union[ValueType, ValueInfo]) -> Tuple[bool, RawValueType, Optional[Exception]]:
        key = self.serializer.dumps(normalize_compound_key(key))
        db_id = request.db_id
        env_id = request.env_id
        
        exception = None
        result = None
        try:
            # self.put_queue
            if env_id not in self.put_queue:
                self.put_queue[env_id] = dict()
            
            env_put_queue = self.put_queue[env_id]
            if db_id not in env_put_queue:
                env_put_queue[db_id] = dict()
            
            env_put_queue_db = env_put_queue[db_id]
            if key not in env_put_queue_db:
                env_put_queue_db[key] = list()
            
            # self.data_cache
            if env_id not in self.data_cache:
                self.data_cache[env_id] = dict()
            
            env_data_cache = self.data_cache[env_id]
            if db_id not in env_data_cache:
                env_data_cache[db_id] = dict()
            
            env_data_cache_db = env_data_cache[db_id]
            if key not in env_data_cache_db:
                env_data_cache_db[key] = list()
            
            # both
            if isinstance(value, ValueInfo):
                result = RawValueInfo(self.serializer.dumps(value.value), value.dupdata, value.overwrite, value.append)
                if env_put_queue_db[key] and not value.dupdata:
                    env_data_cache_db[key][0] = env_put_queue_db[key][0] = result
                else:
                    env_put_queue_db[key].append(result)
                    env_data_cache_db[key].append(result)
            else:
                result = self.serializer.dumps(value)
                if env_put_queue_db[key]:
                    env_data_cache_db[key][0] = env_put_queue_db[key][0] = result
                else:
                    env_put_queue_db[key].append(result)
                    env_data_cache_db[key].append(result)
        except:
            exception = get_exception()
        
        self.make_live()
        return True, result, exception
    
    @check_request
    def _on_put_items(self, request: DbRequest, db_items: Dict[InputKeyType, Union[ValueType, ValueInfo]]) -> Tuple[bool, Dict[DbId, Dict[RawKeyType, Tuple[RawValueType, Optional[Exception]]]], Optional[Exception]]:
        result_items: Dict[DbId, Dict[RawKeyType, Tuple[RawValueType, Optional[Exception]]]] = dict()
        db_id = request.db_id
        env_id = request.env_id

        # self.put_queue
        if env_id not in self.put_queue:
            self.put_queue[env_id] = dict()
        
        env_put_queue = self.put_queue[env_id]
        if db_id not in result_items:
            result_items[db_id] = dict()
        
        result_db_items = result_items[db_id]
        
        if db_id not in env_put_queue:
            env_put_queue[db_id] = dict()
        
        env_put_queue_db = env_put_queue[db_id]

        # self.data_cache
        if env_id not in self.data_cache:
            self.data_cache[env_id] = dict()
        
        env_data_cache = self.data_cache[env_id]
        if db_id not in result_items:
            result_items[db_id] = dict()
        
        result_db_items = result_items[db_id]
        
        if db_id not in env_data_cache:
            env_data_cache[db_id] = dict()
        
        env_data_cache_db = env_data_cache[db_id]

        # both
        for key, value in db_items.items():
            key = self.serializer.dumps(normalize_compound_key(key))
            
            exception = None
            result = None
            try:
                if key not in env_put_queue_db:
                    env_put_queue_db[key] = list()
                
                if key not in env_data_cache_db:
                    env_data_cache_db[key] = list()
                
                if isinstance(value, ValueInfo):
                    result = env_data_cache_db[key][0] = env_put_queue_db[key][0] = RawValueInfo(self.serializer.dumps(value.value), value.dupdata, value.overwrite, value.append)
                    if env_data_cache_db[key] and not value.dupdata:
                        env_data_cache_db[key][0] = env_put_queue_db[key][0] = result
                    else:
                        env_put_queue_db[key].append(result)
                        env_data_cache_db[key].append(result)
                else:
                    result = self.serializer.dumps(value)
                    if env_data_cache_db[key]:
                        env_data_cache_db[key][0] = env_put_queue_db[key][0] = result
                    else:
                        env_put_queue_db[key].append(result)
                        env_data_cache_db[key].append(result)
            except:
                exception = get_exception()
            
            result_db_items[key] = (result, exception)
        
        self.make_live()
        return True, result_items, None
    
    @check_request
    def _on_delete(self, request: DbRequest, key: KeyType) -> Tuple[bool, None, Optional[Exception]]:
        key = self.serializer.dumps(normalize_compound_key(key))
        if key.startswith(EnvInfo.db_name_prefix_bytes):
            return True, None, KeyError(f'Can not delete special key (db info key): {key}')
        
        db_id = request.db_id
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
    
    @check_request
    def _on_delete_kv(self, request: DbRequest, key: InputKeyType, value: ValueType) -> Tuple[bool, RawValueType, Optional[Exception]]:
        raw_key: bytes = self.serializer.dumps(normalize_compound_key(key))
        if raw_key.startswith(EnvInfo.db_name_prefix_bytes):
            return True, None, KeyError(f'Can not delete special raw_key (db info raw_key): {raw_key}')
        
        db_id = request.db_id
        env_id = request.env_id
        
        exception = None
        raw_value = None
        try:
            if env_id not in self.kv_deletion_cache:
                self.kv_deletion_cache[env_id] = dict()
            
            env_kv_deletion_cache = self.kv_deletion_cache[env_id]
            if db_id not in env_kv_deletion_cache:
                env_kv_deletion_cache[db_id] = dict()
            
            env_kv_deletion_cache_db = env_kv_deletion_cache[db_id]
            if raw_key not in env_kv_deletion_cache_db:
                env_kv_deletion_cache_db[raw_key] = list()
            
            raw_value = self.serializer.dumps(value)
            env_kv_deletion_cache_db[raw_key].append(raw_value)
        except:
            exception = get_exception()
        
        self.make_live()
        return True, (raw_key, raw_value), exception
    
    @check_request
    def _on_delete_items(self, request: DbRequest, db_items: Set[InputKeyType]) -> Tuple[bool, Dict[DbId, Dict[RawKeyType, Optional[Exception]]], Optional[Exception]]:
        result_items: Dict[InputKeyType, Tuple[RawKeyType, Optional[Exception]]] = dict()
        db_id = request.db_id
        env_id = request.env_id

        if env_id not in self.deletion_cache:
            self.deletion_cache[env_id] = dict()
        
        env_deletion_cache = self.deletion_cache[env_id]
        if db_id not in env_deletion_cache:
            env_deletion_cache[db_id] = set()
        
        env_deletion_cache_db = env_deletion_cache[db_id]
        for key in db_items:
            exception = None
            try:
                raw_key: bytes = self.serializer.dumps(normalize_compound_key(key))
                if raw_key.startswith(EnvInfo.db_name_prefix_bytes):
                    exception = KeyError(f'Can not delete special key (db info key): {raw_key}')
                else:
                    env_deletion_cache_db.add(raw_key)
            except:
                exception = get_exception()
            
            result_items[key] = (raw_key, exception)

        self.make_live()
        return True, result_items, None
    
    @check_request
    def _on_delete_kv_items(self, request: DbRequest, db_items: Dict[InputKeyType, Tuple[ValueType]]) -> Tuple[bool, Dict[DbId, Dict[RawKeyType, Tuple[RawValueType, Optional[Exception]]]], Optional[Exception]]:
        result_items: Dict[InputKeyType, Tuple[RawKeyType, RawValueType, Optional[Exception]]] = dict()
        db_id = request.db_id
        env_id = request.env_id

        if env_id not in self.kv_deletion_cache:
            self.kv_deletion_cache[env_id] = dict()
        
        env_kv_deletion_cache = self.kv_deletion_cache[env_id]
        if db_id not in env_kv_deletion_cache:
            env_kv_deletion_cache[db_id] = dict()
        
        env_kv_deletion_cache_db = env_kv_deletion_cache[db_id]
        for key, value in db_items.items():
            exception = None
            raw_key = None
            raw_value = None
            try:
                raw_key: bytes = self.serializer.dumps(normalize_compound_key(key))
                if raw_key.startswith(EnvInfo.db_name_prefix_bytes):
                    exception = KeyError(f'Can not delete special key (db info key): {raw_key}')
                else:
                    if raw_key not in env_kv_deletion_cache_db:
                        env_kv_deletion_cache_db[raw_key] = list()
                    
                    raw_value = self.serializer.dumps(value)
                    env_kv_deletion_cache_db[raw_key].append(self.serializer.dumps(value))
            except:
                exception = get_exception()
            
            result_items[key] = (raw_key, raw_value, exception)
        
        self.make_live()
        return True, result_items, None
    
    def _on_open_databases(self, request: DbRequest, db_ids: Set[DbId], *args, **kwargs) -> ServiceProcessingResponse:
        try:
            env_info: EnvInfo = self.db_environments[request.env_id]
        except KeyError:
            exception = UnknownEnvError(request.env_id)
            return True, None, exception
        
        for db_id in db_ids:
            env_info.open_db(db_id, *args, **kwargs)
        
        env_info.env.sync(True)
        return True, None, None
    
    @check_request
    def _on_drop_db(self, request: DbRequest, delete: bool = False) -> ServiceProcessingResponse:
        coro_id = self.current_caller_coro_info.coro_id
        db_id = request.db_id
        env_id = request.env_id

        if env_id not in self.drop_db_requests:
            self.drop_db_requests[env_id] = dict()
        
        drop_db_requests_env = self.drop_db_requests[env_id]

        if db_id not in drop_db_requests_env:
            drop_db_requests_env[db_id] = (False, set())
        
        drop_db_requests_env_db: Tuple[bool, Set[CoroID]] = drop_db_requests_env[db_id]

        if delete and (not drop_db_requests_env_db[0]):
            drop_db_requests_env_db = (True, drop_db_requests_env_db[1])
        
        drop_db_requests_env_db[1].add(coro_id)
        self.make_live()
        return False, None, None
    
    def sync_in_thread_pool(self, env_id: EnvId = None):
        async def sync_db_coro(i: Interface, self: 'Db', env_id: EnvId, asyncio_loop, need_to_ensure_asyncio_loop: bool):
            if need_to_ensure_asyncio_loop:
                asyncio_loop = await i(AsyncioLoop, AsyncioLoopRequest().ensure_loop(None,CoroPriority.low, True))
            else:
                if asyncio_loop is None:
                    asyncio_loop = await i(AsyncioLoop, AsyncioLoopRequest().get())
            
            async def sync_db(self: 'Db', asyncio_loop, env: lmdb.Environment):
                def sync_worker():
                    env.sync(True)
                    self.write_locked.discard(env_id)
                
                await task_in_thread_pool(asyncio_loop, sync_worker)

            env: lmdb.Environment = self.db_environments[env_id].env
            await i(AsyncioLoop, AsyncioLoopRequest().wait(sync_db(self, asyncio_loop, env)))
            self.write_locked_coro_id.discard(i.coro_id)
            self.envs_in_sync.discard(env_id)
            def make_service_live_for_a_next_sync(self: 'Db'):
                self.make_live()
                self.wake_up_handle_registered = False
            
            if not self.wake_up_handle_registered:
                self.wake_up_handle_registered = True
                await i(TimerFuncRunner, self.sync_time_interval, make_service_live_for_a_next_sync, self)

        asyncio_loop = None
        need_to_ensure_asyncio_loop = False
        try:
            asyncio_loop = self._loop.get_service_instance(AsyncioLoop).inline_get()
        except AsyncioLoopWasNotSetError:
            need_to_ensure_asyncio_loop = True

        coro: CoroWrapperBase = put_root_from_other_service(self, sync_db_coro, self, env_id, asyncio_loop, need_to_ensure_asyncio_loop)
        coro.is_background_coro = True
        self.write_locked.add(env_id)
        self.write_locked_coro_id.add(coro.coro_id)
        self.envs_in_sync.add(env_id)


DbRequest.default_service_type = Db


def lmdb_reapplier(env_info: EnvInfo, handler: Callable, *args, **kwargs):
    environment: lmdb.Environment = env_info.env
    failed = True
    while failed:
        need_to_resize: bool = False
        try:
            handler(env_info, *args, **kwargs)
            failed = False
        except DBError as err:
            if isinstance(err.original_exception, lmdb.MapFullError):
                need_to_resize = True
        
        if need_to_resize:
            environment.set_mapsize(environment.info()['map_size'] + 2 * 1024**2)
