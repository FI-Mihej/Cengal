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
__version__ = "4.2.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.parallel_execution.asyncio.run_in_process_pool.versions.v_0.run_in_process_pool import *
import asyncio
from unittest import TestCase, main
from concurrent.futures import ProcessPoolExecutor


async def aworker(text: str) -> str:
    return text.upper()


async def worker(text: str) -> str:
    return text.upper()


class MyException(Exception):
    pass


async def aworker_ex(text: str) -> str:
    raise MyException('test')
    return text.upper()


async def worker_ex(text: str) -> str:
    raise MyException('test')
    return text.upper()


class TestProcessPool(TestCase):
    def test__multiprocess_async(self):
        async def coro(self):
            pp: ProcessPool = ProcessPool(ExecutorTypeSetup(ProcessPoolExecutor))
            pp.set_is_multiprocessing(True)
            result = await pp(aworker, 'test')
            self.assertEqual(result, 'TEST')
        
        asyncio.run(coro(self))

    def test__singleprocess_async(self):
        async def coro(self):
            pp: ProcessPool = ProcessPool(ExecutorTypeSetup(ProcessPoolExecutor))
            pp.set_is_multiprocessing(False)
            result = await pp(aworker, 'test')
            self.assertEqual(result, 'TEST')
        
        asyncio.run(coro(self))

    def test__multiprocess_async_ex(self):
        async def coro(self):
            pp: ProcessPool = ProcessPool(ExecutorTypeSetup(ProcessPoolExecutor))
            pp.set_is_multiprocessing(True)
            with self.assertRaises(MyException) as cm:
                result = await pp(aworker_ex, 'test')
            
            self.assertEqual(str(cm.exception), 'test')
        
        asyncio.run(coro(self))

    def test__multiprocess_sync_ex(self):
        async def coro(self):
            pp: ProcessPool = ProcessPool(ExecutorTypeSetup(ProcessPoolExecutor))
            pp.set_is_multiprocessing(True)
            with self.assertRaises(MyException) as cm:
                result = await pp(worker_ex, 'test')
            
            self.assertEqual(str(cm.exception), 'test')
        
        asyncio.run(coro(self))


if __name__ == '__main__':
    main()
