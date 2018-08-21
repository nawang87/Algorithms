def checkpalindrom(str):
    map = {}
    for letter in str:
        if letter not in map:
            map[letter]=1
        else:
            map[letter]+=1
    odd =0
    for k,v in map.items():
        if v%2 !=0:
            odd+=1
        if odd>1:
            return False
    return True

print(checkpalindrom("aba"))