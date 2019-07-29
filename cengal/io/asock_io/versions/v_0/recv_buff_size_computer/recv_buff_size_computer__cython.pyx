import cython


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = 'ButenkoMS <gtalk@butenkoms.space>'


if cython.compiled:
    print('"{}" - compiled.'.format(__name__))
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
