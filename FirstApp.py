# there is no need to define variable as (int, double)
x = 10
y = 10.20
z = "anika"
addition = x + y

# function for addition
def sum(x,y):
    return  x + y
print(sum(x,y))

print("hello world",z)

#string
firstName = "fardin"
lastName = "khan"
print(firstName,lastName)

statement = "Fardin khan is a node js developer"
#find is in statement using find function which return first index number of seacrhing value
print(statement.find("is"))

# finding "is" in statement which return bool
print("is" in statement)

#capitalize() function used to capitalize the string
print(statement.capitalize())

#split() to split the string in array
print(statement.split(" "))

#lists which work as array
num = [10,5,6,8,9,40];
print("list:", num)
print("lists first value: ",num[0])
print("lists last value: ",num[-1])
