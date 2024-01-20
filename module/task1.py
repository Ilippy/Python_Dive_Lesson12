# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

from collections import OrderedDict


class Factorial:
    def __init__(self, k):
        self.fact = OrderedDict()
        self.k = k

    def __call__(self, number: int):
        result = 1
        for i in range(1, number + 1):
            result *= i
        self.fact[number] = result
        return result

    def get_factorials(self):
        return self.fact


def main():
    f = Factorial(5)
    print(f"{f(9) = }")
    print(f"{f(5) = }")
    print(f"{f(7) = }")
    print(f.get_factorials())


if __name__ == '__main__':
    main()
