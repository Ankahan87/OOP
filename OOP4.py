class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def __str__(self):
        rzd = ","
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.make_average_grade()}\nКурсы в процессе изучения: {rzd.join(self.courses_in_progress)} \nЗавершенные курсы: {rzd.join(self.finished_courses)}"
    def make_average_grade(self):
        all_courses = self.finished_courses + self.courses_in_progress
        sums_grade = 0
        grade_num = 0
        average_grade = 0
        for course in all_courses:
            if course in self.grades:
                grade_num += len(self.grades[course])
                for grade in self.grades[course]:
                    sums_grade += grade
        if grade_num != 0:
            average_grade = sums_grade/grade_num
        return average_grade
        
    def rate_lectors(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.student_grades:
                lector.student_grades[course] += [grade]
            else:
                lector.student_grades[course] = [grade]
        else:
            return 'Ошибка'
    def comparestudent(self, another_stud):
        if isinstance(another_stud, Student):
            myAvGrade = self.make_average_grade()
            anotherAvGrade = another_stud.make_average_grade()
            if myAvGrade > anotherAvGrade:
                return f"Средняя оценка студента {self.name} {self.surname} больше, чем у студента {another_stud.name} {another_stud.surname}"
            elif myAvGrade < anotherAvGrade:
                return f"Средняя оценка студента {another_stud.name} {another_stud.surname} больше, чем у студента {self.name} {self.surname}"
            else:
                return "Средние оценки студентов равны"
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    name = ""
    surname = ""
    student_grades = {}
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.make_average_grade_lector()}"
    def make_average_grade_lector(self):
        all_courses = self.courses_attached
        sums_grade = 0
        grade_num = 0
        average_grade = 0
        for course in all_courses:
            if course in self.student_grades:
                grade_num += len(self.student_grades[course])
                for grade in self.student_grades[course]:
                    sums_grade += grade
        if grade_num != 0:
            average_grade = sums_grade/grade_num
        return average_grade
    def comparelector(self, another_lector):
        if isinstance(another_lector, Lecturer):
            myAvGrade = self.make_average_grade_lector()
            anotherAvGrade = another_lector.make_average_grade_lector()
            if myAvGrade > anotherAvGrade:
                return f"Средняя оценка лектора {self.name} {self.surname} больше, чем у лектора {another_lector.name} {another_lector.surname}"
            elif myAvGrade < anotherAvGrade:
                return f"Средняя оценка лектора {another_lector.name} {another_lector.surname} больше, чем у лектора {self.name} {self.surname}"
            else:
                return "Средние оценки лекторов равны"
class Reviewer(Mentor):
    name = ""
    surname = ""
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
def MakeAvStudentsGrade(students = [], course = ""):
    Sums_Grades = 0
    Grades_Num = 0
    for student in students:
        if isinstance(student, Student):
            all_courses = student.finished_courses + student.courses_in_progress
            if course in all_courses:
                Sums_Grades += student.make_average_grade()
                Grades_Num += 1
    if Grades_Num != 0:
        print(f"Средняя оценка всех студентов на курсе {course} составляет {Sums_Grades/Grades_Num} баллов")

def MakeAvLectorsGrade(lectors = [], course = ""):
    Sums_Grades = 0
    Grades_Num = 0
    for lector in lectors:
        if isinstance(lector, Lecturer):
            all_courses = lector.courses_attached
            if course in all_courses:
                Sums_Grades += lector.make_average_grade_lector()
                Grades_Num += 1
    if Grades_Num != 0:
        print(f"Средняя оценка всех лекторов на курсе {course} составляет {Sums_Grades/Grades_Num} баллов")            

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

Lecturer1 = Lecturer("Иван Иваныч", "Иванов")
Lecturer2= Lecturer("Семен Семеныч", "Семенов")
Reviewer1 = Reviewer("Петр Петрович", "Петров") 
print(best_student.grades)
print(Lecturer1.name, Lecturer1.surname)
print(Reviewer1.name, Reviewer1.surname)

best_student.rate_lectors(Lecturer2, 'Python', 10)
Lecturer1.courses_attached += ['Python']
best_student.rate_lectors(Lecturer2, 'Python', 10)
best_student.rate_lectors(Lecturer1, 'Python', 8)
best_student.rate_lectors(Lecturer1, 'Python', 7)
best_student.rate_lectors(Lecturer1, 'Python', 9)
bad_student = Student("Андрей", "Андреев", "20")
bad_student.courses_in_progress += ['Python']
bad_student.finished_courses += ['Оператор ПК']
bad_student.rate_lectors(Lecturer1, 'Python', 3)
bad_student.rate_lectors(Lecturer1, 'Python', 5)
bad_student.rate_lectors(Lecturer1, 'Python', 8)
bad_student.rate_lectors(Lecturer2, 'Python', 3)
bad_student.rate_lectors(Lecturer2, 'Python', 5)
bad_student.rate_lectors(Lecturer2, 'Python', 8)
Reviewer1.rate_hw(bad_student,'Python', 2)
Reviewer1.rate_hw(bad_student,'Python', 3)
Reviewer1.rate_hw(bad_student,'Python', 5)
print(Lecturer1)
print(Lecturer1.comparelector(Lecturer2))
print(Reviewer1)
print(best_student)
print(best_student.comparestudent(bad_student))
MakeAvLectorsGrade([Lecturer1, Lecturer2], 'Python')
MakeAvStudentsGrade([best_student, bad_student], 'Python')

