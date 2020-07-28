"""Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

head = 1 -> 2 -> 3 -> 4 -> 5 -> 6 , cycle start = 3,  6 -> 3
head = 1 -> 2 -> 3 -> 4 -> 5 -> 6 , cycle start = 4,  6 -> 4
head = 1 -> 2 -> 3 -> 4 -> 5 -> 6 , cycle start = 1,  6 -> 1
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end="")
            temp = temp.next
        print()


# As we know, finding the cycle in a LinkedList with ‘N’ nodes and also finding the
# length of the cycle requires O(N). Also, as we saw in the above algorithm,
# we will need O(N) to find the start of the cycle. Therefore, the overall
# time complexity of our algorithm will be O(N).
# The algorithm runs in constant space O(1)

"""
So the distance from head to start of cycle is D, from D to overlap of both pointers is P and from P to start of cycle is R.
we know the first pointer x has done path of D + P when they meet. Second one has done twice the path of the first so that's
2P + 2D, but on the meeting point we can actually deduct one P so thats 2D + P.

So to calculate R = second - first = 2D + P - D - P = D, which means from meeting point to cycle start we have exactly D nodes.
Which means we can move first to head and count next together with second which starts from overlapping point. 
"""


def find_cycle_start(head):
    slow = head.next
    fast = head.next.next

    while slow != fast:
        slow = slow.next
        fast = fast.next.next
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()

"""
If we know the length of the LinkedList cycle, we can find the start of the cycle through the following steps:

 - Take two pointers. Let’s call them pointer1 and pointer2.
 - Initialize both pointers to point to the start of the LinkedList.
 - We can find the length of the LinkedList cycle using the approach discussed in LinkedList Cycle. 
Let’s assume that the length of the cycle is ‘K’ nodes.
 - Move pointer2 ahead by ‘K’ nodes.
 - Now, keep incrementing pointer1 and pointer2 until they both meet.
 - As pointer2 is ‘K’ nodes ahead of pointer1, which means, pointer2 must have completed one loop in the cycle when both pointers meet. 
 Their meeting point will be the start of the cycle.


"""

def find_cycle_start_2(head):
    cycle_length = 0
    # find the LinkedList cycle
    slow, fast = head, head
    while (fast is not None and fast.next is not None):
        fast = fast.next.next
        slow = slow.next
        if slow == fast:  # found the cycle
        cycle_length = calculate_cycle_length(slow)
        break
    return find_start(head, cycle_length)

# another solution 
def calculate_cycle_length_2(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
        break
    return cycle_length


def find_start(head, cycle_length):
    pointer1 = head
    pointer2 = head
    # move pointer2 ahead 'cycle_length' nodes
    while cycle_length > 0:
        pointer2 = pointer2.next
        cycle_length -= 1
    # increment both pointers until they meet at the start of the cycle
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1