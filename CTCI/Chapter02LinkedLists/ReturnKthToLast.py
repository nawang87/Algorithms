class node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None


def printList(head):
    while head != None:
        print(head.val, " ")
        head = head.next


def returnkthtolast(head,k):
    slow = fast = head
    for i in range(k+1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow