from typing import NoReturn, Set, Dict, Type, TypeVar, Generic, Optional
# from enum import Enum


class IncompatibleEssenceModel(RuntimeError):
    # Must be raised by constructor of EssenceInterface class if incompatible essence_model was given
    pass


class EssenceInterfaceIsNotApplicable(RuntimeError):
    # Must be raised by EssenceModel.__call__ when requested EssenceInterface is not active (applicable)
    pass


class EssenceInterfaceIsNotRegistered(EssenceInterfaceIsNotApplicable):
    # Must be raised by EssenceModel.__call__ when requested EssenceInterface is not registered
    pass


class EssenceModelCanNotInjectSelf(RuntimeError):
    # Must be raised by EssenceModel.emi_inject_model when an object of a class A(EssenceModel) tries
    #   to inject class A - type(self)
    # This behavior is restricted since it may lead to: 
    #   - endless recursion;
    #   - interface collisions when high order model will include several instances of the same interface class.
    pass


class EssenceModelIsNotInjected(RuntimeError):
    # Must be raised by EssenceModel.emi_injected_model if not injected model was requested
    pass


class IncompatibleHighOrderEssenceModel(RuntimeError):
    # Must be raised by EssenceModel.emu_behave_as_unknown_model method if incompatible on attempt to inject it to
    # incompatible high order model
    pass


class UnknownEssenceModeBehaviorWasNotImplementedProperly(NotImplementedError):
    pass


class EssenceModelInheritanceAbstract:
    def __call__(self, interface_class: Type['EssenceInterface']):
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

    def emi_inject_model(self, essence_model: 'EssenceModelInjectionAbstract'):
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
    def emu_behave_as_unknown_model(self):
        raise NotImplementedError

    def emu_on_behave_as_unknown_model(self):
        raise NotImplementedError

    def emu_register_on_model_changed_callback(self, requester: 'EssenceModelUnknownInjectionAbstract'):
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

    emi_compatible_injectable_essence_model_classes: TypeVar[Set[Type['EssenceModel']]] = set()
    emu_compatible_high_order_essence_model_class: TypeVar[Optional[Type['EssenceModel']]] = None

    def __init__(self):
        self.__em_interfaces: Dict[Type['EssenceInterface'], 'EssenceInterface'] = dict()
        self.__em_possible_interfaces: Dict[Type['EssenceInterface'], 'EssenceInterface'] = dict()
        self.__emi_injected_models: Dict[Type['EssenceModel'], 'EssenceModel'] = dict()
        self.__emi_high_order_model: Optional['EssenceModel'] = None
        self.__emu_in_unknown_model_behavior: bool = False

    def __call__(self, interface_class: Type['EssenceInterface']):
        # Should be called in order to get needed model interface
        if interface_class in self.__em_interfaces:
            return self.__em_interfaces[interface_class]
        else:
            injected_model_interface = None
            for injected_model_class, injected_model in self.__emi_injected_models.items():
                model: 'EssenceModel' = injected_model
                if model.em_interface_active(interface_class):
                    injected_model_interface = model(interface_class)
                    break
            if injected_model_interface:
                return injected_model_interface
            elif interface_class in self.__em_possible_interfaces:
                raise EssenceInterfaceIsNotApplicable
            else:
                raise EssenceInterfaceIsNotRegistered

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
            if interface.applicable():
                new_interfaces[interface_class] = interface
            else:
                new_possible_interfaces[interface_class] = interface

        for interface_class, interface in self.__em_possible_interfaces.items():
            if interface.applicable():
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
        self._emi_notify_high_order_model_about_self_update(type(self), interface_class, *args, **kwargs)

    def em_add_interface(self, interface_class: Type['EssenceInterface'], *args, **kwargs) -> bool:
        if (interface_class in self.__em_interfaces) or (interface_class in self.__em_possible_interfaces):
            return False
        else:
            interface = interface_class(self, *args, **kwargs)
            if interface.applicable():
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
            raise EssenceModelCanNotInjectSelf
        self.__emi_injected_models[essence_model_class] = essence_model
        essence_model.emi_on_registered_in_high_order_model(self)
        if essence_model_class not in self.emi_compatible_injectable_essence_model_classes:
            essence_model.emu_behave_as_unknown_model()

    def emi_injected_models(self):
        return set(self.__emi_injected_models)

    def emi_injected_model(self, essence_model_class: Type['EssenceModel']):
        if essence_model_class in self.__emi_injected_models:
            return self.__emi_injected_models[essence_model_class]
        else:
            raise EssenceModelIsNotInjected

    def emi_on_injected_model_updated(self, essence_model_class: Type['EssenceModel'], *args, **kwargs):
        # In 'super' in method of inherit class should be run at the end of the method
        # With deep injection it will be like (model_3, model_2, model_1, interface_1, arg_1, arg_2, arg_3)
        #   where `interface_1` is an interface of the `model_1`
        self._em_check_applicability_of_interfaces()
        self._emi_notify_high_order_model_about_self_update(type(self), essence_model_class, *args, **kwargs)

    def _emi_notify_high_order_model_about_self_update(self, *args, **kwargs):
        if self.__emi_high_order_model:
            high_order_model: 'EssenceModel' = self.__emi_high_order_model
            high_order_model.emi_on_injected_model_updated(*args, **kwargs)

    def emi_remove_injected_model(self, essence_model_class: Type['EssenceModel']):
        injected_model: 'EssenceModel' = self.__emi_injected_models[essence_model_class]
        injected_model.emi_on_unregistering_from_high_order_model()
        del self.__emi_injected_models[essence_model_class]

    def emu_behave_as_unknown_model(self):
        # Should be called by a high order model for an unknown injected model
        if type(self.__emi_high_order_model) != self.emu_compatible_high_order_essence_model_class:
            raise IncompatibleHighOrderEssenceModel
        self.__emi_high_order_model.emu_register_on_model_changed_callback(type(self))
        self.__emu_in_unknown_model_behavior = True
        self.emu_on_behave_as_unknown_model()

    def emu_on_behave_as_unknown_model(self):
        pass

    def emu_register_on_model_changed_callback(self, requester: 'EssenceModelUnknownInjectionAbstract'):
        raise NotImplementedError

    def emu_on_model_changed_callback(self):
        raise UnknownEssenceModeBehaviorWasNotImplementedProperly

    def emu_is_in_unknown_model_behavior(self):
        return self.__emu_in_unknown_model_behavior


Model = TypeVar('Model', bound=EssenceModel)


class EssenceInterface(Generic[Model]):
    essence_model_class: TypeVar[Type[Model]] = EssenceModel

    def __init__(self, essence_model: Model, *args, **kwargs):
        self.essence_model: Model = essence_model
        self.__check_essence_mode_type()

    def __check_essence_mode_type(self):
        if not isinstance(self.essence_model, self.essence_model_class):
            raise IncompatibleEssenceModel

    def applicable(self) -> bool:
        raise NotImplementedError

    def notify_model_about_change(self, *args, **kwargs):
        # Must be run by EssenceInterface's methods if and after changing model's data. It is enough to run in once per
        #   a method - at the end of the method work.
        self.essence_model.em_on_model_updated(type(self), *args, **kwargs)


class EssenceModelFactory:
    def __call__(self, *args, **kwargs):
        model: EssenceModel = EssenceModel()
        model.em_add_interface(EssenceInterface)
        return model
