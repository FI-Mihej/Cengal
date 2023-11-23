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


import socket
import errno
from cengal.code_flow_control.smart_values.versions.v_0 import ResultExistence
from cengal.base.classes import BaseClassSettings



__author__ = 'ButenkoMS <gtalk@butenkoms.space>'


SET_OF_CONNECTION_ERRORS = {errno.ECONNRESET, errno.ECONNREFUSED, errno.ECONNABORTED, errno.EPIPE, errno.ESHUTDOWN}
INET_TYPE_CONNECTIONS = {socket.AF_INET, socket.AF_INET6}


try:
    BlockingIOError
except NameError:
    class BlockingIOError(OSError):
        pass

try:
    InterruptedError
except NameError:
    class InterruptedError(OSError):
        pass

try:
    ConnectionError
except NameError:
    class ConnectionError(OSError):
        pass

try:
    BrokenPipeError
except NameError:
    class BrokenPipeError(ConnectionError):
        pass

try:
    ConnectionAbortedError
except NameError:
    class ConnectionAbortedError(ConnectionError):
        pass

try:
    ConnectionRefusedError
except NameError:
    class ConnectionRefusedError(ConnectionError):
        pass

try:
    ConnectionResetError
except NameError:
    class ConnectionResetError(ConnectionError):
        pass


MESSAGE_SIZE_LEN = 8
SERVER_ANSWER__KEYWORD_ACCEPTED = b'OK'


class SimpleNetworkError(Exception):
    pass


class ConnectionDirectionRole:
    server = 0
    client = 1


# class IPVersion:
#     ipv4 = 0
#     ipv6 = 1


# class ConnectionSettings(BaseClassSettings):
#     def __init__(self, host=None, port=None, keyword=None, direction_role=None, ip_version=None):
#         '''
#         :param host: 'localhost', '192.168.0.1', ect.
#         :param port: 8080
#         :param keyword: b'sdlkfj s894 saf 84ewksdhf sdf'
#         :param direction_role: ConnectionDirectionRole()
#         :param ip_version: IPVersion()
#         :return:
#         '''
#         self.host = host or str()
#         self.port = port or None
#         self.keyword = keyword or bytes()
#         self.direction_role = direction_role or None
#         self.ip_version = ip_version or None
#
#     def check(self):
#         if (self.port is None) or (self.direction_role is None) or (self.ip_version is None):
#             raise Exception('port can\'t be None; direction_role can\'t be None; ip_version can\'t be None.')


class ConnectionSettings(BaseClassSettings):
    def __init__(self, direction_role: ConnectionDirectionRole=None, socket_address=None, keyword: bytes=None,
                 socket_family=socket.AF_INET, socket_type=socket.SOCK_STREAM, socket_protocol=0, socket_fileno=None):
        '''
        :param direction_role: ConnectionDirectionRole()
        :param socket_address: './main.server.AF_UNIX.socket', ('localhost', 8080), ('::', 50007, 0, 0), , ect.
        :param keyword: b'sdlkfj s894 saf 84ewksdhf sdf'. Can be None for a Super Server
        :param socket_family: AF_INET (the default), AF_INET6, AF_UNIX, AF_CAN or AF_RDS
        :param socket_type: SOCK_STREAM (the default), SOCK_DGRAM, SOCK_RAW or perhaps one of the other SOCK_ constants
        :param socket_protocol: in the case where the address family is AF_CAN the protocol should be one of CAN_RAW or
            CAN_BCM
        :param socket_fileno: If fileno is specified, the other arguments are ignored, causing the socket with the
            specified file descriptor to return
        '''
        self.direction_role = direction_role
        self.keyword = keyword
        self.socket_address = socket_address
        self.socket_family = socket_family
        self.socket_type = socket_type
        self.socket_protocol = socket_protocol
        self.socket_fileno = socket_fileno
        self.expected_clients_with_empty_output_fifo = set()


class IOCoreMemoryManagement:
    def __init__(self):
        self.global__data_size_limit = ResultExistence(True, 2 * 1024**3)

        self.global_in__data_size_limit = ResultExistence(True, 512 * 1024**2)
        self.global_in__data_full_size = ResultExistence(True, 0)
        self.global_in__deletable_data_full_size = ResultExistence(True, 0)

        self.global_out__data_size_limit = ResultExistence(True, 512 * 1024**2)
        self.global_out__data_full_size = ResultExistence(True, 0)
        self.global_out__deletable_data_full_size = ResultExistence(True, 0)

    def link_to(self, parent):
        self.global__data_size_limit = parent.global__data_size_limit

        self.global_in__data_size_limit = parent.global_in__data_size_limit
        self.global_in__data_full_size = parent.global_in__data_full_size
        self.global_in__deletable_data_full_size = parent.global_in__deletable_data_full_size

        self.global_out__data_size_limit = parent.global_out__data_size_limit
        self.global_out__data_full_size = parent.global_out__data_full_size
        self.global_out__deletable_data_full_size = parent.global_out__deletable_data_full_size
