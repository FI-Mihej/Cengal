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

import copy
from data_containers.fast_fifo import *

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


def get_obj_parameter(par_path):
    root_obj = par_path[0]
    last_obj = root_obj
    last_par_name = None
    last_par = None
    par_subnames_list = list()
    another_obj = root_obj
    for another_par_name in par_path[1:]:
        another_par = another_obj.__dict__[another_par_name]
        another_obj = another_par

        last_par_name = another_par_name
        last_par = another_par
        par_subnames_list.append(last_par_name)
    full_par_name = '.'.join(par_subnames_list)

    result = (full_par_name, last_par)
    return result


def print_obj_parameter(par_path):
    full_par_name, last_par = get_obj_parameter(par_path)
    print('\t{}: {}'.format(full_par_name, last_par))


def print__FIFOWithLengthControl__internals(fif):
    print_obj_parameter([fif, '_l'])
    print_obj_parameter([fif, '_l_length'])
    print_obj_parameter([fif, '_l_deletable_length'])
    print_obj_parameter([fif, '_data_full_size', 'existence'])
    print_obj_parameter([fif, '_data_full_size', 'result'])
    print_obj_parameter([fif, '_deletable_data_full_size'])
    print()


def test__FIFOWithLengthControl():
    fi = FIFOWithLengthControl(None, 10)
    fi.put('asdf')
    fi.put('1242')
    fi.put('qwre')
    fi.put('4567')
    fi.put('zxcv')
    print__FIFOWithLengthControl__internals(fi)

    print(fi.size())

    fif = copy.copy(fi)

    print(fif.get())
    print__FIFOWithLengthControl__internals(fif)

    print(fif.get())
    print__FIFOWithLengthControl__internals(fif)

    print(fif.get())
    print__FIFOWithLengthControl__internals(fif)


def main():
    test__FIFOWithLengthControl()


if __name__ == '__main__':
    main()
