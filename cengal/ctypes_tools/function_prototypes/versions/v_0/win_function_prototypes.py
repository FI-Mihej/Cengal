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


__all__ = [
    'SetWindowCompositionAttribute',
    'GetWindowPlacement',
    'MonitorFromWindow',
    'GetMonitorInfoW',
    'ShowWindow',
    'CreateWindowExW',
    'LoadCursorW',
    'RegisterClassExW',
    'GetWindowLongPtrW',
    'SetWindowLongPtrW_LongPtr',
    'SetWindowLongPtrW_WndProc',
    'CallWindowProc',
    'SetWindowPos',
    'ShowWindow',
    'DefWindowProcW',
    'DestroyWindow',
    'PostQuitMessage',
    'GetSystemMetrics',
    'GetWindowRect',
    'GetMessageW',
    'TranslateMessage',
    'DispatchMessageW',
    'MessageBoxW',
    'CreateSolidBrush',
    'DwmSetWindowAttribute',
    'GetCurrentThreadId',
    'GetDpiForWindow',
    'UpdateWindow',
    'SHGetKnownFolderPath',
    'CoTaskMemFree',
]


import ctypes
from ctypes import HRESULT, byref, pointer, wintypes, windll, WINFUNCTYPE
import win32gui, win32con, winerror

from ctypes import sizeof, byref, pointer, POINTER, c_int, c_long, c_longlong, c_ulonglong, c_wchar_p
from ctypes.wintypes import ATOM, COLORREF, HANDLE, HBRUSH, HINSTANCE, HMENU, HWND, BOOL, HMONITOR, DWORD, LPCVOID, LPCWSTR, LPMSG, LPRECT, LPVOID, LONG, MSG, RGB, UINT, WPARAM, LPARAM, HHOOK
from win32con import IDC_ARROW, CS_HREDRAW, CS_VREDRAW, GWL_STYLE, GWL_WNDPROC, SWP_FRAMECHANGED, SWP_NOMOVE, SWP_NOSIZE, SWP_NOZORDER, SW_SHOW, SM_CXFRAME, SM_CYFRAME


from cengal.ctypes_tools.types import *
from cengal.ctypes_tools.libraries import user32, gdi32, dwmapi, kernel32, shell32, ole32
from cengal.ctypes_tools.tools import cwfunc_def


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


SetWindowCompositionAttribute = cwfunc_def(user32, 'SetWindowCompositionAttribute', (HWND, POINTER(WINCOMPATTRDATA)), BOOL)
GetWindowPlacement = cwfunc_def(user32, 'GetWindowPlacement', (HWND, POINTER(WINDOWPLACEMENT)), BOOL)
MonitorFromWindow = cwfunc_def(user32, 'MonitorFromWindow', (HWND, DWORD), HMONITOR)
GetMonitorInfoW = cwfunc_def(user32, 'GetMonitorInfoW', (HMONITOR, POINTER(MONITORINFO)), BOOL)
ShowWindow = cwfunc_def(user32, 'ShowWindow', (HWND, c_int), BOOL)
CreateWindowExW = cwfunc_def(user32, 'CreateWindowExW', (DWORD, LPCWSTR, LPCWSTR, DWORD, c_int, c_int, c_int, c_int, HWND, HMENU, HINSTANCE, LPVOID), HWND)
LoadCursorW = cwfunc_def(user32, 'LoadCursorW', (HINSTANCE, LPCWSTR), HCURSOR)
RegisterClassExW = cwfunc_def(user32, 'RegisterClassExW', (POINTER(WNDCLASSEXW),), ATOM)
GetWindowLongPtrW = cwfunc_def(user32, 'GetWindowLongPtrW', (HWND, c_int), LONG_PTR)
SetWindowLongPtrW_LongPtr = cwfunc_def(user32, 'SetWindowLongPtrW', (HWND, c_int, LONG_PTR), LONG_PTR)
SetWindowLongPtrW_WndProc = cwfunc_def(user32, 'SetWindowLongPtrW', (HWND, c_int, WNDPROC), WNDPROC)
CallWindowProc = cwfunc_def(user32, 'CallWindowProcW', (WNDPROC, HWND, UINT, WPARAM, LPARAM), LRESULT)
SetWindowPos = cwfunc_def(user32, 'SetWindowPos', (HWND, HWND, c_int, c_int, c_int, c_int, UINT), BOOL)
ShowWindow = cwfunc_def(user32, 'ShowWindow', (HWND, c_int), BOOL)
DefWindowProcW = cwfunc_def(user32, 'DefWindowProcW', (HWND, UINT, WPARAM, LPARAM), LRESULT)
DestroyWindow = cwfunc_def(user32, 'DestroyWindow', (HWND,), BOOL)
PostQuitMessage = cwfunc_def(user32, 'PostQuitMessage', (c_int,), None)
GetSystemMetrics = cwfunc_def(user32, 'GetSystemMetrics', (c_int,), c_int)
GetWindowRect = cwfunc_def(user32, 'GetWindowRect', (HWND, LPRECT), BOOL)
GetMessageW = cwfunc_def(user32, 'GetMessageW', (LPMSG, HWND, UINT, UINT), BOOL)
TranslateMessage = cwfunc_def(user32, 'TranslateMessage', (POINTER(MSG),), BOOL)
DispatchMessageW = cwfunc_def(user32, 'DispatchMessageW', (POINTER(MSG),), LRESULT)
MessageBoxW = cwfunc_def(user32, 'MessageBoxW', (HWND, LPCWSTR, LPCWSTR, UINT), c_int)
CreateSolidBrush = cwfunc_def(gdi32, 'CreateSolidBrush', (COLORREF,), HBRUSH)
DwmSetWindowAttribute = cwfunc_def(dwmapi, 'DwmSetWindowAttribute', (HWND, DWORD, LPCVOID, DWORD), HRESULT)
# SetWindowsHookEx = cwfunc_def(user32, SetWindowsHookExW, (c_int, WINFUNCTYPE, HINSTANCE, DWORD), HHOOK)
GetCurrentThreadId = cwfunc_def(kernel32, 'GetCurrentThreadId', tuple(), DWORD)
GetDpiForWindow = cwfunc_def(user32, 'GetDpiForWindow', (HWND,), UINT)
UpdateWindow = cwfunc_def(user32, 'UpdateWindow', (HWND,), BOOL)
SHGetKnownFolderPath = cwfunc_def(shell32, 'SHGetKnownFolderPath', (POINTER(GUID), DWORD, HANDLE, POINTER(c_wchar_p)), HRESULT)
CoTaskMemFree = cwfunc_def(ole32, 'CoTaskMemFree', (LPVOID,), None)
