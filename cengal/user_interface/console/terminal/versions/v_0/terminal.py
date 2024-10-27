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
    'StyledText', 
    'SText', 
    'ST', 
    'st', 
    'styled_text_args_to_write_args', 
    'styled_print', 
    's_print', 
    'sprint', 
    'styled_text_line', 
    's_text_line', 
    'stext_line', 
    'stext_ln', 
    'stextln', 
    'stln', 
    'styled_text', 
    's_text', 
    'stext', 
    'fill_current_line', 
    'f_current_line', 
    'f_current_ln', 
    'f_currentln', 
    'fcurrent_ln', 
    'fcurrentln', 
    'f_curr_ln', 
    'fcurr_ln', 
    'fcurrln', 
    'f_cur_ln', 
    'f_curln', 
    'fcur_ln', 
    'fcurln', 
    'Terminal', 
    'terminal', 

    'Key', 
    'KeyId', 
    'KeyDb', 
    # 'parse_infocmp', 
    # 'fill_current_unix_key_db', 
    'read_key', 
    'readkey', 
    'rkey', 
    'key', 
    'ctrl_key', 
    'c_key', 
    'ckey', 
    'key_str', 
    'k_str', 
    'kstr', 

    'BackgroundColor', 
    'BC', 
    'ForegroundColor', 
    'FC', 
    'Style', 
    'S', 
    'BackgroundStyle', 
    'BStyle', 
    'BS', 
    'TerminalCmd', 
    'TC', 
    'Color', 
    'C', 
    'ForegroundTrueColor', 
    'FTC', 
    'BackgroundTrueColor', 
    'BTC', 
    'simple_args_to_write_args', 
    'styled_write', 
    's_write', 
    'swrite', 
    'styled_write_line', 
    's_write_line', 
    'swrite_line', 
    'swriteln', 
    'styled_echo', 
    's_echo', 
    'secho', 
    'write_styled', 
    'set_foreground_color', 
    'set_background_color', 
    'set_foreground_true_color', 
    'set_background_true_color', 
    'is_true_color_supported', 
    'enable_true_colors', 
    'disable_true_colors', 
    'reset_attributes',

    'read_password_from_stdin', 

    'erase_line', 
    'erase_screen', 

    'isatty', 

    'getch', 

    'cursor_backward', 
    'cursor_down', 
    'cursor_forward', 
    'cursor_up', 
    'hide_cursor', 
    'show_cursor', 
    'set_cursor_pos', 
    'set_cursor_x_pos', 
    'set_cursor_y_pos', 

    'terminal_size', 
    'terminal_height', 
    'terminal_width', 
]


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


# from cengal.code_inspection.auto_line_tracer import tr, tl
from cengal.performance_test_lib import mtimetl
from cengal.data_manipulation.conversion.hex import hex_dword_to_int
from cengal.data_manipulation.conversion.binary import bytes_to_ubint
from cengal.data_manipulation.mapping import inverse_mapping
from cengal.code_flow_control.smart_values import ValueHolder
from cengal.system import OS_TYPE
from cengal.user_interface.console.nim_terminal import *

import os
import subprocess
import threading
import re
from enum import IntEnum, Enum
from collections import deque
from contextlib import ContextDecorator, contextmanager
from typing import List, Deque, Tuple, Dict, Set, Union, Optional, Sequence, Callable, Any, overload


