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
__version__ = "4.4.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton)
from cengal.parallel_execution.coroutines.coro_scheduler import current_interface, cs_acoro
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro
from cengal.parallel_execution.coroutines.integrations.qt.pyside6 import CSlot, aemit, amodal, qt_exec_in_coro, CoroThreadWithWorker

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox
from PySide6.QtCore import Signal, Slot, QTime, QTimer

import asyncio
import sys
from datetime import datetime


class CounterWorker(CoroThreadWithWorker):
    counterChanged = Signal(int)

    def __init__(self, parent) -> None:
        super().__init__(parent, cs_acoro(self.main))

    async def main(self):
        counter = 0
        while self.allowed_to_run:
            await asyncio.sleep(0.01)
            counter += 1
            self.counterChanged.emit(counter)


class CustomSignalExample(QMainWindow):
    # Define a signal called 'currentTime' that takes a single argument
    currentTime = Signal(QTime)
    timeAsString = "" # This is the variable that will hold the result from the slot

    def __init__(self, parent=None):
        super(CustomSignalExample, self).__init__(parent)
        self.working: bool = True
        
        # Setup the UI
        self.setWindowTitle('Custom Signal Example')

        self.button_modal = QPushButton('Show Modal', self)
        self.button_modal.setFixedSize(150, 30)  # Set the button size to be 150x30
        self.button_modal.clicked.connect(self.emit_show_modal_signal)
        self.button_modal.move(50, 20)

        self.button = QPushButton('Get Current Time', self)
        self.button.setFixedSize(150, 30)  # Set the button size to be 150x30
        self.button.clicked.connect(self.emit_current_time_signal)
        self.label = QLabel('', self)
        self.label.move(50, 50)
        self.button.move(50, 80)
        self.counterLabel = QLabel("0", self)
        self.counterLabel.move(50, 120)
        self.coroCounterLabel = QLabel("0", self)
        self.coroCounterLabel.move(100, 120)
        self.threadCounterLabel = QLabel("0", self)
        self.threadCounterLabel.move(150, 120)
        self.setFixedSize(250, 150)

        # Connect the 'currentTime' signal to the 'update_time' slot
        self.currentTime.connect(self.update_time)

        # Set up a counter and a timer to update it every second
        self.counter = 0
        self.coro_counter = 0
        self.counter_update_interval = 250  # ms
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_counter)
        self.timer.start(self.counter_update_interval)  # Interval of 1000ms
        self.coro_counter_updating_coro_id = current_interface()(PutCoro, cs_acoro(self.update_counter_coro))

        self.worker = CounterWorker(self)
        self.worker.counterChanged.connect(lambda counter: self.threadCounterLabel.setText(str(counter)))
        self.worker.start()
    
    def closeEvent(self, event):
        QMessageBox.information(self, "Goodbye", "The window is being closed.")
        self.working = False
        self.worker.stop()
        event.accept()

    async def ashow_dialog(self):
        return await amodal(QMessageBox.information, None, "Hit 100", "Click OK when you think you hit 100.")
    
    @Slot()
    def emit_show_modal_signal(self):
        QMessageBox.information(None, "Hit 100", "Click OK when you think you hit 100.")

    @CSlot()
    async def emit_current_time_signal(self):
        await self.ashow_dialog()
        await asyncio.sleep(1)
        # When the button is clicked, emit the 'currentTime' signal with the current time
        await aemit(self.currentTime, QTime.currentTime())

    @CSlot(QTime)
    async def update_time(self, time):
        await asyncio.sleep(1)
        # Update the label with the current time when the 'currentTime' signal is emitted
        time_string = time.toString()
        self.label.setText(time_string)
        # Store the time string as an attribute of the instance
        self.timeAsString = time_string
        print(f'{datetime.now()}>> update_counter: {time_string}')

    @CSlot()
    def update_counter(self):
        # Increase the counter and update the label
        self.counter += 1
        self.counterLabel.setText(str(self.counter))
    
    async def update_counter_coro(self):
        while self.working:
            await asyncio.sleep(self.counter_update_interval / 1000)
            # Increase the counter and update the label
            self.coro_counter += 1
            self.coroCounterLabel.setText(str(self.coro_counter))


@qt_exec_in_coro
def main():
    app = QApplication(sys.argv)
    mainWin = CustomSignalExample()
    mainWin.show()
    return app


if __name__ == "__main__":
    sys.exit(run_in_loop(main))
