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


from cengal.performance_test_lib import MeasureTimeTraceLine
from cengal.code_inspection.auto_line_tracer import LineType


global_names = {'_tstaticobject_attributes_dict', '_tstaticobject_attributes_slots', '_tstaticobject_setable_data_descriptor_field_names'}


def main():
    iter_num = 1000000
    name = 'some_name'

    with MeasureTimeTraceLine(iterations=iter_num, line_type=LineType.previous_line) as mt:
        for _ in range(mt.iterations):
            if (name == '_tstaticobject_attributes_dict') or (name == '_tstaticobject_attributes_slots') or (name == '_tstaticobject_setable_data_descriptor_field_names') or name.startswith('__'):
                pass

    with MeasureTimeTraceLine(iterations=iter_num, line_type=LineType.previous_line) as mt:
        for _ in range(mt.iterations):
            if (name in {'_tstaticobject_attributes_dict', '_tstaticobject_attributes_slots', '_tstaticobject_setable_data_descriptor_field_names'}) or name.startswith('__'):
                pass

    local_names = {'_tstaticobject_attributes_dict', '_tstaticobject_attributes_slots', '_tstaticobject_setable_data_descriptor_field_names'}
    with MeasureTimeTraceLine(iterations=iter_num, line_type=LineType.previous_line) as mt:
        for _ in range(mt.iterations):
            if (name in local_names) or name.startswith('__'):
                pass

    with MeasureTimeTraceLine(iterations=iter_num, line_type=LineType.previous_line) as mt:
        for _ in range(mt.iterations):
            if (name in global_names) or name.startswith('__'):
                pass


if '__main__' == __name__:
    main()