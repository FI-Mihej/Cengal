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


__all__ = [
    'pythonoptimize_env_var_name',
    'pythonoptimize_min_value', 
    'pythonoptimize_max_value', 
    'adjusted_pythonoptimize_param', 
    'adjusted_pythonoptimize_param_name', 
    'prepare_pythonoptimize__set_env_var__and__cmd_line_param', 
    'ensure_popen_params__pythonoptimize', 
    'run_self__pythonoptimize', 
    'popen_self__pythonoptimize', 
    'is_adjusted_pythonoptimize', 
    'pythonoptimize_execution_allowed', 
    'ensure_adjusted_pythonoptimize_implicit', 
    'ensure_adjusted_pythonoptimize_explicit', 
    'ensure_adjusted_pythonoptimize', 
]


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.os.process.ensure_environment import *
from cengal.system import PYTHON_IMPLEMENTATION, PVI

import os
import sys
import subprocess
from random import randint

from typing import Optional, Tuple


pythonoptimize_env_var_name = 'PYTHONOPTIMIZE'
pythonoptimize_min_value = 1
pythonoptimize_max_value = 2
adjusted_pythonoptimize_param = '--adjusted_pythonoptimize'
adjusted_pythonoptimize_param_name = 'adjusted_pythonoptimize'


def prepare_pythonoptimize__set_env_var__and__cmd_line_param(
        pythonoptimize: int = 2, 
        add_command_line_parameter: bool = False, 
        ):
    if add_command_line_parameter:
        end_with_cmd_line_args = [adjusted_pythonoptimize_param]
    else:
        end_with_cmd_line_args = None
    
    set_env_var = {
        pythonoptimize_env_var_name: str(pythonoptimize),
    }
    return set_env_var, end_with_cmd_line_args


def ensure_popen_params__pythonoptimize(
        *popen_args, 
        pythonoptimize: int = 2, 
        add_command_line_parameter: bool = False, 
        **kwargs
        ) -> Tuple:
    set_env_var, end_with_cmd_line_args = prepare_pythonoptimize__set_env_var__and__cmd_line_param(pythonoptimize, add_command_line_parameter)
    args, kwargs, changed = ensure_popen_params(
        *popen_args, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        **kwargs
        )
    return args, kwargs, changed


def run_self__pythonoptimize(
        *run_args, 
        pythonoptimize: int = 2, 
        add_command_line_parameter: bool = False, 
        **kwargs
        ) -> Tuple[subprocess.CompletedProcess, bool]:
    set_env_var, end_with_cmd_line_args = prepare_pythonoptimize__set_env_var__and__cmd_line_param(pythonoptimize, add_command_line_parameter)
    return run_self(
        *run_args, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        **kwargs
        )


def popen_self__pythonoptimize(
        *popen_args, 
        pythonoptimize: int = 2, 
        add_command_line_parameter: bool = False, 
        **kwargs
        ) -> Tuple[subprocess.Popen, bool]:
    set_env_var, end_with_cmd_line_args = prepare_pythonoptimize__set_env_var__and__cmd_line_param(pythonoptimize, add_command_line_parameter)
    return popen_self(
        *popen_args, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        **kwargs
        )


def is_adjusted_pythonoptimize() -> bool:
    pythonoptimize_env_var_present: bool = False
    try:
        pythonoptimize_int_value: int = int(os.environ[pythonoptimize_env_var_name])
        if pythonoptimize_min_value <= pythonoptimize_int_value <= pythonoptimize_max_value:
            pythonoptimize_env_var_present = True
    except (KeyError, ValueError):
        try:
            pythonoptimize_str_value: str = os.environ[pythonoptimize_env_var_name]
            if pythonoptimize_str_value:
                pythonoptimize_env_var_present = True
        except (KeyError, ValueError):
            pass
    
    return (adjusted_pythonoptimize_param in sys.argv) or \
        pythonoptimize_env_var_present


def pythonoptimize_execution_allowed() -> bool:
    pythonoptimize_env_var_present: bool = False
    try:
        pythonoptimize_int_value: int = int(os.environ[pythonoptimize_env_var_name])
        if pythonoptimize_min_value <= pythonoptimize_int_value <= pythonoptimize_max_value:
            pythonoptimize_env_var_present = True
    except (KeyError, ValueError):
        pass
    
    # return (adjusted_pythonoptimize_param not in sys.argv) or \
    #     (not pythonoptimize_env_var_present)
    return True


def ensure_adjusted_pythonoptimize_implicit(
        *run_args, 
        pythonoptimize: int = 2, 
        add_command_line_parameter: bool = False, 
        **kwargs
        ) -> None:
    set_env_var, end_with_cmd_line_args = prepare_pythonoptimize__set_env_var__and__cmd_line_param(pythonoptimize, add_command_line_parameter)
    return ensure_environment_implicit(
        *run_args, 
        execution_allowed=pythonoptimize_execution_allowed, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        **kwargs
        )


def ensure_adjusted_pythonoptimize_explicit(
        *popen_args, 
        pythonoptimize: int = 2, 
        add_command_line_parameter: bool = False, 
        timeout: Optional[float] = 0.1,
        **kwargs
        ) -> None:
    set_env_var, end_with_cmd_line_args = prepare_pythonoptimize__set_env_var__and__cmd_line_param(pythonoptimize, add_command_line_parameter)
    return ensure_environment_explicit(
        *popen_args, 
        execution_allowed=pythonoptimize_execution_allowed, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        timeout=timeout, 
        **kwargs
        )


ensure_adjusted_pythonoptimize = ensure_adjusted_pythonoptimize_implicit
