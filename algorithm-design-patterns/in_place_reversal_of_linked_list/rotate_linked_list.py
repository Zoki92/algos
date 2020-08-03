"""
Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.
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


def rotate(head, rotations):
    if head is None or head.next is None or rotations <= 0:
        return head

    # find the length and the last node of the list
    last_node = head
    list_length = 1

    while last_node.next:
        last_node = last_node.next
        list_length += 1
    # 1 2 3 4 5 6
    last_node.next = head
    # 6 points to 1 now so we have circular list
    # no need to do rotations more than the length of the list
    # 3 % 6 = 3
    rotations %= list_length
    # skip_length = 6 - 3 = 3
    skip_length = list_length - rotations

    # last node is head, 1
    last_node_of_rotated_list = head
    for i in range(skip_length - 1):
        last_node_of_rotated_list = last_node_of_rotated_list.next

    # this is 4, so head start from 4, or last node of rotated list
    head = last_node_of_rotated_list.next

    # this is node 3 where it points to None
    last_node_of_rotated_list.next = None

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = my_func(head, 3)
    print("Nodes of rotated LinkedList are: ", end="")
    result.print_list()


main()
