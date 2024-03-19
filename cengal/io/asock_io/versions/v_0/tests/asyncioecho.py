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
__version__ = "4.2.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import argparse
import asyncio
import gc
import os.path
from socket import *
try:
    import uvloop
except ImportError:
    print('CAN\'T IMPORT "{}" MODULE'.format('uvloop'))


PRINT = 0


async def echo_server(loop, address, unix):
    if unix:
        sock = socket(AF_UNIX, SOCK_STREAM)
    else:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    sock.setblocking(False)
    if PRINT:
        print('Server listening at', address)
    with sock:
        while True:
             client, addr = await loop.sock_accept(sock)
             if PRINT:
                print('Connection from', addr)
             loop.create_task(echo_client(loop, client))


async def echo_client(loop, client):
    try:
        sock.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
    except (OSError, NameError):
        pass

    with client:
        while True:
            data = await loop.sock_recv(client, 102400)
            if not data:
                break
            await loop.sock_sendall(client, data)
    if PRINT:
        print('Connection closed')


async def echo_client_streams(reader, writer):
    sock = writer.get_extra_info('socket')
    try:
        sock.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
    except (OSError, NameError):
        pass
    if PRINT:
        print('Connection from', sock.getpeername())
    while True:
         data = await reader.readline()
         if not data:
             break
         writer.write(data)
    if PRINT:
        print('Connection closed')
    writer.close()


class EchoProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        sock = transport.get_extra_info('socket')
        try:
            sock.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
        except (OSError, NameError):
            pass

    def connection_lost(self, exc):
        self.transport = None

    def data_received(self, data):
        self.transport.write(data)


async def print_debug(loop):
    while True:
        print(chr(27) + "[2J")  # clear screen
        loop.print_debug_info()
        await asyncio.sleep(0.5, loop=loop)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--uvloop', default=False, action='store_true')
    parser.add_argument('--streams', default=False, action='store_true')
    parser.add_argument('--proto', default=False, action='store_true')
    parser.add_argument('--addr', default='127.0.0.1:18495', type=str)
    parser.add_argument('--print', default=False, action='store_true')
    args = parser.parse_args()

    if args.uvloop:
        loop = uvloop.new_event_loop()
        print('using UVLoop')
    else:
        loop = asyncio.new_event_loop()
        print('using asyncio loop')

    asyncio.set_event_loop(loop)
    loop.set_debug(False)

    if args.print:
        PRINT = 1

    if hasattr(loop, 'print_debug_info'):
        loop.create_task(print_debug(loop))
        PRINT = 0

    unix = False
    if args.addr.startswith('file:'):
        unix = True
        addr = args.addr[5:]
        if os.path.exists(addr):
            os.remove(addr)
    else:
        addr = args.addr.split(':')
        addr[1] = int(addr[1])
        addr = tuple(addr)

    print('serving on: {}'.format(addr))

    if args.streams:
        if args.proto:
            print('cannot use --stream and --proto simultaneously')
            exit(1)

        print('using asyncio/streams')
        if unix:
            coro = asyncio.start_unix_server(echo_client_streams,
                                             addr, loop=loop,
                                             limit=1024 * 1024)
        else:
            coro = asyncio.start_server(echo_client_streams,
                                        *addr, loop=loop,
                                        limit=1024 * 1024)
        srv = loop.run_until_complete(coro)
    elif args.proto:
        if args.streams:
            print('cannot use --stream and --proto simultaneously')
            exit(1)

        print('using simple protocol')
        if unix:
            coro = loop.create_unix_server(EchoProtocol, addr)
        else:
            coro = loop.create_server(EchoProtocol, *addr)
        srv = loop.run_until_complete(coro)
    else:
        print('using sock_recv/sock_sendall')
        loop.create_task(echo_server(loop, addr, unix))
    try:
        loop.run_forever()
    finally:
        if hasattr(loop, 'print_debug_info'):
            gc.collect()
            print(chr(27) + "[2J")
            loop.print_debug_info()

        loop.close()
