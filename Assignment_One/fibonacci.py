def fib(x):
    a,b = 0,1
    
    for _ in range(x):
        print(a, end=" ")
        a,b = b,a+b
        
        
x = int(input("Enter a number: "))
fib(x)