# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника
# и встройте контроль недопустимых значений(отрицательных).
# Используйте декораторы свойств.

# Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.

class Rectangle:
    __slots__ = ("__width", "__height")

    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height else self.width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("Сторона не может быть отрицательной")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Сторона не может быть отрицательной")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return 2 * (self.__height * self.__width)

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
    r1 = Rectangle(2, 3)
    r2 = Rectangle(3, 5)
    try:
        r1.width = -5
    except ValueError as e:
        print(e)
    print(r1)


if __name__ == '__main__':
    main()
