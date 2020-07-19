"""Merge two sorted linked lists"""
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
        
def mergeLinkedLists(headOne, headTwo):
    first = headOne
    second = headTwo
    prev = None
    
    while first and second:
        if first.value < second.value:
            prev = first
            first = first.next
        else:
            if prev:
                prev.next = second
            prev = second
            second = second.next
            prev.next = first
            
    if first is None:
        prev.next = second      

     
    return headTwo if headOne.value > headTwo.value else headOne



list1 = LinkedList(2).addMany([6, 7, 8])
list2 = LinkedList(1).addMany([3, 4, 5, 9, 10])

output = mergeLinkedLists(list1, list2)

print(output.getNodesInArray())