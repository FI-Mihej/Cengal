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


# __all__ = [
#     'cursor_backward', 
#     'cursor_down', 
#     'cursor_forward', 
#     'cursor_up', 
#     'erase_line', 
#     'erase_screen', 
#     'getch', 
#     'hide_cursor', 
#     'isatty', 
#     'read_password_from_stdin', 
#     'set_cursor_pos', 
#     'set_cursor_x_pos', 
#     'set_cursor_y_pos', 
#     'show_cursor', 
#     'terminal_height', 
#     'terminal_height_ioctl', 
#     'terminal_size', 
#     'terminal_width', 
#     'terminal_width_ioctl', 

#     'ncursorBackward', 
#     'ncursorDown', 
#     'ncursorForward', 
#     'ncursorUp', 
#     'neraseLine', 
#     'neraseScreen', 
#     'ngetch', 
#     'nhideCursor', 
#     'nisatty', 
#     'nreadPasswordFromStdin', 
#     'nsetCursorPos', 
#     'nsetCursorXPos', 
#     'nsetCursorYPos', 
#     'nshowCursor', 
#     'nterminalHeight', 
#     'nterminalHeightIoctl', 
#     'nterminalSize', 
#     'nterminalWidth', 
#     'nterminalWidthIoctl', 
# ]


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


from cengal.data_manipulation.conversion.hex import hex_dword_to_int
from cengal.data_manipulation.conversion.binary import bytes_to_ubint
from cengal.system import OS_TYPE
from .compilable import *

from enum import IntEnum
from typing import List, Tuple, Dict, Union, Optional, Sequence


class BackgroundColor(IntEnum):
    black = 40  # black
    red = 41  # red
    green = 42  # green
    yellow = 43  # yellow
    blue = 44  # blue
    magenta = 45  # magenta
    cyan = 46  # cyan
    white = 47  # white
    _8bit = 48  # 256-color (not supported, see `enabletruecolors` instead.)
    default = 49  # default terminal background color

    # bgBlack = 40  # black
    # bgRed = 41  # red
    # bgGreen = 42  # green
    # bgYellow = 43  # yellow
    # bgBlue = 44  # blue
    # bgMagenta = 45  # magenta
    # bgCyan = 46  # cyan
    # bgWhite = 47  # white
    # bg8Bit = 48  # 256-color (not supported, see `enableTrueColors` instead.)
    # bgDefault = 49  # default terminal background color


BC = BackgroundColor


class ForegroundColor(IntEnum):
    black = 30  # black
    red = 31  # red
    green = 32  # green
    yellow = 33  # yellow
    blue = 34  # blue
    magenta = 35  # magenta
    cyan = 36  # cyan
    white = 37  # white
    _8bit = 38  # 256-color (not supported, see `enabletruecolors` instead.)
    default = 39  # default terminal foreground color
    
    # fgBlack = 30  # black
    # fgRed = 31  # red
    # fgGreen = 32  # green
    # fgYellow = 33  # yellow
    # fgBlue = 34  # blue
    # fgMagenta = 35  # magenta
    # fgCyan = 36  # cyan
    # fgWhite = 37  # white
    # _8Bit = 38  # 256-color (not supported, see `enableTrueColors` instead.)
    # fgDefault = 39  # default terminal foreground color


FC = ForegroundColor


class Style(IntEnum):
    bright = 1  # bright text
    dim = 2  # dim text
    italic = 3  # italic (or reverse on terminals not supporting)
    underscore = 4  # underscored text
    blink = 5  # blinking/bold text
    blinkrapid = 6  # rapid blinking/bold text (not widely supported)
    reverse = 7  # reverse
    hidden = 8  # hidden text
    strikethrough = 9  # strikethrough

    # styleBright = 1  # bright text
    # styleDim = 2  # dim text
    # styleItalic = 3  # italic (or reverse on terminals not supporting)
    # styleUnderscore = 4  # underscored text
    # styleBlink = 5  # blinking/bold text
    # styleBlinkRapid = 6  # rapid blinking/bold text (not widely supported)
    # styleReverse = 7  # reverse
    # styleHidden = 8  # hidden text
    # styleStrikethrough = 9  # strikethrough


S = Style


class BackgroundStyle(IntEnum):
    default = 0  # default background brightness
    bright = 1  # bright background
    dim = 2  # dim background

    # bgStyleDefault = 0  # default background brightness
    # bgStyleBright = 1  # bright background
    # bgStyleDim = 2  # dim background


BStyle = BackgroundStyle
BS = BackgroundStyle


class TerminalCmd(IntEnum):
    reset_style = 0  # reset attributes
    fg_color = 1  # set foreground's true color
    bg_color = 2  # set background's true color

    # resetStyle = 0  # reset attributes
    # fgColor = 1  # set foreground's true color
    # bgColor = 2  # set background's true color


