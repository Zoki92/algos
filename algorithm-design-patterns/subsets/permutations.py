"""
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

    {1, 2, 3}
    {1, 3, 2}
    {2, 1, 3}
    {2, 3, 1}
    {3, 1, 2}
    {3, 2, 1}

If a set has ‘n’ distinct elements it will have n! permutations.
"""
import pytest
from typing import List
from collections import deque

# We know that there are a total of N! permutations of a set with ‘N’ numbers.
# In the algorithm above, we are iterating through all of these permutations with
# the help of the two ‘for’ loops. In each iteration, we go through all the current
# permutations to insert a new number in them on line 17 (line 23 for C++ solution).
# To insert a number into a permutation of size ‘N’ will take O(N)
# which makes the overall time complexity of our algorithm O(N∗N!)
# All the additional space used by our algorithm is for the result list and
#  the queue to store the intermediate permutations. If you see closely,
# at any time, we don’t have more than N! permutations between the result list and the queue.
#  Therefore the overall space complexity to store N! permutations each containing
# N elements will be O(N∗N!).
def find_permutations(nums: List[int]) -> List[int]:
    nums_length = len(nums)
    result = []
    permutations = deque()
    permutations.append([])
    for current_num in nums:
        n = len(permutations)
        for _ in range(n):
            old_permutation = permutations.popleft()
            for j in range(len(old_permutation) + 1):
                new_permutation = list(old_permutation)
                new_permutation.insert(j, current_num)
                if len(new_permutation) == nums_length:
                    result.append(new_permutation)
                else:
                    permutations.append(new_permutation)
    print(result)
    return result


test_data = [
    ([1, 3, 5], [[1, 3, 5], [1, 5, 3], [3, 1, 5], [3, 5, 1], [5, 1, 3], [5, 3, 1]],)
]


@pytest.mark.parametrize("nums, expected", test_data)
def test_find_permutations(nums, expected):
    assert find_permutations(nums).sort() == expected.sort()
