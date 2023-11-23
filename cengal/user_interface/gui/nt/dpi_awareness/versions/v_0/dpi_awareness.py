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


__all__ = ['ProcessDpiAwareness', 'set_dpi_awareness']


import os
from enum import IntEnum


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


"""
https://stackoverflow.com/questions/41315873/attempting-to-resolve-blurred-tkinter-text-scaling-on-windows-10-high-dpi-disp
https://stackoverflow.com/questions/44398075/can-dpi-scaling-be-enabled-disabled-programmatically-on-a-per-session-basis

typedef enum _PROCESS_DPI_AWARENESS { 
    PROCESS_DPI_UNAWARE = 0,
    /*  DPI unaware. This app does not scale for DPI changes and is
        always assumed to have a scale factor of 100% (96 DPI). It
        will be automatically scaled by the system on any other DPI
        setting. */

    PROCESS_SYSTEM_DPI_AWARE = 1,
    /*  System DPI aware. This app does not scale for DPI changes.
        It will query for the DPI once and use that value for the
        lifetime of the app. If the DPI changes, the app will not
        adjust to the new DPI value. It will be automatically scaled
        up or down by the system when the DPI changes from the system
        value. */

    PROCESS_PER_MONITOR_DPI_AWARE = 2
    /*  Per monitor DPI aware. This app checks for the DPI when it is
        created and adjusts the scale factor whenever the DPI changes.
        These applications are not automatically scaled by the system. */
} PROCESS_DPI_AWARENESS;
"""


class ProcessDpiAwareness(IntEnum):
    process_dpi_unaware = 0
    process_system_dpi_aware = 1
    process_per_monitor_dpi_aware = 2


def set_dpi_awareness(process_dpi_awareness: ProcessDpiAwareness):
    if 'nt' != os.name:
        return
    
    from ctypes import c_int, windll, byref
    from platform import win32_ver

    # Query DPI Awareness (Windows 10 and 8)
    awareness = c_int()
    errorCode = windll.shcore.GetProcessDpiAwareness(0, byref(awareness))
    # print(awareness.value)

    windows_major_version, _, _, _ = win32_ver()
    if windows_major_version in {'8', '10'}:
        # Set DPI Awareness  (Windows 10 and 8)
        errorCode = windll.shcore.SetProcessDpiAwareness(int(process_dpi_awareness))
        # the argument is the awareness level, which can be 0, 1 or 2:
        # for 1-to-1 pixel control I seem to need it to be non-zero (I'm using level 2)
    else:
        # Set DPI Awareness  (Windows 7 and Vista)
        success = windll.user32.SetProcessDPIAware()
        # behaviour on later OSes is undefined, although when I run it on my Windows 10 machine, it seems to work with effects identical to SetProcessDpiAwareness(1)
