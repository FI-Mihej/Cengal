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

import subprocess
import os
import sys
import shlex
from cengal.file_system import change_current_dir

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.2.5"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


CYTHON_MODULES_SETUP_SCRIPTS_LIST = [
    'setup__dynamic_list_of_pieces',
    'setup__recv_buff_size_computer',
    'setup__repeat_for_a_time'
]


def compile_module(setup_full_file_name):
    run_parameters = 'build_ext --inplace'
    # run_parameters = 'build_ext'
    path_to_interpreter = sys.executable
    if os.name == 'nt':
        path_to_interpreter = '"{}"'.format(path_to_interpreter)
        setup_full_file_name = '"{}"'.format(setup_full_file_name)
    run_parameters = '{python} {path} {params}'.format(
        python=path_to_interpreter, path=setup_full_file_name, params=run_parameters)

    call_result = subprocess.call(shlex.split(run_parameters))


def main():
    dir_of_current_file = os.path.dirname(os.path.abspath(__file__))
    parent_dir_path, current_dir_name_only = os.path.split(dir_of_current_file)

    for module_name in CYTHON_MODULES_SETUP_SCRIPTS_LIST:
        setup_full_file_name = os.path.join(dir_of_current_file, module_name + '.py')
        with change_current_dir(parent_dir_path):
            compile_module(setup_full_file_name)


if __name__ == '__main__':
    main()
