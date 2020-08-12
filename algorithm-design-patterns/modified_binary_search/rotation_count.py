"""
Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.

You can assume that the array does not have any duplicates.

Input: [10, 15, 1, 3, 8]
Output: 2
Explanation: The array has been rotated 2 times.

Input: [4, 5, 7, 9, 10, -1, 2]
Output: 5
Explanation: The array has been rotated 5 times.

Input: [1, 3, 8, 10]
Output: 0
Explanation: The array has been not been rotated.
"""
import pytest
from typing import List


# Since we are reducing the search range by half at every step, this means that the time complexity
# of our algorithm will be O(logN) where ‘N’ is the total elements in the given array.
# The algorithm runs in constant space O(1).
def count_rotations(arr: List[int]) -> int:
    start, end = 0, len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1

        if mid > start and arr[mid - 1] > arr[mid]:
            return mid

        if arr[start] < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return 0


test_data = [
    ([10, 15, 1, 3, 8], 2),
    ([4, 5, 7, 9, 10, -1, 2], 5),
    ([1, 3, 8, 10], 0),
]


@pytest.mark.parametrize("arr, expected", test_data)
def test_count_rotations(arr, expected):
    assert count_rotations(arr) == expected
