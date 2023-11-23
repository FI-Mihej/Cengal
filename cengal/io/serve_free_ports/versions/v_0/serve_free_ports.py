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


__all__ = ['find_free_tcp_port', 'simple_port_search', 'asimple_port_search']


# from cengal.parallel_execution.asyncio.efficient_streams import *
import asyncio
from cengal.io.used_ports import used_ports, PortsIterator, Protocol, PortStatus, UsedPorts, purify_ports, unify_ports
from typing import Optional, Union, Tuple, Set
from gc import collect


def client_connected_cb(*args, **kwargs):
    pass


async def find_free_tcp_port(host, ports_iterartor: PortsIterator, timeout: int = 0) -> Optional[int]:
    for ports_range in ports_iterartor:
        start, stop = unify_ports(ports_range)
        for port in range(start, stop + 1):
            try:
                if timeout:
                    server = await asyncio.wait_for(asyncio.start_server(client_connected_cb, host, port), timeout)
                else:
                    server = await asyncio.start_server(client_connected_cb, host, port)
                
                try:
                    server.close()
                except Exception:
                    pass
                finally:
                    del server
                    collect()

                return port
            except TimeoutError as err:
                pass
            except (ConnectionRefusedError, ConnectionError, OSError) as err:
                pass


def simple_port_search(host: str, port_or_range: Union[int, slice, Tuple[int, int]], protocol: Protocol = Protocol.tcp, statuses: Optional[Union[PortStatus, Set[PortStatus]]] = None, desired_number_of_ports: int = 1, timeout: int = 0, used_ports: Optional[UsedPorts] = None):
    """_summary_

    Args:
        host (str): _description_
        port_or_range (Union[int, slice, Tuple[int, int]]): _description_
        protocol (Protocol, optional): _description_. Defaults to Protocol.tcp.
        statuses (Optional[Union[PortStatus, Set[PortStatus]]], optional): _description_. Defaults to None.
        desired_number_of_ports (int, optional): _description_. Defaults to 1.
        timeout (int, optional): _description_. Defaults to 0.
        used_ports (Optional[UsedPorts], optional): !!! UsedPorts() constructions is a long running task so it would be better to create and provide your own instance of UsedPorts once, if you need to call simple_port_search() periodically.

    Returns:
        _type_: _description_
    """    
    if statuses is None: statuses = {PortStatus.na, PortStatus.no}
    if used_ports is None: used_ports = UsedPorts()
    return asyncio.run(find_free_tcp_port(host, PortsIterator(used_ports, protocol, port_or_range, statuses, desired_number_of_ports), timeout))


async def asimple_port_search(host: str, port_or_range: Union[int, slice, Tuple[int, int]], protocol: Protocol = Protocol.tcp, statuses: Optional[Union[PortStatus, Set[PortStatus]]] = None, desired_number_of_ports: int = 1, timeout: int = 0, used_ports: Optional[UsedPorts] = None):
    """_summary_

    Args:
        host (str): _description_
        port_or_range (Union[int, slice, Tuple[int, int]]): _description_
        protocol (Protocol, optional): _description_. Defaults to Protocol.tcp.
        statuses (Optional[Union[PortStatus, Set[PortStatus]]], optional): _description_. Defaults to None.
        desired_number_of_ports (int, optional): _description_. Defaults to 1.
        timeout (int, optional): _description_. Defaults to 0.
        used_ports (Optional[UsedPorts], optional): !!! UsedPorts() constructions is a long running task so it would be better to create and provide your own instance of UsedPorts once, if you need to call asimple_port_search() periodically.

    Returns:
        _type_: _description_
    """    
    if statuses is None: statuses = {PortStatus.na, PortStatus.no}
    if used_ports is None: used_ports = UsedPorts()
    return await find_free_tcp_port(host, PortsIterator(used_ports, protocol, port_or_range, statuses, desired_number_of_ports), timeout)
