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
__version__ = "4.1.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import cProfile
import pstats
import os
from tornado.ioloop import IOLoop
from tornado.tcpserver import TCPServer
import socket

# PROFILE_CODE = True
PROFILE_CODE = False


class StreamHandler:
    def __init__(self, stream):
        print('StreamHandler.__init__()')
        self._stream = stream
        stream.set_nodelay(True)
        self._stream.set_close_callback(self._handle_close)
        self._stream.read_until_close(None, self._handle_read)

    def _handle_read(self, data):
        # print('StreamHandler._handle_read()')
        self._stream.write(data)

    def _handle_close(self):
        print('StreamHandler._handle_close()')
        if PROFILE_CODE:
            IOLoop.instance().stop()


class EchoServer(TCPServer):
    def handle_stream(self, stream, address):
        print('EchoServer.handle_stream() from "{}"'.format(address))
        StreamHandler(stream)


def torecho():
    server = EchoServer()
    server.bind(18495, 'localhost', socket.AF_INET)
    # server.bind(18495, '136.243.105.170', socket.AF_INET)
    server.start(1)
    # server.start(10)
    IOLoop.instance().start()
    IOLoop.instance().close()


def profiled__torecho():
    cProfile.run('torecho()',
                 'profiled__torecho.prof')


def print_profiler_result(function_name):
    if function_name.startswith('profiled__'):
        prof_name = function_name + '.prof'
        prof_full_file_name = os.path.join(os.getcwd(), prof_name)
        s = pstats.Stats(prof_full_file_name)
        s = s.strip_dirs()
        s = s.sort_stats('cumtime', 'tottime', 'ncalls')
        # s.print_stats(.4)
        s.print_stats()
        # s.print_callees(['get_set_of_assumed_triangles'])


if __name__ == '__main__':
    if PROFILE_CODE:
        profiled__torecho()
        print_profiler_result(profiled__torecho.__name__)
    else:
        torecho()
