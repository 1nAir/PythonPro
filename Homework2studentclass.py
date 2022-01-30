from Homework2humanclass import Human


class Student(Human):
    def __init__(self, name, surname, age, course, institution):
        """

        :param name:
        :param surname:
        :param age:
        :param course:
        :param institution:
        """
        super().__init__(name, surname, age)
        self.course = course
        self.institution = institution

    def __str__(self):
        return f"Студент {self.surname} {self.name}, Институт: {self.institution}, " \
               f"Курс: {self.course}, Возраст: {self.age}"
