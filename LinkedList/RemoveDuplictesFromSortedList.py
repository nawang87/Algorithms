# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        k = prev = head
        while head.next:
            if head.next.val != prev.val:
                prev.next = head.next
                prev = prev.next
            head = head.next
        prev.next = None
        return k