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
        'ValueExistenceNamedTuple',
        'ValueExistence',
        'ValueHolder',
        'ResultExistence',
        'ResultHolder',
        'ErrorExistence',
        'ErrorHolder',
        'ValueCache',
        'ValueTypeNamedTuple',
        'ValueType',
        'ValueWithTypeNamedTuple',
        'ValueWithType',
    ]


from cengal.introspection.inspect import entity_module_importable_str_and_owning_names_path, entity_by_name_module_importable_str_and_owning_names_path
from collections import namedtuple
from collections.abc import Sequence
from typing import Any, TypeVar, Generic, Tuple, NamedTuple, Union, Optional

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


# TODO: implement Cython version (smart_values are used by our Cython code)


VT = TypeVar('VT')


ValueExistenceNamedTuple = namedtuple('ValueExistenceNamedTuple', ['existence', 'value'])


class ValueExistence(Generic[VT], Sequence):
    __slots__ = ('existence', '_value')

    def __init__(self, existence: bool = False, value: VT = None):
        self.existence: bool = existence
        self._value: VT = value

    def __len__(self):
        return 2

    def __getitem__(self, index):
        if 0 == index:
            return self.existence
        elif 1 == index:
            return self._value
        else:
            raise IndexError
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self.existence = True
        self._value = value

    def __bool__(self):
        return self.existence

    def __nonzero__(self):
        return self.__bool__()

    def __str__(self):
        return f'{type(self).__name__}({repr(self.existence)}, {repr(self.value)})'

    def __repr__(self):
        return self.__str__()

    def __getstate__(self):
        return self.existence, self.value

    def __setstate__(self, state):
        existence, value = state
        self.value = value
        self.existence = existence
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, ValueExistence):
            return (self.existence == __value.existence) and (self.value == __value.value)
        else:
            if self.existence:
                return self.value == __value
            else:
                return False
    
    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)
    
    def to_namedtuple(self) -> ValueExistenceNamedTuple:
        return ValueExistenceNamedTuple(self.existence, self.value)
    
    def to_tuple(self) -> Tuple:
        return self.existence, self.value
    
    def to_dict(self) -> dict:
        return {
            'existence': self.existence,
            'value': self.value,
        }
    
    def serialize_to_dict(self) -> Tuple[dict, dict]:
        module_importable_str, owning_names_path = entity_module_importable_str_and_owning_names_path(self.__class__)
        return {
            'existence': self.existence,
            'value': self.value,
        }, {
            'class_name': self.__class__,
            'module_importable_str': module_importable_str,
            'owning_names_path': owning_names_path,
        }
    
    @classmethod
    def from_namedtuple(cls, named_tuple: ValueExistenceNamedTuple) -> 'ValueExistence':
        return cls(named_tuple.existence, named_tuple.value)
    
    @classmethod
    def from_tuple(cls, tuple_: Tuple) -> 'ValueExistence':
        return cls(*tuple_)
    
    @classmethod
    def from_dict(cls, dict_: dict) -> 'ValueExistence':
        return cls(dict_['existence'], dict_['value'])
    
    @classmethod
    def deserialize_from_dict(cls, dict_: dict, owning_info: Optional[str] = None) -> 'ValueExistence':
        if owning_info is None:
            return cls(dict_['existence'], dict_['value'])
        else:
            class_type = entity_by_name_module_importable_str_and_owning_names_path(owning_info['class_name'], owning_info['module_importable_str'], owning_info['owning_names_path'])
            return class_type(dict_['existence'], dict_['value'])
    
    @classmethod
    def from_other(cls, value: Union['ValueExistence', ValueExistenceNamedTuple, Tuple, VT]) -> 'ValueExistence':
        if isinstance(value, ValueExistence):
            return cls(value.existence, value.value)
        elif isinstance(value, ValueExistenceNamedTuple):
            return cls.from_namedtuple(value)
        elif isinstance(value, tuple):
            return cls.from_tuple(value)
        elif isinstance(value, dict):
            return cls.from_dict(value)
        else:
            try:
                return cls(value.existence, value.value)
            except AttributeError:
                return cls(True, value)


