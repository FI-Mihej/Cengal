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

import socket
from contextlib import contextmanager
from cengal.base.classes import BaseClassSettings
from .base import *

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
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


class SimpleTcpLinkError(SimpleNetworkError):
    pass


class SimpleTcpLink:
    """
    1 to 1 TCP connection.
    """
    def __init__(self, settings: ConnectionSettings):
        """
        Port should not be open to a external world!
        :param settings: ConnectionSettings()
        :return:
        """
        self.settings = settings
        self.settings.check()
        self._block_state = True
        self._gate = None
        self._conn = None
        self._addr = None

        self.message_size_len = MESSAGE_SIZE_LEN
        self.server_answer__keyword_accepted = SERVER_ANSWER__KEYWORD_ACCEPTED
        self.use_nodelay_inet = False
        pass

    def connect(self):
        if ConnectionType.passive == self.settings.connection_type:
            self._gate = socket.socket(self.settings.socket_family, self.settings.socket_type,
                                       self.settings.socket_protocol, self.settings.socket_fileno)
            self._gate.bind(self.settings.socket_address)
            self._gate.listen(1)
            self._conn, self._addr = self._gate.accept()
            print('Connected by', self._addr)
            keyword_length_raw = self._conn.recv(self.message_size_len)
            keyword_length = int.from_bytes(keyword_length_raw, 'little')
            keyword = self._conn.recv(keyword_length)
            if keyword == self.settings.keyword:
                self._conn.sendall(self._pack_message(self.server_answer__keyword_accepted))
            else:
                # if we'll use loop, hang will be possible.
                raise SimpleTcpLinkError('Wrong keyword: {}. Should be: {}.'.format(
                    keyword, self.settings.keyword))
        elif ConnectionType.active_connected == self.settings.connection_type:
            self._conn = socket.socket(self.settings.socket_family, self.settings.socket_type,
                                       self.settings.socket_protocol, self.settings.socket_fileno)
            self._conn.connect(self.settings.socket_address)
            self.send_message_b(self.settings.keyword)
            if self.read_message_b() != self.server_answer__keyword_accepted:
                raise SimpleTcpLinkError('Server rejected the keyword: {}.'.format(
                    self.settings.keyword))
        else:
            raise NotImplementedError('Unknown ConnectionType.')

        if self.use_nodelay_inet and (self._conn.family in INET_TYPE_CONNECTIONS):
            self._conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    def send_message_b(self, data):
        self._conn.sendall(len(data).to_bytes(self.message_size_len, 'little') + data)

    def read_message_b(self):
        return self._conn.recv(int.from_bytes(self._conn.recv(self.message_size_len), 'little'))

    def send_message(self, data):
        if self._block_state:
            self.send_message_b(data)
        else:
            pass
        pass

    def read_message(self):
        if self._block_state:
            return self.read_message_b()
        else:
            pass

    def message_io_iteration(self):
        pass

    def set_blocking(self, set_blocking_mode=True):
        pass

    def close(self):
        if self._conn is not None:
            self._conn.close()
        if self._gate is not None:
            self._gate.close()

    def _pack_message(self, data):
        return len(data).to_bytes(self.message_size_len, 'little') + data


@contextmanager
def simple_tcp_link_connect(simple_tcp_obj):
    try:
        simple_tcp_obj.connect()
        yield simple_tcp_obj
    except:
        raise
    finally:
        simple_tcp_obj.close()
