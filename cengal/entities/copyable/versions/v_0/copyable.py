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

__all__ = ['copy__impl', 'CopyMixin', 'deepcopy__impl', 'DeepCopyMixin', 'CopyMethodsMixin', 'CopyableMixin', 'get_dict_key_with_callable_default']

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


from copy import deepcopy
from typing import Callable, Dict, Hashable, Any
from cengal.data_manipulation.get_dict_key_with_callable_default import get_dict_key_with_callable_default


def copy__impl(self):
    cls = self.__class__
    result = cls.__new__(cls)
    try:
        result.__dict__.update(self.__dict__)
        return result
    except AttributeError:
        pass

    for field in self.__slots__:
        setattr(result, field, getattr(self, field))
    
    return result


class CopyMixin:
    def __copy__(self):
        return copy__impl(self)


def deepcopy__impl(self, memo):
    cls = self.__class__
    result = cls.__new__(cls)
    memo[id(self)] = result
    try:
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        
        return result
    except AttributeError:
        pass

    for field in self.__slots__:
        setattr(result, field, getattr(self, field))
    
    return result


class DeepCopyMixin:
    def __deepcopy__(self, memo):
        return deepcopy__impl(self, memo)



class CopyMethodsMixin:
    def copy(self):
        """Should make relevant copy of an object (not so general and deep as a deepcopy()). should copy only known object fields.
        Example:
            def copy(self):
                cls = self.__class__
                result = cls.__new__(cls)
                result.__dict__['dimension'] = self.dimension
                result.__dict__['_point'] = self._point.copy()
                return result

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError

    def shallow_copy(self):
        """Same as copy.copy(self), but should copy only known object fields.
        Example:
            def shallow_copy(self):
                cls = self.__class__
                result = cls.__new__(cls)
                result.__dict__['dimension'] = self.dimension
                result.__dict__['_point'] = self._point
                return result

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError

    def updated_copy(self, update: Dict):
        """Will make updated copy of an object. Other behavior should be the same as in the `def copy(self)` method.
        Example:
            # from cengal.data_manipulation.get_dict_key_with_callable_default import get_dict_key_with_callable_default
            from cengal.entities.copyable import CopyableMixin, get_dict_key_with_callable_default
            
            def updated_copy(self, update: Dict):
                cls = self.__class__
                result = cls.__new__(cls)
                result.__dict__['dimension'] = update.get('dimension', self.dimension)
                result.__dict__['_point'] = get_dict_key_with_callable_default(update, '_point', lambda: self._point.copy())
                return result

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError


class CopyableMixin(CopyMixin, DeepCopyMixin, CopyMethodsMixin):
    pass
