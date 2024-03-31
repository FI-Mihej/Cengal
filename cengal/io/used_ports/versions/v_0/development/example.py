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
__version__ = "4.3.0"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.io.used_ports import used_ports, Protocol, PortStatus, unify_ports

''' Output:
slice(18000, 18003, None)
(18000, 18002)
18000
18001
18002
'''

ports = used_ports().range(Protocol.tcp, 18000, {PortStatus.na, PortStatus.no}, 3)()
if ports is not None:
    print(ports)
    print(unify_ports(ports))
    for port in range(ports.start, ports.stop):
        print(port)

ports = used_ports().range(Protocol.tcp, slice(18000, 18100), {PortStatus.na, PortStatus.no}, 3)()
if ports is not None:
    print(ports)
    print(unify_ports(ports))
    for port in range(ports.start, ports.stop):
        print(port)

ports = used_ports().range(Protocol.tcp, slice(18000, 18001), {PortStatus.na, PortStatus.no}, 3)()
if ports is not None:
    print(ports)
    print(unify_ports(ports))
    for port in range(ports.start, ports.stop):
        print(port)

ports = used_ports().range(Protocol.tcp, (18000, 18001), {PortStatus.na, PortStatus.no}, 3)()
if ports is not None:
    print(ports)
    print(unify_ports(ports))
    for port in range(ports.start, ports.stop):
        print(port)