class ValueHolder(ValueExistence[VT]):
    def __init__(self, existence: bool = False, value: VT = None):
        super().__init__(existence, value)


class ResultExistence(ValueExistence[VT]):
    def __init__(self, existence: bool = False, value: VT = None):
        super().__init__(existence, value)


class ResultHolder(ValueExistence[VT]):
    def __init__(self, existence: bool = False, value: VT = None):
        super().__init__(existence, value)


class ErrorExistence(ValueExistence[VT]):
    def __init__(self, existence: bool = False, value: VT = None):
        super().__init__(existence, value)


class ErrorHolder(ValueExistence[VT]):
    def __init__(self, existence: bool = False, value: VT = None):
        super().__init__(existence, value)


class ValueCache(ValueExistence[VT]):
    __slots__ = tuple()

    def __init__(self, existence: bool = False, value: VT = None):
        super(ValueCache, self).__init__(existence, value)

    def __call__(self, *args, **kwargs):
        self.existence = False

    def get(self) -> VT:
        return self.value

    def set(self, new_value: VT):
        self.existence = True
        self.value = new_value

    def reset(self):
        self.existence = False

    def __getstate__(self):
        return self.existence, self.value

    def __setstate__(self, state):
        existence, value = state
        self.value = value
        self.existence = existence
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, ValueExistence):
            return (self.existence == __value.existence) and (self.value == __value.value)
        else:
            if self.existence:
                return self.value == __value
            else:
                return False
    
    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)


TT = TypeVar('TT')


ValueTypeNamedTuple = namedtuple('ValueTypeNamedTuple', ['type_id', 'value'])


class ValueType(Generic[TT, VT], Sequence):
    __slots__ = ('type_id', 'value')

    def __init__(self, type_id: TT, value: VT):
        self.type_id: TT = type_id
        self.value: VT = value

    def __len__(self):
        return 2

    def __getitem__(self, index):
        if 0 == index:
            return self.type_id
        elif 1 == index:
            return self.value
        else:
            raise IndexError

    def __eq__(self, other):
        # "__ne__() delegates to __eq__() and inverts the value"
        if isinstance(other, (ValueType, ValueWithType)):
            return self.type_id == other.type_id
        else:
            return self.type_id == other

    def __getstate__(self):
        return self.type_id, self.value

    def __setstate__(self, state):
        self.type_id, self.value = state

    def __str__(self):
        return f'{type(self).__name__}({repr(self.type_id)}, {repr(self.value)})'

    def __repr__(self):
        return self.__str__()
    
    def to_namedtuple(self) -> ValueTypeNamedTuple:
        return ValueTypeNamedTuple(self.type_id, self.value)
    
    def to_tuple(self) -> Tuple:
        return self.type_id, self.value
    
    def to_dict(self) -> dict:
        return {
            'type_id': self.type_id,
            'value': self.value,
        }
    
    def serialize_to_dict(self) -> Tuple[dict, dict]:
        module_importable_str, owning_names_path = entity_module_importable_str_and_owning_names_path(self.__class__)
        return {
            'type_id': self.type_id,
            'value': self.value,
        }, {
            'class_name': self.__class__,
            'module_importable_str': module_importable_str,
            'owning_names_path': owning_names_path,
        }
    
    @classmethod
    def from_namedtuple(cls, named_tuple: ValueTypeNamedTuple) -> 'ValueExistence':
        return cls(named_tuple.type_id, named_tuple.value)
    
    @classmethod
    def from_tuple(cls, tuple_: Tuple) -> 'ValueExistence':
        return cls(*tuple_)
    
    @classmethod
    def from_dict(cls, dict_: dict) -> 'ValueExistence':
        return cls(dict_['type_id'], dict_['value'])
    
    @classmethod
    def deserialize_from_dict(cls, dict_: dict, owning_info: Optional[str] = None) -> 'ValueExistence':
        if owning_info is None:
            return cls(dict_['type_id'], dict_['value'])
        else:
            class_type = entity_by_name_module_importable_str_and_owning_names_path(owning_info['class_name'], owning_info['module_importable_str'], owning_info['owning_names_path'])
            return class_type(dict_['type_id'], dict_['value'])
    
    @classmethod
    def from_other(cls, value: Union['ValueExistence', ValueTypeNamedTuple, Tuple, VT]) -> 'ValueExistence':
        if isinstance(value, ValueExistence):
            return cls(value.type_id, value.value)
        elif isinstance(value, ValueTypeNamedTuple):
            return cls.from_namedtuple(value)
        elif isinstance(value, tuple):
            return cls.from_tuple(value)
        elif isinstance(value, dict):
            return cls.from_dict(value)
        else:
            try:
                return cls(value.type_id, value.value)
            except AttributeError:
                return cls(None, value)


