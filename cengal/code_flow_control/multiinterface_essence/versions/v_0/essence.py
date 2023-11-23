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
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from inspect import isclass
from cengal.introspection.inspect import get_exception
from cengal.code_flow_control.args_manager import EntityArgsHolder
from typing import Any, Callable, NoReturn, Set, Dict, Type, TypeVar, Generic, Optional, Union, Sequence
# from enum import Enum


class EssenceModelException(Exception):
    pass


class IncompatibleEssenceModelError(RuntimeError, EssenceModelException):
    # Must be raised by constructor of EssenceInterface class if incompatible essence_model was given
    pass


class UnsuitableEssenceInterfaceError(RuntimeError, EssenceModelException):
    pass


class EssenceInterfaceIsNotApplicableError(UnsuitableEssenceInterfaceError, EssenceModelException):
    # Must be raised by EssenceModel.__call__ when requested EssenceInterface is not active (applicable)
    pass


class EssenceInterfaceIsNotRegisteredError(UnsuitableEssenceInterfaceError, EssenceModelException):
    # Must be raised by EssenceModel.__call__ when requested EssenceInterface is not registered
    pass


class EssenceModelCanNotInjectSelfError(RuntimeError, EssenceModelException):
    # Must be raised by EssenceModel.emi_inject_model when an object of a class A(EssenceModel) tries
    #   to inject class A - type(self)
    # This behavior is restricted since it may lead to: 
    #   - endless recursion;
    #   - interface collisions when high order model will include several instances of the same interface class.
    pass


class EssenceModelCanNotBeInjectedError(RuntimeError, EssenceModelException):
    # Must be raised by EssenceModel.emi_inject_model if injectable model can not be injected (incompatible)
    pass


class EssenceModelIsNotInjectedError(RuntimeError, EssenceModelException):
    # Must be raised by EssenceModel.emi_injected_model if not injected model was requested
    pass


class IncompatibleHighOrderEssenceModelError(RuntimeError, EssenceModelException):
    # Must be raised by EssenceModel.emu_behave_as_unknown_model method if incompatible on attempt to inject it to
    # incompatible high order model
    pass


class UnknownEssenceModeBehaviorWasNotImplementedProperlyError(NotImplementedError, EssenceModelException):
    pass


class EssenceModelInheritanceAbstract:
    def __call__(self, interface_class: Type['EssenceInterface'], worker: Optional[Callable] = None, failed_worker: Optional[Callable] = None, *args, **kwargs) -> Any:
        raise NotImplementedError

    def em_interface(self, interface_class: Type['EssenceInterface']) -> 'EssenceInterface':
        raise NotImplementedError

    def em_has_interface(self, interface_class: Type['EssenceInterface']) -> bool:
        raise NotImplementedError

    def em_interface_active(self, interface_class: Type['EssenceInterface']) -> bool:
        raise NotImplementedError

    def em_active_interfaces(self) -> Set[Type['EssenceInterface']]:
        raise NotImplementedError

    def em_all_interfaces(self) -> Set[Type['EssenceInterface']]:
        raise NotImplementedError

    def _em_check_applicability_of_interfaces(self) -> NoReturn:
        raise NotImplementedError

    def em_on_model_updated(self, interface_class: Type['EssenceInterface'], *args, **kwargs):
        raise NotImplementedError

    def em_add_interface(self, interface_class: Type['EssenceInterface'], *args, **kwargs) -> bool:
        raise NotImplementedError

    def em_remove_interface(self, interface_class: Type['EssenceInterface']) -> bool:
        raise NotImplementedError


class EssenceModelInjectionAbstract:
    def emi_on_registered_in_high_order_model(self, high_order_model: 'EssenceModelInjectionAbstract'):
        raise NotImplementedError

    def emi_on_unregistering_from_high_order_model(self):
        raise NotImplementedError

    def _emi_notify_high_order_model_about_self_update(self, *args, **kwargs):
        raise NotImplementedError

    def emi_inject_model(self, essence_model: 'EssenceModelInjectionAbstract') -> bool:
        raise NotImplementedError

    def emi_injected_models(self):
        raise NotImplementedError

    def emi_injected_model(self, essence_model_class: Type['EssenceModelInjectionAbstract']):
        raise NotImplementedError

    def emi_on_injected_model_updated(
            self, essence_model_class: Type['EssenceModelInjectionAbstract'], *args, **kwargs):
        raise NotImplementedError

    def emi_remove_injected_model(self, essence_model_class: Type['EssenceModelInjectionAbstract']):
        raise NotImplementedError


