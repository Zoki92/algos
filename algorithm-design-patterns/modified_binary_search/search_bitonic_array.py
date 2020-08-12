"""
Given a Bitonic array, find if a given ‘key’ is present in it. An array is considered bitonic if it
 is monotonically increasing and then monotonically decreasing. Monotonically increasing or 
 decreasing means that for any index i in the array arr[i] != arr[i+1].

Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

Example 1:

Input: [1, 3, 8, 4, 3], key=4
Output: 3

Example 2:

Input: [3, 8, 3, 1], key=8
Output: 1

Example 3:

Input: [1, 3, 8, 12], key=12
Output: 3

Example 4:

Input: [10, 9, 8], key=10
Output: 0
"""
from typing import List
import pytest


# Since we are reducing the search range by half at every step, this means that the time complexity
# of our algorithm will be O(logN) where ‘N’ is the total elements in the given array.
# The algorithm runs in constant space O(1).
def search_bitonic_array(arr: List[int], key: int) -> int:
    start, end = 0, len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    first_half_index = binary_search(0, end, arr, key)
    if first_half_index != -1:
        return first_half_index
    return binary_search(end + 1, len(arr) - 1, arr, key)


def binary_search(start, end, arr, key):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1


search_bitonic_array([1, 3, 8, 4, 3], 4)

test_data = [
    ([1, 3, 8, 4, 3], 4, 3),
    ([3, 8, 3, 1], 8, 1),
    ([1, 3, 8, 12], 12, 3),
    ([10, 9, 8], 10, 0),
]


@pytest.mark.parametrize("arr, key, expected", test_data)
def test_search_bitonic_array(arr, key, expected):
    assert search_bitonic_array(arr, key) == expected
