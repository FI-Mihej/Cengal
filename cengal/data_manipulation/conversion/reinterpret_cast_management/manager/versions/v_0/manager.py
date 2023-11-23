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


__all__ = ['AutoDerivedClass', 'BaseAutoDerivedObjWrapper', 'ClassWrappingFactory', 'ClassWrappingFactoryWithObjDataSizeLog']


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


from sys import getsizeof
from cengal.data_generation.id_generator import IDGenerator
from cengal.data_manipulation.conversion.reinterpret_cast import TemporaryReinterpretCast, reinterpret_cast
from cengal.entities.copyable import copy__impl, deepcopy__impl
from typing import Dict, Type, Callable, Any, Tuple, FrozenSet, Set, Optional
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
    
    def wrapping_required(self, obj: Any, base_type: Type, fields: Tuple[str], planned_type_name: str) -> bool:
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
            planned_type_name: str = f'{self.class_name}__{self._instance_id}__from__{base_type_name}'
            if self.wrapping_required(obj, base_type, fields, planned_type_name):
                result: Type = type(planned_type_name, self.base_classes(obj, base_type, fields), self.methods(obj, base_type, fields))
                self.derived[base_type_name] = result
                return result
            else:
                return base_type
    
    def __call__(self, obj: Any):
        obj.__class__ = self.type(obj)
        return obj

    def temporary(self, obj: Any):
        return TemporaryReinterpretCast(self.type(obj), obj)

    def persistent(self, obj: Any):
        return reinterpret_cast(self.type(obj), obj)


# class ClassWrapper:
#     def __init__(self, auto_derived_types: AutoDerivedTyped) -> None:
#         self._class_wrapper__data_size: int = 0
#         self._class_wrapper__auto_derived_types: AutoDerivedTyped = auto_derived_types
    
#     def __call__(self, *args: Any, **kwds: Any) -> Any:
#         pass


class ClassWrappingFactory:
    instance_id = IDGenerator()

    def __init__(self):
        self._instance_id: int = self.instance_id()
        self.class_name = type(self).__name__
        self.derived: Dict[Type, Type] = dict()
        self._attributes_and_methods: Dict[str, Callable] = {
            '_class_wrapper__field_names': None,
            '_class_wrapper__factory': self,
        }
    
    @property
    def attributes_and_methods(self) -> Dict[str, Callable]:
        return self._attributes_and_methods.copy()
    
    def edit_derived_type(self, obj: Any, attributes_and_methods, field_names: Tuple[str]) -> Dict[str, Any]:
        """Might be overloaded in a derived class if needed

        Args:
            obj (Any): _description_
            attributes_and_methods (_type_): _description_
            field_names (Tuple[str]): _description_
            data_size (int): _description_

        Returns:
            Dict[str, Any]: _description_
        """        
        return attributes_and_methods
    
    def gen_kwargs(self, obj: Any, attributes_and_methods, field_names: Tuple[str]) -> Optional[Dict[str, Any]]:
        """Might be overloaded in a derived class if needed

        Args:
            obj (Any): _description_
            attributes_and_methods (_type_): _description_
            field_names (Tuple[str]): _description_
            data_size (int): _description_

        Returns:
            Optional[Dict[str, Any]]: _description_
        """        
        return None
    
    def __call__(self, obj: Any):
        base_type = type(obj)
        base_type_name = base_type.__name__
        try:
            return self.derived[base_type_name]
        except KeyError:
            field_names: Tuple = self.gen_fields_tuple(obj)
            
            attributes_and_methods = self.attributes_and_methods
            attributes_and_methods['_class_wrapper__field_names'] = field_names
            attributes_and_methods = self.edit_derived_type(obj, attributes_and_methods, field_names)
            kwargs = self.gen_kwargs(obj, attributes_and_methods, field_names)
            
            if kwargs is None:
                derived: Type = type(f'{self.class_name}__{self._instance_id}__from__{base_type_name}', (base_type,), attributes_and_methods)
            else:
                derived: Type = type(f'{self.class_name}__{self._instance_id}__from__{base_type_name}', (base_type,), attributes_and_methods, **kwargs)

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


class ClassWrappingFactoryWithObjDataSizeLog(ClassWrappingFactory):
    def __init__(self):
        super().__init__()
        self.attributes_and_methods['_class_wrapper__obj_data_size_log'] = 0
    
    def edit_derived_type(self, obj: Any, attributes_and_methods, field_names: Tuple[str], data_size: int) -> Dict[str, Any]:
        data_size = 0
        for field_name in field_names:
            data_size += getsizeof(getattr(obj, field_name))

        attributes_and_methods['_class_wrapper__obj_data_size_log'] = data_size
        return attributes_and_methods
