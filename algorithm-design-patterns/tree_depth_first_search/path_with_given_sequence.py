"""
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree.
# This is due to the fact that we traverse each node once.
# The space complexity of the above algorithm will be O(N) in the worst case. This space will be used to store the recursion stack.
# The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
def find_path(root, sequence):
    if not root:
        return len(sequence) == 0

    return find_path_recursive(root, sequence, 0)


def find_path_recursive(current_node, sequence, sequence_index):
    if not current_node:
        return False

    seq_len = len(sequence)

    if sequence_index >= seq_len or current_node.val != sequence[sequence_index]:
        return False

    # If the current node is a leaf, and it is the end of sequence, we have found a path!
    if (
        current_node.left is None
        and current_node.right is None
        and sequence_index == seq_len - 1
    ):
        return True

    # Recursively call to traverse the left and the right sub-tree
    # return true if any of the two recursive calls return True
    return find_path_recursive(
        current_node.left, sequence, sequence_index + 1
    ) or find_path_recursive(current_node.right, sequence, sequence_index + 1)


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(my_func(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(my_func(root, [1, 1, 6])))


main()

