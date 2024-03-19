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


__all__ = ['find_free_port', 'simple_port_search', 'asimple_port_search', 'find_free_ports_range', 'simple_ports_range_search', 'asimple_ports_range_search']


import asyncio
from cengal.io.used_ports import used_ports, PortsIterator, Protocol, PortStatus, UsedPorts
from cengal.math.numbers import RationalNumber
from typing import Optional, Union, Tuple, Set
from gc import collect


def client_connected_cb(*args, **kwargs):
    pass


async def find_free_port(host, ports_iterartor: PortsIterator, timeout: RationalNumber = 0) -> Optional[int]:
    """_summary_
    Example:

    from cengal.io.serve_free_ports import find_free_port
    from cengal.io.used_ports import PortsIterator, used_ports, Protocol, PortStatus, unify_ports, purify_ports
    import asyncio

    async def main():
        ports_rages_iterator: PortsIterator = used_ports().range(Protocol.tcp, slice(18000, 18100), {PortStatus.na, PortStatus.no})
        port: int = await find_free_port('0.0.0.0', ports_rages_iterator, 5.0)
        if port is not None:
            print(port)  # Output: 18000

    Args:
        host (_type_): _description_
        ports_iterartor (PortsIterator): _description_
        timeout (RationalNumber, optional): _description_. Defaults to 0.

    Returns:
        Optional[int]: _description_
    """    
    for ports_range in ports_iterartor:
        for port in range(ports_range.start, ports_range.stop):
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


def simple_port_search(host: str, port_or_range: Union[int, slice, Tuple[int, int]], protocol: Protocol = Protocol.tcp, statuses: Optional[Union[PortStatus, Set[PortStatus]]] = None, timeout: RationalNumber = 0, used_ports_instance: Optional[UsedPorts] = None) -> Optional[int]:
    """_summary_

    Example:

    from cengal.io.serve_free_ports import simple_port_search
    from cengal.io.used_ports import PortsIterator, used_ports, Protocol, PortStatus, unify_ports, purify_ports

    def main():
        port: int = simple_port_search('0.0.0.0', slice(18000, 18100), Protocol.tcp, {PortStatus.na, PortStatus.no}, 5.0)
        if port is not None:
            print(port)  # Output: 18000

    Args:
        host (str): _description_
        port_or_range (Union[int, slice, Tuple[int, int]]): _description_
        protocol (Protocol, optional): _description_. Defaults to Protocol.tcp.
        statuses (Optional[Union[PortStatus, Set[PortStatus]]], optional): _description_. Defaults to None.
        desired_number_of_ports (int, optional): _description_. Defaults to 1.
        timeout (int, optional): _description_. Defaults to 0.
        used_ports_instance (Optional[UsedPorts], optional): .

    Returns:
        _type_: _description_
    """    
    if statuses is None: statuses = {PortStatus.na, PortStatus.no}
    if used_ports_instance is None: used_ports_instance = used_ports()
    return asyncio.run(find_free_port(host, used_ports_instance.port(protocol, port_or_range, statuses), timeout))


async def asimple_port_search(host: str, port_or_range: Union[int, slice, Tuple[int, int]], protocol: Protocol = Protocol.tcp, statuses: Optional[Union[PortStatus, Set[PortStatus]]] = None, timeout: RationalNumber = 0, used_ports_instance: Optional[UsedPorts] = None) -> Optional[int]:
    """_summary_

    Example:

    from cengal.io.serve_free_ports import asimple_port_search
    from cengal.io.used_ports import PortsIterator, used_ports, Protocol, PortStatus, unify_ports, purify_ports
    import asyncio

    async def main():
        port: int = await asimple_port_search('0.0.0.0', slice(18000, 18100), Protocol.tcp, {PortStatus.na, PortStatus.no}, 5.0)
        if port is not None:
            print(port)  # Output: 18000

    Args:
        host (str): _description_
        port_or_range (Union[int, slice, Tuple[int, int]]): _description_
        protocol (Protocol, optional): _description_. Defaults to Protocol.tcp.
        statuses (Optional[Union[PortStatus, Set[PortStatus]]], optional): _description_. Defaults to None.
        desired_number_of_ports (int, optional): _description_. Defaults to 1.
        timeout (int, optional): _description_. Defaults to 0.
        used_ports_instance (Optional[UsedPorts], optional): .

    Returns:
        _type_: _description_
    """    
    if statuses is None: statuses = {PortStatus.na, PortStatus.no}
    if used_ports_instance is None: used_ports_instance = used_ports()
    return await find_free_port(host, used_ports_instance.port(protocol, port_or_range, statuses), timeout)


