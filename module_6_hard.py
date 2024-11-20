import math


class Figure:
    sides_count = 0

    def __init__(self, new_colors, *new_sides):
        self.__color = [0, 0, 0]
        self.__sides = list(new_sides)
        self.filled = False

        if self.__is_valid_color(*new_colors):
            self.set_color(*new_colors)

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            for i in range(len(new_sides)):
                self.__sides[i] = new_sides[i]

    def get_side_length(self, index):
        return self.__sides[index]

    def __is_valid_color(self, r, g, b):
        is_valid = True
        if not isinstance(r, int) or not isinstance(g, int) or not isinstance(b, int):
            is_valid = False
        elif r < 0 or g < 0 or b < 0 or r > 255 or g > 255 or b > 255:
            is_valid = False
        return is_valid

    def __is_valid_sides(self, new_sides):
        if self.sides_count != len(new_sides):
            return False
        for side in new_sides:
            if not isinstance(side, int):
                return False
        return True

    def __len__(self):
        return sum(self.__sides)

    def __str__(self):
        return f'{self.sides_count}'


class Circle(Figure):
    sides_count = 1

    def __init__(self, new_colors, *new_sides):
        if len(new_sides) != self.sides_count:
            new_sides = 1
        super().__init__(new_colors, *new_sides)
        self.__radius = self.get_side_length(0) / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def set_sides(self, *new_sides):
        prev_length = self.get_side_length(0)
        super().set_sides(*new_sides)
        new_length = self.get_side_length(0)
        if prev_length != new_length:
            self.__set_radius(self.get_side_length(0) / (2 * math.pi))

    def get_radius(self):
        return self.__radius

    def __set_radius(self, radius):
        self.__radius = radius

    def __str__(self):
        return (f'Количество сторон: {self.sides_count}, '
                f'Цвет фигуры: {self.get_color()}, '
                f'Длина сторон: {self.get_sides()}, '
                f'Радиус: {self.get_radius()}, '
                f'Площадь: {self.get_square()}')


class Triangle(Figure):
    sides_count = 3

    def __init__(self, new_colors, *new_sides):
        if len(new_sides) != self.sides_count:
            if len(new_sides) == 1:
                side = new_sides[0]
                new_sides = side, side, side
            else:
                new_sides = 1, 1, 1
        super().__init__(new_colors, *new_sides)

    def get_square(self):
        p = len(self) / 2
        sides = self.get_sides()
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))

    def __str__(self):
        return (f'Количество сторон: {self.sides_count}, '
                f'Цвет фигуры: {self.get_color()}, '
                f'Длина сторон: {self.get_sides()}, '
                f'Площадь: {self.get_square()}')


class Cube(Figure):
    sides_count = 12

    def __init__(self, new_colors, *new_sides):
        if len(new_sides) != self.sides_count:
            if len(new_sides) == 1:
                side = new_sides[0]
                new_sides = (side, side, side, side,
                             side, side, side, side,
                             side, side, side, side)
            else:
                new_sides = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
        super().__init__(new_colors, *new_sides)

    def get_volume(self):
        return self.get_side_length(0) ** 3

    def __str__(self):
        return (f'Количество сторон: {self.sides_count}, '
                f'Цвет фигуры: {self.get_color()}, '
                f'Длина сторон: {self.get_sides()}, '
                f'Объем: {self.get_volume()}')


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