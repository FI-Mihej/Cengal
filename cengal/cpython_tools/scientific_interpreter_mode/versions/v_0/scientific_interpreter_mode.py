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
    'adjusted_scientific_param', 
    'adjusted_scientific_param_name', 
    'prepare_scientific__set_env_var__and__cmd_line_param', 
    'ensure_popen_params__scientific', 
    'run_self__scientific', 
    'popen_self__scientific', 
    'is_adjusted_scientific', 
    'scientific_execution_allowed', 
    'ensure_adjusted_scientific_implicit', 
    'ensure_adjusted_scientific_explicit', 
    'ensure_adjusted_scientific', 
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
from cengal.cpython_tools.pythonhashseed import *
from cengal.cpython_tools.pythonintmaxstrdigits import *
from cengal.cpython_tools.pythonoptimize import *
from cengal.system import PYTHON_IMPLEMENTATION, PVI

import os
import sys
import subprocess
from random import randint

from typing import Optional, Tuple


adjusted_scientific_param = '--adjusted_scientific'
adjusted_scientific_param_name = 'adjusted_scientific'


def prepare_scientific__set_env_var__and__cmd_line_param(
        pythonhashseed: Optional[int] = None, 
        pythonintmaxstrdigits: int = 0, 
        pythonoptimize: int = 2, 
        add_command_line_parameter: bool = False, 
        ):
    pythonhashseed: int = randint(pythonhashseed_min_value, pythonhashseed_max_value) if pythonhashseed is None else pythonhashseed
    if add_command_line_parameter:
        end_with_cmd_line_args = [
            adjusted_scientific_param, 
            adjusted_pythonhashseed_param, 
            adjusted_pythonintmaxstrdigits_param, 
            adjusted_pythonoptimize_param, 
        ]
    else:
        end_with_cmd_line_args = None
    
    set_env_var = {
        pythonhashseed_env_var_name: str(pythonhashseed),
        pythonintmaxstrdigits_env_var_name: str(pythonintmaxstrdigits),
        pythonoptimize_env_var_name: str(pythonoptimize)
    }
    return set_env_var, end_with_cmd_line_args


def simulate_ensure_popen_params____scientific(
        *popen_args, 
        pythonhashseed: Optional[int] = None, 
        pythonintmaxstrdigits: int = 0, 
        pythonoptimize: int = 2, 
        add_command_line_parameter: bool = False, 
        **kwargs
        ) -> bool:
    pythonhashseed_result: bool = False
    if pythonhashseed_execution_allowed():
        _, _, pythonhashseed_result = ensure_popen_params__pythonhashseed(
            *popen_args, 
            pythonhashseed=pythonhashseed, 
            add_command_line_parameter=add_command_line_parameter, 
            **kwargs
            )

    pythonintmaxstrdigits_result: bool = False
    if pythonintmaxstrdigits_execution_allowed():
        _, _, pythonintmaxstrdigits_result = ensure_popen_params__pythonintmaxstrdigits(
            *popen_args, 
            pythonintmaxstrdigits=pythonintmaxstrdigits, 
            add_command_line_parameter=add_command_line_parameter, 
            **kwargs
            )

    pythonoptimize_result: bool = False
    if pythonoptimize_execution_allowed():
        _, _, pythonoptimize_result = ensure_popen_params__pythonoptimize(
            *popen_args, 
            pythonoptimize=pythonoptimize, 
            add_command_line_parameter=add_command_line_parameter, 
            **kwargs
            )
    
    return pythonhashseed_result or pythonintmaxstrdigits_result or pythonoptimize_result


def ensure_popen_params__scientific(
        *popen_args, 
        pythonhashseed: Optional[int] = None, 
        pythonintmaxstrdigits: int = 0, 
        pythonoptimize: int = 2, 
        add_command_line_parameter: bool = False, 
        **kwargs
        ) -> Tuple:
    set_env_var, end_with_cmd_line_args = prepare_scientific__set_env_var__and__cmd_line_param(
        pythonhashseed, 
        pythonintmaxstrdigits, 
        pythonoptimize, 
        add_command_line_parameter
        )
    args, kwargs, changed = ensure_popen_params(
        *popen_args, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        **kwargs
        )
    return args, kwargs, changed


