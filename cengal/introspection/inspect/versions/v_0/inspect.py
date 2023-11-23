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

# __all__ = ['frame', 'get_exception', 'get_exception_tripple', 'exception_to_printable_text', 'is_async', 'is_callable', 'func_param_names', 'frame_param_names', 'intro_func_param_names', 'CodeParamsWithValues', 'intro_func_params_with_values', 'intro_func_all_params_with_values', 'intro_func_all_params_with_values_as_ordered_dict', 'code_params_with_values_to_signature_items_gen', 'code_params_with_values_to_signature']

from typing import Any, Callable, Awaitable, Dict, Generator, List, Optional, Tuple, NamedTuple, OrderedDict as OrderedDictType, Type, Union, Set, Sequence, cast
from types import ModuleType, CodeType, FrameType
import traceback
import inspect
import sys
from cengal.code_flow_control.python_bytecode_manipulator import CodeParamNames, code_param_names, get_code, code_name
from cengal.text_processing.brackets_processing import Bracket, BracketPair, replace_text_with_brackets, find_text_in_brackets
from collections import OrderedDict

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


class WrongDepth(Exception):
    pass


class CanNotRetrieveFrame(Exception):
    pass


def frame(depth: Optional[int] = 1) -> FrameType:
    """
    :param depth: 0 - frame of this function, 1 - frame of the caller function, etc.
    :return:
    """
    depth = depth or 0
    if depth < 0:
        raise WrongDepth(depth)

    result = inspect.currentframe()
    if result is None:
        raise CanNotRetrieveFrame()

    for i in range(depth):
        result = result.f_back

    return result


def get_exception() -> Exception:
    ex_type, ex_value, ex_traceback = sys.exc_info()
    return ex_value.with_traceback(ex_traceback)


def get_exception_tripple() -> Tuple[Type, Exception, Any]:
    return sys.exc_info()


def exception_to_printable_text(exception: Exception) -> str:
    # return ''.join(traceback.format_exception(type(exception), exception, exception.__traceback__))
    return ''.join(traceback.TracebackException.from_exception(exception).format())


def is_async(entity) -> bool:
    return inspect.iscoroutine(entity) or inspect.isgenerator(entity) or inspect.iscoroutinefunction(entity) or inspect.isgeneratorfunction(entity) or inspect.isasyncgen(entity) or inspect.isasyncgenfunction(entity) or inspect.isawaitable(entity)


def is_callable(entity) -> bool:
    return callable(entity)


def func_param_names(func) -> CodeParamNames:
    return code_param_names(get_code(func))


def entity_arguments_description(entity: Callable) -> Tuple[Set[str], Sequence[str], Sequence[str], Sequence[str]]:
    init_code = get_code(entity)
    cpn: CodeParamNames = code_param_names(init_code)
    positional = cpn.positional
    positional_only = cpn.positional_only
    keyword_only = cpn.keyword_only
    all: Set[str] = set(positional) | set(positional_only) | set(keyword_only)
    return all, positional, positional_only, keyword_only


def func_code_name(func):
    code = get_code(func)
    return code_name(code)


def func_name(func):
    try:
        return func.__name__
    except AttributeError:
        return str()


def func_qualname(func):
    try:
        return func.__qualname__
    except AttributeError:
        return str()


def entity_name(entity):
    if isinstance(entity, FrameType):
        entity = entity.f_code
    
    if isinstance(entity, CodeType):
        return code_name(entity)
    else:
        return func_name(entity)


def entity_qualname(entity):
    if isinstance(entity, FrameType):
        entity = entity.f_code
    
    if isinstance(entity, CodeType):
        if sys.version_info >= (3, 11):
            return code_qualname(entity)
        else:
            # raise RuntimeError('CodeType.__qualname__ is available only since Python 3.11')
            entity_instance = find_entity(entity)
            return f'{entity_owner_name(entity_instance)}.{entity_name(entity_instance)}'
    else:
        return func_qualname(entity)


