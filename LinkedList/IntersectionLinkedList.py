# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pointA = headA
        sizeA = 0
        while pointA:
            sizeA += 1
            pointA = pointA.next
        pointB = headB
        sizeB = 0
        while pointB:
            sizeB += 1
            pointB = pointB.next
        pointA, pointB = headA, headB
        if sizeA > sizeB:
            for _ in range(sizeA - sizeB):
                pointA = pointA.next
        else:
            for _ in range(sizeB - sizeA):
                pointB = pointB.next
        while pointA is not pointB:
            pointA, pointB = pointA.next, pointB.next
        return pointA


