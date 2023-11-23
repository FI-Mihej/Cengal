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


Kilogram = float


class Weight:
    def __init__(self, weight: Kilogram):
        self.weight: Kilogram = weight


class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y


class MaterialPoint:
    def __init__(self, material_point: Point):
        self.material_point = material_point


class Quadrangle:
    def __init__(self, tl: Point, tr: Point, bl: Point, br: Point):
        self.tl: Point = tl
        self.tr: Point = tr
        self.bl: Point = bl
        self.br: Point = br


class StretchingQuadrangleFrameModel(EssenceModel, MaterialPoint, Quadrangle, Weight):
    def __init__(self):
        super(StretchingQuadrangleFrameModel, self).__init__()
        Quadrangle.__init__(self, Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0))
        MaterialPoint.__init__(self, Point(0, 0))
        Weight.__init__(self, 0)


class Vector:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end


class Flying:
    def __init__(self, flying_vector: Vector):
        self.flying_vector = flying_vector


class FlyingStretchingQuadrangleFrameModel(StretchingQuadrangleFrameModel, Flying):
    def __init__(self):
        super(FlyingStretchingQuadrangleFrameModel, self).__init__()
        Flying.__init__(self, Vector(Point(0, 0), Point(0, 0)))
