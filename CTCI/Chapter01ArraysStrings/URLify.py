def urilfy(str):
    count = 0
    i = len(str)-1
    for letter in str:
        if letter is " ":
            count +=1
    str+=" "*count*2
    j = len(str)-1
    str = list(str)
    while i!=j:
        if str[i]!=" ":
            temp = str[i]
            str[i]=str[j]
            str[j]=temp
            i-=1
            j-=1
        else:
            str[j]='0'
            str[j-1]='2'
            str[j-2]='%'
            j-=3
            i-=1
    return "".join(str)


def replace(a,b):
    temp = a
    a = b
    b = temp
    return a,b

def urilfy1(str):
    return str.replace(' ','%20')

print(urilfy("Hey Sexy Sam"))
