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


__all__ = [
    'default_serializable_data_types',
    'known_types',
    'known_data_types',
    'known_container_types',
    'DataType',
    'data_type',
    'data_type_by_type',
    'ClassInfoFields',
    'ObjectInfoFields',
    'CanNotAdjustToSerializableError',
    'CanNotAdjustFromSerializableError',
    'RemoteObjectsManager',
]


from cengal.introspection.inspect import (
    entity_module_importable_str_and_owning_names_path,
    entity_by_name_module_importable_str_and_owning_names_path,
    filled_slot_names_with_values_gen,
    is_callable, is_async,
    is_setable_data_descriptor,
)
from cengal.code_flow_control.smart_values import ResultExistence
from cengal.code_flow_control.gc import DisableGC
from cengal.data_generation.id_generator import IDGenerator, GeneratorType
from enum import IntEnum
from collections.abc import MutableMapping, MutableSequence, MutableSet
from struct import pack, unpack
from inspect import getattr_static
from typing import Any, Dict, Optional, Callable, Set, Type, Tuple, List, FrozenSet


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


default_serializable_data_types: Set[Type] = {
    int, float, complex, str, bytes, bytearray, bool, type(None), list, tuple, set, frozenset, dict
}


known_types: Set[Type] = {
    int, float, complex, str, bytes, bytearray, bool, type(None), list, tuple, set, frozenset, dict,
    slice, 
}


known_data_types: Set[Type] = {
    int, float, str, bytes, bytearray, bool, type(None), slice,
}


known_container_types: Set[Type] = {
    complex, list, tuple, set, frozenset, dict,
}


class DataType(IntEnum):
    class_ = 0  # type is not in known_types and not in serializable_data_types
    int_ = 1
    float_ = 2
    complex_ = 3
    str_ = 4
    bytes_ = 5
    bytearray_ = 6
    bool_ = 7
    none_ = 8
    list_ = 9
    tuple_ = 10
    set_ = 11
    frozenset_ = 12
    dict_ = 13
    slice_ = 14
    unknown_serializable = 15  # type is in serializable_data_types but not in known_types


data_type: Dict[DataType, Type] = {
    DataType.class_: object,
    DataType.int_: int,
    DataType.float_: float,
    DataType.complex_: complex,
    DataType.str_: str,
    DataType.bytes_: bytes,
    DataType.bytearray_: bytearray,
    DataType.bool_: bool,
    DataType.none_: type(None),
    DataType.list_: list,
    DataType.tuple_: tuple,
    DataType.set_: set,
    DataType.frozenset_: frozenset,
    DataType.dict_: dict,
    DataType.slice_: slice,
    DataType.unknown_serializable: None,
}


data_type_by_type: Dict[Type, DataType] = {
    object: DataType.class_,
    int: DataType.int_,
    float: DataType.float_,
    complex: DataType.complex_,
    str: DataType.str_,
    bytes: DataType.bytes_,
    bytearray: DataType.bytearray_,
    bool: DataType.bool_,
    type(None): DataType.none_,
    list: DataType.list_,
    tuple: DataType.tuple_,
    set: DataType.set_,
    frozenset: DataType.frozenset_,
    dict: DataType.dict_,
    slice: DataType.slice_,
    None: DataType.unknown_serializable,
}


class ClassInfoFields(IntEnum):
    class_id = 0
    class_name = 1
    module_importable_str = 2
    owning_names_path = 3


