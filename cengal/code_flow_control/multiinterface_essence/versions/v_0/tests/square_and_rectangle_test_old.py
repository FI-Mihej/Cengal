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


import sys

from typing import Tuple
from square_and_rectangle import *


def check_for_exit(input_str: str) -> None:
    if input_str.lower() in {'q', 'quit', 'exit'}:
        raise SystemExit


def get_new_x_y() -> Tuple[bool, float, float]:
    is_ok = True
    x = 0.0
    y = 0.0
    try:
        input_str = input('Enter a new x y dimension: ')
        check_for_exit(input_str)
        input_str_list = input_str.strip().split()
        x = float(input_str_list[0])
        y = float(input_str_list[1])
    except EssenceModelException:
        is_ok = False
    return is_ok, x, y


def get_stretch() -> Tuple[bool, float]:
    is_ok = True
    multiplier = 0.0
    try:
        input_str = input('SQUARE stretch multiplier: ')
        check_for_exit(input_str)
        multiplier = float(input_str.strip())
    except EssenceModelException:
        is_ok = False
    return is_ok, multiplier


def get_x_or_y_stretch() -> Tuple[bool, bool, float]:
    is_ok = True
    is_x = True
    multiplier = 0.0
    try:
        input_str = input('RECTANGLE stretch in a format "is_x multiplier" ("yes 4"): ')
        check_for_exit(input_str)
        input_str_list = input_str.strip().split()
        if input_str_list[0].lower() in {'y', 'yes'}:
            is_x = True
        else:
            is_x = False
        multiplier = float(input_str_list[1])
    except EssenceModelException:
        is_ok = False
    return is_ok, is_x, multiplier


def request_dimension(frame: RectangleModel):
    try:
        rectangle: RectangleInterface = frame.em_interface(RectangleInterface)
        print('Current dimension: ', rectangle.dimension().x, rectangle.dimension().y)
        is_ok, new_x, new_y = get_new_x_y()
        if is_ok:
            rectangle.set_dimension(Point(new_x, new_y))
    except UnsuitableEssenceInterfaceError:
        pass


def stretch_square(frame: RectangleModel):
    try:
        stretching_square: StretchingSquareInterface = frame.em_interface(StretchingSquareInterface)
        print('Current dimension: ', stretching_square.dimension().x, stretching_square.dimension().y)
        is_ok, multiplier = get_stretch()
        if is_ok:
            stretching_square.stretch(multiplier)
    except UnsuitableEssenceInterfaceError:
        pass


def stretch_rectangle(frame: RectangleModel):
    try:
        stretching_rectangle: StretchingRectangleInterface = frame.em_interface(StretchingRectangleInterface)
        print('Current dimension: ', stretching_rectangle.dimension().x, stretching_rectangle.dimension().y)
        is_ok, is_x, multiplier = get_x_or_y_stretch()
        if is_ok:
            if is_x:
                stretching_rectangle.stretch_x(multiplier)
            else:
                stretching_rectangle.stretch_y(multiplier)
    except UnsuitableEssenceInterfaceError:
        pass


def main():
    frame: RectangleModel = rectangle_factory(Point(0, 0))
    while True:
        request_dimension(frame)
        stretch_square(frame)  # Will be executed only if frame is a square
        stretch_rectangle(frame)
        stretch_square(frame)  # Will be executed only if frame is a square


if __name__ == '__main__':
    main()
