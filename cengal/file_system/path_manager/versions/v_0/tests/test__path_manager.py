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
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.file_system.path_manager import *

from unittest import TestCase, skip, main


class TestPathManager(TestCase):
    @skip('Not implemented yet')
    def test_relative_to_src(self):
        self.fail()

    @skip('Not implemented yet')
    def test_path_relative_to_src(self):
        self.fail()

    @skip('Not implemented yet')
    def test_relative_to_cwd(self):
        self.fail()

    @skip('Not implemented yet')
    def test_path_relative_to_cwd(self):
        self.fail()

    @skip('Not implemented yet')
    def test_get_relative_path_part(self):
        self.fail()

    @skip('Not implemented yet')
    def test_canonical_path(self):
        self.fail()
    
    # @skip('Not implemented yet')
    def normalize_path_preserve_leading_dot(self):
        # self.fail()
        print(normalize_path_preserve_leading_dot('./../'))
        print(normalize_path_preserve_leading_dot('../../asd/./../'))
        print(normalize_path_preserve_leading_dot('./../asdf/../'))
        print(normalize_path_preserve_leading_dot('../../asdf/../'))


if '__main__' == __name__:
    main()