class ObjectInfoFields(IntEnum):
    object_id = 0  # (type: int)
    type_id = 1  # (type: DataType)
    object_ = 2  # (Optional), (type: Any). Link to object itself if `(type(obj) in serializable_data_types)`. Not used otherwise.
    class_id = 3  # (Optional), (type: int). Used if `type_id == DataType.class_`
    clonable_slots = 4  # (Optional), (type: Tuple[Tuple[str, Any]]). Used if `type_id == DataType.class_`. Holds ID's (object_id) of slots objects.
    clonable_dict_items = 5  # (Optional), (type: Tuple[Tuple[str, Any]]). Used if `type_id == DataType.class_`. Holds ID's (object_id) of value objects.
    # contained_items = 6  # (Optional), (type: Union[Tuple, List, Set, FrozenSet, Dict]). Used if `type_id in {DataType.list_, DataType.tuple_, DataType.set_, DataType.frozenset_, DataType.dict_, DataType.slice_}`. Holds ID's (object_id) of contained items (for bothe keys and values in the case of Dict).
    contained_mapping = 6  # (Optional), (type: Union[Tuple, List, Set, FrozenSet, Dict]). Used if `type_id in {DataType.list_, DataType.tuple_, DataType.set_, DataType.frozenset_, DataType.dict_, DataType.slice_}`. Holds ID's (object_id) of contained items (for bothe keys and values in the case of Dict).
    contained_sequence = 7  # (Optional), (type: Union[Tuple, List, Set, FrozenSet, Dict]). Used if `type_id in {DataType.list_, DataType.tuple_, DataType.set_, DataType.frozenset_, DataType.dict_, DataType.slice_}`. Holds ID's (object_id) of contained items (for bothe keys and values in the case of Dict).
    contained_set = 8  # (Optional), (type: Union[Tuple, List, Set, FrozenSet, Dict]). Used if `type_id in {DataType.list_, DataType.tuple_, DataType.set_, DataType.frozenset_, DataType.dict_, DataType.slice_}`. Holds ID's (object_id) of contained items (for bothe keys and values in the case of Dict).


class CanNotAdjustToSerializableError(Exception):
    pass


class CanNotAdjustFromSerializableError(Exception):
    pass