class EssenceModelUnknownInjectionAbstract:
    def emu_is_compatible_high_order_model(self, high_order_model_class: Type['EssenceModelInjectionAbstract']) -> bool:
        raise NotImplementedError
    
    def emu_behave_as_unknown_model(self):
        raise NotImplementedError

    def emu_on_behave_as_unknown_model(self):
        raise NotImplementedError

    def _emu_register_on_model_changed_callback(self, requester: 'EssenceModelUnknownInjectionAbstract'):
        raise NotImplementedError

    def _emu_deregister_on_model_changed_callback(self, requester: 'EssenceModelUnknownInjectionAbstract'):
        raise NotImplementedError
    
    def _emu_notify_unknown_models_about_self_update(self):
        raise NotImplementedError

    def emu_on_model_changed_callback(self):
        raise NotImplementedError

    def emu_is_in_unknown_model_behavior(self):
        raise NotImplementedError


class EssenceModel(EssenceModelInheritanceAbstract, EssenceModelInjectionAbstract, EssenceModelUnknownInjectionAbstract):
    # Must contain related data in a consistent state.
    #
    # In order to do this, you must reload em_on_model_updated() and emi_on_injected_model_updated() methods.
    # Your interfaces can provide some appropriate information though an additional parameters of em_on_model_updated()
    # and emi_on_injected_model_updated() methods.
    #
    # Do not forget to:
    #   - run `self._emi_notify_high_order_model_about_self_update(type(self), interface_class, *args, **kwargs)` at
    #       the end of your em_on_model_updated()
    #   - run `self._emi_notify_high_order_model_about_self_update(type(self), essence_model_class, *args, **kwargs)` at
    #       the end of your emi_on_injected_model_updated()

    emi_compatible_injectable_essence_model_classes: Set[Type['EssenceModel']] = set()
    # emu_compatible_high_order_essence_model_class: Optional[Type['EssenceModel']] = None
    emu_compatible_high_order_essence_model_classes: Set[Type['EssenceModel']] = set()

    def __init__(self):
        self.__em_interfaces: Dict[Type['EssenceInterface'], 'EssenceInterface'] = dict()
        self.__em_possible_interfaces: Dict[Type['EssenceInterface'], 'EssenceInterface'] = dict()
        self.__emi_injected_models: Dict[Type['EssenceModel'], 'EssenceModel'] = dict()
        self.__emi_raise_on_uninjectable_model: bool = True
        self.__emi_high_order_model: Optional['EssenceModel'] = None
        self.__emu_in_unknown_model_behavior: bool = False
        self.__emu_raise_on_incompatible_high_order_model: bool = True
        self.__emu_unknown_injected_models: Dict[Type['EssenceModel'], 'EssenceModel'] = dict()

    def em_interface(self, interface_class: Type['EssenceInterface']) -> 'EssenceInterface':
        # Should be called in order to get needed model interface
        if interface_class in self.__em_interfaces:
            return self.__em_interfaces[interface_class]
        else:
            injected_model_interface = None
            for injected_model_class, injected_model in self.__emi_injected_models.items():
                model: 'EssenceModel' = injected_model
                if model.em_interface_active(interface_class):
                    injected_model_interface = model.em_interface(interface_class)
                    break
            if injected_model_interface:
                return injected_model_interface
            elif interface_class in self.__em_possible_interfaces:
                raise EssenceInterfaceIsNotApplicableError
            else:
                raise EssenceInterfaceIsNotRegisteredError

    def __call__(self, interface_class: Type['EssenceInterface'], worker: Callable, failed_worker: Optional[Callable] = None, *args, **kwargs) -> Any:
        interface = None
        exception = None
        try:
            interface = self.em_interface(interface_class)
        except (EssenceInterfaceIsNotApplicableError, EssenceInterfaceIsNotRegisteredError) as exc:
            exception = get_exception()
        
        if interface:
            return worker(interface, *args, **kwargs)
        else:
            if failed_worker:
                return failed_worker(interface, exception, *args, **kwargs)
            else:
                return None
    
    def em_has_interface(self, interface_class: Type['EssenceInterface']) -> bool:
        has_own_interface = (interface_class in self.__em_interfaces) or \
                            (interface_class in self.__em_possible_interfaces)
        one_of_injected_models_has_interface = False
        for injected_model_class, injected_model in self.__emi_injected_models.items():
            model: 'EssenceModel' = injected_model
            if model.em_has_interface(interface_class) or model.em_interface_active(interface_class):
                one_of_injected_models_has_interface = True
                break
        return has_own_interface or one_of_injected_models_has_interface

    def em_interface_active(self, interface_class: Type['EssenceInterface']) -> bool:
        own_interface_active = interface_class in self.__em_interfaces
        one_of_injected_models_has_active_interface = False
        for injected_model_class, injected_model in self.__emi_injected_models.items():
            model: 'EssenceModel' = injected_model
            if model.em_interface_active(interface_class):
                one_of_injected_models_has_active_interface = True
                break
        return own_interface_active or one_of_injected_models_has_active_interface

    def em_active_interfaces(self) -> Set[Type['EssenceInterface']]:
        own_active_interfaces = set(self.__em_interfaces)
        injected_models_active_interfaces: Set[Type['EssenceInterface']] = set()
        for injected_model_class, injected_model in self.__emi_injected_models.items():
            model: 'EssenceModel' = injected_model
            injected_models_active_interfaces.update(model.em_active_interfaces())
        return own_active_interfaces | injected_models_active_interfaces

    def em_all_interfaces(self) -> Set[Type['EssenceInterface']]:
        own_all_interfaces = set(self.__em_interfaces) | set(self.__em_possible_interfaces)
        injected_models_all_interfaces: Set[Type['EssenceInterface']] = set()
        for injected_model_class, injected_model in self.__emi_injected_models.items():
            model: 'EssenceModel' = injected_model
            injected_models_all_interfaces.update(model.em_all_interfaces())
        return own_all_interfaces | injected_models_all_interfaces

    def _em_check_applicability_of_interfaces(self) -> NoReturn:
        new_interfaces = dict()
        new_possible_interfaces = dict()

        for interface_class, interface in self.__em_interfaces.items():
            if interface._applicable_impl():
                new_interfaces[interface_class] = interface
            else:
                new_possible_interfaces[interface_class] = interface

        for interface_class, interface in self.__em_possible_interfaces.items():
            if interface._applicable_impl():
                new_interfaces[interface_class] = interface
            else:
                new_possible_interfaces[interface_class] = interface

        self.__em_interfaces = new_interfaces
        self.__em_possible_interfaces = new_possible_interfaces

    def em_on_model_updated(self, interface_class: Type['EssenceInterface'], *args, **kwargs):
        # Must be run by EssenceInterface (by running EssenceInterface.notify_model_about_change method) after changing
        #   model's data. It is enough to run in once per a method - at the end of the method work.
        # In 'super' in method of inherit class should be run at the end of the method
        self._em_check_applicability_of_interfaces()
        self._emu_notify_unknown_models_about_self_update()
        self._emi_notify_high_order_model_about_self_update(type(self), interface_class, *args, **kwargs)

    def em_add_interface(self, interface_class: Type['EssenceInterface'], *args, **kwargs) -> bool:
        if (interface_class in self.__em_interfaces) or (interface_class in self.__em_possible_interfaces):
            return False
        else:
            interface = interface_class(self, *args, **kwargs)
            if interface._applicable_impl():
                self.__em_interfaces[interface_class] = interface
            else:
                self.__em_possible_interfaces[interface_class] = interface
            return True

    def em_remove_interface(self, interface_class: Type['EssenceInterface']) -> bool:
        if interface_class in self.__em_interfaces:
            del self.__em_interfaces[interface_class]
            return True
        elif interface_class in self.__em_possible_interfaces:
            del self.__em_possible_interfaces[interface_class]
            return True
        else:
            return False

    def emi_on_registered_in_high_order_model(self, high_order_model: 'EssenceModel'):
        # Will be called after high order model successfully registered this mode
        self.__emi_high_order_model = high_order_model

    def emi_on_unregistering_from_high_order_model(self):
        # Will be called before high order model actually unregistered this mode
        self.__emi_high_order_model = None
        self.__emu_in_unknown_model_behavior = False

    def emi_inject_model(self, essence_model: 'EssenceModel'):
        # Should use 'EssenceModel' instead of Type['EssenceModel'] since we should use result of fully constructed
        #   essence_model with all needed interfaces - result of an appropriate factory work
        essence_model_class = type(essence_model)
        if isinstance(essence_model, type(self)) or isinstance(self, essence_model_class):
            raise EssenceModelCanNotInjectSelfError
        
        injectable_model = False
        if essence_model_class in self.emi_compatible_injectable_essence_model_classes:
            injectable_model = True
        else:
            if essence_model.emu_is_compatible_high_order_model(type(self)):
                injectable_model = True
            else:
                if self.__emu_raise_on_incompatible_high_order_model:
                    raise IncompatibleHighOrderEssenceModelError
        
        injected = False
        if injectable_model:
            self.__emi_injected_models[essence_model_class] = essence_model
            essence_model.emi_on_registered_in_high_order_model(self)
            if essence_model_class not in self.emi_compatible_injectable_essence_model_classes:
                essence_model.emu_behave_as_unknown_model()
            
            injected = True
        else:
            if self.__emi_raise_on_uninjectable_model:
                raise EssenceModelCanNotBeInjectedError
            
        return injected

    def emi_injected_models(self):
        return set(self.__emi_injected_models)

    def emi_injected_model(self, essence_model_class: Type['EssenceModel']):
        if essence_model_class in self.__emi_injected_models:
            return self.__emi_injected_models[essence_model_class]
        else:
            raise EssenceModelIsNotInjectedError

    def emi_on_injected_model_updated(self, essence_model_class: Type['EssenceModel'], *args, **kwargs):
        # In 'super' in method of inherit class should be run at the end of the method
        # With deep injection it will be like (model_3, model_2, model_1, interface_1, arg_1, arg_2, arg_3)
        #   where `interface_1` is an interface of the `model_1`
        self._em_check_applicability_of_interfaces()
        self._emu_notify_unknown_models_about_self_update()
        self._emi_notify_high_order_model_about_self_update(type(self), essence_model_class, *args, **kwargs)

    def _emi_notify_high_order_model_about_self_update(self, *args, **kwargs):
        if self.__emi_high_order_model and (not self.__emu_in_unknown_model_behavior):
            high_order_model: 'EssenceModel' = self.__emi_high_order_model
            high_order_model.emi_on_injected_model_updated(*args, **kwargs)

    def emi_remove_injected_model(self, essence_model_class: Type['EssenceModel']):
        injected_model: 'EssenceModel' = self.__emi_injected_models[essence_model_class]
        self._emu_deregister_on_model_changed_callback(injected_model)
        injected_model.emi_on_unregistering_from_high_order_model()
        del self.__emi_injected_models[essence_model_class]

    def emu_is_compatible_high_order_model(self, high_order_model_class: Type['EssenceModelInjectionAbstract']) -> bool:
        """Might be overloaded in order to make this model compatible with more than one high order models

        Args:
            high_order_model_class (Type[): [description]

        Returns:
            bool: [description]
        """
        # return high_order_model_class == self.emu_compatible_high_order_essence_model_class
        return high_order_model_class in self.emu_compatible_high_order_essence_model_classes

    def emu_behave_as_unknown_model(self):
        # Should be called by a high order model for an unknown injected model
        # if type(self.__emi_high_order_model) != self.emu_compatible_high_order_essence_model_class:
        if not self.emu_is_compatible_high_order_model(self.__emi_high_order_model):
            raise IncompatibleHighOrderEssenceModelError
        self.__emi_high_order_model._emu_register_on_model_changed_callback(type(self))
        self.__emu_in_unknown_model_behavior = True
        self.emu_on_behave_as_unknown_model()

    def emu_on_behave_as_unknown_model(self):
        pass

    def _emu_register_on_model_changed_callback(self, requester: 'EssenceModelUnknownInjectionAbstract'):
        self.__emu_unknown_injected_models[type[requester]] = requester

    def _emu_deregister_on_model_changed_callback(self, requester: 'EssenceModelUnknownInjectionAbstract'):
        model_type = type(requester)
        if model_type in self.__emu_unknown_injected_models:
            del self.__emu_unknown_injected_models[model_type]

    def _emu_notify_unknown_models_about_self_update(self, *args, **kwargs):
        for umodel in self.__emu_unknown_injected_models.values():
            unknown_model: 'EssenceModel' = umodel
            unknown_model.emu_on_model_changed_callback()

    def emu_on_model_changed_callback(self):
        raise UnknownEssenceModeBehaviorWasNotImplementedProperlyError

    def emu_is_in_unknown_model_behavior(self):
        return self.__emu_in_unknown_model_behavior


