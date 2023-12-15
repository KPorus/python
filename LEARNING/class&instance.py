class Employee:
    def __init__(self, first, last, paid):
        self.first = first
        self.last = last
        self.paid = paid
        self.email = f"{first}.{last}@gmail.com"
    
    def fullName(self):
        return ("{0} {1}".format(self.first,self.last))

emp1 = Employee("fardin","khan","5000000")
emp2 = Employee("shk","ali","1000000")

print("Name of first employee " + emp1.fullName())
print("Name of second employee " +emp2.fullName())

print(emp1.email)
print(emp2.email)