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
    'pythonhashseed_env_var_name',
    'pythonhashseed_min_value', 
    'pythonhashseed_max_value', 
    'adjusted_pythonhashseed_param', 
    'adjusted_pythonhashseed_param_name', 
    'prepare_pythonhashseed__set_env_var__and__cmd_line_param', 
    'ensure_popen_params__pythonhashseed', 
    'run_self__pythonhashseed', 
    'popen_self__pythonhashseed', 
    'is_adjusted_pythonhashseed', 
    'pythonhashseed_execution_allowed', 
    'ensure_adjusted_pythonhashseed_implicit', 
    'ensure_adjusted_pythonhashseed_explicit', 
    'ensure_adjusted_pythonhashseed', 
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


pythonhashseed_env_var_name = 'PYTHONHASHSEED'
pythonhashseed_min_value = 0
pythonhashseed_max_value = 2**32 - 1
adjusted_pythonhashseed_param = '--adjusted_pythonhashseed'
adjusted_pythonhashseed_param_name = 'adjusted_pythonhashseed'


def prepare_pythonhashseed__set_env_var__and__cmd_line_param(
        pythonhashseed: Optional[int] = None, 
        add_command_line_parameter: bool = False, 
        ):
    pythonhashseed: int = randint(pythonhashseed_min_value, pythonhashseed_max_value) if pythonhashseed is None else pythonhashseed
    if add_command_line_parameter:
        end_with_cmd_line_args = [adjusted_pythonhashseed_param]
    else:
        end_with_cmd_line_args = None
    
    set_env_var = {
        pythonhashseed_env_var_name: str(pythonhashseed),
    }
    return set_env_var, end_with_cmd_line_args


def ensure_popen_params__pythonhashseed(
        *popen_args, 
        pythonhashseed: Optional[int] = None, 
        add_command_line_parameter: bool = False, 
        **kwargs
        ) -> Tuple:
    set_env_var, end_with_cmd_line_args = prepare_pythonhashseed__set_env_var__and__cmd_line_param(pythonhashseed, add_command_line_parameter)
    args, kwargs, changed = ensure_popen_params(
        *popen_args, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        **kwargs
        )
    return args, kwargs, changed


def run_self__pythonhashseed(
        *run_args, 
        pythonhashseed: Optional[int] = None, 
        add_command_line_parameter: bool = False, 
        **kwargs
        ) -> Tuple[subprocess.CompletedProcess, bool]:
    set_env_var, end_with_cmd_line_args = prepare_pythonhashseed__set_env_var__and__cmd_line_param(pythonhashseed, add_command_line_parameter)
    return run_self(
        *run_args, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        **kwargs
        )


def popen_self__pythonhashseed(
        *popen_args, 
        pythonhashseed: Optional[int] = None, 
        add_command_line_parameter: bool = False, 
        **kwargs
        ) -> Tuple[subprocess.Popen, bool]:
    set_env_var, end_with_cmd_line_args = prepare_pythonhashseed__set_env_var__and__cmd_line_param(pythonhashseed, add_command_line_parameter)
    return popen_self(
        *popen_args, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        **kwargs
        )


def is_adjusted_pythonhashseed() -> bool:
    # https://github.com/reingart/pypy/blob/master/pypy/interpreter/app_main.py
    #   Pypy does not implement hash randomization, because it offers no additional security
    #   in CPython either (http://bugs.python.org/issue14621)
    pythonhashseed_env_var_present: bool = False
    try:
        pythonhashseed_int_value: int = int(os.environ[pythonhashseed_env_var_name])
        if pythonhashseed_min_value <= pythonhashseed_int_value <= pythonhashseed_max_value:
            pythonhashseed_env_var_present = True
    except (KeyError, ValueError):
        pass
    
    return ('CPython' != PYTHON_IMPLEMENTATION) or \
        (('CPython' == PYTHON_IMPLEMENTATION) and ((3, 2, 3) > PVI)) or \
        (adjusted_pythonhashseed_param in sys.argv) or \
        pythonhashseed_env_var_present


def pythonhashseed_execution_allowed() -> bool:
    # https://github.com/reingart/pypy/blob/master/pypy/interpreter/app_main.py
    #   Pypy does not implement hash randomization, because it offers no additional security
    #   in CPython either (http://bugs.python.org/issue14621)
    pythonhashseed_env_var_present: bool = False
    try:
        pythonhashseed_int_value: int = int(os.environ[pythonhashseed_env_var_name])
        if pythonhashseed_min_value <= pythonhashseed_int_value <= pythonhashseed_max_value:
            pythonhashseed_env_var_present = True
    except (KeyError, ValueError):
        pass
    
    return not (('CPython' != PYTHON_IMPLEMENTATION) or \
        (('CPython' == PYTHON_IMPLEMENTATION) and ((3, 2, 3) > PVI)) or \
        (adjusted_pythonhashseed_param in sys.argv) or \
        pythonhashseed_env_var_present)


def ensure_adjusted_pythonhashseed_implicit(
        *run_args, 
        pythonhashseed: Optional[int] = None, 
        add_command_line_parameter: bool = False, 
        **kwargs
        ) -> None:
    set_env_var, end_with_cmd_line_args = prepare_pythonhashseed__set_env_var__and__cmd_line_param(pythonhashseed, add_command_line_parameter)
    return ensure_environment_implicit(
        *run_args, 
        execution_allowed=pythonhashseed_execution_allowed, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        **kwargs
        )


def ensure_adjusted_pythonhashseed_explicit(
        *popen_args, 
        pythonhashseed: Optional[int] = None, 
        add_command_line_parameter: bool = False, 
        timeout: Optional[float] = 0.1,
        **kwargs
        ) -> None:
    set_env_var, end_with_cmd_line_args = prepare_pythonhashseed__set_env_var__and__cmd_line_param(pythonhashseed, add_command_line_parameter)
    return ensure_environment_explicit(
        *popen_args, 
        execution_allowed=pythonhashseed_execution_allowed, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args,
        timeout=timeout,  
        **kwargs
        )


ensure_adjusted_pythonhashseed = ensure_adjusted_pythonhashseed_implicit