def entity_class(func) -> Optional[Type]:
    if inspect.ismethod(func):
        for func_class in inspect.getmro(func.__self__.__class__):
            if func_class.__dict__.get(func.__name__) is func:
                return func_class
        
        func_of_the_bound_method = func.__func__
        for func_class in inspect.getmro(func.__self__.__class__):
            if func_class.__dict__.get(func.__name__) is func_of_the_bound_method:
                return func_class
        
        func = func_of_the_bound_method
    
    if inspect.isfunction(func):
        try:
            func_class = getattr_ex(inspect.getmodule(func), func.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0])
        except AttributeError:
            return None
        
        if isinstance(func_class, type):
            return func_class
    
    return getattr_ex(func, '__objclass__', None)


def entity_owner(func) -> Optional[Union[Type, ModuleType]]:
    func_module = None
    if inspect.ismethod(func):
        for func_class in inspect.getmro(func.__self__.__class__):
            if func_class.__dict__.get(func.__name__) is func:
                return func_class
        
        func_of_the_bound_method = func.__func__
        for func_class in inspect.getmro(func.__self__.__class__):
            if func_class.__dict__.get(func.__name__) is func_of_the_bound_method:
                return func_class
        
        func = func_of_the_bound_method
        
    if inspect.isfunction(func):
        func_module = inspect.getmodule(func)
        try:
            func_class = getattr_ex(func_module, func.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0])
        except AttributeError:
            return func_module
        
        if isinstance(func_class, type):
            return func_class
        else:
            return func_module
    
    try:
        return getattr_ex(func, '__objclass__')
    except AttributeError:
        if func_module is None:
            func_module = inspect.getmodule(func)
        
        return func_module


module_repr_importable_str_bracket_pair: BracketPair = BracketPair([Bracket("<module '")], [Bracket("' from '")])
module_repr_full_file_path_bracket_pair: BracketPair = BracketPair([Bracket("' from '")], [Bracket("'>")])


def get_module_importable_str_and_path(module) -> Tuple[str, str]:
    if not inspect.ismodule(module):
        raise TypeError(f'Only modules are supported. {type(module)} was provided instead')
    
    module_repr: str = repr(module)
    importable_str = module_repr[find_text_in_brackets(module_repr, module_repr_importable_str_bracket_pair)]
    full_file_path = module_repr[find_text_in_brackets(module_repr, module_repr_full_file_path_bracket_pair)]
    return importable_str, full_file_path


def entity_owning_module_info_and_owning_path(entity) -> Tuple[ModuleType, str, str, List[Union[Type, ModuleType]]]:
    owning_path: List = list()
    module = None
    owner_is_module: bool = False
    while not owner_is_module:
        module = entity_owner(entity)
        owning_path.append(module)
        entity = module
        owner_is_module = inspect.ismodule(module)
    
    module_importable_str, module_file_full_path = get_module_importable_str_and_path(module)
    return module, module_importable_str, module_file_full_path, owning_path


def entity_owning_module_importable_str(entity) -> str:
    _, module_importable_str, _, _ = entity_owning_module_info_and_owning_path(entity)
    return module_importable_str


module_repr_limited_bracket_pair: BracketPair = BracketPair([Bracket(" from '")], [Bracket("'>")])


def normalized_owner_repr(owner: Optional[Union[Type, ModuleType]]) -> str:
    if owner is None:
        return str()
    
    owner_repr: str = repr(owner)
    result, _ = replace_text_with_brackets(owner_repr, module_repr_limited_bracket_pair, ">", 1)
    return result


def normalized_code_owner_repr(code: CodeType, owner: Optional[Union[Type, ModuleType]]) -> str:
    if owner is None:
        return str()
    
    owner_repr: str = repr(owner)
    result, _ = replace_text_with_brackets(owner_repr, module_repr_limited_bracket_pair, f" line {code.co_firstlineno}>", 1)
    return result


def entity_owner_repr(entity):
    if isinstance(entity, FrameType):
        entity = entity.f_code
    
    if isinstance(entity, CodeType):
        return normalized_code_owner_repr(entity, entity_owner(entity))
    else:
        return normalized_owner_repr(entity_owner(entity))


