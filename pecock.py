list = [];
result = [];
t = int(input());

for i in range(t):
    n = str(input());
    d = n.split(" ")[0];
    if d == "1":
        list.append(n.split(" ")[1])
    if d == "2" and len(list)>0:
        item = list.pop(0)
        result.append(item)
        list.append(item)

for j in result:
    print(j)