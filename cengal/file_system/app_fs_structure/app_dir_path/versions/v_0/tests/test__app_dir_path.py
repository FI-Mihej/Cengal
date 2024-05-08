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
__version__ = "4.4.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.file_system.app_fs_structure.app_dir_path import AppDirectoryType, AppDirPath
from cengal.system import OS_TYPE, PYTHON_IMPLEMENTATION
from unittest import TestCase, main, skip, skipIf


class TestAppDirPath(TestCase):
    @skipIf(('PyPy' == PYTHON_IMPLEMENTATION) and (OS_TYPE in ('Windows', 'Darwin')), 'PyPy on Windows and Mac OS X is not supported')
    def test_print_all_dirs(self):
        for dir_type in AppDirectoryType:
            adp: AppDirPath = AppDirPath()
            print(f'<<< {dir_type.name} >>>')
            print(adp(dir_type, with_structure=False, ensure_dir=False))
            print(adp(dir_type, with_structure=True, ensure_dir=False))
            print(adp(dir_type, 'test_app', with_structure=False, ensure_dir=False))
            print(adp(dir_type, 'test_app', with_structure=True, ensure_dir=False))
            print()


if '__main__' == __name__:
    main()
