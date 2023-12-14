try:
    a = int(input("Enter a first number")) / int(input("Enter a second number"))
    print(f"Result: {a}")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError as v:
    print(f"error: {v}")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("\nPlease enter correctly.")
