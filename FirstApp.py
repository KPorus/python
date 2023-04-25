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