"""
Bubble Sort is the simplest sorting algorithm that works
by repeatedly swapping the adjacent elements if they are in wrong order.
"""

def bubbleSort(arr):
    swap = len(arr)
    while not swap is 0:
        swap = 0
        for i in range(0,len(arr)-1):
            j = i+1
            if(arr[i]>arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                swap +=1
    return arr

arr = [9,8,4,5,6,7,0,1]
sor = [64, 25, 12, 22, 11]
alreadysorted = [11, 12, 22, 25, 64]
print(bubbleSort(arr))