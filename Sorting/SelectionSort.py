"""
The selection sort algorithm sorts an array by repeatedly finding the minimum element
 (considering ascending order) from unsorted part and putting it at the beginning.
"""

def selectionSort(arr):
    k = arr
    elem = arr[0]
    for i in range(0,len(arr)):
        elem = arr[i]
        for j in range(i+1, len(arr)):
            if(arr[j]<elem):
                elem = arr[j]
                index= j
        if elem is not arr[i]:
            arr[index] = arr[i]
            arr[i] = elem
    return arr

arr = [9,8,4,5,6,7,0,1]
sor = [64, 25, 12, 22, 11]
print(selectionSort(sor))