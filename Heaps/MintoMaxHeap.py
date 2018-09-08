from heapq import heapify
def mintomax(arr):
    n = len(arr) - 1
    while n > 0:
        arr[0], arr[n] = arr[n], arr[0]
        k = arr[:n]
        heapify(k)
        arr =k + arr[n:]
        n -= 1
    return arr

print(mintomax([1,2,3,4,5,6]))
print(mintomax([3,5,9,6,8,20,10,12,18,9]))
