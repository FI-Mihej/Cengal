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


from cengal.user_interface.console.encoding_changer import change_console_output_cp
from cengal.code_flow_control import ResultExistence


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


def main():
    with change_console_output_cp(ResultExistence(True, (65001, 'utf-8')),
                                  ResultExistence(True, (65001, 'utf-8'))) as original_encodings:

        print(original_encodings)

        czech = 'Leoš Janáček'
        print(czech)
        pl = 'Zdzisław Beksiński'
        print(pl)
        jp = 'リング 山村 貞子'
        print(jp)
        chinese = '五行'
        print(chinese)
        MIR = 'Машина для Инженерных Расчётов'
        print(MIR)
        pt = 'Minha Língua Portuguesa: çáà'
        print(pt)

    print('DONE.')


if __name__ == '__main__':
    main()
