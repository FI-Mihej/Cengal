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
__version__ = "4.3.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from PySide6.QtCore import Qt, Slot, QObject
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)
from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
from cengal.parallel_execution.coroutines.integrations.qt import exec_common_pyside6_app, slot_common_pyside6_coro, slot_common_pyside6_implicit_coro
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import put_coro
from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.asyncio_loop import AsyncioLoopRequest
from cengal.data_generation.id_generator import IDGenerator

from cengal.introspection.inspect import is_async, is_callable, entity_properties, pdi, entity_class, entity_owner, entity_owning_module_info_and_owning_path
from pprint import pprint

from typing import Optional, Any, Callable, Dict, Type, Tuple

import asyncio
import sys
from inspect import getsourcelines, getmembers, isclass, signature, Signature, Parameter


class AutoDerivedClass:
    instance_id = IDGenerator()

    def __init__(self):
        self._instance_id: int = self.instance_id()
        self.class_name = type(self).__name__
        self.derived: Dict[Type, Type] = dict()
    
    @property
    def methods(self) -> Dict[str, Callable]:
        raise NotImplementedError
    
    def base_classes(self, base_type) -> Tuple[Type]:
        return (base_type,)
    
    def __call__(self, base_type: Type):
        base_type_name = base_type.__name__
        try:
            return self.derived[base_type_name]
        except KeyError:
            result: Type = type(f'{self.class_name}__{self._instance_id}__from__{base_type_name}', self.base_classes(base_type), self.methods)
            self.derived[base_type_name] = result
            return result


class MethodSlotHolder(AutoDerivedClass):
    ...


async def aemit(signal, *args, **kwargs):
    i: Interface = current_interface()
    def coro(i: Interface):
        signal.emit(*args, **kwargs)
    
    return await i(RunCoro, coro)


class CoroSlot(QObject):
    def __init__(self, *types: type, name: Optional[str] = None, result: Optional[str] = None) -> None:
        self._slot = Slot(*types, name, result)
        self._coro = None

    def __call__(self, coro: Coro) -> Any:
        self._coro = coro

        def func_wrapper(*args, **kwargs):
            # return coro(*args, **kwargs)
            from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
            i: Interface = current_interface()
            return i(RunCoro, cs_coro(coro), *args, **kwargs)
        
        coro_worker_sign: Signature = signature(coro)
        func_wrapper.__signature__ = coro_worker_sign.replace(parameters=tuple(coro_worker_sign.parameters.values()), return_annotation=coro_worker_sign.return_annotation)

        print('<<< Wrapper >>>')
        pdi(func_wrapper)
        pprint(entity_properties(func_wrapper))
        pprint(dir(func_wrapper))
        print(func_wrapper.__class__)
        
        print('<<< Coro >>>')
        pdi(coro)
        print('coro class:', entity_class(coro))
        print('coro owner:', entity_owner(coro))
        print('coro lines:', getsourcelines(coro))
        print('coro owner lines:', getsourcelines(entity_owner(coro)))
        # print('coro class lines:', getsourcelines(MainWindow))
        module, module_importable_str, module_file_full_path, owning_path = entity_owning_module_info_and_owning_path(coro)
        print(module, module_importable_str, module_file_full_path, owning_path)
        pprint(entity_properties(coro))
        pprint(dir(coro))
        print(coro.__class__)
        print(coro.__init_subclass__)
        print(coro.__subclasshook__)
        # return self._slot(self.func_wrapper)
        return self._slot(func_wrapper)
        return self._slot(coro)


