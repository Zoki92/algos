"""
Right View of a Binary Tree (easy) #

Given a binary tree, return an array containing nodes in its right view. The right view of a binary 
tree is the set of nodes visible when the tree is seen from the right side.
"""


from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Time complexity is O(n) where n is the total number of nodes in the tree. We traverse each node once
# The space comlexity is O(n) as we need to return a list containing the level order traversal. We will also
# need O(n) space for the queue. Since we can have maximum of N/2 nodes at any level (this can happen only at lowest level)
# therefore we will need O(n) space to store them in the queue.
def tree_right_view(root):
    if not root:
        return
    queue = deque()
    result.append(root.val)

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            current_node = queue.popleft()
            # if i is in the last node of this level add it to the result
            if i == level_size - 1:
                result.append(current_node)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.righ)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end="")
