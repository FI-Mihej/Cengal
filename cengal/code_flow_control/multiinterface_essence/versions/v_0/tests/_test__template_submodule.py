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

"""

"""


Kilogram = float


class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y


class Vector:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end


class Weight(EssenceModel):
    def __init__(self, weight: Kilogram):
        super(Weight, self).__init__()
        self.weight: Kilogram = weight


class MaterialPoint(EssenceModel):
    def __init__(self, material_point: Point):
        super(MaterialPoint, self).__init__()
        self.material_point = material_point


class Riding(EssenceModel):
    def __init__(self, riding_vector: Vector):
        super(Riding, self).__init__()
        self.riding_vector = riding_vector


class Flying(EssenceModel):
    def __init__(self, flying_vector: Vector):
        super(Flying, self).__init__()
        self.flying_vector = flying_vector


class Sitting(EssenceModel):
    def __init__(self):
        super(Sitting, self).__init__()
        self.sitter = None


class EssenceOnCasters(EssenceModel):
    emi_compatible_injectable_essence_model_classes: Set[Type['EssenceModel']] = {Riding}
    def __init__(self, dimension: Point):
        super(EssenceOnCasters, self).__init__()
        self.dimension: Point = dimension


class Chair(EssenceModel):
    def __init__(self, dimension: Point):
        super(Chair, self).__init__()
        self.dimension: Point = dimension


class ChairOnCasters(EssenceModel):
    def __init__(self, dimension: Point):
        super(ChairOnCasters, self).__init__()
        self.dimension: Point = dimension
