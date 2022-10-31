#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2022 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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

__all__ = ['EntityWithExtendableArgs', 'ArgsManagerMixin', 'ExtendKwargsManager', 'EKwargs', 'ExtendArgsManager', 'EArgs', 'ArgsManager', 'merge_func_args', 'interested_args_to_kwargs', 'func_args_to_kwargs', 'number_of_provided_args']

from enum import Enum
from typing import Any, Dict, Type, Callable, Union, Optional, Sequence, Tuple, List
import inspect
import copy
from pprint import pprint

"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2022 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "0.0.8"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


EntityWithExtendableArgs = Union[Type, Callable]


class ArgsManagerMixin:
    def __call__(self, entity: EntityWithExtendableArgs, *args, **kwargs) -> Any:
        raise NotImplementedError


class ExtendKwargsManager(ArgsManagerMixin):
    """
    Usage: 
        am = ArgsManager(
            EKwargs({'a': 'hello', 'next': 'world}),
            EKwargs(a='hello', b='world')
        )
    """
    
    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
        if not self.kwargs:
            self.kwargs = args[0]
        if not isinstance(self.kwargs, Dict):
            raise RuntimeError('Wrong parameters')
    
    def __call__(self, entity: EntityWithExtendableArgs, *args, **kwargs) -> Any:
        kwargs.update(self.kwargs)
        return args, kwargs


EKwargs = ExtendKwargsManager


class ExtendArgsManager(ArgsManagerMixin):
    """
    Usage: 
        def my_func(first, second, third, fourth, a, b, c):
            ...
        
        am = ArgsManager(
            EArgs(first, second, a='hello', b='world'),
        )
        am(my_func, third, fourth, c='!')
        
        am = ArgsManager(
            EArgs(first, second, a='hello', b='world').args_state(ExtendArgsManager.ArgsState.prefix),
        )
        am(my_func, third, fourth, c='!')
        
        am = ArgsManager(
            EArgs(third, fourth, a='hello', b='world').args_state(ExtendArgsManager.ArgsState.suffix),
        )
        am(my_func, first, second, c='!')
        
        am = ArgsManager(
            EArgs(first, second, third, fourth, a='hello', b='world').args_state(ExtendArgsManager.ArgsState.manager),
        )
        am(my_func, c='!')
        # Or:
        # am(my_func, ignored, ignored, ignored, ignored, c='!')
        
        am = ArgsManager(
            EArgs(a='hello', b='world').args_state(ExtendArgsManager.ArgsState.original),
        )
        # Or:
        # am = ArgsManager(
        #     EArgs(ignored, ignored, ignored, ignored, a='hello', b='world').args_state(ExtendArgsManager.ArgsState.original),
        # )
        am(my_func, first, second, third, fourth, c='!')
    """
    class ArgsState(Enum):
        original = 0
        prefix = 1
        suffix = 2
        manager = 3
    
    def __init__(self, *args, **kwargs):
        self.args = args
        self._args_state: 'ExtendArgsManager.ArgsState' = ExtendArgsManager.ArgsState.prefix
        self.kwargs = kwargs or dict()
        if not isinstance(self.kwargs, Dict):
            raise RuntimeError('Wrong parameters')
    
    def args_state(self, args_state: 'ExtendArgsManager.ArgsState') -> 'ExtendArgsManager':
        self._args_state = args_state
        return self
    
    def __call__(self, entity: EntityWithExtendableArgs, *args, **kwargs) -> Any:
        if ExtendArgsManager.ArgsState.original == self._args_state:
            pass
        elif ExtendArgsManager.ArgsState.prefix == self._args_state:
            args = tuple(list(self.args) + list(args))
        elif ExtendArgsManager.ArgsState.suffix == self._args_state:
            args = tuple(list(args) + list(self.args))
        elif ExtendArgsManager.ArgsState.manager == self._args_state:
            args = tuple(self.args)
        kwargs.update(self.kwargs)
        return args, kwargs


EArgs = ExtendArgsManager


