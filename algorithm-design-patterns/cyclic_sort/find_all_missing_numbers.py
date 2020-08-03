"""We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, 
which means some numbers will be missing. Find all those missing numbers.

Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

Input: [2, 4, 1, 2]
Output: 3

Input: [2, 3, 2, 1]
Output: 4
"""
import pytest
from typing import List


# Time complexity is O(n)
# Space complexity is O(1) ingoring the space needed for missing numbers array
def find_missing_numbers(nums: List[int]) -> List[int]:
    missingNumbers = []
    i, n = 0, len(nums)
    while i < n:
        idx = nums[i] - 1
        if nums[i] != nums[idx]:
            nums[i], nums[idx] = nums[idx], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if i + 1 != nums[i]:
            missingNumbers.append(i + 1)
    return missingNumbers


find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1])

test_data = [
    ([2, 3, 1, 8, 2, 3, 5, 1], [4, 6, 7]),
    ([2, 4, 1, 2], [3]),
    ([2, 3, 2, 1], [4]),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_find_missing_numbers(
    arr: List[int], expected: List[int],
):
    # for item in expected:
    assert find_missing_numbers(arr) == expected
