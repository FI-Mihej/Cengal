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

__all__ = ['PointBase', 'PointDimensionIndexError', 'PointNd', 'Point1d', 'Point2d', 'Point3d', 'PointNdXYZ', 'convert_point_to_xyz']

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


from copy import copy
from cengal.entities.copyable import *
from typing import Any, FrozenSet, Optional, Sequence, List, Set, Tuple, Dict, Union
numpy_present = True
try:
    import numpy as np
    from numpy import array_equal, array, ndarray
except:
    numpy_present = False

RawListPointType = List[Union[float, int]]
if numpy_present:
    RawNdarrayPointType = ndarray
    RawUniversalPointType = Union[RawListPointType, RawNdarrayPointType]
else:
    RawUniversalPointType = RawListPointType


class PointBase(CopyableMixin):
    dimension: int = 0

    def copy(self) -> 'PointBase':
        raise NotImplementedError

    def shallow_copy(self) -> 'PointBase':
        raise NotImplementedError
    
    def updated_copy(self, update: Dict) -> 'PointBase':
        raise NotImplementedError

    @property
    def dim(self) -> int:
        return self.dimension

    def __call__(self, *args: Any, **kwds: Any) -> RawListPointType:
        raise NotImplementedError
    
    def clear(self):
        raise NotImplementedError


class PointDimensionIndexError(Exception):
    pass


class PointWrongNdarrayTypeError(Exception):
    pass


