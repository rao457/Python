class Student:
    def __init__(self, name , age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade
class Course:
    def __init__(self, name, max_student):
        self.max_student = max_student
        self.student = []
    def add_student(self, student):
        if len(self.student) < self.max_student:
            self.student.append(student)
            return True
        else:
            return False
    def average_grade(self):
        value = 0
        for student in self.student:
            value += student.get_grade()
        return int(value / len(self.student))
s1 = Student('zohaib', 21, 95)
s2 = Student('sajid', 22, 65)
s3 = Student('Noor Shah', 75, 100)
course = Course('IEEE', 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print(course.average_grade())

