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
__version__ = "3.1.17"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


import marshal
from cengal.introspection.inspect import entity_owner, entity_owning_module_info_and_owning_path
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro
from marshal import dumps

owner = entity_owning_module_info_and_owning_path(PutCoro)
print('PutCoro\'s owner', owner)
p = getattr(owner[0], 'PutCoro')
pp = p(None)
print(repr(pp))
pps = pp.single_task_registration_or_immediate_processing_single
pps_owner = entity_owning_module_info_and_owning_path(pps)
print('pps_owner:', pps_owner)

d = getattr(marshal, 'dumps')
class MyClass:
    pass

owner = entity_owning_module_info_and_owning_path(MyClass)
print('MyClass\' owner', owner)

l = [1, 2, 'hello']
m = d(l)
print(m)
l = [1, MyClass()]
m = marshal.dumps(l)

