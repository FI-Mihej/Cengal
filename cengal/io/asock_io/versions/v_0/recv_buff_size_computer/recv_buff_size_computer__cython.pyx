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
__version__ = "3.2.5"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import cython




__author__ = 'ButenkoMS <gtalk@butenkoms.space>'


if cython.compiled:
    # print('"{}" - compiled.'.format(__name__))
    pass
else:
    print('"{}" - interpreted script.'.format(__name__))


cdef class RecvBuffSizeComputer:
    cdef unsigned int _min_recv_buff_size
    cdef unsigned int _max_recv_buff_size
    cdef unsigned int recv_buff_size
    cdef unsigned int _last_recv_amount
    cdef unsigned int _previous_recv_amount

    def __init__(self):
        self._min_recv_buff_size = 1024
        self._max_recv_buff_size = 1024 * 1024 * 10
        self.recv_buff_size = self._min_recv_buff_size
        self._last_recv_amount = 0
        self._previous_recv_amount = 0

    def calc_new_recv_buff_size(self, unsigned int last_recv_amount):
        cdef unsigned int biggest_recv_amount = 0
        cdef unsigned int new_amount = 0

        # moving resv amounts on list
        self._previous_recv_amount = self._last_recv_amount
        self._last_recv_amount = last_recv_amount

        new_amount = self.recv_buff_size
        if (self._last_recv_amount >= self.recv_buff_size) \
                and (self._previous_recv_amount >= self.recv_buff_size):
            new_amount = self.recv_buff_size << 2
        elif (self._last_recv_amount >= self.recv_buff_size) \
                and (self._previous_recv_amount < self.recv_buff_size):
            new_amount = self.recv_buff_size << 1
        elif (self._last_recv_amount < self.recv_buff_size) \
                and (self._previous_recv_amount >= self.recv_buff_size):
            new_amount = self.recv_buff_size
        elif (self._last_recv_amount < self.recv_buff_size) \
                and (self._previous_recv_amount < self.recv_buff_size):
            # new_amount = max(self._last_recv_amounts_list) * 1.5
            if self._last_recv_amount > self._previous_recv_amount:
                biggest_recv_amount = self._last_recv_amount
            else:
                biggest_recv_amount = self._previous_recv_amount
            new_amount = biggest_recv_amount + (biggest_recv_amount >> 1)

        if new_amount < self._min_recv_buff_size:
            self.recv_buff_size = self._min_recv_buff_size
        elif new_amount > self._max_recv_buff_size:
            self.recv_buff_size = self._max_recv_buff_size
        else:
            self.recv_buff_size = new_amount

        return self.recv_buff_size

    # def calc_new_recv_buff_size(self, unsigned int last_recv_amount):
    #     self.recv_buff_size = 1048576
    #
    #     return self.recv_buff_size
