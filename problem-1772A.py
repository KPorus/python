t = int(input())
sum = []

for i in range(t):
    n = str(input()).split("+");
    x = int(n[0])
    y= int(n[1])
    sum.append(x+y)

for j in sum:
    print(j)