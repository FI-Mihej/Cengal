"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = 'ButenkoMS <gtalk@butenkoms.space>'


class RecvBuffSizeComputer:
    def __init__(self):
        self._min_recv_buff_size = 1024
        self._max_recv_buff_size = 1024 * 1024 * 10
        self.recv_buff_size = self._min_recv_buff_size
        self._last_recv_amount = 0
        self._previous_recv_amount = 0

    def calc_new_recv_buff_size(self, last_recv_amount):
        biggest_recv_amount = 0
        new_amount = 0

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
