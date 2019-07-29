from cengal.code_flow_control.multiinterface_essence.essence import *


class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y


class RectangleModel(EssenceModel):
    def __init__(self, dimension: Point):
        super(RectangleModel, self).__init__()
        self.dimension: Point = dimension


class RectangleInterface(EssenceInterface[RectangleModel]):
    essence_model_class: Type[RectangleModel] = RectangleModel

    def __init__(self, essence_model: EssenceModel):
        super(RectangleInterface, self).__init__(essence_model)

    def applicable(self) -> bool:
        return True

    def set_dimension(self, dimension: Point) -> NoReturn:
        self.essence_model.dimension = dimension
        self.notify_model_about_change()

    def dimension(self) -> Point:
        return self.essence_model.dimension


class StretchingRectangleInterface(RectangleInterface):
    def __init__(self, essence_model: EssenceModel):
        super(StretchingRectangleInterface, self).__init__(essence_model)

    def applicable(self) -> bool:
        return True

    def stretch_x(self, multiplier: float) -> NoReturn:
        self.essence_model.dimension.x *= multiplier
        self.notify_model_about_change()

    def stretch_y(self, multiplier: float) -> NoReturn:
        self.essence_model.dimension.y *= multiplier
        self.notify_model_about_change()


class StretchingSquareInterface(RectangleInterface):
    def __init__(self, essence_model: EssenceModel):
        super(StretchingSquareInterface, self).__init__(essence_model)

    def applicable(self) -> bool:
        return self.essence_model.dimension.x == self.essence_model.dimension.y

    def stretch(self, multiplier: float) -> NoReturn:
        self.essence_model.dimension.x *= multiplier
        self.essence_model.dimension.y *= multiplier
        self.notify_model_about_change()


def rectangle_factory(dimension: Point) -> RectangleModel:
    result: RectangleModel = RectangleModel(dimension)
    result.em_add_interface(RectangleInterface)
    result.em_add_interface(StretchingRectangleInterface)
    result.em_add_interface(StretchingSquareInterface)
    return result