async def find_free_ports_range(host, ports_iterartor: PortsIterator, timeout: RationalNumber = 0) -> Optional[slice]:
    """
    Example:

    from cengal.io.serve_free_ports import find_free_ports_range
    from cengal.io.used_ports import PortsIterator, used_ports, Protocol, PortStatus, unify_ports, purify_ports
    import asyncio

    async def main():
        ports_rages_iterator: PortsIterator = used_ports().range(Protocol.tcp, slice(18000, 18100), {PortStatus.na, PortStatus.no}, 3)
        ports_range = await find_free_ports_range('0.0.0.0', ports_rages_iterator, 5.0)
        if ports_range is not None:
            first_port = ports_range.start  # Output: 18000
            last_port = ports_range.stop - 1  # Output: 18002
            first_port, last_port = unify_ports(ports_range)  # Output: (18000, 18002)
            for port in range(ports_range.start, ports_range.stop):
                print(port)
            
            print(list(range(ports_range.start, ports_range.stop)))  # Output: [18000, 18001, 18002]
            if isinstance(purify_ports(ports_range), slice):
                # type is `slice`
                print('Ports range')
            else:
                # type is `int`
                print('Single port')

    Args:
        host (_type_): _description_
        ports_iterartor (PortsIterator): _description_
        timeout (int, optional): _description_. Defaults to 0.

    Returns:
        Optional[slice]: _description_
    """
    for ports_range in ports_iterartor:
        try:
            for port in range(ports_range.start, ports_range.stop):
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

            return ports_range
        except TimeoutError as err:
            pass
        except (ConnectionRefusedError, ConnectionError, OSError) as err:
            pass


def simple_ports_range_search(host: str, port_or_range: Union[int, slice, Tuple[int, int]], protocol: Protocol = Protocol.tcp, statuses: Optional[Union[PortStatus, Set[PortStatus]]] = None, desired_number_of_ports: int = 1, timeout: RationalNumber = 0, used_ports_instance: Optional[UsedPorts] = None) -> Optional[slice]:
    """_summary_

    Example:

    from cengal.io.serve_free_ports import simple_ports_range_search
    from cengal.io.used_ports import PortsIterator, used_ports, Protocol, PortStatus, unify_ports, purify_ports

    def main():
        ports_range = simple_ports_range_search('0.0.0.0', slice(18000, 18100), Protocol.tcp, {PortStatus.na, PortStatus.no}, 3, 5.0)
        if ports_range is not None:
            first_port = ports_range.start  # Output: 18000
            last_port = ports_range.stop - 1  # Output: 18002
            first_port, last_port = unify_ports(ports_range)  # Output: (18000, 18002)
            for port in range(ports_range.start, ports_range.stop):
                print(port)
            
            print(list(range(ports_range.start, ports_range.stop)))  # Output: [18000, 18001, 18002]
            if isinstance(purify_ports(ports_range), slice):
                # type is `slice`
                print('Ports range')
            else:
                # type is `int`
                print('Single port')

    Args:
        host (str): _description_
        port_or_range (Union[int, slice, Tuple[int, int]]): _description_
        protocol (Protocol, optional): _description_. Defaults to Protocol.tcp.
        statuses (Optional[Union[PortStatus, Set[PortStatus]]], optional): _description_. Defaults to None.
        desired_number_of_ports (int, optional): _description_. Defaults to 1.
        timeout (int, optional): _description_. Defaults to 0.
        used_ports_instance (Optional[UsedPorts], optional): .

    Returns:
        _type_: _description_
    """    
    if statuses is None: statuses = {PortStatus.na, PortStatus.no}
    if used_ports_instance is None: used_ports_instance = used_ports()
    return asyncio.run(find_free_ports_range(host, used_ports_instance.range(protocol, port_or_range, statuses, desired_number_of_ports), timeout))


async def asimple_ports_range_search(host: str, port_or_range: Union[int, slice, Tuple[int, int]], protocol: Protocol = Protocol.tcp, statuses: Optional[Union[PortStatus, Set[PortStatus]]] = None, desired_number_of_ports: int = 1, timeout: RationalNumber = 0, used_ports_instance: Optional[UsedPorts] = None) -> Optional[slice]:
    """_summary_

    Example:

    from cengal.io.serve_free_ports import asimple_ports_range_search
    from cengal.io.used_ports import PortsIterator, used_ports, Protocol, PortStatus, unify_ports, purify_ports
    import asyncio

    async def main():
        ports_range = await asimple_ports_range_search('0.0.0.0', slice(18000, 18100), Protocol.tcp, {PortStatus.na, PortStatus.no}, 3, 5.0)
        if ports_range is not None:
            first_port = ports_range.start  # Output: 18000
            last_port = ports_range.stop - 1  # Output: 18002
            first_port, last_port = unify_ports(ports_range)  # Output: (18000, 18002)
            for port in range(ports_range.start, ports_range.stop):
                print(port)
            
            print(list(range(ports_range.start, ports_range.stop)))  # Output: [18000, 18001, 18002]
            if isinstance(purify_ports(ports_range), slice):
                # type is `slice`
                print('Ports range')
            else:
                # type is `int`
                print('Single port')

    Args:
        host (str): _description_
        port_or_range (Union[int, slice, Tuple[int, int]]): _description_
        protocol (Protocol, optional): _description_. Defaults to Protocol.tcp.
        statuses (Optional[Union[PortStatus, Set[PortStatus]]], optional): _description_. Defaults to None.
        desired_number_of_ports (int, optional): _description_. Defaults to 1.
        timeout (int, optional): _description_. Defaults to 0.
        used_ports_instance (Optional[UsedPorts], optional): .

    Returns:
        _type_: _description_
    """    
    if statuses is None: statuses = {PortStatus.na, PortStatus.no}
    if used_ports_instance is None: used_ports_instance = used_ports()
    return await find_free_ports_range(host, used_ports_instance.range(protocol, port_or_range, statuses, desired_number_of_ports), timeout)
