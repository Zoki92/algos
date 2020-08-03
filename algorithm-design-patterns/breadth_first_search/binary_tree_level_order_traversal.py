"""
Given a binary tree, populate an array to represent its level-by-level traversal.
You should populate the values of all nodes of each level from left to right in separate sub-arrays.

[1, 2, 3, 4, 5, 6, 7]
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
def traverse(root):
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.append(current_level)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
