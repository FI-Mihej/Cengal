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


import inspect
from pprint import pprint
from cengal.introspection.inspect import current_entity_name, print_intro_func_repr, current_entity_owner_name, \
    entity_owning_module_info_and_owning_path, frame as frame_func, entity_class, entity_owner, entity_properties, \
        pdi, class_properties, class_properties_including_overrided


class A:
    def __init__(self):
        self.a = 1

    def get_a(self):
        return self.a


class B(A):
    def __init__(self):
        super().__init__()
        self.b = 2

    def get_b(self):
        return self.b


class C(B):
    def __init__(self):
        super().__init__()
        self.c = 3

    def get_b(self):
        return super().get_b()

    def get_c(self):
        return self.c
    

pprint(dir(A))
pprint(dir(B))
pprint(dir(C))
    

pprint(entity_properties(A))
pprint(entity_properties(B))
pprint(entity_properties(C))
    

pprint(A.__dict__.keys())
pprint(B.__dict__.keys())
pprint(C.__dict__.keys())
    

pprint(class_properties(A))
pprint(class_properties(B))
pprint(class_properties(C))
    

pprint(class_properties_including_overrided(A))
pprint(class_properties_including_overrided(B))
pprint(class_properties_including_overrided(C))
