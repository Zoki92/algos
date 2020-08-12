"""
Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically 
increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any
index i in the array arr[i] != arr[i+1].

Example 1:

Input: [1, 3, 8, 12, 4, 2]
Output: 12
Explanation: The maximum number in the input bitonic array is '12'.

Example 2:

Input: [3, 8, 3, 1]
Output: 8

Example 3:

Input: [1, 3, 8, 12]
Output: 12

Example 4:

Input: [10, 9, 8]
Output: 10
"""

import pytest
from typing import List

# Since we are reducing the search range by half at every step, this means that the time complexity
# of our algorithm will be O(logN) where ‘N’ is the total elements in the given array.
# The algorithm runs in constant space O(1).
def find_max_in_bitonic_array(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    # at the end of the while loop start == end
    return arr[start]


test_data = [
    ([1, 3, 8, 12, 4, 2], 12),
    ([3, 8, 3, 1], 8),
    ([1, 3, 8, 12], 12),
    ([10, 9, 8], 10),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_find_max_in_bitonic_array(arr, expected):
    assert find_max_in_bitonic_array(arr) == expected
