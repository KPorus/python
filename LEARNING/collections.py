import collections

# print(collections.__dict__)
# help(collections)

string = 'Fardin is back'
counter = collections.Counter(string)
print(counter.items())
print(list(counter.elements()))
print(counter.most_common(3)[0][0])


number = collections.deque()

number.append(1)
number.append(2)
number.append(3)
number.append(4)
print(number)

number.extend([5,6,7])
number.extendleft([5,6,7])
number.appendleft(10)
print(number)
number.rotate(-5)
print(number)