TC = TerminalCmd


class Color(int):
    @staticmethod
    def from_str(true_color: str) -> 'Color':
        if true_color.startswith("#"):
            true_color = true_color[1:]
        if len(true_color) != 6:
            raise ValueError("Invalid true color format")
        r = int(true_color[0:2], 16)
        g = int(true_color[2:4], 16)
        b = int(true_color[4:6], 16)
        return Color((r << 16) + (g << 8) + b)

    @staticmethod
    def from_hex_dword(true_color: str) -> 'Color':
        return Color(hex_dword_to_int(true_color, 'big'))

    @staticmethod
    def from_int(true_color: int) -> 'Color':
        return Color(true_color)

    @staticmethod
    def from_bytes(true_color: bytes) -> 'Color':
        return Color(bytes_to_ubint(true_color))


C = Color


class ForegroundTrueColor(Color):
    ...


FTC = ForegroundTrueColor


class BackgroundTrueColor(Color):
    ...


BTC = BackgroundTrueColor


def simple_args_to_write_args(args, kwargs) -> List[Dict]:
    request: List[Tuple[int, Union[str, int]]] = list()
    arg_obj: Dict = {
        'bg_style_type': BackgroundStyle.default.value,
        'bg_color_type': BackgroundColor.default.value,
        'fg_color_type': ForegroundColor.default.value,
        'style_type': list(),
        'str_type': str(),
        'has_reset_style': False,
        'has_foreground_true_color': False,
        'foreground_true_color': 0,
        'has_background_true_color': False,
        'background_true_color': 0,
    }
    style_type: List[Style] = arg_obj['style_type']
    is_terminal_cmd_fg_color: bool = None
    terminal_cmd_fg_color: bool = False
    fg_color: Optional[Color] = None
    terminal_cmd_bg_color: bool = False
    bg_color: Optional[Color] = None
    for arg in args:
        if isinstance(arg, str):
            arg_obj['style_type'] = style_type
            arg_obj['str_type'] = arg
            if terminal_cmd_fg_color and (fg_color is not None):
                arg_obj['has_foreground_true_color'] = True
                arg_obj['foreground_true_color'] = int(fg_color)
            
            if terminal_cmd_bg_color and (bg_color is not None):
                arg_obj['has_background_true_color'] = True
                arg_obj['background_true_color'] = int(bg_color)

            request.append(arg_obj)
            arg_obj = {
                'bg_style_type': BackgroundStyle.default.value,
                'bg_color_type': BackgroundColor.default.value,
                'fg_color_type': ForegroundColor.default.value,
                'style_type': list(),
                'str_type': str(),
                'has_reset_style': False,
                'has_foreground_true_color': False,
                'foreground_true_color': 0,
                'has_background_true_color': False,
                'background_true_color': 0,
            }
            style_type = arg_obj['style_type']
            is_terminal_cmd_fg_color = None
            terminal_cmd_fg_color = False
            fg_color = None
            terminal_cmd_bg_color = False
            bg_color = None
        elif isinstance(arg, BackgroundColor):
            arg_obj['bg_color_type'] = arg.value
        elif isinstance(arg, ForegroundColor):
            arg_obj['fg_color_type'] = arg.value
        elif isinstance(arg, BackgroundStyle):
            arg_obj['bg_style_type'] = int(arg)
        elif isinstance(arg, Style):
            style_type.append(arg.value)
        elif isinstance(arg, ForegroundTrueColor):
            arg_obj['has_foreground_true_color'] = True
            arg_obj['foreground_true_color'] = int(arg)
        elif isinstance(arg, BackgroundTrueColor):
            arg_obj['has_background_true_color'] = True
            arg_obj['background_true_color'] = int(arg)
        elif isinstance(arg, Color):
            if is_terminal_cmd_fg_color is not None:
                if is_terminal_cmd_fg_color:
                    fg_color = arg
                else:
                    bg_color = arg
                
                is_terminal_cmd_fg_color = None
        elif isinstance(arg, TerminalCmd):
            if TerminalCmd.reset_style == arg:
                arg_obj['has_reset_style'] = True
            elif TerminalCmd.fg_color == arg:
                is_terminal_cmd_fg_color = True
                terminal_cmd_fg_color = True
            elif TerminalCmd.bg_color == arg:
                is_terminal_cmd_fg_color = False
                terminal_cmd_bg_color = True
    
    return request


def styled_write_old(*args, args_converter=simple_args_to_write_args, **kwargs):
    nstyledWriteOld(args_converter(args, kwargs))


s_write_fast_old = styled_write_old
swrite_fast_old = styled_write_old
swrite_fo = styled_write_old
swritefo = styled_write_old


