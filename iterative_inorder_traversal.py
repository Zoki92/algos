class BinaryTree:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

def iterativeInOrderTraversal(tree, callback):
    previous_node = None
    current_node = tree

    while current_node:
        if previous_node is None or previous_node == current_node.parent:
            if current_node.left:
                next_node = current_node.left
            else:
                callback(current_node)
                next_node = current_node.right if current_node.right else current_node.parent
        elif previous_node == current_node.left:
            callback(current_node)
            next_node = current_node.right if current_node.right else current_node.parent
        else:
            next_node = current_node.parent
        previous_node = current_node
        current_node = next_node

root = BinaryTree(1)
root.left = BinaryTree(2, parent=root)
root.left.left = BinaryTree(4, parent=root.left)
root.left.left.right = BinaryTree(9, parent=root.left.left)
root.right = BinaryTree(3, parent=root)
root.right.left = BinaryTree(6, parent=root.right)
root.right.right = BinaryTree(7, parent=root.right)

def testCallback(testArray, tree):
    if tree is None:
        return
    testArray.append(tree.value)

test_array = []
actualTestCallback = lambda x: testCallback(test_array, x)
iterativeInOrderTraversal(root, actualTestCallback)
print(test_array)