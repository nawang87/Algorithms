# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        k = prev = ListNode(0)
        prev.next = head
        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return k.next
