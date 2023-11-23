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

import sys
import traceback
from cengal.user_interface.console.chooser import Chooser

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


class TestsRunner(Chooser):
    def __init__(self, list_of_tests: list):
        self.list_of_tests = list(list_of_tests)
        self.list_of_tests.insert(0, self.run_all_tests)
        self.list_of_test_names = list([x.__name__ for x in self.list_of_tests])
        super(TestsRunner, self).__init__(self.list_of_test_names, 'test')

    def choose(self, last_tool_id_str: str=None):
        tool_is_chosen, tool_number, input_raw_last_tool_id = super(TestsRunner, self).choose(last_tool_id_str)
        tool_number -= 1
        result = (tool_is_chosen, tool_number, input_raw_last_tool_id)
        return result

    def choose_and_run(self, last_tool_id_str: str=None):
        tool_is_chosen, tool_number, input_raw_last_tool_id = self.choose(last_tool_id_str)
        tool_number += 1
        if tool_is_chosen:
            test_function = self.list_of_tests[tool_number]
            self.run_test(test_function)
        tool_number -= 1
        result = (tool_is_chosen, tool_number, input_raw_last_tool_id)
        return result

    def run_test(self, test_functor):
        if test_functor is self.run_all_tests:
            test_functor()
        else:
            print('> TEST FUNCTION "{}()"'.format(test_functor.__name__))
            try:
                test_functor()
            except:
                exception = sys.exc_info()
                formatted_traceback = traceback.format_exception(exception[0], exception[1], exception[2])
                print(exception[:2], file=sys.stderr)
                exception = exception[:2] + (formatted_traceback,)
                print(''.join(formatted_traceback), file=sys.stderr)

    def run_all_tests(self):
        for function in self.list_of_tests[1:]:
            self.run_test(function)

