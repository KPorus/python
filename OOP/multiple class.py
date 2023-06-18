class students:
    def __init__(self,name,age,gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def get_grade(self):
        return (self.name,self.gpa)

class courses:
    def __init__(self,name,max_student):
        self.name = name
        self.max_student = max_student
        self.students = []

    def add_student(self,student):
        if ((len(self.students)) < self.max_student):
            self.students.append(student)
            return "Student added"
        return "Student not added"

    def show_students(self):
        return [student.name for student in self.students]

    def average_gpa(self):
        value = 0
        for student in self.students:
            value += student.gpa
        return value/len(self.students)

s1 = students("Fardin",23,3.90)
s2 = students("Omair",25,3.64)

course = courses("Javascript",5)
print(s1.get_grade())
print(course.add_student(s1))
print(course.add_student(s2))
print(course.show_students())
print(course.average_gpa())