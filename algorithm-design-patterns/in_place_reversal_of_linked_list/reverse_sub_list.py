"""
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
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


# Time complexity is O(N) where N is the number of nodes in the list
# Space complexity is O(1)
def reverse_sub_list(head, p, q):
    if p == q:
        return head

    current, previous = head, None

    i = 0
    # p - 1  => 2 - 1 = 1
    while current and i < p - 1:
        previous = current
        current = current.next
        i += 1
    # current = 2
    # previous = 1

    # we are interested in three parts of the Linked List, the part before index p
    # the part between p and q and the part after index q
    last_node_of_first_part = previous
    last_node_of_sub_list = current

    i = 0
    # reverse nodes between p and q
    # q - p + 1 = 4 - 2 + 1 = 3
    while current and i < q - p + 1:
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1

    # connect with the first part
    if last_node_of_first_part:
        last_node_of_first_part.next = previous
    else:
        head = previous
    last_node_of_sub_list.next = current
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()


main()


"""Similar problems
Problem 1: Reverse the first ‘k’ elements of a given LinkedList.

Solution: This problem can be easily converted to our parent problem; to reverse the first ‘k’ nodes of the list, we need to pass p=1 and q=k.

Problem 2: Given a LinkedList with ‘n’ nodes, reverse it based on its size in the following way:

    If ‘n’ is even, reverse the list in a group of n/2 nodes.
    If n is odd, keep the middle node as it is, reverse the first ‘n/2’ nodes and reverse the last ‘n/2’ nodes.

Solution: When ‘n’ is even we can perform the following steps:

    Reverse first ‘n/2’ nodes: head = reverse(head, 1, n/2)
    Reverse last ‘n/2’ nodes: head = reverse(head, n/2 + 1, n)

When ‘n’ is odd, our algorithm will look like:

    head = reverse(head, 1, n/2)
    head = reverse(head, n/2 + 2, n)

Please note the function call in the second step. We’re skipping two elements as we will be skipping the middle element.
"""
