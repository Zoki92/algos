"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
import pytest
from typing import List


def max_product(nums: List[int]) -> int:
    local_max = local_min = global_max = nums[0]
    for i in range(1, len(nums)):
        temp = local_max
        local_max = max(nums[i], nums[i] * local_max, nums[i] * local_min)
        local_min = min(nums[i], nums[i] * local_min, nums[i] * temp)

        global_max = max(global_max, local_max)
    return global_max


test_data = [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
]

"""local_max = 2
local_min = 2
global_max = 2

temp = local_max = 2
local_max = max(3, 6, 6) = 6
local_min  = min(3, 6, 6) = 3
global_max = max(2, 6) = 6

temp = local_max = 6
local_max = max(-2, -12, -6) = -2
local_min = min(-2, -6, -12) = -12
global_max = max(6, -2) = 6"""


@pytest.mark.parametrize("nums, expected", test_data)
def test_max_product(nums, expected):
    assert max_product(nums) == expected
