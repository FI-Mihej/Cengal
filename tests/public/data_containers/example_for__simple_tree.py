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

from cengal.data_containers.simple_tree import Tree, travers_tree_with_path
from cengal.performance_test_lib import test_performance

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


def main():
    tr = Tree()
    tr.put((1, 2, 3))
    tr.put((2, 4, 5))
    tr.put((2, 6))
    tr.put((1, 7))
    print('get_immediate_children([1, 2]): {}'.format(tr.get_immediate_children((1, 2))))
    print('get_immediate_children(tuple()): {}'.format(tr.get_immediate_children(tuple())))
    print('get_immediate_children((2,)): {}'.format(tr.get_immediate_children((2,))))
    print('get_all_children((2,)): {}'.format(tr.get_all_children((2,))))

    with test_performance('Simple Tree - get_immediate_children([1, 2])', 1.0) as tracer:
        while tracer.iter():
            tr.get_immediate_children((1, 2))

    with test_performance('Simple Tree - get_immediate_children(tuple())', 1.0) as tracer:
        while tracer.iter():
            tr.get_immediate_children(tuple())

    with test_performance('Simple Tree - get_immediate_children((2,))', 1.0) as tracer:
        while tracer.iter():
            tr.get_immediate_children((2,))

    with test_performance('Simple Tree - get_immediate_children([1, 2])', 1.0) as tracer:
        while tracer.iter():
            tr.get_all_children((2,))


if __name__ == '__main__':
    main()
