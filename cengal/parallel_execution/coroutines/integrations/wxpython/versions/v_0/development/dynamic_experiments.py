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
__version__ = "4.3.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import wx

class MyDialog(wx.Dialog):
    def __init__(self, parent):
        super(MyDialog, self).__init__(parent, title='My Dialog')
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text = wx.StaticText(self, label='Dialog opened!')
        sizer.Add(self.text, 0, wx.ALL, 10)
        self.SetSizer(sizer)

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        super(MyFrame, self).__init__(parent, id, 'My Frame')
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        # Creating a box sizer
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Creating a static text and adding it to sizer
        self.text = wx.StaticText(self, label='Hello, this is my frame!')
        self.sizer.Add(self.text, 0, wx.ALL, 10)

        # Setting the sizer to the frame
        self.SetSizer(self.sizer)

    def OnClose(self, event):
        # This function will be called when the frame is closing.
        print('Frame is closing.')
        event.Skip()  # Ensure the event is still processed

class MyApp(wx.App):
    def __init__(self, param1, param2):
        super(MyApp, self).__init__()
        self.param1 = param1
        self.param2 = param2

    def OnInit(self):
        self.frame = MyFrame(parent=None, id=-1)
        self.frame.Show()

        self.dialog = MyDialog(self.frame)
        self.dialog.ShowModal()

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.timer.Start(1000) # run every 1 second

        return True

    def OnExit(self):
        print('Application is exiting.')
        # Add cleanup code here if needed
        return 0

    def OnTimer(self, event):
        # code to execute periodically goes here
        print('Timer event!', self.param1, self.param2)


def main():
    app = MyApp('parameter1', 'parameter2')
    app.MainLoop()


if __name__ == '__main__':
    main()
