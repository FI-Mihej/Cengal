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

from collections import deque

from cengal.code_flow_control.smart_values import ValueCache, ValueExistence
from cengal.code_inspection.line_profiling import set_profiler

"""
Быстрый модуль FIFO. Скорость достигается за счет уменьшенного количества аллокаций и деаллокаций памяти и
соответственно, за счет бОльшего размера используемой памяти в пИке. Расход памяти неравномерный: сначала происходит
постоянное увеличение размера используемой памяти, а при превышении лимита - вся ненужная память деалоцируется
одномоментно, что приводит лишь к одному пересозданию контейнерного списка блоков.
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


# set_profiler(True)
set_profiler(False)


class FIFOIsEmpty(Exception):
    pass


class FIFO:
    def __init__(self, on_hold_limit=None):
        self._init_param__on_hold_limit = on_hold_limit

        self._l = list()
        self._offset = 0
        self._offset_limit = on_hold_limit or 1000
        self._useful_size = 0
        self._real_size = 0

    def put(self, data):
        self._l.append(data)
        self._useful_size += 1
        self._real_size += 1

    def extend(self, iterable_data):
        self._l.extend(iterable_data)
        new_full_length = len(self._l)
        diff = new_full_length - self._real_size
        self._useful_size += diff
        self._real_size += diff

    def get(self):
        # l_offset_limit = 1000: 574305.7210067833 iterations per second
        # PyPy: l_offset_limit = 1000: 6666620.042915044 iterations per second
        if self._useful_size <= 0:
            raise FIFOIsEmpty()

        result = self._l[self._offset]
        self._useful_size -= 1
        self._offset += 1
        if self._offset >= self._offset_limit:
            self._real_size -= self._offset
            self._l = self._l[self._offset:]
            self._offset = 0
        return result

    def _free(self, num):
        self._useful_size -= num
        self._offset += num
        if self._offset >= self._offset_limit:
            self._real_size -= self._offset
            self._l = self._l[self._offset:]
            self._offset = 0

    def size(self):
        return self._useful_size

    def full_size(self):
        return self._real_size

    def remove(self):
        pass

    def __copy__(self):
        return FIFO(self._init_param__on_hold_limit)


class FIFOWithLengthControl(FIFO):
    def __init__(self, on_hold_limit=None, on_hold_data_size_limit=None,
                 external_data_full_size: ValueExistence = None,
                 external_deletable_data_full_size: ValueExistence = None):
        super(FIFOWithLengthControl, self).__init__(on_hold_limit)
        self._removed = False

        self._init_param__on_hold_data_size_limit = on_hold_data_size_limit
        self._init_param__external_data_full_size = external_data_full_size
        self._init_param__external_deletable_data_full_size = external_deletable_data_full_size

        self._l_length = list()
        # self._l_deletable_length = list()
        self._data_full_size = ValueCache()
        self._data_full_size.set(0)
        self._deletable_data_full_size = 0
        self._on_hold_data_size_limit = on_hold_data_size_limit or 1024**2 * 10
        self._external_data_full_size = external_data_full_size or ValueExistence(False, 0)
        self._external_deletable_data_full_size = external_deletable_data_full_size or ValueExistence(False, 0)

    def put(self, data):
        if not self._data_full_size:
            self._calculate_data_full_size()

        super(FIFOWithLengthControl, self).put(data)

        data_size = len(data)
        self._l_length.append(data_size)
        self._data_full_size.value += data_size
        self._external_data_full_size.value += data_size

    def extend(self, iterable_data):
        if not self._data_full_size:
            self._calculate_data_full_size()

        index = self._real_size

        self._l.extend(iterable_data)
        new_full_length = len(self._l)
        diff = new_full_length - self._real_size
        self._useful_size += diff
        self._real_size += diff
        full_size_diff = 0

        while index < self._real_size:
            piece_size = len(self._l[index])
            self._l_length.append(piece_size)
            full_size_diff += piece_size
            index += 1
        self._data_full_size.value += full_size_diff
        self._external_data_full_size.value += full_size_diff

    def get(self):
        # l_offset_limit = 1000: 574305.7210067833 iterations per second
        # PyPy: l_offset_limit = 1000: 6666620.042915044 iterations per second
        if self._useful_size <= 0:
            raise FIFOIsEmpty()

        if not self._data_full_size:
            self._calculate_data_full_size()

        result = self._l[self._offset]
        result_len = self._l_length[self._offset]
        # self._l_deletable_length.append(result_len)
        self._deletable_data_full_size += result_len
        self._external_deletable_data_full_size.value += result_len

        self._useful_size -= 1
        self._offset += 1
        if (self._offset >= self._offset_limit) or (self._deletable_data_full_size > self._on_hold_data_size_limit):
            self._real_size -= self._offset
            self._l = self._l[self._offset:]
            # diff_full_data_size = sum(self._l_length[:self._offset])
            # diff_full_data_size = self._deletable_data_full_size
            self._data_full_size.value -= self._deletable_data_full_size
            self._external_data_full_size.value -= self._deletable_data_full_size
            self._l_length = self._l_length[self._offset:]
            self._offset = 0
            # self.get_data_full_size()
            # self._l_deletable_length = list()
            self._external_deletable_data_full_size.value -= self._deletable_data_full_size
            self._deletable_data_full_size = 0
        return result

    # @profile
    def _free(self, num):
        result = self._l_length[self._offset:self._offset + num]
        result_len = sum(result)
        # self._l_deletable_length.extend(result)
        self._deletable_data_full_size += result_len
        self._external_deletable_data_full_size.value += result_len

        self._useful_size -= num
        self._offset += num
        if (self._offset >= self._offset_limit) or (self._deletable_data_full_size > self._on_hold_data_size_limit):
            self._real_size -= self._offset
            self._l = self._l[self._offset:]
            self._data_full_size.value -= self._deletable_data_full_size
            self._external_data_full_size.value -= self._deletable_data_full_size
            self._l_length = self._l_length[self._offset:]
            self._offset = 0
            # self._l_deletable_length = list()
            self._external_deletable_data_full_size.value -= self._deletable_data_full_size
            self._deletable_data_full_size = 0

    def _calculate_data_full_size(self):
        data_full_size = sum(self._l_length)
        last_data_full_size = self._data_full_size.value
        diff_data_full_size = data_full_size - last_data_full_size
        self._data_full_size.set(data_full_size)
        self._external_data_full_size.value += diff_data_full_size

    def get_data_full_size(self):
        if not self._data_full_size:
            self._calculate_data_full_size()

        return self._data_full_size.value

    def get_deletable_data_full_size(self):
        return self._deletable_data_full_size

    def remove(self):
        if not self._removed:
            self._external_data_full_size.value -= self._data_full_size.value
            self._external_deletable_data_full_size.value -= self._deletable_data_full_size
            self._removed = True

    def __copy__(self):
        return FIFOWithLengthControl(self._init_param__on_hold_limit,
                                     self._init_param__on_hold_data_size_limit,
                                     self._init_param__external_data_full_size,
                                     self._init_param__external_deletable_data_full_size)

    def __del__(self):
        self.remove()


class FIFODequeWithLengthControl:
    def __init__(self, external_data_full_size: ValueExistence = None):
        self._removed = False

        self._l = deque()
        self._real_size = 0

        self._init_param__external_data_full_size = external_data_full_size

        # self._l_length = deque()
        self._data_full_size = 0
        self._external_data_full_size = external_data_full_size or ValueExistence(False, 0)

    def put(self, data):
        self._l.append(data)
        self._real_size += 1

        data_size = len(data)
        # self._l_length.append(data_size)
        self._data_full_size += data_size
        self._external_data_full_size.value += data_size

    def extend(self, iterable_data):
        full_size_diff = 0
        for elem in iterable_data:
            self._l.append(elem)
            self._real_size += 1
            elem_size = len(elem)
            # self._l_length.append(elem_size)
            full_size_diff += elem_size
        self._data_full_size += full_size_diff
        self._external_data_full_size.value += full_size_diff

    def get(self):
        if self._real_size <= 0:
            raise FIFOIsEmpty()

        result = self._l.popleft()
        # result_len = self._l_length.popleft()
        result_len = len(result)
        self._real_size -= 1
        self._data_full_size -= result_len
        self._external_data_full_size.value -= result_len

        return result

    def get_at_least_size(self, minimum_data_size):
        if self._real_size <= 0:
            raise FIFOIsEmpty()

        result_data = deque()
        result_size = 0
        result_qnt = 0

        while self._real_size and (result_size < minimum_data_size):
            another_piece = self._l.popleft()
            result_data.append(another_piece)
            self._real_size -= 1
            # result_len = self._l_length.popleft()
            result_len = len(another_piece)
            self._data_full_size -= result_len
            self._external_data_full_size.value -= result_len
            result_size += result_len
            result_qnt += 1

        result = (result_data, result_size, result_qnt)
        return result

    def get_data_full_size(self):
        return self._data_full_size

    def remove(self):
        if not self._removed:
            self._external_data_full_size.value -= self._data_full_size
            self._removed = True

    def __copy__(self):
        return FIFODequeWithLengthControl(self._init_param__external_data_full_size)

    def __del__(self):
        self.remove()

    def size(self):
        return self._real_size

    def full_size(self):
        return self._real_size
