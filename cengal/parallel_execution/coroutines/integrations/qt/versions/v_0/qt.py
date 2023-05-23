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


__all__ = [
    'exec_common_pyside_app', 
    'exec_common_pyside2_app', 
    'exec_common_pyside6_app', 
    'exec_common_pyqt4_app', 
    'exec_common_pyqt5_app', 
    'exec_common_pyqt6_app',
    'slot_common_pyside_gly_patched',
    'slot_common_pyside_coro',
    'slot_common_pyside_put_coro',
    'slot_common_pyside2_gly_patched',
    'slot_common_pyside2_coro',
    'slot_common_pyside2_put_coro',
    'slot_common_pyside6_gly_patched',
    'slot_common_pyside6_coro',
    'slot_common_pyside6_put_coro',
    'slot_common_pyqt4_gly_patched',
    'slot_common_pyqt4_coro',
    'slot_common_pyqt4_put_coro',
    'slot_common_pyqt5_gly_patched',
    'slot_common_pyqt5_coro',
    'slot_common_pyqt5_put_coro',
    'slot_common_pyqt6_gly_patched',
    'slot_common_pyqt6_coro',
    'slot_common_pyqt6_put_coro',
]


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.2.2"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.parallel_execution.coroutines.coro_scheduler import CoroScheduler, Interface, current_interface
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import gly, CoroPriority, gly_patch
from typing import Optional


class WrongQtVersion(Exception):
    pass


def exec_common_pyside_app(app, default_priority: CoroPriority = CoroPriority.normal) -> int:
    from PySide.QtWidgets import QApplication
    from PySide.QtCore import QTimer
    if not isinstance(app, QApplication):
        raise WrongQtVersion('Qt version is not PySide')
    
    timer = QTimer()
    ly = gly(default_priority)
    def yield_func():
        ly()

    timer.timeout.connect(yield_func)
    timer.start(0)
    def cleanup_callback():
        timer.stop()

    app.aboutToQuit.connect(cleanup_callback)
    return app.exec_()


def exec_common_pyside2_app(app, default_priority: CoroPriority = CoroPriority.normal) -> int:
    from PySide2.QtWidgets import QApplication
    from PySide2.QtCore import QTimer
    if not isinstance(app, QApplication):
        raise WrongQtVersion('Qt version is not PySide2')
    
    timer = QTimer()
    ly = gly(default_priority)
    def yield_func():
        ly()

    timer.timeout.connect(yield_func)
    timer.start(0)
    def cleanup_callback():
        timer.stop()

    app.aboutToQuit.connect(cleanup_callback)
    return app.exec_()


def exec_common_pyside6_app(app, default_priority: CoroPriority = CoroPriority.normal) -> int:
    from PySide6.QtWidgets import QApplication
    from PySide6.QtCore import QTimer
    if not isinstance(app, QApplication):
        raise WrongQtVersion('Qt version is not PySide6')
    
    timer = QTimer()
    ly = gly(default_priority)
    def yield_func():
        ly()

    timer.timeout.connect(yield_func)
    timer.start(0)
    def cleanup_callback():
        timer.stop()

    app.aboutToQuit.connect(cleanup_callback)
    return app.exec()


# def exec_common_pyside6_app(app, default_priority: CoroPriority = CoroPriority.normal) -> int:
#     from PySide6.QtWidgets import QApplication
#     from PySide6.QtCore import QTimer
#     if not isinstance(app, QApplication):
#         raise WrongQtVersion('Qt version is not PySide6')
    
#     ly = gly(default_priority)
#     def yield_func():
#         ly()
#         QTimer.singleShot(0, yield_func)

#     QTimer.singleShot(0, yield_func)
#     return app.exec()


def exec_common_pyqt4_app(app, default_priority: CoroPriority = CoroPriority.normal) -> int:
    from PyQt4.QtWidgets import QApplication
    from PyQt4.QtCore import QTimer
    if not isinstance(app, QApplication):
        raise WrongQtVersion('Qt version is not PyQt4')
    
    timer = QTimer()
    ly = gly(default_priority)
    def yield_func():
        ly()

    timer.timeout.connect(yield_func)
    timer.start(0)
    def cleanup_callback():
        timer.stop()

    app.aboutToQuit.connect(cleanup_callback)
    return app.exec()


