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
__version__ = "4.3.2"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from multiprocessing import Process, Queue

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Setup the UI
        self.setWindowTitle('Application Restart Example')
        self.button = QPushButton('Restart Application', self)
        self.button.setFixedSize(150, 30)
        self.button.move(50, 50)
        self.button.clicked.connect(self.restart_application)
        self.setFixedSize(250, 150)

    def restart_application(self):
        QApplication.exit(1000)  # Special exit code for restarting the application

def main(queue):
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    ret = app.exec()
    queue.put(ret)
    return ret

if __name__ == "__main__":
    ret = 1000
    while ret == 1000:
        queue = Queue()
        process = Process(target=main, args=(queue,))
        process.start()
        process.join()
        ret = queue.get()  # Get the exit code from the queue