def owner_name(owner: Optional[Union[Type, ModuleType]]) -> str:
    if owner is None:
        return str()
    
    return owner.__name__


def entity_owner_name(entity):
    return owner_name(entity_owner(entity))


def frame_param_names(frame_instance: FrameType) -> CodeParamNames:
    return code_param_names(frame_instance.f_code)


def intro_func_param_names(depth: Optional[int] = 1) -> CodeParamNames:
    return frame_param_names(frame(depth + 1))


CodeParamsWithValues = CodeParamNames
ParamWithValue = Tuple[str, Any]


def fill_code_params_with_values(code_params: CodeParamNames, args, kwargs) -> Tuple[CodeParamsWithValues, Tuple, Dict]:
    positional, positional_only, keyword_only = code_params
    positional_len = len(positional)
    positional_only_len = len(positional_only)
    keyword_only_len = len(keyword_only)
    positional_only_delimiter_place: Optional[int] = None
    if positional_only_len:
        positional_only_delimiter_place = positional_only_len
    
    positional_values = tuple(((arg, args[index]) for index, arg in enumerate(positional)))
    if positional_only_len:
        positional_only_values = tuple(((arg, args[index]) for index, arg in enumerate(positional_only)))
    else:
        positional_only_values = tuple()
    
    if keyword_only_len:
        keyword_only_values = tuple(((arg, kwargs[arg]) for arg in keyword_only))
    else:
        keyword_only_values = tuple()

    result_args: Tuple = args[positional_len:]
    result_kwargs: Dict = {key: value for key, value in kwargs.items() if key not in keyword_only}
    
    return CodeParamsWithValues(positional_values, positional_only_values, keyword_only_values), result_args, result_kwargs


def func_params_with_values(func: Union[Callable, Awaitable], args, kwargs) -> Tuple[CodeParamsWithValues, Tuple, Dict]:
    return fill_code_params_with_values(func_param_names(func), args, kwargs)


def intro_frame_params_with_values(frame_instance) -> CodeParamsWithValues:
    positional, positional_only, keyword_only = frame_param_names(frame_instance)
    fr_locals = frame_instance.f_locals
    return CodeParamsWithValues(tuple(((arg, fr_locals[arg]) for arg in positional)), \
        tuple(((arg, fr_locals[arg]) for arg in positional_only)), \
        tuple(((arg, fr_locals[arg]) for arg in keyword_only)))


def intro_func_params_with_values(depth: Optional[int] = 1) -> CodeParamsWithValues:
    return intro_frame_params_with_values(frame(depth + 1))


def intro_frame_all_params_with_values(frame_instance) -> Tuple[ParamWithValue]:
    positional, _, keyword_only = frame_param_names(frame_instance)
    all_params = positional + keyword_only
    fr_locals = frame_instance.f_locals
    return tuple(((arg, fr_locals[arg]) for arg in all_params))


def intro_func_all_params_with_values(depth: Optional[int] = 1) -> Tuple[ParamWithValue]:
    return intro_frame_all_params_with_values(frame(depth + 1))


def intro_frame_all_params_with_values_as_ordered_dict(frame_instance) -> OrderedDictType[str, Any]:
    return OrderedDict(intro_frame_all_params_with_values(frame_instance))


def intro_func_all_params_with_values_as_ordered_dict(depth: Optional[int] = 1) -> OrderedDictType[str, Any]:
    return intro_frame_all_params_with_values_as_ordered_dict(frame(depth + 1))


def code_params_with_values_to_signature_items_gen(code_params_with_values: CodeParamsWithValues, verbose: bool = False) -> Generator[str, None, None]:
    positional, positional_only, keyword_only = code_params_with_values
    positional_len = len(positional)
    positional_only_len = len(positional_only)
    keyword_only_len = len(keyword_only)
    positional_only_delimiter_place: Optional[int] = None
    if positional_only_len:
        positional_only_delimiter_place = positional_only_len
    
    for index, arg in enumerate(positional):
        arg_name, arg_value = arg
        if (positional_only_delimiter_place is not None) and (index == positional_only_delimiter_place):
            yield '/'
        
        if verbose:
            yield f'{arg_name}={arg_value}'
        else:
            yield str(arg_value)
    
    if keyword_only_len:
        yield '*'
        for arg in keyword_only:
            arg_name, arg_value = arg
            yield f'{arg_name}={arg_value}'


