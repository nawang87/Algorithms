def isMinHeap(arr):
    for i in range(len(arr)//2 +1):
        l = 2 *i +1
        r = 2 *i + 2
        if l<len(arr)-1 and arr[l]<arr[i]:
            return False
        if r<len(arr)-1 and arr[r]<arr[i]:
            return False
    return True

print(isMinHeap([30, 56, 22, 49, 30, 51, 2, 67]))

