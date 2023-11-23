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


import os
import errno


if 'nt' == os.name:
    if not hasattr(errno, 'WSAEPIPE'):
        WSAEPIPE = -12345
    
    SET_OF_CONNECTION_ERRORS = {errno.WSAECONNRESET, errno.WSAECONNREFUSED, errno.WSAECONNABORTED, WSAEPIPE, errno.WSAESHUTDOWN}
    SET_OF_UDP_MESSAGE_SIZE_RELATED_ERRORS = {errno.WSAEMSGSIZE}
else:
    SET_OF_CONNECTION_ERRORS = {errno.ECONNRESET, errno.ECONNREFUSED, errno.ECONNABORTED, errno.EPIPE, errno.ESHUTDOWN}
    SET_OF_UDP_MESSAGE_SIZE_RELATED_ERRORS = {errno.EMSGSIZE}



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
