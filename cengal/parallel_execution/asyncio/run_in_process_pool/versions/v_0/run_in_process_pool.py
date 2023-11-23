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

__all__ = ['ProcessPoolRuntimeError', 'ExecutorSetupBase', 'ExecutorTypeSetup', 'ExecutorInstanceSetup', 'InitializerSetup', 'ProcessPoolSetup', 'ProcessPool']

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


import sys
import asyncio
from concurrent.futures import Executor
from functools import partial
from typing import Callable, Optional, Type, Any, Tuple
from cengal.introspection.inspect import get_exception, is_async


class ProcessPoolRuntimeError(RuntimeError):
    pass


class ExecutorSetupBase:
    pass


class ExecutorTypeSetup(ExecutorSetupBase):
    def __init__(self, executor_type: Type[Executor], *args, **kwargs) -> None:
        self.executor_type: Type[Executor] = executor_type
        self.args = args
        self.kwargs = kwargs
        super().__init__()


class ExecutorInstanceSetup(ExecutorSetupBase):
    def __init__(self, executor: Executor) -> None:
        self.executor: Executor = executor
        super().__init__()


class InitializerSetup:
    def __init__(self, initializer: Callable, *args, **kwargs) -> None:
        self.initializer: Callable = initializer
        self.args = args
        self.kwargs = kwargs


class ProcessPoolSetup:
    def __init__(self, is_multiprocessing: bool = True, loop: Optional[asyncio.AbstractEventLoop] = None) -> None:
        self.loop: Optional[asyncio.AbstractEventLoop] = loop or asyncio.get_event_loop()
        self.is_multiprocessing: bool = is_multiprocessing


class ProcessPool:
    def __init__(self, executor_setup: ExecutorSetupBase, initializer_setup: Optional[InitializerSetup] = None, process_pool_setup: Optional[ProcessPoolSetup] = None) -> None:
        self.executor_setup: ExecutorSetupBase = executor_setup
        self.process_pool_setup: Optional[ProcessPoolSetup] = process_pool_setup or ProcessPoolSetup()
        self.initializer_setup: Optional[InitializerSetup] = initializer_setup
        self.executor: Executor = None
        self.partial_pool_initializer: Callable = None
        
        self._create_pool()
    
    def set_is_multiprocessing(self, is_multiprocessing: bool):
        self.process_pool_setup.is_multiprocessing = is_multiprocessing
    
    def _create_pool(self):
        if self.initializer_setup is not None:
            self.partial_pool_initializer = partial(ProcessPool._initializer, self.initializer_setup.initializer, *self.initializer_setup.args, **self.initializer_setup.kwargs)
        
        if 7 <= sys.version_info[1]:
            if isinstance(self.executor_setup, ExecutorInstanceSetup):
                self.executor = self.executor_setup.executor
            elif isinstance(self.executor_setup, ExecutorTypeSetup):
                if self.partial_pool_initializer is not None:
                    self.executor_setup.kwargs['initializer'] = self.partial_pool_initializer
                
                self.executor = self.executor_setup.executor_type(*self.executor_setup.args, **self.executor_setup.kwargs)
            else:
                raise ProcessPoolRuntimeError('Unknown "executor_setup" parameter type')
        else:
            self.executor = self.executor_setup.executor_type(*self.executor_setup.args, **self.executor_setup.kwargs)
    
    def shutdown(self, wait=True, cancel_futures=False):
        self.executor.shutdown(wait, cancel_futures=cancel_futures)
    
    @staticmethod
    def _initializer(initializer, *args, **kwargs):
        import multiprocessing
        
        initializer(multiprocessing.current_process()._identity, *args, **kwargs)

    @staticmethod
    def _pool_worker(worker: Callable, *args, **kwargs) -> Tuple[Any, Optional[BaseException]]:
        result = None
        exception = None
        try:
            result = worker(*args, **kwargs)
        except:
            exception = get_exception()
        
        return result, exception

    @staticmethod
    def _pool_worker_wrapper(partial_pool_initializer: Callable, worker: Callable, *args, **kwargs) -> Tuple[Any, Optional[BaseException]]:
        global process_initialized
        if 'process_initialized' not in globals():
            process_initialized = False
        
        if not process_initialized:
            partial_pool_initializer()
            process_initialized = True
        
        return worker(*args, **kwargs)

    @staticmethod
    async def _apool_worker(worker: Callable, *args, **kwargs) -> Tuple[Any, Optional[BaseException]]:
        result = None
        exception = None
        try:
            result = await worker(*args, **kwargs)
        except:
            exception = get_exception()
        
        return result, exception

    @staticmethod
    async def _apool_worker_wrapper(partial_pool_initializer: Callable, worker: Callable, *args, **kwargs) -> Tuple[Any, Optional[BaseException]]:
        global process_initialized
        if 'process_initialized' not in globals():
            process_initialized = False
        
        if not process_initialized:
            partial_pool_initializer()
            process_initialized = True
        
        return await worker(*args, **kwargs)

    async def pool_execute(self, worker: Callable, *args, **kwargs) -> Any:
        if (7 <= sys.version_info[1]) or (self.partial_pool_initializer is None):
            partial_pool_worker = partial(ProcessPool._pool_worker, worker, *args, **kwargs)
        else:
            partial_pool_worker = partial(ProcessPool._pool_worker_wrapper, self.partial_pool_initializer, worker, *args, **kwargs)
            
        if self.process_pool_setup.is_multiprocessing:
            result: Tuple[Any, Optional[BaseException]] = await self.process_pool_setup.loop.run_in_executor(self.executor, partial_pool_worker)
        else:
            if is_async(worker):
                result = await worker(*args, **kwargs)
            else:
                result = worker(*args, **kwargs)
        
        result, exception = result
        
        if exception is not None:
            raise exception
        
        return result
    
    async def __call__(self, worker: Callable, *args, **kwargs) -> Any:
        return await self.pool_execute(worker, *args, **kwargs)


