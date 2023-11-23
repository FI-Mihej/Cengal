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


__all__ = ['PortStatus', 'Table', 'Protocol', 'purify_ports', 'get_tables', 'used_ports', 'PortLord', 'PortInfo', 'UsedPorts', 'PortsIterator', 'unify_ports', 'UnaceptablePortsRangeTypeError']

import pickle
from enum import Enum
from typing import Dict, Optional, Set, List, Tuple, Union, Any
from collections import namedtuple
from cengal.file_system.path_manager import path_relative_to_src


class PortStatus(str, Enum):
    na = 'N/A'                 # In programming APIs (not in communication between hosts), requests a system-allocated (dynamic) port
    yes = 'Yes'                # Described protocol is assigned for this port by IANA and is standardized, specified, or widely used for such.
    unofficial = 'Unofficial'  # Described protocol is not assigned for this port by IANA but is standardized, specified, or widely used for such.
    assigned = 'Assigned'      # Described protocol is assigned by IANA for this port, but is not standardized, specified, or widely used for such.
    no = 'No'                  # Described protocol is not assigned by IANA, standardized, specified, or widely used for the port.
    reserved = 'Reserved'      # Port is reserved by IANA, generally to prevent collision having its previous use removed. The port number may be available for assignment upon request to IANA.


class Table(str, Enum):
    system = 'system'
    user = 'user'
    ephemeral = 'ephemeral'
    

class Protocol(Enum):
    tcp = 0
    udp = 1
    sctp = 2
    dccp = 3


_tables: Dict[Table, List[List]] = None
_known_tables_names = {'system', 'user', 'ephemeral'}
_used_ports = None


def _purify_item(item: Optional[str]) -> PortStatus:
    if item is None:
        return PortStatus.no
    
    return PortStatus(item)


def get_tables() -> Dict[Table, List[List]]:
    global _tables
    if _tables is None:
        tables: Dict[Table, List[List]] = dict()
        for table_name in _known_tables_names:
            with open(path_relative_to_src(f'data/table_{table_name}.pickle'), 'rb') as file:
                tables[Table(table_name)] = pickle.load(file)

        _tables = tables
    
    return _tables


def used_ports() -> 'UsedPorts':
    global _used_ports
    if _used_ports is None:
        _used_ports = UsedPorts()
    
    return _used_ports


PortLord = namedtuple('PortLord', 'tcp udp sctp dccp description')


class PortInfo:
    def __init__(self, port: int, port_lords: Optional[Set[PortLord]] = None) -> None:
        self.port: int = port
        self.port_lords = port_lords or set()
    
    def add(self, port_lord: PortLord) -> int:
        self.port_lords.add(port_lord)
        return len(self.port_lords)


class UsedPorts:
    def __init__(self) -> None:
        self.table: List[PortInfo] = list([PortInfo(i) for i in range(65536)])
        self.tables = {
            Table.system: slice(0, 1024),
            Table.user: slice(1024, 49152),
            Table.ephemeral: slice(49152, 65536),
        }
        raw_tables: Dict[Table, List[List]] = get_tables()
        for table_name, raw_table in raw_tables.items():
            for row in raw_table:
                port_or_range, tcp, udp, sctp, dccp, description = row
                port_lord = PortLord(_purify_item(tcp), _purify_item(udp), _purify_item(sctp), _purify_item(dccp), description)
                if isinstance(port_or_range, tuple):
                    for port in range(int(port_or_range[0]), int(port_or_range[1]) + 1):
                        self.table[port].add(port_lord)
                else:
                    self.table[int(port_or_range)].add(port_lord)
        
        not_used_port = PortLord(PortStatus.no, PortStatus.no, PortStatus.no, PortStatus.no, str())
        for port_info in self.table:
            if not port_info.port_lords:
                port_info.port_lords.add(not_used_port)
    
    def port(self, protocol: Protocol, ports_range: slice, statuses: Union[PortStatus, Set[PortStatus]]) -> 'PortsIterator':
        return PortsIterator(self, protocol, ports_range, statuses, 1)
    
    def range(self, protocol: Protocol, ports_range: slice, statuses: Union[PortStatus, Set[PortStatus]], desired_number_of_ports: int) -> 'PortsIterator':
        return PortsIterator(self, protocol, ports_range, statuses, desired_number_of_ports)
    
    def __call__(self, protocol: Protocol, ports_range: slice, statuses: Union[PortStatus, Set[PortStatus]], desired_number_of_ports: int) -> 'PortsIterator':
        return self.range(protocol, ports_range, statuses, desired_number_of_ports)


class UnaceptablePortsRangeTypeError(Exception):
    pass


class PortsIterator:
    def __init__(self, used_ports: UsedPorts, protocol: Protocol, ports_range: Union[slice, Tuple[int, int]], statuses: Union[PortStatus, Set[PortStatus]], desired_number_of_ports: int) -> None:
        self.used_ports: UsedPorts = used_ports
        self.protocol: Protocol = protocol
        self.ports_range: slice = ports_range
        if isinstance(ports_range, slice):
            pass
        elif isinstance(ports_range, tuple):
            self.ports_range = slice(*ports_range)
        else:
            raise UnaceptablePortsRangeTypeError
        
        if isinstance(statuses, PortStatus):
            statuses = {statuses}
        
        self.statuses: Union[PortStatus, Set[PortStatus]] = statuses
        self.desired_number_of_ports: int = desired_number_of_ports
        self.first_port = self.ports_range.start

    def __iter__(self):
        self.first_port = self.ports_range.start
        return self

    def __next__(self):
        ports_range = self._iter_impl()
        self.first_port += 1
        return ports_range
    
    def _iter_impl(self) -> slice:
        if self.first_port >= self.ports_range.stop:
            raise StopIteration
        
        while self.first_port < self.ports_range.stop:
            result_range_stop = self.first_port + 1
            for offset in range(self.desired_number_of_ports):
                port = self.first_port + offset
                
                port_info: PortInfo = self.used_ports.table[port]
                port_statuses: Set[PortStatus] = set()
                for port_lord in port_info.port_lords:
                    port_statuses.add(port_lord[self.protocol.value])
                
                if 0 == len(port_statuses - self.statuses):
                    is_good = True
                else:
                    is_good = False
                
                if is_good:
                    result_range_stop = port + 1
                else:
                    result_range_stop = None
                    self.first_port = port + 1
                    break
            
            if result_range_stop is not None:
                return slice(self.first_port, result_range_stop)
        
        raise StopIteration
    
    def __call__(self) -> Optional[slice]:
        try:
            return self._iter_impl()
        except StopIteration:
            return None

    def shift_only(self, num: int = 1) -> None:
        self.first_port += num

    def shift(self, num: int = 1) -> Optional[slice]:
        self.first_port += num
        return self()

    def put_only(self, num: int) -> None:
        self.first_port = num

    def put(self, num: int) -> Optional[slice]:
        self.first_port = num
        return self()


def purify_ports(ports_range: Optional[slice]) -> Optional[Union[int, Tuple[int, int]]]:
    start = ports_range.start
    stop = ports_range.stop - 1
    if start == stop:
        return start
    else:
        return start, stop


def unify_ports(ports_range: Optional[slice]) -> Optional[Tuple[int, int]]:
    start = ports_range.start
    stop = ports_range.stop - 1
    return start, stop
    
