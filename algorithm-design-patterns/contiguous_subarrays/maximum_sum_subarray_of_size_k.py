"""Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
"""

import pytest
from typing import List


# Time complexity O(n) where n is the amount of numbers in the array
# The algorithm runs in constant space O(1)
def max_sub_array_of_size_k(input_array: List[int], k: int) -> int:
    max_sum = 0
    current_sum = 0
    window_start = 0
    for i in range(len(input_array)):
        current_sum += input_array[i]
        if i >= k - 1:
            max_sum = max(current_sum, max_sum)
            current_sum -= input_array[window_start]
            window_start += 1
    return max_sum


test_data = [([2, 1, 5, 1, 3, 2], 3, 9), ([2, 3, 4, 1, 5], 2, 7)]


@pytest.mark.parametrize("input_array, k, expected", test_data)
def test_find_averages_of_subarrays(
    input_array: List[int], k: int, expected: int,
):
    # for item in expected:
    assert max_sub_array_of_size_k(input_array, k) == expected