def code_params_to_signature_items_gen(code_params: CodeParamNames) -> Generator[str, None, None]:
    positional, positional_only, keyword_only = code_params
    positional_len = len(positional)
    positional_only_len = len(positional_only)
    keyword_only_len = len(keyword_only)
    positional_only_delimiter_place: Optional[int] = None
    if positional_only_len:
        positional_only_delimiter_place = positional_only_len
    
    for index, arg in enumerate(positional):
        if (positional_only_delimiter_place is not None) and (index == positional_only_delimiter_place):
            yield '/'
        
        # yield arg[0]
        yield arg
    
    if keyword_only_len:
        yield '*'
        for arg in keyword_only:
            # yield arg[0]
            yield arg


def code_params_with_values_to_signature(params_with_values: CodeParamsWithValues, verbose: bool = False) -> str:
    return ', '.join(code_params_with_values_to_signature_items_gen(params_with_values, verbose))


def code_params_to_signature(param_names: CodeParamNames) -> str:
    return ', '.join(code_params_to_signature_items_gen(param_names))


def entity_repr_limited(entity):
    if isinstance(entity, FrameType):
        entity = entity.f_code
    
    if isinstance(entity, CodeType):
        code = entity
    else:
        code = get_code(entity)
    
    func_name = code_name(code)
    param_names = code_param_names(code)
    function_params_str = code_params_to_signature(param_names)
    return f'{func_name}({function_params_str})'


def entity_repr_limited_try_qualname(entity):
    if isinstance(entity, FrameType):
        entity = entity.f_code
    
    if isinstance(entity, CodeType):
        code = entity
        func_name = code_name(code)
    else:
        code = get_code(entity)
        func_name = func_qualname(entity)
    
    param_names = code_param_names(code)
    function_params_str = code_params_to_signature(param_names)
    return f'{func_name}({function_params_str})'


def entity_repr_owner_based(entity):
    if isinstance(entity, FrameType):
        entity = entity.f_code
    
    owner = entity_owner(entity)
    if isinstance(entity, CodeType):
        owner_repr = normalized_code_owner_repr(entity, owner)
    else:
        owner_repr = normalized_owner_repr(owner)

    if isinstance(owner, ModuleType):
        _entity_repr_limited = entity_repr_limited_try_qualname
    else:
        _entity_repr_limited = entity_repr_limited
    
    if owner_repr:
        return f'{owner_repr}.{_entity_repr_limited(entity)}'
    else:
        return _entity_repr_limited(entity)


def entity_repr(entity):
    if isinstance(entity, FrameType):
        entity = entity.f_code
    
    module = inspect.getmodule(entity)
    if isinstance(entity, CodeType):
        owner_repr = normalized_code_owner_repr(entity, module)
    else:
        owner_repr = normalized_owner_repr(module)
    
    if owner_repr:
        return f'{owner_repr}.{entity_repr_limited_try_qualname(entity)}'
    else:
        return entity_repr_limited_try_qualname(entity)


def entity_properties(entity) -> Set[str]:
    """
    Example:
        from cengal.parallel_execution.coroutines.coro_standard_services.wait_coro import WaitCoroRequest
        from cengal.introspection.inspect import entity_properties
        
        print(entity_properties(WaitCoroRequest))
        >> {'__weakref__', 'put_list', 'fastest', 'atomic', 'list', 'single', 'put_fastest', '_save', 'put_single', 'put_atomic'}


        print(entity_properties(WaitCoroRequest()))
        >> {'result_required', 'args', 'tree', 'kill_on_timeout', 'timeout', 'request_type', 'kwargs', 'provide_to_request_handler'}


        def my_func(a, b, *, c, d):
            return a + b + c + d

        my_func.my_property = 2

        print(entity_properties(my_func))
        >> {'my_property'}


    Args:
        entity (_type_): _description_

    Returns:
        Set[str]: _description_
    """    
    entity_type_items = set(dir(type(entity)))
    entity_items = set(dir(entity))
    return entity_items - entity_type_items


