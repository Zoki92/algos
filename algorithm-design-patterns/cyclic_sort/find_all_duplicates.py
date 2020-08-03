"""
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
The array has some duplicates, find all the duplicate numbers without using any extra space.

Input: [3, 4, 4, 5, 5]
Output: [4, 5]

Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]
"""
import pytest
from typing import List

# Space complexity is O(1) and Time complexity O(N)
def find_all_duplicates(nums):
    duplicateNumbers = []
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicateNumbers.append(nums[i])

    return duplicateNumbers


test_data = [
    ([3, 4, 4, 5, 5], [5, 4]),
    ([5, 4, 7, 2, 3, 5, 3], [3, 5]),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_find_all_duplicates(
    arr: List[int], expected: List[int],
):
    # for item in expected:
    assert find_all_duplicates(arr) == expected
