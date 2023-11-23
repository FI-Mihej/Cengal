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


__all__ = ['LONG_PTR', 'UINT_PTR', 'LRESULT', 'GWLP_USERDATA', 'HCURSOR', 'PointerToID', 'WNDPROC', 'CALLWNDPROC', 'MARGINS', 'ACCENT_POLICY', 'WINCOMPATTRDATA', 'WINDOWPLACEMENT', 'PWINDOWPLACEMENT', 'LPWINDOWPLACEMENT', 'MONITORINFO', 'LPMONITORINFO', 'WNDCLASSEXW', 'PWNDCLASSEXW', 'WNDCLASS', 'CREATESTRUCTW', 'LPCREATESTRUCTW', 'WINDOWPOS', 'LPWINDOWPOS', 'PWINDOWPOS', 'NCCALCSIZE_PARAMS', 'LPNCCALCSIZE_PARAMS', 'STYLESTRUCT', 'LPSTYLESTRUCT', 'GUID']

import ctypes
from ctypes import wintypes, windll, WINFUNCTYPE
import win32gui, win32con, winerror
from enum import Enum, IntEnum
from time import sleep
from typing import Sequence, Dict, Optional
from cengal.data_generation.id_generator import IDGenerator

from ctypes import sizeof, byref, pointer, POINTER, c_int, c_long, c_longlong, c_ulonglong, c_uint, Structure, c_void_p
from ctypes.wintypes import ATOM, COLORREF, HANDLE, HBRUSH, HINSTANCE, HMENU, HWND, BOOL, HMONITOR, DWORD, WORD, BYTE, LPCVOID, LPCWSTR, LPMSG, LPRECT, LPVOID, LONG, MSG, RGB, UINT, WPARAM, LPARAM, HHOOK, ULONG, POINT, RECT, HICON, LPCSTR
from win32con import IDC_ARROW, CS_HREDRAW, CS_VREDRAW, GWL_STYLE, GWL_WNDPROC, SWP_FRAMECHANGED, SWP_NOMOVE, SWP_NOSIZE, SW_SHOW, SM_CXFRAME, SM_CYFRAME, GWL_USERDATA

from uuid import UUID


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


LONG_PTR = LPARAM
UINT_PTR = WPARAM
LRESULT = LONG_PTR

GWLP_USERDATA = GWL_USERDATA
# LONG_PTR = POINTER(wintypes.LPARAM)
# LONG_PTR = wintypes.LPARAM
# UINT_PTR = wintypes.WPARAM
# LRESULT = wintypes.LPARAM
# TRUE = win32con.TRUE
# FALSE = win32con.FALSE


# SW_SHOW = win32con.SW_SHOW


HCURSOR = HICON

PointerToID = POINTER(c_long)


# WNDPROC = ctypes.WINFUNCTYPE(c_int, c_long, c_int, c_int, c_int)
# WNDPROC = ctypes.WINFUNCTYPE(c_int, HWND, c_uint, wintypes.WPARAM, wintypes.LPARAM)
WNDPROC = ctypes.WINFUNCTYPE(LRESULT,  # return Value
                              HWND,     # First Param, the handle
                              UINT,     # second Param, message id
                              WPARAM,   # third param, additional message info (depends on message id)
                              LPARAM,   # fourth param, additional message info (depends on message id)
)
CALLWNDPROC = ctypes.WINFUNCTYPE(LRESULT, c_int, WPARAM, LPARAM)


# === STRUCTURES ===============================================================

# needs pointertomarginsstruct
class MARGINS(Structure):
    _fields_ = [("cxLeftWidth", c_int),
                ("cxRightWidth", c_int),
                ("cyTopHeight", c_int),
                ("cyBottomHeight", c_int)
                ]


# class ACCENTPOLICY(Structure):
#     _fields_ = [
#         ('AccentState', ULONG),
#         ('AccentFlags', ULONG),
#         ('GradientColor', ULONG),
#         ('AnimationId', ULONG),
#     ]
class ACCENT_POLICY(ctypes.Structure):
    _fields_ = [
        ("AccentState", wintypes.DWORD),
        ("AccentFlags", wintypes.DWORD),
        ("GradientColor", wintypes.DWORD),
        ("AnimationId", wintypes.DWORD),
        ("GradientAlpha", wintypes.DWORD),
        ("BlurPolicy", wintypes.DWORD),
    ]


class WINCOMPATTRDATA(Structure):
    _fields_ = [
        ('attribute', DWORD),
        ('pData', POINTER(ACCENT_POLICY)),
        ('dataSize', ULONG),
    ]