class CoroSlotI(QObject):
    def __init__(self, *types: type, name: Optional[str] = None, result: Optional[str] = None) -> None:
        self._slot = Slot(*types, name, result)
        self._coro = None

    def __call__(self, coro: Coro) -> Any:
        self._coro = coro

        def func_wrapper(*args, **kwargs):
            # return coro(*args, **kwargs)
            from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
            i: Interface = current_interface()
            return i(RunCoro, coro, *args, **kwargs)
        
        coro_worker_sign: Signature = signature(coro)
        func_wrapper.__signature__ = coro_worker_sign.replace(parameters=tuple(coro_worker_sign.parameters.values())[1:], return_annotation=coro_worker_sign.return_annotation)
        
        print('<<< Wrapper >>>')
        pdi(func_wrapper)
        pprint(entity_properties(func_wrapper))
        pprint(dir(func_wrapper))
        print(func_wrapper.__class__)
        
        print('<<< Coro >>>')
        pdi(coro)
        print('coro class:', entity_class(coro))
        print('coro owner:', entity_owner(coro))
        print('coro lines:', getsourcelines(coro))
        print('coro owner lines:', getsourcelines(entity_owner(coro)))
        # print('coro class lines:', getsourcelines(MainWindow))
        module, module_importable_str, module_file_full_path, owning_path = entity_owning_module_info_and_owning_path(coro)
        print(module, module_importable_str, module_file_full_path, owning_path)
        pprint(entity_properties(coro))
        pprint(dir(coro))
        print(coro.__class__)
        print(coro.__init_subclass__)
        print(coro.__subclasshook__)
        # return self._slot(self.func_wrapper)
        return self._slot(func_wrapper)
        return self._slot(coro)


class CoroSlotDecorator(QObject):
    def __init__(self, *types: type, name: Optional[str] = None, result: Optional[str] = None) -> None:
        self._slot = Slot(*types, name, result)
        self._coro = None

    def __call__(self, coro: Coro) -> Any:
        self._coro = coro

        # class _Wrapper(SemiWeakRef, BaseClass):
        #     # Subclass in order to modify function's __dict__.
        #     def handle(self, *args):
        #         method = self.referent()
        #         assert method is not None, \
        #             "slot called after receiver is supposedly finalized"
        #         transform(method, args, *extra)

        #     functools.update_wrapper(handle, slot)
        #     handle.__dict__.pop("__wrapped__")  # remove strong ref to fn

        # return _Wrapper(slot, weakref.WeakMethod).handle

        def func_wrapper(self_own, *args, **kwargs):
            # return coro(self_own, *args, **kwargs)
            from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
            i: Interface = current_interface()
            return i(RunCoro, cs_coro(coro), self_own, *args, **kwargs)
        
        coro_worker_sign: Signature = signature(coro)
        func_wrapper.__signature__ = coro_worker_sign.replace(parameters=tuple(coro_worker_sign.parameters.values()), return_annotation=coro_worker_sign.return_annotation)
        
        print('<<< Wrapper >>>')
        pdi(func_wrapper)
        pprint(entity_properties(func_wrapper))
        pprint(dir(func_wrapper))
        print(func_wrapper.__class__)
        
        print('<<< Coro >>>')
        pdi(coro)
        print(entity_class(coro))
        print(entity_owner(coro))
        print('coro lines:', getsourcelines(coro))
        print('coro owner lines:', getsourcelines(entity_owner(coro)))
        # print('coro class lines:', getsourcelines(MainWindow))
        module, module_importable_str, module_file_full_path, owning_path = entity_owning_module_info_and_owning_path(coro)
        print(module, module_importable_str, module_file_full_path, owning_path)
        pprint(entity_properties(coro))
        pprint(dir(coro))
        print(coro.__class__)
        print(coro.__init_subclass__)
        print(coro.__subclasshook__)

        print('<<< Coro Module >>>')
        print('ALL MODULE MEMBERS', getmembers(module))
        # print('CLASS MODULE MEMBERS', getmembers(module, isclass))
        print('CLASS MODULE MEMBERS')
        pprint(getmembers(module, isclass))
        # print(getattr(module, 'MainWindow'))

        print('RETURNING')

        # return self._slot(self.func_wrapper)
        return self._slot(func_wrapper)
        return self._slot(coro)

    def func_wrapper(self, coro_self, *args, **kwargs):
        return self.coro(coro_self, *args, **kwargs)
        from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
        i: Interface = current_interface()
        return i(RunCoro, coro, *args, **kwargs)


