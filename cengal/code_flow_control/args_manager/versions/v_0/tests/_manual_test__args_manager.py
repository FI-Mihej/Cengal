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


import justpy as jp
from justpy_components import *
from pprint import pprint
from typing import NoReturn, Union, Optional, Dict, List, Type, Callable, Sequence
from time import perf_counter
# from cengal.parallel_execution.coroutines import *
from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import LoopYieldPriorityScheduler, CoroPriority, gly, agly
from cengal.parallel_execution.coroutines.coro_standard_services.timer_coro_runner import TimerCoroRunner
# from cengal.parallel_execution.coroutines.coro_standard_services.
# from cengal.parallel_execution.coroutines.coro_standard_services.
from cengal.parallel_execution.coroutines.coro_tools.await_coro import RunSchedulerInAsyncioLoop
from cengal.code_flow_control.args_manager import ArgsManager, EArgs
from random import randint
from time import perf_counter
from justpy_coro_helpers import coro_interfaces


Numeric = Union[int, float, complex]


# def hello_world():
#     wp = jp.WebPage()
#     jp.Hello(a=wp)
#     return wp

# jp.justpy(hello_world)

@event_handler(False)
def my_click(self, msg):
    self.text = 'I was clicked'


def event_demo():
    wp = jp.WebPage()
    d = jp.Div(text='Not clicked yet', a=wp, classes='w-48 text-xl m-2 p-1 bg-blue-500 text-white')
    d.on('click', my_click)
    return wp


theme: Theme = {
    jp.Button: 'bg-white hover:bg-gray-100 text-gray-800 font-semibold py-1 px-2 border border-gray-400 rounded-l shadow',
    jp.Label: 'bg-gray-200 text-gray-800 font-semibold py-1 px-2 border border-gray-400 rounded-r shadow',
    jp.Input: 'shadow appearance-none border rounded-l w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline h-auto',
    jp.P: 'text-gray-800 border border-gray-400 rounded-r shadow w-full h-full overflow-y-scroll',
}


class ClickableDiv(Component):
    def __init__(self, *args, **kwargs):
        self.cd = None
        if 'dtext' in kwargs:
            self.dtext = kwargs['dtext']
            del kwargs['dtext']
        super().__init__(*args, **kwargs)
    
    def init(self):
        self.html = self.theme(jp.Div, classes='-- w-auto h-auto')
        self.cd = self.theme(jp.Div, a=self.html, text='Not clicked yet', classes='w-48 h-auto text-xl mt-2 ml-2 mr-2 p-1 bg-blue-500 text-white rounded-t')
        self.cd.on('click', self.on_click)
        self.theme(jp.Div, a=self.html, text=self.dtext, classes='w-48 h-auto text-xl mb-2 ml-2 mr-2 p-1 bg-gray-500 text-white rounded-b')
    
    @event_handler()
    def on_click(self, item, msg):
        self.cd.text =  f'I was clicked: {str(item)}'


