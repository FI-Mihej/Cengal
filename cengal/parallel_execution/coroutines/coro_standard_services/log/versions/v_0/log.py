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


__all__ = ['InfoFields', 'default_info_gatherer', 'LogExtended', 'LogEx', 'Log', 'LogRequest', 
           'view_log', 'clear_log', 'LogClient', 'default_log_client', 'log_fast', 'alog_fast', 
           'log', 'alog', 'put_log_fast', 'plog_fast', 'put_log', 'plog']

from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_tools.await_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import *
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import CoroPriority
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.timer_func_runner import *
from cengal.parallel_execution.coroutines.coro_standard_services.instance import *
from cengal.file_system.app_fs_structure.app_dir_path import AppDirPath, AppDirectoryType
from cengal.file_system.path_manager import RelativePath
from cengal.file_system.file_manager import path_relative_to_current_dir
from cengal.time_management.load_best_timer import perf_counter
from cengal.data_manipulation.serialization import *
from cengal.introspection.inspect import get_exception, frame, entity_repr_owner_based, entity_name
from cengal.code_flow_control.python_bytecode_manipulator import get_code
from cengal.code_flow_control.args_manager import args_kwargs_to_str
from cengal.code_flow_control.smart_values import ValueExistence
from enum import IntEnum
from traceback import format_stack
from typing import Tuple, List, Any, Dict, Callable
from datetime import datetime
import logging
import sys
import os
import asyncio
try:
    import lmdb
