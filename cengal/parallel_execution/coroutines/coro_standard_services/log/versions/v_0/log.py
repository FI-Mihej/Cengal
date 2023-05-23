#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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


__all__ = ['Log', 'LogRequest', 'view_log', 'clear_log', 'log_fast', 'log', 'put_log_fast', 'plog_fast', 'put_log', 'plog', 'alog_fast', 'alog', 'aput_log_fast', 'aplog_fast', 'aput_log', 'aplog']

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_tools.await_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import *
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import CoroPriority
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.timer_func_runner import *
from cengal.file_system.file_manager import path_relative_to_current_dir
from cengal.time_management.load_best_timer import perf_counter
from cengal.data_manipulation.serialization import *
from typing import Tuple, List, Any, Dict, Callable
from cengal.introspection.inspect import get_exception
import sys
import os
import asyncio
import lmdb


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.2.2"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


class LogRequest(ServiceRequest):
    def set_db_environment_path(self, path_to_db_environment: str) -> ServiceRequest:
        return self._save(0, path_to_db_environment)
    def sync(self) -> ServiceRequest:
        return self._save(1)


class Log(TypedService[None], EntityStatsMixin):
    def __init__(self, loop: CoroScheduler):
        super(Log, self).__init__(loop)
        self.log_queue: List[Tuple[Tuple, Dict]] = list()
        self.path_to_db_environment = path_relative_to_current_dir('log.db')
        self.db_environment = None
        self.db = None
        self.async_loop = None
        self.log_counter = Counter()
        self.sync_time_interval = 1.0
        self.characters_in_counter = 16
        self.current_counter_state_key = f'{str(0).zfill(self.characters_in_counter)}'.encode()
        self.last_sync_time = perf_counter()
        self.force_sync = False
        self.write_locked = False
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
            1: self._on_sync,
        }

    def get_entity_stats(self, stats_level: 'EntityStatsMixin.StatsLevel' = EntityStatsMixin.StatsLevel.debug) -> Tuple[str, Dict[str, Any]]:
        return type(self).__name__, {
            'log counter': self.log_counter._index,
            'current counter state key': self.current_counter_state_key,
        }
    
    def put_log(self, *args, **kwargs):
        self.log_queue.append((args, kwargs))
        self.make_live

    def single_task_registration_or_immediate_processing(
            self, *args, **kwargs) -> Tuple[bool, None, None]:
        result = self.try_resolve_request(*args, **kwargs)
        if result is None:
            self.log_queue.append((args, kwargs))
            self.make_live()
            return True, None, None
        else:
            return result

    def full_processing_iteration(self):
        self.force_sync = False
        
        if self.db_environment is None:
            self._init_db()

        log_queue_buff = self.log_queue
        self.log_queue = type(log_queue_buff)()
        current_time = str(perf_counter())

        def handler():
            with self.db_environment.begin(write=True) as txn:
                for args, kwargs in log_queue_buff:
                    key = f'{str(self.log_counter.get()).zfill(self.characters_in_counter)}__{current_time}'.encode()
                    value = self.serializer.dumps((args, kwargs))
                    txn.put(key, value, db=self.db, dupdata=True, append=True)
                txn.put(self.current_counter_state_key, self.serializer.dumps(self.log_counter._index), db=self.db)
        lmdb_reapplier(self.db_environment, self.db, handler)
        
        self.sync_in_thread_pool()
        
        self.last_sync_time = perf_counter()

        self.make_dead()

    def in_work(self) -> bool:
        result: bool = bool(self.log_queue) or (self.force_sync or ((not self.write_locked) and bool(self.log_queue) and ((perf_counter() - self.last_sync_time) >= self.sync_time_interval)))
        return self.thrifty_in_work(result)
    
    def time_left_before_next_event(self) -> Tuple[bool, Optional[Union[int, float]]]:
        time_since_last_sync_time: float = perf_counter() - self.last_sync_time
        if self.sync_time_interval > time_since_last_sync_time:
            return True, self.sync_time_interval - time_since_last_sync_time
        else:
            return True, 0

    def _init_db(self):
        print(f'self.path_to_db_environment: {self.path_to_db_environment}')
        self.db_environment = lmdb.open(self.path_to_db_environment, map_size=20 * 1024**2, writemap=True, max_dbs=2,
                                        map_async=True, lock=False, metasync=False, sync=False, meminit=False)
        self.db = self.db_environment.open_db(b'logs')
        def handler():
            with self.db_environment.begin(write=True) as txn:
                current_counter_state = txn.get(self.current_counter_state_key, db=self.db)
                if current_counter_state is None:
                    txn.put(self.current_counter_state_key, self.serializer.dumps(self.log_counter._index), db=self.db)
                else:
                    self.log_counter._index = self.serializer.loads(current_counter_state)
        lmdb_reapplier(self.db_environment, self.db, handler)
        self.db_environment.sync(True)

    def _on_set_db_environment_path(self, path_to_db_environment: str):
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
    
    def _on_sync(self):
        if self.log_queue:
            self.force_sync = True
            self.make_live()
        else:
            # self.db_environment.sync(True)
            self.sync_in_thread_pool()
        
        return True, None, None
    
    def sync_in_thread_pool(self):
        async def sync_db_coro(i: Interface, self, asyncio_loop, need_to_ensure_asyncio_loop: bool):
            if need_to_ensure_asyncio_loop:
                asyncio_loop = await i(AsyncioLoop, AsyncioLoopRequest().ensure_loop(None,CoroPriority.low, True))
            else:
                if asyncio_loop is None:
                    asyncio_loop = await i(AsyncioLoop, AsyncioLoopRequest.get())
            
            async def sync_db(self, asyncio_loop):
                def sync_worker():
                    self.db_environment.sync(True)
                
                await task_in_thread_pool(asyncio_loop, sync_worker)

            await i(AsyncioLoop, AsyncioLoopRequest.wait(sync_db, self, asyncio_loop))
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


