"""
Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference with the given ‘key’.

Example 1:

Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array 

Example 2:

Input: [4, 6, 10], key = 4
Output: 4

Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: 10

Example 4:

Input: [4, 6, 10], key = 17
Output: 10
"""
import pytest
from typing import List


def search_min_diff_element_2(arr: List[int], key: int) -> int:
    if arr[-1] < key:
        return arr[-1]
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return arr[end]


# Since we are reducing the search range by half at every step, this means that the time complexity
# of our algorithm will be O(logN) where ‘N’ is the total elements in the given array.
# The algorithm runs in constant space O(1).
def search_min_diff_element(arr: List[int], key: int) -> int:
    if key < arr[0]:
        return arr[0]
    if key > arr[-1]:
        return arr[-1]
    n = len(arr)
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > key:
            end = mid - 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            return arr[mid]
    # at the end of the while loop start == end + 1 we
    # are not able to find the element in the given array
    # return the element which is closest to the key
    if (arr[start] - key) < (key - arr[end]):
        return arr[start]
    return arr[end]


test_data = [
    ([4, 6, 10], 7, 6),
    ([4, 6, 10], 4, 4),
    ([1, 3, 8, 10, 15], 12, 10),
    ([4, 6, 10], 17, 10),
]


@pytest.mark.parametrize("arr, key, expected", test_data)
def test_search_min_diff_element(arr, key, expected):
    assert search_min_diff_element(arr, key) == expected
