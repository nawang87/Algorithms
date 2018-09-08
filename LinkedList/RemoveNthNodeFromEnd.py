# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        h = prev = ListNode('a')
        prev.next = nth = head
        while n > 0:
            nth = nth.next
            n -= 1
        while nth:
            nth = nth.next
            prev = prev.next

        prev.next = prev.next.next
        return h.next