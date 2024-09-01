x = int(input("Enter a number: "))

def sumOfeven(x):
    sum = 0
    for i in range(2,x+1,2):
        sum +=i
    print(f"Sum of even: {sum}")
        
sumOfeven(x)