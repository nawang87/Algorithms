# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, l):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """

        dicG = {}
        for item in l:
            dicG[item] = True
        p = head
        last = False
        count = 0
        while p:
            if p.val not in dicG:
                last = False
            if p.val in dicG and not last:
                last = True
                count += 1
            p = p.next
        return count

