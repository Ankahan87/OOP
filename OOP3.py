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
            grade_num += len(self.student_grades[course])
            for grade in self.student_grades[course]:
                sums_grade += grade
        if grade_num != 0:
            average_grade = sums_grade/grade_num
        return average_grade
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

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

Lecturer1 = Lecturer("Иван Иваныч", "Иванов")
Reviewer1 = Reviewer("Петр Петрович", "Петров") 
print(best_student.grades)
print(Lecturer1.name, Lecturer1.surname)
print(Reviewer1.name, Reviewer1.surname)

best_student.rate_lectors(Lecturer1, 'Python', 10)
print(Lecturer1.student_grades)
Lecturer1.courses_attached += ['Python']
best_student.rate_lectors(Lecturer1, 'Python', 10)
print(Lecturer1.student_grades)
best_student.rate_lectors(Lecturer1, 'Python', 8)
best_student.rate_lectors(Lecturer1, 'Python', 7)
best_student.rate_lectors(Lecturer1, 'Python', 9)
print(Lecturer1)
print(Reviewer1)
print(best_student)
