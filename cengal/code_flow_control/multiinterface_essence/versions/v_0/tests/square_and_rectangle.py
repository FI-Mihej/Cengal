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


from cengal.code_flow_control.multiinterface_essence import *


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

    @em_changer
    def set_dimension(self, dimension: Point) -> NoReturn:
        self.essence_model.dimension = dimension

    def dimension(self) -> Point:
        return self.essence_model.dimension


class StretchingRectangleInterface(RectangleInterface):
    def __init__(self, essence_model: EssenceModel):
        super(StretchingRectangleInterface, self).__init__(essence_model)

    @em_changer
    def stretch_x(self, multiplier: float) -> NoReturn:
        self.essence_model.dimension.x *= multiplier

    @em_changer
    def stretch_y(self, multiplier: float) -> NoReturn:
        self.essence_model.dimension.y *= multiplier


class StretchingSquareInterface(RectangleInterface):
    def __init__(self, essence_model: EssenceModel):
        super(StretchingSquareInterface, self).__init__(essence_model)

    def applicable(self) -> bool:
        return self.essence_model.dimension.x == self.essence_model.dimension.y

    @em_changer
    def stretch(self, multiplier: float) -> NoReturn:
        self.essence_model.dimension.x *= multiplier
        self.essence_model.dimension.y *= multiplier


def rectangle_factory(dimension: Point) -> RectangleModel:
    return simple_em_factory(
            EntityArgsHolder(RectangleModel, dimension),
            [
                RectangleInterface,
                StretchingRectangleInterface,
                StretchingSquareInterface,
            ]
        )
    # result: RectangleModel = RectangleModel(dimension)
    # result.em_add_interface(RectangleInterface)
    # result.em_add_interface(StretchingRectangleInterface)
    # result.em_add_interface(StretchingSquareInterface)
    # return result
    
