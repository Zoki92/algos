"""
Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. 
The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.

Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

Input: [4, 6, 10], key = 6
Output: 1
Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.

Input: [1, 3, 8, 10, 15], key = 12
Output: 4
Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.

Input: [4, 6, 10], key = 17
Output: -1
Explanation: There is no number greater than or equal to '17' in the given array.

Input: [4, 6, 10], key = -1
Output: 0
Explanation: The smallest number greater than or equal to '-1' is '4' having index '0'.

"""
import pytest
from typing import List
import math

# Since we are reducing the search range by half at every step, this means that the time complexity
# of our algorithm will be O(logN) where ‘N’ is the total elements in the given array.
# The algorithm runs in constant space O(1).
def search_ceiling_of_a_number(arr, key):
    if key > arr[-1]:
        return -1
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return left


test_data = [
    ([4, 6, 10], 6, 1),
    ([1, 3, 8, 10, 15], 12, 4),
    ([4, 6, 10], 17, -1),
    ([4, 6, 10], -1, 0),
]


@pytest.mark.parametrize("arr, key, expected", test_data)
def test_search_ceiling_of_a_number(arr: List[int], key: int, expected: int):
    assert search_ceiling_of_a_number(arr, key) == expected
