#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2022 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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
__copyright__ = "Copyright © 2012-2022 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "0.0.8"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


# from cengal.parallel_execution.asyncio.efficient_streams import *
import asyncio
from cengal.io.used_ports import used_ports, PortsIterator, purify_ports, unify_ports
from typing import Optional


async def find_free_tcp_port(host, ports_iterartor: PortsIterator, timeout: int = 0) -> Optional[int]:
    for ports_range in ports_iterartor:
        start, stop = unify_ports(ports_range)
        for port in range(start, stop + 1):
            try:
                if timeout:
                    reader, writer = await asyncio.wait_for(asyncio.open_connection(host, port), timeout)
                else:
                    reader, writer = await asyncio.open_connection(host, port)
                
                writer.close()
                try:
                    await writer.wait_closed()
                except AttributeError:
                    pass
                
                return port
            except TimeoutError as err:
                pass
            except (ConnectionRefusedError, ConnectionError, OSError) as err:
                pass
