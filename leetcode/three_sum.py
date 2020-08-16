"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""
import pytest
from typing import List


# Time complexity is O(N^2), space is O(1) ignoring the resulting array
def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    triplets = []
    # [-4, -1, -1, 0, 1, 2]
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        search_pair(nums, -nums[i], i + 1, triplets)
    return triplets


# So X + Y + Z == 0 , by default Y + Z == -X hence we send negative


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        elif target_sum > current_sum:
            left += 1
        else:
            right -= 1


test_data = [
    ([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]]),
]


@pytest.mark.parametrize("nums, expected", test_data)
def test_three_sum(nums, expected):
    assert three_sum(nums).sort() == expected.sort()
