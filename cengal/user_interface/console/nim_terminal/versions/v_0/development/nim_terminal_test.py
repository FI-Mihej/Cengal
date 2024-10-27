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

from cengal.user_interface.console.nim_terminal import *

import curses
from time import sleep


def ctrl(key: str) -> int:
    return ord(key[0].upper()) - ord('A') + 1


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


    # erase_screen()
    print('World!')
    print(terminal_size())
    print('===')
    # cursor_up()
    # erase_line()
    # print(getch())
    while True:
        key: int = getch()
        key_bin: bytes = key.to_bytes(4, 'little')

        # if key == 7:  # Ctrl+G is ASCII value 7
        if key == ctrl('g'):  # Ctrl+G is ASCII value 7
            print(f"Ctrl+G pressed: {key} (ASCII {chr(key)}) (BYTES {key_bin})\n")
            print("Ctrl+G pressed, exiting...\n")
            break
        # elif key == ord('C') - ord('A') + 1:  # Ctrl+C is ASCII value 19
        elif key == ctrl('c'):  # Ctrl+C is ASCII value 19
            print(f"Ctrl+C pressed: {key} (ASCII {chr(key)}) (BYTES {key_bin})\n")
            break
        # elif key == ord('L') - ord('A') + 1:  # Ctrl+L is ASCII value 19
        elif key == ctrl('l'):  # Ctrl+L is ASCII value 19
            print(f"Ctrl+L pressed: {key} (ASCII {chr(key)}) (BYTES {key_bin})\n")
            break
        elif key == curses.KEY_UP:
            print(f"Up arrow pressed: {key} (ASCII {chr(key)}) (BYTES {key_bin})\n")
        elif key == curses.KEY_DOWN:
            print(f"Down arrow pressed: {key} (ASCII {chr(key)}) (BYTES {key_bin})\n")
        elif key == curses.KEY_LEFT:
            print(f"Left arrow pressed: {key} (ASCII {chr(key)}) (BYTES {key_bin})\n")
        elif key == curses.KEY_RIGHT:
            print(f"Right arrow pressed: {key} (ASCII {chr(key)}) (BYTES {key_bin})\n")
        elif key == ord('S') - ord('A') + 1:  # Ctrl+S is ASCII value 19
            print(f"Ctrl+S pressed: {key} (ASCII {chr(key)}) (BYTES {key_bin})\n")
        else:
            print(f"Key pressed: {key} (ASCII {chr(key)}) (BYTES {key_bin})\n")
        
        print('-----')


if '__main__' == __name__:
    try:
        main()
    finally:
        reset_attributes()
