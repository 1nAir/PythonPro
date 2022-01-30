from Homework2studentclass import Student
from Homework2groupclass import Group


if __name__ == '__main__':

    student1 = Student("Ivan", "Ivanov", 20, 1, "ДУТ")
    student2 = Student("Petr", "Petrov", 19, 1, "ДУТ")
    student3 = Student("Kolya", "Kylyaov", 18, 1, "ДУТ")
    student4 = Student("Sergey", "Sergeev", 19, 1, "ДУТ")
    student5 = Student("Alexandr", "Zinchenko", 22, 1, "ДУТ")
    student6 = Student("Evgen", "Akhimov", 21, 1, "ДУТ")
    student7 = Student("Anton", "Vasilev", 20, 1, "ДУТ")
    student8 = Student("Masha", "Melnik", 18, 1, "ДУТ")
    student9 = Student("Natasha", "Kondratenko", 19, 1, "ДУТ")
    student10 = Student("Denys", "Romanuk", 20, 1, "ДУТ")
    student11 = Student("Denys", "Romanuk", 20, 1, "ДУТ")
    student12 = Student("Denys", "Romanuk", 20, 1, "ДУТ")
    student13 = Student("Denys", "Romanuk", 20, 1, "ДУТ")
    student14 = Student("Denys", "Romanuk", 20, 1, "ДУТ")
    student15 = Student("Denys", "Romanuk", 20, 1, "ДУТ")
    student16 = Student("Denysx", "Romanukz", 20, 1, "ДУТ")

    try:
        group = [student1, student2, student3, student4, student5, student11, student12, student13, student14, student15]
        group2 = [student7, student8, student9, student10]
    except Exception as error:
        print(error)

    k_40 = Group(group)
    k_41 = Group(group2)
    print('Группа к40:', k_40, sep='\n')
    print('Группа к41:', k_41, sep='\n')

    try:
        k_40.append_student(student6)
        print('Добавили студента в группу к40:', k_40, sep='\n')
    except Exception as error:
        print(error)

    print('Нашли студента по фамилии:', k_40.search_student("Akhimov"), '\n')

    k_40.remove_student(student3)
    print('Удалили студента из группы к40', k_40, sep='\n')
