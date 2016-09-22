#!/usr/bin/env python

# Copyright © 2016 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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

from testing_lib.tests_list_runner import TestsRunner

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2016 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "1.0.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


cm_per_feet = 30.48
cm_per_inch = 2.54


def feet_to_cm():
    input_data = input('Enter feet, inch like "6, 3": ').split(',')
    input_data = list([int(val) for val in input_data])
    result = input_data[0] * cm_per_feet + input_data[1] * cm_per_inch
    print(result)


def cm_to_feet():
    input_data = float(input('Enter distance in cm like "235": '))
    result = (input_data // cm_per_feet, (input_data % cm_per_feet) / cm_per_inch)
    print(result)


ALL_VARIANTS = [
    feet_to_cm,
    cm_to_feet,

]


def main():
    print('Distance converter')
    exit_loop = False
    while not exit_loop:
        runner = TestsRunner(ALL_VARIANTS)
        tool_is_chosen, tool_number, input_raw_last_tool_id = runner.choose_and_run()
        input_result = input('Enter "exit" for exit or press Enter for retry: ')
        if 'exit' == input_result:
            exit_loop = True
