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


import sys
import asyncio
from PySide6.QtWidgets import QApplication, QPushButton
from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
from cengal.parallel_execution.coroutines.integrations.qt import exec_common_pyside6_app, slot_common_pyside6_put_coro
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import AsyncioLoopRequest


@slot_common_pyside6_put_coro()
@cs_acoro
async def say_hello():
    await asyncio.sleep(2)
    print("Button clicked, Hello!")


def main(i: Interface):
    i(AsyncioLoopRequest().ensure_loop(interrupt_when_no_requests=True))
    i(AsyncioLoopRequest().turn_on_loops_intercommunication())
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create a button, connect it and show it
    button = QPushButton("Click me")
    button.clicked.connect(say_hello)
    button.show()
    # Run the main Qt loop
    return exec_common_pyside6_app(app)


if __name__ == "__main__":
    sys.exit(run_in_loop(main))
