def checkRotation(s1, s2):
    s2+=s2
    return s1 in s2

s1 = 'waterbottle'
s2 = 'erbottlewa'

print(checkRotation(s1,s2))
