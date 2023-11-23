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
from cengal.code_flow_control.none_or import none_or
from cengal.code_flow_control.smart_values.versions.v_0 import ResultExistence
from cengal.data_containers.fast_fifo import FIFODequeWithLengthControl
from typing import Optional, Tuple, List

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


# print("Just a lowly interpreted script.")


class DynamicListOfPieces:
    def __init__(self, joiner=None, on_hold_limit=None):
        self._init_param__joiner = joiner
        self._init_param__on_hold_limit = on_hold_limit

        self._joiner = none_or(joiner, b'')
        self._data = list()
        self._data_length = 0

        self._offset_limit = on_hold_limit or 1000
        self._useful_size = 0
        self._real_size = 0

    def add_piece_of_data(self, piece_of_data):
        self._data.append(piece_of_data)
        piece_of_data_len = len(piece_of_data)
        self._data_length += piece_of_data_len
        self._useful_size += 1
        self._real_size += 1

    def size(self):
        return self._data_length

    def qnt(self):
        return self._useful_size

    # @profile
    def get_data(self, size):
        """
        :param size:
        :return: data or None (if size > self._data_length)
        """
        if size > self._data_length:
            return None
        elif size <= 0:
            # return self._joiner.join(list())  # this is 1.6 times more faster than copy.copy(self._joiner)
            return self._joiner

        result_data_length = 0
        pieces_qnt = delta_range = self._real_size - self._useful_size

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

            # result = self._joiner.join(result_list)
            #
            # if len(result) > 4096:
            #     result = memoryview(result)
            #
            # return result

            return memoryview(self._joiner.join(result_list))

    # @profile
    def read_data(self, size):
        """
        :param size:
        :return: data or None (if size > self._data_length)
        """
        if size > self._data_length:
            return None
        elif size <= 0:
            # return self._joiner.join(list())  # this is 1.6 times more faster than copy.copy(self._joiner)
            return self._joiner

        result_data_length = 0
        pieces_qnt = delta_range = self._real_size - self._useful_size

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

            # result = self._joiner.join(result_list)
            # return result

            return self._joiner.join(result_list)

    def remove(self):
        pass

    def __copy__(self):
        return DynamicListOfPieces(self._init_param__joiner,
                                   self._init_param__on_hold_limit)


class DynamicListOfPiecesWithLengthControl(DynamicListOfPieces):
    def __init__(self, joiner=None, on_hold_limit=None, on_hold_data_size_limit=None,
                 external_data_length: ResultExistence=None,
                 external_deletable_data_full_size: ResultExistence=None):
        super(DynamicListOfPiecesWithLengthControl, self).__init__(joiner, on_hold_limit)

        self._removed = False

        self._init_param__on_hold_data_size_limit = on_hold_data_size_limit
        self._init_param__external_data_length = external_data_length
        self._init_param__external_deletable_data_full_size = external_deletable_data_full_size

        self._on_hold_data_size_limit = on_hold_data_size_limit or 1024**2
        self._deletable_data_full_size = 0

        self._external_data_length = external_data_length or ResultExistence(False, 0)
        self._external_deletable_data_full_size = external_deletable_data_full_size or ResultExistence(False, 0)

    def add_piece_of_data(self, piece_of_data):
        self._data.append(piece_of_data)
        piece_of_data_len = len(piece_of_data)
        self._data_length += piece_of_data_len
        self._external_data_length.result += piece_of_data_len
        self._useful_size += 1
        self._real_size += 1

    # @profile
    def get_data(self, size):
        """
        :param size:
        :return: data or None (if size > self._data_length)
        """
        if size > self._data_length:
            return None
        elif size <= 0:
            # return self._joiner.join(list())  # this is 1.6 times more faster than copy.copy(self._joiner)
            return self._joiner

        result_data_length = 0
        pieces_qnt = delta_range = self._real_size - self._useful_size

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


