val = input()
m = int(val.split(" ")[0])
n = int(val.split(" ")[1])
a = int(val.split(" ")[2])
x = 0
y =0
if m%a == 0 :
    x = int(m/a);
else:
    x = int(m/a + 1)

if n%a == 0:
    y = int(n/a)
else:
    y = int(n/a + 1)

print(x*y)