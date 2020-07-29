"""
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original form once the 
algorithm is finished. The algorithm should have O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true

Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):  #
    if not head or not head.next:
        return True

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    head_second_half = reverse(slow)
    copy_head_second_half = head_second_half

    while head and head_second_half:
        if head.value != head_second_half.value:
            break
        head = head.next
        head_second_half = head_second_half.next

    reverse(copy_head_second_half)

    if head is None or head_second_half is None:
        return True
    return False


# The above algorithm will have a time complexity of O(N) where ‘N’ is the number of nodes in the LinkedList.
# The algorithm runs in constant space O(1)
def reverse(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
