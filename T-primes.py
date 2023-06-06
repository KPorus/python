from math import sqrt
t= int(input())
list = []
def isPrime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    k = int(sqrt(n))+1
    for i in range(5,k,6):
        if n % i == 0 or n % (i+2) == 0:
            return  False
    return True
def isTprimes(n):
    sq = int(sqrt(n))

    if (sq * sq != n):
        return False

    if (isPrime(sq)):
        return True
    else:
        return False

for i in range(t):
    num = int(input())
    if isTprimes(num):
        list.append("Yes")
    else:
        list.append("NO")

for j in list:
    print(j)
