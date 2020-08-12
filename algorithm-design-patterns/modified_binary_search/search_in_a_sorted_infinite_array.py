"""
Given an infinite sorted array (or an array with unknown size), find if a given number ‘key’ is present in the array.
Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Since it is not possible to define an array with infinite (unknown) size, you will be provided with an interface ArrayReader
to read elements of the array. ArrayReader.get(index) will return the number at index; if the array’s size is smaller than the index, 
it will return Integer.MAX_VALUE.

Example 1:

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 16
Output: 6
Explanation: The key is present at index '6' in the array.

Example 2:

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 11
Output: -1
Explanation: The key is not present in the array.

Example 3:

Input: [1, 3, 8, 10, 15], key = 15
Output: 4
Explanation: The key is present at index '4' in the array.

Example 4:

Input: [1, 3, 8, 10, 15], key = 200
Output: -1
Explanation: The key is not present in the array.
"""


import pytest
from typing import List
import math


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


# We are increasing the bounds size exponentially therefore this step will take O(logn) time
# The overall complexity is O(logn) + O(logn) which is O(logn)
# Space complexity is O(1)
def search_in_infinite_array(reader, key):
    start, end = 0, 1
    while reader.get(end) < key:
        new_start = end + 1
        # increase to double the bounds size
        end += (end - start + 1) * 2
        start = new_start

    return binary_search(start, end, reader, key)


# The binary search takes O(logn) time
def binary_search(start, end, reader, key):
    while start <= end:
        mid = (start + end) // 2
        if reader.get(mid) == key:
            return mid
        elif reader.get(mid) > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1


test_data = [
    (ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]), 16, 6),
    (ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]), 11, -1),
    (ArrayReader([1, 3, 8, 10, 15]), 15, 4),
    (ArrayReader([1, 3, 8, 10, 15]), 200, -1),
]


@pytest.mark.parametrize("reader, key, expected", test_data)
def test_search_in_infinite_array(reader, key, expected):
    assert search_in_infinite_array(reader, key) == expected
