def digitOfNumber(x):
    if x == 0:
        print(0)
        exit()
    
    c = 0
    while x != 0:
        x //=10
        c+=1
    print(c)
    
x = int(input('Enter a number: '))
digitOfNumber(x)