def palindrome(s):
    return s[::-1]

s = input("Enter a string: ")
if s==palindrome(s):
    print("True")
else:
    print("False")