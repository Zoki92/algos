"""
Find the path with the maximum sum in a given binary tree. Write a function that
returns the maximum sum. A path can be defined as a sequence of nodes between any
two nodes and doesn’t necessarily pass through the root.
"""

import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaximumPathSum:

    # The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes
    # in the tree. This is due to the fact that we traverse each node once.
    # The space complexity of the above algorithm will be O(N) in the worst case.
    # This space will be used to store the recursion stack. The worst case will happen
    # when the given tree is a linked list (i.e., every node has only one child).
    def find_maximum_path_sum(self, root):
        self.global_max = -math.inf
        self.find_maximum_path_sum_recursive(root)
        return self.global_max

    def find_maximum_path_sum_recursive(self, current_node):
        if not current_node:
            return 0

        max_path_sum_from_left = self.find_maximum_path_sum_recursive(current_node.left)
        max_path_sum_from_right = self.find_maximum_path_sum_recursive(
            current_node.right
        )

        # Ignore paths with negative sum, since we need to find the maximum we should
        # ignore any path which has an overall negative sum
        max_path_sum_from_left = max(max_path_sum_from_left, 0)
        max_path_sum_from_right = max(max_path_sum_from_right, 0)

        # Max path at current node will be equal to the sum of the left subtree and
        # the right subtree plus the val of the current node
        local_maximum_sum = (
            max_path_sum_from_left + max_path_sum_from_right + current_node.val
        )
        self.global_max = max(self.global_max, local_maximum_sum)
        return max(max_path_sum_from_left, max_path_sum_from_right) + current_node.val


def my_func(root):
    global_max = -math.inf
    my_func_recursive(root)
    return global_max


def my_func_recursive(current_node):
    if not current_node:
        return 0

    sum_path_left_subtree = my_func_recursive(current_node.left)
    sum_path_right_subtree = my_func_recursive(current_node.right)

    max_sum_path_left_subtree = max(sum_path_left_subtree, 0)
    max_sum_path_right_subtree = max(sum_path_right_subtree, 0)

    local_max = (
        max_sum_path_left_subtree + max_sum_path_right_subtree + current_node.val
    )

    global_max = max(global_max, local_max)

    return max(max_sum_path_left_subtree, max_sum_path_right_subtree) + current_node.val


def main():
    max_path_sum = MaximumPathSum()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(max_path_sum.find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(max_path_sum.find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(max_path_sum.find_maximum_path_sum(root)))


main()