except ImportError:
    from warnings import warn
    warn('''WARNING: `lmdb` library is not installed. Log service will not work.
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
    

def get_coro_parents_path(coro_id: CoroID) -> List[CoroID]:
    parents: Set[CoroID] = set()
    result: List[CoroID] = list()
    def handler(deep, child, parent, index):
        if parent is not None:
            coro_id = parent.value
            parents.add(coro_id)
            result.append(coro_id)
    
    try_travers_through_all_coro_parents(coro_id, handler)
    return result


def coro_info_string(cs: CoroScheduler, coro_id: CoroID) -> str:
    coro: Optional[CoroWrapperBase] = cs.get_coro(coro_id)
    if coro is None:
        return f'  CoroID: {coro_id:10}'
    else:
        coro_worker = coro.worker
        if isinstance(coro_worker, GreenletWorkerWrapper):
            coro_worker = coro_worker.worker
        
        return f'  CoroID: {coro_id:10}; Type: {"Awaitable" if isinstance(coro, CoroWrapperAsyncAwait) else "Greenlet"}; Worker: {entity_repr_owner_based(coro_worker)}'


def get_coro_parents_strings(coro_id: CoroID) -> List[str]:
    coro_parents_path: List[ValueExistence[CoroID]] = get_coro_parents_path(coro_id)
    if coro_parents_path:
        cs: CoroScheduler = get_current_coro_scheduler()
        if cs is None:
            return list([f'  CoroID: {coro_id:10}' for coro_id in coro_parents_path])
        else:
            return list([coro_info_string(cs, coro_id) for coro_id in coro_parents_path])
    else:
        return list()


class InfoFields(IntEnum):
    current_time = 0
    file_name = 1
    line_number = 2
    caller_info = 3
    traceback_strings = 4
    perf_counter_time = 5
    coro_parents_strings = 6
    logging_level = 7


def default_info_gatherer(depth: int) -> Dict[str, Any]:
    interested_frame = frame(depth + 1)
    try:
        interface: Interface = current_interface()
    except OutsideCoroSchedulerContext:
        interface = None

    if interface is None:
        caller_info = entity_repr_owner_based(interested_frame)
        coro_parents_strings = list()
    else:
        coro_worker = interface._coro.worker
        if isinstance(coro_worker, GreenletWorkerWrapper):
            coro_worker = coro_worker.worker
        
        caller_info = f'CoroID: {interface.coro_id:10}; Type: {"Awaitable" if isinstance(interface._coro, CoroWrapperAsyncAwait) else "Greenlet"}; Worker: {entity_repr_owner_based(coro_worker)}'
        coro_parents_strings = get_coro_parents_strings(interface.coro_id)
    
    return {
        InfoFields.current_time: datetime.now(),
        InfoFields.perf_counter_time: perf_counter(),
        InfoFields.file_name: interested_frame.f_code.co_filename,
        InfoFields.line_number: interested_frame.f_lineno,
        InfoFields.caller_info: caller_info,
        InfoFields.traceback_strings: format_stack(interested_frame),
        InfoFields.coro_parents_strings: coro_parents_strings,
    }


class LogExtended(TypedServiceRequest[None]):
    default__request__type__ = 4

    def __init__(self, info_gatherer: Optional[Callable[[int], Dict[str, Any]]] = None, depth: Optional[int] = 1):
        super().__init__()
        self.info_gatherer: Optional[Callable] = info_gatherer
        self.depth: Optional[int] = depth
    
    def _copy(self) -> 'LogExtended':
        return LogExtended(self.info_gatherer, self.depth)

    def __call__(self, *args, **kwargs) -> 'LogEx':
        if self.info_gatherer is None:
            info = None
        else:
            info = self.info_gatherer(self.depth + 1)
        
        return self._save_to_copy(self.default__request__type__, args, kwargs, info)


LogEx = LogExtended


class LogRequest(ServiceRequest):
    def set_db_environment_path(self, path_to_db_environment: str) -> ServiceRequest:
        return self._save(0, path_to_db_environment)
    
    def sync(self) -> ServiceRequest:
        return self._save(1)

    def add_iteration_handler(self, handler: Callable[['Log', List[Tuple[Tuple, Dict]], float, str], None]) -> ServiceRequest:
        return self._save(2, handler)

    def remove_iteration_handler(self, handler: Callable[['Log', List[Tuple[Tuple, Dict]], float, str], None]) -> ServiceRequest:
        return self._save(3, handler)
    
    def log(self, *args, **kwargs) -> ServiceRequest:
        return LogEx[None](default_info_gatherer, depth=2)(*args, **kwargs)

    def connect_to_logger(self, logger_instance: logging.Logger) -> ServiceRequest:
        return self._save(5, logger_instance)

    def disconnect_from_logger(self, logger_instance: logging.Logger) -> ServiceRequest:
        return self._save(6, logger_instance)
    

class Log(TypedService[None], EntityStatsMixin):
    def __init__(self, loop: CoroScheduler):
        super(Log, self).__init__(loop)
        self.default_logs_dir: str = 'log.db'
        self.path_to_db_environment = None
        self.app_name_waiter: CoroWrapperBase = None
        self.root_path_to_log_environment_rel: RelativePath = None
        self.db_environment: lmdb.Environment = None
        self.db = None
        self.log_queue: List[Tuple[Tuple, Dict, Dict[str, Any]]] = list()
        self.async_loop = None
        self.log_counter = Counter()
        self.sync_time_interval = 0.5
        self.characters_in_counter = 16
        self.current_counter_state_key = f'{str(0).zfill(self.characters_in_counter)}'.encode()
        self.last_sync_time = perf_counter()
        self.force_sync = False
        self.write_locked = False
        self.write_locked_coro_id: Optional[CoroID] = None
        self.periodic_sync_started: bool = False
        self.iteration_handlers: List[Callable[['Log', List[Tuple[Tuple, Dict]], float, str], None]] = list()
        self.new_iteration_handlers_num: int = 0
        self.logger_handlers: Dict[logging.Logger, LoggingHandler] = dict()
        self.logger: logging.Logger = self._loop.logger
        # self.serializer = best_serializer({DataFormats.binary,
        #                                    Tags.can_use_bytes,
        #                                    Tags.decode_str_as_str,
        #                                    Tags.decode_list_as_list,
        #                                    Tags.decode_bytes_as_bytes,
        #                                    Tags.superficial,
        #                                    Tags.current_platform,
        #                                    Tags.multi_platform},
        #                                   test_data_factory(TestDataType.small),
        #                                   0.1)
        self.serializer = Serializer(Serializers.msgspec_messagepack)

        self._request_workers = {
            0: self._on_set_db_environment_path,
            1: self._on_sync,
            2: self._on_add_iteration_handler,
            3: self._on_remove_iteration_handler,
            4: self._on_log_extended,
            5: self._on_connect_to_logger,
            6: self._on_disconnect_from_logger,
        }
        self.inject_handler_to_logger(self._loop.logger)

    def get_entity_stats(self, stats_level: 'EntityStatsMixin.StatsLevel' = EntityStatsMixin.StatsLevel.debug) -> Tuple[str, Dict[str, Any]]:
        return type(self).__name__, {
            'log counter': self.log_counter._index,
            'current counter state key': self.current_counter_state_key,
        }
    
    def put_log(self, args, kwargs):
        self.log_queue.append((args, kwargs, None))
        # self.make_live
    
    def put_log_ex(self, args, kwargs, info):
        self.log_queue.append((args, kwargs, info))

    def destroy(self):
        # TODO: we need to use some loop destroy service in order to put our coro which will write all pending queues,
        # sync envirounments and close them. Also we need to prevent new requests from being processed. (see DB service)
        loggers_instancess = list(self.logger_handlers.keys())
        for logger_instance in loggers_instancess:
            self.eject_handler_from_logger(logger_instance)

        if self.db_environment is not None:
            self.db_environment.close()

    def single_task_registration_or_immediate_processing(
            self, *args, **kwargs) -> Tuple[bool, None, None]:
        result = self.try_resolve_request(*args, **kwargs)
        if result is None:
            coro_info = self.current_caller_coro_info
            coro_worker = coro_info.coro.worker
            if isinstance(coro_worker, GreenletWorkerWrapper):
                coro_worker = coro_worker.worker
            
            caller_info = f'CoroID: {coro_info.coro_id:10}; Type: {"Awaitable" if issubclass(coro_info.coro_type, CoroWrapperAsyncAwait) else "Greenlet"}; Worker: {entity_repr_owner_based(coro_worker)}'
            coro_worker_code = get_code(coro_worker)
            info = {
                InfoFields.current_time: datetime.now(),
                InfoFields.perf_counter_time: perf_counter(),
                InfoFields.file_name: coro_worker_code.co_filename,
                InfoFields.line_number: coro_worker_code.co_firstlineno,
                InfoFields.caller_info: caller_info,
                InfoFields.traceback_strings: list(),
                # InfoFields.coro_parents_strings: get_coro_parents_strings(coro_info.coro_id),
                InfoFields.coro_parents_strings: list(),
            }
            self.log_queue.append((args, kwargs, info))
            # self.make_live()

            # TODO: we need to implement backpressure mechanism here. If we have too many pending requests, we need to put request to queue instead of responding immediately.
            # However this will not be enough for a direct requests. We need to implement some kind of backpressure mechanism for direct requests too.
            return True, None, None
        else:
            return result

    def _ensure_default_db_environment(self) -> bool:
        if self.db_environment is None:
            if self.path_to_db_environment is None:
                if self.app_name_waiter is None:
                    async def coro(i: Interface, self: 'Log'):
                        app_name_for_fs = await i(InstanceRequest().wait('app_name_for_fs'))
                        app_data_dir_path_type: AppDirectoryType = await i(InstanceRequest().wait('app_data_dir_path_type'))
                        app_dir_path: AppDirPath = await i(InstanceRequest().wait(AppDirPath))
                        app_data_dir_path: str = app_dir_path.cached(app_data_dir_path_type, app_name_for_fs)
                        self.path_to_db_environment = RelativePath(app_data_dir_path)(self.default_logs_dir)
                        self._init_db()
                        self.app_name_waiter = None
                        self.make_live()
                    
                    self.app_name_waiter = put_root_from_other_service(self, coro, self)
                
                self.make_dead()
                return False
            else:
                self._init_db()
                return True
        else:
            return True

    def full_processing_iteration(self):
        if not self._ensure_default_db_environment():
            return
        
        self.force_sync = False
        log_queue_buff = self.log_queue
        self.log_queue = type(log_queue_buff)()
        current_time = perf_counter()
        current_time_str = str(current_time)
        for iteration_handler in self.iteration_handlers:
            iteration_handler(self, log_queue_buff, current_time, current_time_str)
        
        self.new_iteration_handlers_num = 0

        def handler():
            with self.db_environment.begin(write=True) as txn:
                for log_info in log_queue_buff:
                    key = f'{str(self.log_counter.get()).zfill(self.characters_in_counter)}__{current_time_str}'.encode()
                    value = self.serializer.dumps(log_info)
                    txn.put(key, value, db=self.db, dupdata=True, append=True)
                
                txn.put(self.current_counter_state_key, self.serializer.dumps(self.log_counter._index), db=self.db)
        
        lmdb_reapplier(self.db_environment, self.db, handler)
        
        self.sync_in_thread_pool()
        
        self.last_sync_time = perf_counter()

        self.make_dead()

    def in_work(self) -> bool:
        result: bool = bool(self.log_queue) \
            or (self.db_environment is None) \
            or (not self.periodic_sync_started) \
            or self.new_iteration_handlers_num \
            or (self.force_sync or ((not self.write_locked) and bool(self.log_queue) and ((perf_counter() - self.last_sync_time) >= self.sync_time_interval)))
        return self.thrifty_in_work(result)
    
    def time_left_before_next_event(self) -> Tuple[bool, Optional[Union[int, float]]]:
        time_since_last_sync_time: float = perf_counter() - self.last_sync_time
        if self.sync_time_interval > time_since_last_sync_time:
            return True, self.sync_time_interval - time_since_last_sync_time
        else:
            return True, 0

    def _init_db(self):
        self.logger.info(f'Path to Log DB Env: {self.path_to_db_environment}')
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
        if self.db_environment is None:
            self.make_live()
        else:
            if self.log_queue:
                self.force_sync = True
                self.make_live()
            else:
                # self.db_environment.sync(True)
                self.sync_in_thread_pool()
        
        return True, None, None

    def _on_log_extended(self, args, kwargs, info):
        self.log_queue.append((args, kwargs, info))
        return True, None, None

    def _on_add_iteration_handler(self, handler: Callable[['Log', List[Tuple[Tuple, Dict]], float, str], None]):
        self.iteration_handlers.append(handler)
        self.new_iteration_handlers_num += 1
        return True, None, None
    
    def _on_remove_iteration_handler(self, handler: Callable[['Log', List[Tuple[Tuple, Dict]], float, str], None]):
        removed = False
        try:
            self.iteration_handlers.remove(handler)
            removed = True
        except ValueError:
            pass

        return True, removed, None

    def sync_in_thread_pool(self):
        async def sync_db_coro(i: Interface, self: 'Log', asyncio_loop, need_to_ensure_asyncio_loop: bool):
            if need_to_ensure_asyncio_loop:
                asyncio_loop = await i(AsyncioLoop, AsyncioLoopRequest().ensure_loop(None, CoroPriority.low, True))
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
            def make_service_live_for_a_next_sync(self: 'Log'):
                self.periodic_sync_started = False
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
        self.periodic_sync_started = True
    
    def get_last_n_logs(self, number: Union[None, int]=None) -> List[Tuple[Tuple, Dict, Dict[str, Any]]]:
        if self.db_environment is None:
            return list()
        
        if number is None:
            number = self.log_counter._index + 1
        elif number <= 0:
            return list()
        
        result = list()
        with self.db_environment.begin(db=self.db) as txn:
            txn.cursor().last()
            for key, value in txn.cursor().iterprev():
                if key == self.current_counter_state_key:
                    continue

                if number <= 0:
                    break

                result.append(self.serializer.loads(value))
                number -= 1
        
        result.reverse()
        return result

    def inject_handler_to_logger(self, logger_instance: logging.Logger) -> bool:
        if logger_instance not in self.logger_handlers:
            logger_handler: LoggingHandler = LoggingHandler(self)
            self.logger_handlers[logger_instance] = logger_handler
            logger_instance.addHandler(logger_handler)
            return True
        else:
            return False

    def _on_connect_to_logger(self, logger_instance: logging.Logger):
        result = self.inject_handler_to_logger(logger_instance)
        return True, result, None

    def eject_handler_from_logger(self, logger_instance: logging.Logger) -> bool:
        if logger_instance in self.logger_handlers:
            logger_instance.removeHandler(self.logger_handlers[logger_instance])
            del self.logger_handlers[logger_instance]
            return True
        else:
            return False

    def _on_disconnect_from_logger(self, logger_instance: logging.Logger):
        result = self.eject_handler_from_logger(logger_instance)
        return True, result, None


LogExtended.default_service_type = Log
LogRequest.default_service_type = Log


class LogClient:
    def __init__(self, info_gatherer: Optional[Callable[[int], Dict[str, Any]]] = None) -> None:
        self.info_gatherer: Optional[Callable] = info_gatherer
        self.log_extended_request: LogEx = LogEx(default_info_gatherer, depth=2)
        self.extended: bool = True

    def log_fast(self, i: Interface, *args, **kwargs) -> Optional[Any]:
        if self.extended:
            i(self.log_extended_request(*args, **kwargs))
        else:
            i(Log, *args, **kwargs)
        
        return args[0] if args else None

    async def alog_fast(self, i: Interface, *args, **kwargs) -> Optional[Any]:
        if self.extended:
            await i(self.log_extended_request(*args, **kwargs))
        else:
            await i(Log, *args, **kwargs)
        
        return args[0] if args else None

    def log(self, *args, **kwargs) -> Optional[Any]:
        if self.extended:
            current_interface()(self.log_extended_request(*args, **kwargs))
        else:
            current_interface()(Log, *args, **kwargs)
        
        return args[0] if args else None

    async def alog(self, *args, **kwargs) -> Optional[Any]:
        if self.extended:
            await current_interface()(self.log_extended_request(*args, **kwargs))
        else:
            await current_interface()(Log, *args, **kwargs)
        
        return args[0] if args else None

    def put_log_fast(self, scheduler: CoroScheduler, *args, **kwargs) -> Optional[Any]:
        if self.extended:
            log_ex_request: LogExtended = self.log_extended_request(*args, **kwargs)
            scheduler.get_service_instance_fast(Log).put_log_ex(*log_ex_request.args, **log_ex_request.kwargs)
        else:
            scheduler.get_service_instance_fast(Log).put_log(args, kwargs)
        
        return args[0] if args else None

    plog_fast = put_log_fast

    # async def aput_log_fast(self, scheduler: CoroScheduler, *args, **kwargs):
    #     if self.extended:
    #         log_ex_request: LogExtended = self.log_extended_request(*args, **kwargs)
    #         scheduler.get_service_instance_fast(Log).put_log_ex(*log_ex_request.args, **log_ex_request.kwargs)
    #     else:
    #         scheduler.get_service_instance_fast(Log).put_log(args, kwargs)

    # aplog_fast = aput_log_fast

    def put_log(self, *args, **kwargs) -> Optional[Any]:
        return self.put_log_fast(current_coro_scheduler(), *args, **kwargs)

    plog = put_log

    # async def aput_log(self, *args, **kwargs):
    #     self.put_log_fast(current_coro_scheduler(), *args, **kwargs)

    # aplog = aput_log


default_log_client: LogClient = LogClient(default_info_gatherer)
log_fast = default_log_client.log_fast
alog_fast = default_log_client.alog_fast
log = default_log_client.log
alog = default_log_client.alog
put_log_fast = default_log_client.put_log_fast
plog_fast = default_log_client.plog_fast
put_log = default_log_client.put_log
plog = default_log_client.plog
# aput_log_fast = default_log_client.aput_log_fast
# aplog_fast = default_log_client.aplog_fast
# aput_log = default_log_client.aput_log
# aplog = default_log_client.aplog


def view_log(path_to_db_environment: Optional[str]=None, file_to_redirect_output: Optional[str]=None):
    if path_to_db_environment is None:
        path_to_db_environment = path_relative_to_current_dir('log.db')

    output_file = None
    if file_to_redirect_output is not None:
        output_file = open(file_to_redirect_output, 'wb')

    try:
        db_environment = lmdb.open(path_to_db_environment, map_size=20 * 1024 ** 2, writemap=True, max_dbs=2)
        db = db_environment.open_db(b'logs')
        # serializer = best_serializer({DataFormats.binary,
        #                               Tags.can_use_bytes,
        #                               Tags.decode_str_as_str,
        #                               Tags.decode_list_as_list,
        #                               Tags.decode_bytes_as_bytes, 
        #                               Tags.superficial,
        #                               Tags.current_platform,
        #                               Tags.multi_platform},
        #                              test_data_factory(TestDataType.small),
        #                              0.1)
        serializer = Serializer(Serializers.msgspec_messagepack)
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
                    args, kwargs, info = serializer.loads(value)
                    if output_file is None:
                        print(f'λ >>>\t{key}: {"~"*8}')
                        print(*args, **kwargs)
                        print(info)
                        print()
                    else:
                        output_file.write(f'λ >>>\t{key}: {"~"*8}\n'.encode())
                        output_file.write(f'{args_kwargs_to_str(args, kwargs)}\n'.encode())
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



class LoggingHandler(logging.Handler):
    def __init__(self, log_service: Log, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log_service: Log = log_service
        self.cs: CoroScheduler = log_service._loop

    def emit(self, record: logging.LogRecord):
        log_entry = self.format(record)
        interested_frame = frame(7)  # TODO: mostly correct at least for a Python 3.8.10 (wrong at least for `warn()` and `exception()` logger methods)
        try:
            interface: Interface = current_interface()
        except OutsideCoroSchedulerContext:
            interface = None

        if interface is None:
            caller_info = f'FuncName: {record.funcName}'
            coro_parents_strings = list()
        else:
            coro_worker = interface._coro.worker
            if isinstance(coro_worker, GreenletWorkerWrapper):
                coro_worker = coro_worker.worker
            
            caller_info = f'FuncName: {record.funcName}; CoroID: {interface.coro_id:10}; Type: {"Awaitable" if isinstance(interface._coro, CoroWrapperAsyncAwait) else "Greenlet"}; Worker: {entity_repr_owner_based(coro_worker)}'
            coro_parents_strings = get_coro_parents_strings(interface.coro_id)
        self.log_service.put_log_ex((log_entry, ), dict(), {
            InfoFields.current_time: datetime.fromtimestamp(record.created),
            InfoFields.perf_counter_time: perf_counter(),
            InfoFields.file_name: record.filename,
            InfoFields.line_number: record.lineno,
            InfoFields.caller_info: caller_info,
            InfoFields.traceback_strings: format_stack(interested_frame),
            InfoFields.coro_parents_strings: coro_parents_strings,
            InfoFields.logging_level: record.levelname,
        })
