"""
Task about inheritance of classes
"""
from os import system
from math import pi, sqrt

_CIRCLE_SIDE_COUNT = 1
_TRIANGLE_SIDE_COUNT = 3
_CUBE_SIDE_COUNT = 12
_DEF_SIDE_LENGTH = 1

def Herons(*args):
    # print(f"Herons: args - {args}")
    _a = args[0][0]
    _b = args[0][1]
    _c = args[0][2]
    # print(f"Herons: args - {args} - {_a}, {_b}, {_c}")
    _p = _a + _b + _c
    # print(f"Herons: p - {_p}")
    _s = _p / 2
    # print(f"Herons: s - {_s}")
    _arg = _s * (_s - _a) * (_s - _b) * (_s - _c)
    # print(f"Herons: arg - {_arg}")
    _A = sqrt(_arg)
    _H = 2 * (_A / _b)
    # print(f"Herons: A - {_A}, H - {_H}")
    return _A, _H



class _Figure():
    sides_count = 0

    def __init__(self, rgb, side_count) -> None:
        self.set_color(*rgb)
        self.__sides = [1] * side_count
        self.sides_count = side_count
        self.filled = False
    
    def __is_valid_color(self, *rgb):
        if rgb[0] in range(256) and rgb[1] in range(256) and rgb[2] in range(256):
            return True
        return False
    
    def __is_valid_sides(self, *sides_value):
        if len(sides_value) == len(self.__sides):
            for i in sides_value:
                if i <= 0:
                    return False
            return True
        else:
            return False
    
    def __len__(self):
        return sum(self.__sides)
    
    def set_color(self, *rgb):
        # input(f" set_color: {rgb}")
        if self.__is_valid_color(*rgb):
            self.__color = list(rgb)
        
    def get_color(self):
        return self.__color
    
    def set_sides(self, *new_sides):
        # print(f"set_sides: {new_sides} - {new_sides[0]}")
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides
    
class Circle(_Figure):
    def __init__(self, rgb, *sides) -> None:
        super().__init__(rgb, _CIRCLE_SIDE_COUNT)
        if len(sides) != self.sides_count:
            self.set_sides(_DEF_SIDE_LENGTH)
        else:
            self.set_sides(sides[0])

    def set_sides(self, *sides):
        super().set_sides(*sides)
        side = self.get_sides()
        self.radius = side[0] / (2 * pi)
    
    def get_square(self):
        side = self.get_sides()
        sq1 = (side[0] ** 2) / (4 * pi)
        sq2 = pi * (self.radius ** 2)
        if sq1 > sq2:
            return sq1
        else:
            return sq2
    
    def get_radius(self):
        return self.radius

class Triangle(_Figure):
    def __init__(self, rgb, *sides):
        super().__init__(rgb, _TRIANGLE_SIDE_COUNT)
        if len(sides) != self.sides_count:
            self.set_sides(_DEF_SIDE_LENGTH, _DEF_SIDE_LENGTH, _DEF_SIDE_LENGTH,)
        else:
            self.set_sides(*sides)

    def __is_triangle_sides(self, *sides):
        _a = sides[0]
        _b = sides[1]
        _c = sides[2]
        if _a < _b + _c and _b < _a + _c and _c < _a + _b:
            return True
        return False

    def set_sides(self, *args):
        if self.__is_triangle_sides(*args):
            super().set_sides(*args)
            self.__square, self.__altitude = Herons(self.get_sides())

    def get_square(self):
        return self.__square
    
    def get_altitude(self):
        return self.__altitude


class Cube(_Figure):
    def __init__(self, rgb, *sides) -> None:
        super().__init__(rgb, _CUBE_SIDE_COUNT)
        self.__sides = [1] * _CUBE_SIDE_COUNT
        if len(sides) != 1:
            self.set_sides(_DEF_SIDE_LENGTH)
        else:
            self.set_sides(*sides)
    
    def __is_valid_sides(self, *sides_value):
        if len(sides_value) != 1 or sides_value[0] <= 0:
            return False 
        return True

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [new_sides[0]] * self.sides_count   

    
    def get_sides(self):
        return self.__sides
    
    def get_volume(self):
        return self.__sides[0] ** 3




if __name__ == '__main__':
    system('cls')

    figure = _Figure((1, 2, 3), 3)

    figure.set_color(255, 255, 255)
    print(f"Main: color - {figure.get_color()}")
    print(f"Main: sides - {figure.get_sides()}")

    figure.set_sides(1, 2, 3)
    print(f"Main: sides - {figure.get_sides()}")
    print(f"Main: len - {len(figure)}")

    circle = Circle((4, 5, 6), 10)
    print(f"Main: circle side - {circle.get_sides()}")
    print(f"Main: circle radius - {circle.get_radius()}")
    print(f"Main: circle square - {circle.get_square()}")

    triangle = Triangle((7, 8, 9), 10, 11, 12)
    print(f"Main: triangle sides - {triangle.get_sides()}")
    print(f"Main: triangle altitude - {triangle.get_altitude()}")
    print(f"Main: triangle square - {triangle.get_square()}")

    cube = Cube((10, 11, 12), 13)
    print(f"Main: cube sides - {cube.get_sides()}")

### Testing
    print("\n testing...\n")
    circle1 = Circle((200, 200, 100), 10)
    cube1 = Cube((222, 35, 130), 6)

    circle1.set_color(55, 66, 77)
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)
    print(cube1.get_color())

    cube1.set_sides(5, 3, 12, 4, 5)
    print(cube1.get_sides())
    circle1.set_sides(15)
    print(circle1.get_sides())

    print(len(circle1))

    print(cube1.get_volume())




    # input('press <Enter> to leave...')