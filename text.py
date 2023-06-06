t = int(input())
i = 0
data = []
def check(str1):
    l = len(str1)
    if l <= 10:
        print(str1)
    else:
        print(str(str1[0]) + str(l - 2) + str(str1[l - 1]))

while(i != t):
    str1 = input()
    data.append(str1)
    i += 1

for i in data:
    check(i)