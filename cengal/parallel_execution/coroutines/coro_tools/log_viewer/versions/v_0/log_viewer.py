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
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_tools.run_in_loop import run_in_loop
from cengal.parallel_execution.coroutines.coro_tools.loop_administration.admin_tk import start_admin
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_on_keyboard_interrupt import ShutdownOnKeyboardInterrupt
from cengal.parallel_execution.coroutines.coro_standard_services.shutdown_loop import ShutdownLoop
from cengal.parallel_execution.coroutines.coro_standard_services.instance import InstanceRequest
from cengal.parallel_execution.coroutines.coro_standard_services.log import LogRequest, Log
from cengal.parallel_execution.coroutines.coro_standard_services.run_coro import RunCoro
from cengal.file_system.app_fs_structure.app_dir_path import AppDirPath, AppDirectoryType
from cengal.code_flow_control.args_manager import AK
from cengal.system import current_cengal_module_import_str
from cengal.introspection.inspect import pdi
import os
import tkinter as tk
from tkinter import filedialog


async def on_close(i: Interface):
    await i(ShutdownLoop)


def request_and_set_log_env_dir(i: Interface, admin_tk_app: tk.Tk):
    app_name_for_fs = i(InstanceRequest().wait('app_name_for_fs'))
    app_data_dir_path_type: AppDirectoryType = i(InstanceRequest().wait('app_data_dir_path_type'))
    app_dir_path: AppDirPath = i(InstanceRequest().wait(AppDirPath))
    app_data_dir_path: str = app_dir_path.cached(app_data_dir_path_type, app_name_for_fs, False)
    initialdir = os.path.dirname(app_data_dir_path)
    log_db_env_path = filedialog.askdirectory(parent=admin_tk_app,
                                                initialdir=initialdir,
                                                title="Please select a folder:")
    if not isinstance(log_db_env_path, str):
        i(LogRequest().sync())
        i.log.warning('Path to Log DB Env was not provided! Using own Log DB Env instead.')
        return
    
    log_db_env_path = log_db_env_path.strip()
    log_db_env_path = os.path.normpath(log_db_env_path)
    if not (os.path.exists(log_db_env_path) and os.path.isdir(log_db_env_path)):
        i(LogRequest().sync())
        i.log.warning('Path does not exist! Using own Log DB Env instead.')
        return

    i(LogRequest().set_db_environment_path(log_db_env_path))


async def main(i: Interface):
    await i(ShutdownOnKeyboardInterrupt)
    await i(InstanceRequest().set('app_name_for_fs', current_cengal_module_import_str()))
    await start_admin(i, on_close, AK(current_children_pack_type = 2))
    admin_tk_app: tk.Tk = await i(InstanceRequest().wait('admin_tk_app'))
    await i(RunCoro, request_and_set_log_env_dir, admin_tk_app)


if '__main__' == __name__:
    run_in_loop(main)
