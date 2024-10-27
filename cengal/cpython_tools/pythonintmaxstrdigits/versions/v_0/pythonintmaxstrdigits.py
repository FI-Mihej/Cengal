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
    'pythonintmaxstrdigits_env_var_name', 
    'pythonintmaxstrdigits_present', 
    'pythonintmaxstrdigits_min_value', 
    'adjusted_pythonintmaxstrdigits_param', 
    'adjusted_pythonintmaxstrdigits_param_name', 
    'prepare_pythonintmaxstrdigits__set_env_var__and__cmd_line_param', 
    'ensure_popen_params__pythonintmaxstrdigits', 
    'run_self__pythonintmaxstrdigits', 
    'popen_self__pythonintmaxstrdigits', 
    'is_adjusted_pythonintmaxstrdigits', 
    'pythonintmaxstrdigits_execution_allowed', 
    'ensure_adjusted_pythonintmaxstrdigits_implicit', 
    'ensure_adjusted_pythonintmaxstrdigits_explicit', 
    'ensure_adjusted_pythonintmaxstrdigits', 
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

import os
import sys
import subprocess

from typing import Tuple, Optional


pythonintmaxstrdigits_env_var_name = 'PYTHONINTMAXSTRDIGITS'
pythonintmaxstrdigits_present: bool = False
try:
    pythonintmaxstrdigits_min_value = sys.int_info.str_digits_check_threshold
    pythonintmaxstrdigits_present = True
except AttributeError:
    pythonintmaxstrdigits_min_value = 640

adjusted_pythonintmaxstrdigits_param = '--adjusted_pythonintmaxstrdigits'
adjusted_pythonintmaxstrdigits_param_name = 'adjusted_pythonintmaxstrdigits'


def prepare_pythonintmaxstrdigits__set_env_var__and__cmd_line_param(
        pythonintmaxstrdigits: int = 0, 
        add_command_line_parameter: bool = False, 
        ):
    if add_command_line_parameter:
        end_with_cmd_line_args = [adjusted_pythonintmaxstrdigits_param]
    else:
        end_with_cmd_line_args = None
    
    set_env_var = {
        pythonintmaxstrdigits_env_var_name: str(pythonintmaxstrdigits),
    }
    return set_env_var, end_with_cmd_line_args


def ensure_popen_params__pythonintmaxstrdigits(
        *popen_args, 
        pythonintmaxstrdigits: int = 0, 
        add_command_line_parameter: bool = False, 
        **kwargs
        ) -> Tuple:
    set_env_var, end_with_cmd_line_args = prepare_pythonintmaxstrdigits__set_env_var__and__cmd_line_param(pythonintmaxstrdigits, add_command_line_parameter)
    args, kwargs, changed = ensure_popen_params(
        *popen_args, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        **kwargs
        )
    return args, kwargs, changed


def run_self__pythonintmaxstrdigits(
        *run_args, 
        pythonintmaxstrdigits: int = 0, 
        add_command_line_parameter: bool = False, 
        **kwargs
        ) -> Tuple[subprocess.CompletedProcess, bool]:
    set_env_var, end_with_cmd_line_args = prepare_pythonintmaxstrdigits__set_env_var__and__cmd_line_param(pythonintmaxstrdigits, add_command_line_parameter)
    return run_self(
        *run_args, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        **kwargs
        )


def popen_self__pythonintmaxstrdigits(
        *popen_args, 
        pythonintmaxstrdigits: int = 0, 
        add_command_line_parameter: bool = False, 
        **kwargs
        ) -> Tuple[subprocess.Popen, bool]:
    set_env_var, end_with_cmd_line_args = prepare_pythonintmaxstrdigits__set_env_var__and__cmd_line_param(pythonintmaxstrdigits, add_command_line_parameter)
    return popen_self(
        *popen_args, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        **kwargs
        )


def is_adjusted_pythonintmaxstrdigits() -> bool:
    pythonintmaxstrdigits_env_var_present: bool = False
    try:
        pythonintmaxstrdigits_int_value: int = int(os.environ[pythonintmaxstrdigits_env_var_name])
        if (pythonintmaxstrdigits_min_value <= pythonintmaxstrdigits_int_value) or (0 == pythonintmaxstrdigits_int_value):
            pythonintmaxstrdigits_env_var_present = True
    except (KeyError, ValueError):
        pass
    
    return (not pythonintmaxstrdigits_present) or \
        (adjusted_pythonintmaxstrdigits_param in sys.argv) or \
        pythonintmaxstrdigits_env_var_present


def pythonintmaxstrdigits_execution_allowed() -> bool:
    pythonintmaxstrdigits_env_var_present: bool = False
    try:
        pythonintmaxstrdigits_int_value: int = int(os.environ[pythonintmaxstrdigits_env_var_name])
        if (pythonintmaxstrdigits_min_value <= pythonintmaxstrdigits_int_value) or (0 == pythonintmaxstrdigits_int_value):
            pythonintmaxstrdigits_env_var_present = True
    except (KeyError, ValueError):
        pass
    
    # return pythonintmaxstrdigits_present or \
    #     (adjusted_pythonintmaxstrdigits_param not in sys.argv) or \
    #     (not pythonintmaxstrdigits_env_var_present)
    return pythonintmaxstrdigits_present


def ensure_adjusted_pythonintmaxstrdigits_implicit(
        *run_args, 
        pythonintmaxstrdigits: int = 0, 
        add_command_line_parameter: bool = False, 
        **kwargs
        ) -> None:
    set_env_var, end_with_cmd_line_args = prepare_pythonintmaxstrdigits__set_env_var__and__cmd_line_param(pythonintmaxstrdigits, add_command_line_parameter)
    return ensure_environment_implicit(
        *run_args, 
        execution_allowed=pythonintmaxstrdigits_execution_allowed, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        **kwargs
        )


def ensure_adjusted_pythonintmaxstrdigits_explicit(
        *popen_args, 
        pythonintmaxstrdigits: int = 0, 
        add_command_line_parameter: bool = False, 
        timeout: Optional[float] = 0.1, 
        **kwargs
        ) -> None:
    set_env_var, end_with_cmd_line_args = prepare_pythonintmaxstrdigits__set_env_var__and__cmd_line_param(pythonintmaxstrdigits, add_command_line_parameter)
    return ensure_environment_explicit(
        *popen_args, 
        execution_allowed=pythonintmaxstrdigits_execution_allowed, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        timeout=timeout, 
        **kwargs
        )


ensure_adjusted_pythonintmaxstrdigits = ensure_adjusted_pythonintmaxstrdigits_implicit
