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


from cengal.parallel_execution.coroutines.coro_scheduler import cs_acoro, cs_callable, current_interface, Interface
from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_tools.await_coro import cs_awaitable
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
import asyncio

from unittest import TestCase, main


class Test__await_coro(TestCase):
    def test__cs_awaitable(self):

        def my_coro_gi(i: Interface, a: str, b: str) -> str:
            i(Sleep, 0.1)

            return a + b

        @cs_awaitable
        @cs_callable
        def my_coro_gia(i: Interface, a: str, b: str) -> str:
            i(Sleep, 0.1)

            return a + b

        def my_coro_g(a: str, b: str) -> str:
            i: Interface = current_interface()
            i(Sleep, 0.1)

            return a + b

        @cs_awaitable
        def my_coro_ga(a: str, b: str) -> str:
            i: Interface = current_interface()
            i(Sleep, 0.1)

            return a + b

        @cs_awaitable
        async def my_coro_a(a: str, b: str) -> str:
            i: Interface = current_interface()
            await i(Sleep, 0.05)

            await asyncio.sleep(0.05)

            return a + b

        @cs_acoro
        async def my_coro_a_implicit(a: str, b: str) -> str:
            i: Interface = current_interface()
            await i(Sleep, 0.05)

            await asyncio.sleep(0.05)

            return a + b

        async def my_coro_a_explicit(i: Interface, a: str, b: str) -> str:
            await i(Sleep, 0.05)

            await asyncio.sleep(0.05)

            return a + b
        
        async def my_coro_asyncio(a: str, b: str) -> str:
            await asyncio.sleep(0.1)

            return a + b
        
        @cs_acoro
        async def amain():
            i: Interface = current_interface()

            # await

            print(await my_coro_gia('a', 'b'))
            print(await my_coro_ga('a', 'b'))
            # print(await my_coro_a('a', 'b'))
            # print(await my_coro_a_implicit('a', 'b'))
            # print(await my_coro_a_explicit(i, 'a', 'b'))
            # print(await my_coro_asyncio('a', 'b'))

            # RunCoro

            print(await i(RunCoro, my_coro_ga('a', 'b')))
            # print(await i(RunCoro, my_coro_gi, 'a', 'b'))
            # # print(await i(RunCoro, my_coro_gia, 'a', 'b'))

            # print(await i(RunCoro, my_coro_a('a', 'b')))
            # print(await i(RunCoro, my_coro_a, 'a', 'b'))
            
            # print(await i(RunCoro, my_coro_a_implicit('a', 'b')))
            # print(await i(RunCoro, my_coro_a_implicit, 'a', 'b'))
            
            # print(await i(RunCoro, my_coro_a_explicit, 'a', 'b'))
            
            # print(await i(RunCoro, my_coro_asyncio('a', 'b')))
            # print(await i(RunCoro, cs_acoro(my_coro_asyncio), 'a', 'b'))

            # PutCoro

            await i(PutCoro, my_coro_ga('a', 'b'))
            # await i(PutCoro, my_coro_gi, 'a', 'b')
            # # await i(PutCoro, my_coro_gia, 'a', 'b')

            # await i(PutCoro, my_coro_a('a', 'b'))
            # await i(PutCoro, my_coro_a, 'a', 'b')
            
            # await i(PutCoro, my_coro_a_implicit('a', 'b'))
            # await i(PutCoro, my_coro_a_implicit, 'a', 'b')
            
            # await i(PutCoro, my_coro_a_explicit, 'a', 'b')
            
            # await i(PutCoro, my_coro_asyncio('a', 'b'))
            # await i(PutCoro, cs_acoro(my_coro_asyncio), 'a', 'b')
        
        @cs_acoro
        def main():
            i: Interface = current_interface()

            # RunCoro

            print(i(RunCoro, my_coro_ga('a', 'b')))
            # print(i(RunCoro, my_coro_gi, 'a', 'b'))
            # # print(i(RunCoro, my_coro_gia, 'a', 'b'))

            # print(i(RunCoro, my_coro_a('a', 'b')))
            # print(i(RunCoro, my_coro_a, 'a', 'b'))
            
            # print(i(RunCoro, my_coro_a_implicit('a', 'b')))
            # print(i(RunCoro, my_coro_a_implicit, 'a', 'b'))
            
            # print(i(RunCoro, my_coro_a_explicit, 'a', 'b'))
            
            # print(i(RunCoro, my_coro_asyncio('a', 'b')))
            # print(i(RunCoro, cs_acoro(my_coro_asyncio), 'a', 'b'))

            # PutCoro

            i(PutCoro, my_coro_ga('a', 'b'))
            # i(PutCoro, my_coro_gi, 'a', 'b')
            # # i(PutCoro, my_coro_gia, 'a', 'b')

            # i(PutCoro, my_coro_a('a', 'b'))
            # i(PutCoro, my_coro_a, 'a', 'b')
            
            # i(PutCoro, my_coro_a_implicit('a', 'b'))
            # i(PutCoro, my_coro_a_implicit, 'a', 'b')
            
            # i(PutCoro, my_coro_a_explicit, 'a', 'b')
            
            # i(PutCoro, my_coro_asyncio('a', 'b'))
            # i(PutCoro, cs_acoro(my_coro_asyncio), 'a', 'b')
        
        run_in_loop(amain)
        run_in_loop(main)


if __name__ == '__main__':
    main()
