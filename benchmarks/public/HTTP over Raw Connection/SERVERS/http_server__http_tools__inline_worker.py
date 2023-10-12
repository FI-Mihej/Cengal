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
__version__ = "3.3.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from asock_io.asock_io_core import *
import httptools



__author__ = 'ButenkoMS <gtalk@butenkoms.space>'


# ======================================================================
# ===================GLOBAL SETTINGS FOR ALL TESTS======================
#

SERVER_KEYWORD = b'http server'
SERVER_ADDRESS = ('localhost', 25000)

BSC__USE_READ_WITH_FIXED_BUFFER = True  # "Optimized for speed". Good for Named Clients.
# BSC__USE_READ_WITH_FIXED_BUFFER = False  # "Optimized for memory". Good for big amount of Unknown Clients (raw,
# http, etc.) if you have small server.

BSC__SOCKET_READ_FIXED_BUFFER_SIZE = 1024 ** 2

BSC__USE_NODELAY_INET = True

BSC__REUSE_GATE_ADDR = True

BSC__REUSE_GATE_PORT = True

LINE_TRACE_ALLOWED = True

#
# ===================GLOBAL SETTINGS FOR ALL TESTS======================
# ======================================================================


class RawClientCheckerAllRaw(CheckIsRawConnection):
    def __call__(self, app_server: ASockIOCore, client_info: Connection):
        return True


def run_http_server_with_inline_processor():
    io_iteration_timeout = 0.5

    # ADD SERVER GATE CONNECTIONS
    set_of_tcp_settings = set()
    tcp_settings = ConnectionSettings(ConnectionType.passive, SERVER_ADDRESS, SERVER_KEYWORD)
    set_of_tcp_settings.add(tcp_settings)

    # CREATE SERVER
    http_server = ASockIOCore(set_of_tcp_settings)

    # SET SERVER SETTINGS
    http_server.raw_checker_for_new_incoming_connections = RawClientCheckerAllRaw()
    http_server.unknown_clients_are_allowed = True
    http_server.should_get_client_addr_info_on_connection = False
    http_server.use_speed_optimized_socket_read = BSC__USE_READ_WITH_FIXED_BUFFER
    http_server.socket_read_fixed_buffer_size.result = BSC__SOCKET_READ_FIXED_BUFFER_SIZE
    http_server.use_nodelay_inet = BSC__USE_NODELAY_INET
    http_server.reuse_gate_addr = BSC__REUSE_GATE_ADDR
    http_server.reuse_gate_port = BSC__REUSE_GATE_PORT
    http_server.class_for_unknown_clients_inline_processing = HttpInlineProcessor  # SETTING UP WORKER CLASS

    # START SERVER
    with asock_io_core_connect(http_server, True, listen_num=1000) as server:
        http_server.need_to_auto_check_incoming_raw_connection = True

        # RUN SERVER LOOP
        while True:
            io_iteration_result = server.io_iteration(io_iteration_timeout)
    
    print('Server had been Shut Down.')


# ==============================================================================================================
#                                       !!!!! IMPORTANT !!!!!
# NEXT CODE SHOULD BE EQUIVALENT TO ASYNCIO HTTP SERVER'S CODE FROM "https://github.com/MagicStack/vmbench" PROJECT
# (BENCHMARKING TOOL FROM 'UVLOOP' DEVELOPERS) FOR FAIR COMPARISON, SO IT'S SO DIRTY.
# (IT'S ALMOST EQUIVALENT: IT DOES NOT HAVE FEW CRITICAL vmbench's BUGS)


_RESP_CACHE = {}


class HttpRequestForInlineProcessor:
    __slots__ = ('_protocol', '_url', '_headers', '_version')

    def __init__(self, protocol, url, headers, version):
        self._protocol = protocol
        self._url = url
        self._headers = headers
        self._version = version


class HttpResponseForInlineProcessor:
    __slots__ = ('_protocol', '_request', '_headers_sent')

    def __init__(self, protocol, request: HttpRequestForInlineProcessor):
        self._protocol = protocol
        self._request = request
        self._headers_sent = False

    def write(self, data):
        self._protocol.output_messages.append(b''.join([
            'HTTP/{} 200 OK\r\n'.format(
                self._request._version).encode('latin-1'),
            b'Content-Type: text/plain\r\n',
            'Content-Length: {}\r\n'.format(len(data)).encode('latin-1'),
            b'\r\n',
            data
        ]))


class HttpInlineProcessor(InlineProcessor):
    __slots__ = ('_current_request', '_current_parser',
                 '_current_url', '_current_headers', '_last_piece_of_data',
                 '_previous_piece_of_data')

    def __init__(self, *args, **kwargs):
        super(HttpInlineProcessor, self).__init__(*args, **kwargs)
        self._current_parser = httptools.HttpRequestParser(self)
        self._current_headers = list()
        self._current_request = None
        self._current_url = None
        self._last_piece_of_data = None
        self._previous_piece_of_data = None

    # ===========================================
    # ==== BEGIN of InlineProcessor methods: ====

    def on__data_received(self, data: bytes):
        self._current_parser.feed_data(data)

    # def on__output_buffers_are_empty(self):
    #     pass

    # def on__connection_lost(self):
    #     pass

    # ==== END of InlineProcessor methods====
    # =======================================

    # =============================================
    # ==== BEGIN of HttpRequestParser methods: ====

    # def on_message_begin(self):
    #     pass

    def on_url(self, url):
        if self._current_url:
            self._current_url += url
        else:
            self._current_url = url

    # def on_status(self, data):
    #     pass

    def on_header(self, name, value):
        self._current_headers.append((name, value))

    def on_headers_complete(self):
        try:
            self._current_request = HttpRequestForInlineProcessor(
                self, self._current_url, self._current_headers,
                self._current_parser.get_http_version())

            self.handle(self._current_request, HttpResponseForInlineProcessor(self, self._current_request))
        except:
            print('ON HEADERS COMPLETE. ID: {}. Last: {}. Previous : {}.'.format(
                self.client_id, self._last_piece_of_data, self._previous_piece_of_data))
            raise

    # def on_body(self, data):
    #     pass

    # def on_message_complete(self):
    #     pass

    # def on_chunk_header(self):
    #     pass

    # def on_chunk_complete(self):
    #     pass

    # ==== END of HttpRequestParser methods====
    # =========================================

    def handle(self, request, response: HttpResponseForInlineProcessor):
        parsed_url = httptools.parse_url(self._current_url)
        payload_size = parsed_url.path.decode('ascii')[1:]
        if not payload_size:
            payload_size = 1024
        else:
            payload_size = int(payload_size)
        resp = _RESP_CACHE.get(payload_size)
        if resp is None:
            resp = b'X' * payload_size
            _RESP_CACHE[payload_size] = resp
        response.write(resp)

        self._current_request = None
        self._current_url = None
        self._current_headers = list()
        if not self._current_parser.should_keep_alive():
            self.mark__socket_as_ready_to_be_closed(True)

# ==============================================================================================================


if __name__ == '__main__':
    run_http_server_with_inline_processor()
