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
        if type(sum(sides)) is int and min(sides) >= 0 and len(list(sides)) == self.sides_count:
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
            self.__sides = list(new_sides)
            return list(self.__sides)
        else:
            # self.__sides = [1]
            return self.__sides

    def get_sides(self):
        return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if self.get_valid_sides(sides):
            self.sides = sides
        else:
            self.sides = [1]

    def get_square(self):
        radius = self.sides[0] / (2 * pi)
        square = pi * radius ** 2
        return square

    def __len__(self):
        p = self.sides[0]
        return p

    def get_sides(self):
        self.sides = super().get_sides()
        return list(self.sides)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if self.get_valid_sides(sides):
            self.sides = sides
        else:
            self.__sides = [1] * 3

    def __len__(self):
        p = sum(self.sides)
        return p

    def get_square(self):
        p_ = sum(self.sides) / 2
        square = (p_ * (p_ - self.sides[0]) * (p_ - self.sides[1]) * (p_ - self.sides[2])) ** 0.5
        return square

    def get_sides(self):
        self.sides = super().get_sides()
        return list(self.sides)


class Cube(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if self.get_valid_sides(sides):
            self.sides = list(sides * 12)
        else:
            self.sides = [1] * 12

    def get_volume(self):
        volume = self.sides[0] ** 3
        return volume

    def get_sides(self):
        self.sides = super().get_sides()
        return list(self.sides * 12)


circle1 = Circle((200, 150, 100), 10)  # (Цвет, стороны)
circle2 = Circle((120, 200, 250), 10, 20)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((50, 100, 150), 5, 5, 7)

print()
print(' = ПРОВЕРКА В РАМКАХ ЗАДАЧИ =')
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
print()

print(' = РАСШИРЕННАЯ ПРОВЕРКА =')
print()
print(' = ПРОВЕРКА КРУГА =')
print('Цвета круга:', circle1.get_color())
print('Стороны круга:', circle1.get_sides())
print('Площадь круга:', circle1.get_square())
print('Периметр круга:', len(circle1))
print()

circle1.set_color(300, 100, 100)  # Изменится
print('Меняем цвет круга неправильно и проверяем, изменится ли:', circle1.get_color())
circle1.set_color(100, 100, 101)  # Изменится
print('Меняем цвет круга правильно и проверяем, изменится ли:', circle1.get_color())
print()

print('Меняем стороны круга неправильно и проверяем изменится ли:', circle1.set_sides(12, 45, 32))
print('Стороны круга:', circle1.get_sides())
print('Периметр круга:', len(circle1))
print('Площадь круга:', circle1.get_square())
print()

print('Меняем стороны круга правильно и проверяем изменится ли:', circle1.set_sides(33))
print('Стороны круга:', circle1.get_sides())
print('Периметр круга:', len(circle1))
print('Площадь круга:', circle1.get_square())
print()

print(' = ПРОВЕРКА ТРЕУГОЛЬНИКА =')
print('Цвета треугольника:', triangle1.get_color())
print('Стороны треугольника:', triangle1.get_sides())
print('Периметр треугольника:', len(triangle1))
print('Площадь треугольника:', triangle1.get_square())
print()

triangle1.set_color(100, 300, 100)  # Изменится
print('Меняем цвет круга неправильно и проверяем, изменится ли:', triangle1.get_color())
triangle1.set_color(100, 100, 102)  # Изменится
print('Меняем цвет круга правильно и проверяем, изменится ли:', triangle1.get_color())
print()

print('Меняем стороны треугольника неправильно и проверяем изменится ли:', triangle1.set_sides(12, 45, 32, 55))
print('Стороны круга:', triangle1.get_sides())
print('Площадь круга:', triangle1.get_square())
print('Периметр круга:', len(triangle1))
print()

print('Меняем стороны треугольника правильно и проверяем изменится ли:', triangle1.set_sides(50, 50, 70))
print('Стороны круга:', triangle1.get_sides())
print('Площадь круга:', triangle1.get_square())
print('Периметр круга:', len(triangle1))
print()

print(' = ПРОВЕРКА КУБА =')
print('Цвета куба:', cube1.get_color())
print('Стороны куба:', cube1.get_sides())
print('Объем куба:', cube1.get_volume())
print()

cube1.set_color(100, 100, 300)  # Изменится
print('Меняем цвет куба неправильно и проверяем, изменится ли:', cube1.get_color())
cube1.set_color(100, 100, 103)  # Изменится
print('Меняем цвет куба правильно и проверяем, изменится ли:', cube1.get_color())
print()

print('Меняем стороны куба неправильно и проверяем изменится ли:', cube1.set_sides(50, 50))
print('Стороны куба:', cube1.get_sides())
print('Объем куба:', cube1.get_volume())
print()

print('Меняем стороны куба правильно и проверяем изменится ли:', cube1.set_sides(100))
print('Стороны куба:', cube1.get_sides())
print('Объем куба:', cube1.get_volume())
print()
print()

print(circle1.__dict__)
print(triangle1.__dict__)
print(cube1.__dict__)
