# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class Validate:
    def __set_name__(self, owner, name):
        self.attribute = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.attribute)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Сторона не может быть отрицательной")
        setattr(instance, self.attribute, value)


class Rectangle:
    __slots__ = ("_width", "_height")

    width = Validate()
    height = Validate()

    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height else self.width

    def area(self):
        return self._height * self._width

    def perimeter(self):
        return 2 * (self._height * self._width)

    def __add__(self, other):
        if isinstance(other, Rectangle):
            per = self.perimeter() + other.perimeter()
            min_side = min(self.width, self.height, other.width, other.height)
            second_side = per / 2 - min_side
            return Rectangle(min_side, second_side)
        raise TypeError("Не поддерживается сложение с этим типом")

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            per = abs(self.perimeter() - other.perimeter())
            min_side = min(self.width, self.height, other.width, other.height)
            second_side = per / 2 - min_side
            return Rectangle(min_side, second_side)
        raise TypeError("Не поддерживается вычитание с этим типом")

    def __str__(self):
        return f"{self.width = }, {self.height = }, {self.perimeter() = }, {self.area() = }"

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        raise TypeError("Не поддерживается сравнение с этим типом")

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        raise TypeError("Не поддерживается сравнение с этим типом")

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.__lt__(other) or self.__eq__(other)
        raise TypeError("Не поддерживается сравнение с этим типом")


def main():
    r1 = Rectangle(5, 3)
    try:
        r1.width = -5
    except ValueError as e:
        print(e)
    print(r1)


if __name__ == '__main__':
    main()