class StyledText:
    @overload
    def __init__(self, text: Union[str, Callable, Any]): ...

    def __init__(self, *args):
        self._reset_style: bool = False
        self._items: Optional[List[StyledText]] = None
        self._text: Union[str, Callable] = None
        if len(args) == 0:
            self._text = str()
        elif len(args) == 1:
            text = args[0]
            self._text = text if callable(text) else f'{text}'
        else:
            self._items = [item if isinstance(item, StyledText) else StyledText(item) for item in args]

        self._style_args: List[Union[BackgroundColor, ForegroundColor, Style, TerminalCmd, Color]] = list()
    
    def __call__(self) -> Tuple:
        if self._items is None:
            text = self._text
            return self._style_args + [text if isinstance(text, str) else f'{text()}']
        else:
            result_args: List = list()
            for item in self._items:
                if not item._reset_style:
                    result_args.extend(self._style_args)
                
                result_args.extend(item())
            
            return result_args
    
    def get_text(self) -> str:
        text = self._text
        return text if isinstance(text, str) else f'{text()}'

    # Parent behavior
    @property
    def resetStyle(self) -> 'StyledText':
        self._reset_style = True
        return self
    
    reset_style = resetStyle
    res_style = resetStyle
    rstyle = resetStyle

    # BackgroundColor
    @property
    def bgBlack(self) -> 'StyledText':
        self._style_args.append(BackgroundColor.black)
        return self
    
    bg_black = bgBlack
    background_color__black = bgBlack
    bc_black = bgBlack
    b_black = bgBlack
    bblack = bgBlack
    bbla = bgBlack

    @property
    def bgRed(self) -> 'StyledText':
        self._style_args.append(BackgroundColor.red)
        return self
    
    bg_red = bgRed
    background_color__red = bgRed
    bc_red = bgRed
    b_red = bgRed
    bred = bgRed

    @property
    def bgGreen(self) -> 'StyledText':
        self._style_args.append(BackgroundColor.green)
        return self
    
    bg_green = bgGreen
    background_color__green = bgGreen
    bc_green = bgGreen
    b_green = bgGreen
    bgreen = bgGreen
    bgre = bgGreen

    @property
    def bgYellow(self) -> 'StyledText':
        self._style_args.append(BackgroundColor.yellow)
        return self
    
    bg_yellow = bgYellow
    background_color__yellow = bgYellow
    bc_yellow = bgYellow
    b_yellow = bgYellow
    byellow = bgYellow
    byel = bgYellow

    @property
    def bgBlue(self) -> 'StyledText':
        self._style_args.append(BackgroundColor.blue)
        return self
    
    bg_blue = bgBlue
    background_color__blue = bgBlue
    bc_blue = bgBlue
    b_blue = bgBlue
    bblue = bgBlue
    bblu = bgBlue

    @property
    def bgMagenta(self) -> 'StyledText':
        self._style_args.append(BackgroundColor.magenta)
        return self
    
    bg_magenta = bgMagenta
    background_color__magenta = bgMagenta
    bc_magenta = bgMagenta
    b_magenta = bgMagenta
    bmagenta = bgMagenta
    bmag = bgMagenta

    @property
    def bgCyan(self) -> 'StyledText':
        self._style_args.append(BackgroundColor.cyan)
        return self
    
    bg_cyan = bgCyan
    background_color__cyan = bgCyan
    bc_cyan = bgCyan
    b_cyan = bgCyan
    bcyan = bgCyan
    bcya = bgCyan

    @property
    def bgWhite(self) -> 'StyledText':
        self._style_args.append(BackgroundColor.white)
        return self
    
    bg_white = bgWhite
    background_color__white = bgWhite
    bc_white = bgWhite
    b_white = bgWhite
    bwhite = bgWhite
    bwhi = bgWhite

    @property
    def bg8Bit(self) -> 'StyledText':
        self._style_args.append(BackgroundColor._8bit)
        return self
    
    bg_8bit = bg8Bit
    background_color__8bit = bg8Bit
    bc_8bit = bg8Bit
    b_8bit = bg8Bit
    b8bit = bg8Bit

    @property
    def bgDefault(self) -> 'StyledText':
        self._style_args.append(BackgroundColor.default)
        return self
    
    bg_default = bgDefault
    background_color__default = bgDefault
    bc_default = bgDefault
    b_default = bgDefault
    bdefault = bgDefault
    bdef = bgDefault

    # ForegroundColor
    @property
    def fgBlack(self) -> 'StyledText':
        self._style_args.append(ForegroundColor.black)
        return self
    
    fg_black = fgBlack
    foreground_color__black = fgBlack
    fc_black = fgBlack
    f_black = fgBlack
    fblack = fgBlack
    fbla = fgBlack

    @property
    def fgRed(self) -> 'StyledText':
        self._style_args.append(ForegroundColor.red)
        return self
    
    fg_red = fgRed
    foreground_color__red = fgRed
    fc_red = fgRed
    f_red = fgRed
    fred = fgRed

    @property
    def fgGreen(self) -> 'StyledText':
        self._style_args.append(ForegroundColor.green)
        return self
    
    fg_green = fgGreen
    foreground_color__green = fgGreen
    fc_green = fgGreen
    f_green = fgGreen
    fgreen = fgGreen
    fgre = fgGreen

    @property
    def fgYellow(self) -> 'StyledText':
        self._style_args.append(ForegroundColor.yellow)
        return self
    
    fg_yellow = fgYellow
    foreground_color__yellow = fgYellow
    fc_yellow = fgYellow
    f_yellow = fgYellow
    fyellow = fgYellow
    fyel = fgYellow

    @property
    def fgBlue(self) -> 'StyledText':
        self._style_args.append(ForegroundColor.blue)
        return self
    
    fg_blue = fgBlue
    foreground_color__blue = fgBlue
    fc_blue = fgBlue
    f_blue = fgBlue
    fblue = fgBlue
    fblu = fgBlue

    @property
    def fgMagenta(self) -> 'StyledText':
        self._style_args.append(ForegroundColor.magenta)
        return self
    
    fg_magenta = fgMagenta
    foreground_color__magenta = fgMagenta
    fc_magenta = fgMagenta
    f_magenta = fgMagenta
    fmagenta = fgMagenta
    fmag = fgMagenta

    @property
    def fgCyan(self) -> 'StyledText':
        self._style_args.append(ForegroundColor.cyan)
        return self
    
    fg_cyan = fgCyan
    foreground_color__cyan = fgCyan
    fc_cyan = fgCyan
    f_cyan = fgCyan
    fcyan = fgCyan
    fcya = fgCyan

    @property
    def fgWhite(self) -> 'StyledText':
        self._style_args.append(ForegroundColor.white)
        return self
    
    fg_white = fgWhite
    foreground_color__white = fgWhite
    fc_white = fgWhite
    f_white = fgWhite
    fwhite = fgWhite
    fwhi = fgWhite

    @property
    def fg8Bit(self) -> 'StyledText':
        self._style_args.append(ForegroundColor._8bit)
        return self
    
    fg_8bit = fg8Bit
    foreground_color__8bit = fg8Bit
    fc_8bit = fg8Bit
    f_8bit = fg8Bit
    f8bit = fg8Bit

    @property
    def fgDefault(self) -> 'StyledText':
        self._style_args.append(ForegroundColor.default)
        return self
    
    fg_default = fgDefault
    foreground_color__default = fgDefault
    fc_default = fgDefault
    f_default = fgDefault
    fdefault = fgDefault
    fdef = fgDefault

    # Style
    @property
    def styleBright(self) -> 'StyledText':
        self._style_args.append(Style.bright)
        return self
    
    style_bright = styleBright
    s_bright = styleBright
    sbright = styleBright
    bright = styleBright
    brig = styleBright

    @property
    def styleDim(self) -> 'StyledText':
        self._style_args.append(Style.dim)
        return self
    
    style_dim = styleDim
    s_dim = styleDim
    sdim = styleDim
    dim = styleDim

    @property
    def styleItalic(self) -> 'StyledText':
        self._style_args.append(Style.italic)
        return self
    
    style_italic = styleItalic
    s_italic = styleItalic
    sitalic = styleItalic
    italic = styleItalic
    ital = styleItalic

    @property
    def styleUnderscore(self) -> 'StyledText':
        self._style_args.append(Style.underscore)
        return self
    
    style_underscore = styleUnderscore
    s_underscore = styleUnderscore
    sunderscore = styleUnderscore
    underscore = styleUnderscore
    unde = styleUnderscore

    @property
    def styleBlink(self) -> 'StyledText':
        self._style_args.append(Style.blink)
        return self
    
    style_blink = styleBlink
    s_blink = styleBlink
    sblink = styleBlink
    blink = styleBlink

    @property
    def styleBlinkRapid(self) -> 'StyledText':
        self._style_args.append(Style.blinkrapid)
        return self
    
    style_blinkrapid = styleBlinkRapid
    s_blinkrapid = styleBlinkRapid
    sblinkrapid = styleBlinkRapid
    blinkrapid = styleBlinkRapid
    blinkr = styleBlinkRapid

    @property
    def styleReverse(self) -> 'StyledText':
        self._style_args.append(Style.reverse)
        return self
    
    style_reverse = styleReverse
    s_reverse = styleReverse
    sreverse = styleReverse
    reverse = styleReverse
    reve = styleReverse

    @property
    def styleHidden(self) -> 'StyledText':
        self._style_args.append(Style.hidden)
        return self
    
    style_hidden = styleHidden
    s_hidden = styleHidden
    shidden = styleHidden
    hidden = styleHidden
    hidd = styleHidden

    @property
    def styleStrikethrough(self) -> 'StyledText':
        self._style_args.append(Style.strikethrough)
        return self
    
    style_strikethrough = styleStrikethrough
    s_strikethrough = styleStrikethrough
    sstrikethrough = styleStrikethrough
    strikethrough = styleStrikethrough
    stri = styleStrikethrough

    # BackgroundStyle
    @property
    def backgroundStyleBright(self) -> 'StyledText':
        self._style_args.append(BackgroundStyle.bright)
        return self
    
    background_style_bright = backgroundStyleBright
    bstyle_bright = backgroundStyleBright
    bs_bright = backgroundStyleBright
    bsbright = backgroundStyleBright
    bbright = backgroundStyleBright
    bbri = backgroundStyleBright

    @property
    def backgroundStyleDim(self) -> 'StyledText':
        self._style_args.append(BackgroundStyle.dim)
        return self
    
    background_style_dim = backgroundStyleDim
    bstyle_dim = backgroundStyleDim
    bs_dim = backgroundStyleDim
    bsdim = backgroundStyleDim
    bdim = backgroundStyleDim

    # Color
    def foreground_true_color(self, color: Color) -> 'StyledText':
        self._style_args.append(ForegroundTrueColor(int(color)))
        return self
    
    ftrue_color = foreground_true_color
    ft_color = foreground_true_color
    ftcolor = foreground_true_color
    ftcol = foreground_true_color
    ftc = foreground_true_color
    foreground_color = foreground_true_color
    f_color = foreground_true_color
    fcolor = foreground_true_color
    fcol = foreground_true_color
    fc = foreground_true_color

    def background_true_color(self, color: Color) -> 'StyledText':
        self._style_args.append(BackgroundTrueColor(int(color)))
        return self
    
    btrue_color = background_true_color
    bt_color = background_true_color
    btcolor = background_true_color
    btcol = background_true_color
    btc = background_true_color
    background_color = background_true_color
    b_color = background_true_color
    bcolor = background_true_color
    bcol = background_true_color
    bc = background_true_color


