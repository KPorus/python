x = int(input("enter 1st the number: "))
y = int(input("enter 2nd the number: "))
print(f"Before swaping numbers x:{x} and y:{y}")
res = x+y
x = y
y = res-x
print(f"After swaping numbers x:{x} and y:{y}")