def class_properties(entity: Type) -> Set[str]:
    """
    Example:

    Args:
        entity (_type_): _description_

    Returns:
        Set[str]: _description_
    """    
    entity_type_items = set(dir(type(entity)))
    entity_items = set(dir(entity))
    mro = inspect.getmro(entity)
    base_members: Set = set()
    for base in mro:
        if base is entity:
            continue
        
        base_members |= set(dir(base))
    
    return (entity_items - entity_type_items) - base_members


def class_properties_including_overrided(entity: Type) -> Set[str]:
    """
    Example:

    Args:
        entity (_type_): _description_

    Returns:
        Set[str]: _description_
    """    
    entity_type_items = set(dir(type(entity)))
    entity_items = set(entity.__dict__.keys())
    return entity_items - entity_type_items


def intro_frame_repr_limited(frame_instance, verbose: bool = False):
    func_name = code_name(frame_instance.f_code)
    params_with_values = intro_frame_params_with_values(frame_instance)
    function_params_str = code_params_with_values_to_signature(params_with_values, verbose)
    return f'{func_name}({function_params_str})'


def intro_frame_repr(frame_instance, verbose: bool = False):
    code = frame_instance.f_code
    func_name = code_name(code)
    module = inspect.getmodule(code)
    owner_repr = normalized_code_owner_repr(code, module)
    params_with_values = intro_frame_params_with_values(frame_instance)
    function_params_str = code_params_with_values_to_signature(params_with_values, verbose)
    return f'{owner_repr}.{func_name}({function_params_str})'


def intro_func_repr_limited(verbose: bool = False, depth: Optional[int] = 1):
    return intro_frame_repr_limited(frame(depth + 1), verbose)


def print_intro_func_repr_limited(verbose: bool = False, depth: Optional[int] = 1):
    print(intro_func_repr_limited(verbose, depth + 1))


pifrl = print_intro_func_repr_limited


def intro_func_repr(verbose: bool = False, depth: Optional[int] = 1):
    return intro_frame_repr(frame(depth + 1), verbose)


def print_intro_func_repr(verbose: bool = False, depth: Optional[int] = 1):
    print(intro_func_repr(verbose, depth + 1))


pifr = print_intro_func_repr


def get_str_of_data_info(data):
    return f'type: {type(data)}; value: {data}'


gsodi = get_str_of_data_info


def print_data_info(data):
    print(get_str_of_data_info(data))


pdi = print_data_info


def get_str_of_data_info_named(name, data):
    return f'<<{name}>> type: {type(data)}; value: {data}'


gsodin = get_str_of_data_info_named


def print_data_info_named(name, data):
    print(get_str_of_data_info_named(name, data))


pdin = print_data_info_named


def get_str_of_data_info_by_name(name, depth: Optional[int] = 1):
    fr = frame(depth + 1)
    data = fr.f_locals[name]
    return get_str_of_data_info_named(name, data)


gsodibn = get_str_of_data_info_by_name


def print_data_info_by_name(name, depth: Optional[int] = 1):
    print(get_str_of_data_info_by_name(name, depth + 1))


pdibn = print_data_info_by_name


def is_descriptor(entity):
    return hasattr(entity, '__get__') or hasattr(entity, '__set__') or hasattr(entity, '__delete__')


def is_filled_descriptor(owning_object, entity):
    """
        class _foo:
        __slots__ = ['foo', 'bar']

        def __init__(self):
            self.bar = 2

    'foo' - not filled
    'bar' - filled

    Args:
        owning_object (_type_): _description_
        entity (_type_): _description_

    Returns:
        _type_: _description_
    """    
    try:
        entity.__get__(owning_object)
    except AttributeError:
        return False
    
    return True


