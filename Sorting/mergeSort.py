"""
Given two separate lists A and B ordered from least to greatest, construct a list C by repeatedly
comparing the least value of A to the least value of B, removing the lesser value, and appending it
onto C. When one list is exhausted, append the remaining items in the other list onto C in order.
The list C is then also a sorted list
"""

def mergeSort(list):
    if len(list) < 2:
        return list
    middle = len(list) // 2
    left = mergeSort(list[:middle])
    right = mergeSort(list[middle:])
    return merge(left, right)


def merge(left, right):
    output = []
    i, j = 0,0
    while i<len(left) and j < len(right):
        if left[i]<=right[j]:
            output.append(left[i])
            i+=1
        else:
            output.append((right[j]))
            j+=1
    output += left[i:]
    output += right[j:]
    return output

arr = [9,8,4,5,6,7,0,1]
sor = [64, 25, 12, 22, 11]
alreadysorted = [11, 12, 22, 25, 64]
print(mergeSort(arr))
left = [1,3,5,9,25]
right = [2,6,9,21,32]
# print(merge(left,right))