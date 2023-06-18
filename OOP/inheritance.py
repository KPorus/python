class Person:
    def __init__(self, name, age, org):
        self.name = name
        self.age = age
        self.org = org

class Manager(Person):
    def __init__(self, name, age, org, role):
        super().__init__(name, age, org)
        self.role = role

class Organization:
    def __init__(self):
        self.persons = []

    def add_person(self, person):
        self.persons.append(person)

    def show_persons(self):
        return [person.name for person in self.persons]

org = Organization()
p1 = Manager("Fardin", 23, "Across the Globe", "admin")
p2 = Manager("omair", 25, "Across the Globe", "manager")
org.add_person(p1)
org.add_person(p2)

print(org.show_persons())
