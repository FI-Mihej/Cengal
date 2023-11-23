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


from cengal.io.used_ports import *
port = purify_ports(used_ports().port(Protocol.tcp, used_ports().tables[Table.user], {PortStatus.no})())
print(f'port: {port}')
ports_iter = used_ports()(Protocol.tcp, used_ports().tables[Table.user], {PortStatus.no, PortStatus.reserved}, 6)
start, stop = purify_ports(ports_iter())
print(f'first port: {start}, last port: {stop}')
start, stop = purify_ports(ports_iter.shift(100))
print(f'first port: {start}, last port: {stop}')
start, stop = purify_ports(ports_iter.shift(35))
print(f'first port: {start}, last port: {stop}')

print('System ports:')
index = 10
for ports_range in used_ports().port(Protocol.tcp, used_ports().tables[Table.system], {PortStatus.no}):
    port = purify_ports(ports_range)
    print(f'\tfree port: {port}')
    index -= 1
    if index <= 0:
        break

print('User ports ranges:')
index = 10
for ports_range in used_ports()(Protocol.tcp, used_ports().tables[Table.user], {PortStatus.no, PortStatus.reserved}, 50):
    start, stop = purify_ports(ports_range)
    print(f'\tfirst port: {start}, last port: {stop}')
    index -= 1
    if index <= 0:
        break

print('Not overlapping User ports ranges:')
index = 10
ports_iter = used_ports()(Protocol.tcp, used_ports().tables[Table.user], {PortStatus.no, PortStatus.reserved}, 50)
for ports_range in ports_iter:
    start, stop = purify_ports(ports_range)
    print(f'\tfirst port: {start}, last port: {stop}')
    ports_iter.put_only(stop + 1)
    index -= 1
    if index <= 0:
        break

print('Not overlapping User ports ranges:')
index = 10
ports_iter = used_ports()(Protocol.tcp, used_ports().tables[Table.ephemeral], {PortStatus.no, PortStatus.reserved, PortStatus.unofficial}, 50)
for ports_range in ports_iter:
    start, stop = purify_ports(ports_range)
    print(f'\tfirst port: {start}, last port: {stop}')
    ports_iter.put_only(stop + 1)
    index -= 1
    if index <= 0:
        break