def run_self__scientific(
        *run_args, 
        pythonhashseed: Optional[int] = None, 
        pythonintmaxstrdigits: int = 0, 
        pythonoptimize: int = 2, 
        add_command_line_parameter: bool = False, 
        **kwargs
        ) -> Tuple[subprocess.CompletedProcess, bool]:
    set_env_var, end_with_cmd_line_args = prepare_scientific__set_env_var__and__cmd_line_param(
        pythonhashseed, 
        pythonintmaxstrdigits, 
        pythonoptimize, 
        add_command_line_parameter
        )
    return run_self(
        *run_args, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        **kwargs
        )


def popen_self__scientific(
        *popen_args, 
        pythonhashseed: Optional[int] = None, 
        pythonintmaxstrdigits: int = 0, 
        pythonoptimize: int = 2, 
        add_command_line_parameter: bool = False, 
        **kwargs
        ) -> Tuple[subprocess.Popen, bool]:
    set_env_var, end_with_cmd_line_args = prepare_scientific__set_env_var__and__cmd_line_param(
        pythonhashseed, 
        pythonintmaxstrdigits, 
        pythonoptimize, 
        add_command_line_parameter
        )
    return popen_self(
        *popen_args, 
        set_env_var=set_env_var, 
        end_with_cmd_line_args=end_with_cmd_line_args, 
        **kwargs
        )


def is_adjusted_scientific() -> bool:
    return is_adjusted_pythonhashseed() and \
        is_adjusted_pythonintmaxstrdigits() and \
        is_adjusted_pythonoptimize()


def scientific_execution_allowed() -> bool:
    result = pythonhashseed_execution_allowed() or \
        pythonintmaxstrdigits_execution_allowed() or \
        pythonoptimize_execution_allowed()
    return result


def ensure_adjusted_scientific_implicit(
        *run_args, 
        pythonhashseed: Optional[int] = None, 
        pythonintmaxstrdigits: int = 0, 
        pythonoptimize: int = 2, 
        add_command_line_parameter: bool = False, 
        **kwargs
        ) -> None:
    allowed: bool = simulate_ensure_popen_params____scientific(
        *run_args, 
        pythonhashseed=pythonhashseed, 
        pythonintmaxstrdigits=pythonintmaxstrdigits, 
        pythonoptimize=pythonoptimize, 
        add_command_line_parameter=add_command_line_parameter,
        **kwargs
        )
    if allowed:
        set_env_var, end_with_cmd_line_args = prepare_scientific__set_env_var__and__cmd_line_param(
            pythonhashseed, 
            pythonintmaxstrdigits, 
            pythonoptimize, 
            add_command_line_parameter,
            )
        return ensure_environment_implicit(
            *run_args, 
            execution_allowed=scientific_execution_allowed, 
            set_env_var=set_env_var, 
            end_with_cmd_line_args=end_with_cmd_line_args, 
            **kwargs
            )


def ensure_adjusted_scientific_explicit(
        *popen_args, 
        pythonhashseed: Optional[int] = None, 
        pythonintmaxstrdigits: int = 0, 
        pythonoptimize: int = 2, 
        add_command_line_parameter: bool = False, 
        timeout: Optional[float] = 0.1,
        **kwargs
        ) -> None:
    allowed: bool = simulate_ensure_popen_params____scientific(
        *popen_args, 
        pythonhashseed=pythonhashseed, 
        pythonintmaxstrdigits=pythonintmaxstrdigits, 
        pythonoptimize=pythonoptimize, 
        add_command_line_parameter=add_command_line_parameter,
        **kwargs
        )
    if allowed:
        set_env_var, end_with_cmd_line_args = prepare_scientific__set_env_var__and__cmd_line_param(
            pythonhashseed, 
            pythonintmaxstrdigits, 
            pythonoptimize, 
            add_command_line_parameter,
            )
        return ensure_environment_explicit(
            *popen_args, 
            execution_allowed=scientific_execution_allowed, 
            set_env_var=set_env_var, 
            end_with_cmd_line_args=end_with_cmd_line_args, 
            timeout=timeout, 
            **kwargs
            )


ensure_adjusted_scientific = ensure_adjusted_scientific_implicit
