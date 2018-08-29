
# Build
# Clear
# FIndMinimum
# ExtractMinimum
# Insert
# isempty
# Size
# heapify
# delete
# union
# decreasekey

from heapq import heappush, heappop, heapify


# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining
#             heap invarient
# heapify - transform list into heap, in place, in linear time

class MinHeap:
    # Constructor to initialize a heap
    def __init__(self):
        self.heap = []

    #Minimum Element
    def findMinimum(self):
        return self.heap[0]

    #ExtractMinimum - Delete the minimum element
    def extractMinimum(self):
        return heappop(self.heap)

    #Delete an element - Make the element -infinity and extract minimum
    def delete(self,item):
        self.decreseKey(item, float('-inf'))
        self.extractMinimum()

    #Insert New Element
    def insert(self,item):
        return heappush(self.heap,item)

    #Decrease Key
    def decreaseKey(self,index,newVal):
        self.heap[index] = newVal
        while(self.heap[index] < self.heap[self.parent(index)]):
            self.heap[index]= self.heap[self.parent(index)]
            self.heap[self.parent(index)] = newVal
        return self.heap

    #returns parent
    def parent(self,index):
        if index == 0 : return 0
        return (index-1)//2

    #Print the heap
    # def print(self):




heapObj = MinHeap()
heapObj.insert(1)
heapObj.insert(4)
heapObj.insert(6)
heapObj.insert(17)
heapObj.insert(3)
heapObj.insert(2)
heapObj.insert(9)
heapObj.insert(8)
print(heapObj.findMinimum())
# print(heapObj.extractMinimum())
print(heapObj.findMinimum())
print(heapObj.parent(8))
heapObj.decreaseKey(2,5)
print(heapObj.parent(0))



