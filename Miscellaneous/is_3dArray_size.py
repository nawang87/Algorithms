#Check if a 3d array can be made of the given input size. Also, size 1 for nay dimension is not allowed.

def is_3d_array_size(a_size):
    if a_size<8:
        return False
    factors =[]
    div = 2
    inp = a_size
    while len(factors)<3:
        if a_size%div==0:
            factors.append(2)
            a_size= a_size//div
        else:
            div+=1
        if div >=inp:
            break
    if len(factors) >= 3:
        # print True, factors
        return True

    return False

print(is_3d_array_size(10))#False
print(is_3d_array_size(8)) #True