def filled_slots_names(owning_object):
    try:
        slots_names = owning_object.__slots__
    except AttributeError:
        return None
    
    result = list()
    for slot_name in slots_names:
        slot = inspect.getattr_static(owning_object, slot_name)
        if is_filled_descriptor(owning_object, slot):
            result.append(slot_name)
    
    return result


def filled_slots(owning_object):
    try:
        slots_names = owning_object.__slots__
    except AttributeError:
        return None
    
    result = list()
    for slot_name in slots_names:
        slot = inspect.getattr_static(owning_object, slot_name)
        if is_filled_descriptor(owning_object, slot):
            result.append(slot)
    
    return result


def filled_slots_with_names(owning_object):
    try:
        slots_names = owning_object.__slots__
    except AttributeError:
        return None
    
    result = list()
    for slot_name in slots_names:
        slot = inspect.getattr_static(owning_object, slot_name)
        if is_filled_descriptor(owning_object, slot):
            result.append((slot_name, slot))
    
    return result


def current_entity_name(depth: Optional[int] = 1):
    fr = frame(depth + 1)
    return entity_name(fr)
    # entity_name = code_name(fr.f_code)
    # # print(dir(fr.f_code))
    # # print(fr.f_code.__class__)
    # # print(dir(fr))
    # # print(fr.__class__)
    # return entity_name


cen = current_entity_name


def current_entity_owner_name(depth: Optional[int] = 1):
    fr = frame(depth + 1)
    return owner_name(entity_owner(fr.f_code))


# def current_entity_full_name(depth: Optional[int] = 1):
#     fr = frame(depth + 1)
#     entity_name = code_name(fr.f_code)
#     return entity_name


# cefn = current_entity_full_name


def getattr_ex(entity, attr_name: str) -> Any:
    try:
        return getattr(entity, attr_name)
    except AttributeError:  # See code of the `inspect.getmembers()`
        if attr_name in entity.__dict__:
            return entity.__dict__[attr_name]
        else:
            raise AttributeError(f'Attribute "{attr_name}" was not found in the entity "{entity}"')


def entity_is_function(entity) -> bool:
    owner: Optional[Union[Type, ModuleType]] = entity_owner(entity)
    if owner is None:
        return False
    
    if inspect.ismodule(owner):
        entity_name_str: str = entity_name(entity)
        if hasattr(owner, entity_name_str):
            possible_entity = getattr_ex(owner, entity_name_str)
            possible_entity_code = get_code(possible_entity)
            entity_code = get_code(entity)
            if possible_entity_code is entity_code:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def get_function_by_entity(entity) -> Optional[Callable]:
    owner: Optional[Union[Type, ModuleType]] = entity_owner(entity)
    if owner is None:
        return None
    
    if inspect.ismodule(owner):
        entity_name_str: str = entity_name(entity)
        if hasattr(owner, entity_name_str):
            possible_entity = getattr_ex(owner, entity_name_str)
            possible_entity_code = get_code(possible_entity)
            entity_code = get_code(entity)
            if possible_entity_code is entity_code:
                return possible_entity
            else:
                return None
        else:
            return None
    else:
        return None


def entity_is_method(entity) -> bool:
    owner: Optional[Union[Type, ModuleType]] = entity_owner(entity)
    if owner is None:
        return False
    
    if inspect.isclass(owner):
        entity_name_str: str = entity_name(entity)
        if hasattr(owner, entity_name_str):
            possible_entity = getattr_ex(owner, entity_name_str)
            possible_entity_code = get_code(possible_entity)
            entity_code = get_code(entity)
            if possible_entity_code is entity_code:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def get_method_by_entity(entity) -> Optional[Callable]:
    owner: Optional[Union[Type, ModuleType]] = entity_owner(entity)
    if owner is None:
        return None
    
    if inspect.isclass(owner):
        entity_name_str: str = entity_name(entity)
        if hasattr(owner, entity_name_str):
            possible_entity = getattr_ex(owner, entity_name_str)
            possible_entity_code = get_code(possible_entity)
            entity_code = get_code(entity)
            if possible_entity_code is entity_code:
                return possible_entity
            else:
                return None
        else:
            return None
    else:
        return None