SText = StyledText
ST = StyledText
st = StyledText


def styled_text_args_to_write_args(args, kwargs) -> List[Dict]:
    result_args = list()
    for styled_text in args:
        if not isinstance(styled_text, StyledText):
            styled_text = StyledText(styled_text)
        
        result_args.extend(styled_text())
    
    return simple_args_to_write_args(result_args, kwargs)


def styled_print(*args, end_line: bool = True, **kwargs):
    if end_line:
        nstyledWriteLine(styled_text_args_to_write_args(args, kwargs))
        # with mtimetl():
        #     args = styled_text_args_to_write_args(args, kwargs)
        
        # with mtimetl():
        #     nstyledWriteLine(args)
    else:
        nstyledWrite(styled_text_args_to_write_args(args, kwargs))


s_print = styled_print
sprint = styled_print


def styled_text_line(*args, **kwargs):
    nstyledWriteLine(styled_text_args_to_write_args(args, kwargs))


s_text_line = styled_text_line
stext_line = styled_text_line
stext_ln = styled_text_line
stextln = styled_text_line
stln = styled_text_line


def styled_text(*args, **kwargs):
    nstyledWrite(styled_text_args_to_write_args(args, kwargs))


s_text = styled_text
stext = styled_text


def fill_current_line(styled_char: StyledText = None):
    styled_char: StyledText = st(' ') if styled_char is None else styled_char
    styled_char._text = styled_char.get_text() * terminal_width()
    sprint(styled_char)
    cursor_up()


f_current_line = fill_current_line
f_current_ln = fill_current_line
f_currentln = fill_current_line
fcurrent_ln = fill_current_line
fcurrentln = fill_current_line
f_curr_ln = fill_current_line
f_currln = fill_current_line
fcurr_ln = fill_current_line
fcurrln = fill_current_line
f_cur_ln = fill_current_line
f_curln = fill_current_line
fcur_ln = fill_current_line
fcurln = fill_current_line


class Key(Enum):
    Escape = 0
    Backspace = 1
    Tab = 2
    Enter = 3
    Space = 4
    F1 = 5
    F2 = 6
    F3 = 7
    F4 = 8
    F5 = 9
    F6 = 10
    F7 = 11
    F8 = 12
    F9 = 13
    F10 = 14
    F11 = 15
    F12 = 16
    Up = 17
    Down = 18
    Right = 19
    Left = 20
    Home = 21
    Insert = 22
    Delete = 23
    End = 24
    PageUp = 25
    PageDown = 26
    CtrlBackspace = 27


KeyId = Union[int, Key]


_need_to_stop: bool = False


