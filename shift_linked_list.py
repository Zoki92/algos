"""Write a function that takes the Head of a Singly Linked list and an integer k, shifts the list in place
and returns its new head.
Whether nodes are moved forward or backward is determined by k, whether is positive or negative.
"""


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time O(1) space
def shiftLinkedList(head, k):
    list_length = 1
    list_tail = head

    while list_tail.next:
        list_tail = list_tail.next
        list_length += 1
    
    offset = abs(k) % list_length
    if offset == 0:
        return head
    
    new_tail_position = list_length - offset if k > 0 else offset
    new_tail = head

    for i in range(1, new_tail_position):
        new_tail = new_tail.next
        
    new_head = new_tail.next
    new_tail.next = None
    list_tail.next = head
    return new_head

def linkedListToArray(head):
    array = []
    current = head
    while current is not None:
        array.append(current.value)
        current = current.next
    return array



def shiftLinkedList2(head, k):
    current = head
    list_length = 1

    while current.next:
        list_length += 1
        current = current.next
    
    break_point = list_length - k if k > 0 else k

    i = 1
    node = head
    while i <= list_length:
        if i == abs(break_point):
            break
        node = node.next
        i += 1
    
        
    new_head = node.next
    node.next = None
    current.next = head
    return new_head












head = LinkedList(0)
head.next = LinkedList(1)
head.next.next = LinkedList(2)
head.next.next.next = LinkedList(3)
head.next.next.next.next = LinkedList(4)
head.next.next.next.next.next = LinkedList(5)

# result = shiftLinkedList(head, -2)
result = shiftLinkedList2(head, -2)
array = linkedListToArray(result)

print(array)