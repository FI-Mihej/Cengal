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


from cengal.text_processing.regex import *

import re

from unittest import TestCase, main, skip


class TestRegex(TestCase):
    def test_text_word_character(self):
        target_string = "\r\n _PINEAPPLE_ \nasdf"
        result = re.search(f'{text_word_character}+', target_string)
        self.assertEqual(result.span(), (4, 13))

    def test_dev_word_character(self):
        target_string = "\r\n _PINEAPPLE_ \nasdf"
        result = re.search(f'{dev_word_character}+', target_string)
        self.assertEqual(result.span(), (3, 14))


if '__main__' == __name__:  # pragma: no cover
    main()
