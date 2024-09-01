a = input("Enter a character: ")
vowel = ["a","e","i","o","u"]
for i in vowel:
    if a == i:
        print("Vowel")
        exit()
        
print("Consonant")