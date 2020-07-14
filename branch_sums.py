"""
Write a function that takes ina  Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum.
"""

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self
    
    def __str__(self):
        return f"{self.value} - {self.left} - {self.right}"

# O(n) time | O(n) space, we go through every node in the tree
# and we also put recursive calls in the memory, and we call it n times as well.
def branch_sums(root):
    current = root
    branches_sum = []
    current_sum = 0
    calculate_branches_sum(current, branches_sum, current_sum)
    return branches_sum

def calculate_branches_sum(current, branches_sum, current_sum):
    if current is None:
        return

    current_sum += current.value
    if current.left is None and current.right is None:
        branches_sum.append(current_sum)

    calculate_branches_sum(current.left, branches_sum, current_sum)
    calculate_branches_sum(current.right, branches_sum, current_sum)
        
def calculate_sum_depths(root, depth=0):
    if root is None:
        return 0
    return depth + calculate_sum_depths(root.left, depth + 1) + calculate_sum_depths(root.right, depth + 1)
    


tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])

# print(branch_sums(tree))
print(calculate_sum_depths(tree))

def invertBinaryTree(tree):
    if tree is None:
        return
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)