class AClickableDiv(Component):
    # def __init__(self, parent: Optional[Container], coro_scheduler: CoroScheduler, theme: Optional[ArgsManager]=None, dtext: Optional[str]=None):
    def __init__(self, parent: Optional[Container], await_coro_fast: Callable, await_task_fast: Callable, theme: Optional[ArgsManager]=None, dtext: Optional[str]=None):
        # self.cd = None
        # self.cs = coro_scheduler
        # # self.acf = ArgsManager(
        # #     EArgs(jp.asyncio.get_event_loop(), self.cs, CoroType.auto),
        # # )
        # self.await_coro_fast = ArgsManager(
        #     EArgs(jp.asyncio.get_event_loop(), self.cs, CoroType.auto),
        # ).callable(await_coro_fast)
        self.await_coro_fast: Callable = await_coro_fast
        self.await_task_fast: Callable = await_task_fast
        self.dtext = dtext
        self.click_counter = 0
        super().__init__(parent, theme)

    def init(self):
        self.html = self.theme(jp.Div, classes='-- w-auto h-auto')
        self.cd = self.theme(jp.Div, a=self.html, text='Click me!', classes='select-none w-48 h-auto text-xl mt-2 ml-2 mr-2 p-1 bg-blue-500 text-white rounded-t')
        # self.cd.on('click', self.on_click)
        # self.cd.on('click', AsyncEventHandlerRunner(self.on_click_ahandler))
        # self.cd.on('click', async_handle_runner(self.on_click_ahandler))
        self.cd.on('click', self.on_click_ahandler)
        self.theme(jp.Div, a=self.html, text=self.dtext, classes='w-48 h-auto text-xl mb-2 ml-2 mr-2 p-1 bg-gray-500 text-white rounded-b')
    
    @event_handler()
    async def on_click(self, item, msg):
        # print(f'{perf_counter()} > 0 - {item}')
        # self.cd.text = f'Waiting...'
        # print(f'{perf_counter()} > 1 - {item}')
        # await msg.page.update()
        # print(f'{perf_counter()} > 2 - {item}')
        # await jp.asyncio.sleep(5)
        # print(f'{perf_counter()} > 3 - {item}')
        # self.cd.text =  f'Sum: {20 + self.click_counter}'
        # print(f'{perf_counter()} > 4 - {item}')
        # await msg.page.update()
        # print(f'{perf_counter()} > 5 - {item}')
        # self.click_counter += 1
        # print(f'{perf_counter()} > 6 - {item}')
        # # coro_future = await_coro_fast(jp.asyncio.get_event_loop(), self.cs, CoroType.greenlet, AClickableDiv.on_click_coro, self)
        # # result = await coro_future
        # # self.cd.text =  f'Sum: {result}'
        jp.run_task(self.on_click_ahandler(item, msg))
    
    @staticmethod
    def add_coro(interface, a, b, item):
        print(f'{perf_counter()} > 4 - {item}')
        result = a + b
        print(f'{perf_counter()} > 5 - {item}')
        interface(Sleep, 2)
        print(f'{perf_counter()} > 6 - {item}')
        return result
    
    @staticmethod
    def on_click_coro(interface: Interface, self, item):
        print(f'{perf_counter()} > 2 - {item}')
        # interface(Sleep, 0.5)
        print(f'{perf_counter()} > 3 - {item}')
        cc = self.click_counter
        self.click_counter += 1
        result = interface(RunCoro, CoroType.auto, AClickableDiv.add_coro, 10, cc, item)
        print(f'{perf_counter()} > 7 - {item}')
        print(f'{perf_counter()} > 8 - {item}')
        return result
    
    @staticmethod
    async def on_click_handler(interface: Interface, self, item, msg):
        print(f'{perf_counter()} > 1 - {item}')
        result = await interface(RunCoro, CoroType.auto, AClickableDiv.on_click_coro, self, item)
        print(f'{perf_counter()} > 9 - {item}')
        self.cd.text =  f'_PreSum: {result}'
        print(f'{perf_counter()} > 10 - {item}')
        return result
    
    @staticmethod
    def on_click_handler_green(interface: Interface, self, item, msg):
        print(f'{perf_counter()} > 1 - {item}')
        result = interface(RunCoro, CoroType.auto, AClickableDiv.on_click_coro, self, item)
        print(f'{perf_counter()} > 9 - {item}')
        self.cd.text =  f'_PreSum: {result}'
        print(f'{perf_counter()} > 10 - {item}')
        return result

    @event_handler()
    async def on_click_ahandler(self, item, msg):
        print(f'{perf_counter()} > 0 - {item}')
        self.cd.text = 'Clicked...'
        await msg.page.update()
        # self.cs.put_coro(AClickableDiv.on_click_handler, self, item, msg)
        # result = await await_coro_fast(jp.asyncio.get_event_loop(), self.cs, CoroType.auto, AClickableDiv.on_click_handler, self, item, msg)
        # result = await await_coro_fast(jp.asyncio.get_event_loop(), self.cs, CoroType.auto, AClickableDiv.on_click_handler_green, self, item, msg)
        # result = await self.acf(await_coro_fast(AClickableDiv.on_click_handler_green, self, item, msg))
        # result = await self.await_coro_fast(AClickableDiv.on_click_handler, self, item, msg)
        # result = await self.await_coro_fast(AClickableDiv.on_click_handler_green, self, item, msg)
        def handler(interface: Interface, self, item, msg):
            print(f'{perf_counter()} > 1 - {item}')
            result = interface(RunCoro, CoroType.auto, AClickableDiv.on_click_coro, self, item)
            print(f'{perf_counter()} > 9 - {item}')
            self.cd.text =  f'_PreSum: {result}'
            print(f'{perf_counter()} > 10 - {item}')
            return result
        result = await self.await_coro_fast(handler, self, item, msg)
        print(f'{perf_counter()} > 11 - {item}')
        await msg.page.update()
        await jp.asyncio.sleep(2)
        self.cd.text = f'Sum: {result}'
        await msg.page.update()
        print(f'{perf_counter()} > 12 - {item}')


class Screen(Component):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def init(self):
        self.html = self.container = self.theme(jp.Div, classes='-- h-screen flex')