class PointNd(PointBase):
    dimension: int = None
    _dim_names_translation_table: Tuple[Tuple[Set, int]] = tuple()
    _default_ndarray_type = float
    _default_shallow_copy = False

    def __init__(self
            , dimension: int
            , *args: Union[Tuple[Sequence[Union[float, int]]], Tuple[Union[float, int]]]
            , **kwargs: Dict[str, Union[float, int]]
            ) -> None:
        shallow_copy = kwargs.get('shallow_copy', self._default_shallow_copy)
        kwargs.pop('shallow_copy', None)
        if shallow_copy and args and isinstance(args[0], PointNd):
            first_element = args[0]
            self.dimension = first_element.dimension
            self._point = first_element._point
            self._ndarray_type = first_element._ndarray_type
        else:
            if dimension is not None:
                self.dimension: int = dimension
            
            self._point: RawListPointType = None
            self._ndarray_type = kwargs.get('ndarray_type', self._default_ndarray_type)
            kwargs.pop('ndarray_type', None)
            if self._ndarray_type not in {int, float}:
                print(f'Wrong type: {self._ndarray_type}')
                raise PointWrongNdarrayTypeError
            
            self.clear()
            self(*args, **kwargs)
    
    def __repr__(self):
        return f'{type(self).__name__}(dimension={self.dimension}, point=({", ".join((str(item) for item in self._point))}), ndarray_type={self._ndarray_type})'
    
    def copy(self) -> 'PointNd':
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__['dimension'] = self.dimension
        result.__dict__['_point'] = self._point.copy()
        result.__dict__['_ndarray_type'] = self._ndarray_type
        return result
    
    def shallow_copy(self) -> 'PointNd':
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__['dimension'] = self.dimension
        result.__dict__['_point'] = self._point
        result.__dict__['_ndarray_type'] = self._ndarray_type
        return result
    
    def updated_copy(self, update: Dict) -> 'PointNd':
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__['dimension'] = self.dimension
        result.__dict__['_point'] = get_dict_key_with_callable_default(update, '_point', lambda: self._point.copy())
        result.__dict__['_ndarray_type'] = self._ndarray_type
        return result
    
    def clear(self):
        self._point = [self._ndarray_type()] * self.dim
        if numpy_present:
            self._point = array(self._point)

    def __call__(self
            , *args: Union[Tuple[Sequence[Union[float, int]]], Tuple[Union[float, int]]]
            , **kwargs: Dict[str, Union[float, int]]
            ) -> RawUniversalPointType:
        if args:
            first_element = args[0]
            data = first_element
            if isinstance(first_element, PointNd):
                data = first_element()
            elif isinstance(first_element, (float, int)):
                data = args

            for index, item in enumerate(data):
                if index >= self.dim:
                    break

                self._point[index] = item
        elif kwargs:
            for dim_name_variants, dim_index in self._dim_names_translation_table:
                for dim_name in dim_name_variants:
                    if dim_name in kwargs:
                        kwargs[f'n{dim_index}'] = kwargs[dim_name]
                        break

            for dim_index in range(self.dimension):
                dim_name = f'n{dim_index}'
                dim_value = kwargs.get(dim_name, None)
                if dim_value is not None:
                    self._point[dim_index] = dim_value
        
        return self._point
    
    def as_list(self) -> RawListPointType:
        return list(self._point)
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        for dim_name_variants, dim_index in self._dim_names_translation_table:
            if __name in dim_name_variants:
                self._point[dim_index] = __value
                return __value

        if __name and __name.startswith('n'):
            index_str = __name[1:]
            if index_str.isnumeric():
                index = int(index_str)
                if index < self.dim:
                    self._point[index] = __value
                    return __value
                else:
                    raise PointDimensionIndexError

        return super().__setattr__(__name, __value)
    
    def __getattribute__(self, __name: str) -> Any:
        for dim_name_variants, dim_index in super().__getattribute__('_dim_names_translation_table'):
            if __name in dim_name_variants:
                return super().__getattribute__('_point')[dim_index]

        if __name and __name.startswith('n'):
            index_str = __name[1:]
            if index_str.isnumeric():
                index = int(index_str)
                if index < super().__getattribute__('dim'):
                    return super().__getattribute__('_point')[index]
                else:
                    raise PointDimensionIndexError

        return super().__getattribute__(__name)
    
    def __getitem__(self, index_or_key):
        if isinstance(index_or_key, int):
            return self._point[index_or_key]
        elif isinstance(index_or_key, str):
            for dim_name_variants, dim_index in self._dim_names_translation_table:
                if index_or_key in dim_name_variants:
                    return self._point[dim_index]

            if index_or_key and index_or_key.startswith('n'):
                index_str = index_or_key[1:]
                if index_str.isnumeric():
                    index = int(index_str)
                    if index < self.dim:
                        return self._point[index]
                    else:
                        raise PointDimensionIndexError
        else:
            raise KeyError

    def __setitem__(self, index_or_key, value):
        if isinstance(index_or_key, int):
            self._point[index_or_key] = value
        elif isinstance(index_or_key, str):
            for dim_name_variants, dim_index in self._dim_names_translation_table:
                if index_or_key in dim_name_variants:
                    self._point[dim_index] = value

            if index_or_key and index_or_key.startswith('n'):
                index_str = index_or_key[1:]
                if index_str.isnumeric():
                    index = int(index_str)
                    if index < self.dim:
                        self._point[index] = value
                    else:
                        raise PointDimensionIndexError
        else:
            raise KeyError
    
    def __len__(self):
        return self.dim

    def crop_to(self, *args) -> 'PointNd':
        """Example:
        >> p4 = Point3d(3, 5, 2, 8)
        >> p3 = convert_point_to_xyz(p4.crop_to('z', 'n0', 3))
        >> print(p3)
        Point3d(2, 3, 8)

        Raises:
            PointDimensionIndexError: _description_
            KeyError: _description_

        Returns:
            PointNd: _description_
        """
        if args:
            first_item = args[0]
            data = first_item
            if isinstance(first_item, (int, str)):
                data = args
            
            index_sequence = list()
            for index_or_key in data:
                if isinstance(index_or_key, int):
                    index_sequence.append(index_or_key)
                elif isinstance(index_or_key, str):
                    for dim_name_variants, dim_index in self._dim_names_translation_table:
                        if index_or_key in dim_name_variants:
                            index_sequence.append(dim_index)

                    if index_or_key and index_or_key.startswith('n'):
                        index_str = index_or_key[1:]
                        if index_str.isnumeric():
                            index = int(index_str)
                            if index < self.dim:
                                index_sequence.append(index)
                            else:
                                raise PointDimensionIndexError
                else:
                    raise KeyError
            
            croped_data = list()
            for index in index_sequence:
                croped_data.append(self._point[index])
            
            return PointNd(len(croped_data), croped_data)
        else:
            return self.copy()

    def expand_to(self, dimension: int, *args) -> 'PointNd':
        """Example:
        >> p2 = Point2d(2, 3)
        >> p3 = convert_point_to_xyz(p2.expand_to(3, 2, 'n0'))
        >> print(p3)
        Point3d(3, 0, 2)

        Args:
            dimension (int): _description_
            *args (Union[Tuple[int], Tuple[str]]): list used to map `point item` with index equal to `list's item index` to `result point item` with index equals to `list's item value`. If value is str: it should starts from 'n' char and continue with (positive) numeric chars only

        Raises:
            PointDimensionIndexError: when `len(args) > len(self)`
            KeyError: wrong type of *args or type/format of it's value(s)

        Returns:
            PointNd: _description_
        """
        if args:
            first_item = args[0]
            data = first_item
            if isinstance(first_item, (int, str)):
                data = args
            
            index_sequence = list()
            for index_or_key in data:
                if isinstance(index_or_key, int):
                    index_sequence.append(index_or_key)
                elif isinstance(index_or_key, str):
                    if index_or_key and index_or_key.startswith('n'):
                        index_str = index_or_key[1:]
                        if index_str.isnumeric():
                            index = int(index_str)
                            if index < dimension:
                                index_sequence.append(index)
                            else:
                                raise PointDimensionIndexError
                        else:
                            raise KeyError
                    else:
                        raise KeyError
                else:
                    raise KeyError
            
            expansion_data = dict()
            for source_index, destination_index in enumerate(index_sequence):
                expansion_data[f'n{destination_index}'] = self._point[source_index]
            
            return PointNd(dimension, **expansion_data)
        else:
            return self.copy()
    
    def __eq__(self, other) -> bool:
        if isinstance(other, PointNd):
            if numpy_present:
                return (self.dim == other.dim) and array_equal(self._point, other._point)
            else:
                return (self.dim == other.dim) and (self._point == other._point)
        
        return False
    
    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
    
    def __hash__(self) -> int:
        return hash((self.dim, tuple(self._point)))
    
    def __bool__(self) -> bool:
        """If not zero point

        Returns:
            bool: _description_
        """
        for item in self._point:
            if item:
                return True
        
        return False


