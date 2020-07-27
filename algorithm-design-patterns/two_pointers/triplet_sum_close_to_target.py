"""
Given an array of unsorted numbers and a target number, find a triplet in the array 
whose sum is as close to the target number as possible, return the sum of the triplet. 
If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
"""
import pytest
from typing import List
import math


"""
We can follow a similar approach to iterate through the array, taking one number at a time. 
At every step, we will save the difference between the triplet and the target number, 
so that in the end, we can return the triplet with the closest sum.
"""


# Time complexity is O(n^2) and space complexity is O(n)
def triplet_sum_close_to_target(arr: List[int], target_sum: int) -> int:
    arr.sort()
    smallest_difference = math.inf
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            target_diff = target_sum - arr[i] - arr[left] - arr[right]
            if target_diff == 0:
                return target_sum - target_diff
            # handle smallest sum when we have more than one solution
            if abs(target_diff) < abs(smallest_difference) or (
                abs(target_diff) == abs(smallest_difference)
                and target_diff > smallest_difference
            ):
                smallest_difference = target_diff

            if target_diff > 0:
                left += 1
            else:
                right -= 1
    return target_sum - smallest_difference


test_data = [
    ([-2, 0, 1, 2], 2, 1),
    ([-3, -1, 1, 2], 1, 0),
    ([1, 0, 1, 1], 100, 3),
]


@pytest.mark.parametrize("arr, target, expected", test_data)
def test_triplet_sum_close_to_target(
    arr: List[int], target: int, expected: List[int],
):
    # for item in expected:
    assert triplet_sum_close_to_target(arr, target) == expected
