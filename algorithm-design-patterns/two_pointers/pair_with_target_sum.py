"""Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6


Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

"""
import pytest
from typing import List


# Space complexity will be O(1)
# Time complexity will be O(N) at worst, where N is the number of items in the list arr
def pair_with_targetsum(arr: List[int], target_sum: int) -> List[int]:
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] == target_sum:
            return [left, right]
        elif arr[left] + arr[right] < target_sum:
            left += 1
        else:
            right -= 1
    return [-1, -1]


test_data = [
    ([1, 2, 3, 4, 6], 6, [1, 3]),
    ([2, 5, 9, 11], 11, [0, 2]),
]


@pytest.mark.parametrize("arr, target, expected", test_data)
def test_pair_with_targetsum(
    arr: List[int], target: int, expected: List[int],
):
    # for item in expected:
    assert pair_with_targetsum(arr, target) == expected
