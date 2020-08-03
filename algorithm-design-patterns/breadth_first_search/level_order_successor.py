"""
Given a binary tree and a node, find the level order successor of the given node in the tree.
The level order successor is the node that appears right after the given node in the level order traversal.
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Time complexity is O(n) where n is the total number of nodes in the tree. We traverse each node once
# The space comlexity is O(n) as we need to return a list containing the level order traversal. We will also
# need O(n) space for the queue. Since we can have maximum of N/2 nodes at any level (this can happen only at lowest level)
# therefore we will need O(n) space to store them in the queue.
def find_successor(root, key):
    if not root or not key:
        return root

    queue = deque()
    queue.append(root)
    while queue:
        current_node = queue.popleft()
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        if current_node.val == key:
            break
    return queue[0] if queue else None


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)


main()
