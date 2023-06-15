def linear_search(array,key):
    print("key",key)
    for i in range(len(array)):
        if (array[i] == key):
            return i
    return "Not Found"

array = []
t = int(input("Enter a size for array "))

for i in range(t):
    value = int(input("Enter a number "))
    array.append(value)
print(array)
#Descending order
for i in range(1,t):
    store = array[i]
    for j in range(0,t):
        if store > array[j]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

print(array)

key = int(input("Enter a value to search "))
print(linear_search(array,key))