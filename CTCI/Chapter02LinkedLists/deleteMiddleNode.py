class node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None


def printList(head):
    while head != None:
        print(head.val, " ")
        head = head.next


def deletemiddle(node):
    node.val = node.next.val
    node.next = node.next.next