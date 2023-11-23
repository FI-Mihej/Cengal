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

__all__ = ['VectorDimentionConflictError', 'VectorBase', 'CoordinateVectorDimentionsAreNotMatch', 'CoordinateVectorNd', 'VectorNd', 'DirectedGraphNd']


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


from time import perf_counter
from cengal.entities.copyable import *
from cengal.math.geometry.point import *
from typing import Any, FrozenSet, Optional, Sequence, List, Set, Tuple, Dict, Union
from math import sqrt
numpy_present = True
try:
    import numpy as np
    from numpy import linalg, array
except:
    numpy_present = False


class VectorDimentionConflictError(ValueError):
    pass


class VectorBase(CopyableMixin):
    def copy(self) -> 'VectorBase':
        raise NotImplementedError

    def shallow_copy(self) -> 'VectorBase':
        raise NotImplementedError
    
    def updated_copy(self, update: Dict) -> 'VectorBase':
        raise NotImplementedError

    @property
    def dim(self) -> int:
        raise NotImplementedError
    
    def _is_dimension_ok(self) -> bool:
        raise NotImplementedError

    def _is_new_points_dimension_ok(self, new_point: PointNd) -> bool:
        raise NotImplementedError

    def _set_forgotten_points_to_zero(self):
        raise NotImplementedError

    def __call__(self
            , *args: Tuple[PointNd]
            , **kwargs: Dict[str, PointNd]
            ) -> PointNd:
        raise NotImplementedError
    
    def __len__(self):
        raise NotImplementedError


class CoordinateVectorDimentionsAreNotMatch(ValueError):
    pass


class CoordinateVectorNd(VectorBase):
    _terminal_point_names = {'tp', 'terminal_point', 'terminal point'}

    def __init__(self, terminal_point: PointNd) -> None:
        self.terminal_point: PointNd = terminal_point
    
    def __repr__(self):
        return f'{type(self).__name__}(tp={repr(self.terminal_point)})'
    
    def copy(self) -> 'CoordinateVectorNd':
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__['terminal_point'] = self.terminal_point.copy()
        return result
    
    def shallow_copy(self) -> 'CoordinateVectorNd':
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__['terminal_point'] = self.terminal_point
        return result
    
    def updated_copy(self, update: Dict) -> 'CoordinateVectorNd':
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__['terminal_point'] = get_dict_key_with_callable_default(update, 'terminal_point', lambda: self.terminal_point.copy())
        return result
    
    @property
    def dim(self):
        return self.terminal_point.dim
    
    def _is_dimension_ok(self) -> bool:
        return True

    def __call__(self
            , *args: Tuple[PointNd]
            , **kwargs: Dict[str, PointNd]
            ) -> PointNd:
        if args:
            first_item = args[0]
            if isinstance(first_item, CoordinateVectorNd):
                data = first_item()
            elif isinstance(first_item, PointNd):
                data = first_item
            else:
                raise ValueError
            
            self.terminal_point = data
        elif kwargs:
            terminal_point = kwargs.get('terminal_point')
            for terminal_point_name_variant in self._terminal_point_names:
                terminal_point = kwargs.get(terminal_point_name_variant, None)
                if terminal_point is not None:
                    self.terminal_point = terminal_point
        
        return self.terminal_point
    
    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 == index:
                return self.terminal_point
            else:
                raise IndexError
        else:
            if index in self._terminal_point_names:
                return self.terminal_point
            else:
                raise KeyError
    
    def __setitem__(self, index, value):
        if isinstance(index, int):
            if 0 == index:
                self.terminal_point = value
            else:
                raise IndexError
        else:
            if index in self._terminal_point_names:
                self.terminal_point = value
            else:
                raise KeyError
    
    def __len__(self):
        return 1

    def magnitude(self) -> float:
        if numpy_present:
            return linalg.norm(self.terminal_point())
        else:
            result = 0
            for item in self.terminal_point:
                result += item * item
            
            return sqrt(result)
    
    def length(self) -> float:
        return self.magnitude()

    def magnitude_square(self) -> float:
        if numpy_present:
            tp = self.terminal_point()
            return sum(tp * tp)
        else:
            result = 0
            for item in self.terminal_point:
                result += item * item
            
            return result
    
    # add
    def __add__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(self.terminal_point[index] + other.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(self.terminal_point[index] + other)
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __radd__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        return self.__add__(other)
    
    def __iadd__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        if numpy_present:
            if isinstance(other, CoordinateVectorNd):
                self.terminal_point._point += other.terminal_point()
            elif isinstance(other, (float, int)):
                self.terminal_point._point += other
            else:
                raise NotImplemented
        else:
            if isinstance(other, CoordinateVectorNd):
                for index in range(self.dim):
                    self.terminal_point[index] += other.terminal_point[index]
            elif isinstance(other, (float, int)):
                for index in range(self.dim):
                    self.terminal_point[index] += other
            else:
                raise NotImplemented

        return self
    
    # sub
    def __sub__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        if numpy_present:
            result = None
            if isinstance(other, CoordinateVectorNd):
                result = self.terminal_point() - other.terminal_point()
            elif isinstance(other, (float, int)):
                result = self.terminal_point() - other
            else:
                raise NotImplemented
            
            return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result, ndarray_type=type(result[0].item()))))
        else:
            result = list()
            if isinstance(other, CoordinateVectorNd):
                for index in range(self.dim):
                    result.append(self.terminal_point[index] - other.terminal_point[index])
            elif isinstance(other, (float, int)):
                for index in range(self.dim):
                    result.append(self.terminal_point[index] - other)
            else:
                raise NotImplemented
            
            return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __rsub__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(other.terminal_point[index] - self.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(other - self.terminal_point[index])
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __isub__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                self.terminal_point[index] -= other.terminal_point[index]
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                self.terminal_point[index] -= other
        else:
            raise NotImplemented

        return self
    
    # mul
    def __mul__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        """Multiplication to number or to other coordinate vector (item by item)

        v1 = [1, 2, 3]
        v2 = [2, 3, 1]
        v3 = v1 * v2 = [1 * 2, 2 * 3, 3 * 1] = [2, 6, 3]

        Args:
            other (Union[float, int, &#39;CoordinateVectorNd&#39;]): _description_

        Raises:
            NotImplemented: _description_

        Returns:
            CoordinateVectorNd: _description_
        """
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(self.terminal_point[index] * other.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(self.terminal_point[index] * other)
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __rmul__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        """Multiplication to number or to other coordinate vector (item by item)

        v1 = [1, 2, 3]
        v2 = [2, 3, 1]
        v3 = v1 * v2 = [1 * 2, 2 * 3, 3 * 1] = [2, 6, 3]

        Args:
            other (Union[float, int, &#39;CoordinateVectorNd&#39;]): _description_

        Returns:
            CoordinateVectorNd: _description_
        """
        return self.__mul__(other)
    
    def __imul__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        """Multiplication to number or to other coordinate vector (item by item)

        v1 = [1, 2, 3]
        v2 = [2, 3, 1]
        v3 = v1 * v2 = [1 * 2, 2 * 3, 3 * 1] = [2, 6, 3]

        Args:
            other (Union[float, int, &#39;CoordinateVectorNd&#39;]): _description_

        Raises:
            NotImplemented: _description_

        Returns:
            CoordinateVectorNd: _description_
        """
        if numpy_present:
            if isinstance(other, CoordinateVectorNd):
                self.terminal_point._point *= other.terminal_point()
            elif isinstance(other, (float, int)):
                self.terminal_point._point *= other
            else:
                raise NotImplemented
        else:
            if isinstance(other, CoordinateVectorNd):
                for index in range(self.dim):
                    self.terminal_point[index] *= other.terminal_point[index]
            elif isinstance(other, (float, int)):
                for index in range(self.dim):
                    self.terminal_point[index] *= other
            else:
                raise NotImplemented

        return self
    
    # matmul
    def __matmul__(self, other: Union[float, int, 'CoordinateVectorNd']) -> Union[float, int]:
        """Dot product
        >> cv0 = CoordinateVectorNd(2, 4)
        >> cv1 = CoordinateVectorNd(1, 3)
        >> dot_product = cv0 @ cv1
        >> print(dot_product)
        14

        Args:
            other (Union[float, int, &#39;CoordinateVectorNd&#39;]): _description_

        Raises:
            NotImplemented: _description_
            CoordinateVectorDimentionsAreNotMatch: _description_

        Returns:
            Union[float, int]: _description_
        """
        if not isinstance(other, CoordinateVectorNd):
            raise NotImplemented
        
        dim = self.dim
        if dim != other.dim:
            raise CoordinateVectorDimentionsAreNotMatch

        result = 0
        for index in range(dim):
            result += self.terminal_point[index] * other.terminal_point[index]
        
        return result
    
    # truediv
    def __truediv__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(self.terminal_point[index] / other.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(self.terminal_point[index] / other)
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __rtruediv__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(other.terminal_point[index] / self.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(other / self.terminal_point[index])
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __itruediv__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        if numpy_present:
            if isinstance(other, CoordinateVectorNd):
                self.terminal_point._point /= other.terminal_point()
            elif isinstance(other, (float, int)):
                self.terminal_point._point /= other
            else:
                raise NotImplemented
        else:
            if isinstance(other, CoordinateVectorNd):
                for index in range(self.dim):
                    self.terminal_point[index] /= other.terminal_point[index]
            elif isinstance(other, (float, int)):
                for index in range(self.dim):
                    self.terminal_point[index] /= other
            else:
                raise NotImplemented

        return self
    
    # floordiv
    def __floordiv__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(self.terminal_point[index] // other.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(self.terminal_point[index] // other)
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __rfloordiv__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(other.terminal_point[index] // self.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(other // self.terminal_point[index])
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __ifloordiv__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        if numpy_present:
            if isinstance(other, CoordinateVectorNd):
                self.terminal_point._point //= other.terminal_point()
            elif isinstance(other, (float, int)):
                self.terminal_point._point //= other
            else:
                raise NotImplemented
        else:
            if isinstance(other, CoordinateVectorNd):
                for index in range(self.dim):
                    self.terminal_point[index] //= other.terminal_point[index]
            elif isinstance(other, (float, int)):
                for index in range(self.dim):
                    self.terminal_point[index] //= other
            else:
                raise NotImplemented

        return self
    
    # mod
    def __mod__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(self.terminal_point[index] % other.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(self.terminal_point[index] % other)
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __rmod__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(other.terminal_point[index] % self.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(other % self.terminal_point[index])
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __imod__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                self.terminal_point[index] %= other.terminal_point[index]
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                self.terminal_point[index] %= other
        else:
            raise NotImplemented

        return self
    
    # pow
    def __pow__(self, other: Union[float, int, 'CoordinateVectorNd'], modulo) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(pow(self.terminal_point[index], other.terminal_point[index], modulo))
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(pow(self.terminal_point[index], other, modulo))
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __rpow__(self, other: Union[float, int, 'CoordinateVectorNd'], modulo) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(pow(other.terminal_point[index], self.terminal_point[index], modulo))
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(pow(other, self.terminal_point[index], modulo))
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __ipow__(self, other: Union[float, int, 'CoordinateVectorNd'], modulo) -> 'CoordinateVectorNd':
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                self.terminal_point[index].__ipow__(other.terminal_point[index], modulo)
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                self.terminal_point[index].__ipow__(other, modulo)
        else:
            raise NotImplemented

        return self
    
    # lshift
    def __lshift__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(self.terminal_point[index] << other.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(self.terminal_point[index] << other)
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __rlshift__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(other.terminal_point[index] << self.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(other << self.terminal_point[index])
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __ilshift__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                self.terminal_point[index] <<= other.terminal_point[index]
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                self.terminal_point[index] <<= other
        else:
            raise NotImplemented

        return self
    
    # rshift
    def __rshift__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(self.terminal_point[index] >> other.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(self.terminal_point[index] >> other)
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __rrshift__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(other.terminal_point[index] >> self.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(other >> self.terminal_point[index])
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __irshift__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                self.terminal_point[index] >>= other.terminal_point[index]
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                self.terminal_point[index] >>= other
        else:
            raise NotImplemented

        return self
    
    # and
    def __and__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(self.terminal_point[index] & other.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(self.terminal_point[index] & other)
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __rand__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(other.terminal_point[index] & self.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(other & self.terminal_point[index])
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __iand__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                self.terminal_point[index] &= other.terminal_point[index]
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                self.terminal_point[index] &= other
        else:
            raise NotImplemented

        return self
    
    # xor
    def __xor__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(self.terminal_point[index] ^ other.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(self.terminal_point[index] ^ other)
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __rxor__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(other.terminal_point[index] ^ self.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(other ^ self.terminal_point[index])
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __ixor__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                self.terminal_point[index] ^= other.terminal_point[index]
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                self.terminal_point[index] ^= other
        else:
            raise NotImplemented

        return self
    
    # or
    def __or__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(self.terminal_point[index] | other.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(self.terminal_point[index] | other)
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __ror__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        result = list()
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                result.append(other.terminal_point[index] | self.terminal_point[index])
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                result.append(other | self.terminal_point[index])
        else:
            raise NotImplemented
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __ior__(self, other: Union[float, int, 'CoordinateVectorNd']) -> 'CoordinateVectorNd':
        if isinstance(other, CoordinateVectorNd):
            for index in range(self.dim):
                self.terminal_point[index] |= other.terminal_point[index]
        elif isinstance(other, (float, int)):
            for index in range(self.dim):
                self.terminal_point[index] |= other
        else:
            raise NotImplemented

        return self
    
    # neg
    def __neg__(self) -> 'CoordinateVectorNd':
        if numpy_present:
            result = self.terminal_point().__neg__()
            return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result, ndarray_type=type(result[0].item()))))
        else:
            result = list()
            for index in range(self.dim):
                result.append(self.terminal_point[index].__neg__())
            
            return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    # pos
    def __pos__(self) -> 'CoordinateVectorNd':
        result = list()
        for index in range(self.dim):
            result.append(self.terminal_point[index].__pos__())
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    # abs
    def __abs__(self) -> 'CoordinateVectorNd':
        result = list()
        for index in range(self.dim):
            result.append(self.terminal_point[index].__abs__())
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    # invert
    def __invert__(self) -> 'CoordinateVectorNd':
        result = list()
        for index in range(self.dim):
            result.append(self.terminal_point[index].__invert__())
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    # complex
    def __complex__(self) -> 'CoordinateVectorNd':
        result = list()
        for index in range(self.dim):
            result.append(self.terminal_point[index].__complex__())
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    # int
    def __int__(self) -> 'CoordinateVectorNd':
        result = list()
        for index in range(self.dim):
            result.append(self.terminal_point[index].__int__())
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    # float
    def __float__(self) -> 'CoordinateVectorNd':
        result = list()
        for index in range(self.dim):
            result.append(self.terminal_point[index].__float__())
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    # round
    def __round__(self, ndigits) -> 'CoordinateVectorNd':
        result = list()
        for index in range(self.dim):
            result.append(self.terminal_point[index].__round__(ndigits))
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    # trunc
    def __trunc__(self) -> 'CoordinateVectorNd':
        result = list()
        for index in range(self.dim):
            result.append(self.terminal_point[index].__trunc__())
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    # floor
    def __floor__(self) -> 'CoordinateVectorNd':
        result = list()
        for index in range(self.dim):
            result.append(self.terminal_point[index].__floor__())
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    # ceil
    def __ceil__(self) -> 'CoordinateVectorNd':
        result = list()
        for index in range(self.dim):
            result.append(self.terminal_point[index].__ceil__())
        
        return CoordinateVectorNd(convert_point_to_xyz(PointNd(len(result), result)))
    
    def __eq__(self, other) -> bool:
        if isinstance(other, PointNd):
            return self.terminal_point == other.terminal_point
        
        return False
    
    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
    
    def __hash__(self) -> int:
        return hash(self.terminal_point)
    
    def __bool__(self) -> bool:
        """If not zero point

        Returns:
            bool: _description_
        """
        return self.terminal_point.__bool__()

    # TODO: Другие операции умножения применимые к координатным векторам - реализовать в методах.
    # А неприменимые - в соответствующих классах (например DirectedGraphNd отлично подходит на роль 
    # матрицы с которой будут производится манипуляции. Каждая точка - отдельный столбец. 
    # Направление слева-направо: слева нулевой индекс, а справа - максимальный индекс)


class VectorNd(VectorBase):
    _initial_point_names = {'ip', 'initial_point', 'initial point'}
    _terminal_point_names = {'tp', 'terminal_point', 'terminal point'}

    def __init__(self
            , *args: Tuple[PointNd]
            , **kwargs: Dict[str, PointNd]
            ) -> None:
        self.initial_point: PointNd = None
        self.terminal_point: PointNd = None
        self(*args, **kwargs)
    
    def copy(self) -> 'VectorNd':
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__['initial_point'] = self.initial_point.copy()
        result.__dict__['terminal_point'] = self.terminal_point.copy()
        return result
    
    def shallow_copy(self) -> 'VectorNd':
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__['initial_point'] = self.initial_point
        result.__dict__['terminal_point'] = self.terminal_point
        return result
    
    def updated_copy(self, update: Dict) -> 'VectorNd':
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__['initial_point'] = get_dict_key_with_callable_default(update, 'initial_point', lambda: self.initial_point.copy())
        result.__dict__['terminal_point'] = get_dict_key_with_callable_default(update, 'terminal_point', lambda: self.terminal_point.copy())
        return result
    
    @property
    def dim(self):
        if self.initial_point is None:
            return None
        
        return self.initial_point.dim

    def _is_dimension_ok(self) -> bool:
        if (self.initial_point is None) and (self.terminal_point is None):
            return True
        
        initial_dim = self.initial_point.dim
        terminal_dim = self.terminal_point.dim
        if initial_dim == terminal_dim:
            return True
        else:
            raise VectorDimentionConflictError
    
    def _set_forgotten_points_to_zero(self):
        if (self.initial_point is not None) and (self.terminal_point is None):
            dim = self.initial_point.dim
            self.terminal_point = PointNd(dim, [0] * dim)
        elif (self.initial_point is None) and (self.terminal_point is not None):
            dim = self.terminal_point.dim
            self.initial_point = PointNd(dim, [0] * dim)
        elif (self.initial_point is None) and (self.terminal_point is None):
            pass

    def __call__(self
            , *args: Tuple[PointNd]
            , **kwargs: Dict[str, PointNd]
            ) -> Tuple[PointNd]:
        if args:
            first_item = args[0]
            data = first_item
            if isinstance(first_item, VectorNd):
                data = first_item()
            if isinstance(first_item, CoordinateVectorNd):
                terminal_point = first_item()
                data = [PointNd(terminal_point.dim), terminal_point]
            elif isinstance(first_item, PointNd):
                data = args
            
            self.initial_point = data[0]
            data_len = len(data)
            if data_len == 2:
                self.terminal_point = data[1]
            elif data_len > 2:
                raise IndexError
            
            self._set_forgotten_points_to_zero()
            self._is_dimension_ok()
        elif kwargs:
            for initial_point_name_variant in self._initial_point_names:
                initial_point = kwargs.get(initial_point_name_variant, None)
                if initial_point is not None:
                    self.initial_point = initial_point
                    break

            for terminal_point_name_variant in self._terminal_point_names:
                terminal_point = kwargs.get(terminal_point_name_variant, None)
                if terminal_point is not None:
                    self.terminal_point = terminal_point
                    break
            
            self._set_forgotten_points_to_zero()
            self._is_dimension_ok()
        
        return [self.initial_point, self.terminal_point]
    
    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 == index:
                return self.initial_point
            elif 1 == index:
                return self.terminal_point
            else:
                raise IndexError
        else:
            if index in self._initial_point_names:
                return self.initial_point
            elif index in self._terminal_point_names:
                return self.terminal_point
            else:
                raise KeyError
    
    def __setitem__(self, index, value):
        if isinstance(index, int):
            if 0 == index:
                self.initial_point = value
            elif 1 == index:
                self.terminal_point = value
            else:
                raise IndexError
        else:
            if index in self._initial_point_names:
                self.initial_point = value
            elif index in self._terminal_point_names:
                self.terminal_point = value
            else:
                raise KeyError
        
        self._set_forgotten_points_to_zero()
        self._is_dimension_ok()
    
    def __len__(self):
        return 2

    def magnitude(self) -> float:
        if numpy_present:
            distance_vec = self.terminal_point() - self.initial_point()
            return linalg.norm(distance_vec)
        else:
            init_vec: CoordinateVectorNd = CoordinateVectorNd(self.initial_point)
            term_vec: CoordinateVectorNd = CoordinateVectorNd(self.terminal_point)
            distance_vec: CoordinateVectorNd = term_vec - init_vec
            return distance_vec.magnitude()
    
    def length(self) -> float:
        return self.magnitude()

    def magnitude_square(self) -> float:
        if numpy_present:
            distance_vec = self.terminal_point() - self.initial_point()
            return sum(distance_vec * distance_vec)
        else:
            init_vec: CoordinateVectorNd = CoordinateVectorNd(self.initial_point)
            term_vec: CoordinateVectorNd = CoordinateVectorNd(self.terminal_point)
            distance_vec: CoordinateVectorNd = term_vec - init_vec
            return distance_vec.magnitude_square()
    
    def is_convergence(self, other: 'VectorNd'):
        if numpy_present:
            init_dist = other.initial_point() - self.initial_point()
            term_dist = other.terminal_point() - self.terminal_point()
            return sum(init_dist * init_dist) > sum(term_dist * term_dist)
        else:
            return VectorNd(self.initial_point, other.initial_point).magnitude_square() \
                > VectorNd(self.terminal_point, other.terminal_point).magnitude_square()
    
    def is_divergence(self, other: 'VectorNd'):
        if numpy_present:
            init_dist = other.initial_point() - self.initial_point()
            term_dist = other.terminal_point() - self.terminal_point()
            return sum(init_dist * init_dist) < sum(term_dist * term_dist)
        else:
            return VectorNd(self.initial_point, other.initial_point).magnitude_square() \
                < VectorNd(self.terminal_point, other.terminal_point).magnitude_square()
    
    def is_conver_diver_parity(self, other: 'VectorNd'):
        if numpy_present:
            init_dist = other.initial_point() - self.initial_point()
            term_dist = other.terminal_point() - self.terminal_point()
            return sum(init_dist * init_dist) == sum(term_dist * term_dist)
        else:
            return VectorNd(self.initial_point, other.initial_point).magnitude_square() \
                == VectorNd(self.terminal_point, other.terminal_point).magnitude_square()
    
    def conver_diver_state(self, other: 'VectorNd') -> int:
        if numpy_present:
            init_dist = other.initial_point() - self.initial_point()
            term_dist = other.terminal_point() - self.terminal_point()
            init_magnitude_square = sum(init_dist * init_dist)
            term_magnitude_square = sum(term_dist * term_dist)
        else:
            init_magnitude_square = VectorNd(self.initial_point, other.initial_point).magnitude_square()
            term_magnitude_square = VectorNd(self.terminal_point, other.terminal_point).magnitude_square()

        if init_magnitude_square > term_magnitude_square:
            return 1
        elif init_magnitude_square == term_magnitude_square:
            return 0
        elif init_magnitude_square < term_magnitude_square:
            return -1


class DirectedGraphNd(VectorBase):
    def __init__(self
            , *args: Union[Tuple[PointNd], Tuple[Sequence[PointNd]]]
            ) -> None:
        self.points_list: List[PointNd] = None
        self(*args)
    
    def copy(self) -> 'DirectedGraphNd':
        cls = self.__class__
        result = cls.__new__(cls)
        if self.points_list is None:
            result.__dict__['points_list'] = self.points_list
        else:
            result.__dict__['points_list'] = [point.copy() for point in self.points_list]

        return result
    
    def shallow_copy(self) -> 'DirectedGraphNd':
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__['points_list'] = self.points_list
        return result
    
    def updated_copy(self, update: Dict) -> 'DirectedGraphNd':
        cls = self.__class__
        result = cls.__new__(cls)
        def copy_points():
            if self.points_list is None:
                return self.points_list
            else:
                return [point.copy() for point in self.points_list]

        result.__dict__['points_list'] = get_dict_key_with_callable_default(update, 'points_list', copy_points)
        return result
    
    @property
    def dim(self):
        if self.points_list:
            return self.points_list[0].dim
        else:
            return None

    def _is_dimension_ok(self) -> bool:
        if self.points_list:
            initial_dim = self.points_list[0].dim
            for point in self.points_list:
                if initial_dim != point.dim:
                    raise VectorDimentionConflictError
        else:
            return True

    def _is_new_points_dimension_ok(self, new_point: PointNd) -> bool:
        dim = self.dim
        if dim is None:
            return True
        else:
            if dim == new_point.dim:
                return True
            else:
                raise VectorDimentionConflictError

    def __call__(self
            , *args: Union[Tuple[PointNd], Tuple[Sequence[PointNd]]]
            ) -> Optional[List[PointNd]]:
        if args:
            first_item = args[0]
            data = first_item
            if isinstance(first_item, VectorNd):
                data = first_item()
            elif isinstance(first_item, PointNd):
                data = args
            
            self.points_list = list(data)
        
        self._is_dimension_ok()
        return self.points_list
    
    def get_vector(self, index: int) -> VectorNd:
        if 0 <= index < (len(self) - 1):
            return VectorNd(self[index], self[index + 1])
        else:
            raise IndexError
    
    def get_vector_reversed(self, index: int) -> VectorNd:
        if 1 <= index < len(self):
            return VectorNd(self[index], self[index - 1])
        else:
            raise IndexError
    
    def __getitem__(self, index):
        return self.points_list[index]
    
    def __setitem__(self, index, value):
        self._is_new_points_dimension_ok(value)
        self.points_list[index] = value
    
    def __len__(self):
        return len(self.points_list)


# class VectorBase:
#     def move(self, point: PointBase):
#         raise NotImplementedError

# class Vector1d:
#     pass

# class Vector3d:
#     pass
