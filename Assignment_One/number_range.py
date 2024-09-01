x = int(input("Enter the number: "))

if 0 <= x <= 50:
    print("The number is in the range 0-50.")
elif 51 <= x <= 100:
    print("The number is in the range 51-100.")
elif 101 <= x <= 150:
    print("The number is in the range 101-150.")
elif x > 150:
    print("The number is above 150.")
else:
    print("The number is below 0.")