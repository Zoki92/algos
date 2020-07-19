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

    def getNthNode(self, n):
        counter = 1
        current = self
        while counter < n:
            current = current.next
            counter += 1
        return current
        
def find_loop(head):
    first = head.next
    second = head.next.next
    while first != second:
        first = first.next
        second = second.next.next
        
    first = head
    while first != second:
        first = first.next
        second = second.next
        
    return first


test = LinkedList(0).addMany([1,2,3,4,5,6,7,8,9])
test.getNthNode(10).next = test.getNthNode(5)

print(find_loop(test))