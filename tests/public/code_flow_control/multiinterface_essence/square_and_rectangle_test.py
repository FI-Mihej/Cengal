from typing import Tuple
from .square_and_rectangle import *


def get_new_x_y() -> Tuple[bool, float, float]:
    is_ok = True
    x = 0.0
    y = 0.0
    try:
        input_str = input('Enter a new x y dimension: ')
        input_str_list = input_str.strip().split()
        x = float(input_str_list[0])
        y = float(input_str_list[1])
    except:
        is_ok = False
    return is_ok, x, y


def get_stretch() -> Tuple[bool, float]:
    is_ok = True
    multiplier = 0.0
    try:
        input_str = input('SQUARE stretch multiplier: ')
        multiplier = float(input_str.strip())
    except:
        is_ok = False
    return is_ok, multiplier


def get_x_or_y_stretch() -> Tuple[bool, bool, float]:
    is_ok = True
    is_x = True
    multiplier = 0.0
    try:
        input_str = input('RECTANGLE stretch in a format "is_x multiplier": ')
        input_str_list = input_str.strip().split()
        if input_str_list[0].lower() in {'y', 'yes'}:
            is_x = True
        else:
            is_x = False
        multiplier = float(input_str_list[1])
    except:
        is_ok = False
    return is_ok, is_x, multiplier


def request_dimension(frame: RectangleModel):
    try:
        rectangle: RectangleInterface = frame(RectangleInterface)
        print('Current dimension: ', rectangle.dimension().x, rectangle.dimension().y)
        is_ok, new_x, new_y = get_new_x_y()
        if is_ok:
            rectangle.set_dimension(Point(new_x, new_y))
    except EssenceInterfaceIsNotApplicable:
        pass


def stretch_square(frame: RectangleModel):
    try:
        stretching_square: StretchingSquareInterface = frame(StretchingSquareInterface)
        print('Current dimension: ', stretching_square.dimension().x, stretching_square.dimension().y)
        is_ok, multiplier = get_stretch()
        if is_ok:
            stretching_square.stretch(multiplier)
    except EssenceInterfaceIsNotApplicable:
        pass


def stretch_rectangle(frame: RectangleModel):
    try:
        stretching_rectangle: StretchingRectangleInterface = frame(StretchingRectangleInterface)
        print('Current dimension: ', stretching_rectangle.dimension().x, stretching_rectangle.dimension().y)
        is_ok, is_x, multiplier = get_x_or_y_stretch()
        if is_ok:
            if is_x:
                stretching_rectangle.stretch_x(multiplier)
            else:
                stretching_rectangle.stretch_y(multiplier)
    except EssenceInterfaceIsNotApplicable:
        pass


def main():
    frame: RectangleModel = rectangle_factory(Point(0, 0))
    while True:
        request_dimension(frame)
        stretch_square(frame)
        stretch_rectangle(frame)
        stretch_square(frame)


if __name__ == '__main__':
    main()