class KeyDb:
    def __init__(self, seq_start: Set[int]):
        self._seq_start: Set[int] = seq_start
        self._id_seq_set__by__key_id: Dict[Union[None, int, Key], Set[Sequence[int]]] = dict()
        self._key_id_set__by__id_seq: Dict[Sequence[int], Set[Union[None, int, Key]]] = dict()
        self._id_seq_set__by__id_seq_prefix: Dict[Sequence[int], Set[Sequence[int]]] = dict()
    
    def add(self, key_id: Union[int, Key], id_seq: Union[Sequence[int], Set[Sequence[int]]]):
        if isinstance(id_seq, set):
            id_seq_set: Set[Sequence[int]] = id_seq
        else:
            id_seq_set = {tuple(id_seq)}
        for id_seq in id_seq_set:
            if key_id not in self._id_seq_set__by__key_id:
                self._id_seq_set__by__key_id[key_id] = set()
            
            self._id_seq_set__by__key_id[key_id].add(id_seq)
            if id_seq not in self._key_id_set__by__id_seq:
                self._key_id_set__by__id_seq[id_seq] = set()
            
            self._key_id_set__by__id_seq[id_seq].add(key_id)
            id_seq_prefix: Sequence[int] = id_seq
            while id_seq_prefix:
                if id_seq_prefix not in self._id_seq_set__by__id_seq_prefix:
                    self._id_seq_set__by__id_seq_prefix[id_seq_prefix] = set()
                
                self._id_seq_set__by__id_seq_prefix[id_seq_prefix].add(id_seq)
                id_seq_prefix = id_seq_prefix[:-1]
    
    def find(self, id_seq: Sequence[int]) -> Optional[Set[Union[int, Key]]]:
        id_seq = tuple(id_seq)
        if not id_seq:
            return set()

        if id_seq in self._key_id_set__by__id_seq:
            result = set(self._key_id_set__by__id_seq[id_seq])
            if 1 < len(result):
                if None in result:
                    result.discard(None)
            
            return result
        elif id_seq in self._id_seq_set__by__id_seq_prefix:
            if id_seq:
                if id_seq[0] in self._seq_start:
                    return set()
                else:
                    return None
            else:
                return None
        else:
            return None
    
    def get(self, key_id: Union[None, int, Key]) -> Set[Sequence[int]]:
        return self._id_seq_set__by__key_id.get(key_id, None)


if 'Windows' == OS_TYPE:
    # See: Key Scan Codes
    #   https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-6.0/aa299374(v=vs.60)
    windows_capname_by_key_id: Dict[Union[int, Key], str] = {
        Key.Escape: 'ESC',
        Key.Space: 'SPACE',
        Key.Backspace: 'BKSP',
        Key.Tab: 'TAB',
        Key.Enter: 'ENTER',
        Key.F1: 'F1',
        Key.F2: 'F2',
        Key.F3: 'F3',
        Key.F4: 'F4',
        Key.F5: 'F5',
        Key.F6: 'F6',
        Key.F7: 'F7',
        Key.F8: 'F8',
        Key.F9: 'F9',
        Key.F10: 'F10',
        Key.F11: 'F11',
        Key.F12: 'F12',
        Key.Up: 'UP',
        Key.Down: 'DOWN',
        Key.Right: 'RIGHT',
        Key.Left: 'LEFT',
        Key.Home: 'HOME',
        Key.Insert: 'INS',
        Key.Delete: 'DEL',
        Key.End: 'END',
        Key.PageUp: 'PGUP',
        Key.PageDown: 'PGDN',
        Key.CtrlBackspace: 'CTRL+BKSP',
    }


    windows_keycode_by_key_id_seq: Dict[Union[int, Key], List[int]] = {
        Key.Escape: [ord('\x1b')],
        Key.Space: [ord(' ')],
        Key.Enter: [10],
    }


    windows_key_db: KeyDb = KeyDb({224, 0})


    windows_capabilities: Dict[str, List[int]] = {
        'ESC': [27],
        'SPACE': [32],
        'BKSP': [8],
        'TAB': [9],
        'ENTER': [13],
        'F1': [0, 59],
        'F2': [0, 60],
        'F3': [0, 61],
        'F4': [0, 62],
        'F5': [0, 63],
        'F6': [0, 64],
        'F7': [0, 65],
        'F8': [0, 66],
        'F9': [0, 67],
        'F10': [0, 68],
        'F11': [224, 133],
        'F12': [224, 134],
        'UP': {(224, 72), (0, 72)},
        'DOWN': {(224, 80), (0, 80)},
        'RIGHT': {(224, 77), (0, 77)},
        'LEFT': {(224, 75), (0, 75)},
        'HOME': {(224, 71), (0, 71)},
        'INS': {(224, 82), (0, 82)},
        'DEL': {(224, 83), (0, 83)},
        'END': {(224, 79), (0, 79)},
        'PGUP': {(224, 73), (0, 73)},
        'PGDN': {(224, 81), (0, 81)},
        'CTRL+BKSP': [127],
    }


    def fill_windows_key_db():
        for key_id, key_code_seq in windows_keycode_by_key_id_seq.items():
            windows_key_db.add(key_id, key_code_seq)
        
        for key_id, capname in windows_capname_by_key_id.items():
            windows_key_db.add(key_id, windows_capabilities[capname])
        
        for _, id_seq in windows_capabilities.items():
            windows_key_db.add(None, id_seq)


    fill_windows_key_db()


    def read_key_async(timeout: Optional[float] = 0.35) -> Optional[Union[int, Key]]:
        key_int_seq: Deque[int] = wait_for_key_async(timeout)
        possible_keys = windows_key_db.find(key_int_seq)
        if possible_keys is None:
            if 1 == len(key_int_seq):
                return key_int_seq[0]
            else:
                return None
        else:
            if 1 == len(possible_keys):
                return possible_keys.pop()
            else:
                return None


    def read_keys_thread_func_async(key_int_seq: Deque, timeout: Optional[float] = (1/60 + 0.001)):
        while not _need_to_stop:
            key_int: Optional[Tuple[int]] = win_try_getch(timeout)
            if key_int is None:
                return

            key_int_seq.extend(key_int)
            # break
            possible_keys: Optional[Set[Union[int, Key]]] = windows_key_db.find(key_int_seq)
            if possible_keys is None:
                return
            else:
                if (1 < len(possible_keys)) and (None in possible_keys):
                    possible_keys.discard(None)
                
                if 1 == len(possible_keys):
                    if possible_keys & {224, 0}:
                        continue
                    else:
                        return
                else:
                    continue


    def wait_for_key_async(timeout: Optional[float] = (1/60 + 0.001)):
        key_int_seq: Deque[int] = deque()
        save_stdout_state()
        try:
            read_keys_thread_func_async(key_int_seq, timeout)
        finally:
            restore_stdout_state()
        
        return key_int_seq


    read_key = read_key_async
    readkey = read_key
    rkey = read_key


    def key(key_value: Union[str, int, Key]) -> Union[int, Key]:
        if isinstance(key_value, Key):
            return key_value

        if isinstance(key_value, int):
            return key(chr(key_value))

        if key_value.casefold().startswith('ctrl  '):
            return ctrl_key(' ')
        elif key_value.casefold().startswith('ctrl '):
            parts = key_value.split(maxsplit=1)
            return ctrl_key(parts[1])
        elif key_value.casefold().startswith('ctrl+'):
            parts = key_value.split('+', maxsplit=1)
            return ctrl_key(parts[1])
        elif key_value.casefold().startswith('ctrl-'):
            parts = key_value.split('-', maxsplit=1)
            return ctrl_key(parts[1])
        elif key_value.casefold().startswith('ctrl_'):
            parts = key_value.split('_', maxsplit=1)
            return ctrl_key(parts[1])
        elif key_value.casefold().startswith('ctrl'):
            return ctrl_key(key_value[len('ctrl'):])
        elif '\t' == key_value[0]:
            return Key.Tab
        elif '\n' == key_value[0]:
            return Key.Enter
        elif '\r' == key_value[0]:
            return Key.Enter
        elif ' ' == key_value[0]:
            return Key.Space
        else:
            return ord(key_value[0])


    min_ctrl_plus_int: int = ord('A') - ord('A') + 1
    max_ctrl_plus_int: int = ord('`') - ord('A') + 1


    ctrl_key__by__key = {
        'q': 17,
        'w': 23,
        'e': 5,
        'r': 18,
        't': 20,
        'y': 25,
        'u': 21,
        'i': 9,
        'o': 16,
        'p': 19,
        'a': 1,
        's': 19,
        'd': 4,
        'f': 6,
        'g': 7,
        'h': 8,
        'j': 10,
        'k': 11,
        'l': 12,
        'z': 26,
        'x': 24,
        'c': 3,
        'v': 22,
        'b': 2,
        'n': 14,
        'm': 13,
        '\\': 28,
        '[': 27,
        ']': 29,
        '-': 31,
    }
    key__by__ctrl_key = inverse_mapping(ctrl_key__by__key)


    def ctrl_key(key_value: str) -> Union[int, Key]:
        casefold_key_value: str = key_value.casefold()
        key_value_int: int = ord(casefold_key_value)
        if key_value.casefold() in ctrl_key__by__key:
            if 'i' == casefold_key_value:
                return Key.Tab
            elif 'm' == casefold_key_value:
                return Key.Enter
            elif 'h' == casefold_key_value:
                return Key.CtrlBackspace
            elif '[' == casefold_key_value:
                return Key.Escape
            else:
                return ctrl_key__by__key[key_value.casefold()]
        else:
            raise ValueError(f'Key "{casefold_key_value}" of id "{key_value_int}" can not produce Ctrl+ sequence')


    c_key = ctrl_key
    ckey = ctrl_key


    def key_str(key_id: Union[int, Key]) -> str:
        key_id = key(key_id)
        if isinstance(key_id, Key):
            return key_id.name
        elif isinstance(key_id, int):
            if (255 < key_id) or (0 > key_id):
                raise ValueError(f'Unknown key id: {key_id}')
            
            if key_id in key__by__ctrl_key:
                orig_key: str = key__by__ctrl_key[key_id]
                alt_key: Union[int, Key] = key(ctrl_key(orig_key))
                if isinstance(alt_key, Key):
                    return alt_key.name
                else:
                    return f'Ctrl+{orig_key}'
            else:
                orig_key: str = chr(key_id)
                alt_key: Union[int, Key] = key(orig_key)
                if isinstance(alt_key, Key):
                    return alt_key.name
                else:
                    return orig_key
        else:
            raise TypeError(f'Unsupported type ({type(key_id)}) of key id: {key_id}')


    k_str = key_str
    kstr = key_str
