"""Reverse linked list"""

def reverseLinkedList(head):
    p1, p2 = None, head
    while p2:
        p3 = p2.next
        p2.next = p1
        p3.next = p2
        p1 = p2
        p2 = p3
    return p1