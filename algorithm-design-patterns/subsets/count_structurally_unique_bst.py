"""
Given a number ‘n’, write a function to return the count of structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’.

Input: 2
Output: 2
Explanation: As we saw in the previous problem, there are 2 unique BSTs storing numbers from 1-2.

Input: 3
Output: 5
Explanation: There will be 5 unique BSTs that can store numbers from 1 to 5.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Since we can have 2^N​​ permutations at the most and while processing each
# permutation we convert it into a character array, the overall time complexity of the algorithm will be O(N∗2^N).
# All the additional space used by our algorithm is for the output list. Since we can have a total of
# 2^N​​ permutations, the space complexity of our algorithm is O(2^N).
def count_trees(n):
    if n <= 1:
        return 1
    count = 0
    for i in range(1, n + 1):
        # making 'i' root of the tree
        countOfLeftSubtrees = count_trees(i - 1)
        countOfRightSubtrees = count_trees(n - i)
        count += countOfLeftSubtrees * countOfRightSubtrees

    return count


def main():
    print("Total trees: " + str(count_trees(2)))
    print("Total trees: " + str(count_trees(3)))


main()


def count_trees_memoized(n):
    return count_trees_rec({}, n)


def count_trees_rec(map, n):
    if n in map:
        return map[n]

    if n <= 1:
        return 1
    count = 0
    for i in range(1, n + 1):
        # making 'i' the root of the tree
        countOfLeftSubtrees = count_trees_rec(map, i - 1)
        countOfRightSubtrees = count_trees_rec(map, n - i)
        count += countOfLeftSubtrees * countOfRightSubtrees

    map[n] = count
    return count


def main_memo():
    print("Total trees: " + str(count_trees(2)))
    print("Total trees: " + str(count_trees(3)))


main_memo()
