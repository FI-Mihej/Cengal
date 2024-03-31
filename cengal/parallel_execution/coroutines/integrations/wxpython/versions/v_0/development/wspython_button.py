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
# import wx.html2
from cengal.time_management.cpu_clock_cycles import cpu_clock_cycles
from cengal.user_interface.gui.nt.blur_behind import prepare_for_composition
from cengal.hardware.info.cpu import cpu_info

print(cpu_info().is_x86)


tsc_value = cpu_clock_cycles()
print(f"Timestamp Counter Value: {tsc_value}")
from cengal.time_management.high_precision_sync_sleep import hps_sleep
print('start')
# hps_sleep(1.5)
print('end')


class TransparentFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(TransparentFrame, self).__init__(*args, **kwargs)

        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        # Create a device context
        dc = wx.PaintDC(self)
        # Create a graphics context from the device context
        gc = wx.GraphicsContext.Create(dc)

        # Create a semi-transparent red colour
        red = wx.Colour(0, 0, 0, 255)  # RGBA

        # Set the brush for the graphics context
        brush = gc.CreateBrush(wx.Brush(red))
        gc.SetBrush(brush)

        # Get the size of the window
        width, height = self.GetClientSize()

        # Draw a rectangle that covers the entire window
        gc.DrawRectangle(0, 0, width, height)


class TransparentRedPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(TransparentRedPanel, self).__init__(*args, **kwargs)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        
        # Create a vertical box sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # # Create a WebView widget
        # self.browser = wx.html2.WebView.New(self)

        # # Load a webpage
        # self.browser.LoadURL("http://www.google.com")

        # # Add browser to the sizer
        # sizer.Add(self.browser, proportion=1, flag=wx.EXPAND)

        # Set the sizer for the frame
        self.SetSizer(sizer)

    # Make sure CEF finalizes when the frame is destroyed
    def OnClose(self, event):
        # self.browser.CloseBrowser(True)
        self.Destroy()

    def OnPaint(self, event):
        # Create a device context
        dc = wx.PaintDC(self)
        # Create a graphics context from the device context
        gc = wx.GraphicsContext.Create(dc)

        # Create a semi-transparent red colour
        red = wx.Colour(100, 10, 100, 255)  # RGBA

        # Set the brush for the graphics context
        brush = gc.CreateBrush(wx.Brush(red))
        gc.SetBrush(brush)

        # Get the size of the window
        width, height = self.GetClientSize()

        # Draw a rectangle that covers the entire window
        gc.DrawRectangle(0, 0, width, height)


class CustomButton(wx.Panel):
    def __init__(self, parent, id=wx.ID_ANY, label="", pos=wx.DefaultPosition, size=wx.DefaultSize):
        wx.Panel.__init__(self, parent, id, pos, size, style=wx.NO_BORDER)
        self.label = label

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnPress)
        self.Bind(wx.EVT_LEFT_UP, self.OnRelease)
        self.Bind(wx.EVT_ENTER_WINDOW, self.OnEnter)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeave)

        self.hover = False
        self.pressed = False

    def OnPaint(self, event):
        width, height = self.GetSize()
        dc = wx.PaintDC(self)
        gc = wx.GraphicsContext.Create(dc)

        if self.hover:
            if self.pressed:
                brush = wx.Brush("#ee2222")
            else:
                brush = wx.Brush("#ff0000")
        else:
            if self.pressed:
                brush = wx.Brush("#0000ff")
            else:
                brush = wx.Brush("#00ffff")

        gc.SetBrush(brush)
        gc.DrawRoundedRectangle(0, 0, width, height, 0)

        font = self.GetFont()
        gc.SetFont(font, "#000000")

        text_width, text_height = dc.GetTextExtent(self.label)
        gc.DrawText(self.label, (width - text_width) / 2, (height - text_height) / 2)

    def OnPress(self, event):
        self.pressed = True
        self.Refresh()

    def OnRelease(self, event):
        self.pressed = False
        self.Refresh()

    def OnEnter(self, event):
        self.hover = True
        self.Refresh()

    def OnLeave(self, event):
        self.hover = False
        self.pressed = False
        self.Refresh()

    def OnButtonClick(self, event):
        print("Button clicked!")


# usage
app = wx.App()
frame = TransparentFrame(None, -1, "Custom Button Test", size=(500, 400))
prepare_for_composition(frame.GetHandle())
panel = TransparentRedPanel(frame, -1)

# Create a sizer for the main layout
main_sizer = wx.BoxSizer(wx.VERTICAL)

# Add a spacer for the top border
main_sizer.AddSpacer(30)

# Create a horizontal sizer for the panel with left and right borders
h_sizer = wx.BoxSizer(wx.HORIZONTAL)
h_sizer.AddSpacer(4)  # Add a spacer for the left border
h_sizer.Add(panel, 1, flag=wx.EXPAND)
h_sizer.AddSpacer(4)  # Add a spacer for the right border

# Add the horizontal sizer to the main sizer
main_sizer.Add(h_sizer, 1, flag=wx.EXPAND)

# Add a spacer for the bottom border
main_sizer.AddSpacer(4)

# Set the sizer for the frame
frame.SetSizer(main_sizer)

button = CustomButton(panel, -1, "Click me!", pos=(50, 50), size=(80, 30))

frame.Show()
frame.Refresh()
frame.Update()
size = frame.GetSize()
frame.SetSize(size.width + 1, size.height + 1)
frame.SetSize(size.width, size.height)
app.MainLoop()