class WINDOWPLACEMENT(Structure):
    _fields_ = [
        ('length', UINT),
        ('flags', UINT),
        ('showCmd', UINT),
        ('ptMinPosition', POINT),
        ('ptMaxPosition', POINT),
        ('rcNormalPosition', RECT),
    ]

PWINDOWPLACEMENT = POINTER(WINDOWPLACEMENT)
LPWINDOWPLACEMENT = POINTER(WINDOWPLACEMENT)


class MONITORINFO(Structure):
    _fields_ = [
        ('cbSize', DWORD),
        ('rcMonitor', RECT),
        ('rcWork', RECT),
        ('dwFlags', DWORD),
    ]

LPMONITORINFO = POINTER(MONITORINFO)

class WNDCLASSEXW(Structure):
    _fields_ = [
        ('cbSize', UINT),
        ('style', UINT),
        ('lpfnWndProc', WNDPROC),
        ('cbClsExtra', c_int),
        ('cbWndExtra', c_int),
        ('hInstance', HANDLE),
        ('hIcon', HANDLE),
        ('hCursor', HANDLE),
        ('hbrBackground', wintypes.HBRUSH),
        ('lpszMenuName', wintypes.LPCWSTR),
        ('lpszClassName', wintypes.LPCWSTR),
        ('hIconSm', HICON),
    ]

PWNDCLASSEXW = POINTER(WNDCLASSEXW)

class WNDCLASS(Structure):
    _fields_ = [('style', c_uint),
            ('lpfnWndProc', WNDPROC),
            ('cbClsExtra', c_int),
            ('cbWndExtra', c_int),
            ('hInstance', HANDLE),
            ('hIcon', HANDLE),
            ('hCursor', HANDLE),
            ('hbrBackground', HANDLE),
            ('lpszMenuName', LPCSTR),
            ('lpszClassName', LPCSTR)]


# class CREATESTRUCTW(Structure):
#     _fields_ = [
#         ('lpCreateParams', c_void_p),
#         ('hInstance', wintypes.HINSTANCE),
#         ('hMenu', wintypes.HMENU),
#         ('hwndParent', HWND),
#         ('cy', c_int),
#         ('cx', c_int),
#         ('y', c_int),
#         ('x', c_int),
#         ('style', LONG),
#         ('lpszName', wintypes.LPCWSTR),
#         ('lpszClass', wintypes.LPCWSTR),
#         ('dwExStyle', DWORD),
#     ]

class CREATESTRUCTW(Structure):
    _fields_ = [
        ('lpCreateParams', c_void_p),
        ('hInstance', HANDLE),
        ('hMenu', HANDLE),
        ('hwndParent', HWND),
        ('cy', c_int),
        ('cx', c_int),
        ('y', c_int),
        ('x', c_int),
        ('style', c_int),
        ('lpszName', wintypes.LPCWSTR),
        ('lpszClass', wintypes.LPCWSTR),
        ('dwExStyle', c_int)
    ]

LPCREATESTRUCTW = POINTER(CREATESTRUCTW)


class WINDOWPOS(Structure):
    _fields_ = [
        ('hwnd', HWND),
        ('hwndInsertAfter', HWND),
        ('x', c_int),
        ('y', c_int),
        ('cx', c_int),
        ('cy', c_int),
        ('flags', UINT),
    ]

LPWINDOWPOS = POINTER(WINDOWPOS)
PWINDOWPOS = POINTER(WINDOWPOS)


class NCCALCSIZE_PARAMS(Structure):
    _fields_ = [
        ('rgrc', RECT * 3),
        ('lppos', PWINDOWPOS),
    ]

LPNCCALCSIZE_PARAMS = POINTER(NCCALCSIZE_PARAMS)


class STYLESTRUCT(Structure):
    _fields_ = [
        ('styleOld', DWORD),
        ('styleNew', DWORD),
    ]

LPSTYLESTRUCT = POINTER(STYLESTRUCT)


class GUID(Structure):
    _fields_ = [
        ("Data1", DWORD),
        ("Data2", WORD),
        ("Data3", WORD),
        ("Data4", BYTE * 8)
    ]

    @classmethod
    def from_uuid(cls, uuid_obj: UUID) -> 'GUID':
        return cls(
            uuid_obj.time_low,
            uuid_obj.time_mid,
            uuid_obj.time_hi_version,
            (BYTE * 8)(*uuid_obj.node.to_bytes(8, byteorder='big'))
        )
