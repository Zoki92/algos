"""Given an unsorted array containing numbers, find the smallest missing positive number in it.

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'

Input: [3, -2, 0, 1, 2]
Output: 4

Input: [3, 2, 5, 1]
Output: 4
"""
import pytest
from typing import List

# Time complexity O(n)
# Space complexity O(1)
def find_first_missing_positive(nums):
    i = 0
    n = len(nums)
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if i + 1 != nums[i]:
            return i + 1
    return -1


test_data = [
    ([-3, 1, 5, 4, 2], 3),
    ([3, -2, 0, 1, 2], 4),
    ([3, 2, 5, 1], 4),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_find_first_missing_positive(
    arr: List[int], expected: int,
):
    # for item in expected:
    assert find_first_missing_positive(arr) == expected
