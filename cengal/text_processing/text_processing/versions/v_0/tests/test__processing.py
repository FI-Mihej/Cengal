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


from cengal.text_processing.text_processing import *

from unittest import TestCase, main, skip


class TestTextProcessing(TestCase):
    def test__find_any_spaces(self):
        text = 'Hello,      \t\n World! This is a test text. Test text.'
        result = find_any_spaces(text)
        self.assertEqual(result, slice(6, 15))

        text = 'Hello,      \t\n World! This is a test text. Test text.'
        result = find_any_spaces(text, start=7, stop=14)
        self.assertEqual(result, slice(7, 14))

        text = 'Hello'
        result = find_any_spaces(text)
        self.assertEqual(result, None)

    def test__rfind_any_spaces(self):
        text = ' Hello,      \t\n World!'
        result = rfind_any_spaces(text)
        self.assertEqual(result, slice(7, 16))

        text = ' Hello,      \t\n World!'
        result = rfind_any_spaces(text, start=8, stop=15)
        self.assertEqual(result, slice(8, 15))

        text = 'Hello'
        result = rfind_any_spaces(text)
        self.assertEqual(result, None)

    def test__startswith_any_spaces(self):
        text = '      \t\n World!'
        result = startswith_any_spaces(text)
        self.assertEqual(result, slice(0, 9))

        text = '      \t\n World!'
        result = startswith_any_spaces(text, start=1, stop=8)
        self.assertEqual(result, slice(1, 8))

        text = 'Hello'
        result = startswith_any_spaces(text)
        self.assertEqual(result, None)

    def test__endswith_any_spaces(self):
        text = 'Hello,      \t\n '
        result = endswith_any_spaces(text)
        self.assertEqual(result, slice(6, 15))

        text = 'Hello,      \t\n '
        result = endswith_any_spaces(text, start=7, stop=14)
        self.assertEqual(result, slice(7, 14))

        text = 'Hello'
        result = endswith_any_spaces(text)
        self.assertEqual(result, None)

    def test__find_spaces_or_tabs(self):
        text = 'Hello,      \t\n World! This is a test text. Test text.'
        result = find_spaces_or_tabs(text)
        self.assertEqual(result, slice(6, 13))

    def test__find_spaces(self):
        text = 'Hello,      \t\n World! This is a test text. Test text.'
        result = find_spaces(text)
        self.assertEqual(result, slice(6, 12))

    def test__find_tabs(self):
        text = 'Hello,      \t\n World! This is a test text. Test text.'
        result = find_tabs(text)
        self.assertEqual(result, slice(12, 13))

    def test__find_universal_line_delimiter(self):
        text = 'Hello,      \t\n World! This is a test text. Test text.'
        result = find_universal_line_delimiter(text)
        self.assertEqual(result, slice(13, 14))

        text = 'Hello,      \t\r\n\n World! This is a test text. Test text.'
        result = find_universal_line_delimiter(text)
        self.assertEqual(result, slice(13, 15))

    def test__find_line_delimiter(self):
        text = 'Hello,      \t\n World! This is a test text. Test text.'
        result = find_line_delimiter(text)
        self.assertEqual(result, slice(13, 14))

        text = 'Hello,      \t\r\n\n World! This is a test text. Test text.'
        result = find_line_delimiter(text)
        self.assertEqual(result, slice(13, 15))

    def test__find_word(self):
        text = 'Hello, World! This is a test text. Test text.'
        word = 'test'
        result = find_word(text, word)
        self.assertEqual(result, slice(24, 28))
    
        text = 'Hello, World! This is a _test test text. Test text.'
        word = 'test'
        result = find_word(text, word)
        self.assertEqual(result, slice(25, 29))
    
        text = 'Hello, World! This is a 0test test text. Test text.'
        word = 'test'
        result = find_word(text, word)
        self.assertEqual(result, slice(30, 34))
    
        text = 'test text. Test text.'
        word = 'test'
        result = find_word(text, word)
        self.assertEqual(result, slice(0, 4))
    
        text = 'Hello test'
        word = 'test'
        result = find_word(text, word)
        self.assertEqual(result, slice(6, 10))
    
        text = 'Hello'
        word = ''
        result = find_word(text, word)
        self.assertEqual(result, slice(0, 5))
    
        text = 'Hello'
        word = None
        result = find_word(text, word)
        self.assertEqual(result, slice(0, 5))
    
        text = 'Hello'
        result = find_word(text)
        self.assertEqual(result, slice(0, 5))
    
        text = '  Hello  '
        word = ''
        result = find_word(text, word)
        self.assertEqual(result, slice(2, 7))
    
        text = '  _Hello  '
        word = ''
        result = find_word(text, word)
        self.assertEqual(result, slice(3, 8))

        text = ' test test '
        word = 'test'
        result = find_word(text, word)
        self.assertEqual(result, slice(1, 5))
    
        text = ' test test '
        word = 'test'
        result = find_word(text, word, 1, 5)
        self.assertEqual(result, slice(1, 5))
    
        text = ' test test '
        word = 'test'
        result = find_word(text, word, 1, 5, False)
        self.assertEqual(result, slice(1, 5))
    
        text = ' testr test '
        word = 'test'
        result = find_word(text, word, 1, 5)
        self.assertEqual(result, None)
    
        text = ' testr test '
        word = 'test'
        result = find_word(text, word, 1, 5, False)
        self.assertEqual(result, slice(1, 5))
    
        text = ' rtest test '
        word = 'test'
        result = find_word(text, word, 2, 6)
        self.assertEqual(result, None)
    
        text = ' rtest test '
        word = 'test'
        result = find_word(text, word, 2, 6, False)
        self.assertEqual(result, slice(2, 6))

    def test__rfind_word(self):
        text = ' test test '
        word = 'test'
        result = rfind_word(text, word)
        self.assertEqual(result, slice(6, 10))
    
        text = ' test test '
        word = 'test'
        result = rfind_word(text, word, 6, 10)
        self.assertEqual(result, slice(6, 10))
    
        text = ' test test '
        word = 'test'
        result = rfind_word(text, word, 6, 10, False)
        self.assertEqual(result, slice(6, 10))
    
        text = ' test testr'
        word = 'test'
        result = rfind_word(text, word, 6, 10)
        self.assertEqual(result, None)
    
        text = ' test testr'
        word = 'test'
        result = rfind_word(text, word, 6, 10, False)
        self.assertEqual(result, slice(6, 10))
    
        text = ' test rtest '
        word = 'test'
        result = rfind_word(text, word, 7, 11)
        self.assertEqual(result, None)
    
        text = ' test rtest '
        word = 'test'
        result = rfind_word(text, word, 7, 11, False)
        self.assertEqual(result, slice(7, 11))
    
    def test__replace_word(self):
        text = 'Hello, World! This is a test text. Test text.'
        word = 'test'
        new_word = 'exam'
        result = replace_word(text, word, new_word)
        self.assertEqual(result, 'Hello, World! This is a exam text. Test text.')
    
        text = 'Hello, World! This is a _test test text. Test text.'
        word = 'test'
        new_word = 'exam'
        result = replace_word(text, word, new_word)
        self.assertEqual(result, 'Hello, World! This is a _exam exam text. Test text.')
    
        text = 'test text. Test text.'
        word = 'test'
        new_word = 'exam'
        result = replace_word(text, word, new_word)
        self.assertEqual(result, 'exam text. Test text.')
    
        text = 'Hello test'
        word = 'test'
        new_word = 'exam'
        result = replace_word(text, word, new_word)
        self.assertEqual(result, 'Hello exam')
    
    def test__find_dev_word(self):
        text = 'Hello, World! This is a test text. Test text.'
        word = 'test'
        result = find_dev_word(text, word)
        self.assertEqual(result, slice(24, 28))
    
        text = 'Hello, World! This is a _test test text. Test text.'
        word = 'test'
        result = find_dev_word(text, word)
        self.assertEqual(result, slice(30, 34))
    
        text = 'Hello, World! This is a 0test test text. Test text.'
        word = 'test'
        result = find_dev_word(text, word)
        self.assertEqual(result, slice(25, 29))
    
        text = 'Hello, World! This is a test0 test text. Test text.'
        word = 'test'
        result = find_dev_word(text, word)
        self.assertEqual(result, slice(30, 34))
    
        text = 'test text. Test text.'
        word = 'test'
        result = find_dev_word(text, word)
        self.assertEqual(result, slice(0, 4))
    
        text = 'Hello test'
        word = 'test'
        result = find_dev_word(text, word)
        self.assertEqual(result, slice(6, 10))
        
        text = 'Hello'
        word = ''
        result = find_dev_word(text, word)
        self.assertEqual(result, slice(0, 5))
    
        text = 'Hello'
        word = None
        result = find_dev_word(text, word)
        self.assertEqual(result, slice(0, 5))
    
        text = 'Hello'
        result = find_dev_word(text)
        self.assertEqual(result, slice(0, 5))
    
        text = '  Hello  '
        word = ''
        result = find_dev_word(text, word)
        self.assertEqual(result, slice(2, 7))
    
        text = '  _Hello  '
        word = ''
        result = find_dev_word(text, word)
        self.assertEqual(result, slice(2, 8))

    def test__replace_dev_word(self):
        text = 'Hello, World! This is a test text. Test text.'
        word = 'test'
        new_word = 'exam'
        result = replace_dev_word(text, word, new_word)
        self.assertEqual(result, 'Hello, World! This is a exam text. Test text.')
    
        text = 'Hello, World! This is a _test test text. Test text.'
        word = 'test'
        new_word = 'exam'
        result = replace_dev_word(text, word, new_word)
        self.assertEqual(result, 'Hello, World! This is a _test exam text. Test text.')
    
        text = 'test text. Test text.'
        word = 'test'
        new_word = 'exam'
        result = replace_dev_word(text, word, new_word)
        self.assertEqual(result, 'exam text. Test text.')
    
        text = 'Hello test'
        word = 'test'
        new_word = 'exam'
        result = replace_dev_word(text, word, new_word)
        self.assertEqual(result, 'Hello exam')


if __name__ == '__main__':
    main()
