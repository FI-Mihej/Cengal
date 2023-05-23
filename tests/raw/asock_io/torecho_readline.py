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
__version__ = "3.2.2"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from tornado.ioloop import IOLoop
from tornado.tcpserver import TCPServer


class StreamHandler:
    def __init__(self, stream):
        self._stream = stream
        stream.set_nodelay(True)
        self._stream.read_until(b'\n', self._handle_read)

    def _handle_read(self, data):
        self._stream.write(data)
        self._stream.read_until(b'\n', self._handle_read)


class EchoServer(TCPServer):
    def handle_stream(self, stream, address):
        StreamHandler(stream)


if __name__ == '__main__':
    server = EchoServer()
    server.bind(25000)
    server.start(1)
    IOLoop.instance().start()
    IOLoop.instance().close()
