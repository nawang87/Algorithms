from heapq import heapify,heappop, heappush
def sort(arr,k):
    aux = []
    temp = []
    heapify(temp)
    for i in range(0,len(arr)):
        if i >k:
            aux.append(heappop(temp))
        heappush(temp,arr[i])
    while len(temp)>0:
        aux.append(heappop(temp))
    return aux

print(sort([2, 6, 3, 12, 56, 8,9], 3))