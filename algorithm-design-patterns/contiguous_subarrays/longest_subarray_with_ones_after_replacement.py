"""Given an array containing 0s and 1s if you are allowed to replace no more than k 0s with 1s, find the
length of the longest contiguous subarray having all 1s

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""
import pytest
from typing import List


# Time complexity is O(N) where N is the length of the arr
# Space complexity is O(1)
def length_of_longest_substring(arr: List[int], k: int) -> int:
    longest, window_start = 0, 0
    frequency_of_zeros = 0

    for window_end in range(len(arr)):
        right_number = arr[window_end]
        if right_number == 0:
            frequency_of_zeros += 1

        if frequency_of_zeros > k:
            left = arr[window_start]
            if left == 0:
                frequency_of_zeros -= 1
            window_start += 1
        longest = max(longest, window_end - window_start + 1)
    return longest


test_data = [
    ([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2, 6),
    ([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3, 9),
]


@pytest.mark.parametrize("arr, k, expected", test_data)
def test_length_of_longest_substring(
    arr: List[int], k: int, expected: int,
):
    # for item in expected:
    assert length_of_longest_substring(arr, k) == expected
