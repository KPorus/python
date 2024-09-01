x = int(input("Enter the number: "))
def fact(x):
    if x < 1:
        print("Negative number. no factorial")
        exit()
        
        
    result = 1
    i = x

    while i >1:
        result *=i
        i -=1
        
    return result

print(fact(x))
        
    