class RemoteObjectsManager:
    def __init__(self, 
                 on_new_class_handler: Optional[Callable] = None,
                 on_new_obj_info_handler: Optional[Callable] = None,
                 # classess_db: Optional[Dict[int, Type]] = None, 
                 objects_db: Optional[Dict[int, Any]] = None, 
                 classes_id_gen: Optional[Callable] = None,
                 objects_id_gen: Optional[Callable] = None,
                 serializable_data_types: Optional[Set[Type]] = None,
                 ) -> None:
        # self.classess_db: Dict[int, Type] = dict() if classess_db is None else classess_db
        self.classes_id_gen: IDGenerator = IDGenerator() if classes_id_gen is None else classes_id_gen
        self.objects_db: Dict[int, Any] = dict() if objects_db is None else objects_db
        self.objects_id_gen: IDGenerator = IDGenerator() if objects_id_gen is None else objects_id_gen
        self.serializable_data_types: Set[Type] = default_serializable_data_types if serializable_data_types is None else serializable_data_types
        self.serializable_any: bool = not self.serializable_data_types
        self.serializable_int: bool = (int in self.serializable_data_types) or self.serializable_any
        self.serializable_float: bool = (float in self.serializable_data_types) or self.serializable_any
        self.serializable_complex: bool = (complex in self.serializable_data_types) or self.serializable_any
        self.serializable_str: bool = (str in self.serializable_data_types) or self.serializable_any
        self.serializable_bytes: bool = (bytes in self.serializable_data_types) or self.serializable_any
        self.serializable_bytearray: bool = (bytearray in self.serializable_data_types) or self.serializable_any
        self.serializable_bool: bool = (bool in self.serializable_data_types) or self.serializable_any
        self.serializable_none: bool = (type(None) in self.serializable_data_types) or self.serializable_any
        self.serializable_list: bool = (list in self.serializable_data_types) or self.serializable_any
        self.serializable_tuple: bool = (tuple in self.serializable_data_types) or self.serializable_any
        self.serializable_set: bool = (set in self.serializable_data_types) or self.serializable_any
        self.serializable_frozenset: bool = (frozenset in self.serializable_data_types) or self.serializable_any
        self.serializable_dict: bool = (dict in self.serializable_data_types) or self.serializable_any
        self.serializable_slice: bool = (slice in self.serializable_data_types) or self.serializable_any
        self.known_classes: Dict[Type, int] = dict()
        self.known_classes_by_id: Dict[int, Type] = dict()
        self.known_classes_info: Dict[Tuple, int] = dict()
        self.known_classes_info_by_id: Dict[int, Tuple] = dict()
        self.on_new_class_handler: Optional[Callable] = on_new_class_handler
        self.on_new_obj_info_handler: Optional[Callable] = on_new_obj_info_handler
        self.objects_ids: Dict[int, int] = dict()  # (Key: object_id, Value: id(obj))
        self.objects_ids_by_id: Dict[int, int] = dict()  # (Key: id(obj), Value: object_id)

    def del_object_by_id(self, id_: int) -> None:
        if id_ in self.objects_ids_by_id:
            object_id = self.objects_ids_by_id[id_]
            self.objects_ids_by_id.pop(id_, None)
            self.objects_ids.pop(object_id, None)
            self.objects_db.pop(object_id, None)
    
    dobi = del_object_by_id
    
    def del_object_by_object_id(self, object_id: int) -> None:
        if object_id in self.objects_ids:
            id_ = self.objects_ids[object_id]
            self.objects_ids_by_id.pop(id_, None)
            self.objects_ids.pop(object_id, None)
            self.objects_db.pop(object_id, None)
    
    doboi = del_object_by_object_id
    
    def adjust_to_serializable(self, type_id: DataType, obj: Any) -> Any:
        if DataType.int_ == type_id:
            return obj
        elif DataType.float_ == type_id:
            return obj
        elif DataType.complex_ == type_id:
            if self.serializable_complex:
                return obj
            elif self.serializable_bytes:
                return pack('=dd', obj.real, obj.imag)
            elif self.serializable_bytearray:
                return bytearray(pack('=dd', obj.real, obj.imag))
            elif self.serializable_str:
                return str(obj)
            elif self.serializable_float:
                if self.serializable_tuple:
                    return (obj.real, obj.imag)
                elif self.serializable_list:
                    return [obj.real, obj.imag]
                else:
                    pass
            else:
                pass
        elif DataType.str_ == type_id:
            return obj
        elif DataType.bytes_ == type_id:
            if self.serializable_bytes:
                return obj
            elif self.serializable_bytearray:
                return bytearray(obj)
            elif self.serializable_str:
                return obj.hex()
            elif self.serializable_tuple:
                if self.serializable_int:
                    return  tuple(int(c) for c in obj)
                if self.serializable_float:
                    return  tuple(float(int(c)) for c in obj)
                else:
                    pass
            elif self.serializable_list:
                if self.serializable_int:
                    return  [int(c) for c in obj]
                if self.serializable_float:
                    return  [float(int(c)) for c in obj]
                else:
                    pass
            else:
                pass
        elif DataType.bytearray_ == type_id:
            if self.serializable_bytearray:
                return obj
            elif self.serializable_bytes:
                return bytes(obj)
            elif self.serializable_str:
                return obj.hex()
            elif self.serializable_tuple:
                if self.serializable_int:
                    return  tuple(int(c) for c in obj)
                if self.serializable_float:
                    return  tuple(float(int(c)) for c in obj)
                else:
                    pass
            elif self.serializable_list:
                if self.serializable_int:
                    return  [int(c) for c in obj]
                if self.serializable_float:
                    return  [float(int(c)) for c in obj]
                else:
                    pass
            else:
                pass
        elif DataType.bool_ == type_id:
            return obj
        elif DataType.none_ == type_id:
            return obj
        elif DataType.list_ == type_id:
            if self.serializable_list:
                return obj
            elif self.serializable_tuple:
                return tuple(obj)
            elif self.serializable_dict:
                return dict({index: item for index, item in enumerate(obj)})
            else:
                pass
        elif DataType.tuple_ == type_id:
            if self.serializable_tuple:
                return obj
            elif self.serializable_list:
                return list(obj)
            elif self.serializable_dict:
                return dict({index: item for index, item in enumerate(obj)})
            else:
                pass
        elif DataType.set_ == type_id:
            if self.serializable_set:
                return obj
            elif self.serializable_frozenset:
                return frozenset(obj)
            elif self.serializable_tuple:
                return tuple(obj)
            elif self.serializable_list:
                return list(obj)
            elif self.serializable_dict:
                return dict({k: None for k in obj})
            else:
                pass
        elif DataType.frozenset_ == type_id:
            if self.serializable_frozenset:
                return obj
            elif self.serializable_set:
                return set(obj)
            elif self.serializable_tuple:
                return tuple(obj)
            elif self.serializable_list:
                return list(obj)
            elif self.serializable_dict:
                return dict({k: None for k in obj})
            else:
                pass
        elif DataType.dict_ == type_id:
            return obj
        elif DataType.slice_ == type_id:
            if self.serializable_slice:
                return obj
            elif self.serializable_tuple:
                return (obj.start, obj.stop, obj.step)
            elif self.serializable_list:
                return [obj.start, obj.stop, obj.step]
            elif self.serializable_dict:
                return {0: obj.start, 1: obj.stop, 2: obj.step}
            else:
                pass
        else:
            raise RuntimeError('Unknown type_id')
        
        raise CanNotAdjustToSerializableError(f'Can not adjust to serializable. Type: {type_id}, obj: {obj}')

    ats = adjust_to_serializable

    def adjust_from_serializable(self, type_id: DataType, obj: Any) -> Any:
        if DataType.int_ == type_id:
            return obj
        elif DataType.float_ == type_id:
            return obj
        elif DataType.complex_ == type_id:
            if self.serializable_complex:
                return obj
            elif self.serializable_bytes:
                return complex(*unpack('=dd', obj))
            elif self.serializable_bytearray:
                return complex(*unpack('=dd', bytes(obj)))
            elif self.serializable_str:
                return complex(*obj)
            elif self.serializable_float:
                if self.serializable_tuple:
                    return complex(*obj)
                elif self.serializable_list:
                    return complex(*obj)
                else:
                    pass
            else:
                pass
        elif DataType.str_ == type_id:
            return obj
        elif DataType.bytes_ == type_id:
            if self.serializable_bytes:
                return obj
            elif self.serializable_bytearray:
                return bytes(obj)
            elif self.serializable_str:
                return bytes.fromhex(obj)
            elif self.serializable_tuple:
                if self.serializable_int:
                    return  b''.join(item.to_bytes(1, 'little') for item in obj)
                if self.serializable_float:
                    return  b''.join((int(round(item))).to_bytes(1, 'little') for item in obj)
                else:
                    pass
            elif self.serializable_list:
                if self.serializable_int:
                    return  b''.join(item.to_bytes(1, 'little') for item in obj)
                if self.serializable_float:
                    return  b''.join((int(round(item))).to_bytes(1, 'little') for item in obj)
                else:
                    pass
            else:
                pass
        elif DataType.bytearray_ == type_id:
            if self.serializable_bytearray:
                return obj
            elif self.serializable_bytes:
                return bytearray(obj)
            elif self.serializable_str:
                return bytearray(bytes.fromhex(obj))
            elif self.serializable_tuple:
                if self.serializable_int:
                    return  bytearray(b''.join(item.to_bytes(1, 'little') for item in obj))
                if self.serializable_float:
                    return  bytearray(b''.join((int(round(item))).to_bytes(1, 'little') for item in obj))
                else:
                    pass
            elif self.serializable_list:
                if self.serializable_int:
                    return  bytearray(b''.join(item.to_bytes(1, 'little') for item in obj))
                if self.serializable_float:
                    return  bytearray(b''.join((int(round(item))).to_bytes(1, 'little') for item in obj))
                else:
                    pass
            else:
                pass
        elif DataType.bool_ == type_id:
            return obj
        elif DataType.none_ == type_id:
            return None
        elif DataType.list_ == type_id:
            if self.serializable_list:
                return obj
            elif self.serializable_tuple:
                return list(obj)
            elif self.serializable_dict:
                return [value for key, value in sorted(obj.items(), key=lambda x: x[0])]
            else:
                pass
        elif DataType.tuple_ == type_id:
            if self.serializable_tuple:
                return obj
            elif self.serializable_list:
                return tuple(obj)
            elif self.serializable_dict:
                return tuple(value for key, value in sorted(obj.items(), key=lambda x: x[0]))
            else:
                pass
        elif DataType.set_ == type_id:
            if self.serializable_set:
                return obj
            elif self.serializable_frozenset:
                return set(obj)
            elif self.serializable_tuple:
                return set(obj)
            elif self.serializable_list:
                return set(obj)
            elif self.serializable_dict:
                return set(obj.keys())
            else:
                pass
        elif DataType.frozenset_ == type_id:
            if self.serializable_frozenset:
                return obj
            elif self.serializable_set:
                return frozenset(obj)
            elif self.serializable_tuple:
                return frozenset(obj)
            elif self.serializable_list:
                return frozenset(obj)
            elif self.serializable_dict:
                return frozenset(obj.keys())
            else:
                pass
        elif DataType.dict_ == type_id:
            return obj
        elif DataType.slice_ == type_id:
            if self.serializable_slice:
                return obj
            elif self.serializable_tuple:
                return slice(*obj)
            elif self.serializable_list:
                return slice(*obj)
            elif self.serializable_dict:
                return slice(obj[0], obj[1], obj[2])
            else:
                pass
        else:
            raise RuntimeError('Unknown type_id')
        
        raise CanNotAdjustFromSerializableError(f'Can not adjust from serializable. Type: {type_id}, obj: {obj}')
    
    afs = adjust_from_serializable
    
    # def is_replicatable_object_attribute(self, attribute: Any) -> bool:
    #     if is_setable_data_descriptor(attribute):
    #         data = attribute.__get__(None, None)
    #     elif is_callable(attribute):
    #         return False
    #     else:
    #         return True

    def serialize_container(self, type_id: DataType, obj: Any) -> Any:
        if DataType.list_ == type_id:
            new_obj = list()
            for item in obj:
                result: ResultExistence[int] = self.serialize_impl(item)
                if result:
                    new_obj.append(result.value)
        elif DataType.tuple_ == type_id:
            new_obj = list()
            for item in obj:
                result: ResultExistence[int] = self.serialize_impl(item)
                if result:
                    new_obj.append(result.value)
            
            new_obj = tuple(new_obj)
        elif DataType.set_ == type_id:
            new_obj = set()
            for item in obj:
                result: ResultExistence[int] = self.serialize_impl(item)
                if result:
                    new_obj.add(result.value)
        elif DataType.frozenset_ == type_id:
            new_obj = set()
            for item in obj:
                result: ResultExistence[int] = self.serialize_impl(item)
                if result:
                    new_obj.add(result.value)
                
            new_obj = frozenset(new_obj)
        elif DataType.dict_ == type_id:
            new_obj = dict()
            for key, value in obj.items():
                key_result: ResultExistence[int] = self.serialize_impl(key)
                value_result: ResultExistence[int] = self.serialize_impl(value)
                if key_result and value_result:
                    new_obj[key_result.value] = value_result.value
        
        return new_obj
    
    sc = serialize_container

    def serialize_impl(self, obj: Any, ignore_empty_classes: bool = False) -> ResultExistence[int]:
        result_exists: bool = True
        id_: int = id(obj)
        obj_type = type(obj)
        if (int != obj_type) and (id_ in self.objects_ids_by_id):
            new_object: bool = False
            object_id: int = self.objects_ids_by_id[id_]
        else:
            # int object must always produce new object_id because first 256 ints are persistent across Python sessions and
            # this can cause issues within users of current module. For example within `cengal/hardware/memory/shared_memory`
            # which changes int values inline instead of producing new objects.
            new_object = True
            object_id = self.objects_id_gen()
            self.objects_ids[object_id] = id_
            self.objects_db[object_id] = obj
        
        if not new_object:
            return ResultExistence[int](result_exists, object_id)
        
        if  self.serializable_any or (obj_type in self.serializable_data_types):
            serializable: bool = True
            type_id: DataType = data_type_by_type.get(obj_type, DataType.unknown_serializable)
        else:
            serializable = False
            type_id = data_type_by_type.get(obj_type, DataType.class_)
        
        if obj_type in known_container_types:
            known_container: bool = True
        else:
            known_container = False
        
        class_info: Dict[int, Any] = None
        known_data: bool = None
        class_id: int = None
        is_new_class: bool = None
        class_name: str = None
        new_obj_slots: List[Tuple[str, Any]] = None
        new_obj_dict: Dict[str, Any] = None
        obj_mapping: Dict = None
        obj_sequence: List = None
        obj_set: Set = None
        if serializable:
            if known_container:
                object_info = (
                    object_id,
                    type_id.value,
                    self.sc(type_id, obj),
                )
            else:
                object_info = (
                    object_id,
                    type_id.value,
                    obj,
                )
        else:
            if obj_type in known_data_types:
                known_data = True
            else:
                known_data = False
            
            if DataType.class_ == type_id:
                new_obj_slots = list()
                for slot_name, slot_value in filled_slot_names_with_values_gen(obj):
                    adjusted_slot_name = slot_name
                    item_result: ResultExistence[int] = self.serialize_impl(slot_value)
                    if item_result:
                        if self.serializable_tuple:
                            new_obj_slots.append((adjusted_slot_name, item_result.value))
                        elif self.serializable_list:
                            new_obj_slots.append([adjusted_slot_name, item_result.value])
                        else:
                            new_obj_slots.append(self.ats(DataType.tuple_, (adjusted_slot_name, item_result.value)))
                
                if new_obj_slots:
                    if self.serializable_list:
                        pass
                    elif self.serializable_tuple:
                        new_obj_slots = tuple(new_obj_slots)
                    else:
                        new_obj_slots = self.ats(DataType.list_, new_obj_slots)
                
                new_obj_dict = dict()
                if hasattr(obj, '__dict__'):
                    for key, value in obj.__dict__.items():
                        # raw_value = getattr_static(obj, key)
                        # if hasattr(raw_value, '__get__') and (not hasattr(raw_value, '__set__')):
                        #     # if not setable descriptor
                        #     continue

                        adjusted_key = key

                        value_result: ResultExistence[int] = self.serialize_impl(value)
                        if value_result:
                            new_obj_dict[adjusted_key] = value_result.value
                        else:
                            continue
                
                obj_mapping = dict()
                obj_sequence = list()
                obj_set = list()
                if isinstance(obj, MutableMapping):
                    for key, value in obj.items():
                        key_result: ResultExistence[int] = self.serialize_impl(value)
                        if not key_result:
                            continue

                        value_result: ResultExistence[int] = self.serialize_impl(value)
                        if value_result:
                            obj_mapping[key_result.value] = value_result.value
                        else:
                            continue
                elif isinstance(obj, MutableSequence):
                    for item in obj:
                        item_result: ResultExistence[int] = self.serialize_impl(item)
                        if item_result:
                            obj_sequence.append(item_result.value)
                        else:
                            continue
                    
                    if obj_sequence:
                        if self.serializable_list:
                            pass
                        else:
                            obj_sequence = self.ats(DataType.list_, obj_sequence)
                elif isinstance(obj, MutableSet):
                    for item in obj:
                        item_result: ResultExistence[int] = self.serialize_impl(item)
                        if item_result:
                            obj_set.append(item_result.value)
                        else:
                            continue
                    
                    if obj_set:
                        if self.serializable_set:
                            pass
                        else:
                            obj_set = self.ats(DataType.list_, obj_set)
                else:
                    pass

                if ignore_empty_classes:
                    result_exists = new_obj_slots or new_obj_dict or obj_mapping or obj_sequence or obj_set
                
                if result_exists:
                    if obj_type in self.known_classes:
                        is_new_class = False
                        class_id = self.known_classes[obj_type]
                    else:
                        class_info = dict()
                        is_new_class = True
                        class_name = obj_type.__name__
                        class_id = self.classes_id_gen()
                        self.known_classes[obj_type] = class_id
                        self.known_classes_by_id[class_id] = obj_type
                        module_importable_str, owning_names_path = entity_module_importable_str_and_owning_names_path(obj)
                        module_importable_str_and_owning_names_path = (class_name, module_importable_str, tuple(owning_names_path))
                        self.known_classes_info[module_importable_str_and_owning_names_path] = class_id
                        self.known_classes_info_by_id[class_id] = module_importable_str_and_owning_names_path

                        class_info = (
                            class_id,
                            class_name,
                            module_importable_str,
                            owning_names_path,
                        )
                        
                        if self.on_new_class_handler:
                            self.on_new_class_handler(
                                class_info,
                                obj_type,
                                class_id,
                                class_name,
                                module_importable_str,
                                owning_names_path,
                                module_importable_str_and_owning_names_path
                            )

                # will be later serialized much faster than without `if else None`
                object_info = (
                    object_id,
                    type_id.value,
                    0,
                    class_id,
                    new_obj_slots if new_obj_slots else 0,
                    new_obj_dict if new_obj_dict else 0,
                    obj_mapping if obj_mapping else 0,
                    obj_sequence if obj_sequence else 0,
                    obj_set if obj_set else 0,
                )
            elif known_data:
                object_info = (
                    object_id,
                    type_id.value,
                    self.ats(type_id, obj),
                )
            elif known_container:
                object_info = (
                    object_id,
                    type_id.value,
                    self.ats(type_id, self.sc(type_id, obj)),
                )
            else:
                raise RuntimeError('Unknown type_id')

        if result_exists:
            if self.on_new_obj_info_handler:
                self.on_new_obj_info_handler(
                    object_info,
                    obj,
                    object_id,
                    type_id,
                    serializable,
                    known_container,
                    known_data,
                    class_id,
                    is_new_class,
                    new_obj_slots,
                    new_obj_dict,
                    obj_mapping,
                    obj_sequence,
                    obj_set,
                )
        
        return ResultExistence[int](result_exists, object_id)
    
    si = serialize_impl

    def serialize(self, obj: Any, ignore_empty_classes: bool = False) -> ResultExistence[int]:
        with DisableGC():
            return self.serialize_impl(obj, ignore_empty_classes)
    
    s = serialize
    
    def deserialize_class_impl(self, class_info: Tuple) -> ResultExistence[Tuple[int, Type]]:
        class_id: int = class_info[ClassInfoFields.class_id.value]
        if class_id in self.known_classes_by_id:
            return ResultExistence[Tuple[int, Type]](True, (class_id, self.known_classes_by_id[class_id]))
        else:
            class_name: str = class_info[ClassInfoFields.class_name.value]
            module_importable_str: str = class_info[ClassInfoFields.module_importable_str.value]
            owning_names_path: List[str] = self.afs(DataType.list_, class_info[ClassInfoFields.owning_names_path.value])
            obj_class: Type = entity_by_name_module_importable_str_and_owning_names_path(class_name, module_importable_str, owning_names_path)
            self.known_classes_by_id[class_id] = obj_class
            self.known_classes[obj_class] = class_id
            class_info_tuple: Tuple = (class_name, module_importable_str, tuple(owning_names_path)) 
            self.known_classes_info[class_info_tuple] = class_id
            self.known_classes_info_by_id[class_id] = class_info_tuple
            return ResultExistence[Tuple[int, Type]](True, (class_id, obj_class))
    
    dcli = deserialize_class_impl
    
    def deserialize_class(self, class_info: Tuple) -> ResultExistence[Tuple[int, Type]]:
        with DisableGC():
            return self.deserialize_class_impl(class_info)
    
    dcl = deserialize_class

    def deserialize_container_impl(self, type_id: DataType, obj: Any) -> Any:
        new_obj = obj
        if DataType.list_ == type_id:
            new_obj = list()
            for item_id in obj:
                new_obj.append(self.objects_db[item_id])
        elif DataType.tuple_ == type_id:
            new_obj = list()
            for item_id in obj:
                new_obj.append(self.objects_db[item_id])
            
            new_obj = tuple(new_obj)
        elif DataType.set_ == type_id:
            new_obj = set()
            for item_id in obj:
                new_obj.add(self.objects_db[item_id])
        elif DataType.frozenset_ == type_id:
            new_obj = set()
            for item_id in obj:
                new_obj.add(self.objects_db[item_id])
                
            new_obj = frozenset(new_obj)
        elif DataType.dict_ == type_id:
            new_obj = dict()
            for key_id, value_id in obj.items():
                new_obj[self.objects_db[int(key_id)]] = self.objects_db[value_id]
        
        return new_obj
    
    dcoi = deserialize_container_impl

    def deserialize_container(self, type_id: DataType, obj: Any) -> Any:
        with DisableGC():
            return self.deserialize_container_impl(type_id, obj)
    
    dco = deserialize_container

    def deserialize_obj_impl(self, obj_info: Tuple) -> ResultExistence[Tuple[int, Any]]:
        object_id: int = obj_info[ObjectInfoFields.object_id.value]
        if object_id in self.objects_db:
            return ResultExistence[Tuple[int, Any]](True, (object_id, self.objects_db[object_id]))
        
        type_id: DataType = DataType(obj_info[ObjectInfoFields.type_id.value])
        
        obj_type = data_type[type_id] 
        serializable: bool = self.serializable_any or (obj_type in self.serializable_data_types)
        known_container: bool = obj_type in known_container_types
        known_data: bool = None
        
        if serializable:
            if known_container:
                obj = self.dcoi(type_id, obj_info[ObjectInfoFields.object_.value])
            else:
                obj = obj_info[ObjectInfoFields.object_.value]
        else:
            known_data = obj_type in known_data_types
            
            if DataType.class_ == type_id:
                class_id: int = obj_info[ObjectInfoFields.class_id.value]
                obj_class: Type = self.known_classes_by_id[class_id]
                obj: Any = obj_class.__new__(obj_class)

                if obj_info[ObjectInfoFields.clonable_slots.value]:
                    clonable_slots = self.afs(DataType.list_, obj_info[ObjectInfoFields.clonable_slots.value])
                    for slot_name, slot_id in clonable_slots:
                        child_obj = self.objects_db[slot_id]
                        setattr(obj, slot_name, child_obj)
                
                if obj_info[ObjectInfoFields.clonable_dict_items.value]:
                    clonable_dict_items = obj_info[ObjectInfoFields.clonable_dict_items.value]
                    for key, value_id in clonable_dict_items.items():
                        child_obj = self.objects_db[value_id]
                        setattr(obj, key, child_obj)
                
                if obj_info[ObjectInfoFields.contained_mapping.value]:
                    contained_mapping = obj_info[ObjectInfoFields.contained_mapping.value]
                    for key_id, value_id in contained_mapping.items():
                        child_key = self.objects_db[int(key_id)]
                        child_value = self.objects_db[value_id]
                        obj[child_key] = child_value
                
                if obj_info[ObjectInfoFields.contained_sequence.value]:
                    contained_sequence = self.afs(DataType.list_, obj_info[ObjectInfoFields.contained_sequence.value])
                    for item_id in contained_sequence:
                        child_item = self.objects_db[item_id]
                        obj.append(child_item)
                
                if obj_info[ObjectInfoFields.contained_set.value]:
                    contained_set = self.afs(DataType.list_, obj_info[ObjectInfoFields.contained_set.value])
                    for item_id in contained_set:
                        child_item = self.objects_db[item_id]
                        obj.add(child_item)
            elif known_data:
                obj = self.afs(type_id, obj_info[ObjectInfoFields.object_.value])
            elif known_container:
                obj = self.dcoi(type_id, self.afs(type_id, obj_info[ObjectInfoFields.object_.value]))
            else:
                raise RuntimeError('Unknown type_id')
        
        self.objects_db[object_id] = obj
        id_: int = id(obj)
        self.objects_ids[object_id] = id_
        self.objects_ids_by_id[id_] = object_id
        return ResultExistence[Tuple[int, Any]](True, (object_id, obj))
    
    doi = deserialize_obj_impl

    def deserialize_obj(self, obj_info: Tuple) -> ResultExistence[Tuple[int, Any]]:
        with DisableGC():
            return self.deserialize_obj_impl(obj_info)
    
    do = deserialize_obj