LogRequest.default_service_type = Log


def log_fast(i: Interface, *args, **kwargs):
    i(Log, *args, **kwargs)


def log(*args, **kwargs):
    current_interface()(Log, *args, **kwargs)


def put_log_fast(scheduler: CoroScheduler, *args, **kwargs):
    scheduler.get_service_instance_fast(Log).put_log(*args, **kwargs)


plog_fast = put_log_fast


def put_log(*args, **kwargs):
    put_log_fast(current_coro_scheduler(), *args, **kwargs)


plog = put_log


async def alog_fast(i: Interface, *args, **kwargs):
    await i(Log, *args, **kwargs)


async def alog(*args, **kwargs):
    current_interface()(Log, *args, **kwargs)


async def aput_log_fast(scheduler: CoroScheduler, *args, **kwargs):
    scheduler.get_service_instance_fast(Log).put_log(*args, **kwargs)


aplog_fast = aput_log_fast


async def aput_log(*args, **kwargs):
    put_log_fast(current_coro_scheduler(), *args, **kwargs)


aplog = aput_log


def view_log(path_to_db_environment: Optional[str]=None, file_to_redirect_output: Optional[str]=None):
    if path_to_db_environment is None:
        path_to_db_environment = path_relative_to_current_dir('log.db')

    output_file = None
    if file_to_redirect_output is not None:
        output_file = open(file_to_redirect_output, 'wb')

    try:
        db_environment = lmdb.open(path_to_db_environment, map_size=20 * 1024 ** 2, writemap=True, max_dbs=2)
        db = db_environment.open_db(b'logs')
        serializer = best_serializer({DataFormats.binary,
                                      Tags.can_use_bytes,
                                      Tags.decode_str_as_str,
                                      Tags.decode_list_as_list,
                                      Tags.decode_bytes_as_bytes,
                                      Tags.superficial,
                                      Tags.current_platform,
                                      Tags.multi_platform},
                                     test_data_factory(TestDataType.small),
                                     0.1)
        with db_environment.begin() as txn:
            for key, value in txn.cursor(db=db):
                if key == f'{str(0).zfill(16)}'.encode():
                    if output_file is None:
                        print(f'λλλ <<< {serializer.loads(value)} >>>')
                        print()
                    else:
                        output_file.write(f'λλλ <<< {serializer.loads(value)} >>>'.encode())
                        output_file.write('\n'.encode())
                else:
                    args, kwargs = serializer.loads(value)
                    if output_file is None:
                        print(f'λ >>>\t{key}: {"~"*8}')
                        print(*args, **kwargs)
                        print()
                    else:
                        output_file.write(f'λ >>>\t{key}: {"~"*8}\n'.encode())
                        output_file.write(f'{str((args, kwargs))}\n'.encode())
                        output_file.write('\n'.encode())
    finally:
        if output_file is not None:
            output_file.close()


def clear_log(path_to_db_environment: Optional[str]=None):
    if path_to_db_environment is None:
        path_to_db_environment = path_relative_to_current_dir('log.db')
    db_environment = lmdb.open(path_to_db_environment, map_size=20 * 1024 ** 2, writemap=True, max_dbs=2)
    db = db_environment.open_db(b'logs')
    def handler():
        with db_environment.begin(write=True) as txn:
            txn.drop(db=db, delete=False)
    lmdb_reapplier(db_environment, db, handler)


def lmdb_reapplier(environment: lmdb.Environment, db, handler: Callable):
    failed = True
    while failed:
        need_to_drop = False
        try:
            handler()
            failed = False
        except lmdb.MapFullError:
            need_to_drop = True
        
        if need_to_drop:
            environment.set_mapsize(environment.info()['map_size'] + 2 * 1024**2)
            with environment.begin(write=True) as txn:
                txn.drop(db=db, delete=False)
