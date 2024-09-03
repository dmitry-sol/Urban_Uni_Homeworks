# module6hard
# Дополнительное практическое задание по модулю: "Наследование классов."
from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = sides
        # self. filled = False

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, sides):
        if type(sum(sides)) is int and len(list(sides)) == self.sides_count:
            return True
        else:
            return False

    def get_valid_sides(self, sides):
        if self.__is_valid_sides(sides):
            return True
        else:
            return False

    def __is_valid_color(self, r, g, b):
        if 0 < r < 255 and 0 < g < 255 and 0 < b < 255:
            return r, g, b
        else:
            return self.__color

    def set_color(self, r, g, b):
        self.__color = list(self.__is_valid_color(r, g, b))
        return self.__color

    def __len__(self):
        return self.__len__

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.sides = list(new_sides)
            return self.sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if self.get_valid_sides(sides):
            self.sides = sides
        else:
            self.sides = [1]
        self.radius = self.sides[0] / (2 * pi)

    def get_square(self):
        square = pi * self.radius ** 2
        return square

    def __len__(self):
        p = self.sides[0]
        return p

    def get_sides(self):
        return self.sides


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if self.get_valid_sides(sides):
            self.sides = sides
        else:
            self.sides = [1] * 3

    def __len__(self):
        p = sum(self.sides)
        return p

    def get_square(self):
        p_2 = sum(self.sides) / 2
        square = (p_2 * (p_2 - self.sides[0]) * (p_2 - self.sides[1]) * (p_2 - self.sides[2])) ** 0.5
        return square

    def get_sides(self):
        return self.sides


class Cube(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if self.get_valid_sides(sides):
            self.sides = sides * 12
        else:
            self.sides = [1] * 12

    def get_volume(self):
        volume = self.sides[0] ** 3
        return volume

    def get_sides(self):
        return list(self.sides)


circle1 = Circle((200, 150, 100), 10)  # (Цвет, стороны)
circle2 = Circle((120, 200, 250), 10, 20)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((50, 100, 150), 5, 5, 7)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
print()
# Площадь круга
print(circle1.get_square())
print()
# Проверка треугольника
triangle1.set_color(77, 77, 77)  # Изменится
print(triangle1.get_color())
# Периметр треугольника
print(len(triangle1))
# Площадь треугольника
print(triangle1.get_square())
