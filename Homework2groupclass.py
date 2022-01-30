from Homework2studentclass import Student

MAX_STUDENTS = 10


class InputError(Exception):
    def __init__(self, expression, message):
        """

        :param expression:
        :param message:
        """
        self.expression = expression
        self.message = message


class Group:
    def __init__(self, students=None):
        """

        :param students:
        """
        try:
            if len(students) not in range(0, MAX_STUDENTS):
                raise InputError(len(students), 'Student in group must be between 0-10')
        except InputError as err:
            print(err)
        finally:
            if students is None:
                self.students = []
            else:
                self.students = students

    def append_student(self, student):
        if len(self.students) > MAX_STUDENTS:
            raise InputError(len(self.students), 'In group already all places are occupied')
        self.students.append(student)

    def search_student(self, surname):
        for student in self.students:
            if student.surname == surname:
                return student

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def __str__(self):
        self.result = ""
        for i in range(len(self.students)):
            self.result += str(i + 1) + ". " + self.students[i].surname + "\n"
        return self.result


