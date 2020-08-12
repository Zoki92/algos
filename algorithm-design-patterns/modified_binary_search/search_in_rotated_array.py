"""
Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, 
find if a given ‘key’ is present in it.

Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1.
 You can assume that the given array does not have any duplicates.

Example 1:

Input: [10, 15, 1, 3, 8], key = 15
Output: 1
Explanation: '15' is present in the array at index '1'.

Example 2:

Input: [4, 5, 7, 9, 10, -1, 2], key = 10
Output: 4
Explanation: '10' is present in the array at index '4'.
"""
import pytest
from typing import List


# Since we are reducing the search range by half at every step, this means that the time complexity
# of our algorithm will be O(logN) where ‘N’ is the total elements in the given array.
# The algorithm runs in constant space O(1).
def search_rotated_array(arr: List[int], key: int) -> int:
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid

        if arr[start] <= arr[mid]:
            if key >= arr[start] and key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key > arr[mid] and key < arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


test_data = [([10, 15, 1, 3, 8], 15, 1), ([4, 5, 7, 9, 10, -1, 2], 10, 4)]


@pytest.mark.parametrize("arr, key, expected", test_data)
def test_search_rotated_array(arr, key, expected):
    assert search_rotated_array(arr, key) == expected
