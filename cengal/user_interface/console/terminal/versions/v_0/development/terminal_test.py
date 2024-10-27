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


__all__ = []


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

from cengal.user_interface.console.terminal import *
from cengal.code_inspection.auto_line_tracer import tr, tl
from cengal.performance_test_lib import mtimetl

from time import sleep
from typing import Union


@terminal()
def main():
    w, h = terminal_size()
    erase_screen()
    set_cursor_pos(0, 0)
    secho(Style.bright, Style.blink, Style.underscore, Style.strikethrough, "styled text 1. ")
    secho(ForegroundColor.green, BackgroundColor.red, "styled text 2. ")
    print('Hello')
    secho(Style.bright, Style.blink, Style.underscore, ForegroundColor.yellow, BackgroundColor.magenta, "styled text 3.1. ")
    secho(Style.dim, Style.blink, Style.underscore, ForegroundColor.yellow, BackgroundColor.magenta, "styled text 3.2. ")
    secho(Style.blink, Style.underscore, ForegroundColor.yellow, BackgroundColor.magenta, "styled text 3.3. ")

    sprint(st('Hello').dim.underscore.fyellow.bmagenta, ', ', st('World').bright.underscore.fyellow.bmagenta)
    sprint(st(st('Hello').dim.unde.fyel.bmag, ', ', st('World').brig.unde.fyel.bmag, ' my dear friends', st('!').fred.bdef, st('!').fmag, '!').bblu)

    sprint(st(st('Hello').dim.unde.fyel.bmag, ', ', st('World').brig.unde.fyel.bmag, ' my ', st('dear').fbla.fc(Color.from_hex_dword('00112233')), ' friends', st('!').fred.bdef, st('!').fmag, '!').bblu)
    if is_true_color_supported():
        sprint(st('TrueColors - Supported!').b_green.f_blue)
        enable_true_colors()
    else:
        sprint(st('TrueColors - NOT Supported!').b_red.f_yellow)

    sprint(st(st('Hello').dim.unde.fyel.bmag, ', ', st('World').brig.unde.fyel.bmag, ' my ', st('dear').fbla.fc(Color.from_hex_dword('00112233')), ' friends', st('!').fred.bdef, st('!').fmag, '!').bblu)
    sprint(st(st('Hello').dim.unde.fyel.bmag, ', ', st(', ').res_style, ', ', st('World').brig.unde.fyel.bmag, ' my ', st('dear').fbla.fc(Color.from_hex_dword('00112233')), ' friends', st('!').fred.bdef, st('!').fmag, '!').bblu)

    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_default, ' b_default')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_default.bs_dim, ' b_default bs_dim')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_default.bs_bright, ' b_default bs_bright')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_black, ' b_black')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_black.bs_dim, ' b_black bs_dim')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_black.bs_bright, ' b_black bs_bright')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_red, ' b_red')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_red.bs_dim, ' b_red bs_dim')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_red.bs_bright, ' b_red bs_bright')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_green, ' b_green')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_green.bs_dim, ' b_green bs_dim')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_green.bs_bright, ' b_green bs_bright')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_yellow, ' b_yellow')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_yellow.bs_dim, ' b_yellow bs_dim')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_yellow.bs_bright, ' b_yellow bs_bright')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_blue, ' b_blue')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_blue.bs_dim, ' b_blue bs_dim')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_blue.bs_bright, ' b_blue bs_bright')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_magenta, ' b_magenta')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_magenta.bs_dim, ' b_magenta bs_dim')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_magenta.bs_bright, ' b_magenta bs_bright')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_cyan, ' b_cyan')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_cyan.bs_dim, ' b_cyan bs_dim')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_cyan.bs_bright, ' b_cyan bs_bright')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_white, ' b_white')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_white.bs_dim, ' b_white bs_dim')
    fill_current_line(st(' ').b_cyan.bs_dim)
    sprint(st(st('0').fdef, st('0').fdef.brig, st('0').fbla, st('0').fbla.brig, st('0').fred, st('0').fred.brig, 
              st('0').fgre, st('0').fgre.brig, st('0').fyel, st('0').fyel.brig, st('0').fblu, st('0').fblu.brig, 
              st('0').fmag, st('0').fmag.brig, st('0').fcya, st('0').fcya.brig, st('0').fwhi, st('0').fwhi.brig).b_white.bs_bright, ' b_white bs_bright')


    # sprint(st(st('0').fdef, st('0').fbla, st('0').fred, st('0').fgre, st('0').fyel, st('0').fblu, st('0').fmag, st('0').fcya, st('0').fwhi,
    #           st('0').fdef.brig, st('0').fbla.brig, st('0').fred.brig, st('0').fgre.brig, st('0').fyel.brig, st('0').fblu.brig, st('0').fmag.brig, st('0').fcya.brig, st('0').fwhi.brig).b_black)
    # sprint(st(st('0').fdef, st('0').fbla, st('0').fred, st('0').fgre, st('0').fyel, st('0').fblu, st('0').fmag, st('0').fcya, st('0').fwhi,
    #           st('0').fdef.brig, st('0').fbla.brig, st('0').fred.brig, st('0').fgre.brig, st('0').fyel.brig, st('0').fblu.brig, st('0').fmag.brig, st('0').fcya.brig, st('0').fwhi.brig).b_red)
    # sprint(st(st('0').fdef, st('0').fbla, st('0').fred, st('0').fgre, st('0').fyel, st('0').fblu, st('0').fmag, st('0').fcya, st('0').fwhi,
    #           st('0').fdef.brig, st('0').fbla.brig, st('0').fred.brig, st('0').fgre.brig, st('0').fyel.brig, st('0').fblu.brig, st('0').fmag.brig, st('0').fcya.brig, st('0').fwhi.brig).b_green)
    # sprint(st(st('0').fdef, st('0').fbla, st('0').fred, st('0').fgre, st('0').fyel, st('0').fblu, st('0').fmag, st('0').fcya, st('0').fwhi,
    #           st('0').fdef.brig, st('0').fbla.brig, st('0').fred.brig, st('0').fgre.brig, st('0').fyel.brig, st('0').fblu.brig, st('0').fmag.brig, st('0').fcya.brig, st('0').fwhi.brig).b_yellow)
    # sprint(st(st('0').fdef, st('0').fbla, st('0').fred, st('0').fgre, st('0').fyel, st('0').fblu, st('0').fmag, st('0').fcya, st('0').fwhi,
    #           st('0').fdef.brig, st('0').fbla.brig, st('0').fred.brig, st('0').fgre.brig, st('0').fyel.brig, st('0').fblu.brig, st('0').fmag.brig, st('0').fcya.brig, st('0').fwhi.brig).b_blue)
    # sprint(st(st('0').fdef, st('0').fbla, st('0').fred, st('0').fgre, st('0').fyel, st('0').fblu, st('0').fmag, st('0').fcya, st('0').fwhi,
    #           st('0').fdef.brig, st('0').fbla.brig, st('0').fred.brig, st('0').fgre.brig, st('0').fyel.brig, st('0').fblu.brig, st('0').fmag.brig, st('0').fcya.brig, st('0').fwhi.brig).b_magenta)
    # sprint(st(st('0').fdef, st('0').fbla, st('0').fred, st('0').fgre, st('0').fyel, st('0').fblu, st('0').fmag, st('0').fcya, st('0').fwhi,
    #           st('0').fdef.brig, st('0').fbla.brig, st('0').fred.brig, st('0').fgre.brig, st('0').fyel.brig, st('0').fblu.brig, st('0').fmag.brig, st('0').fcya.brig, st('0').fwhi.brig).b_cyan)
    # sprint(st(st('0').fdef, st('0').fbla, st('0').fred, st('0').fgre, st('0').fyel, st('0').fblu, st('0').fmag, st('0').fcya, st('0').fwhi,
    #           st('0').fdef.brig, st('0').fbla.brig, st('0').fred.brig, st('0').fgre.brig, st('0').fyel.brig, st('0').fblu.brig, st('0').fmag.brig, st('0').fcya.brig, st('0').fwhi.brig).b_white)

    # erase_screen()
    print('World!')
    print(terminal_size())
    print('===')
    # cursor_up()
    # erase_line()
    # print(getch())
    while True:
        # key_int: int = getch()
        # key_int: KeyId = rkey(None)
        # with mtimetl():
        key_int: KeyId = rkey()
            
        if key_int is None:
            continue

        key_string: str = None
        try:
            key_string = kstr(key_int)
        except ValueError:
            pass

        key_bin: bytes = None
        try:
            if isinstance(key_int, int):
                key_bin: bytes = key_int.to_bytes(4, 'little')
        except OverflowError:
            pass

        # if key_int == 7:  # Ctrl+G is ASCII value 7
        if key_int == ctrl_key('g'):  # Ctrl+G is ASCII value 7
            print(f"Ctrl+G pressed: {key_int} (ASCII {key_string}) (BYTES {key_bin})\n")
            print("Ctrl+G pressed, exiting...\n")
            # break
        # elif key_int == ord('C') - ord('A') + 1:  # Ctrl+C is ASCII value 19
        elif key_int == ctrl_key('c'):  # Ctrl+C is ASCII value 19
            print(f"Ctrl+C pressed: {key_int} (ASCII {key_string}) (BYTES {key_bin})\n")
            break
        # elif key_int == ord('L') - ord('A') + 1:  # Ctrl+L is ASCII value 19
        elif key_int == ctrl_key('l'):  # Ctrl+L is ASCII value 19
            print(f"Ctrl+L pressed: {key_int} (ASCII {key_string}) (BYTES {key_bin})\n")
            break
        elif key_int == 7:  # Ctrl+g is ASCII value 19
            print(f"Ctrl+g pressed: {key_int} (ASCII {key_string}) (BYTES {key_bin})\n")
            # break
        elif key_int == ord('S') - ord('A') + 1:  # Ctrl+S is ASCII value 19
            print(f"Ctrl+S pressed: {key_int} (ASCII {key_string}) (BYTES {key_bin})\n")
        else:
            if key('\r') == key_int:
                print(f"Key pressed: {key_int} (ASCII {key_string}) (BYTES {key_bin})\n")
            elif key('\t') == key_int:
                print(f"Key pressed: {key_int} (ASCII {key_string}) (BYTES {key_bin})\n")
            else:
                # print(f"Key pressed: {key_int} (ASCII \\r) (BYTES {key_bin})+\n")
                print(f"Key pressed: {key_int} (ASCII {key_string}) (BYTES {key_bin})\n")
        
        print('-----')


if '__main__' == __name__:
    main()
    pass
