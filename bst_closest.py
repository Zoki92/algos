class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # O(logN) average, O(N) worst case, space O(1)


def findClosestValueInBst(tree, target):
    currentTree = tree
    closest = target			# O(1) space
    closest_helper = float('inf')  # O(1) space
    while currentTree is not None:
        if abs(currentTree.value - target) < closest_helper:
            closest = currentTree.value
            closest_helper = abs(currentTree.value - target)
        if currentTree.value > target:
            currentTree = currentTree.left
        elif currentTree.value <= target:
            currentTree = currentTree.right
    return closest


root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)

root.right.left.right = BST(14)
root.right.right = BST(22)
expected = 13


print(findClosestValueInBst(root, 12))

print(f"Expected: {expected == findClosestValueInBst(root, 12)}")