class Point1d(PointNd):
    dimension: int = 1
    _dim_names_translation_table: Tuple[Tuple[Set, int]] = (
        ({'x', 'X'}, 0),
    )

    def __init__(self
            , *args: Union[Tuple[Sequence[Union[float, int]]], Tuple[Union[float, int]]]
            , **kwargs: Dict[str, Union[float, int]]
            ) -> None:
        PointNd.__init__(self, None, *args, **kwargs)


class Point2d(PointNd):
    dimension: int = 2
    _dim_names_translation_table: Tuple[Tuple[Set, int]] = (
        ({'x', 'X'}, 0),
        ({'y', 'Y'}, 1),
    )

    def __init__(self
            , *args: Union[Tuple[Sequence[Union[float, int]]], Tuple[Union[float, int]]]
            , **kwargs: Dict[str, Union[float, int]]
            ) -> None:
        PointNd.__init__(self, None, *args, **kwargs)


class Point3d(PointNd):
    dimension: int = 3
    _dim_names_translation_table: Tuple[Tuple[Set, int]] = (
        ({'x', 'X'}, 0),
        ({'y', 'Y'}, 1),
        ({'z', 'Z'}, 2),
    )

    def __init__(self
            , *args: Union[Tuple[Sequence[Union[float, int]]], Tuple[Union[float, int]]]
            , **kwargs: Dict[str, Union[float, int]]
            ) -> None:
        PointNd.__init__(self, None, *args, **kwargs)


class PointNdXYZ(PointNd):
    dimension: int = None
    _dim_names_translation_table: Tuple[Tuple[Set, int]] = (
        ({'x', 'X'}, 0),
        ({'y', 'Y'}, 1),
        ({'z', 'Z'}, 2),
    )

    def __init__(self
            , dimension: int
            , *args: Union[Tuple[Sequence[Union[float, int]]], Tuple[Union[float, int]]]
            , **kwargs: Dict[str, Union[float, int]]
            ) -> None:
        super().__init__(dimension, *args, **kwargs)


def convert_point_to_xyz(point: PointNd) -> PointNd:
    if 1 == point.dim:
        return Point1d(point, shallow_copy=True)
    elif 2 == point.dim:
        return Point2d(point, shallow_copy=True)
    elif 3 == point.dim:
        return Point3d(point, shallow_copy=True)
    elif 3 < point.dim:
        return PointNdXYZ(point, shallow_copy=True)
