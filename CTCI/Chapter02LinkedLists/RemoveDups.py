class node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None
def printList(head):
    while head != None:
        print(head.val, " ")
        head = head.next

start = node(10)
start.next = node(12)
start.next.next = node(11)
start.next.next.next = node(11)
start.next.next.next.next = node(13)
start.next.next.next.next.next = node(11)
start.next.next.next.next.next.next = node(15)


def removedups(head):
    k = prev = node('$')
    prev.next = head
    history = {}
    while head:
        if head.val not in history:
            history[head.val] = 1
            prev.next = head
            prev = prev.next
        head = head.next
    prev.next = None

    printList(k.next)

removedups(start)
