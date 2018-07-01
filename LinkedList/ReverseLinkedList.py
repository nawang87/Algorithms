# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        items = []
        while head:
            items.append(head.val)
            head = head.next

        pointer = head = ListNode(0)
        i = 0
        k = len(items)
        for i in range(k):
            pointer.next = ListNode(items.pop())
            pointer = pointer.next
        return head.next