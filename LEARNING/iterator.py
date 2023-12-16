mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
for i in range(len(mytuple)):
	print(next(myit))

string = "Fardin"
it = iter(string)

for i in range(len(string)):
    print(next(it))
    
for item in string:
    print(item)
    
    
class Numbers:
    def __init__(self,a) :
        self.a = a

    def __iter__(self):
        return self
    
    def __next__(self):
        self.a = self.a + 1
        return self.a
    
num = Numbers(0)
ite = iter(num)

for i in range(5):
    print(next(num))