class DynamicListOfPiecesDequeWithLengthControl:
    def __init__(self, joiner=None, external_data_length: ResultExistence=None):
        self._removed = False

        self._init_param__joiner = joiner
        self._init_param__external_data_length = external_data_length

        self._joiner = none_or(joiner, b'')
        self._data = deque()
        self._data_length = 0

        self._real_size = 0

        self._external_data_length = external_data_length or ResultExistence(False, 0)

    def size(self):
        return self._data_length

    def qnt(self):
        return self._real_size

    def add_piece_of_data(self, piece_of_data):
        self._data.append(piece_of_data)
        piece_of_data_len = len(piece_of_data)
        self._data_length += piece_of_data_len
        self._external_data_length.result += piece_of_data_len
        self._real_size += 1

    # @profile
    def get_data(self, size):
        """
        :param size:
        :return: data or None (if size > self._data_length)
        """
        if size > self._data_length:
            return None
        elif size <= 0:
            # return self._joiner.join(list())  # this is 1.6 times more faster than copy.copy(self._joiner)
            return self._joiner

        first_piece_len = len(self._data[0])
        if size < first_piece_len:
            current_piece = memoryview(self._data[0])
            result = current_piece[:size]
            self._data[0] = current_piece[size:]
            self._data_length -= size
            self._external_data_length.result -= size
            return result
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

    def read_data(self, size):
        """
        :param size:
        :return: data or None (if size > self._data_length)
        """
        if size > self._data_length:
            return None
        elif size <= 0:
            # return self._joiner.join(list())  # this is 1.6 times more faster than copy.copy(self._joiner)
            return self._joiner

        first_piece_len = len(self._data[0])
        if size < first_piece_len:
            current_piece = memoryview(self._data[0])
            return current_piece[:size]
        elif size == first_piece_len:
            return memoryview(self._data[0])
        else:
            result_data = deque()
            result_size = 0

            index = 0
            while result_size < size:
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

            return self._joiner.join(result_data)

    # @profile
    def get_data_pieces(self, size) -> List[bytes]:
        """
        :param size:
        :return: data or None (if size > self._data_length)
        """
        if size > self._data_length:
            return None
        elif size <= 0:
            # return self._joiner.join(list())  # this is 1.6 times more faster than copy.copy(self._joiner)
            return [self._joiner]

        first_piece_len = len(self._data[0])
        if size <= first_piece_len:
            self._data_length -= first_piece_len
            self._external_data_length.result -= first_piece_len
            self._real_size -= 1
            return [self._data.popleft()]
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

    def read_data_pieces(self, size):
        """
        :param size:
        :return: data or None (if size > self._data_length)
        """
        if size > self._data_length:
            return None
        elif size <= 0:
            # return self._joiner.join(list())  # this is 1.6 times more faster than copy.copy(self._joiner)
            return [self._joiner]

        first_piece_len = len(self._data[0])
        if size <= first_piece_len:
            return [memoryview(self._data[0])]
        else:
            result_data = deque()
            result_size = 0

            index = 0
            while result_size < size:
                another_piece = memoryview(self._data[index])
                index += 1
                another_piece_len = len(another_piece)
                result_data.append(another_piece)
                result_size += another_piece_len

            return result_data

    def get_data_at_least(self, size):
        return self._joiner.join(self.get_data_pieces(size))

    def read_data_at_least(self, size):
        return self._joiner.join(self.read_data_pieces(size))

    def get_data_nearly(self, size):
        return self._joiner.join(self.get_data_pieces(min(size, self.size())))

    def read_data_nearly(self, size):
        return self._joiner.join(self.read_data_pieces(min(size, self.size())))
    
    def item_by_index(self, index: int) -> Tuple[int, int]:
        if index >= self._data_length:
            return -1, -1
        
        offset = 0
        for item_index, item in enumerate(self._data):
            item_len = len(item)
            offset += item_len
            if index < offset:
                index_within_item = item_len - (offset - index)
                return item_index, index_within_item
    
    def startswith(self, 
        __prefix,
        __start = None,
        __end = None
    ) -> bool:
        if not self._data_length:
            return False
            
        if isinstance(__prefix, tuple):
            prefix_len = max((len(item) for item in __prefix))
        else:
            prefix_len = len(__prefix)
        
        start_index = __start or 0
        prefix_end_index = start_index + prefix_len
        if __end is None:
            end_index = prefix_end_index
        else:
            end_index = __end
        
        end_index = min(end_index, prefix_end_index)
        if end_index < start_index:
            return False

        start_item_index, index_within_start_item = self.item_by_index(start_index)
        if -1 == start_item_index:
            return False
        
        end_item_index, index_within_end_item = self.item_by_index(end_index)
        if -1 == end_item_index:
            end_item_index = self._real_size -1
            index_within_end_item = len(self._data[end_item_index]) - 1
        
        return self._joiner.join(self._data[start_item_index: end_item_index]).startswith(
            __prefix, index_within_start_item, index_within_end_item)

    def find(
            self, __sub, __start = None, __end = None
        ) -> int:
        if not self._data_length:
            return False

        start_index = __start or 0
        end_index = __end or (self._data_length - 1)

        start_item_index, index_within_start_item = self.item_by_index(start_index)
        if -1 == start_item_index:
            return False
        
        end_item_index, index_within_end_item = self.item_by_index(end_index)
        if -1 == end_item_index:
            end_item_index = self._real_size -1
            index_within_end_item = len(self._data[end_item_index]) - 1
        
        return self._joiner.join(self._data[start_item_index: end_item_index]).find(
            __sub, index_within_start_item, index_within_end_item)

    def clear(self):
        self.get_data_pieces(self._real_size)

    def remove(self):
        if not self._removed:
            self._external_data_length.result -= self._data_length
            self._removed = True

    def __copy__(self):
        return DynamicListOfPiecesDequeWithLengthControl(
            self._init_param__joiner, self._init_param__external_data_length)

    def __del__(self):
        self.remove()


