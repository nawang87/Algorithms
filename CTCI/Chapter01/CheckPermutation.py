#O(n)
def checkPermutation1(str1, str2):
    if len(str1) != len(str2):
        return False
    map ={}
    for letter in str1:
        if letter not in map:
            map[letter]=1
        else:
            map[letter]+=1
    for letter in str2:
        if letter not in map:
            return False
        else:
            map[letter]-=1
    for k, v in map.items():
        return v == 0


#O(nlogn)
def checkPermutation2(str1,str2):
    str1 = sorted(str1)
    str2 = sorted(str2)
    return str1== str2

print(checkPermutation1('abc', 'cba'))

