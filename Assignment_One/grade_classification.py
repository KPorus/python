grade = int(input("Enter the grade: "))

if grade >=90:
    print("A+")
elif grade >=80 and grade <= 89:
    print("A")
elif grade >=70 and grade <=79:
    print("C")
elif grade >=60 and grade <=69:
    print("B")
elif grade <60:
    print("Fail")