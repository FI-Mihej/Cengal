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

import cython
from collections import deque
from cengal.code_flow_control.smart_values.versions.v_0 import ResultExistence

"""
Динамический кусочный массив данных. Заполняется отдельными массивами байт (например принятых по TCP во время
ассинхронного режима работы сокета), но функционирует так, как буд-то это цельный непрерывный массив.
Дает значительный выигрыш в скорости по сравнению с обновлением встроенного контейнера list() за счет гораздо
меньшего количества аллокаций и копирований памяти.
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


if cython.compiled:
    # print('"{}" - compiled.'.format(__name__))
    pass
else:
    print('"{}" - interpreted script.'.format(__name__))


cdef class DynamicListOfPieces:
    cdef object _init_param__joiner
    cdef long long _init_param__on_hold_limit

    cdef object _joiner

    cdef object _data
    cdef long long _data_length

    cdef long long _offset_limit
    cdef long long _useful_size
    cdef long long _real_size

    def __init__(self, object joiner=None, long long on_hold_limit=0):
        self._init_param__joiner = joiner
        self._init_param__on_hold_limit = on_hold_limit

        self._joiner = b'' if joiner is None else joiner

        self._data = list()
        self._data_length = 0

        self._offset_limit = on_hold_limit or 1000
        self._useful_size = 0
        self._real_size = 0

    def add_piece_of_data(self, object piece_of_data):
        self._data.append(piece_of_data)
        self._data_length += len(piece_of_data)
        self._useful_size += 1
        self._real_size += 1

    def size(self):
        return self._data_length

    def get_data(self, long long size):
        """
        :param size:
        :return: data or None (if size > self._data_length)
        """
        if size > self._data_length:
            return None
        elif size <= 0:
            # return self._joiner.join(list())  # this is 1.6 times more faster than copy.copy(self._joiner)
            return self._joiner

        cdef long long result_data_length = 0
        cdef long long pieces_qnt = self._real_size - self._useful_size
        cdef long long delta_range = pieces_qnt

        cdef object result = None

        cdef object piece
        cdef long long piece_length = 0

        cdef object result_list = None

        cdef object splittable_piece = None
        cdef long long needed = 0
        cdef object last_current_data_part = None
        cdef object first_undecoded_data_part = None

        if size < len(self._data[pieces_qnt]):
            result = self._data[pieces_qnt][:size]
            self._data_length -= size
            self._data[pieces_qnt] = self._data[pieces_qnt][size:]
            return result
        elif size == len(self._data[pieces_qnt]):
            result = self._data[pieces_qnt]
            self._data_length -= size
            pieces_qnt += 1
            self._useful_size -= 1
            if pieces_qnt >= self._offset_limit:
                self._real_size = self._useful_size
                self._data = self._data[pieces_qnt:]
            return result
        else:
            for piece_num in range(delta_range, self._real_size):
                piece = self._data[piece_num]
                piece_length = len(piece)
                if (result_data_length + piece_length) <= size:
                    result_data_length += piece_length
                    pieces_qnt += 1
                else:
                    break

            result_list = list()
            if size > result_data_length:
                splittable_piece = self._data[pieces_qnt]
                # if (len(splittable_piece) > 4096 * 1024**2) and (type(splittable_piece) is not memoryview):
                #     splittable_piece = memoryview(splittable_piece)
                needed = size - result_data_length

                last_current_data_part = splittable_piece[:needed]
                first_undecoded_data_part = splittable_piece[needed:]

                # result_list.append(last_current_data_part)
                self._data[pieces_qnt] = first_undecoded_data_part

                result_list = self._data[delta_range:pieces_qnt]
                result_list.append(last_current_data_part)

            else:
                result_list = self._data[delta_range:pieces_qnt]

            self._useful_size = self._real_size - pieces_qnt
            if pieces_qnt >= self._offset_limit:
                self._real_size = self._useful_size
                self._data = self._data[pieces_qnt:]

            self._data_length -= size

            result = self._joiner.join(result_list)

            if len(result) > 4096:
                result = memoryview(result)

            return result

    def read_data(self, long long size):
        """
        :param size:
        :return: data or None (if size > self._data_length)
        """
        if size > self._data_length:
            return None
        elif size <= 0:
            # return self._joiner.join(list())  # this is 1.6 times more faster than copy.copy(self._joiner)
            return self._joiner

        cdef long long result_data_length = 0
        cdef long long pieces_qnt = self._real_size - self._useful_size
        cdef long long delta_range = pieces_qnt

        cdef object piece
        cdef long long piece_length = 0

        cdef object result_list = None

        cdef object splittable_piece = None
        cdef long long needed = 0

        cdef object result

        if size < len(self._data[pieces_qnt]):
            return self._data[pieces_qnt][:size]
        elif size == len(self._data[pieces_qnt]):
            return self._data[pieces_qnt]
        else:
            for piece_num in range(delta_range, self._real_size):
                piece = self._data[piece_num]
                piece_length = len(piece)
                if (result_data_length + piece_length) <= size:
                    result_data_length += piece_length
                    pieces_qnt += 1
                else:
                    break

            result_list = list()
            if size > result_data_length:
                splittable_piece = self._data[pieces_qnt]
                needed = size - result_data_length

                result_list = self._data[delta_range:pieces_qnt]
                result_list.append(splittable_piece[:needed])

            else:
                result_list = self._data[delta_range:pieces_qnt]

            result = self._joiner.join(result_list)

            if len(result) > 4096:
                result = memoryview(result)

            return result

    def remove(self):
        pass

    def __copy__(self):
        return DynamicListOfPieces(self._init_param__joiner,
                                   self._init_param__on_hold_limit)


cdef class DynamicListOfPiecesWithLengthControl(DynamicListOfPieces):
    cdef bint _removed

    cdef long long _init_param__on_hold_data_size_limit
    cdef object _init_param__external_data_length
    cdef object _init_param__external_deletable_data_full_size

    cdef long long _on_hold_data_size_limit
    cdef long long _deletable_data_full_size

    cdef object _external_data_length
    cdef object _external_deletable_data_full_size

    def __init__(self, object joiner=None, long long on_hold_limit=0, long long on_hold_data_size_limit=0,
                 object external_data_length=None,
                 object external_deletable_data_full_size=None):
        super(DynamicListOfPiecesWithLengthControl, self).__init__(joiner, on_hold_limit)

        self._removed = True

        self._init_param__on_hold_data_size_limit = on_hold_data_size_limit
        self._init_param__external_data_length = external_data_length
        self._init_param__external_deletable_data_full_size = external_deletable_data_full_size

        self._on_hold_data_size_limit = on_hold_data_size_limit or 1024**2
        self._deletable_data_full_size = 0

        self._external_data_length = external_data_length or ResultExistence(False, 0)
        self._external_deletable_data_full_size = external_deletable_data_full_size or ResultExistence(False, 0)

    def add_piece_of_data(self, object piece_of_data):
        self._data.append(piece_of_data)
        piece_of_data_len = len(piece_of_data)
        self._data_length += piece_of_data_len
        self._external_data_length.result += piece_of_data_len
        self._useful_size += 1
        self._real_size += 1

    # @profile
    def get_data(self, long long size):
        """
        :param size:
        :return: data or None (if size > self._data_length)
        """
        if size > self._data_length:
            return None
        elif size <= 0:
            # return self._joiner.join(list())  # this is 1.6 times more faster than copy.copy(self._joiner)
            return self._joiner

        cdef long long result_data_length = 0
        cdef long long pieces_qnt = self._real_size - self._useful_size
        cdef long long delta_range = pieces_qnt

        cdef object result = None

        cdef object piece
        cdef long long piece_length = 0

        cdef object result_list = None

        cdef object splittable_piece = None
        cdef long long needed = 0
        cdef object last_current_data_part = None
        cdef object first_undecoded_data_part = None

        first_piece_len = len(self._data[pieces_qnt])
        if size < first_piece_len:
            result = self._data[pieces_qnt][:size]
            self._data_length -= size
            self._external_data_length.result -= size
            self._deletable_data_full_size += size
            self._external_deletable_data_full_size.result += size
            self._data[pieces_qnt] = self._data[pieces_qnt][size:]
            return result
        elif size == first_piece_len:
            result = self._data[pieces_qnt]
            self._data_length -= size
            self._external_data_length.result -= size
            self._deletable_data_full_size += size
            self._external_deletable_data_full_size.result += size
            pieces_qnt += 1
            self._useful_size -= 1
            if (pieces_qnt >= self._offset_limit) or (self._deletable_data_full_size > self._on_hold_data_size_limit):
                self._external_deletable_data_full_size.result -= self._deletable_data_full_size
                self._deletable_data_full_size = 0
                self._real_size = self._useful_size
                self._data = self._data[pieces_qnt:]
            return result
        else:
            for piece_num in range(delta_range, self._real_size):
                piece = self._data[piece_num]
                piece_length = len(piece)
                if (result_data_length + piece_length) <= size:
                    result_data_length += piece_length
                    pieces_qnt += 1
                else:
                    break

            result_list = list()
            if size > result_data_length:
                splittable_piece = self._data[pieces_qnt]
                # if (len(splittable_piece) > 4096 * 1024**2) and (type(splittable_piece) is not memoryview):
                #     splittable_piece = memoryview(splittable_piece)
                needed = size - result_data_length

                last_current_data_part = splittable_piece[:needed]
                first_undecoded_data_part = splittable_piece[needed:]

                # result_list.append(last_current_data_part)
                self._data[pieces_qnt] = first_undecoded_data_part

                result_list = self._data[delta_range:pieces_qnt]
                result_list.append(last_current_data_part)

            else:
                result_list = self._data[delta_range:pieces_qnt]

            self._deletable_data_full_size += size
            self._external_deletable_data_full_size.result += size
            self._useful_size = self._real_size - pieces_qnt
            if pieces_qnt >= self._offset_limit:
                self._external_deletable_data_full_size.result -= self._deletable_data_full_size
                self._deletable_data_full_size = 0
                self._real_size = self._useful_size
                self._data = self._data[pieces_qnt:]

            self._data_length -= size
            self._external_data_length.result -= size

            # result = self._joiner.join(result_list)
            #
            # if len(result) > 4096:
            #     result = memoryview(result)
            #
            # return result

            return memoryview(self._joiner.join(result_list))

    def remove(self):
        if not self._removed:
            self._external_data_length.result -= self._data_length
            self._external_deletable_data_full_size.result -= self._deletable_data_full_size
            self._removed = True

    def __copy__(self):
        return DynamicListOfPiecesWithLengthControl(self._init_param__joiner,
                                                    self._init_param__on_hold_limit,
                                                    self._init_param__on_hold_data_size_limit,
                                                    self._init_param__external_data_length,
                                                    self._init_param__external_deletable_data_full_size)

    def __del__(self):
        self.remove()


cdef class DynamicListOfPiecesDequeWithLengthControl:
    cdef bint _removed

    cdef object _init_param__joiner
    cdef object _init_param__external_data_length

    cdef object _joiner

    cdef object _data
    cdef long long _data_length

    cdef long long _real_size

    cdef object _external_data_length

    def __init__(self, object joiner=None, object external_data_length=None):
        self._removed = True

        self._init_param__joiner = joiner
        self._init_param__external_data_length = external_data_length

        self._joiner = b'' if joiner is None else joiner
        self._data = deque()
        self._data_length = 0

        self._real_size = 0

        self._external_data_length = external_data_length or ResultExistence(False, 0)

    def size(self):
        return self._data_length

    def qnt(self):
        return self._real_size

    def add_piece_of_data(self, object piece_of_data):
        cdef long long piece_of_data_len

        self._data.append(piece_of_data)
        piece_of_data_len = len(piece_of_data)
        self._data_length += piece_of_data_len
        self._external_data_length.result += piece_of_data_len
        self._real_size += 1

    # @profile
    def get_data(self, long long size):
        """
        :param size:
        :return: data or None (if size > self._data_length)
        """
        if size > self._data_length:
            return None
        elif size <= 0:
            # return self._joiner.join(list())  # this is 1.6 times more faster than copy.copy(self._joiner)
            return self._joiner

        cdef long long first_piece_len
        cdef object current_piece
        cdef object result_data
        cdef long long result_size
        cdef object another_piece
        cdef long long another_piece_len
        cdef long long delta_size

        first_piece_len = len(self._data[0])
        if size < first_piece_len:
            current_piece = memoryview(self._data[0])
            self._data[0] = current_piece[size:]
            self._data_length -= size
            self._external_data_length.result -= size
            return current_piece[:size]
        elif size == first_piece_len:
            self._data_length -= size
            self._external_data_length.result -= size
            self._real_size -= 1
            # return memoryview(self._data.popleft())
            return self._data.popleft()
        else:
            result_data = deque()
            result_size = 0

            while self._real_size and (result_size < size):
                another_piece = self._data.popleft()
                another_piece_len = len(another_piece)
                result_data.append(another_piece)
                self._data_length -= another_piece_len
                self._external_data_length.result -= another_piece_len
                self._real_size -= 1
                result_size += another_piece_len
                if (result_size < size) and ((len(self._data[0]) + result_size) > size):
                    break

            if result_size < size:
                delta_size = size - result_size
                current_piece = memoryview(self._data[0])
                result_data.append(current_piece[:delta_size])
                self._data[0] = current_piece[delta_size:]
                self._data_length -= delta_size
                self._external_data_length.result -= delta_size

            # return memoryview(self._joiner.join(result_data))
            return self._joiner.join(result_data)

    def read_data(self, long long size):
        """
        :param size:
        :return: data or None (if size > self._data_length)
        """
        if size > self._data_length:
            return None
        elif size <= 0:
            # return self._joiner.join(list())  # this is 1.6 times more faster than copy.copy(self._joiner)
            return self._joiner

        cdef long long first_piece_len
        cdef object current_piece
        cdef object result_data
        cdef long long result_size
        cdef object another_piece
        cdef long long another_piece_len
        cdef long long delta_size
        cdef long long piece_index

        first_piece_len = len(self._data[0])
        if size < first_piece_len:
            current_piece = memoryview(self._data[0])
            return current_piece[:size]
        elif size == first_piece_len:
            return memoryview(self._data[0])
        else:
            result_data = deque()
            result_size = 0

            piece_index = 0
            while self._real_size and (result_size < size):
                another_piece = self._data[index]
                index += 1
                another_piece_len = len(another_piece)
                result_data.append(another_piece)
                result_size += another_piece_len
                if (result_size < size) and ((len(self._data[index]) + result_size) > size):
                    break

            if result_size < size:
                delta_size = size - result_size
                current_piece = memoryview(self._data[index])
                result_data.append(current_piece[:delta_size])

            # return memoryview(self._joiner.join(result_data))
            return self._joiner.join(result_data)

    # @profile
    def get_data_pieces(self, long long size):
        """
        :param size:
        :return: data or None (if size > self._data_length)
        """
        if size > self._data_length:
            return None
        elif size <= 0:
            # return self._joiner.join(list())  # this is 1.6 times more faster than copy.copy(self._joiner)
            return self._joiner

        cdef long long first_piece_len
        cdef object current_piece
        cdef object result_data
        cdef long long result_size
        cdef object another_piece
        cdef long long another_piece_len
        cdef long long delta_size

        first_piece_len = len(self._data[0])
        if size <= first_piece_len:
            self._data_length -= size
            self._external_data_length.result -= size
            self._real_size -= 1
            return self._data.popleft()
        else:
            result_data = deque()
            result_size = 0

            while self._real_size and (result_size < size):
                another_piece = self._data.popleft()
                another_piece_len = len(another_piece)
                result_data.append(another_piece)
                self._data_length -= another_piece_len
                self._external_data_length.result -= another_piece_len
                self._real_size -= 1
                result_size += another_piece_len

            return result_data

    def read_data_pieces(self, long long size):
        """
        :param size:
        :return: data or None (if size > self._data_length)
        """
        if size > self._data_length:
            return None
        elif size <= 0:
            # return self._joiner.join(list())  # this is 1.6 times more faster than copy.copy(self._joiner)
            return self._joiner

        cdef long long first_piece_len
        cdef object current_piece
        cdef object result_data
        cdef long long result_size
        cdef object another_piece
        cdef long long another_piece_len
        cdef long long delta_size
        cdef long long piece_index

        first_piece_len = len(self._data[0])
        if size <= first_piece_len:
            return memoryview(self._data[0])
        else:
            result_data = deque()
            result_size = 0

            piece_index = 0
            while self._real_size and (result_size < size):
                another_piece = memoryview(self._data[index])
                index += 1
                another_piece_len = len(another_piece)
                result_data.append(another_piece)
                result_size += another_piece_len

            return result_data

    def remove(self):
        if not self._removed:
            self._external_data_length.result -= self._data_length
            self._removed = True

    def __copy__(self):
        return DynamicListOfPiecesDequeWithLengthControl(
            self._init_param__joiner, self._init_param__external_data_length)

    def __del__(self):
        self.remove()


def get_num_pieces_with_full_size_lesser_than(object iter_object, long long full_size):
    cdef long long index = -1
    cdef long long result_size = 0
    cdef long long piece_len = 0
    cdef object piece

    if iter_object:
        result_size = 0
        index = 0
        for piece in iter_object:
            piece_len = len(piece)
            if (result_size + piece_len) > full_size:
                break
            else:
                result_size += piece_len
                index += 1
    return index


def get_num_pieces_with_full_size_lesser_than_with_offset(object iter_object, long long full_size,
                                                                              long long offset):
    cdef long long pieces_qnt = -1
    cdef long long object_size = 0
    cdef long long result_data_length = 0
    cdef long long piece_num = 0
    cdef object piece
    cdef long long piece_length = 0

    if iter_object:
        object_size = len(iter_object)
        result_data_length = 0
        pieces_qnt = 0
        for piece_num in range(offset, object_size):
            piece = iter_object[piece_num]
            piece_length = len(piece)
            if (result_data_length + piece_length) > full_size:
                break
            else:
                result_data_length += piece_length
                pieces_qnt += 1
    return pieces_qnt
