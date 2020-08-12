"""
In a non-empty array of integers, every number appears twice except for one, find that single number.

Example 1:

Input: 1, 4, 2, 1, 3, 2, 3
Output: 4

Example 2:

Input: 7, 9, 7
Output: 9
"""
import pytest
from typing import List

# Time Complexity: Time complexity of this solution is O(n) as we iterate through all numbers of the input once.
# Space Complexity: The algorithm runs in constant space O(1).
def find_single_number(arr: List[int]) -> int:
    x1 = 0
    for num in arr:
        x1 ^= num
    return x1


test_data = [
    ([1, 4, 2, 1, 3, 2, 3], 4),
    ([7, 9, 7], 9),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_find_single_number(arr, expected):
    assert find_single_number(arr) == expected
