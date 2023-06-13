array = []
t = int(input("Enter the size of array "))

for i in range(t):
    value = int(input("Enter a value "))
    array.append(value)

print(array)

for j in range(0,t-1):
    for i in range(1,t):
        if array[j]>array[i]:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp

print(array)