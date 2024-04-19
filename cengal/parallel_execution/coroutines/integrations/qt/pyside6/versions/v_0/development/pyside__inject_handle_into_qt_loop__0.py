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
__version__ = "4.3.4"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PySide6.QtCore import Signal, Slot, QTime, QTimer

class CustomSignalExample(QMainWindow):
    # Define a signal called 'currentTime' that takes a single argument
    currentTime = Signal(QTime)
    timeAsString = "" # This is the variable that will hold the result from the slot

    def __init__(self, parent=None):
        super(CustomSignalExample, self).__init__(parent)
        
        # Setup the UI
        self.setWindowTitle('Custom Signal Example')
        self.button = QPushButton('Get Current Time', self)
        self.button.setFixedSize(150, 30)  # Set the button size to be 150x30
        self.button.clicked.connect(self.emit_current_time_signal)
        self.label = QLabel('', self)
        self.label.move(50, 50)
        self.button.move(50, 80)
        self.counterLabel = QLabel("0", self)
        self.counterLabel.move(50, 120)
        self.setFixedSize(250, 150)

        # Connect the 'currentTime' signal to the 'update_time' slot
        self.currentTime.connect(self.update_time)

        # Set up a counter and a timer to update it every second
        self.counter = 0
        self.timer = QTimer(self)
        # Use a lambda function as the timer's timeout handler
        self.timer.timeout.connect(lambda: self.counterLabel.setText(str(self.counter)))
        self.timer.timeout.connect(lambda: setattr(self, 'counter', self.counter + 1))
        self.timer.start(1000)  # Interval of 1000ms

    @Slot()
    def emit_current_time_signal(self):
        # When the button is clicked, emit the 'currentTime' signal with the current time
        self.currentTime.emit(QTime.currentTime())

    @Slot(QTime)
    def update_time(self, time):
        # Update the label with the current time when the 'currentTime' signal is emitted
        time_string = time.toString()
        self.label.setText(time_string)
        # Store the time string as an attribute of the instance
        self.timeAsString = time_string


def main():
    app = QApplication(sys.argv)

    mainWin = CustomSignalExample()
    mainWin.show()

    # Run the event loop
    ret = app.exec()

    # Print the time string after the event loop has finished
    print(mainWin.timeAsString)

    sys.exit(ret)


if __name__ == "__main__":
    main()
