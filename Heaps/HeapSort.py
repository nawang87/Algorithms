class HeapSort:
    def heapify(self,arr,n,i):
        largest = i
        left = 2 *i +1
        right = 2 *i +2

        if left <n and arr[largest]<arr[left]:
            largest = left

        if right <n and arr[largest]<arr[right]:
            largest = right

        if largest != i:
            temp = arr[i]
            arr[i]= arr[largest]
            arr[largest]= temp

            #heapify the child tree
            self.heapify(arr,n,i)

    def sort(self,arr):
        n = len(arr)
        for i in range(len(arr)//2 +1, -1, -1):
            self.heapify(arr, n,i)

        i = 0
        for i in range(n - 1, 0, -1):
            arr[0],arr[i]=arr[i],arr[0]
            self.heapify(arr,i,0)
        return arr

arr = [ 12, 11, 13, 5, 6, 7]
s = HeapSort()
print(s.sort(arr))

