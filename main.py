class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = 0

    def rate_lectorer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка!'
        sum = 0
        len = 0
        for key in lecturer.grades.keys():
            for grad in list(lecturer.grades[key]):
                sum = sum + grad
                len += 1
        lecturer.average_rating = round(sum / len, 2)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нельзя сравнить')
            return
        return self.average_rating < other.average_rating

    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка студента: {self.average_rating}\n Курсы в процессе изучения: {self.courses_in_progress}\n Завершенные курсы: {self.finished_courses}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_rating = 0
        self.students_list = []

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Нельзя сравнить")
            return
        return self.average_rating < other.average_rating

    def __str__(self):
        res = f'Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка: {self.average_rating}'
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка!"
        sum = 0
        len = 0
        for key in student.grades.keys():
            for grad in list(student.grades[key]):
                sum = sum + grad
                len += 1
        student.average_rating = round(sum / len, 2)

    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}'
        return res


student_1 = Student("Олег", "Олегов", "м")
student_1.finished_courses += ["С++"]
student_1.courses_in_progress += ["GIT"]
student_1.courses_in_progress += ["Python"]

student_2 = Student("Дмитрий", "Дмитриев", "м")
student_2.courses_in_progress += ["Python"]
student_2.finished_courses += ["C#"]

lecturer_1 = Lecturer("Максим", "Максимов")
lecturer_1.courses_attached += ["Python"]
lecturer_1.courses_attached += ["GIT"]

lecturer_2 = Lecturer("Ольга", "Петрова")
lecturer_2.courses_attached += ["GIT"]

reviewer_1 = Reviewer("Анастасия", "Иванова")
reviewer_1.courses_attached += ["Python"]

reviewer_2 = Reviewer("Алексей", "Попович")
reviewer_2.courses_attached += ["GIT"]
reviewer_2.courses_attached += ["Python"]

# Задание 4.Полевые испытания
student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]


def average_rating_hw(students, courses):
    sum_course_grade = 0
    iterator = 0
    for student in students:
        for key, value in student.grades.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_course_grade / iterator, 2)


def average_rating_lectorers(lecturers, courses):
    sum_course_grade = 0
    iterator = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_course_grade / iterator, 2)


student_1.rate_lectorer(lecturer_2, "GIT", 9)
student_1.rate_lectorer(lecturer_2, "GIT", 10)
student_1.rate_lectorer(lecturer_1, "GIT", 10)
student_1.rate_lectorer(lecturer_1, "GIT", 8)
student_1.rate_lectorer(lecturer_1, "Python", 9)
student_2.rate_lectorer(lecturer_1, "Python", 10)
student_2.rate_lectorer(lecturer_1, "Python", 10)

reviewer_1.rate_hw(student_1, "Python", 10)
reviewer_2.rate_hw(student_1, "GIT", 9)
reviewer_2.rate_hw(student_1, "GIT", 10)
reviewer_1.rate_hw(student_1, "Python", 10)
reviewer_1.rate_hw(student_2, "Python", 7)
reviewer_1.rate_hw(student_2, "Python", 10)
reviewer_1.rate_hw(student_2, "Python", 8)

print(f'Студентов:\n {student_1}\n {student_2} \n')
print()
print(f'Лекторов:\n {lecturer_1}\n {lecturer_2} \n')
print()
print(f'Эксперты:\n {reviewer_1}\n {reviewer_2}\n')


# Подсчет средней оценки за курсы по дз и за курс:
print(f'Средняя оценка студентов за курс GIT: {average_rating_hw(student_list, "GIT")}')
print(f'Средняя оценка студентов за курс Python: {average_rating_hw(student_list, "Python")}')
print(f'Средняя оценка лекторов за курс Python: {average_rating_lectorers(lecturer_list, "Python")}')
print(f'Средняя оценка лекторов за курс GIT: {average_rating_lectorers(lecturer_list, "GIT")}')
