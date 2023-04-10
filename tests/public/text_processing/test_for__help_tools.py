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

import unittest
from cengal.text_processing.help_tools import *

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.1.10"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


class TestHelpToolsFind(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestHelpToolsFind, self).__init__(*args, **kwargs)

        # # ----
        # self.full_string = 'First Second Third SubWord End'
        #
        # self.sub_strings_full_word = [('First', (0, 5)), ('Second', (6, 12)), ('Third', (13, 18)),
        #                               ('SubWord', (19, 26)), ('End', (27, 30))]
        # self.sub_strings_sub_word = [('Sub', (19, 22)), ('Word', (22, 26)), ('bWo', (21, 24))]
        # self.sub_strings_all = self.sub_strings_full_word + self.sub_strings_sub_word
        # self.sub_strings_all_sub_word_on_start_of_words = self.sub_strings_full_word + [('Sub', (19, 22))]
        # self.sub_strings_sub_word_on_start_of_words = [('Sub', (19, 22))]
        # self.sub_strings_sub_word_in_middle_of_words = [('Word', (22, 26)), ('bWo', (21, 24))]

        # ----
        self.full_string = '\r\nFirst Second Third SubWord End'

        self.sub_strings_full_word = [('First', (2, 7)), ('Second', (8, 14)), ('Third', (15, 20)),
                                      ('SubWord', (21, 28)), ('End', (29, 32))]
        self.sub_strings_sub_word = [('Sub', (21, 24)), ('Word', (24, 28)), ('bWo', (23, 26))]
        self.sub_strings_all = self.sub_strings_full_word + self.sub_strings_sub_word
        self.sub_strings_all_sub_word_on_start_of_words = self.sub_strings_full_word + [('Sub', (21, 24))]
        self.sub_strings_sub_word_on_start_of_words = [('Sub', (21, 24))]
        self.sub_strings_sub_word_in_middle_of_words = [('Word', (24, 28)), ('bWo', (23, 26))]

    def test_find_substring(self):
        print()
        print('=======================')
        print('<<<<TEST_FIND_SUBSTRING>>')
        print()
        print('>> find good sub-strings')
        for sub_string, good_result in self.sub_strings_all:
            print(sub_string)
            self.assertEqual(find_substring(self.full_string.encode(), sub_string.encode()),
                             good_result)

        print()
        print('>> find lower sub-strings')
        for sub_string, good_result in self.sub_strings_all:
            sub_string = sub_string.lower()
            print(sub_string)
            self.assertEqual(find_substring(self.full_string.encode(), sub_string.encode()),
                             (None, None))

    def test_find_substring_full_word(self):
        print()
        print('=======================')
        print('<<<<TEST_FIND_SUBSTRING_FULL_WORD>>')
        print()
        print('>> find good words')
        for sub_string, good_result in self.sub_strings_full_word:
            print(sub_string)
            self.assertEqual(find_substring_full_word(self.full_string.encode(), sub_string.encode()),
                             good_result)

        print()
        print('>> find bad words on start of words')
        for sub_string, good_result in self.sub_strings_sub_word_on_start_of_words:
            print(sub_string)
            self.assertEqual(find_substring_full_word(self.full_string.encode(), sub_string.encode()),
                             (good_result[0], None))

        print()
        print('>> find bad words in middle of words')
        for sub_string, good_result in self.sub_strings_sub_word_in_middle_of_words:
            print(sub_string)
            self.assertEqual(find_substring_full_word(self.full_string.encode(), sub_string.encode()),
                             (None, None))

        print()
        print('>> find lower words')
        for sub_string, good_result in self.sub_strings_all:
            sub_string = sub_string.lower()
            print(sub_string)
            self.assertEqual(find_substring_full_word(self.full_string.encode(), sub_string.encode()),
                             (None, None))

if __name__ == '__main__':
    unittest.main()
