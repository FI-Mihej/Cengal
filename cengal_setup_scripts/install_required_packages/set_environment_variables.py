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


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""


__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.2.6"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import os
import sys




__author__ = 'ButenkoMS <gtalk@butenkoms.space>'


def main():
    if sys.platform == 'linux':
        dir_of_the_current_file = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(dir_of_the_current_file)
        parent_dir = os.path.dirname(parent_dir)
        path_to_lib = os.path.join(parent_dir, 'cengal')
        call_result = os.system('export PYTHONPATH=$PYTHONPATH:{}'.format(path_to_lib))
        if path_to_lib not in sys.path:
            sys.path.append(path_to_lib)


if __name__ == '__main__':
    main()