Model = TypeVar('Model', bound=EssenceModel)


class EssenceInterface(Generic[Model]):
    essence_model_class: Type[Model] = EssenceModel

    def __init__(self, essence_model: Model, *args, **kwargs):
        self.essence_model: Model = essence_model
        self._on_applicability_changed_handlers: Set[Callable] = set()
        self._applicability_state: bool = None
        self.__check_essence_mode_type()

    def __check_essence_mode_type(self):
        if not isinstance(self.essence_model, self.essence_model_class):
            raise IncompatibleEssenceModelError

    def applicable(self) -> bool:
        return True

    def _applicable_impl(self) -> bool:
        result: bool = self.applicable()
        if result != self._applicability_state:
            self._applicability_state = result
            for handler in self._on_applicability_changed_handlers:
                handler(self)
        
        return result
    
    def add_on_applicability_changed_handler(self, handler: Callable):
        self._on_applicability_changed_handlers.add(handler)
    
    def discard_on_applicability_changed_handler(self, handler: Callable):
        self._on_applicability_changed_handlers.discard(handler)

    def notify_model_about_change(self, *args, **kwargs):
        # Must be run by EssenceInterface's methods if and after changing model's data. It is enough to run in once per
        #   a method - at the end of the method work.
        self.essence_model.em_on_model_updated(type(self), *args, **kwargs)


