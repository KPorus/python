def permutation_recursive(s,pocket=""):
    if len(s) == 0:
        print(pocket)
    else:
        for i in range(len(s)):
            letter = s[i]
            front = s[0:i]
            back = s[i+1:]
            total = front + back
            permutation_recursive(total,letter + pocket)
print(permutation_recursive("AB",""))