"""
Given a binary tree, find the length of its diameter. The diameter of a tree is the
number of nodes on the longest path between any two leaf nodes. The diameter of a tree may or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.
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
class TreeDiameter:
    def __init__(self):
        self.treeDiameter = 0

    def find_diameter(self, root):
        self.calculate_height(root)
        return self.treeDiameter

    def calculate_height(self, current_node):
        if not current_node:
            return 0

        left_tree_height = self.calculate_height(current_node.left)
        right_tree_height = self.calculate_height(current_node.right)

        # diameter at the current node will be equal to the height of the left subtree
        # and the height of the right subtree + 1 for the current node
        diameter = left_tree_height + right_tree_height + 1

        self.treeDiameter = max(self.treeDiameter, diameter)
        # height of the current tree node will be equal to the maximum of the heights of
        # left and right subtrees plus 1 for the current node
        return max(left_tree_height, right_tree_height) + 1


def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()

