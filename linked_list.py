"""Write a doubly linked list class that has a head and tail, both of which point either a linked list node or None.
The class should support :
- Setting the head and tail of the linked list
- Inserting nodes before and after other nodes as well as at given positions.
- Removing given nodes and removing nodes with given values.
- Searching for nodes with given values.

1 <> 2 <> 3 <> 4 <> 5
set_head(4)
4 <> 1 <> 2 <> 3 <> 5

set_tail(6)
4 <> 1 <> 2 <> 3 <> 5 <> 6

insert before (6, 3)
4 <> 1 <> 2 <> 3 <> 5 <> 3 <> 6
insert after (6, 3)

4 <> 1 <> 2 <> 3 <> 5 <> 3 <> 6 <> 3

insert at position (1, 3)
3 <> 4 <> 1 <> 2 <> 3 <> 5 <> 3 <> 6 <> 3

remove Nodes with value (3)
4 <> 1 <> 2 <> 5 <> 6

remove (2)
4 <> 1 <> 5 <> 6

contains node with value (5)
true
"""


# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, node_to_insert):
        if node_to_insert == self.head and node_to_insert == self.tail:
            return
        self.remove(node_to_insert)
        node_to_insert.prev = node.prev
        node_to_insert.next = node
        if node.prev is None:
            self.head = node_to_insert
        else:
            node.prev.next = node_to_insert
        node.prev = node_to_insert

    def insertAfter(self, node, node_to_insert):
        if node_to_insert == self.head and node_to_insert == self.tail:
            return
        self.remove(node_to_insert)
        node_to_insert.prev = node
        node_to_insert.next = node.next
        if node.next is None:
            self.tail = node_to_insert
        else:
            node.next.prev = node_to_insert
        node.next = node_to_insert

    def insertAtPosition(self, position, node_to_insert):
        if position == 1:
            self.setHead(node_to_insert)
            return
        node = self.head
        current_pos = 1
        while node is not None and current_pos != position:
            node = node.next
            current_pos += 1
        if node is not None:
            self.insertBefore(node, node_to_insert)
        else:
            self.setTail(node_to_insert)

    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            node_to_remove = node
            node = node.next
            if node_to_remove.value == value:
                self.remove(node_to_remove)

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.remove_node_bindings(node)

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

	def remove_node_bindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