class CoroSlotDecoratorI(QObject):
    def __init__(self, *types: type, name: Optional[str] = None, result: Optional[str] = None) -> None:
        self._slot = Slot(*types, name, result)
        self._coro = None

    def __call__(self, coro: Coro) -> Any:
        self._coro = coro

        # class _Wrapper(SemiWeakRef, BaseClass):
        #     # Subclass in order to modify function's __dict__.
        #     def handle(self, *args):
        #         method = self.referent()
        #         assert method is not None, \
        #             "slot called after receiver is supposedly finalized"
        #         transform(method, args, *extra)

        #     functools.update_wrapper(handle, slot)
        #     handle.__dict__.pop("__wrapped__")  # remove strong ref to fn

        # return _Wrapper(slot, weakref.WeakMethod).handle

        def func_wrapper(self_own, *args, **kwargs):
            # return coro(self_own, *args, **kwargs)
            from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
            i: Interface = current_interface()
            return i(RunCoro, cs_coro(coro), self_own, *args, **kwargs)
        
        coro_worker_sign: Signature = signature(coro)
        params = list(coro_worker_sign.parameters.values())
        print('params:', params)
        params.pop(1)
        params = tuple(params)
        func_wrapper.__signature__ = coro_worker_sign.replace(parameters=params, return_annotation=coro_worker_sign.return_annotation)
        
        print('<<< Wrapper >>>')
        pdi(func_wrapper)
        pprint(entity_properties(func_wrapper))
        pprint(dir(func_wrapper))
        print(func_wrapper.__class__)
        
        print('<<< Coro >>>')
        pdi(coro)
        print(entity_class(coro))
        print(entity_owner(coro))
        print('coro lines:', getsourcelines(coro))
        print('coro owner lines:', getsourcelines(entity_owner(coro)))
        # print('coro class lines:', getsourcelines(MainWindow))
        module, module_importable_str, module_file_full_path, owning_path = entity_owning_module_info_and_owning_path(coro)
        print(module, module_importable_str, module_file_full_path, owning_path)
        pprint(entity_properties(coro))
        pprint(dir(coro))
        print(coro.__class__)
        print(coro.__init_subclass__)
        print(coro.__subclasshook__)

        print('<<< Coro Module >>>')
        print('ALL MODULE MEMBERS', getmembers(module))
        # print('CLASS MODULE MEMBERS', getmembers(module, isclass))
        print('CLASS MODULE MEMBERS')
        pprint(getmembers(module, isclass))
        # print(getattr(module, 'MainWindow'))

        print('RETURNING')

        # return self._slot(self.func_wrapper)
        return self._slot(func_wrapper)
        return self._slot(coro)

    def func_wrapper(self, coro_self, *args, **kwargs):
        return self.coro(coro_self, *args, **kwargs)
        from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
        i: Interface = current_interface()
        return i(RunCoro, coro, *args, **kwargs)



class AsyncioCoroSlot(QObject):
    def __init__(self, *types: type, name: Optional[str] = None, result: Optional[str] = None) -> None:
        self._slot = Slot(*types, name, result)

    def __call__(self, coro: Coro) -> Any:
        def func_wrapper(*args, **kwargs):
            from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
            i: Interface = current_interface()
            if is_async(coro):
                result_coro = cs_acoro(coro)
            elif is_callable(coro):
                result_coro = cs_coro(coro)
            else:
                raise TypeError('coro must be callable or async callable')

            return i(RunCoro, result_coro, *args, **kwargs)
        
        return self._slot(func_wrapper)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QVBoxLayout(widget)

        self.text = QLabel("The answer is 42.")
        layout.addWidget(self.text, alignment=Qt.AlignmentFlag.AlignCenter)

        async_trigger = QPushButton(text="What is the question?")

        # async_trigger.clicked.connect(self.set_text)
        # async_trigger.clicked.connect(self.set_text_2)

        # async_trigger.clicked.connect(CoroSlotI(()(self.set_text))
        async_trigger.clicked.connect(CoroSlotI()(self.aset_text))

        # # async_trigger.clicked.connect(CoroSlot(()(self.set_text_3))
        # async_trigger.clicked.connect(CoroSlot()(self.aset_text_3))

        layout.addWidget(async_trigger, alignment=Qt.AlignmentFlag.AlignCenter)

    async def asyncio_coro(self, a, b):
        await asyncio.sleep(1)
        self.text.setText(f"What do you get if you multiply six by nine? {a * b}")

    # @Slot()
    # def set_text(self):
    #     put_coro(cs_acoro(self.asyncio_coro), 7, 9)

    # @CoroSlotDecorator()
    # def set_text_2(self):
    #     put_coro(cs_acoro(self.asyncio_coro), 7, 9)

    # @CoroSlotDecorator()
    # def set_text_2(self, i: Interface):
    #     return i(RunCoro, cs_acoro(self.asyncio_coro), 7, 9)

    @CoroSlotDecorator()
    def set_text_2(self):
        i: Interface = current_interface()
        return i(RunCoro, cs_acoro(self.asyncio_coro), 7, 9)

    @CoroSlotDecoratorI()
    def set_text_4(self, i: Interface):
        return i(RunCoro, cs_acoro(self.asyncio_coro), 7, 9)

    # def set_text(self):
    #     put_coro(cs_acoro(self.asyncio_coro), 7, 9)

    def set_text(self, i: Interface):
        return i(RunCoro, cs_acoro(self.asyncio_coro), 7, 9)

    async def aset_text(self, i: Interface):
        return await i(RunCoro, cs_acoro(self.asyncio_coro), 7, 9)

    def set_text_3(self):
        i: Interface = current_interface()
        return i(RunCoro, cs_acoro(self.asyncio_coro), 7, 9)

    async def aset_text_3(self):
        i: Interface = current_interface()
        return await i(RunCoro, cs_acoro(self.asyncio_coro), 7, 9)

    # @CoroSlot()
    # def set_text(i: Interface, self):
    #     return i(RunCoro, cs_acoro(self.asyncio_coro), 7, 9)

    # @slot_common_pyside6_implicit_coro()
    # async def set_text(self):
    #     a = 7
    #     b = 9
    #     await asyncio.sleep(1)
    #     self.text.setText(f"What do you get if you multiply six by nine? {a * b}")

    # @Slot()
    # def func_wrapper(*args, **kwargs):
    #     from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
    #     i: Interface = current_interface()
    #     return i(RunCoro, coro, *args, **kwargs)


