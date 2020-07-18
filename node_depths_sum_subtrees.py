"""Function that takes Binary tree and returns the sum of its subtrees node's depth's."""

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    


def allKindsOfNodeDepths(root):
    sum_of_all_depths = 0
    stack = [root]

    while len(stack) > 0:
        node = stack.pop()
        if node is None:
            continue
        sum_of_all_depths += node_depths(node)
        stack.append(node.left)
        stack.append(node.right)
    return sum_of_all_depths

def node_depths(node: BinaryTree, depth: int=0):
    if node is None:
        return 0
    return depth + node_depths(node.left, depth+1) + node_depths(node.right, depth+1)