def styled_write(*args, args_converter=simple_args_to_write_args, **kwargs):
    nstyledWrite(args_converter(args, kwargs))


s_write = styled_write
swrite = styled_write


def styled_write_fast(*args, args_converter=simple_args_to_write_args, **kwargs):
    nstyledWriteFast(args_converter(args, kwargs))


s_write_fast = styled_write_fast
swrite_fast = styled_write_fast
swrite_f = styled_write_fast
swritef = styled_write_fast


def styled_write_line(*args, args_converter=simple_args_to_write_args, **kwargs):
    nstyledWriteLine(args_converter(args, kwargs))


s_write_line = styled_write_line
swrite_line = styled_write_line
swriteln = styled_write_line


def styled_echo(*args, args_converter=simple_args_to_write_args, **kwargs):
    nstyledEcho(args_converter(args, kwargs))


s_echo = styled_echo
secho = styled_echo


def ansi_style_code(style: Style) -> str:
    return nansiStyleCode(style.value)


def write_styled(txt: str, style: Optional[Sequence[Style]] = None):
    style = [Style.styleBright.value] if style is None else [item.value for item in style]
    nwriteStyled(txt, style)


def set_foreground_color(fg: ForegroundColor, bright: bool = False):
    nsetForegroundColor(fg.value, bright)


def set_background_color(bg: BackgroundColor, bright: bool = False):
    nsetBackgroundColor(bg.value, bright)


def ansi_foreground_color_code(fg: ForegroundColor, bright: bool = False) -> str:
    return nansiForegroundColorCode(fg.value, bright)


def ansi_foreground_true_color_code(color: Color) -> str:
    return nansiForegroundTrueColorCode(int(color))


def ansi_background_color_code(color: Color) -> str:
    return nansiBackgroundColorCode(int(color))


def set_foreground_true_color(color: Color):
    nsetForegroundTrueColor(int(color))


def set_background_true_color(color: Color):
    nsetBackgroundTrueColor(int(color))


def is_true_color_supported() -> bool:
    return nisTrueColorSupported()


def enable_true_colors():
    nenableTrueColors()


def disable_true_colors():
    ndisableTrueColors()


def cursor_backward(count: int = 1):
    ncursorBackward(count)


def cursor_down(count: int = 1):
    ncursorDown(count)


def cursor_forward(count: int = 1):
    ncursorForward(count)


def cursor_up(count: int = 1):
    ncursorUp(count)


def erase_line():
    neraseLine()


def erase_screen():
    neraseScreen()


def getch() -> str:
    return ngetch()


def hide_cursor():
    nhideCursor()


def isatty() -> bool:
    return nisatty()


def read_password_from_stdin(prompt: str = "password: ") -> str:
    return nreadPasswordFromStdin(prompt)


def set_cursor_pos(x: int, y: int):
    nsetCursorPos(x, y)


def set_cursor_x_pos(x: int):
    nsetCursorXPos(x)


def set_cursor_y_pos(y: int):
    if 'Windows' == OS_TYPE:
        nsetCursorYPos(y)
    else:
        raise NotImplementedError


def show_cursor():
    nshowCursor()


def terminal_height() -> int:
    return nterminalHeight()


def terminal_height_ioctl() -> int:
    return nterminalHeightIoctl()


def terminal_size() -> Tuple[int, int]:
    return nterminalSize()


def terminal_width() -> int:
    return nterminalWidth()


def terminal_width_ioctl() -> int:
    return nterminalWidthIoctl()


def reset_attributes():
    nresetAttributes()


def enter_term(full_screen: bool = True, mouse: bool = False):
    nenterTerm(full_screen, mouse)


def exit_term():
    nexitTerm()


def save_stdout_state():
    nsaveStdoutState()


def restore_stdout_state():
    nrestoreStdoutState()


def prepare_try_getch(timeout: float = 0.35) -> bool:
    timeout = 0.0 if timeout < 0.0 else timeout
    int_timeout: int = int(round(timeout * 1000))
    ms = 2147483647 if int_timeout > 2147483647 else 2147483647
    return nprepareTryGetch(ms)


def try_getch() -> Optional[int]:
    num, char_int = ntryGetch()
    if not num:
        return None
    else:
        return char_int


def win_try_getch(timeout: float = 0.35) -> Optional[int]:
    timeout = 0.0 if timeout < 0.0 else timeout
    int_timeout: int = int(round(timeout * 1000))
    ms = 2147483647 if int_timeout > 2147483647 else 2147483647
    has_ch, ch, has_vsc, vsc = nwinTryGetch(ms)
    if has_ch:
        if has_vsc:
            return (ch, vsc)
        else:
            return (ch,)
    else:
        return None
