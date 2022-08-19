import cv2.cv2 as cv
import numpy as np

class Point:
    # Stable
    x = 0
    y = 0
    def __init__(self, x=0, y=0):
        if type(x) is list:
            self.assign_list(x)
        else:
            if type(x) is Point:
                x, y = x.get()
            self.x = x
            self.y = y
        # Must return None.

    def assign_xy(self, x, y):
        self.x = x
        self.y = y
        return self

    def assign_list(self, list):
        self.x, self.y = list[:2]
        return self

    def split(self, list_of_points):
        list_x = [x[0] for x in list_of_points]
        list_y = [y[0] for y in list_of_points]
        return [list_x, list_y]

    def get(self):
        return [self.x, self.y]

    def __add__(self, other):
        other = Point(other)
        tmp = [self.x + other.x, self.y + other.y]
        return Point(tmp)

    def __sub__(self, other):
        other = Point(other)
        tmp = [self.x - other.x, self.y - other.y]
        return Point(tmp)

    def __neg__(self):
        return Point(-self.x, -self.y)


class Refer:
    # Indev
    # Single value cannot be referred to.
    target = None
    data_begin = data_end = None
    flag_entire = False

    def __init__(self, target, flag_entire:bool, data_begin=None, data_end=None):
        self.target = target
        if flag_entire == False:
            self.data_begin = data_begin
            self.data_end = data_end
        # Must return None.