import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PySide6.QtCore import Signal, Slot, QTime


class CustomSignalExample(QMainWindow):
    # Define a signal called 'currentTime' that takes a single argument
    currentTime = Signal(QTime)

    def __init__(self, parent=None):
        super(CustomSignalExample, self).__init__(parent)
        
        # Setup the UI
        self.setWindowTitle('Custom Signal Example')
        self.button = QPushButton('Get Current Time', self)
        # self.button.clicked.connect(self.emit_current_time_signal)
        self.button.clicked.connect(CoroSlot()(self.aemit_current_time_signal_1))
        # self.button.clicked.connect(CoroSlot()(self.emit_current_time_signal_2))
        self.label = QLabel('', self)
        self.label.move(50, 50)
        self.button.move(50, 80)
        self.setFixedSize(200, 150)

        # Connect the 'currentTime' signal to the 'update_time' slot
        # self.currentTime.connect(self.update_time)
        self.currentTime.connect(CoroSlot(QTime)(self.aupdate_time_1))
        # self.currentTime.connect(CoroSlot(QTime)(self.update_time_2))

    @Slot()
    def emit_current_time_signal(self):
        # When the button is clicked, emit the 'currentTime' signal with the current time
        self.currentTime.emit(QTime.currentTime())

    async def aemit_current_time_signal_1(self):
        # When the button is clicked, emit the 'currentTime' signal with the current time
        await asyncio.sleep(1)
        # self.currentTime.emit(QTime.currentTime())
        await aemit(self.currentTime, QTime.currentTime())

    def emit_current_time_signal_2(self):
        # When the button is clicked, emit the 'currentTime' signal with the current time
        i: Interface = current_interface()
        i(Sleep, 1)
        self.currentTime.emit(QTime.currentTime())

    @Slot(QTime)
    def update_time(self, time):
        # Update the label with the current time when the 'currentTime' signal is emitted
        self.label.setText(time.toString())

    async def aupdate_time_1(self, time):
        # Update the label with the current time when the 'currentTime' signal is emitted
        await asyncio.sleep(1)
        self.label.setText(time.toString())

    def update_time_2(self, time):
        # Update the label with the current time when the 'currentTime' signal is emitted
        i: Interface = current_interface()
        i(Sleep, 1)
        self.label.setText(time.toString())


def main(i: Interface):
    i._loop.suppress_coro_exceptions = False
    i(AsyncioLoopRequest().ensure_loop(interrupt_when_no_requests=True))
    i(AsyncioLoopRequest().turn_on_loops_intercommunication())
    app = QApplication(sys.argv)
    # main_window = MainWindow()
    main_window = CustomSignalExample()
    main_window.show()
    return exec_common_pyside6_app(app)


if __name__ == "__main__":
    sys.exit(run_in_loop(main))
