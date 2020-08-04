"""
Given a binary tree, connect each node with its level order successor. 
The last node of each level should point to the first node of the next level.
"""

from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end="")
        current = self
        while current:
            print(str(current.val) + " ", end="")
            current = current.next


# Time complexity is O(n) where n is the total number of nodes in the tree. We traverse each node once
# The space comlexity is O(n) as we need to return a list containing the level order traversal. We will also
# need O(n) space for the queue. Since we can have maximum of N/2 nodes at any level (this can happen only at lowest level)
# therefore we will need O(n) space to store them in the queue.
def connect_all_siblings(root):
    if not root:
        return root

    queue = deque()
    queue.append(root)
    previous_node = None
    current_node = None
    while queue:
        current_node = queue.popleft()
        if previous_node:
            previous_node.next = current_node
        previous_node = current_node
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()


main()