def exec_common_pyqt5_app(app, default_priority: CoroPriority = CoroPriority.normal) -> int:
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import QTimer
    if not isinstance(app, QApplication):
        raise WrongQtVersion('Qt version is not PyQt5')
    
    timer = QTimer()
    ly = gly(default_priority)
    def yield_func():
        ly()

    timer.timeout.connect(yield_func)
    timer.start(0)
    def cleanup_callback():
        timer.stop()

    app.aboutToQuit.connect(cleanup_callback)
    return app.exec()


def exec_common_pyqt6_app(app, default_priority: CoroPriority = CoroPriority.normal) -> int:
    from PyQt6.QtWidgets import QApplication
    from PyQt6.QtCore import QTimer
    if not isinstance(app, QApplication):
        raise WrongQtVersion('Qt version is not PyQt6')
    
    timer = QTimer()
    ly = gly(default_priority)
    def yield_func():
        ly()

    timer.timeout.connect(yield_func)
    timer.start(0)
    def cleanup_callback():
        timer.stop()

    app.aboutToQuit.connect(cleanup_callback)
    return app.exec()


# def exec_common_pyqt6_app(app, default_priority: CoroPriority = CoroPriority.normal) -> int:
#     from PyQt6.QtWidgets import QApplication
#     from PyQt6.QtCore import QTimer
#     if not isinstance(app, QApplication):
#         raise WrongQtVersion('Qt version is not PyQt6')
    
#     ly = gly(default_priority)
#     def yield_func():
#         ly()
#         QTimer.singleShot(0, yield_func)

#     QTimer.singleShot(0, yield_func)
#     return app.exec()


# ======================================================================================================================


# === PySide ====


def slot_common_pyside_gly_patched(*slot_args, **slot_kwargs):
    def wrapper(func):
        from PySide.QtCore import Slot
        return Slot(*slot_args, **slot_kwargs)(gly_patch(func))

    return wrapper


def slot_common_pyside_coro(*slot_args, **slot_kwargs):
    def wrapper(coro):
        from PySide.QtCore import Slot
        @Slot(*slot_args, **slot_kwargs)
        def func_wrapper(*args, **kwargs):
            from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
            i: Interface = current_interface()
            i(RunCoro, coro, *args, **kwargs)
        
        return func_wrapper

    return wrapper


def slot_common_pyside_put_coro(*slot_args, **slot_kwargs):
    def wrapper(coro):
        from PySide.QtCore import Slot
        @Slot(*slot_args, **slot_kwargs)
        def func_wrapper(*args, **kwargs):
            from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import put_coro
            put_coro(coro, *args, **kwargs)
        
        return func_wrapper

    return wrapper


# === PySide2 ====


def slot_common_pyside2_gly_patched(*slot_args, **slot_kwargs):
    def wrapper(func):
        from PySide2.QtCore import Slot
        return Slot(*slot_args, **slot_kwargs)(gly_patch(func))

    return wrapper


def slot_common_pyside2_coro(*slot_args, **slot_kwargs):
    def wrapper(coro):
        from PySide2.QtCore import Slot
        @Slot(*slot_args, **slot_kwargs)
        def func_wrapper(*args, **kwargs):
            from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
            i: Interface = current_interface()
            i(RunCoro, coro, *args, **kwargs)
        
        return func_wrapper

    return wrapper


def slot_common_pyside2_put_coro(*slot_args, **slot_kwargs):
    def wrapper(coro):
        from PySide2.QtCore import Slot
        @Slot(*slot_args, **slot_kwargs)
        def func_wrapper(*args, **kwargs):
            from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import put_coro
            put_coro(coro, *args, **kwargs)
        
        return func_wrapper

    return wrapper


# === PySide6 ====


def slot_common_pyside6_gly_patched(*slot_args, **slot_kwargs):
    def wrapper(func):
        from PySide6.QtCore import Slot
        return Slot(*slot_args, **slot_kwargs)(gly_patch(func))

    return wrapper


