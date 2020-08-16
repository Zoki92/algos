"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has
the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""

import pytest
from typing import List
import math


def max_sub_array(nums: List[int]) -> int:
    global_max = -math.inf
    local_max = 0

    for num in nums:
        local_max = max(num, local_max + num)
        if local_max > global_max:
            global_max = local_max
    return global_max


test_data = [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
]


@pytest.mark.parametrize("nums, expected", test_data)
def test_max_sub_array(nums, expected):
    assert max_sub_array(nums) == expected
