"""
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
The array originally contained all the numbers from 1 to ‘n’, but due to a data error, 
one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.

Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.

Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
"""
import pytest
from typing import List


# Time complexity is O(n)
# Space complexity is O(1)
def find_corrupt_numbers(nums: List[int]) -> List[int]:
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if i + 1 != nums[i]:
            return [nums[i], i + 1]
    return [-1, -1]


find_corrupt_numbers([3, 1, 2, 5, 2])

test_data = [
    ([3, 1, 2, 5, 2], [2, 4]),
    ([3, 1, 2, 3, 6, 4], [3, 5]),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_find_corrupt_numbers(
    arr: List[int], expected: List[int],
):
    # for item in expected:
    assert find_corrupt_numbers(arr) == expected