# TODO: implement in Cython:
class DynamicListOfPiecesMemoryviewDequeWithLengthControl:
    def __init__(self, joiner=None, external_data_length: Optional[ResultExistence] = None, mem_buffer_size: Optional[ResultExistence] = None, output_fifo: Optional[FIFODequeWithLengthControl] = None):
        self._removed = False

        self._init_param__joiner = joiner
        self._init_param__external_data_length = external_data_length
        self._init_param__mem_buffer_size = mem_buffer_size

        self._joiner = none_or(joiner, b'')
        self._data = deque()
        self._data_length = 0

        self._real_size = 0

        self._external_data_length = external_data_length or ResultExistence(False, 0)

        self.mem_buffer_size = mem_buffer_size or ResultExistence(False, 1024)
        self.mem_buffer = memoryview(bytearray(self.mem_buffer_size.result))
        self._external_data_length.result += self.mem_buffer_size.result

        self.mem_buffer_offset = 0
        self.mem_buffer_nbytes = 0
        self.mem_buffer_diff = 0
        self.mem_buffer_message_nbytes = 0

        self.output_data = output_fifo or FIFODequeWithLengthControl(self._external_data_length)

    def _allocate_new_mem_buffer(self):
        self._external_data_length.result -= len(self.mem_buffer.obj)
        self.mem_buffer = memoryview(bytearray(self.mem_buffer_size.result))
        self._external_data_length.result += self.mem_buffer_size.result

    def size(self):
        return self._data_length

    def qnt(self):
        return self._real_size

    def add_piece_of_data(self, piece_of_data):
        raise NotImplemented()

    def _add_piece_of_data(self, piece_of_data):
        self._data.append(piece_of_data)
        piece_of_data_len = len(piece_of_data)
        self._data_length += piece_of_data_len
        self._external_data_length.result += piece_of_data_len
        self._real_size += 1

    def piece_of_data_had_been_added(self, nbytes):
        self.mem_buffer = self.mem_buffer[nbytes:]
        self.mem_buffer_nbytes += nbytes
        self.mem_buffer_diff += nbytes

        if not self.mem_buffer:
            if self.mem_buffer_diff:
                self._add_piece_of_data(memoryview(self.mem_buffer.obj)[self.mem_buffer_offset:])
            self._allocate_new_mem_buffer()

    # @profile
    def get_data(self, size):
        """
        :param size:
        :return: data or None (if size > self._data_length)
        """
        if size > self._data_length:
            return None
        elif size <= 0:
            # return self._joiner.join(list())  # this is 1.6 times more faster than copy.copy(self._joiner)
            return self._joiner

        first_piece_len = len(self._data[0])
        if size < first_piece_len:
            current_piece = memoryview(self._data[0])
            result = current_piece[:size]
            self._data[0] = current_piece[size:]
            self._data_length -= size
            self._external_data_length.result -= size
            return result
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

    def read_data(self, size):
        raise NotImplemented()

    def remove(self):
        if not self._removed:
            self._external_data_length.result -= self._data_length
            self._external_data_length.result -= len(self.mem_buffer.obj)
            self._removed = True

    def __copy__(self):
        return DynamicListOfPiecesDequeWithLengthControl(
            self._init_param__joiner, self._init_param__external_data_length)

    def __del__(self):
        self.remove()


def get_num_pieces_with_full_size_lesser_than(iter_object, full_size):
    index = -1
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


def get_num_pieces_with_full_size_lesser_than_with_offset(iter_object, full_size, offset):
    pieces_qnt = -1
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
