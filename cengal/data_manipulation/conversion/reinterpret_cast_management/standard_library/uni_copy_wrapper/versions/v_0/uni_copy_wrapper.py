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

from cengal.data_manipulation.conversion.reinterpret_cast_management.manager import BaseAutoDerivedObjWrapper
from cengal.entities.copyable import copy__impl, deepcopy__impl
from typing import Dict, Type, Callable, Any, Tuple, FrozenSet, Set
from copy import Error as CopyError, copy, deepcopy

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


class UniCopyWrapper(BaseAutoDerivedObjWrapper):
    def __init__(self):
        super().__init__()
        self._copy_wrapping_required_per_type: Dict[Type, bool] = dict()
        self._deepcopy_wrapping_required_per_type: Dict[Type, bool] = dict()
        self._methods_per_type: Dict[Type, Dict[str, Callable]] = dict()
    
    def wrapping_required(self, obj: Any, base_type: Type, fields: Tuple[str], planned_type_name: str) -> bool:
        copy_required: bool = None
        try:
            copy_required = self._copy_wrapping_required_per_type[base_type]
        except KeyError:
            pass
        
        if copy_required is None:
            try:
                copy(obj)
                copy_required = False
            except CopyError:
                copy_required = True
            
            self._copy_wrapping_required_per_type[base_type] = copy_required
        
        deepcopy_required: bool = None
        try:
            deepcopy_required = self._deepcopy_wrapping_required_per_type[base_type]
        except KeyError:
            pass
        
        if deepcopy_required is None:
            try:
                deepcopy(obj)
                deepcopy_required = False
            except CopyError:
                deepcopy_required = True
            
            self._deepcopy_wrapping_required_per_type[base_type] = deepcopy_required
        
        return copy_required or deepcopy_required
    
    def methods(self, obj: Any, base_type: Type, fields: Tuple[str]) -> Dict[str, Callable]:
        try:
            return self._methods_per_type[base_type]
        except KeyError:
            pass
        
        if self._copy_wrapping_required_per_type[base_type]:
            methods = {
                '__copy__': copy__impl,
            }
        else:
            methods = {}
        
        if self._deepcopy_wrapping_required_per_type[base_type]:
            methods['__deepcopy__'] = deepcopy__impl

        self._methods_per_type[base_type] = methods
        return methods