class ArgsManager(ArgsManagerMixin):
    """
    Usage:
        am = ArgsManager(
            EKwargs({'a': 'hello', 'next': 'world}),
            EKwargs(a='hello', b='world')
        )

    Example:
        class Item(Enum):
            Div = 0
            Button = 1
        
        def html(item, color, size, step=None, length=None, strength=None) -> Any:
            ...
        
        am = ArgsManager(
            EKwargs({'size': 12, 'step': 'one'}),
            EKwargs(color='green', strength=24)
        )
        
        page = list()
        page.append(am(html, Item.Div))
        page.append(am(html, Item.Button))
        # The same as:
        # page = list()
        # page.append(html(Item.Div, 'green', 12, 'one', strength=24))
        # page.append(html(Item.Button, 'green', 12, 'one', strength=24))
    """
    def __init__(self, *args):
        self.managers = list(args)
        self.one_shot_managers = list()
        self.interceptors = list()
        self.one_shot_interceptors = list()
    
    def append(self, manager) -> 'ArgsManager':
        self.managers.append(manager)
        return self
    
    def append_one_shot(self, manager) -> 'ArgsManager':
        self.one_shot_managers.append(manager)
        return self
    
    def add_interceptor(self, interceptor: Callable) -> 'ArgsManager':
        self.interceptors.append(interceptor)
        return self
    
    def add_interceptor_one_shot(self, interceptor: Callable) -> 'ArgsManager':
        self.one_shot_interceptors.append(interceptor)
        return self
    
    def callable(self, entity: EntityWithExtendableArgs) -> Callable:
        def callable_entity(*args, **kwargs) -> Any:
            original_args: Tuple[Tuple, Dict] = (copy.copy(args), copy.copy(kwargs))
            for manager in self.managers:
                args, kwargs = manager(entity, *args, **kwargs)
                
            one_shot_managers_buff = self.one_shot_managers
            self.one_shot_managers = type(one_shot_managers_buff)()
            for manager in one_shot_managers_buff:
                args, kwargs = manager(entity, *args, **kwargs)
            
            resulting_args: Tuple[Tuple, Dict] = (args, kwargs)
            instance = entity(*args, **kwargs)
            
            for interceptor in self.interceptors:
                interceptor(instance, entity, original_args, resulting_args)
            
            one_shot_interceptors_buff = self.one_shot_interceptors
            self.one_shot_interceptors = type(one_shot_interceptors_buff)()
            for interceptor in one_shot_interceptors_buff:
                interceptor(instance, entity, original_args, resulting_args)
            
            return instance
        return callable_entity
    
    def __call__(self, entity: EntityWithExtendableArgs, *args, **kwargs) -> Any:
        original_args: Tuple[Tuple, Dict] = (copy.copy(args), copy.copy(kwargs))
        for manager in self.managers:
            args, kwargs = manager(entity, *args, **kwargs)
            
        one_shot_managers_buff = self.one_shot_managers
        self.one_shot_managers = type(one_shot_managers_buff)()
        for manager in one_shot_managers_buff:
            args, kwargs = manager(entity, *args, **kwargs)
        
        resulting_args: Tuple[Tuple, Dict] = (args, kwargs)
        instance = entity(*args, **kwargs)
        for interceptor in self.interceptors:
            interceptor(instance, entity, original_args, resulting_args)
        
        return instance


def merge_func_args(func_list: Sequence[Callable]) -> Tuple:
    args: List = list()
    default_args: List = list()
    for func in func_list:
        is_method = None
        if inspect.ismethod(func):
            is_method = True
        elif callable(func):
            is_method = False
        else:
            raise RuntimeError(f'Is not callable: {repr(func)}')
        varnames = func.__code__.co_varnames
        if is_method:
            if len(varnames) > 0:
                if 'self' == varnames[0]:
                    varnames = varnames[1:]
        spec = inspect.getfullargspec(func)
        # print(f'ArgSpec:')
        # pprint(spec)
        
        if spec.defaults is None:
            args.extend(varnames)
        else:
            defaults_len = len(spec.defaults)
            args.extend(varnames[:-defaults_len])
            default_args.extend(varnames[-defaults_len:])
    # print(f'Args:')
    # pprint(args)
    # print(f'Default args:')
    # pprint(default_args)
    return args + default_args


def interested_args_to_kwargs(interested_args, args, kwargs):
    kwargs = copy.copy(kwargs)
    absent_args = list()
    for arg in interested_args:
        if arg not in kwargs:
            absent_args.append(arg)
    kwargs.update(zip(absent_args, args))
    return kwargs


def func_args_to_kwargs(func, args, kwargs):
    kwargs = copy.copy(kwargs)
    interested_names = func.__code__.co_varnames
    is_method = None
    if inspect.ismethod(func):
        is_method = True
    elif callable(func):
        is_method = False
    else:
        raise RuntimeError(f'Is not callable: {repr(func)}')
    
    kwargs.update(zip(interested_names, args))
    not_needed_names = set(kwargs) - set(interested_names)
    for name in not_needed_names:
        kwargs.pop(name, None)
    if is_method:
        kwargs.pop('self', None)
    return kwargs


def number_of_provided_args(args, kwargs):
    return len(args) + len(kwargs)