ValueWithTypeNamedTuple = namedtuple('ValueWithTypeNamedTuple', ['type_id', 'value'])


class ValueWithType(Generic[TT, VT], Sequence):
    __slots__ = ('type_id', 'value')

    def __init__(self, type_id: TT, value: VT):
        self.type_id: TT = type_id
        self.value: VT = value

    def __len__(self):
        return 2

    def __getitem__(self, index):
        if 0 == index:
            return self.type_id
        elif 1 == index:
            return self.value
        else:
            raise IndexError

    def __eq__(self, other):
        # "__ne__() delegates to __eq__() and inverts the value"
        if isinstance(other, ValueType):
            return self.type_id == other.type_id
        elif isinstance(other, ValueWithType):
            return (self.type_id == other.type_id) and (self.value == other.value)
        else:
            return self.value == other

    def __getstate__(self):
        return self.type_id, self.value

    def __setstate__(self, state):
        self.type_id, self.value = state

    def __str__(self):
        return f'{type(self).__name__}({repr(self.type_id)}, {repr(self.value)})'

    def __repr__(self):
        return self.__str__()
    
    def to_namedtuple(self) -> ValueWithTypeNamedTuple:
        return ValueWithTypeNamedTuple(self.type_id, self.value)
    
    def to_tuple(self) -> Tuple:
        return self.type_id, self.value
    
    def to_dict(self) -> dict:
        return {
            'type_id': self.type_id,
            'value': self.value,
        }
    
    def serialize_to_dict(self) -> Tuple[dict, dict]:
        module_importable_str, owning_names_path = entity_module_importable_str_and_owning_names_path(self.__class__)
        return {
            'type_id': self.type_id,
            'value': self.value,
        }, {
            'class_name': self.__class__,
            'module_importable_str': module_importable_str,
            'owning_names_path': owning_names_path,
        }
    
    @classmethod
    def from_namedtuple(cls, named_tuple: ValueWithTypeNamedTuple) -> 'ValueExistence':
        return cls(named_tuple.type_id, named_tuple.value)
    
    @classmethod
    def from_tuple(cls, tuple_: Tuple) -> 'ValueExistence':
        return cls(*tuple_)
    
    @classmethod
    def from_dict(cls, dict_: dict) -> 'ValueExistence':
        return cls(dict_['type_id'], dict_['value'])
    
    @classmethod
    def deserialize_from_dict(cls, dict_: dict, owning_info: Optional[str] = None) -> 'ValueExistence':
        if owning_info is None:
            return cls(dict_['type_id'], dict_['value'])
        else:
            class_type = entity_by_name_module_importable_str_and_owning_names_path(owning_info['class_name'], owning_info['module_importable_str'], owning_info['owning_names_path'])
            return class_type(dict_['type_id'], dict_['value'])
    
    @classmethod
    def from_other(cls, value: Union['ValueExistence', ValueWithTypeNamedTuple, Tuple, VT]) -> 'ValueExistence':
        if isinstance(value, ValueExistence):
            return cls(value.type_id, value.value)
        elif isinstance(value, ValueWithTypeNamedTuple):
            return cls.from_namedtuple(value)
        elif isinstance(value, tuple):
            return cls.from_tuple(value)
        elif isinstance(value, dict):
            return cls.from_dict(value)
        else:
            try:
                return cls(value.type_id, value.value)
            except AttributeError:
                return cls(None, value)
