"""
We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’
based on their creation sequence. This means that the object with sequence number ‘3’ was created just before the 
object with sequence number ‘4’.

Write a function to sort the objects in-place on their creation sequence number in O(n) and without any extra space.
For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]

Input: [2, 6, 4, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6]

Input: [1, 5, 6, 4, 3, 2]
Output: [1, 2, 3, 4, 5, 6]
"""

import pytest
from typing import List

# The time complexity of this algorithm is O(n), or more correct O(n) + O(n - 1).
# Space complexity is O(1)
def cyclic_sort(nums: List[int]) -> List[int]:
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1
        if correct_idx != i:
            swap(i, correct_idx, nums)
        else:
            i += 1
    return nums


def swap(current, correct, nums):
    nums[current], nums[correct] = nums[correct], nums[current]


test_data = [
    ([3, 1, 5, 4, 2], [1, 2, 3, 4, 5]),
    ([2, 6, 4, 3, 1, 5], [1, 2, 3, 4, 5, 6]),
    ([1, 5, 6, 4, 3, 2], [1, 2, 3, 4, 5, 6]),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_cyclic_sort(
    arr: List[int], expected: List[int],
):
    # for item in expected:
    assert cyclic_sort(arr) == expected
