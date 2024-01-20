from statistics import mean


class CheckName:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    @staticmethod
    def validate(value):
        """Метод, проверяющий, что имя состоит только из букв и начинается на заглавную"""
        if not value.istitle() or not value.isalpha():
            raise ValueError(f'Неверное значение {value}.\n'
                             f'ФИО должно состоять только из букв и начинаться на заглавную')


class CheckSubject:
    def __init__(self, path):
        self.path = path

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    def validate(self, value):
        """Метод, проверяющий, что предмет находится в списке"""
        with open(self.path, 'r', newline='', encoding='utf-8') as c:
            if value.lower() not in [sub.strip() for sub in c]:
                raise ValueError(f'Предмета {value} нет в списке')


class CheckSubjectScore:
    def __init__(self, min_sub_score, max_sub_score):
        self.min_sub_score = min_sub_score
        self.max_sub_score = max_sub_score

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    def validate(self, value):
        """Метод, проверяющий, что оценки входят в диапазон"""
        if self.min_sub_score > value or value > self.max_sub_score:
            raise ValueError(f"Некорректная оценка предмета: {value}\n"
                             f"Оценка должна быть в диапазоне от {self.min_sub_score} до {self.max_sub_score}")


class CheckTesttScore:
    def __init__(self, min_test_score, max_test_score):
        self.min_test_score = min_test_score
        self.max_test_score = max_test_score

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        return setattr(instance, self.param_name, value)

    def validate(self, value):
        """Метод, проверяющий, что оценки входят в диапазон"""
        if self.min_test_score > value or value > self.max_test_score:
            raise ValueError(f"Некорректная оценка теста: {value}\n"
                             f"Оценка должна быть в диапазоне от {self.min_test_score} до {self.max_test_score}")


class Student:
    """Класс описывающий студента"""
    FILE_NAME = 'students.csv'
    first_name = CheckName()
    last_name = CheckName()
    middle_name = CheckName()
    subject = CheckSubject(FILE_NAME)
    subject_score = CheckSubjectScore(min_sub_score=2, max_sub_score=5)
    test_score = CheckTesttScore(min_test_score=0, max_test_score=100)
    subjects = []

    def __init__(self, first_name, last_name, middle_name, subject, subject_score, test_score):
        """
        Конструктор класса
        :param first_name: Имя студента
        :param last_name: Фамилия студента
        :param middle_name: Отчество студента
        :param subject: Предмет студента
        :param subject_score: Оценка по предмету
        :param test_score: Оценка теста по предмету
        """
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.subject = subject
        self.subject_score = subject_score
        self.test_score = test_score
        self._update_subjects()

    def add_subject(self, subject, subject_score, test_score):
        """Метод добавления нового предмета студенту"""
        self.subject = subject
        self.subject_score = subject_score
        self.test_score = test_score
        self._update_subjects()

    def _update_subjects(self):
        """Метод добавления предмета в список предметов"""
        self.subjects.append({
            "subject": self.subject,
            "subject_score": self.subject_score,
            "test_score": self.test_score,
        })

    def get_avg(self):
        """Метод, возвращающий информацию по среднему балу за оценки и тесты"""
        avg_sub_score = mean(score['subject_score'] for score in self.subjects)
        avg_test_score = mean(score['test_score'] for score in self.subjects)
        return f"""Предметы студента: {', '.join([sub['subject'].title() for sub in self.subjects])}
Средний бал по урокам: {avg_sub_score}
Средний бал по тестам: {avg_test_score}\n"""


if __name__ == '__main__':
    s = Student("Иван", "Иванов", "Иванович", "математика", 5, 87)
    print(s.get_avg())
    s.add_subject("русский", 3, 54)
    s.add_subject('алгебра', 4, 66)
    print(s.get_avg())
