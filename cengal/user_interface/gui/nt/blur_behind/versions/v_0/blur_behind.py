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


__all__ = ['prepare_for_composition']


import ctypes
from ctypes import wintypes
from cengal.system import OS_TYPE


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


def prepare_for_composition(hwnd):
    if 'Windows' != OS_TYPE:
        return
    
    dwm = ctypes.windll.dwmapi

    # needs pointertomarginsstruct
    class MARGINS(ctypes.Structure):
        _fields_ = [("cxLeftWidth", ctypes.c_int),
                    ("cxRightWidth", ctypes.c_int),
                    ("cyTopHeight", ctypes.c_int),
                    ("cyBottomHeight", ctypes.c_int)
                    ]
    
    thisWin = hwnd
    
    # if self.is_composition_enabled:
    #     # lt()
    #     margins = MARGINS(-1, 0, 0, 0)
    #     result = dwm.DwmExtendFrameIntoClientArea(thisWin, ctypes.byref(margins))
    # else:
    #     # lt()
    #     margins = MARGINS(0, 0, 0, 0)
    #     result = dwm.DwmExtendFrameIntoClientArea(thisWin, ctypes.byref(margins))
    
    # if 0 == result:
    #     self.is_aero_glass_turned_on = True
    # else:
    #     self.is_aero_glass_turned_on = False

    # --------------------
    
    user32 = ctypes.windll.user32
    
    WCA_ACCENT_POLICY = 19
    ACCENT_ENABLE_BLURBEHIND = 3
    
    class AccentPolicy(ctypes.Structure):
        _fields_ = [
            ('AccentState', wintypes.ULONG),
            ('AccentFlags', wintypes.ULONG),
            ('GradientColor', wintypes.ULONG),
            ('AnimationId', wintypes.ULONG),
        ]
    
    class WINCOMPATTRDATA(ctypes.Structure):
        _fields_ = [
            ('attribute', wintypes.DWORD),
            ('pData', ctypes.POINTER(AccentPolicy)),
            ('dataSize', wintypes.ULONG),
        ]
    
    accent_policy = AccentPolicy(ACCENT_ENABLE_BLURBEHIND, 0, 0, 0)
    wincompattrdata = WINCOMPATTRDATA(WCA_ACCENT_POLICY, ctypes.pointer(accent_policy), ctypes.sizeof(accent_policy))
    
    result = user32.SetWindowCompositionAttribute(thisWin, ctypes.pointer(wincompattrdata))
    
    if 0 != result:
        return None
    else:
        return ctypes.windll.Kernel32.GetLastError()
