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


__all__ = ['WindowManagerCS', 'CompositorCS', 'TerminalApplication', 'TermApp']


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import put_coro_to
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_loop import ShutdownLoop
from cengal.parallel_execution.coroutines.coro_tools.prepare_loop import prepare_loop
from cengal.code_flow_control.smart_values import ValueExistence
from cengal.data_manipulation.conversion.reinterpret_cast import reinterpret_cast

from pytermgui import WindowManager as PTGWindowManager
from pytermgui.window_manager import Compositor as PTGCompositor

from typing import Any, Dict, Tuple, Optional, Callable


class CompositorCS(PTGCompositor):
    def init_cs(self, setup_coro_worker: AnyWorker, *args, **kwargs):
        self.setup_coro_worker: AnyWorker = setup_coro_worker
        self.setup_coro_worker_args: Tuple = args
        self.setup_coro_worker_kwargs: Dict = kwargs
        self.cs: CoroScheduler = None
        self.setup_coro_worker_value_holder: ValueExistence = None

    def ensure_cs(self):
        if self.cs is None:
            self.cs, self.setup_coro_worker_value_holder = prepare_loop(self.setup_coro_worker, *self.setup_coro_worker_args, **self.setup_coro_worker_kwargs)

    def iter_cs(self):
        in_work = self.cs.iteration()

    def draw(self, force: bool = False) -> None:
        self.ensure_cs()
        self.iter_cs()
        super().draw(force)
    
    def put_coro(self, coro_worker: AnyWorker, *args, **kwargs):
        put_coro_to((self.cs, None, False), coro_worker, *args, **kwargs)

    def stop(self) -> None:
        async def coro(i: Interface, self):
            def shutdown_handler():
                self._is_running = False
            
            i._loop.on_destroyed_handlers.add(shutdown_handler)
            await i(ShutdownLoop)
        
        self.put_coro(coro, self)


class WindowManagerCS(PTGWindowManager):
    @staticmethod
    def replace(window_manager: PTGWindowManager, model, view_setup: Callable, controller_coro_setup_worker: Optional[AnyWorker] = None, *args, **kwargs) -> 'WindowManagerCS':
        reinterpret_cast(WindowManagerCS, window_manager)
        view_setup(window_manager, model)
        window_manager.init_cs(controller_coro_setup_worker, model, *args, **kwargs)
        return window_manager

    def init_cs(self, setup_coro_worker: AnyWorker, *args, **kwargs):
        reinterpret_cast(CompositorCS, self.compositor)
        self.cs: CoroScheduler = None
        self.compositor.init_cs(setup_coro_worker, *args, **kwargs)
    
    def put_coro(self, coro_worker: AnyWorker, *args, **kwargs):
        self.compositor.put_coro(coro_worker, *args, **kwargs)


class TerminalApplication:
    def __init__(self):
        self.model = self.model_setup()
        self.manager: WindowManagerCS = None
    
    def run(self):
        with PTGWindowManager() as manager:
            self.manager = manager
            WindowManagerCS.replace(manager, self.model, self.ui_setup, self.controller_loop_setup)
    
    def __call__(self):
        self.run()
    
    def model_setup(self):
        raise NotImplementedError()
    
    def ui_setup(self, manager: WindowManagerCS, model):
        raise NotImplementedError()
    
    def controller_loop_setup(self, i: Interface, model):
        raise NotImplementedError()


TermApp = TerminalApplication
