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
__version__ = "3.1.10"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import asyncio
import logging
from io.used_ports import used_ports

server: asyncio.AbstractServer = None

sw = asyncio.StreamWriter
sr = asyncio.StreamReader


async def client_connected(reader, writer):
    # Communicate with the client with
    # reader/writer streams.  For example:
    await reader.readline()


async def main(host, port):
    global server
    print('Main started...')
    try:
        server = await asyncio.start_server(
            client_connected, host, port)
    except OSError:
        logging.exception('')
        return
        
    print(server.sockets)
    ports = set()
    for serv_sock in server.sockets:
        host, port = serv_sock.getsockname()
        ports.add(port)
    
    print(f'Listening ports: {ports}')
    await server.serve_forever()


# asyncio.run(main('127.0.0.1', 0))
asyncio.run(main('127.0.0.1', 27060))
