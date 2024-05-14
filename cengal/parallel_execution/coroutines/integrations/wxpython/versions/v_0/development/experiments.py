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
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.parallel_execution.coroutines.coro_scheduler import CoroScheduler, CoroSchedulerType, Interface, Coro, AnyWorker, current_interface, current_coro_scheduler, cs_coro, cs_acoro
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import CoroPriority
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
from cengal.parallel_execution.coroutines.coro_tools.await_coro import cs_awaitable
from cengal.parallel_execution.coroutines.integrations.wxpython import CoroApp, wx_exec_in_coro, event_handler, aevent_handler, asyncio_event_handler, event_handler_implicit, blocking_event_handler_implicit, bind_asyncio_coro, bind_coro, bind_coro_explicit, abind_coro_explicit, asyncio_bind_coro_explicit, bind_to, bind
from cengal.data_generation.id_generator import IDGenerator

from datetime import datetime

import wx
import sys
import asyncio


class MyDialog(wx.Dialog):
    def __init__(self, parent):
        super(MyDialog, self).__init__(parent, title='My Dialog', pos=(400, 400), size=(300, 200))
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text = wx.StaticText(self, label='Dialog opened!')
        sizer.Add(self.text, 0, wx.ALL, 10)
        self.SetSizer(sizer)
        # self.Centre()  # Position the dialog in the center of the screen


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        super(MyFrame, self).__init__(parent, id, 'My Frame', pos=(400, 400), size=(300, 200))

        # Creating a box sizer
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Creating a static text and adding it to sizer
        self.text = wx.StaticText(self, label='')
        self.sizer.Add(self.text, 0, wx.ALL, 10)

        # Creating a static text and adding it to sizer
        self.text2 = wx.StaticText(self, label='')
        self.sizer.Add(self.text2, 0, wx.ALL, 10)

        # Creating a button and adding it to sizer
        self.button = wx.Button(self, label='Click me!')
        # self.button.Bind(wx.EVT_BUTTON, self.OnButton)
        # self.button.Bind(wx.EVT_BUTTON, bind(self.OnButton))
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)
        self.sizer.Add(self.button, 0, wx.ALL, 10)

        # Setting the sizer to the frame
        self.SetSizer(self.sizer)

        # self.Centre()  # Position the dialog in the center of the screen

        # bind_asyncio_coro(self, self.background_task())
        bind_coro(self, self.background_task)
        # bind_coro(self, self.background_task_2, 5)
        bind_coro_explicit(self, self.background_task_2(5))

    # @event_handler
    @asyncio_event_handler
    async def OnButton(self, event):
        # This function will be called when the button is clicked.
        await asyncio.sleep(2)
        self.text2.SetLabel(f'Button clicked at {datetime.now()}')
        await asyncio_bind_coro_explicit(self, self.background_task_2(5))
    
    async def background_task(self):
        while True:
            await asyncio.sleep(0.250)
            self.text.SetLabel(str(datetime.now()))
    
    async def background_task_2(self, iter_num: int):
        while iter_num >= 0:
            await asyncio.sleep(0.250)
            print(f'{iter_num=}')
            iter_num -= 1


class MyApp(CoroApp):
    def __init__(self, default_priority: CoroPriority = CoroPriority.normal):
        super().__init__(default_priority)
        self.dialog_opened: bool = False
    
    def OnInit(self):
        super().OnInit()
        self.frame = MyFrame(parent=None, id=-1)
        self.frame.Show()
        self.index_0 = IDGenerator()
        self.index_1 = IDGenerator()
        self.index_2 = IDGenerator()

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        # self.Bind(wx.EVT_TIMER, bind(self.OnTimer), self.timer)
        # self.Bind(wx.EVT_TIMER, bind(self.on_timer), self.timer)
        # self.Bind(wx.EVT_TIMER, bind_to(self, self.on_timer), self.timer)
        # self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        # self.Bind(wx.EVT_TIMER, bind(self.on_timer_blocking), self.timer)
        self.timer.Start(1000) # run every 1 second
        return True

    def OnTimer(self, event):
        if not self.dialog_opened:
            self.dialog_opened = True
            self.dialog = MyDialog(self.frame)
            self.dialog.ShowModal()
            self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)

        # code to execute periodically goes here
        index = self.index_2()
        print(f'OnTimer >> {datetime.now()}; {index}>> before sleep')
        i: Interface = current_interface()
        i(Sleep, 1)
        print(f'OnTimer >> {datetime.now()}; {index}>> after sleep')

    @event_handler_implicit
    async def on_timer(self, event):
        # if not self.dialog_opened:
        #     self.dialog_opened = True
        #     self.dialog = MyDialog(self.frame)
        #     self.dialog.ShowModal()

        # code to execute periodically goes here
        index = self.index_0()
        print(f'on_timer >> {datetime.now()}; {index}>> before sleep')
        await asyncio.sleep(0.3)
        print(f'on_timer >> {datetime.now()}; {index}>> after sleep')

    @blocking_event_handler_implicit
    async def on_timer_blocking(self, event):
        # if not self.dialog_opened:
        #     self.dialog_opened = True
        #     self.dialog = MyDialog(self.frame)
        #     self.dialog.ShowModal()

        # code to execute periodically goes here
        index = self.index_1()
        print(f'on_timer_blocking >> {datetime.now()}; {index}>> before sleep')
        await asyncio.sleep(0.5)
        print(f'on_timer_blocking >> {datetime.now()}; {index}>> after sleep')


@wx_exec_in_coro
def main():
    app = MyApp()
    return app


if __name__ == "__main__":
    sys.exit(run_in_loop(main))