class Pannels(Component):
    def __init__(self, *args, **kwargs):
        if 'pan_l_classes' in kwargs:
            self.pan_l_classes = kwargs['pan_l_classes']
            del kwargs['pan_l_classes']
        super().__init__(*args, **kwargs)
    
    def init(self):
        self.html = self.theme(jp.Div, classes='-- h-full flex')
        self.containers['pan_l'] = self.theme(jp.Div, a=self.html, classes='-- h-auto overflow-y-auto '+self.pan_l_classes)
        pan_r_holder = self.theme(jp.Div, a=self.html, classes='-- flex-1 flex overflow-hidden')
        self.container = self.containers['pan_r'] = self.theme(jp.Div, a=pan_r_holder, classes='-- flex-1 overflow-y-auto')

# GLOBAL_LOOPER = None

class Looper:
    def __init__(self):
        self.external_loop = jp.asyncio.get_event_loop()
        self.cs = CoroScheduler()
        self.configure_coro_scheduler()
        self.iter_num = 0
        self.delta_num = 0
        self.register_looper()
        self.rs = RunSchedulerInAsyncioLoop(self.cs, 0.020, self.external_loop)
        self.rs.register()
    
    def register_looper(self):
        self.external_loop.call_soon(self.looper, self.external_loop, 0, 0.0, 0)
    
    def looper(self, loop, iter_num: int, last_rendering_time: float, last_renderred_num: int):
        current_time = perf_counter()
        if 1.0 <= (current_time - last_rendering_time):
            last_rendering_time = current_time
            delta_num = iter_num - last_renderred_num
            last_renderred_num = iter_num
            self.iter_num = iter_num
            self.delta_num = delta_num
            print(f'<><><> Looper <><><> iteration id: {iter_num}; iteration delta: {delta_num} <><><>')
        loop.call_soon(self.looper, loop, iter_num + 1,last_rendering_time, last_renderred_num)
    
    def make_sum(self, interface: Interface, a: Numeric, b: Numeric) -> Numeric:
        print('Greenlet')
        interface(Sleep, 1)
        ly = gly(CoroPriority.normal)
        result = 0
        for i in range(randint(1, 100000)):
            result += a + b + i
            ly()
        return result
    
    async def amake_sum(self, interface: Interface, a: Numeric, b: Numeric) -> Numeric:
        print('Awaitable')
        await interface(Sleep, 1)
        ly = await agly(CoroPriority.normal)
        result = 0
        for i in range(randint(1, 100000)):
            result += a + b + i
            await ly()
        return result

    def main_coro(self, interface: Interface):
        last_cs = interface._loop.context_switches
        while True:
            # res = interface(RunCoro, CoroType.greenlet, self.make_sum, self.iter_num, self.delta_num)
            # res = interface(RunCoro, CoroType.awaitable, self.amake_sum, self.iter_num, self.delta_num)
            coro_list = (self.make_sum, self.amake_sum)
            chosen_coro = coro_list[randint(0, len(coro_list) - 1)]
            res = interface(RunCoro, CoroType.auto, chosen_coro, self.iter_num, self.delta_num)
            print(f'<><><> CORO <><><> iteration id: {self.iter_num}; iteration delta: {self.delta_num}; sum: {res}; delta context switches: {interface._loop.context_switches - last_cs} <><><>')
            last_cs = interface._loop.context_switches
            interface(Sleep, 2)
            for i in range(randint(1, 25000)):
                result = self.iter_num + self.delta_num
                gly(CoroPriority.normal)()

    def configure_coro_scheduler(self):
        self.cs.register_service(RunCoro)
        self.cs.register_service(LoopYieldPriorityScheduler)
        self.cs.register_service(TimerCoroRunner)
        self.cs.register_service(Sleep)
        self.cs.register_service(RunCoro)
        self.cs.put_coro(self.main_coro)


# def components_demo():
#     Looper()
    
#     # pprint(globals())
    
#     tm = ThemeManager(theme)
#     wp = jp.WebPage()
    
#     screen = tm(Screen, wp)
    
#     tm(ClickableDiv, screen, dtext='0')
#     main_pannel = tm(Pannels, screen, pan_l_classes='w-auto')
#     tm(ClickableDiv, main_pannel, dtext='1')
#     tm(ClickableDiv, main_pannel.containers['pan_l'], dtext='2.0')
#     tm(ClickableDiv, main_pannel.containers['pan_l'], dtext='2.1')
#     tm(ClickableDiv, main_pannel.containers['pan_l'], dtext='2.2')
#     tm(ClickableDiv, main_pannel.containers['pan_l'], dtext='2.3')
#     tm(ClickableDiv, main_pannel.containers['pan_l'], dtext='2.4')
#     tm(ClickableDiv, main_pannel.containers['pan_l'], dtext='2.5')
#     tm(ClickableDiv, main_pannel.containers['pan_l'], dtext='2.6')
    
