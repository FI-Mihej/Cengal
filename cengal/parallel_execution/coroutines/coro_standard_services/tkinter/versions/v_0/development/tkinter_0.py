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
__version__ = "4.2.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.tkinter import TkinterContextManager
from cengal.parallel_execution.coroutines.integrations.customtkinter import prepare_mainloop
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_on_keyboard_interrupt import ShutdownOnKeyboardInterrupt
from cengal.parallel_execution.coroutines.coro_tools.wait_coro import sync_coro
from cengal.parallel_execution.coroutines.coro_standard_services.lazy_print import lprint

from time import perf_counter

import tkinter


def tkinter_main(i: Interface):
    i(ShutdownOnKeyboardInterrupt)
    with(TkinterContextManager(i, None)) as wr:
        wr.set_update_period(1 / 240)
        root = wr.tk
        root.geometry("700x650")
        win_handler = int(wr.tk.frame(), 0)
        print(f'Window {win_handler}')
        wr.put_coro(rotator, wr, 1/240, 0.5)


def rotator(i, root, interval, d_per_tick):
    # canvas = tkinter.Canvas(root.tk, height=600, width=600, outline="")
    canvas = tkinter.Canvas(root.tk, height=600, width=600)
    canvas.pack()
    deg = 0
    color = 'black'
    arc = canvas.create_arc(100, 100, 500, 500, style=tkinter.CHORD,
                            start=0, extent=deg, fill=color, width=1)
    
    start = perf_counter()
    while i(Sleep, interval):
        end = perf_counter()
        tdelta = end - start
        tick_deg = (tdelta / interval) * d_per_tick
        deg, color = deg_color(deg, tick_deg, color)
        canvas.itemconfigure(arc, extent=deg, fill=color)
        start = perf_counter()


def deg_color(deg, d_per_tick, color):
    from random import randrange as rr
    deg += d_per_tick
    if 360 <= deg:
        deg %= 360
        color = '#%02x%02x%02x' % (rr(0, 256), rr(0, 256), rr(0, 256))
    return deg, color


def main():
    run_in_loop(tkinter_main)


if '__main__' == __name__:
    main()
