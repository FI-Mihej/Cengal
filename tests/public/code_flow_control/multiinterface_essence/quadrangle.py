from cengal.code_flow_control.multiinterface_essence.essence import *


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