else:
    # See: https://man7.org/linux/man-pages/man5/terminfo.5.html
    #   and https://en.wikipedia.org/wiki/ANSI_escape_code
    unix_capname_by_key_id: Dict[Union[int, Key], str] = {
        Key.Backspace: 'kbs',
        Key.Tab: 'ht',
        Key.Enter: 'cr',
        Key.F1: 'kf1',
        Key.F2: 'kf2',
        Key.F3: 'kf3',
        Key.F4: 'kf4',
        Key.F5: 'kf5',
        Key.F6: 'kf6',
        Key.F7: 'kf7',
        Key.F8: 'kf8',
        Key.F9: 'kf9',
        Key.F10: 'kf10',
        Key.F11: 'kf11',
        Key.F12: 'kf12',
        Key.Up: 'kcuu1',
        Key.Down: 'kcud1',
        Key.Right: 'kcuf1',
        Key.Left: 'kcub1',
        Key.Home: 'khome',
        Key.Insert: 'kich1',
        Key.Delete: 'kdch1',
        Key.End: 'kend',
        Key.PageUp: 'kpp',   # kpp stands for PageUp
        Key.PageDown: 'knp',  # knp stands for PageDown
        Key.CtrlBackspace: 'cub1',  # Generally, Ctrl-Backspace is not standard, this might be incorrect
    }


    unix_keycode_by_key_id_seq: Dict[Union[int, Key], List[int]] = {
        Key.Escape: [ord('\x1b')],
        Key.Space: [ord(' ')],
        Key.Enter: [ord('\n')],  # 10
    }


    current_unix_key_db: KeyDb = KeyDb({27})


    unix_capabilities: Dict[str, List[int]] = dict()


    def get_infocmp_output(term=None):
        if term is None:
            term = os.environ.get('TERM', '')
        
        result = subprocess.run(['infocmp', term], capture_output=True, text=True, check=True)
        return result.stdout


    def parse_statement(statement: str) -> List[int]:
        result = list()
        while statement:
            if statement.startswith('\E'):
                result.append(ord('\x1b'))
                statement = statement.removeprefix('\\E')
            elif statement.startswith('\\e'):
                result.append(ord('\x1b'))
                statement = statement.removeprefix('\e')
            elif statement.startswith('\\n'):
                result.append(ord('\n'))
                statement = statement.removeprefix('\\n')
            elif statement.startswith('\\l'):  # same as '\n'
                result.append(ord('\n'))
                statement = statement.removeprefix('\l')
            elif statement.startswith('\\r'):
                result.append(ord('\r'))
                statement = statement.removeprefix('\\r')
            elif statement.startswith('\\t'):
                result.append(ord('\t'))
                statement = statement.removeprefix('\\t')
            elif statement.startswith('\\b'):
                result.append(ord('\b'))
                statement = statement.removeprefix('\\b')
            elif statement.startswith('\\f'):
                result.append(ord('\f'))
                statement = statement.removeprefix('\\f')
            elif statement.startswith('\\s'):
                result.append(ord(' '))
                statement = statement.removeprefix('\s')
            elif statement.startswith('\\\\'):
                result.append(ord('\\'))
                statement = statement.removeprefix('\\\\')
            elif statement.startswith('\\,'):
                result.append(ord(','))
                statement = statement.removeprefix('\\,')
            elif statement.startswith('\\054'):
                result.append(ord(','))
                statement = statement.removeprefix('\\054')
            elif statement.startswith('\\:'):
                result.append(ord(':'))
                statement = statement.removeprefix('\\:')
            elif statement.startswith('\\^'):
                result.append(ord('^'))
                statement = statement.removeprefix('\\^')
            elif statement.startswith('\\0'):
                result.append(ord('\x80'))
                statement = statement.removeprefix('\\0')
            elif statement.startswith('^?'):
                result.append(ord('\x7f'))
                statement = statement.removeprefix('^?')
            elif statement.startswith('^'):
                result.append(ctrl_key(statement[1]))
                statement = statement.removeprefix('^?')


    def format_infocmp_output(output: str) -> Dict[str, str]:
        lines = output.split('\n')
        new_lines: List[str] = list()
        for line in lines:
            line = line.strip()
            if line.endswith(','):
                line = line[:-1]
            
            statements: List[str] = line.split(', ')
            new_lines.extend([statement.strip() for statement in statements if '=' in statement])
        
        return '\n'.join(new_lines)


    def split_infocmp_output(output: str) -> Dict[str, str]:
        result: Dict[str, str] = dict()
        lines = output.split('\n')
        new_lines: List[str] = list()
        for line in lines:
            line = line.strip()
            if line.endswith(','):
                line = line[:-1]
            
            statements: List[str] = line.split(', ')
            new_lines.extend([statement.strip() for statement in statements if '=' in statement])
        
        for line in new_lines:
            capname, seq_str = line.split('=')
            result[capname] = seq_str
        
        return result


    ESCAPE_SEQUENCES = {
        r'\E': '\x1b',  # Escape
        r'\e': '\x1b',  # Escape
        r'\n': '\n',    # Newline
        r'\l': '\n',    # Line-feed (same as newline)
        r'\r': '\r',    # Return
        r'\t': '\t',    # Tab
        r'\b': '\b',    # Backspace
        r'\f': '\f',    # Form-feed
        r'\s': ' ',     # Space
        r'\^': '^',     # Literal caret
        r'\\': '\\',    # Backslash
        r'\,': ',',     # Comma
        r'\:': ':',     # Colon
        r'\0': '\x80',  # Null (0x80)
        r'^?': '\x7f',  # DEL character (127)
    }

    def replace_escape_sequences(value):
        # Replace known escape sequences
        for esc_seq, char in ESCAPE_SEQUENCES.items():
            value = value.replace(esc_seq, char)
        
        # Replace octal sequences (e.g., \033)
        value = re.sub(r'\\([0-7]{3})', lambda x: chr(int(x.group(1), 8)), value)
        # Replace control characters (e.g., ^X)
        value = re.sub(r'\^([A-Z@[\]^_])', lambda x: chr(ord(x.group(1)) & 0x1f), value)
        return value


    def escape_sequence_to_int_list(seq):
        """Convert an escape sequence string to a list of integers."""
        seq = replace_escape_sequences(seq)
        return [ord(char) for char in seq]


    def parse_infocmp(output):
        capabilities = {}
        for line in output.splitlines():
            match = re.match(r'^(\w+)\s*=\s*(.*)', line)
            if match:
                key = match.group(1)
                value = match.group(2).strip().strip(',')
                capabilities[key] = escape_sequence_to_int_list(value)
        return capabilities


    def fill_current_unix_key_db():
        infocmp_output = format_infocmp_output(get_infocmp_output())
        # print()
        # print(infocmp_output)
        # print()
        # print('=============')
        global unix_capabilities
        unix_capabilities = parse_infocmp(infocmp_output)
        for key_id, key_code_seq in unix_keycode_by_key_id_seq.items():
            current_unix_key_db.add(key_id, key_code_seq)
        
        for key_id, capname in unix_capname_by_key_id.items():
            current_unix_key_db.add(key_id, unix_capabilities[capname])
        
        for _, id_seq in unix_capabilities.items():
            current_unix_key_db.add(None, id_seq)

        # print(unix_capabilities)

        # # Example: Print the integer sequences for the arrow keys
        # keys_to_check = ['kend', 'kent', 'kf1', 'cr']
        # for key in keys_to_check:
        #     if key in unix_capabilities:
        #         print(f"{key}: {unix_capabilities[key]}")


    fill_current_unix_key_db()


    # key_int_seq: Deque[int] = deque()

    # def read_key() -> Optional[Union[int, Key]]:
    #     if not key_int_seq:
    #         return None

    #     current_seq: List[int] = list()
    #     key_int: int = key_int_seq.popleft()
    #     current_seq.append(key_int)
    #     possible_keys: Optional[Set[Union[int, Key]]] = current_unix_key_db.find(current_seq)
    #     if not possible_keys:
    #         return key_int
    #     else:
    #         if 1 == len(possible_keys):
    #             key_id = possible_keys.pop()
    #             if Key.Escape == key_id:
    #                 # input_thread = threading.Thread(target=read_keys_thread_func, args=(current_seq,), daemon=True)
    #                 # input_thread.start()
    #                 # input_thread.join(timeout=escape_timeout)
    #                 key_found: bool = False
    #                 while key_int_seq and (not key_found):
    #                     another_key_int: int = key_int_seq.popleft()
    #                     current_seq.append(another_key_int)
    #                     another_possible_keys: Optional[Set[Union[int, Key]]] = current_unix_key_db.find(current_seq)
    #                     if not another_possible_keys:
    #                         break

    #                     if 1 == len(another_possible_keys):
    #                         key_found = True
    #                         return another_possible_keys.pop()
                    
    #                 if not key_found:
    #                     for another_key_ing in reversed(current_seq):
    #                         key_int_seq.appendleft(another_key_ing)
                        
    #                     return None
    #             else:
    #                 return key_id
    #         else:
    #             key_int_seq.appendleft(key_int)
    #             current_seq
    #             wait_for_key()
    #             possible_keys = current_unix_key_db.find(current_seq)
    #             return None


    class WatchdogTimeoutError(Exception):
        pass


    def watchdog_thread_func(read_key_done: ValueHolder, timeout: Optional[float] = (1/60 + 0.001)):
        from time import sleep
        from signal import SIG_IGN, SIGUSR1, raise_signal, signal
        if 'Windows' == OS_TYPE:
            raised_signal = SIG_IGN
        else:
            raised_signal = SIGUSR1
        
        sleep(timeout)
        if not read_key_done.value:
            print('raise_signal(raised_signal)')
            raise_signal(raised_signal)


    def watchdog_interrupt_handler(sig, frame):
        raise WatchdogTimeoutError


    @contextmanager
    def watchdog(timeout: Optional[float] = (1/60 + 0.002)):
        read_key_done: ValueHolder[bool] = ValueHolder(True, False)
        from signal import SIG_IGN, SIGUSR1, raise_signal, signal
        if 'Windows' == OS_TYPE:
            raised_signal = SIG_IGN
        else:
            raised_signal = SIGUSR1
        
        previous_handler = signal(raised_signal, watchdog_interrupt_handler)
        input_thread = threading.Thread(target=watchdog_thread_func, args=(read_key_done, timeout,), daemon=True)
        save_stdout_state()
        input_thread.start()
        try:
            yield read_key_done
        except WatchdogTimeoutError:
            pass
        finally:
            signal(raised_signal, previous_handler)
            restore_stdout_state()
            input_thread.join(timeout)


    # def read_key_singlethread() -> Optional[Union[int, Key]]:
    #     key_int_seq: Deque[int] = deque()
    #     possible_keys: Optional[Set[Union[int, Key]]] = None
    #     while (not _need_to_stop) and ((key_int_seq and (possible_keys is not None)) or (not key_int_seq)) and (((possible_keys is not None)) and ((1 != len(possible_keys)) or ((1 == len(possible_keys)) and (Key.Escape == key_int_seq[0])))):
    #         with watchdog(5) as read_key_done:
    #             key_int: int = getch()
    #             print(key_int)
    #             read_key_done.value = True
            
    #         key_int_seq.append(key_int)
    #         possible_keys = current_unix_key_db.find(key_int_seq)

    #     possible_keys = current_unix_key_db.find(key_int_seq)
    #     if (possible_keys is not None) and (1 == len(possible_keys)):
    #         return possible_keys.pop()
    #     else:
    #         return None


    def read_key_singlethread(timeout: Optional[float] = 0.35) -> Optional[Union[int, Key]]:
        key_int_seq: Deque[int] = wait_for_key_singlethread(timeout)
        possible_keys = current_unix_key_db.find(key_int_seq)
        if possible_keys is None:
            if 1 == len(key_int_seq):
                return key_int_seq[0]
            else:
                return None
        else:
            if 1 == len(possible_keys):
                return possible_keys.pop()
            else:
                return None


    def wait_for_key_singlethread(timeout: Optional[float] = (1/60 + 0.002)):
        key_int_seq: Deque[int] = deque()
        save_stdout_state()
        try:
            with watchdog(timeout) as read_key_done:
                read_keys_thread_func(key_int_seq)
                read_key_done.value = True
        finally:
            restore_stdout_state()
        
        return key_int_seq


    # ========================================================


    def read_key_multithread(timeout: Optional[float] = 0.35) -> Optional[Union[int, Key]]:
        key_int_seq: Deque[int] = wait_for_key(timeout)
        possible_keys = current_unix_key_db.find(key_int_seq)
        if possible_keys is None:
            if 1 == len(key_int_seq):
                return key_int_seq[0]
            else:
                return None
        else:
            if 1 == len(possible_keys):
                return possible_keys.pop()
            else:
                return None
    

    def flush_key_queue():
        while read_key() is not None:
            pass


    def read_keys_thread_func(key_int_seq):
        while not _need_to_stop:
            key_int: int = getch()
            key_int_seq.append(key_int)
            # break
            possible_keys: Optional[Set[Union[int, Key]]] = current_unix_key_db.find(key_int_seq)
            if possible_keys is None:
                return
            else:
                if (1 < len(possible_keys)) and (None in possible_keys):
                    possible_keys.discard(None)
                
                if 1 == len(possible_keys):
                    if Key.Escape in possible_keys:
                        continue
                    else:
                        return
                else:
                    continue


    def wait_for_key(timeout: Optional[float] = (1/60 + 0.001)):
        key_int_seq: Deque[int] = deque()
        input_thread = threading.Thread(target=read_keys_thread_func, args=(key_int_seq,), daemon=True)
        save_stdout_state()
        try:
            input_thread.start()
            input_thread.join(timeout)
        finally:
            restore_stdout_state()
        
        return key_int_seq


    # ========================================================


    def read_key_async(timeout: Optional[float] = 0.35) -> Optional[Union[int, Key]]:
        key_int_seq: Deque[int] = wait_for_key_async(timeout)
        possible_keys = current_unix_key_db.find(key_int_seq)
        if possible_keys is None:
            if 1 == len(key_int_seq):
                return key_int_seq[0]
            else:
                return None
        else:
            if 1 == len(possible_keys):
                return possible_keys.pop()
            else:
                return None


    def read_keys_thread_func_async(key_int_seq, timeout: Optional[float] = (1/60 + 0.001)):
        if not prepare_try_getch(timeout):
            return
        
        while not _need_to_stop:
            key_int: Optional[int] = tr(try_getch())
            if key_int is None:
                return

            key_int_seq.append(key_int)
            # break
            possible_keys: Optional[Set[Union[int, Key]]] = current_unix_key_db.find(key_int_seq)
            if possible_keys is None:
                return
            else:
                if (1 < len(possible_keys)) and (None in possible_keys):
                    possible_keys.discard(None)
                
                if 1 == len(possible_keys):
                    if Key.Escape in possible_keys:
                        continue
                    else:
                        return
                else:
                    continue


    def wait_for_key_async(timeout: Optional[float] = (1/60 + 0.001)):
        key_int_seq: Deque[int] = deque()
        save_stdout_state()
        try:
            read_keys_thread_func_async(key_int_seq, timeout)
        finally:
            restore_stdout_state()
        
        return key_int_seq


    read_key = read_key_async
    readkey = read_key
    rkey = read_key


    def key(key_value: Union[str, int, Key]) -> Union[int, Key]:
        if isinstance(key_value, Key):
            return key_value

        if isinstance(key_value, int):
            return key(chr(key_value))

        if key_value.casefold().startswith('ctrl  '):
            return ctrl_key(' ')
        elif key_value.casefold().startswith('ctrl '):
            parts = key_value.split(maxsplit=1)
            return ctrl_key(parts[1])
        elif key_value.casefold().startswith('ctrl+'):
            parts = key_value.split('+', maxsplit=1)
            return ctrl_key(parts[1])
        elif key_value.casefold().startswith('ctrl-'):
            parts = key_value.split('-', maxsplit=1)
            return ctrl_key(parts[1])
        elif key_value.casefold().startswith('ctrl_'):
            parts = key_value.split('_', maxsplit=1)
            return ctrl_key(parts[1])
        elif key_value.casefold().startswith('ctrl'):
            return ctrl_key(key_value[len('ctrl'):])
        elif '\t' == key_value[0]:
            return Key.Tab
        elif '\n' == key_value[0]:
            return Key.Enter
        elif '\r' == key_value[0]:
            return Key.Enter
        elif ' ' == key_value[0]:
            return Key.Space
        else:
            return ord(key_value[0])


    min_ctrl_plus_int: int = ord('A') - ord('A') + 1
    max_ctrl_plus_int: int = ord('`') - ord('A') + 1


    def ctrl_key(key_value: str) -> Union[int, Key]:
        upper_key_value: str = key_value[0].upper()
        key_value_int: int = ord(upper_key_value)
        if (ord('A') > key_value_int) or (ord('`') < key_value_int):
            raise ValueError(f'Key "{upper_key_value}" of id "{key_value_int}" can not produce Ctrl+ sequence')
        
        if 'I' == upper_key_value:
            return Key.Tab
        elif 'M' == upper_key_value:
            return Key.Enter
        elif 'H' == upper_key_value:
            return Key.CtrlBackspace
        else:
            return ord(upper_key_value) - ord('A') + 1


    c_key = ctrl_key
    ckey = ctrl_key


    def key_str(key_id: Union[int, Key]) -> str:
        key_id = key(key_id)
        if isinstance(key_id, Key):
            return key_id.name
        elif isinstance(key_id, int):
            if (255 < key_id) or (0 > key_id):
                raise ValueError(f'Unknown key id: {key_id}')

            if min_ctrl_plus_int <= key_id <= max_ctrl_plus_int:
                real_key_id: int = key_id + ord('A') - 1
                real_key_str: str = chr(real_key_id)
                alt_ctrl_real_key: Union[int, Key] = key(ctrl_key(real_key_str))
                if isinstance(alt_ctrl_real_key, Key):
                    return alt_ctrl_real_key.name
                else:
                    return f'Ctrl+{chr(real_key_id)}'
            else:
                key_str: str = chr(key_id)
                alt_key: Union[int, Key] = key(key_str)
                if isinstance(alt_key, Key):
                    return alt_key.name
                else:
                    return key_str
        else:
            raise TypeError(f'Unsupported type ({type(key_id)}) of key id: {key_id}')


    k_str = key_str
    kstr = key_str


