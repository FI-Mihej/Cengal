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


import time
from typing import List

import pytermgui as ptg
from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.integrations.pytermgui import WindowManagerCS
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro


class Model:
    def __init__(self):
        self.all_formats: List[str] = [
            None, "%H:%M:%S", "%c", "%I:%M:%S %p", "%x", "%I:%M %p", "%X", "%H:%M",
        ]
        self.current_format_index = 0
        self.current_format = self.all_formats[self.current_format_index]


def ui_setup(window_manager: ptg.WindowManager, model: Model):
    def macro_time(fmt: str) -> str:
        return time.strftime(fmt if model.current_format is None else model.current_format)

    ptg.tim.define("!time", macro_time)
    window_manager.layout.add_slot("Body")
    window_manager.add(
        ptg.Window("[bold]The current time is:[/]\n\n[!time 75]%c", box="EMPTY")
    )


async def periodic_format_changer(i: Interface, model: Model):
    while await i(Sleep, 1.5):
        model.current_format_index += 1
        if model.current_format_index >= len(model.all_formats):
            model.current_format_index = 0
        
        model.current_format = model.all_formats[model.current_format_index]


async def controller_loop_setup(i: Interface, model: Model):
    await i(PutCoro, periodic_format_changer, model)


if __name__ == "__main__":
    with ptg.WindowManager() as manager:
        manager: WindowManagerCS = WindowManagerCS.replace(manager, Model(), ui_setup, controller_loop_setup)
