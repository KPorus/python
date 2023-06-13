# incomplete ==============
from math import ceil
t = int(input())
alice = 0;
win = []
bob = 0;
for i in range(t):
    n = int(input())
    a = input().split(" ")
    d = input()
    if len(d) == 3:
        if d[0] == "R" and int(a[0]) > 0:
            alice += 1
            win.append("P")
        if d[0] == "R" and int(a[0]) <= 0:
            alice += 0
        if d[1] == "P" and int(a[1]) > 0:
            alice += 1
            win.append("S")
        if d[1] == "P" and int(a[1]) <= 0:
            alice += 0
        if d[2] == "S" and int(a[2]) > 0:
            alice += 1
            win.append("R")
        if d[2] == "S" and int(a[2]) <= 0:
            alice += 0
    if len(d) == 2:
        if d[0] == "R" and int(a[0]) > 0:
            alice += 1
            win.append("P")
        if d[0] == "R" and int(a[0]) <= 0:
            alice += 0
        if d[1] == "R" and int(a[1]) > 0:
            alice += 1
            win.append("P")
        if d[1] == "R" and int(a[1]) <= 0:
            alice += 0
        if d[1] == "P" and int(a[1]) > 0:
            alice += 1
            win.append("S")
        if d[1] == "P" and int(a[1]) <= 0:
            alice += 0
        if d[1] == "S" and int(a[1]) > 0:
            alice += 1
            win.append("R")
        if d[1] == "S" and int(a[1]) <= 0:
            alice += 0
        if d[0] == "S" and int(a[1]) > 0:
            alice += 1
            win.append("R")
        if d[0] == "S" and int(a[1]) <= 0:
            alice += 0
        if d[0] == "P" and int(a[1]) > 0:
            alice += 1
            win.append("S")
        if d[0] == "P" and int(a[1]) <= 0:
            alice += 0
    if len(d) == 1:
        if d[0] == "R" and int(a[0]) > 0:
            alice += 1
            win.append("P")
        if d[0] == "R" and int(a[0]) <= 0:
            alice += 0
        if d[0] == "P" and int(a[1]) > 0:
            alice += 1
            win.append("S")
        if d[0] == "P" and int(a[1]) <= 0:
            alice += 0
        if d[0] == "S" and int(a[1]) > 0:
            alice += 1
            win.append("R")
        if d[0] == "S" and int(a[1]) <= 0:
            alice += 0
    check = ceil(n / 2)
    if check <= alice:
        print("YES")
        if len(win) == 3:
            print(win[0] + win[1] + win[2])
        if len(win) == 2:
            print(win[0] + win[1])
        if len(win) == 1:
            print(win[0])
    else:
        print("NO")
    alice = 0