class Terminal(ContextDecorator):
    def __init__(self, full_screen: bool = False, mouse: bool = False, timeout: Optional[float] = 0.35) -> None:
        super().__init__()
        self._full_screen: bool = full_screen
        self._mouse: bool = mouse
        self._timeout: Optional[float] = timeout
        self._input_thread = None
    
    def __enter__(self):
        enter_term(self._full_screen, self._mouse)
        if 'Windows' != OS_TYPE:
            # See: https://stackoverflow.com/questions/46013064/why-does-terminfo-disagree-with-read
            #   , https://stackoverflow.com/questions/31641910/why-is-terminfokcuu1-eoa
            #   and https://man7.org/linux/man-pages/man5/terminfo.5.html
            nwriteStyled(''.join([chr(item) for item in unix_capabilities['smkx']]))
        
        # self._input_thread = threading.Thread(target=read_keys_thread_func, daemon=True)
        # self._input_thread.start()
        return self

    def __exit__(self, *exc):
        global _need_to_stop
        _need_to_stop = True
        # self._input_thread.join(self._timeout)
        # reset_attributes()
        if 'Windows' != OS_TYPE:
            # See: https://stackoverflow.com/questions/46013064/why-does-terminfo-disagree-with-read
            #   , https://stackoverflow.com/questions/31641910/why-is-terminfokcuu1-eoa
            #   and https://man7.org/linux/man-pages/man5/terminfo.5.html
            nwriteStyled(''.join([chr(item) for item in unix_capabilities['rmkx']]))
        
        exit_term()
        return False


terminal = Terminal
