"""
Write a function that takes in the head of a Singly Linked list and an integer k and removes the kth
node from the end of the list
Each Linked List node has an integer value as well as next node pointing to the next node in the list or to None if
its the tail of the list.
You can assume that the input Linked list will always have atleast 2 nodes and more specifically atleast k nodes.

head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
k = 4
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9

One way to do this would be to have counter 
"""

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes

def removeKthNodeFromEnd(head, k):
    node = head
    counter = 1
    hash_map = {}
    while node:
        counter += 1
        hash_map[counter] = node
        node = node.next
    removed = max(hash_map.keys()) - k + 1
    removed_before = removed - 1
    removed_after = removed + 1

    hash_map[removed_before].next = hash_map[removed_after]


test = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
        
print(test.getNodesInArray())
removeKthNodeFromEnd(test, 1)
print(test.getNodesInArray())