def slot_common_pyside6_coro(*slot_args, **slot_kwargs):
    def wrapper(coro):
        from PySide6.QtCore import Slot
        @Slot(*slot_args, **slot_kwargs)
        def func_wrapper(*args, **kwargs):
            from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
            i: Interface = current_interface()
            i(RunCoro, coro, *args, **kwargs)
        
        return func_wrapper

    return wrapper


def slot_common_pyside6_put_coro(*slot_args, **slot_kwargs):
    def wrapper(coro):
        from PySide6.QtCore import Slot
        @Slot(*slot_args, **slot_kwargs)
        def func_wrapper(*args, **kwargs):
            from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import put_coro
            put_coro(coro, *args, **kwargs)
        
        return func_wrapper

    return wrapper


# === PyQt4 ====


def slot_common_pyqt4_gly_patched(*slot_args, **slot_kwargs):
    def wrapper(func):
        from PyQt4.QtCore import pyqtSlot
        return pyqtSlot(*slot_args, **slot_kwargs)(gly_patch(func))

    return wrapper


def slot_common_pyqt4_coro(*slot_args, **slot_kwargs):
    def wrapper(coro):
        from PyQt4.QtCore import pyqtSlot
        @pyqtSlot(*slot_args, **slot_kwargs)
        def func_wrapper(*args, **kwargs):
            from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
            i: Interface = current_interface()
            i(RunCoro, coro, *args, **kwargs)
        
        return func_wrapper

    return wrapper


def slot_common_pyqt4_put_coro(*slot_args, **slot_kwargs):
    def wrapper(coro):
        from PyQt4.QtCore import pyqtSlot
        @pyqtSlot(*slot_args, **slot_kwargs)
        def func_wrapper(*args, **kwargs):
            from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import put_coro
            put_coro(coro, *args, **kwargs)
        
        return func_wrapper

    return wrapper


# === PyQt5 ====


def slot_common_pyqt5_gly_patched(*slot_args, **slot_kwargs):
    def wrapper(func):
        from PyQt5.QtCore import pyqtSlot
        return pyqtSlot(*slot_args, **slot_kwargs)(gly_patch(func))

    return wrapper


def slot_common_pyqt5_coro(*slot_args, **slot_kwargs):
    def wrapper(coro):
        from PyQt5.QtCore import pyqtSlot
        @pyqtSlot(*slot_args, **slot_kwargs)
        def func_wrapper(*args, **kwargs):
            from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
            i: Interface = current_interface()
            i(RunCoro, coro, *args, **kwargs)
        
        return func_wrapper

    return wrapper


def slot_common_pyqt5_put_coro(*slot_args, **slot_kwargs):
    def wrapper(coro):
        from PyQt5.QtCore import pyqtSlot
        @pyqtSlot(*slot_args, **slot_kwargs)
        def func_wrapper(*args, **kwargs):
            from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import put_coro
            put_coro(coro, *args, **kwargs)
        
        return func_wrapper

    return wrapper


# === PyQt6 ====


def slot_common_pyqt6_gly_patched(*slot_args, **slot_kwargs):
    def wrapper(func):
        from PyQt6.QtCore import pyqtSlot
        return pyqtSlot(*slot_args, **slot_kwargs)(gly_patch(func))

    return wrapper


def slot_common_pyqt6_coro(*slot_args, **slot_kwargs):
    def wrapper(coro):
        from PyQt6.QtCore import pyqtSlot
        @pyqtSlot(*slot_args, **slot_kwargs)
        def func_wrapper(*args, **kwargs):
            from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
            i: Interface = current_interface()
            i(RunCoro, coro, *args, **kwargs)
        
        return func_wrapper

    return wrapper


def slot_common_pyqt6_put_coro(*slot_args, **slot_kwargs):
    def wrapper(coro):
        from PyQt6.QtCore import pyqtSlot
        @pyqtSlot(*slot_args, **slot_kwargs)
        def func_wrapper(*args, **kwargs):
            from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import put_coro
            put_coro(coro, *args, **kwargs)
        
        return func_wrapper

    return wrapper