# def pool_initializer(text):
#     import multiprocessing
    
#     print(text, multiprocessing.current_process()._identity[0])


# def create_pool():
#     global executor_init_params
#     executor_init_params = (('hello pool',), dict())
#     global executor
#     if 7 <= sys.version_info[1]:
#         pool_args, pool_kwargs = executor_init_params
#         partial_pool_initializer = partial(pool_initializer, *pool_args, **pool_kwargs)
#         executor = ProcessPoolExecutor(max_workers=2, initializer=partial_pool_initializer)
#     else:
#         executor = ProcessPoolExecutor(max_workers=2)


# def pool_worker_impl(item: int):
#     return 1000 / item


# def pool_worker(*args, **kwargs):
#     result = None
#     exception = None
#     try:
#         result = pool_worker_impl(*args, **kwargs)
#     except:
#         exception = get_exception()
    
#     return result, exception


# def pool_worker_wrapper(pool_init_params, *args, **kwargs):
#     global process_initialized
#     if 'process_initialized' not in globals():
#         process_initialized = False
    
#     if not process_initialized:
#         pool_args, pool_kwargs = pool_init_params
#         pool_initializer(*pool_args, **pool_kwargs)
#         process_initialized = True
    
#     return pool_worker(*args, **kwargs)
        

# async def pool_execute(*args, **kwargs):
#     if 7 <= sys.version_info[1]:
#         partial_pool_worker = partial(pool_worker, *args, **kwargs)
#     else:
#         partial_pool_worker = partial(pool_worker_wrapper, executor_init_params, *args, **kwargs)
        
#     if is_multiprocessing:
#         result = await loop.run_in_executor(executor, partial_pool_worker)
#     else:
#         result = pool_worker(*args, **kwargs)
    
#     result, exception = result
    
#     if exception is not None:
#         raise exception
    
#     return result


# async def pool_single_processing_example(item: int = 2):
#     return await pool_execute(item)


# async def pool_gather_example(num: int = 3):
#     return await asyncio.gather(*[pool_execute(i) for i in range(num)])
