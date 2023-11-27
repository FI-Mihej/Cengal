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
__version__ = "4.1.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)
from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
from cengal.parallel_execution.coroutines.integrations.qt import exec_common_pyside6_app
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import put_coro
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import AsyncioLoopRequest

import asyncio
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QVBoxLayout(widget)

        self.text = QLabel("The answer is 42.")
        layout.addWidget(self.text, alignment=Qt.AlignmentFlag.AlignCenter)

        async_trigger = QPushButton(text="What is the question?")

        async_trigger.clicked.connect(self.set_text)
        layout.addWidget(async_trigger, alignment=Qt.AlignmentFlag.AlignCenter)

    async def asyncio_coro(self, a, b):
        await asyncio.sleep(1)
        self.text.setText(f"What do you get if you multiply six by nine? {a * b}")

    @Slot()
    def set_text(self):
        put_coro(cs_acoro(self.asyncio_coro), 7, 9)


def main(i: Interface):
    i(AsyncioLoopRequest().ensure_loop(interrupt_when_no_requests=True))
    i(AsyncioLoopRequest().turn_on_loops_intercommunication())
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    return exec_common_pyside6_app(app)


if __name__ == "__main__":
    sys.exit(run_in_loop(main))
