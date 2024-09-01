x = int(input("Enter 1st value: "))
y = int(input("Enter 2nd value: "))
z = int(input("Enter 3rd value: "))

if x + y > z or x + z > y or y + z > x:
    print("Triangle is created")
else:
    print(" invalid Triangle")
    