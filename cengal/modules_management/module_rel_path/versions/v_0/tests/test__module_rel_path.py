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


import unittest
from cengal.modules_management.module_rel_path import *


class TestCaseForModuleRelPath(unittest.TestCase):
    def test_module_dir(self):
        import os
        import asyncio
        from asyncio import coroutines
        from cengal.introspection.inspect import get_module_importable_str_and_path

        mdir: str = module_dir(asyncio)
        mrpath: str = module_rel_path(asyncio, coroutines)
        fpath: str = os.path.join(mdir, mrpath)
        module_file_full_path = get_module_importable_str_and_path(coroutines)[1]
        self.assertEqual(fpath, module_file_full_path)

    def test_module_rel_path(self):
        import asyncio
        from asyncio import coroutines
        self.assertEqual(module_rel_path(asyncio, coroutines), 'coroutines.py')

    def test_module_rel_import_str(self):
        import asyncio
        from asyncio import coroutines
        self.assertEqual(module_import_str(asyncio, coroutines), 'asyncio.coroutines')

    def test_current_module_dir(self):
        import os
        from cengal.introspection.inspect import entity_owning_module_info_and_owning_path, frame

        mdir: str = current_module_dir()
        _, _, module_file_full_path, _ = entity_owning_module_info_and_owning_path(frame())
        self.assertEqual(os.path.join(mdir, os.path.basename(module_file_full_path)), module_file_full_path)

    def test_current_module_rel_path(self):
        import cengal
        self.assertEqual(current_module_rel_path(cengal), 'modules_management/module_rel_path/versions/v_0/tests/test__module_rel_path.py')

    def test_current_module_import_str(self):
        import cengal
        self.assertEqual(current_module_import_str(cengal), 'cengal.modules_management.module_rel_path.versions.v_0.tests.test__module_rel_path')


if __name__ == '__main__':
    unittest.main()
