"""
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""The time complexity of the above algorithm is O(N^2), where ‘N’ is the total number
of nodes in the tree. This is due to the fact that we traverse each node once (which will take O(N)), 
and for every leaf node we might have to store its path which will take O(N).
If we ignore the space required for the allPaths list, the space complexity of the above algorithm will be O(N) in the worst case. 
This space will be used to store the recursion stack. 
The worst case will happen when the given tree is a linked list (i.e., every node has only one child).

Here we have seven nodes (i.e., N = 7). Since, for binary trees, there exists only one path to reach any leaf node, 
we can easily say that total root-to-leaf paths in a binary tree can’t be more than the number of leaves. 
As we know that there can’t be more than N/2 leaves in a binary tree, therefore the maximum number of 
elements in allPaths will be O(N/2)=O(N). Now, each of these paths can have many nodes in them. 
For a balanced binary tree (like above), each leaf node will be at maximum depth. As we know that the depth (or height) 
of a balanced binary tree is O(logN) we can say that, at the most, each path can have logN nodes 
in it. This means that the total size of the allPaths list will be O(N∗logN). If the tree is not balanced,
we will still have the same worst-case space complexity.

From the above discussion, we can conclude that the overall space complexity of our algorithm is O(N∗logN).

Also from the above discussion, since for each leaf node, in the worst case, we have to copy log(N) nodes to store its path,
therefore the time complexity of our algorithm will also be O(N∗logN).
"""


def find_paths(root, required_sum):
    allPaths = []
    find_paths_recursive(root, required_sum, [], allPaths)
    return allPaths


def find_paths_recursive(current_node, required_sum, current_path, allPaths):
    if current_node is None:
        return

    current_path.append(current_node.val)

    if (
        current_node.val == required_sum
        and current_node.left is None
        and current_node.right is None
    ):
        # add it as a list because will have, [[12, 7, 4], [12, 1, 10]]
        allPaths.append(list(current_path))
    else:
        find_paths_recursive(
            current_node.left, required_sum - current_node.val, current_path, allPaths
        )
        find_paths_recursive(
            current_node.right, required_sum - current_node.val, current_path, allPaths
        )
    # if we don't find the required sum in the path we need to delete this path
    # when going up recursively
    del current_path[-1]


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) + ": " + str(find_paths(root, sum)))


main()