def entity_is_unbound_method(entity):
    owner: Optional[Union[Type, ModuleType]] = entity_owner(entity)
    if owner is None:
        return False
    
    if inspect.ismodule(owner):
        entity_name_str: str = entity_name(entity)
        if hasattr(owner, entity_name_str):
            possible_entity = getattr_ex(owner, entity_name_str)
            possible_entity_code = get_code(possible_entity)
            entity_code = get_code(entity)
            if possible_entity_code is entity_code:
                return False
            else:
                return True
        else:
            return True
    else:
        return False


def get_unbound_method_by_entity(entity) -> Optional[Callable]:
    raise NotImplementedError()


class AnAppropriateOwnerParameterWasNotFoundError(Exception):
    pass


class PossibleOwnerParameterDoesNotMatchError(AnAppropriateOwnerParameterWasNotFoundError):
    pass


class EntityHasNoPositionalParametersError(AnAppropriateOwnerParameterWasNotFoundError):
    pass


def get_owner_parameter(entity, owner_parameter_name: str, return_even_if_not_match: bool = False):
    if entity_is_function(entity):
        raise TypeError(f'Function has no {owner_parameter_name} parameter')
    
    if entity_is_method(entity):
        return entity.__self__
    elif entity_is_unbound_method(entity):
        if isinstance(entity, FrameType):
            entity_name_str: str = entity_name(entity)
            params_with_values: CodeParamsWithValues = intro_frame_params_with_values(entity)
            positional, positional_only, keyword_only = params_with_values
            if positional:
                possible_positional_self = positional[0][1]
            elif positional_only:
                possible_positional_self = positional_only[0][1]
            else:
                raise EntityHasNoPositionalParametersError
            
            if hasattr(possible_positional_self, entity_name_str):
                possible_entity = getattr_ex(possible_positional_self, entity_name_str)
                possible_entity_code = get_code(possible_entity)
                entity_code = get_code(entity)
                if possible_entity_code is entity_code:
                    return possible_positional_self
                else:
                    if return_even_if_not_match:
                        return possible_positional_self
                    else:
                        raise PossibleOwnerParameterDoesNotMatchError
            
            raise AnAppropriateOwnerParameterWasNotFoundError(f'Can not find an appropriate {owner_parameter_name} parameter in {entity}')
    else:
        raise TypeError(f'{entity} of type {type(entity)} is not supported')


def get_self_parameter(entity):
    return get_owner_parameter(entity, 'self')


def get_cls_parameter(entity):
    return get_owner_parameter(entity, 'cls')


def get_any_owner_parameter(entity, owner_parameter_name: str, any_positional: bool = True, any_keyword: bool = True):
    if entity_is_function(entity):
        raise TypeError(f'Function has no {owner_parameter_name} parameter')
    
    if entity_is_method(entity):
        return entity.__self__
    elif entity_is_unbound_method(entity):
        if isinstance(entity, FrameType):
            entity_name_str: str = entity_name(entity)
            params_with_values: CodeParamsWithValues = intro_frame_params_with_values(entity)
            positional, positional_only, keyword_only = params_with_values
            
            if any_positional:
                all_positional = positional + positional_only
                for param in all_positional:
                    possible_positional_self_name, possible_positional_self = param
                    if hasattr(possible_positional_self, entity_name_str):
                        possible_entity = getattr_ex(possible_positional_self, entity_name_str)
                        possible_entity_code = get_code(possible_entity)
                        entity_code = get_code(entity)
                        if possible_entity_code is entity_code:
                            return possible_positional_self
            else:
                if positional:
                    possible_positional_self = positional[0][1]
                elif positional_only:
                    possible_positional_self = positional_only[0][1]
                
                if hasattr(possible_positional_self, entity_name_str):
                    possible_entity = getattr_ex(possible_positional_self, entity_name_str)
                    possible_entity_code = get_code(possible_entity)
                    entity_code = get_code(entity)
                    if possible_entity_code is entity_code:
                        return possible_positional_self
            
            if any_keyword:
                for possible_keyword_self_name, possible_keyword_self in keyword_only:
                    if hasattr(possible_keyword_self, entity_name_str):
                        possible_entity = getattr_ex(possible_keyword_self, entity_name_str)
                        possible_entity_code = get_code(possible_entity)
                        entity_code = get_code(entity)
                        if possible_entity_code is entity_code:
                            return possible_keyword_self
            else:
                keyword_only_dict: Dict[str, Any] = dict(keyword_only)
                if owner_parameter_name in keyword_only_dict:
                    possible_keyword_self = keyword_only_dict[owner_parameter_name]
                    if hasattr(possible_keyword_self, entity_name_str):
                        possible_entity = getattr_ex(possible_keyword_self, entity_name_str)
                        possible_entity_code = get_code(possible_entity)
                        entity_code = get_code(entity)
                        if possible_entity_code is entity_code:
                            return possible_keyword_self
            
            raise AnAppropriateOwnerParameterWasNotFoundError(f'Can not find {owner_parameter_name} parameter in {entity}')


