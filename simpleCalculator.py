#q = input("what do you want (sum, multipilication, add, division) than enter(+,-,*,/) ");
#print(q)
while 1 :
    def div(x, y):
        return x/ y
    def multi(x, y):
        return x * y
    def sub(x, y):
        return x - y
    def add(x, y):
        return x + y

    #n = int(input("How many number you want to calculate(only 2 number): "))
    #i = 0
    #while i < n:
     #   num1 = float(input("Enter a number: "))
      #  i += 1
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter a number: "))

    q = input(
        "what do you want (sum, multipilication, add, division) than enter(+,-,*,/) // if you want to exit than press 0 ")
    if q == '0':
        print("exit....")
        break
    if q == "+":
        print("result of addition: ", add(num1, num2))
    elif q == "-":
        print("result of subtraction: ", sub(num1,num2))
    elif q == "/":
        print("result of division: ", div(num1,num2))
    elif q == "*":
        print("result of multiplication: ", multi(num1,num2))
    """ if n > 1:
        q = input(
            "what do you want (sum, multipilication, add, division) than enter(+,-,*,/) // if you want to exit than press 0 ")
        if  q == '0':
            print("exit....")
            break
        if q == "+":
            print("result of addition: ", add(num1,num2))
    else:
            print("You enter only one number. ") """




