"""
Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
"""


from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


# Time complexity is O(n)
# Space complexity is O(1)
def reverse_alternate_k_elements(head, k):
    if k <= 1 and not head:
        return head

    current, previous = head, None

    while True:
        last_node_of_first_part = previous
        last_node_of_sub_list = current

        next = None
        i = 0
        while current and i < k:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        if last_node_of_first_part:
            last_node_of_first_part.next = previous
        else:
            head = previous

        last_node_of_sub_list.next = current

        i = 0
        # skip k nodes
        while current and i < k:
            previous = current
            current = current.next
            i += 1

        if not current:
            break

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = reverse_alternate_k_elements(head, 2)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()


main()
