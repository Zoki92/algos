"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

import pytest
from typing import List


# Time complexity is O(N), space complexity is O(1)
def max_area(height: List[int]) -> int:
    max_area = 0
    left, right = 0, len(height) - 1

    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_area


test_data = [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)]


@pytest.mark.parametrize("height, expected", test_data)
def test_max_area(height, expected):
    assert max_area(height) == expected
