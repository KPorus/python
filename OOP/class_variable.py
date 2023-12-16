class Employee:
    numberOfEmployee = 0
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{}{}@gmail.com".format(self.first,self.last)
        Employee.numberOfEmployee += 1
        pass
    def fullName(self):
        return "{} {}".format(self.first,self.last)
    
emp1 = Employee("Fardin",'Khan',5000000)
emp2 = Employee("Shk",'ali',500000)

print(Employee.numberOfEmployee)