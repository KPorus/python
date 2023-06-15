#sort, import,delete,show using class
class Student:
    info = []

    def __init__(self, name, roll, GPA):
        self.name = name
        self.roll = roll
        self.GPA = GPA
        Student.info.append({"name": self.name, "roll": self.roll, "GPA": self.GPA})

    def show_data(self):
        return Student.info

    def show_sort_data(self):
        n = len(Student.info)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if Student.info[j]["roll"] > Student.info[j+1]["roll"]:
                    Student.info[j], Student.info[j+1] = Student.info[j+1], Student.info[j]

    def delete_data(self, roll):
        n = len(Student.info)
        for i in range(n):
            if Student.info[i]["roll"] == roll:
                Student.info.pop(i)
                break

Data = Student("Fardin", 451, 3.90)
Data = Student("Omair", 411, 3.64)
Data = Student("Robiul", 445, 3.55)
Data = Student("Ali", 431, 3.54)

print(Data.show_data())
Data.show_sort_data()
print("Sorted Data--", Data.show_data())

Data.delete_data(445)
print("Data after deletion--", Data.show_data())
