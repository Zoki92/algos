"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and 
it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true

Example 2:

Input: [1,2,3,4]
Output: false

Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
import pytest
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    nums_frequency = {}
    for num in nums:
        if num in nums_frequency:
            return True
        else:
            nums_frequency[num] = nums_frequency.get(num, 0) + 1
    return False


test_data = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
]


@pytest.mark.parametrize("nums, expected", test_data)
def test_contains_duplicate(nums, expected):
    assert contains_duplicate(nums) == expected

