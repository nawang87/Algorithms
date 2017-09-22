"""

At each iteration, insertion sort removes one element from the input data,
finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain
"""

def insertionSort(arr):
    i = 1
    while i < len(arr):
        key = arr[i]
        index = i
        for j in range(i-1, -1, -1):
            print(j)
            if(key<arr[j]):
                arr[j+1] = arr[j]
                index = j
        arr[index] = key
        print("Array = ", arr)
        i+=1

    return arr

arr = [9,8,4,5,6,7,0,1]
sor = [64, 25, 12, 22, 11]
alreadysorted = [11, 12, 22, 25, 64]
print(insertionSort(sor))