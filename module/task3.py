# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

from math import factorial


class Generator:
    def __init__(self, start, stop=None, step=1):
        if not stop:
            self.start = 1
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.step = step

    def __iter__(self):
        if not self.step:
            raise ValueError("Шаг не может быть 0")
        self.current = self.start
        return self

    def __next__(self):
        while self.current < self.stop if self.step > 0 else self.current > self.stop:
            result = factorial(self.current)
            self.current += self.step
            return result
        raise StopIteration


def main():
    gen = Generator(10, -1, -2)
    for n in gen:
        print(n, end=' ')
    print()
    for n in gen:
        print(n, end=' ')


if __name__ == '__main__':
    main()
