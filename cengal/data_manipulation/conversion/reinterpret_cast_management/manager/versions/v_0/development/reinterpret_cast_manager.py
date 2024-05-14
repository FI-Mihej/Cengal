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
__version__ = "4.4.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.data_generation.id_generator import IDGenerator
from cengal.data_manipulation.conversion.reinterpret_cast import TemporaryReinterpretCast
from cengal.entities.copyable import copy__impl, deepcopy__impl
from typing import Dict, Type, Callable, Any, Tuple, FrozenSet, Set
from copy import Error as CopyError, copy, deepcopy
from socket import SocketIO


class AutoDerivedClass:
    instance_id = IDGenerator()

    def __init__(self):
        self._instance_id: int = self.instance_id()
        self.class_name = type(self).__name__
        self.derived: Dict[Type, Type] = dict()
    
    @property
    def methods(self) -> Dict[str, Callable]:
        raise NotImplementedError
    
    def base_classes(self, base_type) -> Tuple[Type]:
        return (base_type,)
    
    def __call__(self, base_type: Type):
        base_type_name = base_type.__name__
        try:
            return self.derived[base_type_name]
        except KeyError:
            result: Type = type(f'{self.class_name}__{self._instance_id}__from__{base_type_name}', self.base_classes(base_type), self.methods)
            self.derived[base_type_name] = result
            return result


class BaseAutoDerivedObjWrapper:
    instance_id = IDGenerator()

    def __init__(self):
        self._instance_id: int = self.instance_id()
        self.class_name = type(self).__name__
        self.derived: Dict[Type, Type] = dict()
        self.t = self.type
    
    def wrapping_required(self, obj: Any, base_type: Type, fields: Tuple[str]):
        return True
    
    def methods(self, obj: Any, base_type: Type, fields: Tuple[str]) -> Dict[str, Callable]:
        raise NotImplementedError

    def base_classes(self, obj: Any, base_type: Type, fields: Tuple[str]) -> Tuple[Type]:
        return (base_type,)
    
    def gen_fields_tuple(self, obj: Any):
        try:
            return obj.__slots__
        except AttributeError:
            pass

        return tuple(obj.__dict__.keys())
    
    def type(self, obj: Any):
        base_type = type(obj)
        base_type_name = base_type.__name__
        try:
            return self.derived[base_type_name]
        except KeyError:
            fields: Tuple = self.gen_fields_tuple(obj)
            if self.wrapping_required(obj, base_type, fields):
                result: Type = type(f'{self.class_name}__{self._instance_id}__from__{base_type_name}', self.base_classes(obj, base_type, fields), self.methods(obj, base_type, fields))
                self.derived[base_type_name] = result
                return result
            else:
                return base_type
    
    def __call__(self, obj: Any):
        obj.__class__ = self.type(obj)
        return obj

    def temp(self, obj: Any):
        return TemporaryReinterpretCast(self.type(obj), obj)


class CopyWrapper(BaseAutoDerivedObjWrapper):
    def __init__(self):
        super().__init__()
        self._wrapping_required_per_type: Dict[Type, bool] = dict()
        self._methods_per_type: Dict[Type, Dict[str, Callable]] = dict()
    
    def wrapping_required(self, obj: Any, base_type: Type, fields: Tuple[str]):
        try:
            return self._wrapping_required_per_type[base_type]
        except KeyError:
            pass

        required: bool = False
        try:
            copy(obj)
        except CopyError:
            required = True
        
        self._wrapping_required_per_type[base_type] = required
        return required
    
    def methods(self, obj: Any, base_type: Type, fields: Tuple[str]) -> Dict[str, Callable]:
        try:
            return self._methods_per_type[base_type]
        except KeyError:
            pass
        
        methods = {
            '__copy__': copy__impl,
        }
        self._methods_per_type[base_type] = methods
        return methods


class DeepCopyWrapper(BaseAutoDerivedObjWrapper):
    def __init__(self):
        super().__init__()
        self._wrapping_required_per_type: Dict[Type, bool] = dict()
        self._methods_per_type: Dict[Type, Dict[str, Callable]] = dict()
    
    def wrapping_required(self, obj: Any, base_type: Type, fields: Tuple[str]):
        try:
            return self._wrapping_required_per_type[base_type]
        except KeyError:
            pass

        required: bool = False
        try:
            deepcopy(obj)
        except CopyError:
            required = True
        
        self._wrapping_required_per_type[base_type] = required
        return required
    
    def methods(self, obj: Any, base_type: Type, fields: Tuple[str]) -> Dict[str, Callable]:
        try:
            return self._methods_per_type[base_type]
        except KeyError:
            pass
        
        methods = {
            '__deepcopy__': deepcopy__impl,
        }
        self._methods_per_type[base_type] = methods
        return methods


class UniCopyWrapper(BaseAutoDerivedObjWrapper):
    def __init__(self):
        super().__init__()
        self._copy_wrapping_required_per_type: Dict[Type, bool] = dict()
        self._deepcopy_wrapping_required_per_type: Dict[Type, bool] = dict()
        self._methods_per_type: Dict[Type, Dict[str, Callable]] = dict()
    
    def wrapping_required(self, obj: Any, base_type: Type, fields: Tuple[str]):
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


class ClassWrapper:
    def __init__(self, auto_derived_types: AutoDerivedTyped) -> None:
        self._class_wrapper__data_size: int = 0
        self._class_wrapper__auto_derived_types: AutoDerivedTyped = auto_derived_types
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass


class ClassWrappingFactory:
    def __init__(self):
        self.class_name = type(self).__name__
        self.derived: Dict[Type, Type] = dict()
        self._methods: Dict[str, Callable] = {
            '_class_wrapper__fields': None,
            '_class_wrapper__data_size': 0,
            '_class_wrapper__auto_derived_types': self,
        }
    
    @property
    def methods(self) -> Dict[str, Callable]:
        return self._methods.copy()
    
    def __call__(self, obj: Any):
        base_type = type(obj)
        base_type_name = base_type.__name__
        try:
            return self.derived[base_type_name]
        except KeyError:
            fields: Tuple = self.gen_fields_tuple(obj)
            methods = self.methods
            methods['_class_wrapper__fields'] = fields
            derived: Type = type(f'{self.class_name}__from__{base_type_name}', (base_type,), methods)
            self.derived[base_type_name] = derived
            return derived
    
    def gen_fields_tuple(self, obj: Any):
        try:
            return obj.__slots__
        except AttributeError:
            pass

        try:
            return tuple(obj.__dict__.keys())
        except AttributeError:
            pass
        
        return tuple()
