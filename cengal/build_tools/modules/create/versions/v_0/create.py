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
__version__ = "4.2.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from os import rename, remove
from os.path import sep as os_sep, dirname, exists, isfile
from distutils.dir_util import copy_tree
from distutils.file_util import copy_file
from cengal.file_system.win_fs.global_install_uninstall import win_fs
from cengal.file_system.path_manager import path_relative_to_src, RelativePath
from cengal.file_system.file_manager import file_exists
from cengal.text_processing.text_processing import removeprefix
from cengal.file_system.file_patch.simple import patch_text_file
import os
from typing import Set


create_env_variants: Set[str] = {
    'create_env.sh',
    'create_env.cmd',
    'command/_common.sh',
    'command/_common.cmd',
}


def create(src_dir: str, module_submodule_path: str, sep: str = '/'):
    with win_fs():
        src_dir_path = RelativePath(src_dir)
        template_module_dir = src_dir_path('_template_module')
        template_submodule_dir = src_dir_path('_template_module/_template_submodule')
        required_path_input = module_submodule_path
        required_path_input = required_path_input.replace(os_sep, sep)
        required_path_input = required_path_input.strip()
        required_path_input = required_path_input.strip(sep)
        # if sep not in required_path_input:
        #     print('Wrong path: both module and submodule are mandatory')
        #     return
        
        required_path_input_parts = required_path_input.split(sep)
        submodule_name = required_path_input_parts[-1]
        submodule_path = src_dir_path(required_path_input)
        module_path = RelativePath(submodule_path)('..')
        copy_tree(template_submodule_dir, submodule_path, update=True)

        template_submodule_py_path = RelativePath(submodule_path)('versions/v_0/_template_submodule.py')
        template_submodule_py_new_path = RelativePath(submodule_path)(f'versions/v_0/{submodule_name}.py')
        if exists(template_submodule_py_new_path) and isfile(template_submodule_py_new_path):
            remove(template_submodule_py_path)
        else:
            rename(template_submodule_py_path, template_submodule_py_new_path)

        init_py_path = RelativePath(submodule_path)('versions/v_0/__init__.py')
        patch_text_file(init_py_path, [('_template_submodule', submodule_name)])

        for index in range(1, 1 + len(required_path_input_parts)):
            subpath: str = sep.join(required_path_input_parts[:index])
            subpath_init: str = src_dir_path(subpath + sep + '__init__.py')
            if not file_exists(subpath_init):
                copy_file(src_dir_path('_template_module/__init__.py'), subpath_init, verbose=0)

        # create_env_sh_path = RelativePath(submodule_path)('versions/v_0/development/create_env.sh')
        # development_dir_path = dirname(create_env_sh_path)
        development_dir_path = RelativePath(submodule_path)('versions/v_0/development')
        remaining_path = removeprefix(development_dir_path, src_dir)
        sep_num = remaining_path.count(sep)
        cd_2_parent_num = 1 + sep_num  # since we need dir parent to the `src_dir`
        new_relativeness = '/..' * cd_2_parent_num
        new_relativeness_win32 = '\\..' * cd_2_parent_num

        development_dir_path_rel: RelativePath = RelativePath(development_dir_path)
        for create_env_variant in create_env_variants:
            create_env_sh_path = development_dir_path_rel(create_env_variant)
            if not file_exists(create_env_sh_path):
                continue
            
            patch_text_file(create_env_sh_path, [
                ('$WORKDIR/../../../../../..`', f'$WORKDIR{new_relativeness}`'),
                ('$CURRENT_PROJECT_DIR_PATH/../../../../../.."', f'$CURRENT_PROJECT_DIR_PATH{new_relativeness}"'),
                ('%CURRENT_PROJECT_DIR_PATH%\..\..\..\..\..\.."', f'%CURRENT_PROJECT_DIR_PATH%{new_relativeness_win32}"'),
            ])