def get_any_self_parameter(entity, any_positional: bool = True, any_keyword: bool = True):
    return get_owner_parameter(entity, 'self', any_positional, any_keyword)


def get_any_cls_parameter(entity, any_positional: bool = True, any_keyword: bool = True):
    return get_owner_parameter(entity, 'cls' , any_positional, any_keyword)


def find_method_in_module_by_code(module, code_to_find: CodeType) -> Optional[CodeType]:
    for entity_name_str in dir(module):
        entity = getattr_ex(module, entity_name_str)
        if inspect.isclass(entity):
            possible_method = find_method_in_class_by_code(entity, code_to_find)
            if possible_method is not None:
                return possible_method
    
    return None


def find_method_in_class_by_code(class_to_search_in, code_to_find: CodeType) -> Optional[CodeType]:
    subclassess = list()
    for entity_name_str in class_properties_including_overrided(class_to_search_in):
        entity = getattr_ex(class_to_search_in, entity_name_str)
        if inspect.isclass(entity):
            subclassess.append(entity)
        elif inspect.isfunction(entity) or inspect.ismethod(entity):
            if get_code(entity) is code_to_find:
                return entity
        
    for subclass in subclassess:
        possible_method = find_method_in_class_by_code(subclass, code_to_find)
        if possible_method is not None:
            return possible_method
    
    return None


class EntityWasNotFoundError(Exception):
    pass


def find_entity(entity: Union[Callable, FrameType, CodeType]) -> Callable:
    if not (inspect.isfunction(entity) or inspect.ismethod(entity) or isinstance(entity, FrameType) or isinstance(entity, CodeType)):
        raise TypeError(f'Only functions, methods, frames and codes are supported. {type(entity)} was provided instead')
    
    result = get_function_by_entity(entity)
    if result is not None:
        return result
    
    result = get_method_by_entity(entity)
    if result is not None:
        return result
    
    entity_name_str: str = entity_name(entity)
    entity_instance: Callable = None
    if isinstance(entity, FrameType):
        owner = None
        need_to_try_clr: bool = False
        try:
            owner = get_self_parameter(entity)
        except AnAppropriateOwnerParameterWasNotFoundError:
            need_to_try_clr = True
        
        if need_to_try_clr:
            try:
                owner = get_cls_parameter(entity)
            except AnAppropriateOwnerParameterWasNotFoundError:
                pass
        
        entity_code = entity.f_code
        if owner is not None:
            entity_instance = getattr_ex(owner, entity_name_str)
            if get_code(entity_instance) is entity_code:
                return entity_instance
        
        entity = entity_code
    
    if isinstance(entity, CodeType):
        entity_owner_instance = entity_owner(entity)
        entity_instance = find_method_in_module_by_code(entity_owner_instance, entity)
        if entity_instance is not None:
            return entity_instance
    
    raise EntityWasNotFoundError


def find_current_entity(depth: Optional[int] = 1) -> Callable:
    return find_entity(frame(depth + 1))
