#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.2.0"
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

from datetime import datetime
import tkinter
import customtkinter


def custom_tkinter_main(i: Interface):
    i(ShutdownOnKeyboardInterrupt)
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    original_app = customtkinter.CTk()
    with(TkinterContextManager(i, original_app)) as wr:
        app: customtkinter.CTk = wr.tk

        app.geometry("400x240")

        @sync_coro
        def button_function(i: Interface):
            lprint(f'{datetime.now()} >> button pressed - start...')
            i(Sleep, 0.01)
            lprint(f'{datetime.now()} >> button pressed - done.')

        button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
        button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        prepare_mainloop(app)


def main():
    run_in_loop(custom_tkinter_main)


if '__main__' == __name__:
    main()
