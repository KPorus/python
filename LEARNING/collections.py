import collections

# print(collections.__dict__)
# help(collections)

string = 'Fardin is back'
counter = collections.Counter(string)
print(counter.items())
print(counter.most_common(3))