#     limiter = jp.Div(a=main_pannel.container, classes="h-24")
#     # limiter = jp.Div(a=main_pannel.container, classes="h-auto")
    
#     sub_pannel = tm(Pannels, limiter, pan_l_classes='w-auto')
#     tm(ClickableDiv, sub_pannel, dtext='3')
#     tm(ClickableDiv, sub_pannel, dtext='4')
#     tm(ClickableDiv, sub_pannel, dtext='5')
#     tm(ClickableDiv, sub_pannel, dtext='6')
#     tm(ClickableDiv, sub_pannel, dtext='7')
#     tm(ClickableDiv, sub_pannel, dtext='8')
#     tm(ClickableDiv, sub_pannel, dtext='9')
#     tm(ClickableDiv, sub_pannel, dtext='10')
#     tm(ClickableDiv, sub_pannel, dtext='11')
#     tm(ClickableDiv, sub_pannel.containers['pan_l'], dtext='12')
#     tm(ClickableDiv, sub_pannel.containers['pan_l'], dtext='13')
#     tm(ClickableDiv, sub_pannel.containers['pan_l'], dtext='14')

#     tm(ClickableDiv, main_pannel, dtext='15')
#     # f1 = tm(ClickableDiv, wp, dtext='16')
#     # tm(ClickableDiv, f1, dtext='17')
#     return wp

# jp.justpy(components_demo)

async def acomponents_demo():
    # global GLOBAL_LOOPER
    # GLOBAL_LOOPER = Looper()
    
    # pprint(globals())

    external_loop = jp.asyncio.get_event_loop()
    cs = CoroScheduler()
    cs.register_service(RunCoro)
    cs.register_service(LoopYieldPriorityScheduler)
    cs.register_service(TimerCoroRunner)
    cs.register_service(Sleep)
    cs.register_service(RunCoro)
    rs = RunSchedulerInAsyncioLoop(cs, 0.020, external_loop)
    rs.register()
    
    # lp = Looper()
    # cs = lp.cs
    
    tm = ArgsManager(
        ThemeArgsManager(theme)
    )
    am = ArgsManager(
        ThemeArgsManager(theme),
        coro_interfaces(cs)
    )
    
    wp = jp.WebPage()
    
    screen = tm(Screen, wp)
    
    am(AClickableDiv, screen, dtext='0')
    main_pannel = tm(Pannels, screen, pan_l_classes='w-auto')
    am(AClickableDiv, main_pannel, dtext='1')
    am(AClickableDiv, main_pannel.containers['pan_l'], dtext='2.0')
    am(AClickableDiv, main_pannel.containers['pan_l'], dtext='2.1')
    am(AClickableDiv, main_pannel.containers['pan_l'], dtext='2.2')
    am(AClickableDiv, main_pannel.containers['pan_l'], dtext='2.3')
    am(AClickableDiv, main_pannel.containers['pan_l'], dtext='2.4')
    am(AClickableDiv, main_pannel.containers['pan_l'], dtext='2.5')
    am(AClickableDiv, main_pannel.containers['pan_l'], dtext='2.6')
    
    limiter = jp.Div(a=main_pannel.container, classes="h-24")
    # limiter = jp.Div(a=main_pannel.container, classes="h-auto")
    
    sub_pannel = tm(Pannels, limiter, pan_l_classes='w-auto')
    am(AClickableDiv, sub_pannel, dtext='3')
    am(AClickableDiv, sub_pannel, dtext='4')
    am(AClickableDiv, sub_pannel, dtext='5')
    am(AClickableDiv, sub_pannel, dtext='6')
    am(AClickableDiv, sub_pannel, dtext='7')
    am(AClickableDiv, sub_pannel, dtext='8')
    am(AClickableDiv, sub_pannel, dtext='9')
    am(AClickableDiv, sub_pannel, dtext='10')
    am(AClickableDiv, sub_pannel, dtext='11')
    am(AClickableDiv, sub_pannel.containers['pan_l'], dtext='12')
    am(AClickableDiv, sub_pannel.containers['pan_l'], dtext='13')
    am(AClickableDiv, sub_pannel.containers['pan_l'], dtext='14')

    am(AClickableDiv, main_pannel, dtext='15')
    # f1 = am(AClickableDiv, wp, dtext='16')
    # am(AClickableDiv, f1, dtext='17')
    return wp

jp.justpy(acomponents_demo)


# def pannel_demo():
#     tm = ThemeManager(theme)
#     wp = jp.WebPage()
#     screen = tm(Screen, wp)
#     tm(ClickableDiv, screen)
#     main_pannel = tm(Pannels, screen)
#     tm(ClickableDiv, main_pannel)
#     tm(ClickableDiv, main_pannel.containers['pan_l'])
#     return wp

# jp.justpy(pannel_demo)


