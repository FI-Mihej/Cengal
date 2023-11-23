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


__all__ = ['BindableToType', 'AlreadyBoundError', 'NotBoundYetError']


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


from typing import Tuple, Any, Optional
from inspect import isclass


class AlreadyBoundError(Exception):
    pass


class NotBoundYetError(Exception):
    pass


class BindableToType:
    """ Bindable to type or to type of given object

    Example:

        class MyGlobalData(BindableToType):
            def __init__(self) -> None:
                super().__init__()
                self.data = 2


        class MyStructure:
            global_data = MyGlobalData()
            def __init__(self):
                self.index = 3


        print(f'{MyStructure.global_data.bound_to() = }')  # (<class '__main__.MyStructure'>, 'global_data')

        ms = MyStructure()

        print(f'{ms.global_data.bound_to() = }')  # (<class '__main__.MyStructure'>, 'global_data')

        MyGlobalData().bind(MyStructure, 'global_data_2')

        print(f'{ms.global_data_2.bound_to() = }')  # (<class '__main__.MyStructure'>, 'global_data')
        print(f'{MyStructure.global_data_2.bound_to() = }')  # (<class '__main__.MyStructure'>, 'global_data')

        MyGlobalData().bind(ms, 'global_data_3')

        print(f'{ms.global_data_3.bound_to() = }')  # (<class '__main__.MyStructure'>, 'global_data_2')
        print(f'{MyStructure.global_data_3.bound_to() = }')  # (<class '__main__.MyStructure'>, 'global_data_2')
    """    
    def __init__(self) -> None:
        self._bound_to_owner_type = None
        self._bound_to_name = None
    
    def on_bind(self, owner_type, name):
        pass
    
    def on_unbind(self, owner_type, name):
        pass

    def __set_name__(self, owner_type, name):
        self._bound_to_owner_type = owner_type
        self._bound_to_name = name
        self.on_bind(owner_type, name)
    
    def bind(self, owner_type_or_obj, name):
        if self._bound_to_owner_type is not None:
            raise AlreadyBoundError
        
        if isclass(owner_type_or_obj):
            owner_class = owner_type_or_obj
        else:
            owner_class = type(owner_type_or_obj)
        
        setattr(owner_class, name, self)
        self.__set_name__(owner_class, name)
    
    def unbind(self) -> Tuple[Any, str]:
        if self._bound_to_owner_type is None:
            raise NotBoundYetError
        
        delattr(self._bound_to_owner_type, self._bound_to_name)
        result = (self._bound_to_owner_type, self._bound_to_name)
        self._bound_to_owner_type = None
        self._bound_to_name = None
        self.on_unbind(self._bound_to_owner_type, self._bound_to_name)
        return result
    
    def bound(self) -> bool:
        return self._bound_to_owner_type is not None
    
    def bound_to(self) -> Optional[Tuple[Any, str]]:
        result = None
        if self.bound():
            result = (self._bound_to_owner_type, self._bound_to_name)
        
        return result
    
    def force_bind(self, owner_type_or_obj, name) -> Optional[Tuple[Any, str]]:
        result = None
        if self.bound():
            result = self.unbind()
        
        self.bind(owner_type_or_obj, name)
        return result
