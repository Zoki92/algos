"""
Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’?

Input: 2
Output: List containing root nodes of all structurally unique BSTs.
Explanation: Here are the 2 structurally unique BSTs storing all numbers from 1 to 2:
1 -> 2
2 -> 1

Input: 3
Output: List containing root nodes of all structurally unique BSTs.
Explanation: Here are the 5 structurally unique BSTs storing all numbers from 1 to 3:

    1          1             2          3           3
     \          \           / \        /           /
      2          3         1   3      1           2
       \        /                      \         /
        3      2                        2       1

"""
import pytest


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.val}"


def find_unique_trees(n: int) -> int:
    result = []
    if n <= 0:
        return []
    return find_unique_trees_rec(1, n)


# Since we can have 2^N​​ permutations at the most and while processing each
# permutation we convert it into a character array, the overall time complexity of the algorithm will be O(N∗2^N).
# All the additional space used by our algorithm is for the output list. Since we can have a total of
# 2^N​​ permutations, the space complexity of our algorithm is O(2^N).
def find_unique_trees_rec(start, end):
    result = []
    # Base condition return None for an empty sub tree
    # consider n = 1, in this case will have start=end=1, this means that we should only have 1 tree
    # we will have two recursive calls, find_unique_trees_recursive(1, 0) & (2, 1)
    # both of these should return None for the left and the right child
    if start > end:
        result.append(None)
        return result

    for i in range(start, end + 1):
        # making i the root of the tree
        left_subtrees = find_unique_trees_rec(start, i - 1)
        right_subtrees = find_unique_trees_rec(i + 1, end)

        for left_tree in left_subtrees:
            for right_tree in right_subtrees:
                root = TreeNode(i)
                root.left = left_tree
                root.right = right_tree
                result.append(root)
    return result


find_unique_trees(2)

# start = 1
# i = 0
# 2 , 1

test_data = [(3, 5), (2, 2)]


@pytest.mark.parametrize("input, expected", test_data)
def test_find_unique_trees(input, expected):
    assert len(find_unique_trees(input)) == expected
