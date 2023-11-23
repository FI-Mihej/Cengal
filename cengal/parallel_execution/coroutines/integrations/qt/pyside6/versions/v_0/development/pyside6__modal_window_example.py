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
__version__ = "4.1.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"




from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton)
from cengal.parallel_execution.coroutines.coro_scheduler import Interface
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import AsyncioLoopRequest
from cengal.parallel_execution.coroutines.integrations.qt.pyside6 import CoroSlot, aemit, execa

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PySide6.QtCore import Signal, QTime

import asyncio
import sys

import asyncio
import qtinter
from PySide6 import QtWidgets

async def main():
    async def counter():
        nonlocal n
        while True:
            print(f"\r{n}", end='', flush=True)
            await asyncio.sleep(0.025)
            n += 1

    n = 0
    counter_task = asyncio.create_task(counter())
    await qtinter.modal(QtWidgets.QMessageBox.information)(
        None, "Hit 100", "Click OK when you think you hit 100.")
    counter_task.cancel()
    if n == 100:
        print("\nYou did it!")
    else:
        print("\nTry again!")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    with qtinter.using_qt_from_asyncio():
        asyncio.run(main())


def main(i: Interface):
    i._loop.suppress_coro_exceptions = False
    i(AsyncioLoopRequest().ensure_loop(interrupt_when_no_requests=True))
    i(AsyncioLoopRequest().turn_on_loops_intercommunication())
    app = QtWidgets.QApplication([])
    main_window = CustomSignalExample()
    main_window.show()
    return execa(app)


if __name__ == "__main__":
    sys.exit(run_in_loop(main))
