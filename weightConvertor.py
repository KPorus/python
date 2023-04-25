num = int(input("Enter your weight: "))
c = input("K(g) or (L)bs ")

if c.upper() == "K":
    print("your weight in L(bs): ",num/0.454)
elif c.upper() == "L" :
    print("your weight in kg: ", num * 4.54)