def essence_model_changer(func):
    def wrapper(self: EssenceInterface, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        finally:
            self.notify_model_about_change(*args, **kwargs)

    return wrapper


em_changer = essence_model_changer


class EssenceModelFactoryExample:
    def __call__(self, *args, **kwargs):
        model: EssenceModel = EssenceModel()
        model.em_add_interface(EssenceInterface)
        return model


def simple_essence_model_factory(
        model: Union[Type[EssenceModel], EntityArgsHolder], 
        interfaces: Union[
                Type[EssenceInterface], 
                EntityArgsHolder, 
                Sequence[Union[Type[EssenceInterface], EntityArgsHolder]]
            ]
    ) -> EssenceModel:
    model_instance: EssenceModel = model()
    if isinstance(interfaces, EntityArgsHolder) or (isinstance(interfaces, type) and issubclass(interfaces, EssenceInterface)):
        interfaces = (interfaces,)
    
    for interface in interfaces:
        if isinstance(interface, type):
            if issubclass(interface, EssenceInterface):
                model_instance.em_add_interface(interface)
        elif isinstance(interface, EntityArgsHolder):
            model_instance.em_add_interface(*interface.entity_args_kwargs())
        else:
            raise TypeError(f'Wrong interface type: {type(interface)}')

    return model_instance


simple_em_factory = simple_essence_model_factory
