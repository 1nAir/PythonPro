from Homework2studentclass import Student


class Group:
    def __init__(self, students=None):
        if students is None:
            self.students = []
        else:
            self.students = students

    def append_student(self, student):
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


if __name__ == '__main__':

    student1 = Student("Ivan", "Ivanov", "20", 1, "ДУТ")
    student2 = Student("Petr", "Petrov", "19", 1, "ДУТ")
    student3 = Student("Kolya", "Kylyaov", "18", 1, "ДУТ")
    student4 = Student("Sergey", "Sergeev", "19", 1, "ДУТ")
    student5 = Student("Alexandr", "Zinchenko", "22", 1, "ДУТ")
    student6 = Student("Evgen", "Akhimov", "21", 1, "ДУТ")
    student7 = Student("Anton", "Vasilev", "20", 1, "ДУТ")
    student8 = Student("Masha", "Melnik", "18", 1, "ДУТ")
    student9 = Student("Natasha", "Kondratenko", "19", 1, "ДУТ")
    student10 = Student("Denys", "Romanuk", "20", 1, "ДУТ")

    group = [student1, student2, student3, student4, student5]
    group2 = [student7, student8, student9, student10]
    k_40 = Group(group)
    k_41 = Group(group2)
    print('Группа к40:', k_40, sep='\n')
    print('Группа к41:', k_41, sep='\n')

    k_40.append_student(student6)
    print('Добавили студента в группу к40:', k_40, sep='\n')

    print('Нашли студента по фамилии:', k_40.search_student("Petrov"), '\n')

    k_40.remove_student(student3)
    print('Удалили студента из группы к40', k_40, sep='\n')
